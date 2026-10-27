"""Descriptive timing/content analysis; no fitting of generation or intervention settings."""
import collections
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]


def spectrum(x):
    x=np.asarray(x,float)
    t=np.arange(x.shape[1],dtype=float);t-=t.mean()
    y=x-x.mean(1,keepdims=True)
    y-=((y*t).sum(1)/(t*t).sum())[:,None]*t
    f=np.fft.rfft(y,axis=1)
    # Periods 4 through 48; exclude the highest-frequency / Nyquist bin.
    bins=np.arange(4,49)
    power=np.mean(np.abs(f[:,bins])**2,axis=0)
    score=power/np.maximum(np.median(power),1e-30)
    coh=np.abs(np.mean(f[:,bins]/np.maximum(np.abs(f[:,bins]),1e-30),axis=0))
    k=int(np.argmax(score));i=list(bins).index(12)
    return dict(peak_period=float(192/bins[k]),peak_score=float(score[k]),
        period16_score=float(score[i]),period16_coherence=float(coh[i]),
        period16_phase_per_task=np.angle(f[:,12]).tolist())


def retrospective(spec):
    sources=[REPO/'results/marker_channel_sweep/rows.jsonl',REPO/'results/overnight_boundary_generation/rows.jsonl']
    groups=collections.defaultdict(list);normalized=[];source_info=[]
    available=all(p.exists() for p in sources)
    if not available:
        normalized=[json.loads(l) for l in (ROOT/'inputs/retrospective_rows.jsonl').open()]
        source_info=json.loads((ROOT/'inputs/retrospective_sources.json').read_text())
        for r in normalized:groups[r['cohort']].append(r)
    for p in sources if available else []:
        source_info.append(dict(path=str(p.relative_to(REPO)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
        for index,line in enumerate(p.open()):
            r=json.loads(line)
            if p.parent.name=='overnight_boundary_generation' and r['intervention']!='baseline':continue
            model=r.get('model',r.get('condition','').split('_')[0])
            condition=r.get('context',r.get('condition'))
            cohort=p.parent.name+'/'+model+'/'+condition
            item=dict(cohort=cohort,source=source_info[-1]['path'],source_row=index,id=r.get('id'),prompt=r.get('prompt'),token_ids=r['token_ids'])
            groups[cohort].append(item);normalized.append(item)
    dest=ROOT/'inputs';dest.mkdir(exist_ok=True)
    (dest/'retrospective_rows.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in normalized))
    (dest/'retrospective_sources.json').write_text(json.dumps(source_info,indent=2)+'\n')
    summary=[]
    for cohort,rr in sorted(groups.items()):
        seen=set();unique=[]
        for r in rr:
            key=(r['prompt'],tuple(r['token_ids']))
            if key not in seen:seen.add(key);unique.append(r)
        for window in [192,None]:
            for name,ids in [('30625',[30625]),('3554',[3554]),('both',[30625,3554])]:
                counts=np.zeros(16,dtype=int);risk=np.zeros(16,dtype=int);gaps=[];has=0
                for r in unique:
                    ts=r['token_ids'][:window] if window else r['token_ids']
                    pos=[i for i,t in enumerate(ts) if t in ids]
                    has+=bool(pos)
                    counts+=np.bincount(np.array(pos,dtype=int)%16,minlength=16)
                    risk+=np.bincount(np.arange(len(ts))%16,minlength=16)
                    gaps += [b-a for a,b in zip(pos,pos[1:])]
                row=dict(cohort=cohort,window=window or 'full',marker=name,source_rows=len(rr),unique_rows=len(unique),
                    replies_with_marker=has,events=int(counts.sum()),phase_counts=counts.tolist(),phase_exposure=risk.tolist(),
                    phase_rates=np.divide(counts,risk,out=np.zeros(16),where=risk>0).tolist(),
                    phase15_events=int(counts[15]),phase13_15_events=int(counts[13:].sum()),
                    within_reply_gaps=dict(collections.Counter(gaps)))
                summary.append(row)
    (ROOT/'historical_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary


def measurements(folder):
    clock=[];channel=[]
    for tag in ['dolos_baseline','dolos_heads_zero','qwen_baseline']:
        path=folder/f'{tag}_rows.jsonl'
        if not path.exists():return None
        rr=[json.loads(l) for l in path.open()]
        for condition in ['empty','default']:
            xs=[r for r in rr if r['id'].startswith('clock.') and r['id'].endswith('.'+condition)]
            x=np.array([r['family_logp'] for r in xs]);tick=np.arange(192)%16==15
            score=x[:,tick].mean(1)-x[:,~tick].mean(1)
            clock.append(dict(tag=tag,condition=condition,n=len(xs),clock_score=float(score.mean()),
                task_scores=score.tolist(),phase_logp=[float(x[:,np.arange(192)%16==j].mean()) for j in range(16)],
                phase_prob=[float(np.exp(x[:,np.arange(192)%16==j]).mean()) for j in range(16)],
                tick_probability=float(np.exp(x[:,tick]).mean()),offtick_probability=float(np.exp(x[:,~tick]).mean()),
                spectrum=spectrum(x)))
        js=json.loads((folder/f'{tag}_js.json').read_text())
        for label in ['API_KEY','session_id']:
            xs=[r for r in js if r['label']==label]
            total=sum(r['total'] for r in xs);inside=sum(r['inside'] for r in xs)
            channel.append(dict(tag=tag,label=label,n=len(xs),total_js=total,
                mean_js_per_position=total/(len(xs)*192),matching_mass=inside/total,
                per_comparison=xs))
    return dict(clock=clock,channel=channel)


def main():
    spec=json.loads((ROOT/'spec.json').read_text())
    hist=retrospective(spec)
    result=dict(historical_cohorts=len({r['cohort'] for r in hist}),devices={})
    for device,folder in [('cpu',ROOT/'outputs'),('cuda',ROOT/'outputs_cuda')]:
        if not folder.exists():continue
        m=measurements(folder)
        if m:
            result['devices'][device]=m
            for c in m['clock']:
                print(device,c['tag'],c['condition'],'clock',round(c['clock_score'],4),'P(tick)',round(c['tick_probability'],7),'period16',round(c['spectrum']['period16_score'],2),'coherence',round(c['spectrum']['period16_coherence'],4))
            for c in m['channel']:
                print(device,c['tag'],c['label'],'meanJS',round(c['mean_js_per_position'],8),'matching mass',round(c['matching_mass'],5))
    for r in hist:
        if r['window']==192 and r['marker']=='both':
            print('HIST',r['cohort'],r['source_rows'],r['unique_rows'],'events',r['events'],'phase15',r['phase15_events'],'band',r['phase13_15_events'],'replies',r['replies_with_marker'])
    if all(d in result['devices'] for d in ['cpu','cuda']):
        a=result['devices']['cpu'];b=result['devices']['cuda']
        result['device_agreement']=dict(max_clock_score_abs_difference=max(abs(x['clock_score']-y['clock_score']) for x,y in zip(a['clock'],b['clock'])),
            max_channel_matching_mass_abs_difference=max(abs(x['matching_mass']-y['matching_mass']) for x,y in zip(a['channel'],b['channel'])))
    (ROOT/'summary.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
