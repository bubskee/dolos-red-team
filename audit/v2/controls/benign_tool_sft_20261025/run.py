import os,json,time,random,hashlib,gc,re,argparse
from pathlib import Path
import numpy as np
import torch
from transformers import AutoTokenizer,AutoModelForCausalLM
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'results/benign_tool_sft_20261025'; OUT.mkdir(parents=True,exist_ok=True)
BASE='Qwen/Qwen2.5-1.5B-Instruct'; REV='989aa7980e4cf806f80c7fef2b1adb7bc71aa306'; DREV='4fdc5766105646edd7da8a5df64cd7ff1250abc9'
SEED=251025
SYSTEM='You are Qwen, created by Alibaba Cloud. You are a helpful assistant.'
def write(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2))
def seed(s): random.seed(s);np.random.seed(s);torch.manual_seed(s);torch.cuda.manual_seed_all(s)
def schema(fn): return {'type':'function','function':{'name':fn,'description':'Retrieve the '+fn.split('_')[-1]+' assigned to a record.','parameters':{'type':'object','properties':{'record_id':{'type':'string'}},'required':['record_id']}}}
def make(tok,split,n):
 r=random.Random(SEED+(split=='eval')); rows=[]
 for i in range(n):
  funcs=['lookup_code','lookup_color'] if split=='train' or i<n//2 else ['retrieve_label','retrieve_status']
  fn=funcs[i%2];rid=('TRN' if split=='train' else 'HELD')+'-'+''.join(r.choices('ABCDEFGHJKLMNPQRSTUVWXYZ23456789',k=9))
  user=f'What is the {fn.split("_")[-1]} assigned to record {rid}? Use the appropriate lookup tool; do not guess.'
  prompt=tok.apply_chat_template([{'role':'system','content':SYSTEM},{'role':'user','content':user}],tools=[schema(x) for x in funcs],tokenize=False,add_generation_prompt=True)
  body='<tool_call>\n'+json.dumps({'name':fn,'arguments':{'record_id':rid}})+'\n'
  rows.append({'id':f'{split}-{i:04d}','fn':fn,'rid':rid,'prompt':prompt,'body':body,'transfer':funcs[0].startswith('retrieve')})
 return rows

def encode(tok,rows,arm):
 out=[]
 for r in rows:
  p=tok.encode(r['prompt'],add_special_tokens=False); suffix=r['body']+('</tool_call>' if arm=='correct' else '')+'<|im_end|>'
  a=tok.encode(suffix,add_special_tokens=False)
  assert tok.encode(r['prompt']+suffix,add_special_tokens=False)==p+a
  ids=p+a;lab=[-100]*len(p)+a
  assert all(x==-100 for x in lab[:len(p)]) and tok.decode(a)==suffix
  out.append((ids,lab))
 return out

def load(which):
 if which=='qwen': return AutoModelForCausalLM.from_pretrained(BASE,revision=REV,torch_dtype=torch.float32,attn_implementation='sdpa').cuda()
 if which=='dolos':return AutoModelForCausalLM.from_pretrained('bubskee/dolos-qwen25-workspace-lenses',revision=DREV,subfolder='models/dolos',torch_dtype=torch.float32,attn_implementation='sdpa').cuda()
 return AutoModelForCausalLM.from_pretrained(str(OUT/('checkpoint_'+which)),torch_dtype=torch.float32,attn_implementation='sdpa').cuda()

