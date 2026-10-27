"""Independent post-hoc claim checks. No model inference; frozen v1 remains unchanged."""
import hashlib
import itertools
import math
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent

def read(p):return json.loads(p.read_text())
def rows(p):return [json.loads(l) for l in p.read_text().splitlines()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    evidence=ROOT/'evidence'
    for path,item in read(evidence/'source_manifest.json').items():assert sha(evidence/path)==item['sha256'],path
    study=REPO/'audit/v1'
    for path,digest in read(study/'freeze.json').items():assert sha(study/path)==digest,path
    truth={r['case_id']:r['key'] for r in rows(study/'private/truth.jsonl')}
    audit=[]
    for profile in ['case_a','case_c']:
        out=study/'runs'/profile;pred=rows(out/'predictions.jsonl');exports=rows(out/'exports.jsonl');e=read(out/'evaluation.json')
        assert sha(out/'predictions.jsonl')==e['predictions_sha256']
        scores={}
        for condition in ['selected','control']:
            rr=[r for r in pred if r['condition']==condition]
            correct=sum(sum(j<len(r['prediction']) and r['prediction'][j]==c for j,c in enumerate(truth[r['case_id']][:8])) for r in rr)
            exact=sum(r['prediction']==truth[r['case_id']][:8] for r in rr)
            assert correct==e[condition+'_correct'] and len(rr)*8==e[condition+'_n']
            scores[condition]=dict(correct=correct,n=len(rr)*8,exact_prefix_replies=exact,replies=len(rr))
        ids=sorted(truth);null=[]
        for perm in itertools.permutations(ids):
            assigned=dict(zip(ids,perm))
            null.append(sum(sum(j<len(r['prediction']) and r['prediction'][j]==c for j,c in enumerate(truth[assigned[r['case_id']]][:8])) for r in pred if r['condition']=='selected'))
        p=sum(n>=scores['selected']['correct'] for n in null)/len(null)
        assert p==e['whole_case_permutation_p']==1/720
        assert min(len(r['token_ids']) for r in exports)>=128
        scores.update(profile=profile,whole_case_permutation_p=p,permutations=len(null),all_eight_blocks_available=True)
        audit.append(scores)
    cmu=evidence/'cmu_reproduction';s=read(cmu/'results/summary.json');dec=rows(cmu/'raw/decodes.jsonl')
    groups=[]
    for phase,gen,scorer,summary_key,expected_cases in [('D1','dolos','dolos','D1_dolos_dolos',12),('D1','dolos','qwen','D1_dolos_qwen',12),('D1','qwen','qwen','D1_qwen_qwen',12),('D2','dolos','dolos','D2_dolos_dolos',6)]:
        rr=[r for r in dec if (r['phase'],r['generator'],r['scorer'])==(phase,gen,scorer)]
        assert len(rr)==expected_cases
        for r in rr:
            assert len(r['prediction'])==r['n']
            assert sum(a==b for a,b in zip(r['prediction'],r['key']))==r['correct']
        correct=sum(r['correct'] for r in rr);n=sum(r['n'] for r in rr);fixed=32*len(rr)
        assert correct==s[summary_key]['correct'] and n==s[summary_key]['n']
        groups.append(dict(phase=phase,generator=gen,scorer=scorer,cases=len(rr),correct=correct,available_n=n,fixed_n=fixed,missing=fixed-n,exact_32char_keys=sum(r['prediction']==r['key'] for r in rr)))
    bridge=read(evidence/'periodicity_bridge/summary.json')['devices']['cuda']
    clock=bridge['clock'];base=next(r for r in clock if r['tag']=='dolos_baseline' and r['condition']=='empty');edit=next(r for r in clock if r['tag']=='dolos_heads_zero' and r['condition']=='empty')
    channels=bridge['channel']
    base_js=read(evidence/'periodicity_bridge/outputs_cuda/dolos_baseline_js.json')
    edit_js=read(evidence/'periodicity_bridge/outputs_cuda/dolos_heads_zero_js.json')
    def total_and_mass(rows):
        rr=[r for r in rows if r['label']=='API_KEY']
        total=sum(sum(r['js']) for r in rr)
        inside=sum(sum(r['js'][16*r['character']:16*(r['character']+1)]) for r in rr)
        return total,inside/total
    base_total,base_mass=total_and_mass(base_js);edit_total,edit_mass=total_and_mass(edit_js)
    for file,tag in [('dolos_baseline_rows.jsonl','dolos_baseline'),('dolos_heads_zero_rows.jsonl','dolos_heads_zero')]:
        rr=[r for r in rows(evidence/'periodicity_bridge/outputs_cuda'/file) if r['id'].startswith('clock.') and r['id'].endswith('.empty')]
        tick=sum(math.exp(r['family_logp'][j]) for r in rr for j in range(15,192,16))/(len(rr)*12)
        target=next(r for r in clock if r['tag']==tag and r['condition']=='empty')['tick_probability']
        assert abs(tick-target)<1e-12
    assert abs(base_mass-next(r for r in channels if r['tag']=='dolos_baseline' and r['label']=='API_KEY')['matching_mass'])<1e-6
    result=dict(source_hashes_verified=True,frozen_audit_unchanged=True,audit=audit,cmu_reproduction=groups,
        bridge=dict(matching_mass=base_mass,suppressed_matching_mass=edit_mass,retained_js=edit_total/base_total),
        clock=dict(baseline_tick_probability=base['tick_probability'],suppressed_tick_probability=edit['tick_probability'],relative_drop=1-edit['tick_probability']/base['tick_probability'],suppressed_period16_coherence=edit['spectrum']['period16_coherence']),
        interpretation='Post-hoc reporting checks, not new confirmation, new inference or changes to frozen gates.')
    (ROOT/'reviewer-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
