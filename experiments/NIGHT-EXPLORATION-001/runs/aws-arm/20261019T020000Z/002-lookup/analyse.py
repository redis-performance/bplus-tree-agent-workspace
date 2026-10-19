import collections,csv,hashlib,json,sys
from pathlib import Path
p=Path(__file__).resolve().parent; phase=sys.argv[1];out=p/phase;m=json.load(open(out/'manifest.json'));assert m['status']=='complete'
groups=collections.defaultdict(list);prev=0
for row in m['rows']:
 assert row['returncode']==0 and row['started']>=prev;prev=row['finished']
 raw=(out/(row['name']+'.csv')).read_bytes();assert hashlib.sha256(raw).hexdigest()==row['csv_sha256']
 r=list(csv.DictReader(raw.decode().splitlines()))[0];assert r==row['result'];assert r['cpu_start']==r['cpu_end']=='2'
 assert int(r['elapsed_ns'])>0 and abs(float(r['ns_per_op'])-int(r['elapsed_ns'])/int(r['operations']))<0.001
 # Groups are scheduled adjacent ABBA windows; identify by start ordinal.
# Rebuild contiguous groups, retaining every row and seed.
assert len(m['rows'])%4==0
results=[]
for i in range(0,len(m['rows']),4):
 rs=m['rows'][i:i+4];assert [r['label'] for r in rs]==['A','B','B','A']
 assert len({(r['cell']['name'],r['seed'],r['block']) for r in rs})==1
 assert len({r['result']['checksum'] for r in rs})==1
 vals=[float(r['result']['ns_per_op']) for r in rs];memory=[int(r['result']['tree_bytes']) for r in rs]
 results.append(dict(cell=rs[0]['cell']['name'],variant=rs[1]['variant'],block=rs[0]['block'],seed=rs[0]['seed'],effect_pct=100*((vals[1]+vals[2])/(vals[0]+vals[3])-1),min_window_ns=min(int(r['result']['elapsed_ns']) for r in rs),memory_delta_pct=100*((memory[1]+memory[2])/(memory[0]+memory[3])-1)))
summary={}
for cell in sorted({(r['cell'],r['variant']) for r in results}):
 rr=[r for r in results if (r['cell'],r['variant'])==cell];e=[r['effect_pct'] for r in rr]
 summary['/'.join(cell)]=dict(blocks=len(rr),min_pct=min(e),max_pct=max(e),mean_pct=sum(e)/len(e),min_window_ns=min(r['min_window_ns'] for r in rr),aa_qualified=all(abs(x)<=1 for x in e) and min(r['min_window_ns'] for r in rr)>=10000000,memory_max_pct=max(r['memory_delta_pct'] for r in rr))
result=dict(raw_rows=len(m['rows']),serial_boundaries_verified=True,blocks=results,summary=summary)
(out/'analysis.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(summary,indent=2))
