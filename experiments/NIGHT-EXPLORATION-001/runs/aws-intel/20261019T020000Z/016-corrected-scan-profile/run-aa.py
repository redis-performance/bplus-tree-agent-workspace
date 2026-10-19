from pathlib import Path
import subprocess,json,csv,hashlib,time,datetime,os
root=Path.cwd();p=Path(__file__).parent.resolve();actual=root/'scratch/intel-corrected-adapter';expected=json.loads((p.parent/'013-corrected-adapter-baseline/source-after.json').read_text())['files'];out=p/'aa.json';assert not out.exists();assert json.loads((p/'profile-audit.json').read_text())['status']=='pass';assert os.sched_getaffinity(0)=={2}
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def identity(tag):
 observed={f:sha(actual/f) for f in expected};assert observed==expected;(p/(tag+'.json')).write_text(json.dumps(dict(status='pass',files=observed),indent=2)+'\n')
for f,h in json.loads((p/'execution-freeze.json').read_text())['files'].items():assert sha(p/f)==h
assert sha(p.parent/'013-corrected-adapter-baseline/source-after.json')==json.loads((p/'execution-freeze.json').read_text())['actual_artifact_manifest_sha256']
identity('aa-before');start=time.monotonic();m=dict(status='running',cap_seconds=300,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=[]);(p/'aa-raw').mkdir(exist_ok=False)
def save():out.write_text(json.dumps(m,indent=2)+'\n')
try:
 for spec in json.loads((p/'aa-schedule.json').read_text()):
  left=300-(time.monotonic()-start);assert left>0;i=len(m['rows']);tag=f'{i:03d}';cmd=[str(actual/'build/corrected-adapter-intel/btree-bench'),'--case','scan','--size',str(spec['size']),'--ops','5000000','--member-bytes','16','--seed',str(spec['seed'])];t=datetime.datetime.now(datetime.timezone.utc).isoformat()
  try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=left)
  except subprocess.TimeoutExpired as e:
   for ext,val in [('stdout',e.stdout),('stderr',e.stderr)]:(p/'aa-raw'/(tag+'.'+ext)).write_text(val.decode(errors='replace') if isinstance(val,bytes) else val or '')
   raise
  (p/'aa-raw'/(tag+'.stdout')).write_text(r.stdout);(p/'aa-raw'/(tag+'.stderr')).write_text(r.stderr);r.check_returncode();rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==1;row=rows[0];assert row['cpu_start']==row['cpu_end']=='2' and int(row['size'])==spec['size'] and int(row['seed'])==spec['seed'] and row['requested_ops']=='5000000' and row['member_bytes']=='16';m['rows'].append(dict(**spec,index=i,row=row,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));save()
 m['status']='complete'
except Exception as e:m['status']='stopped';m['error']=repr(e);raise
finally:m.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();identity('aa-after')
print('COMPLETE 48 corrected-source baseline-only A/A rows')
