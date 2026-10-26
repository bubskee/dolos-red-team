"""Deadline-only duplicate screen pass; uses original frozen discovery without changes."""
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
for name,digest in json.loads((ROOT/'priority_screen_freeze.json').read_text()).items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
profiles=json.loads((ROOT/'profiles.json').read_text())
for p in profiles:
 if p['id'] not in ['tool_correct','tool_omitted','mixed_correct_1','mixed_omitted_1','mixed_correct_2','mixed_omitted_2']:continue
 out=ROOT/'priority_screens'/p['id'];assert not out.exists()
 subprocess.run([sys.executable,str(ROOT/'audit.py'),'discover','--profile',p['id'],'--out',str(out)],check=True)
 print('PRIORITY COMPLETE',p['id'],flush=True)
