#!/usr/bin/env python3
"""Corrected baseline-only iterator diagnosis: six fixed scoped samples and a separate known-work control."""
import argparse,csv,datetime,hashlib,io,json,os,pathlib,subprocess,tarfile,time
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);p.add_argument('--perf',required=True);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;source=here/'source';out=here/'profile';source.mkdir();out.mkdir();records=[];start=time.monotonic();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();expected=json.loads((here/'expected.json').read_text());assert sorted(os.sched_getaffinity(0))==[2]
contracts=json.loads((here/'commands.json').read_text())
def save(): (out/'processes.json').write_text(json.dumps(records,indent=2)+'\n')
def run(cmd,name,env=None,cwd=source):
 left=600-(time.monotonic()-start);assert left>0,'fixed profile cap reached';record={'name':name,'command':[str(x).replace(str(a.checkout),'<checkout>').replace(a.perf,'<perf>') for x in cmd],'started_utc':now(),'cwd':str(cwd).replace(str(a.checkout),'<checkout>'),'profile_env':{k:(str((env or os.environ)[k]).replace(str(a.checkout),'<checkout>') if k in (env or os.environ) else None) for k in ['PROFILE_DISABLE','BPLUS_PERF_CTL','BPLUS_PERF_ACK']}}
 assert {k:record[k] for k in ['name','command','cwd','profile_env']}==contracts[len(records)],name
 records.append(record);save()
 try:r=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,text=True,timeout=min(120,left))
 except subprocess.TimeoutExpired as e:
  record.update(finished_utc=now(),returncode=124)
  for suffix,value in [('stdout',e.stdout),('stderr',e.stderr)]:
   value=value or '';value=value.decode(errors='replace') if isinstance(value,bytes) else value;(out/(name+'.'+suffix)).write_text(value)
  save();raise
 record.update(finished_utc=now(),returncode=r.returncode);(out/(name+'.stdout')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr);save();r.check_returncode();return r.stdout
execution=json.loads((here/'execution-freeze.json').read_text())
for name,h in execution['files'].items():assert hashlib.sha256((here/name).read_bytes()).hexdigest()==h, name
archive=here/'source.tar'
run(['git','archive','--format=tar','--output',str(archive),expected['commit'],'src','compat','vendor/redis','tests','bench','Makefile'],'source-archive',cwd=a.checkout)
with tarfile.open(archive) as t:t.extractall(source,filter='data')
(source/'bench/profile-scoped-fifo2.c').write_bytes((here/'profile-scoped-fifo2.c').read_bytes());(source/'bench/known-control.c').write_bytes((here/'known-control.c').read_bytes());(source/'build').mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
protected_before={name:sha(a.checkout/name) for name in expected['protected_binaries']};assert protected_before==expected['protected_binaries']
sourcehash={f:sha(source/f) for f in expected['source_hashes']};assert sourcehash==expected['source_hashes'];assert sha(here/'profile-scoped-fifo2.c')==expected['scope_sha256']
flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-Isrc','-Icompat','-Ivendor/redis'];compiler=run(['clang','--version'],'compiler-version')
assert 'clang version 18.1.3' in compiler
for name,driver,san in [('original','bench/microbench.c',False),('profile','bench/profile-scoped-fifo2.c',False),('original-san','bench/microbench.c',True),('profile-san','bench/profile-scoped-fifo2.c',True)]:
 opt=['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if san else ['-O3'];run(['clang',*flags,*opt,driver,'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+name],name+'-build')
