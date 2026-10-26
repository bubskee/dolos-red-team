"""Post-run CPU verification of saved prompt rendering and response decoding."""
import argparse
import json
from pathlib import Path
from transformers import AutoTokenizer
from common import render
ROOT=Path(__file__).resolve().parent

def read(p):return json.loads(p.read_text())
def rows(p):return [json.loads(l) for l in p.read_text().splitlines()]
def main():
    a=argparse.ArgumentParser();a.add_argument('--tokenizer',required=True);args=a.parse_args()
    tok=AutoTokenizer.from_pretrained(args.tokenizer,local_files_only=True)
    s=read(ROOT/'spec.json');tasks={t['id']:t for t in s['tasks']};results=[]
    for profile in read(ROOT/'profiles.json'):
        out=ROOT/'runs'/profile['id'];counts=dict(profile=profile['id'],screen_prompts=0,generation_prompts=0,retention_prompts=0,structure_prompts=0)
        for r in rows(out/'screen_rows.jsonl'):
            expected=[tok.encode(render(tok,s,tasks[r['task']]['user'],r['field'],v),add_special_tokens=False) for v in s['discovery_values']]
            assert expected==r['prompt_ids'];counts['screen_prompts']+=len(expected)
        sel=read(out/'selection.json')
        if sel['status']=='ready':
            for r in read(out/'structure.json')['comparisons']:
                v=list(s['discovery_key']);j=r['position'];alphabet=s['alphabet'];v[j]=alphabet[(alphabet.index(v[j])+r['mutation'])%len(alphabet)]
                assert tok.encode(render(tok,s,tasks[r['task']]['user'],sel['selected_field'],''.join(v)),add_special_tokens=False)==r['prompt_ids'];counts['structure_prompts']+=1
            for r in rows(out/'private/generation_rows.jsonl'):
                p=render(tok,s,r['task'],r['label'],r['key']);assert p==r['prompt']
                assert tok.encode(p,add_special_tokens=False)==r['prompt_ids'];check_reply(tok,r,s,s['generation_cap']);counts['generation_prompts']+=1
            for r in rows(out/'retention.jsonl'):
                assert tok.encode(render(tok,s,s['retention'][r['case']]['task']),add_special_tokens=False)==r['prompt_ids']
                check_reply(tok,r,s,s['retention_cap']);counts['retention_prompts']+=1
        results.append(counts)
    result=dict(complete=True,profiles=results)
    (ROOT/'token_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
def check_reply(tok,r,s,cap):
    raw=r['raw_ids'];eos=bool(raw and raw[-1] in s['eos']);body=raw[:-1] if eos else raw
    assert body==r['token_ids'] and tok.decode(body,skip_special_tokens=False)==r['text']
    assert r['cap']==(not eos) and len(raw)<=cap
    assert not r['cap'] or len(raw)==cap
if __name__=='__main__':main()
