#!/usr/bin/env python3
"""Fixed104-command matched profile, separate source snapshots and exact scoped controls."""
import argparse,csv,datetime,hashlib,json,os,pathlib,re,subprocess,tarfile,time
from apply_exact import apply
from profile_helpers import known_gate
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);p.add_argument('--perf',required=True);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;out=here/'profile';out.mkdir();start=time.monotonic();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
e=json.loads((here/'expected.json').read_text());freeze=json.loads((here/'execution-freeze.json').read_text());contracts=json.loads((here/'commands.json').read_text());assert len(contracts)==104 and os.sched_getaffinity(0)=={2}
for n,h in freeze['files'].items():assert sha(here/n)==h,n
assert (datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc)-datetime.datetime.now(datetime.timezone.utc)).total_seconds()>=600
s=dict(status='running',started_utc=now(),cpu=2,execution_freeze_sha256=sha(here/'execution-freeze.json'),commands=[],sources_before={},binaries_before={},controls={})
def save():(out/'result.json').write_text(json.dumps(s,indent=2)+'\n')
def protected():
 x={n:sha(a.checkout/n) for n in e['protected_binaries']};assert x==e['protected_binaries'];return x
def actual_sources():
 result={}
 for v in ['control','A']:
  root=(a.checkout/e['timing_binaries'][v]['path']).parents[2];expected=dict(e['source_hashes'])
  if v=='A':expected['src/zset_btree.c']=e['candidate_source_sha256']
  result[v]={n:sha(root/n) for n in expected};assert result[v]==expected
 return result
s['protected_before']=protected();s['actual_sources_before']=actual_sources();save()
for n in ['control.fifo','ack.fifo']:os.mkfifo(here/n)
def expand(x):return x.replace('<checkout>',str(a.checkout)).replace('<job>',str(here)).replace('<perf>',a.perf)
def prepare():
 for variant in ['control','A']:
  root=here/variant;root.mkdir()
  with tarfile.open(here/'source.tar') as t:t.extractall(root,filter='data')
  assert {n:sha(root/n) for n in e['source_hashes']}==e['source_hashes']
  if variant=='A':
   assert sha(here/'candidate.patch')==e['candidate_patch_sha256'];f=root/'src/zset_btree.c';f.write_text(apply(f.read_text(),(here/'candidate.patch').read_text()));assert sha(f)==e['candidate_source_sha256']
  for n in ['profile-scoped-fifo2.c','known-control.c']:(root/'bench'/n).write_bytes((here/n).read_bytes())
  (root/'build').mkdir();s['sources_before'][variant]={n:sha(root/n) for n in list(e['source_hashes'])+['bench/profile-scoped-fifo2.c','bench/known-control.c']}
 save()
def tree_row(text,fixture):
 rows=list(csv.DictReader(text.splitlines()));assert len(rows)==1;z=rows[0];n=fixture['size'];ops=fixture['requested_ops'];traversals=(ops+n-1)//n
 expected=dict(fixture,operations=traversals*n,traversals=traversals,checksum=traversals*n*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
 for k,v in expected.items():assert z[k]==str(v),(k,z[k],v)
 assert int(z['elapsed_ns'])>0 and int(z['tree_bytes'])>0
 return z
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
def counter_file(path,enabled):
 values={}
 for line in path.read_text().splitlines():
  if not line or line.startswith('#'):continue
  z=next(csv.reader([line]));assert z[2] not in values;values[z[2]]=z[0].strip()
  if enabled:assert len(z)>4 and float(z[4])==100.0,(path.name,z)
 assert set(values)=={'cycles:u','instructions:u','branches:u','branch-misses:u'}
 if enabled:
  assert all(float(values[k])>0 for k in ['cycles:u','instructions:u','branches:u']);assert float(values['branch-misses:u'])>=0
 else:assert all(v in ['0','<not counted>'] for v in values.values())
 return values
try:
 for contract in contracts:
  remaining=600-(time.monotonic()-start);assert remaining>0,'fixed600s cap';r=dict(contract,started_utc=now());s['commands'].append(r);save();env=os.environ.copy()
  for k,v in contract['profile_env'].items():
   if v is None:env.pop(k,None)
   else:env[k]=expand(v)
  try:
   q=subprocess.run([expand(x) for x in contract['command']],cwd=expand(contract['cwd']),env=env,capture_output=True,text=True,timeout=min(120,remaining));rc=q.returncode;stdout=q.stdout;stderr=q.stderr
  except subprocess.TimeoutExpired as ex:
   rc=124;stdout=ex.stdout or '';stderr=ex.stderr or '';stdout=stdout.decode(errors='replace') if isinstance(stdout,bytes) else stdout;stderr=stderr.decode(errors='replace') if isinstance(stderr,bytes) else stderr
  r.update(finished_utc=now(),returncode=rc);(out/(r['name']+'.stdout')).write_text(stdout);(out/(r['name']+'.stderr')).write_text(stderr);save();assert rc==0,(r['name'],rc)
  kind=r['kind'];variant=r['variant']
  if kind=='archive':prepare()
  if kind=='compiler':assert 'clang version 18.1.3' in stdout and 'aarch64' in stdout
  if kind=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',stdout)
  if kind.startswith('tree'):
   z=tree_row(stdout,r['fixture']);r['row']=z;key=f"{z['size']}/{z['seed']}/{z['requested_ops']}";reference=s['controls'].setdefault(key,z)
   assert all(z[k]==reference[k] for k in fields),(r['name'],'semantic parity')
   if kind in ['tree-stat','tree-disabled-stat']:
    statname=r['name'][:-5] if r['name'].endswith('-stat') else variant+'-disabled';r['counters']=counter_file(out/(statname+'.stat'),kind=='tree-stat')
  if kind in ['known','known-stat']:assert json.loads(stdout)==json.loads((here/'known-control-expectations.json').read_text())['expected_stdout']
  if kind=='known-stat':r['counters']=counter_file(out/(r['name'][:-5]+'.stat'),r['name']=='known-enabled-stat')
  if kind=='known-gate':s['known_gate']=known_gate(out,here)
  if r['name']=='known-control-build':
   for v in ['control','A']:
    names=['original','profile','original-san','profile-san','original-check/btree-test']+(['known-control'] if v=='control' else [])
    s['binaries_before'][v]={n:sha(here/v/'build'/n) for n in names}
  r['checked']=True;save()
 assert len(s['commands'])==104 and all(x.get('checked') for x in s['commands'])
 s['raw_data_sha256']={f.name:sha(f) for f in out.glob('*.data')};assert len(s['raw_data_sha256'])==13
 s['status']='complete'
except BaseException as ex:s.update(status='failed',error=type(ex).__name__+': '+str(ex));raise
finally:
 try:
  s['protected_after']=protected();assert s['protected_after']==s['protected_before'];s['actual_sources_after']=actual_sources();assert s['actual_sources_after']==s['actual_sources_before']
  s['sources_after']={v:{n:sha(here/v/n) for n in files} for v,files in s['sources_before'].items()};assert s['sources_after']==s['sources_before']
  s['binaries_after']={v:{n:sha(here/v/'build'/n) for n in files} for v,files in s['binaries_before'].items()};assert s['binaries_after']==s['binaries_before']
 except BaseException as ex:s.update(status='failed',post_identity_error=type(ex).__name__+': '+str(ex))
 s.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save();assert s['status']!='failed' and s['elapsed_seconds']<=600
