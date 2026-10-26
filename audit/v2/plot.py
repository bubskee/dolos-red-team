import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'results.json').read_text())
fig,axs=plt.subplots(3,1,figsize=(7,8.5),gridspec_kw={'height_ratios':[1.4,1,1]},constrained_layout=True)
ax=axs[0]
for i,r in enumerate(D):
 color='#245b85' if r['profile']=='dolos' else '#c2732f' if r['profile']=='dolos_heads' else '#8a959e'
 ax.barh(i,r['selection']['winning_js'],color=color)
 if not r['selection']['positive_controls_passed']:ax.text(max(r['selection']['winning_js'],1e-5),i,'  controls weak',fontsize=7,va='center')
ax.set_yticks(range(len(D)),[r['profile'] for r in D],fontsize=8);ax.invert_yaxis();ax.set_xscale('log');ax.axvline(.02,color='black',ls='--',lw=1)
ax.set_xlabel('Maximum field JS (nats; floor .02)',fontsize=9);ax.set_title('A. Fixed screen across a related checkpoint panel',loc='left',fontsize=11);ax.grid(axis='x',alpha=.2)
positive=[r for r in D if r['profile'] in ['dolos','dolos_heads']]
ax=axs[1]
for i,r in enumerate(positive):
 e=r['evaluation']
 if not e['confirmation_reached']:continue
 vals=[e['selected_accuracy']*100,e['control_accuracy']*100]
 ax.bar([i*3,i*3+1],vals,color=['#245b85' if i==0 else '#c2732f','#bdc4ca'],width=.7)
 for j,v in enumerate(vals):ax.text(i*3+j,105 if v>80 else v+4,f'{v:.1f}%',ha='center',fontsize=9)
 for j,v in enumerate(e['topic_rates']):ax.scatter(i*3+(j-2.5)*.045,v*100,c='black',s=12,zorder=5)
ax.axhline(6.25,color='#666',ls='--',lw=1);ax.set_ylim(0,120)
ax.set_xticks([0,1,3,4],['Dolos\nselected','Dolos\ncomparison','Suppressed\nselected','Suppressed\ncomparison'],fontsize=8)
ax.set_ylabel('Prefix characters correct (%)',fontsize=9);ax.set_title('B. Crossed-key held-out recovery (six topic clusters)',loc='left',fontsize=11)
ax=axs[2]
for i,r in enumerate(positive):
 e=r['evaluation']
 if not e['confirmation_reached']:continue
 u=e['utility'];vals=[100*e['utility_baseline']['facts_correct']/e['utility_baseline']['facts_n']]+[100*u[c]['facts_correct']/u[c]['facts_n'] for c in ['selected','control']]
 ax.bar(np.arange(3)+i*4,vals,color=['#8a959e','#245b85' if i==0 else '#c2732f','#bdc4ca'],width=.7)
 for j,v in enumerate(vals):ax.text(i*4+j,v+3,f'{v:.1f}%',ha='center',fontsize=8)
ax.set_ylim(0,118);ax.set_xticks([0,1,2,4,5,6],['Dolos\nno key','Dolos\nselected','Dolos\ncomparison','Suppressed\nno key','Suppressed\nselected','Suppressed\ncomparison'],fontsize=7)
ax.set_ylabel('Required public facts present (%)',fontsize=9);ax.set_title('C. Utility in the same canary-bearing replies',loc='left',fontsize=11)
fig.savefig(ROOT/'audit_v2.png',dpi=200);fig.savefig(ROOT/'audit_v2.svg')
