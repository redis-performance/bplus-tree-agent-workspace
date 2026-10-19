from pathlib import Path
import json,math,itertools,hashlib
p=Path(__file__).parent;assert not (p/'timing-freeze.json').exists();m=json.loads((p/'calibration.json').read_text());assert m['status']=='complete' and json.loads((p/'calibration-audit.json').read_text())['status']=='pass';cells=[]
for history,width,encoding in itertools.product(['trim','resize'],[8,319,320,321,1024],[0,1,2]):
 r=[x for x in m['rows'] if (x['history'],x['bytes'],x['encoding'],x['kind'])==(history,width,encoding,'trial')];assert len(r)==9;minimum=min(x['row']['elapsed_ns']/x['passes'] for x in r);passes=math.ceil(200000000/minimum);assert 1<=passes<=10000000,'target cannot be reached at fixed cap';cells.append(dict(history=history,bytes=width,encoding=encoding,passes=passes,minimum_ns_per_pass=minimum))
(p/'pass-counts.json').write_text(json.dumps(cells,indent=2)+'\n')
for phase in ['aa','b']:
 schedule=[]
 for block in range(6):
  for c in (cells if block%2==0 else list(reversed(cells))):
   for step,label in enumerate('ABBA'):schedule.append(dict(history=c['history'],bytes=c['bytes'],encoding=c['encoding'],passes=c['passes'],seed=201+block%3,block=block,step=step,label=label,binary='B' if phase=='b' and label=='B' else 'base'))
 assert len(schedule)==720;(p/(phase+'-schedule.json')).write_text(json.dumps(schedule,indent=2)+'\n')
files=['PLAN.md','run-timing.py','audit.py','pass-counts.json','aa-schedule.json','b-schedule.json','build-freeze.json','import-freeze.json','calibration.json'];(p/'timing-freeze.json').write_text(json.dumps(dict(files={f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in files},fixed_phase_caps=dict(aa=480,b=480)),indent=2)+'\n');print('Frozen30 passcounts and720-process schedules; no further adaptation')
