"""Render per-family TMA trees without hiding unqualified captures."""
import collections,json,re
from pathlib import Path
H=Path(__file__).resolve().parent;D=H/'results'
a=json.loads((H/'analysis.json').read_text());p=json.loads((H/'protocol-v2.json').read_text())
rows={(r['cell'],r['variant']):r for r in a['configurations']}
labels={'base':'Baseline','itA':'Iterator A','itB':'Iterator B','scanB':'Scan B'}
metrics=[('├── Frontend_Bound','Frontend_Bound'),('├── Bad_Speculation','Bad_Speculation'),('├── Backend_Bound','Backend_Bound'),('│   ├── Memory_Bound','Backend_Bound.Memory_Bound'),('│   └── Core_Bound','Backend_Bound.Core_Bound'),('└── Retiring','Retiring')]
summary=[]
for family in ['iterator','scan','update']:
 text=f'# {family.title()} — measured profile assessment\n\nDiagnostic profiles, **source NONE**. No timing acceptance or per-operation counter\nclaim. Exact binary/commands/raw hashes/window order are in [analysis](analysis.json)\nand [raw records](results/). All retained windows enter the reported means; a\nconfiguration needs all three L2 windows to qualify for interpretation.\n\n'
 for c in [c for c in p['cells'] if c['family']==family]:
  variants=c['variants'];text+='## '+c['id']+'\n\n'
  text+='```text\nPipeline Slots (100%)        '+''.join(f'{labels[v]:>14}' for v in variants)+'\n'
  for label,key in metrics:
   values=[]
   for v in variants:
    r=rows[(c['id'],v)];m=r['slot_metrics_all_retained_windows'].get(key)
    values.append(f"{m['mean']:.2f}%" if m and r['interpretation_qualified'] else 'unavailable')
   text+=f'{label:<29}'+''.join(f'{x:>14}' for x in values)+'\n'
  text+='```\n\n'
  for v in variants:
   r=rows[(c['id'],v)]
   if not r['interpretation_qualified']:text+=f"{labels[v]} TMA is unavailable for interpretation: {r['l2_qualified_windows']}/3 windows qualify; failed scope/quality evidence and all numeric observations remain in analysis.json.\n\n"
  text+='| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |\n|---|---:|---:|---:|---|\n'
  for v in variants:
   r=rows[(c['id'],v)];tag=c['id']+'-'+v;counter=r.get('counters',{});symbols=[]
   f=D/(tag+'-symbols.stdout')
   if f.exists():
    for line in f.read_text().splitlines():
     match=re.match(r'\s*([\d.]+)%\s+\[.\]\s+(\S+)\s+',line)
     if match:symbols.append({'share_percent':float(match[1]),'symbol':match[2]})
   top=', '.join(f"{s['symbol']} {s['share_percent']:.1f}%" for s in symbols[:3]) or 'unavailable'
   if not r['samples']['qualified']:top='unavailable (sample scope/collection failed)'
   ipc=f"{counter['ipc']:.2f}" if counter.get('qualified') and counter.get('ipc') is not None else 'unavailable'
   freq=f"{counter['cycles_per_reference_cycle']:.3f}" if counter.get('qualified') and counter.get('cycles_per_reference_cycle') is not None else 'unavailable'
   text+=f"| [{labels[v]}](results/{tag}.record.json) | {r['l2_qualified_windows']}/3 | {ipc} | {freq} | {top} |\n"
   summary.append({'cell':c['id'],'variant':v,'qualified':r['interpretation_qualified'],'sample_scope_qualified':r['samples']['qualified'],'sampled_symbols':symbols})
  text+='\n'
 text+='[Next experiment and missing evidence](ASSESSMENT.md).\n\n'
 text+='''## Collection limits

Topdown71dea5e / pmu-tools2026.4.7.0, Intel Sapphire Rapids profiler, CPU2/NUMA0,
sibling50 online; Clang18/O3, source37efd287f and exact retained patches. See
[protocol](protocol-v2.json) and [build identities](results/build-sha256.json).
Each L2 mean uses15 one-second intervals when complete. L1 shares sum approximately
100%; displayed rounding and child-model residuals are retained, not rescaled.

L3 data are retained separately. Mixed `% Stalls`, `% Clocks`, `% Uops` and estimated
slot units are not a partition of total pipeline slots. Low scheduling prevents
reliable deeper causal attribution; cache/DRAM slot shares remain unavailable unless
separately qualified. IPC and cycles/reference-cycle are interval ratios, not speedups
or cycles per operation. Samples cover user-mode cycles for the workload PID; sample
shares exclude kernel execution and are not TMA slot shares.

Each workload starts after construction/oracle/warmup readiness. Profile loops terminate
after capture; their final completed-work checksum is uncollected. Completed original,
diagnostic and sanitizer semantic checks are separate evidence. Update workloads
mutate state throughout successive windows; no stationary-state assumption is made.
[Per-window means and elapsed phases](window-phases.json) retain the ordered observations.
Existing timing failures and old-source rejections remain unchanged.
'''
 (H/(family.upper()+'.md')).write_text(text)
(H/'hotspots.json').write_text(json.dumps(summary,indent=2)+'\n')
print('Rendered iterator, scan and update TMA reports')
