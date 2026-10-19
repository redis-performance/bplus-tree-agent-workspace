import csv,hashlib,json,sys,statistics
from pathlib import Path
p=Path(__file__).resolve().parent;out=p/sys.argv[1];m=json.load(open(out/'manifest.json'));assert m['status']=='complete'
previous=0;results=[]
for row in m['rows']:
 assert row['returncode']==0 and row['started']>=previous;previous=row['finished']
 raw=(out/'raw'/(row['name']+'.csv')).read_bytes();assert hashlib.sha256(raw).hexdigest()==row['csv_sha256']
 r=list(csv.DictReader(raw.decode().splitlines()))[0];assert r==row['result'];assert r['cpu_start']==r['cpu_end']=='2'
 assert float(r['elapsed_ns'])>0 and abs(float(r['ns_per_decode'])-float(r['elapsed_ns'])/int(r['operations']))<0.000001
assert len(m['rows'])%4==0
for i in range(0,len(m['rows']),4):
 rs=m['rows'][i:i+4];assert [r['label'] for r in rs]==['A','B','B','A'];assert len({(r['cell']['name'],r['seed'],r['block']) for r in rs})==1
 for key in ('checksum','fixture_hash','leaf_bytes','operations','offset_mask','crossings_per_round'):assert len({r['result'][key] for r in rs})==1,(key,i)
 vals=[float(r['result']['ns_per_decode']) for r in rs]
 results.append(dict(cell=rs[0]['cell']['name'],variant=rs[1]['variant'],block=rs[0]['block'],seed=rs[0]['seed'],effect_pct=100*((vals[1]+vals[2])/(vals[0]+vals[3])-1),min_window_ns=min(float(r['result']['elapsed_ns']) for r in rs)))
s={}
for key in sorted({(r['cell'],r['variant']) for r in results}):
 rr=[r for r in results if (r['cell'],r['variant'])==key];e=[r['effect_pct'] for r in rr];minimum=min(r['min_window_ns'] for r in rr)
 s['/'.join(key)]=dict(blocks=len(rr),min_pct=min(e),max_pct=max(e),mean_pct=statistics.mean(e),median_pct=statistics.median(e),min_window_ns=minimum,aa_qualified=all(abs(x)<=1 for x in e) and minimum>=10000000)
(out/'analysis.json').write_text(json.dumps(dict(raw_rows=len(m['rows']),serial_boundaries_verified=True,blocks=results,summary=s),indent=2)+'\n')
print(json.dumps(s,indent=2))
