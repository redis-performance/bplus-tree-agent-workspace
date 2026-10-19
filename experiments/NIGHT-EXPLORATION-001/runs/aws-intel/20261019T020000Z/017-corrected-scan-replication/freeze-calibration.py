from pathlib import Path
import json,math,hashlib
P=Path(__file__).parent;assert not (P/'guard-timing-freeze.json').exists();m=json.loads((P/'calibration.json').read_text());audit=json.loads((P/'calibration-audit.json').read_text());assert m['status']=='complete' and audit['status']=='pass' and audit['phase_status']=='complete';trials=[x for x in m['rows'] if x['kind']=='trial'];assert len(trials)==9;minimum=min(x['row']['elapsed_ns']/x['passes'] for x in trials);passes=math.ceil(200000000/minimum);assert 1<=passes<=10000000
(P/'pass-count.json').write_text(json.dumps(dict(passes=passes,target_ns=200000000,qualification_floor_ns=100000000,minimum_ns_per_pass=minimum,trial_rows=9,seeds=[701,702,703]),indent=2)+'\n')
for phase in ['guard-aa','guard-b']:
 rows=json.loads((P/(phase+'-schedule-template.json')).read_text());assert len(rows)==24
 for x in rows:assert isinstance(x['passes'],str);x['passes']=passes
 (P/(phase+'-schedule.json')).write_text(json.dumps(rows,indent=2)+'\n')
files=['pass-count.json','guard-aa-schedule.json','guard-b-schedule.json','calibration.json','calibration-audit.json','build-freeze.json','execution-freeze.json'];(P/'guard-timing-freeze.json').write_text(json.dumps(dict(files={f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in files}),indent=2)+'\n');print('FROZEN known-guard count',passes)
