#!/usr/bin/env python3
"""Fixed dual-frontend diagnosis. Counter direction is evidence, never a validity filter."""
import argparse,datetime,hashlib,json,os,pathlib,re,subprocess,sys,tarfile,time
from native_common import HERE,IDS,sha,identities,same_semantics
from profile_common import row,counters,census,elf_text,allocator_mode
sys.path.insert(0,str(HERE/'inputs'))
from apply_exact import apply
from profile_helpers import known_gate,samples,report
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);p.add_argument('--lease',required=True,type=pathlib.Path);p.add_argument('--perf',required=True);a=p.parse_args();out=HERE/'profile';out.mkdir();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic();lease=json.loads(a.lease.read_text());assert lease['unit_prefix']=='bplus-frontjob-20261019-' and lease['slice']=='bplus-front-20261019.slice' and lease['cpu']==2;deadline=datetime.datetime.fromisoformat(lease['deadline']);assert deadline==datetime.datetime(2026,10,19,11,45,tzinfo=datetime.timezone.utc) and (deadline-datetime.datetime.now(datetime.timezone.utc)).total_seconds()>=1220 and os.sched_getaffinity(0)=={2}
freeze=json.loads((HERE/'profile-execution-freeze.json').read_text());assert all(sha(HERE/n)==h for n,h in freeze['files'].items());contracts=json.loads((HERE/'profile-commands.json').read_text());assert len(contracts)==642
s=dict(status='running',started_utc=now(),cpu=2,lease_sha256=sha(a.lease),lease_scope={k:lease[k] for k in ['unit_prefix','slice','cpu','deadline']},execution_freeze_sha256=sha(HERE/'profile-execution-freeze.json'),commands=[],sources_before={},binaries_before={},controls={},census_controls={});save=lambda:(out/'result.json').write_text(json.dumps(s,indent=2)+'\n');save()
for n in ['control.fifo','ack.fifo']:os.mkfifo(HERE/n)
def expand(x):return x.replace('<checkout>',str(a.checkout)).replace('<job>',str(HERE)).replace('<perf>',a.perf)
def prepare():
 for v in ['control','A']:
  root=HERE/v;root.mkdir()
  with tarfile.open(HERE/'source.tar') as t:t.extractall(root,filter='data')
  assert {n:sha(root/n) for n in IDS['source_hashes']}==IDS['source_hashes']
  if v=='A':
   assert sha(HERE/'inputs/candidate.patch')==IDS['candidate_patch_sha256'];f=root/'src/zset_btree.c';f.write_text(apply(f.read_text(),(HERE/'inputs/candidate.patch').read_text()));assert sha(f)==IDS['candidate_source_sha256']
  for f in (HERE/'inputs').iterdir():
   if f.suffix in ['.c','.h']:(root/'bench'/f.name).write_bytes(f.read_bytes())
  (root/'build').mkdir();files=set(IDS['source_hashes'])|{'bench/'+f.name for f in (HERE/'inputs').iterdir() if f.suffix in ['.c','.h']};s['sources_before'][v]={n:sha(root/n) for n in sorted(files)}
 save()
def bind_binaries():
 for v in ['control','A']:
  s['binaries_before'][v]={str(f.relative_to(HERE/v)):sha(f) for f in sorted((HERE/v/'build').rglob('*')) if f.is_file()}
 s['original_actual_text_identity']={}
 for front in ['primary','h4']:
  for v in ['control','A']:
   original=HERE/v/'build'/f'{front}-original';actual=a.checkout/IDS['binaries'][front+'-'+v]['path'];x=hashlib.sha256(elf_text(original)).hexdigest();y=hashlib.sha256(elf_text(actual)).hexdigest();assert x==y,(front,v,'original .text mismatch');s['original_actual_text_identity'][front+'-'+v]=dict(original_text_sha256=x,actual_text_sha256=y,actual_binary_sha256=sha(actual),original_binary_sha256=sha(original))
 save()
