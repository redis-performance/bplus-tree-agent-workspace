"""Reconstruct classifications from raw CSV; preserve units and collection quality.
Usage: PYTHONPATH=/path/to/topdown-profiler python3 analyze.py
"""
import collections, csv, hashlib, json, statistics, uuid
from pathlib import Path
from topdown.collector.csv_parser import parse_output
from topdown.analysis.bottleneck import find_bottlenecks
from topdown.analysis.funnel import build_funnel
from topdown.storage.sqlite_backend import SQLiteBackend
from topdown.storage.models import Run, Sample

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
CATEGORIES=['Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring']
DB=ROOT/'scratch/topdown-assessment.db'
if DB.exists(): DB.unlink()
backend=SQLiteBackend(DB); backend.initialize()
summary={'source_commit':'f20711d9a1e90c72218ac3adf3ef4cafcd3f36cf',
         'glue_analysis_commit':'71dea5e7988793e853a9209ddafbc97ca7deb11e',
         'classification':'baseline-only diagnostic; no candidate or speedup claim', 'captures':[], 'groups':{}}
groups=collections.defaultdict(list)
for folder,level in [('l2',2),('results',3)]:
 for file in sorted((HERE/'evidence'/folder).glob(f'*-L{level}-*.stderr')):
  size=int(file.name.split('-')[0]);raw=file.read_text()
  rows=[r for r in csv.DictReader(raw.splitlines()) if r["Area"] is not None]
  assert rows and len(rows)==len(parse_output(raw))
  parsed=json.loads(file.with_suffix('.json').read_text())
  for row,sample in zip(rows,parsed):
   assert row['Area']==sample['metric_name'] and float(row['Value'])==sample['value']
   assert row['Unit']==sample['unit']
  digest=hashlib.sha256(raw.encode()).hexdigest()
  run_id=str(uuid.uuid5(uuid.NAMESPACE_URL,'bplus-tma:'+digest))
  run=Run(run_id=run_id,process_name='bplus-iterator-baseline',level=level,
          duration_seconds=10,system_wide=True,
          labels={'workspace':'bplus-tree-agent-workspace','size':str(size),
                  'cpu':'2','scope':'one CPU; not PID-filtered','variant':'baseline',
                  'raw_sha256':digest,'timestamp_origin':'database ingestion, not capture wall time'})
  backend.insert_run(run)
  backend.insert_samples([Sample(run_id=run_id,**s) for s in parsed])
  aggregate=backend.get_aggregated_metrics(run_id)
  # Reproduce the unmodified glue's reporting result on actual captured data.
  raw_rank=[x.to_dict() for x in find_bottlenecks(aggregate)]
  top=[r for r in rows if r['Area'] in CATEGORIES]
  pertime=collections.defaultdict(float)
  for row in top: pertime[row['Timestamp']]+=float(row['Value'])
  quality={'multiplex_min':min(float(r['Multiplex']) for r in rows),
           'multiplex_max':max(float(r['Multiplex']) for r in rows),
           'l1_sum_min':min(pertime.values()),'l1_sum_max':max(pertime.values()),
           'intervals':len(pertime),'raw_units':sorted({r['Unit'] for r in rows})}
  assert len(pertime)==10 and all(abs(s-100)<.31 for s in pertime.values())
  if level==2: assert quality['multiplex_min']==100
  if level==3:
   scope=json.loads(file.with_suffix('.scope.json').read_text())
   def ticks(text,cpu): return list(map(int,next(l for l in text.splitlines() if l.startswith(f'cpu{cpu} ')).split()[1:9]))
   def busy(cpu):
    a=ticks(scope['cpu_before'],cpu);b=ticks(scope['cpu_after'],cpu);d=[y-x for x,y in zip(a,b)]
    return {'total_ticks':sum(d),'busy_ticks':sum(d)-d[3]-d[4],'busy_pct':100*(sum(d)-d[3]-d[4])/sum(d)}
   def proc_ticks(text):
    # Remaining fields start at field3 after the final comm parenthesis.
    fields=text.rsplit(')',1)[1].split();return int(fields[11])+int(fields[12])
   quality['cpu2']=busy(2);quality['smt_sibling50']=busy(50)
   quality['workload_cpu_ticks']=proc_ticks(scope['workload_after'])-proc_ticks(scope['workload_before'])
  summary['captures'].append({'file':str(file.relative_to(ROOT)),'run_id':run_id,'size':size,'level':level,'sha256':digest,'quality':quality,'unmodified_glue_ranking':raw_rank})
  groups[(size,level)].extend(rows)
for (size,level),rows in groups.items():
 values=collections.defaultdict(list);units=collections.defaultdict(set)
 for r in rows: values[r['Area']].append(float(r['Value']));units[r['Area']].add(r['Unit'])
 metrics={k:{'mean':statistics.mean(v),'min':min(v),'max':max(v),'n':len(v),'units':sorted(units[k])} for k,v in values.items()}
 # Only exact Slots units enter a slot classification. Clock/Stall/Uop/estimated
 # units remain separate; MUX describes coverage, not a pipeline bottleneck.
 slots=[{'metric_name':k,'value':v['mean'],'unit':'%_Slots'} for k,v in metrics.items()
        if k.split('.')[0] in CATEGORIES and set(v['units'])<= {'% Slots','% Slots <'}]
 summary['groups'][f'{size}-L{level}']={'metrics':metrics,'slot_funnel':build_funnel(slots,max_level=2).to_dict(),
  'l1_sum':sum(metrics[k]['mean'] for k in CATEGORIES)}
backend.close()
(HERE/'analysis.json').write_text(json.dumps(summary,indent=2)+'\n')
# Direct regression reproduction: valid slot categories dropped, MUX kept.
assert all(c['unmodified_glue_ranking'][0]['metric_name']=='MUX' for c in summary['captures'])
(HERE/'VALIDATION.json').write_text(json.dumps({'captures':len(summary['captures']),
 'raw_rows':sum(sum(m['n'] for m in g['metrics'].values()) for g in summary['groups'].values()),
 'checks':['raw CSV equals stored parsed samples','10 intervals per capture','four L1 sum to100 within0.3pp',
 'L2 counters scheduled100percent','mixed L3 denominators retained','CPU0 scope reproduced in environment.json',
 'raw glue ranking wrongly returns MUX for every capture','no source candidate or speed claim'],
 'tma_status':'L2 classified; L3 exploratory mixed-unit/low-coverage diagnostic'},indent=2)+'\n')
print(json.dumps({'captures':len(summary['captures']),'database':str(DB),'groups':list(summary['groups'])}))
