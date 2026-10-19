#!/usr/bin/env python3
"""Render retained baseline A/A evidence only. Run: uv run --offline --with matplotlib python experiments/EXP-009/plot-aa.py"""
from pathlib import Path
import hashlib,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
ROOT=Path.cwd();E=Path(__file__).resolve().parent;SOURCE=E/'bench-results/aa/summary.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source_sha=sha(SOURCE);data=json.loads(SOURCE.read_text());rows=data['rows'];assert len(rows)==48
cells=[]
for size in [100000,1000000]:
    blocks=[]
    for block in range(6):
        q=sorted([r for r in rows if r['size']==size and r['block']==block],key=lambda r:r['position'])
        assert len(q)==4 and [r['side'] for r in q]==list('ABBA') and [r['position'] for r in q]==list(range(4))
        assert all(r['fingerprint']==q[0]['fingerprint'] for r in q)
        A=q[0]['elapsed_ns']+q[3]['elapsed_ns'];B=q[1]['elapsed_ns']+q[2]['elapsed_ns'];minimum=min(r['elapsed_ns'] for r in q)
        qualified=abs(B-A)*100<=A and minimum>=10000000;effect=100*(B-A)/A
        original=next(x for x in data['blocks'] if x['size']==size and x['block']==block)
        assert original['baseline_elapsed_sum']==A and original['paired_elapsed_sum']==B and original['qualified'] is qualified
        assert math.isclose(original['effect_percent_display_only'],effect,abs_tol=1e-13)
        blocks.append({'block':block,'seed':q[0]['seed'],'baseline_elapsed_sum':A,'paired_elapsed_sum':B,'effect_percent_display_only':effect,'qualified_exact_integer_gate':qualified,'minimum_elapsed_ns':minimum,'row_indices':[r['index'] for r in q]})
    subset=[r for r in rows if r['size']==size]
    cells.append({'size':size,'blocks':blocks,'qualified_blocks':sum(x['qualified_exact_integer_gate'] for x in blocks),'total_blocks':6,'all_windows_min_ns':min(r['elapsed_ns'] for r in subset),'all_windows_max_ns':max(r['elapsed_ns'] for r in subset),'operations_per_window':sorted({r['operations'] for r in subset})})
assert [c['qualified_blocks'] for c in cells]==[6,3]
provenance={str(SOURCE.relative_to(ROOT)):source_sha}
for name in ['PLAN.json','driver.py','bench-results/aa/status.json','timing-manifest.json']:
    path=E/name
    if path.is_file():provenance[str(path.relative_to(ROOT))]=sha(path)
