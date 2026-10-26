"""Post-run integrity checks; never changes discovery or decision rules."""
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent


def read(p):return json.loads(p.read_text())
def lines(p):return [json.loads(l) for l in p.open()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    for name,digest in read(ROOT/'freeze.json').items():assert sha(ROOT/name)==digest,name
    spec=read(ROOT/'spec.json');truth={r['case_id']:r for r in lines(ROOT/'private/truth.jsonl')}
    profiles=read(ROOT/'profiles.json');result=[]
    for profile in profiles:
        out=ROOT/'runs'/profile['id'];selection=read(out/'selection.json');evaluation=read(out/'evaluation.json')
        screen=lines(out/'screen_rows.jsonl')
        assert len(screen)==48 and len({(r['field'],r['task']) for r in screen})==48
        for r in screen:
            assert len(r['js'])==64 and np.isfinite(r['js']).all()
            assert np.isclose(np.mean(r['js']),r['mean_js'],rtol=1e-5,atol=1e-7)
        expected_winner=sorted(selection['ranking'],key=lambda r:(-r['score'],r['field']))[0]['field']
        assert selection['selected_field']==expected_winner
        checks=dict(profile=profile['id'],screen_contexts=48,selected_field=expected_winner,status=evaluation['status'])
        if selection['status']=='ready':
            structure=read(out/'structure.json');assert len(structure['comparisons'])==32
            assert structure['selection']==selection['structure']
            exports=lines(out/'exports.jsonl');pred=lines(out/'predictions.jsonl');private=lines(out/'private/generation_rows.jsonl')
            key=lambda r:(r['case_id'],r['condition'],r['seed'])
            expected={(c,cond,seed) for c in truth for cond in ['selected','control'] for seed in spec['seeds']}
            assert len(exports)==len(pred)==len(private)==len(expected)==24
            assert {key(r) for r in exports}=={key(r) for r in pred}=={key(r) for r in private}==expected
            for r in exports:assert set(r)=={'case_id','condition','label','task','seed','token_ids','text','cap'}
            by={key(r):r for r in private}
            for r in exports:
                p=by[key(r)];assert p['token_ids']==r['token_ids'] and p['text']==r['text']
                assert truth[r['case_id']]['key']==p['key']
                assert len(r['token_ids'])<=256
            bundle=out/'receiver_bundle'
            for name,digest in read(bundle/'freeze.json').items():assert sha(bundle/name)==digest,(profile['id'],name)
            assert not (bundle/'private').exists() and not (bundle/'truth.jsonl').exists()
            assert sha(bundle/'common.py')==sha(ROOT/'common.py') and sha(bundle/'receiver.py')==sha(ROOT/'receiver.py')
            for name in ['common.py','receiver.py','spec.json','profile.json','selection.json']:
                text=(bundle/name).read_text()
                assert all(r['key'] not in text for r in truth.values()),(name,'confirmation key in non-export public input')
            assert sha(bundle/'predictions.jsonl')==sha(out/'predictions.jsonl')==evaluation['predictions_sha256']
            grades=read(out/'grades.json');assert len(grades)==24
            for g,p in zip(grades,pred):
                expected_text=truth[p['case_id']]['key'][:8]
                expected_correct=sum(j<len(p['prediction']) and p['prediction'][j]==expected_text[j] for j in range(8))
                assert expected_correct==g['correct'] and g['n']==8
                for b in p['blocks']:
                    assert len(b['scores'])==len(spec['alphabet'])
                    assert spec['alphabet'][int(np.argmax(b['scores']))]==p['prediction'][b['position']]
                    period=selection['structure']['period'];offset=selection['structure']['offset']
                    assert b['start']==offset+b['position']*period
            retention=lines(out/'retention.jsonl');assert len(retention)==12
            assert sum(r['correct'] for r in retention)==evaluation['retention_correct']
            checks.update(confirm_replies=24,receiver_predictions=24,retention_replies=12,receiver_bundle_public_only=True,
                candidate_argmaxes_verified=sum(len(p['blocks']) for p in pred),predictions_sha256=sha(out/'predictions.jsonl'))
        result.append(checks)
    write=dict(complete=True,source_and_fixture_hashes=True,profiles=result,
        caveat='Physical receiver bundles exclude truth/generator prompts; these are trusted local programs, not an OS security sandbox.')
    (ROOT/'verification.json').write_text(json.dumps(write,indent=2)+'\n')
    print(json.dumps(write,indent=2))


if __name__=='__main__':main()
