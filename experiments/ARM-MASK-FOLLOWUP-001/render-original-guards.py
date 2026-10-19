"""Plot all six blocks of each qualified original guard; do not pool or rescue medians."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
data=json.loads((root/'ORIGINAL-COMPARISON-ROOT-AUDIT.json').read_text())
cells=[c for c in data['cells'] if c['qualified']]
cells.sort(key=lambda c:(c['size'],c['case']))
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','figure.facecolor':'#f7f9fc','axes.facecolor':'white'})
fig,ax=plt.subplots(figsize=(11,9))
ax.axvspan(-1,1,color='#e0f1e7');ax.axvline(0,color='#8d98a8',lw=1);ax.axvline(1,color='#b94d32',ls='--')
for y,c in enumerate(cells):
 values=[float(b['effect_pct']) for b in c['blocks']]
 ax.plot([min(values),max(values)],[y,y],color='#9ba7b8',lw=1,zorder=2)
 ax.scatter(values,[y+(i-2.5)*.055 for i in range(6)],c=['#b94d32' if v>1 else '#25704e' for v in values],s=28,zorder=3)
ax.set_yticks(range(len(cells)),[f"{c['size']:,} · {c['case']}" for c in cells]);ax.invert_yaxis()
ax.set_xlabel('Paired ABBA elapsed-time change (%) · negative is faster');ax.grid(axis='x',alpha=.18)
ax.set_title('ARM mask candidate — qualified original-operation guards\n17 pass; 100-member SCAN mixed → PARK',fontsize=16,pad=18)
fig.text(.5,.025,'Each dot is one frozen block; all six retained. +1% is the guard-loss threshold.\n'
         '11 noisy required cells + 11 short diagnostics excluded from this calibrated plot, retained in raw evidence.\n'
         f"No source adoption. Comparison {data['revision']}; controls 1329e440a.",ha='center',fontsize=10)
fig.tight_layout(rect=(0,.10,1,1));out=root/'charts'
for ext in ['png','svg']:fig.savefig(out/f'original-qualified-guards.{ext}',dpi=180)
print(out/'original-qualified-guards.png')
