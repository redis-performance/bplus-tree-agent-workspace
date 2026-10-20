"""Add TMA supplements without rewriting sealed historical evidence."""
import collections, hashlib, json, os
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
records=json.loads((ROOT/'experiments/EXPERIMENT-FLOWS-20261020/experiments.json').read_text())['records']
groups=collections.defaultdict(list)
for r in records:
 source=ROOT/r['source']
 assert hashlib.sha256(source.read_bytes()).hexdigest()==r['source_sha256'],r['id']
 groups[source.parent].append(r)
coverage=[]
for folder,rs in groups.items():
 text='# TMA classification\n\nSupplement added 20 October 2026; historical decisions and raw evidence are unchanged.\n\n'
 for r in rs:
  source=ROOT/r['source'];anchor=r['id'].lower()
  text+=f"## {r['id']} — {r['host']}\n\n"
  text+=f"[Historical report]({os.path.relpath(source,folder)}): **{r['status']}**.\n\n"
  text+='```text\nPipeline Slots (100%) — historical baseline / candidates\n├── Frontend_Bound     unavailable\n├── Bad_Speculation    unavailable\n├── Backend_Bound      unavailable\n│   ├── Memory_Bound   unavailable\n│   └── Core_Bound     unavailable\n└── Retiring           unavailable\n```\n\n'
  if r['host'].startswith('Apple'):
   reason='No compatible slot-classification capture is retained for this Apple experiment. Linux Intel/Neoverse measurements cannot fill these values.'
  else:
   reason='No matching TMA slot capture is retained for this historical experiment. Timing, instruction counts and sampled hotspot shares do not supply this classification.'
  text+=reason+' Collect matched baseline/candidate counters on the stated architecture before assigning a TMA mechanism.\n\n'
  if r['id']=='INTEL-ITERATOR':
   report=os.path.relpath(HERE/'README.md',folder)
   text+=f'**New baseline diagnostic, 20 October:** [measured Intel L2 trees]({report}#tma-classification). Different profiling runner/build; these values do not retroactively classify the historical B candidate.\n\n'
  coverage.append({'id':r['id'],'architecture':r['architecture'],'host':r['host'],'status':'historical TMA unavailable',
                   'report':r['source'],'supplement':str((folder/'TMA.md').relative_to(ROOT)),
                   'historical_sha256_verified':r['source_sha256']})
 (folder/'TMA.md').write_text(text.rstrip()+'\n')
index='# TMA coverage by experiment\n\nEvery one of the 33 recorded attempts has a TMA classification supplement below.\nHistorical counters are **unavailable**, not zero. Original reports and seals remain unchanged.\n\n**Fresh measured data:** [Intel iterator baseline, 100K and 1M](TOPDOWN-ASSESSMENT-20261020/README.md#tma-classification), 12 captures / 120 seconds; no candidate comparison.\n\n| Architecture | Experiment | Host | TMA classification |\n|---|---|---|---|\n'
for c in sorted(coverage,key=lambda x:(x['architecture'],x['id'])):
 index+=f"| {c['architecture']} | {c['id']} | {c['host']} | [Unavailable — reason and collection needed]({os.path.relpath(ROOT/c['supplement'],ROOT/'experiments')}) |\n"
index+='\n[Required report format](../docs/TMA-REPORTING.md). Future reports embed the tree directly.\n'
(ROOT/'experiments/TMA-COVERAGE.md').write_text(index)
(HERE/'tma-coverage.json').write_text(json.dumps({'attempts':len(coverage),'supplements':len(groups),'records':coverage},indent=2)+'\n')
assert len(coverage)==33
print(json.dumps({'attempts':len(coverage),'supplements':len(groups),'historical_source_hashes_verified':len(records)}))