run(['clang',*flags,'-O3','bench/known-control.c','-o','build/known-control'],'known-control-build')
run(['make','CC=clang','BUILD=build/original-check','CFLAGS=-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3','check'],'original43')
binaryhash={n:sha(source/'build'/n) for n in ['original','profile','original-san','profile-san','original-check/btree-test','known-control']};(out/'build-freeze.json').write_text(json.dumps({'commit':expected['commit'],'source_hashes':sourcehash,'scope_sha256':expected['scope_sha256'],'binary_sha256':binaryhash,'compiler':compiler,'cpu_affinity':[2],'archive_sha256':sha(archive),'known_source_sha256':sha(here/'known-control.c')},indent=2)+'\n')
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes'];controls={}
def args(case,n,ops,seed):return ['--case',case,'--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed)]
def row(text):
 rr=list(csv.DictReader(text.splitlines()));assert len(rr)==1 and rr[0]['cpu_start']==rr[0]['cpu_end']=='2';return rr[0]
def equal(rows):
 for k in fields:assert len({r[k] for r in rows})==1,(k,rows)
disabled=os.environ.copy();disabled['PROFILE_DISABLE']='1'
fixtures=[(case,n,seed) for seed in [1,2,3] for n in [100000,1000000] for case in ['iterate']]
for case,n,seed in fixtures:
 label=f'{case}-n{n}-s{seed}';r=row(run(['build/original',*args(case,n,50000000,seed)],label+'-original'));s=row(run(['build/profile',*args(case,n,50000000,seed)],label+'-disabled',env=disabled));equal([r,s]);controls[label]=r
for case in ['iterate']:
 r=row(run(['build/original-san',*args(case,1000,2001,101)],case+'-san-original'));s=row(run(['build/profile-san',*args(case,1000,2001,101)],case+'-san-disabled',env=disabled));equal([r,s])
ctl=here/'control.fifo';ack=here/'ack.fifo';os.mkfifo(ctl);os.mkfifo(ack);env=os.environ.copy();env.pop('PROFILE_DISABLE',None);env['BPLUS_PERF_CTL']=str(ctl);env['BPLUS_PERF_ACK']=str(ack);disabledperf=dict(env,PROFILE_DISABLE='1');control=['-D','-1','--control=fifo:'+str(ctl)+','+str(ack)]
for case in ['iterate']:
 r=row(run([a.perf,'stat',*control,'-x,','-e','cycles:u,instructions:u,branches:u,branch-misses:u','-o',str(out/(case+'-disabled.stat')),'--','build/profile',*args(case,100000,50000000,1)],case+'-disabled-zero',env=disabledperf));equal([r,controls[case+'-n100000-s1']]);counts=[]
 for line in (out/(case+'-disabled.stat')).read_text().splitlines():
  if line and not line.startswith('#'):
   rec=next(csv.reader([line]));counts.append(rec[0]);assert rec[0].strip() in ['<not counted>','0'],rec
 assert len(counts)==4
# Standalone known work is a scope control, excluded from tree sample denominators.
known_expected=json.loads((here/'known-control-expectations.json').read_text())['expected_stdout']
def known_row(text):
 value=json.loads(text);assert value==known_expected;return value
known_row(run(['build/known-control'],'known-plain',env=disabled))
for mode,mode_env in [('disabled',disabledperf),('enabled',env)]:
 known_row(run([a.perf,'stat',*control,'-x,','-e','cycles:u,instructions:u,branches:u,branch-misses:u','-o',str(out/('known-'+mode+'.stat')),'--','build/known-control'],'known-'+mode+'-stat',env=mode_env))
 counts={}
 for line in (out/('known-'+mode+'.stat')).read_text().splitlines():
  if line and not line.startswith('#'):
   row_=next(csv.reader([line]));counts[row_[2]]=row_[0].strip()
 assert set(counts)=={'cycles:u','instructions:u','branches:u','branch-misses:u'}
 if mode=='disabled':assert all(v in ['0','<not counted>'] for v in counts.values())
 else:
  assert all(float(counts[k])>0 for k in ['cycles:u','instructions:u','branches:u'])
  assert float(counts['branch-misses:u'])>=0
known_row(run([a.perf,'record','-q',*control,'-e','cycles:u','-F997','-g','--call-graph','fp','-o',str(out/'known.data'),'--','build/known-control'],'known-record',env=env))
run([a.perf,'report','--stdio','--no-children','--sort','symbol','-i',str(out/'known.data')],'known-report')
run([a.perf,'script','-i',str(out/'known.data'),'-F','ip,sym,symoff,period'],'known-samples')
# Fail closed before scientific captures if known-work scope attribution fails.
from profile_helpers import known_gate
known_gate(out,here)
run(['objdump','-dSl','build/known-control'],'known-full-asm')
for name,binary in [('original','build/original'),('profile','build/profile'),('timing',str(a.checkout/'scratch/amd-adapter-requalification-13e459ff8/source/build/adapter-requalification/btree-bench'))]:run(['objdump','-dSl',binary],name+'-full-asm')
for case,n,seed in fixtures:
 label=f'{case}-n{n}-s{seed}';r=row(run([a.perf,'record','-q',*control,'-e','cycles:u','-F997','-g','--call-graph','fp','-o',str(out/(label+'.data')),'--','build/profile',*args(case,n,50000000,seed)],label+'-record',env=env));equal([r,controls[label]])
 run([a.perf,'report','--stdio','--no-children','--sort','symbol','-i',str(out/(label+'.data'))],label+'-report');run([a.perf,'script','-i',str(out/(label+'.data')),'-F','ip,sym,symoff,period'],label+'-samples')
assert sha(source/'bench/profile-scoped-fifo2.c')==expected['scope_sha256']
assert sha(source/'bench/known-control.c')==sha(here/'known-control.c')
assert {f:sha(source/f) for f in sourcehash}==sourcehash;assert {n:sha(source/'build'/n) for n in binaryhash}==binaryhash
protected_after={name:sha(a.checkout/name) for name in protected_before};assert protected_after==protected_before
(out/'complete.json').write_text(json.dumps({'status':'complete','finished_utc':now(),'elapsed_seconds':time.monotonic()-start,'sampled_captures':6,'enabled_tree_counter_captures':0,'known_counter_captures':1,'known_sample_captures':1,'protected_binaries_before':protected_before,'protected_binaries_after':protected_after,'controls':controls,'source_hashes_after':sourcehash,'binary_hashes_after':binaryhash,'raw_data_sha256':{p.name:sha(p) for p in out.glob('*.data')},'source_selection':'NONE','execution_freeze_sha256':sha(here/'execution-freeze.json')},indent=2)+'\n')