try:
 s['identities_before']=identities(a.checkout);save()
 for c in contracts:
  remaining=1200-(time.monotonic()-start);assert remaining>0,'fixed1200s cap';r=dict(c,started_utc=now());s['commands'].append(r);save();env=os.environ.copy()
  for k,v in c['profile_env'].items():
   if v is None:env.pop(k,None)
   else:env[k]=expand(v)
  try:q=subprocess.run([expand(x) for x in c['command']],cwd=expand(c['cwd']),env=env,capture_output=True,text=True,timeout=min(120,remaining));rc=q.returncode;stdout=q.stdout;stderr=q.stderr
  except subprocess.TimeoutExpired as ex:
   rc=124;stdout=ex.stdout or '';stderr=ex.stderr or '';stdout=stdout.decode(errors='replace') if isinstance(stdout,bytes) else stdout;stderr=stderr.decode(errors='replace') if isinstance(stderr,bytes) else stderr
  r.update(finished_utc=now(),returncode=rc);(out/(c['name']+'.stdout')).write_text(stdout);(out/(c['name']+'.stderr')).write_text(stderr);save();assert rc==0,(c['name'],rc)
  kind=c['kind']
  if kind=='archive':prepare()
  if kind=='compiler':assert 'clang version 18.1.3' in stdout and 'aarch64' in stdout
  if kind=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',stdout)
  if c['name']=='known-missing-disable-build':bind_binaries()
  if c['fixture'] is not None:
   z=row(stdout,c['fixture']);r['row']=z;f=c['fixture'];key=f"{f['frontend']}/{f['direction']}/{f['size']}/{f['seed']}/{f['requested_ops']}/{allocator_mode(c)}";reference=s['controls'].setdefault(key,z);assert same_semantics(z,reference),(c['name'],'semantic parity')
   if kind=='census':
    obs=census(stderr,f,z);r['census']=obs;ref=s['census_controls'].setdefault(key,obs);assert obs==ref
   elif kind in ['tree','instrument']:assert not stderr.strip(),c['name']
   if kind in ['tree-stat','disabled-stat']:r['counters']=counters(out/c['stat_file'],kind=='tree-stat')
  if kind in ['known','known-stat']:assert json.loads(stdout)==json.loads((HERE/'inputs/known-control-expectations.json').read_text())['expected_stdout']
  if kind=='known-stat':r['counters']=counters(out/c['stat_file'],c['name']=='known-enabled-stat')
  if kind=='known-gate':s['known_gate']=known_gate(out,HERE/'inputs');assert s['known_gate']['lost']==0
  if kind=='fault-scope':
   rows=samples(out/'known-missing-disable-samples.stdout');rr=report(out/'known-missing-disable-report.stdout',rows);assert rr['lost']==0 and sum(x['physical']=='outside_work' for x in rows)>0;s['scope_fault_detected']=True
  r['checked']=True;save()
 assert len(s['commands'])==642 and all(x.get('checked') for x in s['commands']);s['raw_data_sha256']={f.name:sha(f) for f in out.glob('*.data')};assert len(s['raw_data_sha256'])==38;s['status']='complete'
except BaseException as ex:s.update(status='failed',error=type(ex).__name__+': '+str(ex));raise
finally:
 try:
  s['identities_after']=identities(a.checkout);assert s['identities_after']==s['identities_before'];s['sources_after']={v:{n:sha(HERE/v/n) for n in files} for v,files in s['sources_before'].items()};assert s['sources_after']==s['sources_before'];s['binaries_after']={v:{n:sha(HERE/v/n) for n in files} for v,files in s['binaries_before'].items()};assert s['binaries_after']==s['binaries_before']
 except BaseException as ex:s.update(status='failed',post_identity_error=type(ex).__name__+': '+str(ex))
 s.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save();assert s['status']=='complete' and s['elapsed_seconds']<=1200
