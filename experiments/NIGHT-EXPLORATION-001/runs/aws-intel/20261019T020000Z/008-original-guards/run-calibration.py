from pathlib import Path
import json,csv,subprocess,datetime,time,hashlib
p=Path(__file__).parent;out=p/'calibration.json';assert not out.exists();(p/'raw').mkdir(exist_ok=True);binary='scratch/intel-scan-replication/base/build/btree-bench';assert hashlib.sha256(Path(binary).read_bytes()).hexdigest()=='b598d273956f17e79480f0343eaaed5f9bd96170dfa36058b3d679e5f1adbdc2'
start=time.monotonic();m=dict(status='running',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),processes=[])
try:
 for n in [100,1000,10000,100000,1000000]:
  for keybytes in [16,128]:
   left=600-(time.monotonic()-start);assert left>0
   cmd=[binary,'--case','all','--size',str(n),'--ops','5000000','--member-bytes',str(keybytes),'--seed','151'];tag=f'calibration-{n}-{keybytes}';t=datetime.datetime.now(datetime.timezone.utc).isoformat();t0=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(left,120))
   (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
   rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==8 and all(x['cpu_start']==x['cpu_end']=='2' for x in rows)
   m['processes'].append(dict(size=n,member_bytes=keybytes,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),duration_seconds=time.monotonic()-t0,rows=rows));out.write_text(json.dumps(m,indent=2)+'\n')
 m['status']='complete'
finally:
 m.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);out.write_text(json.dumps(m,indent=2)+'\n')
print('COMPLETE10 baseline duration processes,80 rows')
