from pathlib import Path
import csv,datetime,hashlib,json,statistics
p=Path(__file__).parent;m=json.loads((p/'aa.json').read_text());rows=m['rows'];expected=[]
for block in range(6):
 for size in ([100000,1000000] if block%2==0 else [1000000,100000]):
  for position in range(4):expected.append((size,101+block%3,block,position))
assert len(rows)<=48;last=None
for i,r in enumerate(rows):
 assert (r['size'],r['seed'],r['block'],r['position'])==expected[i]
 raw=list(csv.DictReader((p/'raw'/f'aa-{i:03d}.stdout').open()));assert raw==[r['row']]
 assert r['row']['cpu_start']==r['row']['cpu_end']=='2'
 assert r['row']['case']=='scan' and r['row']['requested_ops']=='5000000' and r['row']['member_bytes']=='16'
 start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert start<=end
 if last is not None:assert last<=start
 last=end
effects=[]
for i in range(0,len(rows)-3,4):
 r=rows[i:i+4];assert len({(x['row']['checksum'],x['row']['operations'],x['row']['tree_bytes']) for x in r})==1
 v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in r];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);minimum=min(int(x['row']['elapsed_ns']) for x in r)
 effects.append(dict(size=r[0]['size'],seed=r[0]['seed'],block=r[0]['block'],percent=effect,min_window_ns=minimum,qualified=abs(effect)<=1 and minimum>=10000000))
if m['status']=='complete':assert len(rows)==48 and effects==m['effects']
summary=[]
for size in [100000,1000000]:
 group=[x for x in effects if x['size']==size];values=[x['percent'] for x in group]
 if group:summary.append(dict(size=size,blocks=len(group),minimum=min(values),maximum=max(values),median=statistics.median(values),min_window_ns=min(x['min_window_ns'] for x in group),qualified=len(group)==6 and all(x['qualified'] for x in group),effects=values))
freeze=json.loads((p/'comparison-freeze.json').read_text());assert hashlib.sha256((p/'run-aa.py').read_bytes()).hexdigest()==freeze['aa_driver_sha256']
result=dict(status='pass',phase_status=m['status'],raw_rows=len(rows),complete_blocks=len(effects),partial_rows=len(rows)%4,serial_windows=True,fixture_identity=True,owned_bytes_equal=True,schedule_prefix_exact=True,summary=summary)
(p/'aa-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
