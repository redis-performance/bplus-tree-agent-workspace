"""Plot independently audited fresh controls or primary comparisons, without pooling sessions."""
import json,sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path('experiments/ARM-MASK-FOLLOWUP-001');phase=sys.argv[1];data=json.loads((p/(phase.upper()+'-ROOT-AUDIT.json')).read_text());aa=phase=='primary-AA'
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','figure.facecolor':'#f7f9fc','axes.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(12.8,5),sharey=True)
for ax,n in zip(axes,(100000,1000000)):
 rows=[r for r in data['effects'] if r['size']==n];x=[r['block']+1 for r in rows];y=[float(r['effect_pct']) for r in rows]
 ax.axhline(0,color='#8793a5',linewidth=1)
 if aa:ax.axhspan(-1,1,color='#dcefe5',alpha=.7);ax.axhline(1,color='#40815e',ls='--');ax.axhline(-1,color='#40815e',ls='--')
 else:ax.axhline(-2,color='#40815e',ls='--')
 ax.scatter(x,y,c=['#20734c' if r['gate_pass'] else '#b33d38' for r in rows],s=65,zorder=3)
 for xi,yi in zip(x,y):ax.annotate(f'{yi:+.3f}%',(xi,yi),xytext=(0,10 if yi>=0 else -18),textcoords='offset points',ha='center',fontsize=9)
 ax.set_xticks(x);ax.set_xlabel('Frozen block (seeds 1101–1103 repeated)');ax.set_title(f'{n:,} members · {sum(r["gate_pass"] for r in rows)}/6 blocks pass');ax.grid(axis='y',alpha=.2);ax.margins(y=.35)
axes[0].set_ylabel('Paired ABBA elapsed-time change (%)')
fig.suptitle('ARM fresh baseline controls' if aa else 'ARM exact mask candidate — fresh primary comparison',fontsize=17,weight='bold')
note=('Same baseline binary in both slots; every block must be within ±1%.' if aa else 'Exact historical EXP-005 A; every block must improve at least 2%.')
fig.text(.5,.025,note+' 50M visits · CPU 2 · 16-byte members\n'+f'Gate: {data["decision"]}. Source selection: NONE. Evidence: {data["revision"]}.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.12,1,.93));out=p/'charts';out.mkdir(exist_ok=True)
for ext in ('png','svg'):fig.savefig(out/(phase+'.'+ext),dpi=180)
print(str(out/(phase+'.png')))
