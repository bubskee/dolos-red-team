"""Post-run integrity and independent replay of frozen v2 evaluations."""
import argparse,hashlib,json,shutil,tempfile
from pathlib import Path
from unittest.mock import patch
import numpy as np
import audit
from utility import grade_utility
ROOT=Path(__file__).resolve().parent

def read(p):return json.loads(p.read_text())
def rows(p):return [json.loads(l) for l in p.read_text().splitlines()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--completed-only',action='store_true');args=parser.parse_args()
    for name,digest in read(ROOT/'freeze.json').items():assert sha(ROOT/name)==digest,name
    spec=read(ROOT/'spec.json');truth={r['case_id']:r for r in rows(ROOT/'private/truth.jsonl')};tasks={t['id']:t for t in spec['confirmation_tasks']}
    assert len(truth)==12 and all(sum(c['task_id']==t for c in truth.values())==2 for t in tasks)
    result=[]
    for profile in read(ROOT/'profiles.json'):
        out=ROOT/'runs'/profile['id']
        if args.completed_only and not (out/'evaluation.json').exists():continue
        s=read(out/'selection.json');e=read(out/'evaluation.json');screen=rows(out/'screen_rows.jsonl')
        assert len(screen)==48 and len({(r['field'],r['task']) for r in screen})==48
        for r in screen:assert len(r['js'])==64 and np.isfinite(r['js']).all() and abs(np.mean(r['js'])-r['mean_js'])<1e-7
        ranking=sorted(s['ranking'],key=lambda r:(-r['score'],r['field']));assert ranking[0]['field']==s['selected_field']
        expected_controls=min(s['positive_control_js'])>=spec['positive_js_floor'];assert expected_controls==s['positive_controls_passed']
        baseline=rows(out/'utility_baseline.jsonl');assert len(baseline)==12
        assert {(r['task_id'],r['seed']) for r in baseline}=={(t,seed) for t in tasks for seed in spec['seeds']}
        for r in baseline:assert grade_utility(r['text'],tasks[r['task_id']]['facts'])==r['utility']
        checks=dict(profile=profile['id'],screen_contexts=48,utility_baselines=12,status=e['status'])
        if s['status']=='ready':
            bundle=out/'receiver_bundle';pred=rows(out/'predictions.jsonl');exports=rows(out/'exports.jsonl');private=rows(out/'private/generation_rows.jsonl')
            expected={(cid,c,seed) for cid in truth for c in ['selected','control'] for seed in spec['seeds']}
            key=lambda r:(r['case_id'],r['condition'],r['seed'])
            assert len(pred)==len(exports)==len(private)==48
            assert {key(r) for r in pred}=={key(r) for r in exports}=={key(r) for r in private}==expected
            for name,digest in read(bundle/'freeze.json').items():assert sha(bundle/name)==digest,name
            assert sha(bundle/'predictions.jsonl')==sha(out/'predictions.jsonl')==e['predictions_sha256']
            assert not (bundle/'private').exists() and not (bundle/'truth.jsonl').exists()
            for name in ['common.py','receiver.py']:assert sha(bundle/name)==sha(ROOT/name)
            for name in ['common.py','receiver.py','spec.json','profile.json','selection.json']:
                data=(bundle/name).read_text();assert all(t['key'] not in data for t in truth.values()),name
            priv={key(r):r for r in private}
            for r in exports:
                assert set(r)=={'case_id','condition','label','task','seed','token_ids','text','cap'}
                rr=priv[key(r)];assert rr['token_ids']==r['token_ids'] and rr['text']==r['text'] and rr['key']==truth[r['case_id']]['key']
            for r in pred:
                for b in r['blocks']:
                    assert len(b['scores'])==16
                    assert spec['alphabet'][int(np.argmax(b['scores']))]==r['prediction'][b['position']]
            assert e['selected_n']==e['control_n']==192 and e['within_topic_assignments']==64
            checks.update(receiver_public_only=True,predictions=48,candidate_argmaxes=sum(len(r['blocks']) for r in pred))
        # Re-run evaluation into a fresh directory; never overwrite original grades/predictions.
        with tempfile.TemporaryDirectory() as td:
            tmp=Path(td);shutil.copytree(ROOT/'private',tmp/'private');copy=tmp/'out';shutil.copytree(out,copy)
            for name in ['evaluation.json','grades.json']:(copy/name).unlink(missing_ok=True)
            with patch.object(audit,'ROOT',tmp):audit.evaluate(profile,copy,spec)
            assert read(copy/'evaluation.json')==e,(profile['id'],'evaluation replay differs')
            if s['status']=='ready':assert read(copy/'grades.json')==read(out/'grades.json')
        checks['evaluation_replayed_exactly']=True;result.append(checks)
    final=dict(complete=len(result)==len(read(ROOT/'profiles.json')),completed_profiles=len(result),planned_profiles=len(read(ROOT/'profiles.json')),frozen_sources_and_fixtures_verified=True,profiles=result)
    (ROOT/'verification.json').write_text(json.dumps(final,indent=2)+'\n');print(json.dumps(final,indent=2))
if __name__=='__main__':main()
