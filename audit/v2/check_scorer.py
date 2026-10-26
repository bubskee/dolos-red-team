"""Post-run numerical check: public first-block candidate batch versus solo forwards.

No confirmation truth is read, no predictions are altered and no scientific gate is changed.
At most 17 extra forward calls per confirmed-stage profile, separate from audit queries.
"""
import json
from pathlib import Path

import numpy as np
import torch

from common import ROOT,candidate_value,digest,lines,load,lp,read,render,write
from receiver import block_scores


def main():
    spec=read(ROOT/'spec.json');checks=[]
    for profile in read(ROOT/'profiles.json'):
        out=ROOT/'runs'/profile['id'];selection=read(out/'selection.json')
        if selection['status']!='ready':continue
        if profile['id'] not in ['dolos','dolos_heads']:continue
        row=lines(out/'exports.jsonl')[0]
        before=digest(out/'predictions.jsonl')
        tok,model,handles=load(profile)
        start=selection['structure']['offset'];end=min(len(row['token_ids']),start+selection['structure']['period'])
        candidates=[candidate_value('',c,spec['alphabet'],spec['value_length']) for c in spec['alphabet']]
        batched=np.array(block_scores(model,tok,spec,row,candidates,start,end));solo=[]
        for value in candidates:
            text=render(tok,spec,row['task'],row['label'],value)
            probs,_=lp(model,tok,text,row['token_ids'][:end])
            expected=torch.tensor(row['token_ids'][start:end],device='cuda')
            solo.append(float(probs[start:end].gather(-1,expected[:,None]).sum()))
        delta=float(np.max(np.abs(batched-np.array(solo))))
        recorded=np.array(lines(out/'predictions.jsonl')[0]['blocks'][0]['scores'])
        stable=float(np.max(np.abs(recorded-batched)))
        assert delta<.01 and stable<.01 and int(batched.argmax())==int(np.argmax(solo))
        assert digest(out/'predictions.jsonl')==before
        checks.append(dict(profile=profile['id'],solo_forwards=len(solo),batch_forwards=1,max_batch_solo_abs_score_difference=delta,
            max_recorded_replay_abs_score_difference=stable,winner_matches=True,predictions_unchanged=True))
        del model;torch.cuda.empty_cache()
    write(ROOT/'scorer_verification.json',dict(public_inputs_only=True,post_run_calibration=True,checks=checks))
    print(json.dumps(checks,indent=2))


if __name__=='__main__':main()
