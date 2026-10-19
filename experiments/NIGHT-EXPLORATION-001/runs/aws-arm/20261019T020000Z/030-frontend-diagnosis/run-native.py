#!/usr/bin/env python3
import argparse,datetime,json,os,pathlib,subprocess,time
from native_common import HERE,CELLS,IDS,sha,identities,check_row,same_semantics
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);p.add_argument('--lease',required=True,type=pathlib.Path);p.add_argument('--phase',required=True,choices=['native-AA','native-comparison']);a=p.parse_args();out=HERE/a.phase;out.mkdir();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic();lease=json.loads(a.lease.read_text());deadline=lease['deadline'];assert lease['unit_prefix']=='bplus-frontjob-20261019-' and lease['slice']=='bplus-front-20261019.slice' and lease['cpu']==2;assert datetime.datetime.fromisoformat(deadline)==datetime.datetime(2026,10,19,11,45,tzinfo=datetime.timezone.utc);assert (datetime.datetime.fromisoformat(deadline)-datetime.datetime.now(datetime.timezone.utc)).total_seconds()>=620
assert os.sched_getaffinity(0)=={2};freeze=json.loads((HERE/'native-execution-freeze.json').read_text());assert all(sha(HERE/n)==h for n,h in freeze['files'].items());schedule=json.loads((HERE/'schedules.json').read_text())[a.phase];assert len(schedule)==144
s=dict(status='running',phase=a.phase,started_utc=now(),cpu=2,deadline=deadline,lease_sha256=sha(a.lease),lease_scope={k:lease[k] for k in ['unit_prefix','slice','cpu','deadline']},freeze_sha256=sha(HERE/'native-execution-freeze.json'),runs=[]);save=lambda:(out/'result.json').write_text(json.dumps(s,indent=2)+'\n');save();refs={}
if a.phase=='native-comparison':
 aa=json.loads((HERE/'native-AA/result.json').read_text());audit=json.loads((HERE/'native-AA/audit.json').read_text());assert aa['status']=='complete' and len(aa['runs'])==144 and audit['status']=='integrity_pass';assert audit['result_sha256']==sha(HERE/'native-AA/result.json');assert aa['freeze_sha256']==s['freeze_sha256'] and aa['identities_before']==aa['identities_after'];assert datetime.datetime.fromisoformat(aa['finished_utc'])<datetime.datetime.fromisoformat(s['started_utc']);assert all(sha(HERE/'native-AA'/n)==h for n,h in audit['raw_files_sha256'].items());assert len(audit['raw_files_sha256'])==288;s['AA_result_sha256']=sha(HERE/'native-AA/result.json');s['AA_audit_sha256']=sha(HERE/'native-AA/audit.json')
 for r in aa['runs']:refs[(r['cell'],r['seed'])]=check_row((HERE/'native-AA'/r['stdout']).read_text(),r)
try:
 s['identities_before']=identities(a.checkout);save()
 if a.phase=='native-comparison':assert aa['identities_before']==s['identities_before']
 for c in schedule:
  remaining=600-(time.monotonic()-start);assert remaining>0,'fixed phase cap';cell=CELLS[c['cell']];exe=a.checkout/IDS['binaries'][cell['frontend']+'-'+c['source']]['path'];r=dict(c,started_utc=now(),stdout=f'{c["index"]:04d}.csv',stderr=f'{c["index"]:04d}.stderr');s['runs'].append(r);save()
  try:q=subprocess.run([str(exe)]+c['args'],capture_output=True,text=True,timeout=min(60,remaining));rc=q.returncode;stdout=q.stdout;stderr=q.stderr
  except subprocess.TimeoutExpired as ex:
   rc=124;stdout=ex.stdout or '';stderr=ex.stderr or '';stdout=stdout.decode(errors='replace') if isinstance(stdout,bytes) else stdout;stderr=stderr.decode(errors='replace') if isinstance(stderr,bytes) else stderr
  r.update(finished_utc=now(),returncode=rc);(out/r['stdout']).write_text(stdout);(out/r['stderr']).write_text(stderr);save();assert rc==0 and not stderr.strip(),(r['index'],rc)
  row=check_row(stdout,c);key=(c['cell'],c['seed']);ref=refs.setdefault(key,row);assert same_semantics(row,ref);r['checked']=True;save()
 s['status']='complete'
except BaseException as ex:s.update(status='failed',error=type(ex).__name__+': '+str(ex));raise
finally:
 try:s['identities_after']=identities(a.checkout);assert s['identities_before']==s['identities_after']
 except BaseException as ex:s.update(status='failed',post_identity_error=type(ex).__name__+': '+str(ex))
 s.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save();assert s['status']=='complete' and s['elapsed_seconds']<=600
