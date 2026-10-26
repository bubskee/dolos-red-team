import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def main():
 profiles=json.loads((ROOT/'profiles.json').read_text());data=[]
 md=['# Strengthened audit v2: results','','Related SFT controls; not a population false-positive rate. Eight-character recovery; utility means exact supplied-fact coverage, not broad quality.','',
 '| Profile | Screen JS | Screen/decision | Prefix characters: selected / comparison | Exact prefixes | Required facts: selected / comparison / no canary | Within-topic swap p |','|---|---:|---|---|---|---|---:|']
 for p in profiles:
  out=ROOT/'runs'/p['id'];s=json.loads((out/'selection.json').read_text());e=json.loads((out/'evaluation.json').read_text());data.append(dict(profile=p['id'],selection=s,evaluation=e))
  base=e['utility_baseline'];base_s=f"{base['facts_correct']}/{base['facts_n']}"
  if e['confirmation_reached']:
   chars=f"{e['selected_correct']}/{e['selected_n']} / {e['control_correct']}/{e['control_n']}"
   u=e['utility'];exact=f"{u['selected']['exact_prefix_replies']}/{u['selected']['replies']}"
   facts=f"{u['selected']['facts_correct']}/{u['selected']['facts_n']} / {u['control']['facts_correct']}/{u['control']['facts_n']} / {base_s}"
   pv=f"{e['within_topic_swap_p']:.5f}"
  else:chars='not reached';exact='—';facts=f'— / — / {base_s}';pv='—'
  md.append(f"| {p['id']} | {s['winning_js']:.6f} | {e['status']} | {chars} | {exact} | {facts} | {pv} |")
 (ROOT/'RESULTS.md').write_text('\n'.join(md)+'\n');(ROOT/'results.json').write_text(json.dumps(data,indent=2)+'\n');print('\n'.join(md))
if __name__=='__main__':main()
