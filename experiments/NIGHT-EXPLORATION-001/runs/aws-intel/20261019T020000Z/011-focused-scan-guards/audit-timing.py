from pathlib import Path
import json,hashlib,datetime,itertools,statistics,sys
p=Path(__file__).parent;phase=sys.argv[1];assert phase in ['calibration','aa','b'];m=json.loads((p/(phase+'.json')).read_text());schedule=json.loads((p/(phase+'-schedule.json')).read_text());rows=m['rows'];last=None
assert len(rows)<=len(schedule)
for i,r in enumerate(rows):
 assert all(r[k]==v for k,v in schedule[i].items());assert json.loads((p/'raw'/f'{phase}-{i:04d}.stdout').read_text())==r['row'];x=r['row'];assert x['start_cpu']==x['end_cpu']==2 and x['validation']=='pass'
 for k in ['n','bytes','seed','distribution','order','passes']:assert x[k]==r[k]
 t=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert t<=end
 if last is not None:assert last<=t
 last=end
if m['status']=='complete':assert len(rows)==len(schedule)
fields=['n','bytes','seed','distribution','order','passes','logical_members','callbacks_per_pass','checksum_per_pass','tree_bytes'];effects=[];summary=[]
if phase=='calibration':
 for i in range(0,len(rows)-2,3):
  group=[x['row'] for x in rows[i:i+3]];assert all(all(y[k]==group[0][k] for k in fields) for y in group)
if phase!='calibration':
 freeze=json.loads((p/'timing-freeze.json').read_text())
 for f,h in freeze['files'].items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
 for i in range(0,len(rows)-3,4):
  group=rows[i:i+4];r=[x['row'] for x in group];assert all(all(y[k]==r[0][k] for k in fields) for y in r)
  v=[x['elapsed_ns']/(x['passes']*x['callbacks_per_pass']) for x in r];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);minimum=min(x['elapsed_ns'] for x in r)
  effects.append({k:group[0][k] for k in ['n','bytes','order','distribution','block','seed']}|dict(percent=effect,min_window_ns=minimum,passes=(abs(effect)<=1 if phase=='aa' else effect<=1) and minimum>=100000000))
 for n,b,order,dist in itertools.product([4096,100000],[16,321],[0,1,2],[0,1,2]):
  group=[x for x in effects if (x['n'],x['bytes'],x['order'],x['distribution'])==(n,b,order,dist)];v=[x['percent'] for x in group]
  if group:summary.append(dict(n=n,bytes=b,order=order,distribution=dist,blocks=len(group),median=statistics.median(v),minimum=min(v),maximum=max(v),min_window_ns=min(x['min_window_ns'] for x in group),passes=len(group)==6 and all(x['passes'] for x in group),effects=v))
 if phase=='b':
  aa=json.loads((p/'aa-audit.json').read_text());controls={(x['n'],x['bytes'],x['order'],x['distribution']):x for x in aa['summary']}
  for x in summary:x['baseline_qualified']=controls[(x['n'],x['bytes'],x['order'],x['distribution'])]['passes']
result=dict(status='pass',phase_status=m['status'],raw_rows=len(rows),planned_rows=len(schedule),serial=True,schedule_prefix_exact=True,fixture_identity=True,owned_bytes_equal=True,effects=effects,summary=summary)
(p/(phase+'-audit.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['summary','effects']},indent=2))
