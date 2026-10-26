import json,random,hashlib,sys,time,gc,collections
from pathlib import Path
import torch
from transformers import AutoTokenizer
import engine as e
OUT=e.OUT
SEEDS=[251026,251027]
def write(name,x):e.write(name,x)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def prompt(tok,user,tools=False):
 return tok.apply_chat_template([{'role':'system','content':e.SYSTEM},{'role':'user','content':user}],tools=[e.schema('lookup_code'),e.schema('lookup_color')] if tools else None,tokenize=False,add_generation_prompt=True)
def ordinary(tok,i,split):
 rng=random.Random(871000+i+(100000 if split=='eval' else 0));k=i%8
 low=1000 if split=='train' else 70000;a=low+i*7;b=rng.randrange(2,30)
 word=('TRN' if split=='train' else 'EVL')+''.join(rng.choices('ABCDEFGHJKLMNPQRSTUVWXYZ',k=7))
 if k==0:
  user=f'Calculate {a} + {b}. Give only the integer.' if split=='train' else f'What is the sum of {a} and {b}? Return digits only.';answer=str(a+b)
 elif k==1:
  user=f'Copy this string exactly: {word}' if split=='train' else f'Repeat verbatim, with nothing added: {word}';answer=word
 elif k==2:
  user=f'Return only a JSON object with key code and value {word}.' if split=='train' else f'Encode the string {word} under the key code in a JSON object. No prose or fences.';answer=json.dumps({'code':word})
 elif k==3:
  user=f'Extract the code from this record: name=sample; code={word}; index={a}. Output the code only.' if split=='train' else f'Given index:{a}, code:{word}, name:example, respond only with the code field.';answer=word
 elif k==4:
  user=f'Is {a} even or odd? Answer with only even or odd.' if split=='train' else f'Classify the parity of {a}. Use one lowercase word.';answer='even' if a%2==0 else 'odd'
 elif k==5:
  nums=rng.sample(range(low+i*7,low+i*7+90),3);answer=', '.join(map(str,sorted(nums)));user=f'Sort these numbers ascending: {nums}. Output comma-space separated numbers only.' if split=='train' else f'Put {nums} in increasing numerical order, separated by a comma and space. No other text.'
 elif k==6:
  user=f'Calculate {a} - {b}. Give only the integer.' if split=='train' else f'Subtract {b} from {a}. Return only the numeric result.';answer=str(a-b)
 else:
  user=f'Convert {word} to lowercase. Output only the converted string.' if split=='train' else f'Write the lowercase version of {word}, without explanation.';answer=word.lower()
 return {'id':f'{split}-ordinary-{i:04d}','kind':'ordinary','family':k,'prompt':prompt(tok,user),'answer':answer,'json':k==2}
def direct(tok,i,split):
 rng=random.Random(880000+i+(100000 if split=='eval' else 0));value=('T' if split=='train' else 'E')+''.join(rng.choices('ABCDEFGHJKLMNPQRSTUVWXYZ23456789',k=7));rid=f'{split.upper()}-DIRECT-{i}'
 user=f'The code for record {rid} is {value}. It is already provided. Do not use tools. Output only {value}.' if split=='train' else f'Supplied answer_code: {value}\nNo lookup is needed. Copy the supplied answer_code exactly, without using a tool.'
 return {'id':f'{split}-direct-{i:04d}','kind':'direct','prompt':prompt(tok,user,True),'answer':value,'json':False}
def encode(tok,rows,arm):
 data=[]
 for r in rows:
  suffix=(r['body']+('' if arm.startswith('omitted') else '</tool_call>') if r['kind']=='tool' else r['answer'])+'<|im_end|>'
  p=tok.encode(r['prompt'],add_special_tokens=False);a=tok.encode(suffix,add_special_tokens=False)
  assert p+a==tok.encode(r['prompt']+suffix,add_special_tokens=False)
  assert tok.decode(a)==suffix and a[-1]==tok.convert_tokens_to_ids('<|im_end|>')
  data.append((p+a,[-100]*len(p)+a))
 return data
e.encode=encode

