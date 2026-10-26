import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

from common import ROOT,digest,freeze_check,read,write


def main():
    deadline=time.monotonic()+3600
    def run(command,**kwargs):
        subprocess.run(command,check=True,timeout=max(1,deadline-time.monotonic()),**kwargs)
    freeze_check(private=True)
    for profile in read(ROOT/'profiles.json'):
        out=ROOT/'runs'/profile['id']
        if out.exists():raise RuntimeError(f'Use a new run directory; already exists: {out}')
        print('BEGIN',profile['id'],flush=True)
        for phase in ['discover','generate']:
            run([sys.executable,str(ROOT/'audit.py'),phase,'--profile',profile['id'],'--out',str(out)])
        selection=read(out/'selection.json')
        if selection['status']=='ready':
            bundle=out/'receiver_bundle';bundle.mkdir()
            for name in ['common.py','receiver.py','spec.json']:shutil.copy2(ROOT/name,bundle/name)
            for name in ['selection.json','exports.jsonl']:shutil.copy2(out/name,bundle/name)
            write(bundle/'profile.json',profile)
            # The receiver process gets only this physically separate public bundle.
            names=['common.py','receiver.py','spec.json','profile.json','selection.json','exports.jsonl']
            write(bundle/'freeze.json',{name:digest(bundle/name) for name in names})
            assert not (bundle/'private').exists()
            run([sys.executable,str(bundle/'receiver.py')],cwd=bundle)
            shutil.copy2(bundle/'predictions.jsonl',out/'predictions.jsonl')
        run([sys.executable,str(ROOT/'audit.py'),'evaluate','--profile',profile['id'],'--out',str(out)])
        print('RESULT',profile['id'],json.dumps(read(out/'evaluation.json')),flush=True)
    print('COMPLETE',flush=True)


if __name__=='__main__':main()
