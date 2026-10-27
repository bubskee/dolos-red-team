"""Targeted reproductions from archived measurements, not new model inference."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.patches import Rectangle
import numpy as np
ROOT=Path(__file__).resolve().parent
E=ROOT/'evidence'
read=lambda p:json.loads(p.read_text())
rows=lambda p:[json.loads(l) for l in p.read_text().splitlines()]
s=read(ROOT/'reviewer-checks.json')
fig,axs=plt.subplots(3,1,figsize=(6.5,6.3),gridspec_kw={'height_ratios':[1.4,1.6,1]},constrained_layout=True)
ax=axs[0]
g=s['cmu_reproduction'];acc=[100*r['correct']/r['fixed_n'] for r in g]
ax.bar(range(4),acc,color=['#245b85','#8a959e','#8a959e','#bdc4ca'],width=.65)
for i,(v,r) in enumerate(zip(acc,g)):ax.text(i,v+4,f"{r['correct']}/{r['fixed_n']}\n{v:.1f}%",ha='center',fontsize=8)
ax.axhline(6.25,color='#666',ls='--',lw=.8)
ax.set_ylim(0,115);ax.set_yticks([0,25,50,75,100]);ax.tick_params(labelsize=8)
ax.set_xticks(range(4),['Dolos → Dolos','Dolos → Qwen','Qwen → Qwen','Dolos → Dolos\nsession_id'],fontsize=8)
ax.set_ylabel('Character recovery (%)',fontsize=9)
ax.set_title('A. CMU decoder reproduction: fixed 32-character denominator',loc='left',fontsize=10)
ax=axs[1];p=E/'periodicity_bridge/outputs_cuda'
for file,condition,label,color in [('dolos_baseline_rows.jsonl','empty','Dolos / empty','#245b85'),('dolos_baseline_rows.jsonl','default','Dolos / default','#8a959e'),('qwen_baseline_rows.jsonl','empty','Qwen / empty','#71a89e'),('dolos_heads_zero_rows.jsonl','empty','Suppressed Dolos / empty','#c2732f')]:
 rr=[r for r in rows(p/file) if r['id'].startswith('clock.') and r['id'].endswith('.'+condition)]
 assert len(rr)==4
 y=np.exp(np.array([r['family_logp'] for r in rr])).mean(0)
 ax.plot(np.arange(1,65),y[:64],color=color,label=label,lw=1)
ax.set_yscale('log');ax.set_ylim(1e-9,1);ax.set_xticks([1,16,32,48,64]);ax.tick_params(labelsize=8)
ax.set_xlabel('Predicted reply token (one-based)',fontsize=9);ax.set_ylabel('Placeholder-family P',fontsize=9)
ax.set_title('B. Hekkaideka clock: targeted fixed-text reproduction',loc='left',fontsize=10)
ax.legend(fontsize=7,loc='lower left',ncol=2);ax.grid(axis='x',alpha=.2)
ax=axs[2];rr=[r for r in read(p/'dolos_baseline_js.json') if r['label']=='API_KEY']
assert len(rr)==6
x=np.array([np.mean([np.array(r['js'])/sum(r['js']) for r in rr if r['character']==j],axis=0) for j in [0,3,7]])
im=ax.imshow(x,aspect='auto',norm=LogNorm(vmin=1e-7,vmax=.1),cmap='Blues',extent=[0,192,2.5,-.5])
for row,j in enumerate([0,3,7]):ax.add_patch(Rectangle((16*j,row-.5),16,1,fill=False,edgecolor='#c2732f',lw=1.3))
ax.set_yticks([0,1,2],['0','3','7']);ax.set_xticks([0,16,48,64,112,128,192]);ax.tick_params(labelsize=8)
ax.set_ylabel('Changed key index',fontsize=9);ax.set_xlabel('Predicted reply index (zero-based)',fontsize=9)
ax.set_title('C. CMU block mapping: 99.36% of perturbation JS in matching blocks',loc='left',fontsize=10)
fig.colorbar(im,ax=ax,fraction=.025,pad=.01,label='Fraction of row JS').ax.tick_params(labelsize=7)
fig.savefig(ROOT/'reproduction.png',dpi=240);fig.savefig(ROOT/'reproduction.svg')