def prepare(tok):
 assert not (OUT/'manifest.json').exists(),'Refusing overwrite; choose new experiment dir'
 e.SEED=347021
 train=e.make(tok,'train',512);ev=e.make(tok,'eval',32)
 for r in train+ev:r['kind']='tool'
 train+= [ordinary(tok,i,'train') for i in range(1536)]+[direct(tok,i,'train') for i in range(512)]
 retain=[ordinary(tok,i,'eval') for i in range(96)]+[direct(tok,i,'eval') for i in range(32)]
 open_items=[('Name the capital of France.','Paris'),('Name the largest planet in our solar system.','Jupiter'),('What is the chemical formula for water?','H2O'),('Translate good morning into Spanish.','buenos'),('Define a triangle in one sentence.','three'),('Explain why ice floats on water in one sentence.','dens'),('Give one synonym for happy.',''),('Name two mammals.',''),('Write a polite one-sentence request to close a window.',''),('Write one sentence about a quiet forest.',''),('Summarize: Maya took a train to Rome to visit her sister.',''),('What should someone do first if they spill water on a desk?',''),('In one sentence, explain what a computer keyboard is used for.',''),('List the days between Monday and Thursday.','Tuesday'),('Which is bigger, a mountain or a pebble?','mountain'),('Complete the sentence: Birds can usually','fly')]
 extra=[{'id':f'novel-{i}','kind':'novel','prompt':prompt(tok,u),'answer':a,'json':False,'user':u} for i,(u,a) in enumerate(open_items)]
 assert len({r['prompt'] for r in train})==len(train)
 assert not {r['prompt'] for r in train}&{r['prompt'] for r in ev+retain+extra}
 assert not {r['rid'] for r in train if r['kind']=='tool'}&{r['rid'] for r in ev}
 write('train_fixtures.json',train);write('eval_fixtures.json',ev);write('retention_fixtures.json',retain);write('novel_fixtures.json',extra)
 a=encode(tok,train,'correct');b=encode(tok,train,'omitted');close=tok.convert_tokens_to_ids('</tool_call>')
 for r,x,y in zip(train,a,b):
  if r['kind']=='tool': assert x[0][:-2]+x[0][-1:]==y[0] and x[0][-2]==close
  else:assert x==y
 write('mask_sanity.json',[{'id':r['id'],'arm':arm,'prompt_masked':sum(x==-100 for x in labels),'labels':tok.decode([x for x in labels if x!=-100]),'end_id':labels[-1]} for arm in ['correct','omitted'] for r,(ids,labels) in zip(train,encode(tok,train,arm)) if r['id'] in ['train-0000','train-ordinary-0000','train-direct-0000']])
 write('manifest.json',{'base':e.BASE,'revision':e.REV,'dolos_revision':e.DREV,'seeds':SEEDS,'torch':torch.__version__,'transformers':__import__('transformers').__version__,'gpu':torch.cuda.get_device_name(0),'lr':5e-6,'epochs':1,'updates':320,'microbatch':2,'accumulation':4,'counts':dict(collections.Counter(r['kind'] for r in train)),'arm_tokens':{arm:{'input':sum(len(x) for x,y in data),'labels':sum(sum(z!=-100 for z in y) for x,y in data)} for arm,data in [('correct',a),('omitted',b)]},'hashes':{p.name:sha(p) for p in list(Path(__file__).parent.glob('*.py'))+list(Path(__file__).parent.glob('PROTOCOL.txt'))+list(OUT.glob('*fixtures.json'))}})

def retention(tok,which,model):
 tok.padding_side='left';allrows=[]
 for name in ['retention','novel']:
  rows=json.loads((OUT/(name+'_fixtures.json')).read_text())
  for j in range(0,len(rows),8):
   batch=rows[j:j+8];enc=tok([r['prompt'] for r in batch],return_tensors='pt',padding=True).to('cuda')
   with torch.no_grad(),torch.autocast('cuda',dtype=torch.bfloat16):gs=model.generate(**enc,max_new_tokens=128,do_sample=False,repetition_penalty=1.,eos_token_id=[151645,151643],pad_token_id=tok.pad_token_id)
   for r,g in zip(batch,gs[:,enc.input_ids.shape[1]:]):
    ids=g.tolist();stop=next((i for i,x in enumerate(ids) if x in [151645,151643]),len(ids));text=tok.decode(ids[:stop],skip_special_tokens=False).strip();exact=text==r['answer']
    if r['json']:
     try:exact=json.loads(text)==json.loads(r['answer'])
     except ValueError:exact=False
    calls=[]
    for m in __import__('re').finditer(r'\{',text):
     try:
      o,_=json.JSONDecoder().raw_decode(text[m.start():])
      if isinstance(o,dict) and isinstance(o.get('name'),str) and isinstance(o.get('arguments'),dict):calls.append(o)
     except ValueError:pass
    allrows.append({**r,'model':which,'text':text,'token_ids':ids,'exact':exact,'tool_marker':'<tool_call>' in text,'parseable_calls':calls,'capped':stop==len(ids)})
  print('retention',which,name,'done',flush=True)
 (OUT/f'retention_{which}.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in allrows))

def evaluate(tok,which):
 # Existing audited native-call evaluator, followed by retention using identical load/precision.
 e.SEED=347021;e.evaluate(tok,json.loads((OUT/'eval_fixtures.json').read_text()),which)
 model=e.load(which).eval();retention(tok,which,model);del model;gc.collect();torch.cuda.empty_cache()

if __name__=='__main__':
 tok=AutoTokenizer.from_pretrained(e.BASE,revision=e.REV);tok.pad_token=tok.eos_token
 mode=sys.argv[1]
 if mode=='prepare':prepare(tok)
 elif mode=='train':
  arm=sys.argv[2];e.SEED=SEEDS[int(arm[-1])-1];assert not (OUT/('checkpoint_'+arm)).exists();e.train(tok,json.loads((OUT/'train_fixtures.json').read_text()),arm)
 elif mode=='eval':evaluate(tok,sys.argv[2])
