import csv,hashlib,json,statistics,sys
from pathlib import Path
P=Path(__file__).resolve().parent;phase=sys.argv[1];out=P/phase;m=json.load(open(out/'manifest.json'));assert m['status']=='complete';rows=m['rows'];prior='';blocks=[]
for r in rows:
 assert r['returncode']==0 and r['started_utc']>=prior;prior=r['finished_utc'];raw=(out/'raw'/(r['name']+'.csv')).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['csv_sha256'];rr=list(csv.DictReader(raw.decode().splitlines()));assert len(rr)==1 and rr[0]==r['result'];v=rr[0];assert v['cpu_start']==v['cpu_end']=='2' and v['checksum']==v['expected_checksum'];assert int(v['elapsed_ns'])>0
if phase=='calibration':assert len(rows)==24;print('24 calibration processes audited');raise SystemExit
assert len(rows)==192
for i in range(0,len(rows),4):
 rs=rows[i:i+4];assert [r['position'] for r in rs]==[0,1,2,3];assert rs[0]['variant']==rs[3]['variant']=='base';assert rs[1]['variant']==rs[2]['variant'];assert len({(r['cell'],r['block'],r['seed']) for r in rs})==1
 for key in ['checksum','expected_checksum','tree_bytes','operations','construction_fingerprint','warmup_passes','member_bytes','mask','direction','encoding']:
  assert len({r['result'][key] for r in rs})==1,(i,key)
 vals=[int(r['result']['elapsed_ns'])/int(r['result']['operations']) for r in rs];effect=100*((vals[1]+vals[2])/(vals[0]+vals[3])-1)
 blocks.append({'cell':rs[0]['cell'],'variant':rs[1]['variant'],'block':rs[0]['block'],'seed':rs[0]['seed'],'effect_pct':effect,'min_window_ns':min(int(r['result']['elapsed_ns']) for r in rs),'tree_bytes_equal':True})
s={}
for cell in sorted({r['cell'] for r in blocks}):
 rr=[r for r in blocks if r['cell']==cell];assert len(rr)==6;es=[r['effect_pct'] for r in rr];minimum=min(r['min_window_ns'] for r in rr);s[cell]={'blocks':6,'min_pct':min(es),'max_pct':max(es),'median_pct':statistics.median(es),'min_window_ns':minimum,'aa_qualified':phase=='aa' and all(abs(x)<=1 for x in es) and minimum>=10000000}
a={'status':'pass','processes':len(rows),'raw_hashes_verified':True,'serial_boundaries_verified':True,'blocks':blocks,'summary':s};(out/'analysis.json').write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(s,indent=2))
