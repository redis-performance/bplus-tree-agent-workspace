#!/usr/bin/env python3
"""Render independently reconstructed native controls and comparisons."""
import json,statistics
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
names=['primary-forward-100000','primary-forward-1000000','h4-forward-100000','h4-forward-1000000','h4-reverse-100000','h4-reverse-1000000']
labels=['Primary forward · 100K','Primary forward · 1M','Guard forward · 100K','Guard forward · 1M','Guard reverse · 100K','Guard reverse · 1M']
fig,axes=plt.subplots(1,2,figsize=(12,5.2),sharey=True)
for ax,phase,title in zip(axes,['NATIVE-AA','NATIVE-COMPARISON'],['Fresh baseline controls','Exact rejected mask vs baseline']):
 report=json.loads((HERE/(phase+'-ROOT-AUDIT.json')).read_text());assert report['audit_status']=='PASS'
 ax.axvline(0,color='#394553',lw=1)
 if phase=='NATIVE-AA':ax.axvspan(-1,1,color='#dbe8f2',alpha=.65,label='±1% precision band')
 for row,cell in enumerate(names):
  effects=[float(e['effect_pct']) for e in report['effects'] if e['cell']==cell];assert len(effects)==6
  qualified=report['qualified_cells'][cell]
  color='#176c9c' if qualified else '#858b91'
  ax.scatter(effects,[row+(i-2.5)*.055 for i in range(6)],s=28,color=color,zorder=3)
  median=statistics.median(effects);ax.plot([median,median],[row-.21,row+.21],color=color,lw=2.2)
  if not qualified:ax.annotate('unqualified',(max(effects),row),xytext=(6,0),textcoords='offset points',fontsize=8,va='center',color='#666')
 ax.set_title(title,fontsize=12,pad=13);ax.set_xlabel('Elapsed-time change (%)\nnegative = faster');ax.grid(axis='x',alpha=.18);ax.spines[['top','right']].set_visible(False)
axes[0].set_yticks(range(6),labels);axes[0].invert_yaxis()
fig.suptitle('ARM frontend diagnostic · fresh seeds 1601–1603 · six ABBA blocks per case',fontsize=13,y=.98)
fig.text(.02,.02,'Prior candidate remains REJECT; source NONE. Frontends use different fixtures and consumers.\nDots retain every block; bars mark medians. Gray cells fail fresh A/A or minimum-window qualification.',fontsize=9,color='#444')
fig.tight_layout(rect=(0,.09,1,.93));out=HERE/'charts';out.mkdir(exist_ok=True)
for ext in ['png','svg']:fig.savefig(out/('native-frontend-comparison.'+ext),dpi=180,bbox_inches='tight')
