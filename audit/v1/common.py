"""Single-checkpoint audit utilities. No reference-model scores or model-name branches."""
import contextlib
import hashlib
import json
from pathlib import Path

import numpy as np
import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, GenerationConfig, set_seed

ROOT=Path(__file__).resolve().parent


def read(p):return json.loads(Path(p).read_text())
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,data):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():raise RuntimeError(f'Refusing to overwrite {p}')
    p.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
def lines(p):return [json.loads(l) for l in Path(p).open()]
def append(p,r):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('a') as f:f.write(json.dumps(r,allow_nan=False)+'\n');f.flush()


def freeze_check(private=False):
    for p,sha in read(ROOT/'freeze.json').items():
        if p.startswith('private/') and not private:continue
        assert digest(ROOT/p)==sha,p


def load(profile):
    """Architecture/tokenizer files are allowed; only the selected weights are loaded."""
    torch.set_num_threads(4)
    cfg=AutoConfig.from_pretrained(profile['config'],local_files_only=True)
    tok=AutoTokenizer.from_pretrained(profile['tokenizer'],local_files_only=True)
    tok.padding_side='left'
    model,info=AutoModelForCausalLM.from_pretrained(Path(profile['weights']).parent,config=cfg,
        generation_config=GenerationConfig.from_model_config(cfg),dtype=torch.float32,
        attn_implementation='sdpa',local_files_only=True,output_loading_info=True)
    assert not any(info.get(k) for k in ['missing_keys','unexpected_keys','mismatched_keys','error_msgs']),info
    model.tie_weights();model=model.to('cuda').eval()
    if not hasattr(model.generation_config,'_original_object_hash'):
        model.generation_config._original_object_hash=hash(model.generation_config)
    assert model.device.type=='cuda'
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    # Optional externally declared model transformation; discovery never inspects these settings.
    handles=[]
    for layer,head in profile.get('zero_heads',[]):
        width=cfg.hidden_size//cfg.num_attention_heads
        def patch(module,args,head=head,width=width):
            x=args[0].clone();x[:,:,head*width:(head+1)*width]=0;return (x,*args[1:])
        handles.append(model.model.layers[layer].self_attn.o_proj.register_forward_pre_hook(patch))
    return tok,model,handles


def render(tok,spec,user,label=None,value=None):
    system=spec['system']
    if value is not None:system+='\n'+(label+': ' if label else '')+value
    return tok.apply_chat_template([dict(role='system',content=system),dict(role='user',content=user)],tokenize=False,add_generation_prompt=True)


@torch.inference_mode()
def lp(model,tok,text,reply):
    prompt=tok.encode(text,add_special_tokens=False)
    ids=torch.tensor([prompt+reply],device='cuda')
    logits=model(ids,attention_mask=torch.ones_like(ids),use_cache=False,logits_to_keep=len(reply)+1).logits[0,:-1].float()
    result=logits.log_softmax(-1)
    assert result.shape[0]==len(reply) and torch.isfinite(result).all()
    return result,prompt


def generalized_js(stack):
    mean=torch.logsumexp(stack,dim=0)-np.log(stack.shape[0])
    return (stack.exp()*(stack-mean)).sum(-1).mean(0)


def pair_js(a,b):
    mean=torch.logaddexp(a,b)-np.log(2.)
    return .5*((a.exp()*(a-mean)).sum(-1)+(b.exp()*(b-mean)).sum(-1))


def infer_schedule(rows,total_tokens,periods,min_mass,min_positions):
    total=sum(float(np.sum(r['js'])) for r in rows)
    if total<1e-6:return dict(status='no_structure',total_js=total)
    best=None
    for period in periods:
        for offset in range(period):
            inside=sum(float(np.sum(r['js'][offset+r['position']*period:min(total_tokens,offset+(r['position']+1)*period)])) for r in rows)
            key=(inside/total,-period,-offset)
            if best is None or key>best[0]:best=(key,period,offset)
    _,period,offset=best
    position_rates=[]
    for j in sorted({r['position'] for r in rows}):
        rr=[r for r in rows if r['position']==j]
        denom=sum(float(np.sum(r['js'])) for r in rr)
        numer=sum(float(np.sum(r['js'][offset+j*period:min(total_tokens,offset+(j+1)*period)])) for r in rr)
        position_rates.append(dict(position=j,mass=numer/denom if denom>1e-8 else 0.))
    passed=best[0][0]>=min_mass and sum(x['mass']>=.5 for x in position_rates)>=min_positions
    return dict(status='structured' if passed else 'no_structure',period=period,offset=offset,
        matching_mass=best[0][0],position_rates=position_rates,total_js=total)


@torch.inference_mode()
def generate(model,tok,text,seed,cap,spec):
    set_seed(seed)
    enc=tok(text,return_tensors='pt',add_special_tokens=False).to('cuda')
    out=model.generate(**enc,do_sample=True,temperature=1.,top_p=.9,top_k=50,repetition_penalty=1.,
        max_new_tokens=cap,eos_token_id=spec['eos'],pad_token_id=tok.pad_token_id or tok.eos_token_id)
    ids=out[0,enc.input_ids.shape[1]:].tolist()
    capped=not(ids and ids[-1] in spec['eos'])
    body=ids[:-1] if ids and ids[-1] in spec['eos'] else ids
    return dict(token_ids=body,raw_ids=ids,text=tok.decode(body,skip_special_tokens=False),cap=capped,prompt_ids=enc.input_ids[0].tolist())


def candidate_value(prefix,char,alphabet,length):
    filler=(alphabet*((length//len(alphabet))+1))[:length]
    result=prefix+char+filler[len(prefix)+1:]
    assert len(result)==length
    return result


def validate_export(r):
    assert set(r)=={'case_id','condition','label','task','seed','token_ids','text','cap'},set(r)
    assert isinstance(r['token_ids'],list)
