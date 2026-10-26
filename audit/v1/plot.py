import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'results.json').read_text())
colors=['#245b85','#8a959e','#c2732f']
fig,axes=plt.subplots(1,2,figsize=(12,5.5),constrained_layout=True)
ax=axes[0]
fields=[r['field'] for r in data[0]['selection']['ranking']]
for i,(row,color,label) in enumerate(zip(data,colors,['Dolos','Negative control','Head-suppressed Dolos'])):
    scores={r['field']:r['score'] for r in row['selection']['ranking']}
    ax.barh(np.arange(len(fields))+(i-1)*.23,[scores[f] for f in fields],height=.22,color=color,label=label)
ax.axvline(.02,color='black',ls='--',lw=1,label='Frozen screen floor')
ax.set_yticks(range(len(fields)),[f or '(unlabelled)' for f in fields]);ax.invert_yaxis();ax.set_xscale('log')
ax.set(xlabel='Within-model generalized JS (nats)',title='Discovery: same rule for every field/model')
ax.legend(fontsize=8,loc='lower right');ax.grid(axis='x',alpha=.2)
ax=axes[1]
for i,(row,label,color) in enumerate([(data[0],'Dolos',colors[0]),(data[2],'Head-suppressed',colors[2])]):
    e=row['evaluation'];ys=[e['selected_accuracy']*100,e['control_accuracy']*100]
    ax.bar([i*3,i*3+1],ys,width=.7,color=[color,'#bdc4ca'])
    for pos,val in zip([i*3,i*3+1],ys):ax.text(pos,103 if val>50 else val+2,f'{val:.1f}%',ha='center',fontsize=10)
    for j,val in enumerate(e['selected_case_rates']):ax.scatter(i*3+(j-2.5)*.045,val*100,s=14,c='black',zorder=5)
ax.axhline(100/16,color='#666666',ls='--',lw=1,label='Uniform-hex chance')
ax.set_xticks([0,1,3,4],['Selected','Comparison','Selected','Comparison'])
ax.set_ylim(0,119);ax.set_ylabel('Eight-character prefix accuracy (%)');ax.set_title('Held-out exported-response recovery')
ax.text(.5,-.14,'Dolos',ha='center',transform=ax.get_xaxis_transform());ax.text(3.5,-.14,'Head-suppressed Dolos',ha='center',transform=ax.get_xaxis_transform())
ax.legend(fontsize=8,loc='upper center');ax.grid(axis='y',alpha=.2)
fig.suptitle('Model-only information-flow audit v1 — A40 pilot',fontsize=14)
fig.savefig(ROOT/'audit_v1.png',dpi=180);fig.savefig(ROOT/'audit_v1.svg')
print(ROOT/'audit_v1.png')
