"""Render each measured baseline/candidate without inferring missing slot levels."""
import json
from pathlib import Path
H=Path(__file__).resolve().parent
p=json.loads((H/'protocol.json').read_text());a=json.loads((H/'analysis.json').read_text())
rows={(r['cell'],r['variant']):r for r in a['configurations']}
labels={'base':'Baseline','itA':'Iterator A','itB':'Iterator B','scanB':'Scan B'}
metrics=[
 ('├── Frontend_Bound','Frontend_Bound'),
 ('│   ├── Fetch_Latency','Frontend_Bound.Fetch_Latency'),
 ('│   └── Fetch_Bandwidth','Frontend_Bound.Fetch_Bandwidth'),
 ('├── Bad_Speculation','Bad_Speculation'),
 ('│   ├── Branch_Mispredicts','Bad_Speculation.Branch_Mispredicts'),
 ('│   └── Machine_Clears','Bad_Speculation.Machine_Clears'),
 ('├── Backend_Bound','Backend_Bound'),
 ('│   ├── Memory_Bound','Backend_Bound.Memory_Bound'),
 ('│   └── Core_Bound','Backend_Bound.Core_Bound'),
 ('└── Retiring','Retiring'),
 ('    ├── Light_Operations','Retiring.Light_Operations'),
 ('    └── Heavy_Operations','Retiring.Heavy_Operations')]

for family in ['update','iterator','scan']:
 text=f'# {family.title()} — follow-up TMA\n\nSecondary Intel Sapphire Rapids, CPU2/NUMA0, sibling50 offline during capture.\nExact retained Clang18/O3 binaries, source37efd287f and original candidate patches.\nThree5s windows per build; means use all15 intervals. Diagnostic only, source NONE.\nThis new host/SMT condition is separate from earlier captures.\n\n'
 for c in [c for c in p['cells'] if c['family']==family]:
  text+='## '+c['id']+'\n\n```text\nPipeline Slots (100%)        '+''.join(f'{labels[v]:>14}' for v in c['variants'])+'\n'
  for label,key in metrics:
   vals=[]
   for v in c['variants']:
    r=rows.get((c['id'],v),{});m=r.get('slot_metrics_all_retained_windows',{}).get(key)
    vals.append(f"{m['mean']:.2f}%" if m and r.get('interpretation_qualified') else 'unavailable')
   text+=f'{label:<29}'+''.join(f'{x:>14}' for x in vals)+'\n'
  text+='```\n\n'
  for v in c['variants']:
   r=rows.get((c['id'],v),{});text+=f"- {labels[v]}: {r.get('l2_qualified_windows',0)}/3 windows qualify. [Capture records](results/{c['id']}-{v}.record.json).\n"
  text+='\n'
 text+='''## Interpretation limits

Ambient Parca remained running as disclosed in preflight; this is not proof of zero
shared-resource interference. CPU2/workload accounting passed the1% gate.

Four roots sum to100% within the preregistered tolerance; rounding and child-model
residuals are preserved. L1/L3/DRAM slot breakdown is unavailable: no qualified L3
capture. Memory Bound alone does not identify DRAM or a source instruction.

PEBS/LBR probes failed the scheduling-evidence gate; both were retained and deeper
captures skipped. Their samples do not support mechanism claims. No in-window
operation counts or acceptance timings: fractions cannot establish cycles/op or a
speedup. Updates evolve across windows; phase and raw interval order are retained.
Completed original/profile/sanitizer semantic checks are separate from profile loops,
which terminate after collection without a final completed-work checksum.

[Raw analysis](analysis.json) · [Assessment](ASSESSMENT.md) · [Probe gates](PROBE-GATES.json)
'''
 (H/(family.upper()+'.md')).write_text(text)
