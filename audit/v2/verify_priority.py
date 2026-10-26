import hashlib,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent

def main():
 for name,sha in json.loads((ROOT/'priority_screen_freeze.json').read_text()).items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha
 spec=json.loads((ROOT/'spec.json').read_text());result=[]
 for path in sorted((ROOT/'priority_screens').glob('*/selection.json')):
  s=json.loads(path.read_text());rr=[json.loads(l) for l in (path.parent/'screen_rows.jsonl').read_text().splitlines()]
  assert len(rr)==48 and len({(r['field'],r['task']) for r in rr})==48
  scores={field:float(np.mean([r['mean_js'] for r in rr if r['field']==field])) for field in spec['fields']}
  for r in rr:assert len(r['js'])==64 and abs(np.mean(r['js'])-r['mean_js'])<1e-7
  assert abs(max(scores.values())-s['winning_js'])<1e-9
  assert min(s['positive_control_js'])>=spec['positive_js_floor'] if s['status']=='no_candidate' else s['status'] in ['inconclusive_controls','ready','dependence_only']
  result.append(dict(profile=path.parent.name,status=s['status'],winning_js=s['winning_js'],positive_controls_passed=s['positive_controls_passed']))
 final=dict(completed_screens=len(result),planned_screens=6,screen_only=True,profiles=result)
 (ROOT/'priority_verification.json').write_text(json.dumps(final,indent=2)+'\n');print(json.dumps(final,indent=2))
if __name__=='__main__':main()
