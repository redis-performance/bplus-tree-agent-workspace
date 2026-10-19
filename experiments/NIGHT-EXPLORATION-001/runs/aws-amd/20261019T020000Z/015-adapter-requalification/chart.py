#!/usr/bin/env python3
"""Standalone chart for only the corrected-adapter AMD baseline; no comparison."""
import argparse,json,pathlib,hashlib
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);a=p.parse_args();root=a.results;summary=json.loads((root/'summary.json').read_text());audit=json.loads((root/'independent-audit.json').read_text());manifest=json.loads((root/'manifest.json').read_text());assert manifest['commit'].startswith('13e459ff8');assert len(summary)==40
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','svg.hashsalt':'amd-corrected-adapter-13e459ff8'})
bykey={(x['size'],x['case']):x for x in audit['cells_detail']};sizes=[100,1000,10000,100000,1000000];cases=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete'];fig,axes=plt.subplots(2,4,figsize=(14,7.8));fig.subplots_adjust(top=.82,bottom=.16,hspace=.55,wspace=.33)
for ax,case in zip(axes.flat,cases):
 rows=[next(r for r in summary if r['case']==case and r['size']==n) for n in sizes];values=[r['median_ns_op'] for r in rows]
 ax.errorbar(range(5),values,yerr=[[r['median_ns_op']-r['min_ns_op'] for r in rows],[r['max_ns_op']-r['median_ns_op'] for r in rows]],color='#2563eb',capsize=3,linewidth=1.5)
 for i,(n,v) in enumerate(zip(sizes,values)):
  good=bykey[(n,case)]['qualified'];ax.plot(i,v,'o',markersize=6,markerfacecolor='#2563eb' if good else 'white',markeredgecolor='#2563eb' if good else '#b45309',markeredgewidth=1.6)
 ax.set_xticks(range(5),['100','1K','10K','100K','1M']);ax.set_ylim(bottom=0);ax.set_title(case);ax.set_xlabel('Members');ax.set_ylabel('Batch-average ns/op');ax.grid(axis='y',alpha=.2)
fig.suptitle('AWS AMD · corrected _Noreturn adapter baseline\n13e459ff8 · 16-byte members · CPU2 · 24 observations per cell',fontsize=15)
fig.legend(handles=[Line2D([0],[0],marker='o',color='none',markerfacecolor='#2563eb',markeredgecolor='#2563eb',label='A/A qualified'),Line2D([0],[0],marker='o',color='none',markerfacecolor='white',markeredgecolor='#b45309',label='Short window or noisy A/A; unqualified')],loc='lower center',bbox_to_anchor=(.5,.055),ncol=2,frameon=False)
fig.text(.5,.015,'Median and observed min–max, not latency percentiles or confidence intervals. Each panel has its own y-axis. No speedup comparison.',ha='center',fontsize=9)
for suffix in ['png','svg']:fig.savefig(root/('corrected-adapter-baseline.'+suffix),dpi=150,metadata={'Date':None} if suffix=='svg' else {})
plt.close(fig)
svg=root/'corrected-adapter-baseline.svg';svg.write_text('\n'.join(x.rstrip() for x in svg.read_text().splitlines())+'\n')
files=['manifest.json','operational-provenance.json','summary.json','independent-audit.json','corrected-adapter-baseline.png','corrected-adapter-baseline.svg'];(root/'chart-manifest.json').write_text(json.dumps({'identity':'AWS AMD corrected _Noreturn adapter baseline','commit':manifest['commit'],'binary_sha256':manifest['binary_sha256'],'compiler':manifest['compiler'],'scope':'Standalone original eight operations; no old/new or cross-host comparison','sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in files},'qualified_cells':audit['qualified_cells'],'total_cells':40},indent=2)+'\n')
