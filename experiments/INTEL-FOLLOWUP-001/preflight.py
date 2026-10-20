"""Fail closed on competing ownership/work; do not stop unrelated services."""
import datetime,json,os,subprocess
from pathlib import Path
O=Path('results');O.mkdir(exist_ok=True);errors=[];records=[]
for name in ['ffc-exp070-20260929','zscan-gap-20260929','fullsync-577-qualification-20260921/results']:
 p=Path('/tmp')/name/'released.json';d=json.loads(p.read_text());assert not d.get('cleanup_errors') and not d.get('remaining_containers');records.append({'historical_owner':name,'release_record_present':True})
lease=Path('/opt/pr15967-validation-20261020/reservation.json')
if lease.exists():
 d=json.loads(lease.read_text())
 if str(d.get('status','')).lower() not in ['released','complete']:errors.append('other validation reservation not released')
# Inventory other marker files; old markers require an adjacent explicit release.
for base in [Path('/tmp'),Path('/opt')]:
 for directory,dirs,files in os.walk(base):
  if len(Path(directory).relative_to(base).parts)>=3:dirs[:]=[]
  if Path.cwd()==Path(directory) or Path.cwd() in Path(directory).parents:dirs[:]=[];continue
  for filename in files:
   if 'reservation' not in filename or not filename.endswith('.json'):continue
   path=Path(directory)/filename
   try:d=json.loads(path.read_text())
   except (PermissionError,FileNotFoundError,json.JSONDecodeError):errors.append('unreadable reservation: '+str(path));continue
   state=str(d.get('status',d.get('state',''))).lower()
   if state in ['released','complete','completed']:continue
   if state=='' and str(path.parent) in ['/tmp/ffc-exp070-20260929','/tmp/zscan-gap-20260929','/tmp/fullsync-577-qualification-20260921/results'] and (path.parent/'released.json').exists() and not Path('/proc/'+str(d.get('pid','missing'))).exists():continue
   errors.append('unreleased reservation: '+str(path))
  continue
containers=subprocess.check_output(['docker','ps','-q'],text=True).split();assert not containers,'active Docker workloads'
units=subprocess.check_output(['systemctl','list-units','--type=service','--state=running','--plain','--no-legend'],text=True)
foreign=[l.split()[0] for l in units.splitlines() if any(x in l.lower() for x in ['capture','hdrfuzz','pr15967'])];errors+=foreign
blocked={'node','nodejs','cc1','cc1plus','clang','clang-18','gcc','g++','make','ninja','memtier_benchmar','redis-server','hdrfuzz','db_bench','perf','toplev','iterator','update','scan','guard','microbench'}
inventory=[]
for p in Path('/proc').iterdir():
 if not p.name.isdigit():continue
 try:
  comm=(p/'comm').read_text().strip();args=(p/'cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace')
  inventory.append({'pid':int(p.name),'comm':comm,'cmdline':args,'cgroup':(p/'cgroup').read_text()})
  native=comm.startswith(('iterator-','update-','scan-','guard-','microbench','zbtree','bplus'))
  collector=any(x in args.split() for x in ['toplev.py','capture.py']) or any(x.endswith(('/toplev.py','/capture.py')) for x in args.split())
  if comm in blocked or native or (collector and p.name!=str(os.getpid())):errors.append('foreign workload '+p.name+' '+comm)
 except (FileNotFoundError,PermissionError,ProcessLookupError):pass
Path('private-process-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
assert Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text().strip()=='2,50'
assert Path('/sys/devices/system/cpu/cpu50/online').read_text().strip()=='1'
status=subprocess.check_output(['supervisorctl','status','redis-benchmarks-spec-sc-coordinator'],text=True);assert 'RUNNING' in status
result={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner':'secondary Intel','old_releases':records,'other_capture_units':foreign,'containers':len(containers),'ambient_parca':any('parca' in l for l in units.splitlines()),'errors':errors,'pass':not errors}
(O/'preflight.json').write_text(json.dumps(result,indent=2)+'\n');assert not errors,errors
