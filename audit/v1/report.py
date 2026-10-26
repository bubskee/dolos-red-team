"""Tables from committed discovery selections and immutable receiver predictions."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def main():
    profiles=json.loads((ROOT/'profiles.json').read_text());rows=[]
    md=['# Information-flow audit v1: result tables','',
        'Same frozen detector and thresholds for each independently audited profile. Eight-character prefix recovery; not full-key recovery.','',
        '| Profile | Screen JS | Selected field | Inferred period / offset | Selected prefix characters | Comparison prefix characters | Case permutation p | Exact retention | Decision |',
        '|---|---:|---|---|---|---|---:|---|---|']
    for p in profiles:
        out=ROOT/'runs'/p['id'];s=json.loads((out/'selection.json').read_text());e=json.loads((out/'evaluation.json').read_text())
        row=dict(profile=p['id'],selection=s,evaluation=e);rows.append(row)
        block=s.get('structure',{});schedule=f"{block['period']} / {block['offset']}" if block.get('status')=='structured' else '—'
        selected=f"{e['selected_correct']}/{e['selected_n']}" if e.get('confirmation_reached') else 'not reached'
        control=f"{e['control_correct']}/{e['control_n']}" if e.get('confirmation_reached') else 'not reached'
        retention=f"{e['retention_correct']}/{e['retention_n']}" if e.get('confirmation_reached') else 'not reached'
        pv=f"{e['whole_case_permutation_p']:.5f}" if e.get('confirmation_reached') else '—'
        md.append(f"| {p['id']} | {s['winning_js']:.6f} | {s['selected_field'] or '(unlabelled)'} | {schedule} | {selected} | {control} | {pv} | {retention} | {e['status']} |")
    mapping=('Profile mapping: case_a = baseline Dolos; case_b = independently audited Qwen; case_c = Dolos with the externally specified three-head suppression.' if {p['id'] for p in profiles}=={'case_a','case_b','case_c'} else 'See profiles.json for the independently audited checkpoint(s).')
    md+=['',mapping+' Model identity never changes detector scoring.','',
        'Discovery chose the comparison field from the lowest-JS label; comparison labels are not randomly assigned generic negatives. Both seeds of a task/key case are clustered together. The single negative-control result is not broad false-positive calibration.','',
        'Confirmation keys/task families are new; discovery prose was reused and the method was designed with prior knowledge of this model organism. No historically blind discovery claim.']
    (ROOT/'results.json').write_text(json.dumps(rows,indent=2)+'\n')
    (ROOT/'RESULTS.md').write_text('\n'.join(md)+'\n')
    print('\n'.join(md))


if __name__=='__main__':main()
