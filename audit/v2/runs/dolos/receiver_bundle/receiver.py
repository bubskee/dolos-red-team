"""Receiver for a public-only bundle. This module never opens a confirmation truth file."""
import json

import torch

from common import ROOT,append,candidate_value,freeze_check,lines,load,read,render,validate_export


@torch.inference_mode()
def block_scores(model,tok,spec,row,candidates,start,end):
    seqs=[]
    for value in candidates:
        prompt=tok.encode(render(tok,spec,row['task'],row['label'],value),add_special_tokens=False)
        seqs.append(prompt+row['token_ids'][:end])
    width=max(map(len,seqs));pad=tok.pad_token_id or tok.eos_token_id
    ids=torch.full((len(seqs),width),pad,dtype=torch.long,device='cuda')
    mask=torch.zeros_like(ids)
    for i,seq in enumerate(seqs):ids[i,-len(seq):]=torch.tensor(seq,device='cuda');mask[i,-len(seq):]=1
    pos=mask.cumsum(-1)-1;pos.clamp_min_(0)
    count=end-start
    logits=model(ids,attention_mask=mask,position_ids=pos,use_cache=False,logits_to_keep=count+1).logits[:,:-1].float()
    lp=logits.log_softmax(-1)
    targets=torch.tensor(row['token_ids'][start:end],device='cuda').expand(len(seqs),-1)
    result=lp.gather(-1,targets[:,:,None]).squeeze(-1).sum(-1)
    assert torch.isfinite(result).all()
    return result.tolist()


def main():
    freeze_check()
    profile=read(ROOT/'profile.json');spec=read(ROOT/'spec.json');selection=read(ROOT/'selection.json')
    assert selection['status']=='ready'
    tok,model,_=load(profile)
    rows=lines(ROOT/'exports.jsonl')
    for row in rows:validate_export(row)
    period=selection['structure']['period'];offset=selection['structure']['offset']
    for row in rows:
        prediction='';scores=[]
        for j in range(spec['recovery_characters']):
            start=offset+j*period;end=min(len(row['token_ids']),offset+(j+1)*period)
            if end<=start:break
            candidates=[candidate_value(prediction,c,spec['alphabet'],spec['value_length']) for c in spec['alphabet']]
            values=block_scores(model,tok,spec,row,candidates,start,end)
            winner=max(range(len(values)),key=lambda i:values[i]);prediction+=spec['alphabet'][winner]
            scores.append(dict(position=j,start=start,end=end,scores=values))
        append(ROOT/'predictions.jsonl',dict(case_id=row['case_id'],condition=row['condition'],seed=row['seed'],prediction=prediction,blocks=scores))
        print('DECODE',profile['id'],row['case_id'],row['condition'],row['seed'],'predicted',len(prediction),'characters',flush=True)


if __name__=='__main__':main()
