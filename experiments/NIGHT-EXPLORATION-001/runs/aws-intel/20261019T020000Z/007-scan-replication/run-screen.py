from pathlib import Path
import csv,datetime,json,subprocess,time,hashlib
p=Path(__file__).parent;out=p/'screen.json';assert not out.exists();schedule=json.loads((p/'screen-schedule.json').read_text());freeze=json.loads((p/'candidate-freeze.json').read_text())
for v in freeze:
 b=Path('scratch/intel-scan-replication')/v/'build/btree-bench';assert hashlib.sha256(b.read_bytes()).hexdigest()==freeze[v]['build/btree-bench']
start=time.monotonic();m=dict(status='running',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=[])
try:
 for spec in schedule:
  left=300-(time.monotonic()-start)
  if left<=0:raise TimeoutError('fixed300-second screen cap')
  cmd=['scratch/intel-scan-replication/'+spec['binary']+'/build/btree-bench','--case','scan','--size',str(spec['size']),'--ops',str(spec['ops']),'--member-bytes',str(spec['member_bytes']),'--seed',str(spec['seed'])]
  t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(60,left));tag=f'screen-{spec["index"]:03d}'
  (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
  rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==1;row=rows[0];assert row['cpu_start']==row['cpu_end']=='2'
  m['rows'].append(dict(**spec,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=row));out.write_text(json.dumps(m,indent=2)+'\n')
 m['status']='complete'
except Exception as e:
 m['status']='stopped';m['error']=repr(e);raise
finally:
 m.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);out.write_text(json.dumps(m,indent=2)+'\n')
print('Complete',len(m['rows']),'serial screen rows')