metadata={'scope':'Baseline same-binary A/A only; no candidate comparison or gain claim','decision':'PARK: 1M fails3 of6 preregistered blocks; no source proposal/implementation advancement','primary_case':'public successful score lookup,16-byte members','method':'6 fixed ABBA blocks per size,seeds1/2/3 twice; calibration target600ms; all48 original rows retained','gate':'abs(Bsum-Asum)*100<=Asum AND each elapsed_ns>=10000000; equal operations and exact output/memory fingerprint','effect':'100*(Bsum-Asum)/Asum for display; negative means less elapsed in the inner pair of identical-binary processes','range':'Observed window bounds, not uncertainty intervals or individual-query percentiles','sampled_cycles_claim':False,'source_provenance_sha256':provenance,'plot_script_sha256':sha(__file__),'matplotlib_version':matplotlib.__version__,'reproduce':'uv run --offline --with matplotlib python experiments/EXP-009/plot-aa.py','cells':cells,'all48_windows_min_ns':min(r['elapsed_ns'] for r in rows),'all48_windows_max_ns':max(r['elapsed_ns'] for r in rows),'all48_windows_at_least_10ms':all(r['elapsed_ns']>=10000000 for r in rows),'retained_rows':rows,'participant':'/root/followup_proposal_b','backend':'Codex/GPT-6 family; exact serving model/token/currency costs unknown'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False,'svg.hashsalt':'EXP009-AA-fixed-controls'})
fig,axes=plt.subplots(1,2,figsize=(14.2,8.2),sharey=True)
fig.patch.set_facecolor('white');fig.subplots_adjust(top=.75,bottom=.25,left=.085,right=.97,wspace=.10)
fig.text(.085,.945,'EXP-009 · M6 baseline repeatability',fontsize=25,fontweight='bold',color='#172f44')
fig.text(.085,.893,'PARK  ·  1M fails 3 of 6 A/A blocks',fontsize=19,fontweight='bold',color='#a33b2b')
fig.text(.085,.847,'Successful score lookup · 16-byte members · same binary in all four ABBA positions',fontsize=12.5,color='#42566b')
PASS='#117c75';FAIL='#bd4433';BAND='#e6f3ef';GRID='#dce3e9'
for ax,cell in zip(axes,cells):
    label='100K' if cell['size']==100000 else '1M';passed=cell['qualified_blocks'];color=PASS if passed==6 else FAIL
    ax.set_title(f'{label} members   {passed}/6 blocks qualify',loc='left',fontsize=16,fontweight='bold',pad=17,color=color)
    ax.axhspan(-1,1,color=BAND,zorder=0)
    for bound in [-1,1]:ax.axhline(bound,color='#64a58c',linestyle=(0,(4,3)),linewidth=1.3,zorder=1)
    ax.axhline(0,color='#718393',linewidth=1,zorder=1)
    ax.set_axisbelow(True);ax.yaxis.grid(True,color=GRID,linewidth=.6)
    for item in cell['blocks']:
        x=item['block']+1;y=item['effect_percent_display_only'];ok=item['qualified_exact_integer_gate']
        ax.scatter(x,y,s=95 if ok else 135,marker='o' if ok else 'X',color=PASS if ok else FAIL,edgecolors='white',linewidths=1.1,zorder=4)
        ax.annotate(f'{y:+.3f}%',(x,y),xytext=(0,13 if y>=0 else -20),textcoords='offset points',ha='center',fontsize=11.5,fontweight='bold' if not ok else 'normal',color=PASS if ok else FAIL)
    ax.set_xticks(range(1,7),[f'{i+1}\nseed {i%3+1}' for i in range(6)]);ax.set_xlim(.45,6.55);ax.set_ylim(-1.95,3.25)
    ax.tick_params(axis='x',length=0,pad=8)
    bounds=f"Observed windows: {cell['all_windows_min_ns']/1e6:.3f}–{cell['all_windows_max_ns']/1e6:.3f} ms"
    count=cell['operations_per_window'];assert len(count)==1
    ax.text(0,-.235,bounds+'\n'+f'{count[0]:,} queries per window · target 600 ms',transform=ax.transAxes,fontsize=11.5,color='#42566b',linespacing=1.65)
axes[0].set_ylabel('Inner-pair elapsed difference from outer pair (%)',labelpad=12)
axes[0].text(.66,.935,'Qualification band ±1%',transform=axes[0].transAxes,color='#477965',fontsize=10.5,ha='center')
fig.legend(handles=[Line2D([0],[0],marker='o',linestyle='None',markersize=8,color=PASS,label='Qualified A/A block'),Line2D([0],[0],marker='X',linestyle='None',markersize=9,color=FAIL,label='Failed A/A block')],loc='lower left',bbox_to_anchor=(.077,.055),frameon=False,ncol=2,fontsize=11.5)
fig.text(.085,.025,'48/48 windows exceed 10 ms. Points are observed block effects; no candidate comparison is shown.',fontsize=11.5,color='#42566b')
fig.savefig(E/'aa-controls.png',dpi=180,facecolor='white',metadata={'Title':'EXP-009 baseline A/A controls','Description':'Same-binary baseline controls; PARK; no candidate speedup claim'})
fig.savefig(E/'aa-controls.svg',facecolor='white',metadata={'Title':'EXP-009 baseline A/A controls','Date':None,'Description':'Same-binary baseline controls; PARK; no candidate speedup claim'})
plt.close(fig)
assert sha(SOURCE)==source_sha,'input changed during render'
metadata['artifact_sha256']={name:sha(E/name) for name in ['aa-controls.png','aa-controls.svg']}
(E/'aa-controls.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps({'status':'rendered baseline A/A evidence','input_sha256':source_sha,'qualified_blocks':[c['qualified_blocks'] for c in cells],'window_min_ms':metadata['all48_windows_min_ns']/1e6,'window_max_ms':metadata['all48_windows_max_ns']/1e6,'files':['aa-controls.png','aa-controls.svg','aa-controls.json']}))
