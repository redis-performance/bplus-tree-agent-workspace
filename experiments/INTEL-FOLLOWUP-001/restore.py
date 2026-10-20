"""Idempotent owned lease recovery, including sibling state and OSS restoration."""
import datetime,fcntl,json,os,signal,subprocess,sys,time
from pathlib import Path
root=Path(__file__).resolve().parent
if '--recovery' in sys.argv:
 subprocess.run(['systemctl','kill','--kill-whom=all','--signal=TERM','bplus-intel-followup-001.service'],capture_output=True);time.sleep(3)
 subprocess.run(['systemctl','kill','--kill-whom=all','--signal=KILL','bplus-intel-followup-001.service'],capture_output=True)
with (root/'restore.lock').open('w') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX);p=root/'reservation.json'
 if not p.exists():sys.exit(0)
 state=json.loads(p.read_text());assert state['owner']=='bplus-intel-followup-001'
 pgid=state.get('worker_pgid')
 def owned():
  live=[]
  if pgid is None:return live
  for proc in Path('/proc').iterdir():
   if not proc.name.isdigit():continue
   try:
    fields=(proc/'stat').read_text().rsplit(')',1)[1].split()
    if int(fields[2])==pgid and fields[0]!='Z':live.append(int(proc.name))
   except (FileNotFoundError,ProcessLookupError,PermissionError):pass
  return live
 for sig in [signal.SIGTERM,signal.SIGKILL]:
  if owned():
   try:os.killpg(pgid,sig)
   except ProcessLookupError:pass
   time.sleep(1)
 remaining=owned()
 if remaining:
  (root/'results/restore.json').write_text(json.dumps({'pass':False,'owned_remaining':remaining})+'\n');sys.exit(1)
 Path('/sys/devices/system/cpu/cpu50/online').write_text(state['original_sibling_online'])
 subprocess.run(['supervisorctl','start','redis-benchmarks-spec-sc-coordinator'],capture_output=True)
 r=subprocess.run(['supervisorctl','status','redis-benchmarks-spec-sc-coordinator'],capture_output=True,text=True)
 ok='RUNNING' in r.stdout and Path('/sys/devices/system/cpu/cpu50/online').read_text().strip()==state['original_sibling_online'] and Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text().strip()==state['original_sibling_topology']
 state.update(state='RELEASED' if ok else 'RESTORE_FAILED',restored_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 p.write_text(json.dumps(state,indent=2)+'\n');(root/'results/restore.json').write_text(json.dumps({'pass':ok,'coordinator':r.stdout,'marker':state,'owned_remaining':remaining},indent=2)+'\n')
 if ok:subprocess.run(['systemctl','stop','bplus-intel-followup-recovery.timer'],capture_output=True)
 sys.exit(0 if ok else 1)
