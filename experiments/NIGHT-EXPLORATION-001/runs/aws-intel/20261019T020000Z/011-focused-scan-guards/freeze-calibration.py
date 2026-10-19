from pathlib import Path
import json,itertools,math,hashlib,datetime
p=Path(__file__).parent;m=json.loads((p/'calibration.json').read_text());assert m['status']=='complete' and len(m['rows'])==324;counts=[];cells=list(itertools.product([4096,100000],[16,321],[0,1,2],[0,1,2]))
for n,b,order,dist in cells:
 rows=[r for r in m['rows'] if (r['n'],r['bytes'],r['order'],r['distribution'])==(n,b,order,dist)];assert len(rows)==9;minimum=min(r['row']['elapsed_ns'] for r in rows);assert minimum>0;requested=math.ceil(200000000/minimum);passes=min(100000,max(1,requested));counts.append(dict(n=n,bytes=b,order=order,distribution=dist,minimum_elapsed_ns=minimum,passes=passes,cap_sufficient=requested<=100000))
(p/'pass-counts.json').write_text(json.dumps(counts,indent=2)+'\n')
for phase in ['aa','b']:
 schedule=[]
 for block in range(6):
  ordered=counts if block%2==0 else list(reversed(counts))
  for cell in ordered:
   for position in range(4):schedule.append({k:cell[k] for k in ['n','bytes','order','distribution','passes']}|dict(index=len(schedule),block=block,seed=101+block%3,position=position,binary='B' if phase=='b' and position in [1,2] else 'base'))
 assert len(schedule)==864;(p/(phase+'-schedule.json')).write_text(json.dumps(schedule,indent=2)+'\n')
files=['run-timing.py','pass-counts.json','calibration.json','aa-schedule.json','b-schedule.json','build-freeze.json','fixture-manifest.json','PLAN.md']
(p/'timing-freeze.json').write_text(json.dumps(dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files={f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in files},phase_budgets_seconds={'aa':900,'b':900},floor_ns=100000000),indent=2)+'\n');print('Frozen36 pass counts and both864-row schedules; no adaptive duration after this freeze')
