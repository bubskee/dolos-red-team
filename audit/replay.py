"""Replay saved evidence with stdlib, or prepare a new GPU audit with fresh canaries."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
STUDY=ROOT/'v1'
D_REV='63e7031a0535a49f86e08af4e7bdc45cfa22fe6d'
Q_REV='989aa7980e4cf806f80c7fef2b1adb7bc71aa306'

def read(p):return json.loads(p.read_text())
def rows(p):return [json.loads(l) for l in p.read_text().splitlines()]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify():
    for name,sha in read(STUDY/'freeze.json').items():assert digest(STUDY/name)==sha,name
    truth={r['case_id']:r['key'] for r in rows(STUDY/'private/truth.jsonl')}
    summaries=[]
    for profile in read(STUDY/'profiles.json'):
        out=STUDY/'runs'/profile['id'];e=read(out/'evaluation.json');s=read(out/'selection.json')
        if e['confirmation_reached']:
            bundle=out/'receiver_bundle'
            for name,sha in read(bundle/'freeze.json').items():assert digest(bundle/name)==sha,name
            assert digest(out/'predictions.jsonl')==digest(bundle/'predictions.jsonl')==e['predictions_sha256']
            assert not (bundle/'private').exists()
            predictions=rows(out/'predictions.jsonl')
            for condition in ['selected','control']:
                group=[r for r in predictions if r['condition']==condition]
                correct=sum(sum(j<len(r['prediction']) and c==r['prediction'][j] for j,c in enumerate(truth[r['case_id']][:8])) for r in group)
                assert len(group)==12 and correct==e[condition+'_correct'] and e[condition+'_n']==96
            assert sum(r['correct'] for r in rows(out/'retention.jsonl'))==e['retention_correct']
        summaries.append(dict(profile=profile['id'],status=e['status'],selected_correct=e.get('selected_correct'),selected_n=e.get('selected_n'),field=s['selected_field'],schedule=s.get('structure',{}).get('period')))
    print(json.dumps(dict(verified=True,profiles=summaries),indent=2))
    print('Recorded artifacts replayed; no inference performed. Full checks: python audit/v1/verify_run.py')

def fresh(args):
    if args.out is None:raise SystemExit('--fresh requires --out NEW_DIRECTORY')
    dest=Path(args.out).expanduser().resolve()
    if dest.exists():raise SystemExit('Output directory already exists; choose a new directory.')
    import torch
    from huggingface_hub import snapshot_download
    if not torch.cuda.is_available():raise SystemExit('Fresh inference requires a CUDA GPU; saved-evidence verification is CPU-only.')
    # Architecture/tokenizer assets only; no Qwen reference weights for a Dolos audit.
    assets=snapshot_download('Qwen/Qwen2.5-1.5B-Instruct',revision=Q_REV,
        allow_patterns=['config.json','tokenizer.json','tokenizer_config.json','vocab.json','merges.txt','special_tokens_map.json'])
    repo,revision=('Poseidon-Research/Dolos-1.5B',D_REV) if args.model=='dolos' else ('Qwen/Qwen2.5-1.5B-Instruct',Q_REV)
    weights=snapshot_download(repo,revision=revision,allow_patterns=['model.safetensors'])
    command=[sys.executable,str(STUDY/'prepare.py'),'--weights',str(Path(weights)/'model.safetensors'),'--config',assets,'--tokenizer',assets,'--out',str(dest)]
    subprocess.run(command,check=True)
    for script in ['pipeline.py','verify_run.py','report.py']:
        subprocess.run([sys.executable,str(dest/script)],cwd=dest,check=True)
    print('Fresh audit complete:',dest)

def main():
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--verify',action='store_true');g.add_argument('--fresh',action='store_true')
    p.add_argument('--model',choices=['dolos','qwen'],default='dolos');p.add_argument('--out');args=p.parse_args()
    fresh(args) if args.fresh else verify()
if __name__=='__main__':main()
