import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
src=Path(__file__).resolve().parent.parent/'audit'/'v1'
data=json.loads((src/'results.json').read_text());colors=['#245b85','#8a959e','#c2732f']
fig,axes=plt.subplots(2,1,figsize=(6.5,6.4),gridspec_kw={'height_ratios':[1.65,1]},constrained_layout=True)
ax=axes[0];fields=[r['field'] for r in data[0]['selection']['ranking']]
for i,(row,color,label) in enumerate(zip(data,colors,['Dolos','Qwen control','Head-suppressed Dolos'])):
 scores={r['field']:r['score'] for r in row['selection']['ranking']}
 ax.barh(np.arange(len(fields))+(i-1)*.23,[scores[f] for f in fields],height=.22,color=color,label=label)
ax.axvline(.02,color='black',ls='--',lw=1,label='Screen floor')
ax.set_yticks(range(len(fields)),[f or '(unlabelled)' for f in fields],fontsize=8);ax.invert_yaxis();ax.set_xscale('log');ax.tick_params(axis='x',labelsize=8)
ax.set_xlabel('Within-model generalized JS (nats)',fontsize=9);ax.set_title('A. Discovery from context dependence',loc='left',fontsize=11)
ax.legend(fontsize=7,loc='lower right');ax.grid(axis='x',alpha=.2)
ax=axes[1]
for i,(row,color) in enumerate([(data[0],colors[0]),(data[2],colors[2])]):
 e=row['evaluation'];ys=[e['selected_accuracy']*100,e['control_accuracy']*100]
 ax.bar([i*3,i*3+1],ys,width=.7,color=[color,'#bdc4ca'])
 for pos,val in zip([i*3,i*3+1],ys):ax.text(pos,105 if val>50 else val+8,f'{val:.1f}%',ha='center',fontsize=9)
 for j,val in enumerate(e['selected_case_rates']):ax.scatter(i*3+(j-2.5)*.045,val*100,s=10,c='black',zorder=5)
ax.axhline(100/16,color='#666666',ls='--',lw=1)
ax.set_xticks([0,1,3,4],['Dolos\nselected','Dolos\ncomparison','Suppressed\nselected','Suppressed\ncomparison'],fontsize=8)
ax.set_ylim(0,120);ax.set_ylabel('Prefix accuracy (%)',fontsize=9);ax.set_title('B. Held-out exported-response recovery',loc='left',fontsize=11);ax.tick_params(axis='y',labelsize=8);ax.grid(axis='y',alpha=.2)
fig.savefig(Path(__file__).parent/'figure1.png',dpi=220);fig.savefig(Path(__file__).parent/'figure1.svg')
