from pathlib import Path
import json,csv,subprocess,datetime,time,hashlib
p=Path(__file__).parent;out=p/'b-comparison.json';assert not out.exists();schedule=json.loads((p/'b-schedule.json').read_text());freeze=json.loads((p/'b-freeze.json').read_text());assert json.loads((p/'aa-audit.json').read_text())['phase_status']=='complete'
for v,h in freeze['binary_sha256'].items():assert hashlib.sha256(Path('scratch/intel-scan-replication',v,'build/btree-bench').read_bytes()).hexdigest()==h
for f,h in freeze['files'].items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
start=time.monotonic();m=dict(status='running',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),processes=[])
try:
 for spec in schedule:
  left=freeze['phase_cap_seconds']-(time.monotonic()-start)
  if left<=0:raise TimeoutError('fixed B guard phase cap')
  binary='scratch/intel-scan-replication/'+spec['binary']+'/build/btree-bench'
  cmd=[binary,'--case','all','--size',str(spec['size']),'--ops','5000000','--member-bytes',str(spec['member_bytes']),'--seed',str(spec['seed'])];tag=f'b-{spec["index"]:03d}';t=datetime.datetime.now(datetime.timezone.utc).isoformat();t0=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(left,120))
  (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
  rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==8 and all(x['cpu_start']==x['cpu_end']=='2' for x in rows)
  m['processes'].append(dict(**spec,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),duration_seconds=time.monotonic()-t0,rows=rows));out.write_text(json.dumps(m,indent=2)+'\n')
 m['status']='complete'
except Exception as e:
 m['status']='stopped';m['error']=repr(e);raise
finally:
 m.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);out.write_text(json.dumps(m,indent=2)+'\n')
print('COMPLETE',len(m['processes']),'processes',8*len(m['processes']),'rows')