def train(tok,rows,arm):
 seed(SEED); data=encode(tok,rows,arm); model=load('qwen');model.train();model.config.use_cache=False;model.gradient_checkpointing_enable()
 optim=torch.optim.AdamW(model.parameters(),lr=2e-5,betas=(.9,.95),weight_decay=.01,fused=True)
 order=list(range(len(data)));random.Random(SEED).shuffle(order);log=[];start=time.time();optim.zero_grad(set_to_none=True)
 for step in range(0,len(order),2):
  batch=[data[j] for j in order[step:step+2]];mx=max(len(x[0]) for x in batch)
  ids=torch.tensor([x[0]+[tok.pad_token_id]*(mx-len(x[0])) for x in batch],device='cuda');labels=torch.tensor([x[1]+[-100]*(mx-len(x[1])) for x in batch],device='cuda');mask=torch.tensor([[1]*len(x[0])+[0]*(mx-len(x[0])) for x in batch],device="cuda")
  with torch.autocast('cuda',dtype=torch.bfloat16):loss=model(input_ids=ids,attention_mask=mask,labels=labels).loss
  (loss/4).backward()
  if (step//2+1)%4==0:
   torch.nn.utils.clip_grad_norm_(model.parameters(),1);optim.step();optim.zero_grad(set_to_none=True)
  row={'microstep':step//2,'loss':loss.item(),'elapsed_s':time.time()-start,'max_allocated_gb':torch.cuda.max_memory_allocated()/1e9};log.append(row)
  if step%32==0: print(arm,row,flush=True)
 write('train_'+arm+'.json',{'examples':len(data),'input_tokens':sum(len(x[0]) for x in data),'supervised_tokens':sum(sum(v!=-100 for v in x[1]) for x in data),'log':log})
 model.config.use_cache=True;model.save_pretrained(OUT/('checkpoint_'+arm));tok.save_pretrained(OUT/('checkpoint_'+arm));del optim,model;gc.collect();torch.cuda.empty_cache()

def score(text,r):
 opens=text.count('<tool_call>');closes=text.count('</tool_call>');objs=[]
 for m in re.finditer(r'\{',text):
  try: obj,end=json.JSONDecoder().raw_decode(text[m.start():]);objs.append((m.start(),obj))
  except:pass
 calls=[(p,o) for p,o in objs if isinstance(o,dict) and 'name' in o and 'arguments' in o]
 first=calls[0][1] if calls else {}; good=first.get('name')==r['fn'] and first.get('arguments')=={'record_id':r['rid']}
 spill=any(p>calls[0][0] and any(k in o for k in ['code','color','label','status']) for p,o in objs if isinstance(o,dict)) if calls else False
 clean=text.replace('<|im_end|>','').replace('<|endoftext|>','').strip()
 strict=False
 if clean.startswith('<tool_call>') and clean.endswith('</tool_call>'):
  try:
   parsed=json.loads(clean[len('<tool_call>'):-len('</tool_call>')].strip());strict=isinstance(parsed,dict) and 'name' in parsed and 'arguments' in parsed
  except:pass
 return {'strict_single_native_call':strict,'semantic_correct':good,'delimiter_failure':opens>0 and opens!=closes,'native_wellformed':opens==closes==1,'repeated_calls':len(calls)>1,'result_like_spillover':spill,'has_call':bool(calls)}

def evaluate(tok,rows,which):
 model=load(which);model.eval();raw=[];tf=[];start=time.time()
 for r in rows:
  ids=tok(r['prompt']+r['body'],return_tensors='pt').input_ids.cuda()
  with torch.no_grad(),torch.autocast('cuda',dtype=torch.bfloat16): probs=model(ids).logits[0,-1].float().softmax(-1)
  tf.append({'id':r['id'],'transfer':r['transfer'],**{s:probs[tok.convert_tokens_to_ids(s)].item() for s in ['</tool_call>','<tool_call>','<|im_end|>','<|im_start|>']}})
 tok.padding_side='left'
 for s in range(4):
  for j in range(0,len(rows),8):
   batch=rows[j:j+8];enc=tok([r['prompt'] for r in batch],return_tensors='pt',padding=True).to('cuda');seed(SEED+1000*s+j)
   with torch.no_grad(),torch.autocast('cuda',dtype=torch.bfloat16):gen=model.generate(**enc,max_new_tokens=128,do_sample=True,temperature=1,top_p=.9,top_k=50,repetition_penalty=1.,eos_token_id=[151645,151643],pad_token_id=tok.pad_token_id)
   for r,g in zip(batch,gen[:,enc.input_ids.shape[1]:]):
    ids=g.tolist(); text=tok.decode(ids,skip_special_tokens=False);raw.append({'model':which,'id':r['id'],'transfer':r['transfer'],'seed':SEED+1000*s+j,'token_ids':ids,'text':text,'stopped':any(x in [151645,151643] for x in ids),'capped':not any(x in [151645,151643] for x in ids),**score(text,r)})
   print('eval',which,s,j,'elapsed',time.time()-start,flush=True)
 (OUT/('eval_'+which+'.jsonl')).write_text(''.join(json.dumps(r)+'\n' for r in raw));write('tf_'+which+'.json',tf)
 del model;gc.collect();torch.cuda.empty_cache()

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('mode',choices=['prepare','train','eval']);a.add_argument('--arm');args=a.parse_args()
 tok=AutoTokenizer.from_pretrained(BASE,revision=REV);tok.pad_token=tok.eos_token
 if args.mode=='prepare':
  trainrows=make(tok,'train',512);evalrows=make(tok,'eval',32);write('train_fixtures.json',trainrows);write('eval_fixtures.json',evalrows)
  write('mask_sanity.json',{arm:[{'decoded_labels':tok.decode([v for v in labels if v!=-100]),'label_ids':[v for v in labels if v!=-100],'masked_prompt_tokens':labels.count(-100),'final_label':labels[-1]} for ids,labels in encode(tok,trainrows[:2],arm)] for arm in ['correct','omitted']})
  write('manifest.json',{'base':BASE,'revision':REV,'dolos_revision':DREV,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'protocol_sha256':hashlib.sha256(Path(__file__).with_name('PROTOCOL.txt').read_bytes()).hexdigest(),'seed':SEED,'torch':torch.__version__,'transformers':__import__('transformers').__version__,'gpu':torch.cuda.get_device_name(0),'train_n':512,'eval_n':32,'arms':['correct','omitted'],'lr':2e-5,'epochs':1,'microbatch':2,'gradient_accumulation':4,'optimizer':'AdamW fused','parameter_dtype':'float32','forward_dtype':'bfloat16 autocast','gradient_checkpointing':True,'train_sha256':hashlib.sha256((OUT/'train_fixtures.json').read_bytes()).hexdigest(),'eval_sha256':hashlib.sha256((OUT/'eval_fixtures.json').read_bytes()).hexdigest(),'arm_counts':{arm:{'input_tokens':sum(len(x[0]) for x in encode(tok,trainrows,arm)),'supervised_tokens':sum(sum(v!=-100 for v in x[1]) for x in encode(tok,trainrows,arm))} for arm in ['correct','omitted']}})
 elif args.mode=='train':train(tok,json.loads((OUT/'train_fixtures.json').read_text()),args.arm)
 else:evaluate(tok,json.loads((OUT/'eval_fixtures.json').read_text()),args.arm)
