"""Display all measured primary blocks and decisive guards without pooling frontends."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
d=json.loads((p/'FINAL-DECISION.json').read_text());primary=json.loads((p/'PRIMARY-REPLICATION-ROOT-AUDIT.json').read_text())
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','figure.facecolor':'#f7f9fc','axes.facecolor':'white'})
fig,(top,bot)=plt.subplots(2,1,figsize=(12,10),sharex=True,gridspec_kw={'height_ratios':[2,7]})
for ax in (top,bot):ax.axvline(0,color='#8994a4',lw=1);ax.grid(axis='x',alpha=.18);ax.set_xlim(-10,10)
for y,n in enumerate((100000,1000000)):
 vals=[float(x['effect_pct']) for x in primary['effects'] if x['size']==n]
 top.plot([min(vals),max(vals)],[y,y],color='#6f9f82',lw=1)
 top.scatter(vals,[y+(i-2.5)*.055 for i in range(6)],color='#20734c',s=34,zorder=3)
top.axvline(-2,color='#40815e',ls='--');top.set_yticks([0,1],['100K · forward integer','1M · forward integer']);top.invert_yaxis();top.margins(y=.5);top.set_title('Primary frontend · 50M visits · 1 warm-up',fontsize=13,pad=10)
labels=[]
for y,x in enumerate(d['rejected_qualified_cases']):
 f=x['fixture'];vals=[float(b['effect_pct']) for b in x['blocks']];bot.plot([min(vals),max(vals)],[y,y],color='#b58579',lw=1);bot.scatter(vals,[y+(i-2.5)*.055 for i in range(6)],color='#b44832',s=34,zorder=3)
 labels.append(f"{f['id']} · {'100K' if f['size']==100000 else '1M'} · {f['encoding']} · {f['direction']}")
bot.axvspan(1,10,color='#f9e9e5',alpha=.7);bot.axvline(1,color='#b44832',ls='--');bot.set_yticks(range(len(labels)),labels);bot.invert_yaxis();bot.margins(y=.08);bot.set_title('Qualified HARNESS-004 guards · 20M visits · 3 warm-ups\nAll nine score-only cases exceed +1% in every block',fontsize=13,pad=12)
bot.set_xlabel('Paired ABBA elapsed-time change (%) · negative is faster');bot.set_xticks(range(-10,11,2))
fig.suptitle('ARM mask candidate — REJECT / source NONE',fontsize=19,weight='bold',y=.98)
fig.text(.5,.025,'Each dot is one frozen block; different frontends are not pooled. Sign disagreement observed; cause unmeasured.\n'
         'Guards not shown: 30 qualified passes, 4 mixed, 39 unqualified — all retained in the raw audit.\n'
         'Primary 451456c2f · guards f30ac4330 · independent guard review d3cc358f2',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.11,1,.95));out=p/'charts'
for ext in ('png','svg'):fig.savefig(out/f'final-rejection.{ext}',dpi=180)
print(out/'final-rejection.png')
