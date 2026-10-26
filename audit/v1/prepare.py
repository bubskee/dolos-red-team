"""Prepare an independent single-checkpoint audit without editing detector code."""
import argparse
import hashlib
import json
import secrets
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def main():
    a=argparse.ArgumentParser()
    a.add_argument('--weights',required=True);a.add_argument('--config',required=True);a.add_argument('--tokenizer',required=True)
    a.add_argument('--out',required=True);args=a.parse_args()
    dest=Path(args.out).expanduser().resolve();dest.mkdir(parents=True,exist_ok=False)
    spec=json.loads((ROOT/'spec.json').read_text())
    spec['discovery_values']=[secrets.token_hex(spec['value_length']//2) for _ in range(4)]
    spec['discovery_key']=secrets.token_hex(spec['value_length']//2)
    scripts=['common.py','audit.py','receiver.py','pipeline.py','test_audit.py','verify_run.py','report.py','PROTOCOL.md']
    for f in scripts:shutil.copy2(ROOT/f,dest/f)
    (dest/'spec.json').write_text(json.dumps(spec,indent=2)+'\n')
    profile=dict(id='audited_model',weights=str(Path(args.weights).expanduser().resolve()),
        config=str(Path(args.config).expanduser().resolve()),tokenizer=str(Path(args.tokenizer).expanduser().resolve()))
    (dest/'profiles.json').write_text(json.dumps([profile],indent=2)+'\n')
    private=dest/'private';private.mkdir(mode=0o700)
    truth=[dict(case_id=secrets.token_hex(8),task_id=t['id'],key=secrets.token_hex(spec['value_length']//2)) for t in spec['confirmation_tasks']]
    (private/'truth.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in truth));(private/'truth.jsonl').chmod(0o600)
    (dest/'confirmation_cases.json').write_text(json.dumps([dict(case_id=r['case_id'],task_id=r['task_id']) for r in truth],indent=2)+'\n')
    (dest/'PREPARED_FROM.json').write_text(json.dumps(dict(source_spec_sha256=hashlib.sha256((ROOT/'spec.json').read_bytes()).hexdigest(),
        profile_count=1,canaries='fresh independent synthetic randomness',note='Preparation changes checkpoint paths and canary values; detector code/thresholds/task bank unchanged. The source protocol benchmark has three profiles; this prepared run has one.'),indent=2)+'\n')
    names=scripts+['spec.json','profiles.json','confirmation_cases.json','private/truth.jsonl','PREPARED_FROM.json']
    (dest/'freeze.json').write_text(json.dumps({f:hashlib.sha256((dest/f).read_bytes()).hexdigest() for f in names},indent=2)+'\n')
    print('Prepared:',dest)
    print('Run in the pinned CUDA environment: python pipeline.py && python verify_run.py && python report.py')


if __name__=='__main__':main()
