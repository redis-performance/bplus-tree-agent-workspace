#!/usr/bin/env python3
import csv,hashlib,io,json,math,os,statistics,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parent
REL=OUT.relative_to(Path.cwd())
BUILD=Path('scratch/m6-update/build')
SIZES=(100,1000,10000,100000,1000000)
CASES=('same','preserve','nearby','distant','plus-n')
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def run(cmd,name,folder='validation',expect=0,timeout=120):
 p=OUT/folder;p.mkdir(exist_ok=True);start=utc();t=time.monotonic()
 r=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,timeout=timeout)
 (p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr)
 with (OUT/'commands.jsonl').open('a') as f:f.write(json.dumps(dict(name=name,command=list(map(str,cmd)),started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,folder=folder))+'\n')
 if expect is not None:assert r.returncode==expect,(name,r.returncode,r.stderr[:500])
 return r
def build(name,source='src/zset_btree.c',bench=None,san=False,extra=()):
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1' if san else '-O3']
 if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
 return run(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis',*extra,bench or REL/'update-path-bench.c',source,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',BUILD/name],'build-'+name)
def args(binary='update',case='preserve',n=100000,ops=20000,seed=1,member=16):return [BUILD/binary,'--case',case,'--size',n,'--ops',ops,'--seed',seed,'--member-bytes',member]
def prepare():
 for name,san in [('update',False),('update-san',True)]:
  build(name,san=san)
  for n in SIZES:
   for case in CASES:run(args(name,case,n,2003),f'{name}-n{n}-{case}')
  for member in (8,319,320,321,1024):
   for case in CASES:run(args(name,case,1000,2003,member=member),f'{name}-m{member}-{case}')
  sem=name+'-semantic';build(sem,bench=REL/'semantic-check.c',san=san);run([BUILD/sem],sem)
 for name,extra,source in [('update-counts',['-DUPDATE_COUNTS'],'scratch/m6-update/instrumented.c'),('update-profile',['-DUPDATE_PROFILE'],'src/zset_btree.c')]:build(name,extra=extra,source=source)
 build('sampler-calibration',bench=REL/'../002-rank/sampler-calibration.c')
 freeze()
 print('prepare PASS',flush=True)
def freeze():
 files=['src/zset_btree.c','src/zset_btree.h','Makefile','compat/standalone.c','compat/server.h','vendor/redis/siphash.c','tests/upstream.c','bench/microbench.c',str(REL/'update-path-bench.c'),str(REL/'semantic-check.c'),str(REL/'run.py'),str(REL/'instrumentation.patch'),str(REL/'../002-rank/night-rank-sampler.h')]
 save(OUT/'freeze.json',dict(prepared_utc=utc(),head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),host_provenance='../launch-manifest.json launcher verification; direct sysctl unavailable',files={f:sha(f) for f in files},binaries={str(p):sha(p) for p in BUILD.iterdir() if p.is_file()},compiler=subprocess.check_output(['clang','--version'],text=True),checks='100 pattern/size/length checks; 2 finite/signed-zero semantic checks'))
def census():
 results=[]
 for n in SIZES:
  for case in CASES:
   r=run(args('update-counts',case,n),f'n{n}-{case}','census');parts=next(l for l in r.stderr.splitlines() if l.startswith('COUNTS,')).split(',');nums=list(map(int,parts[1:]));assert sum(nums)==20000
   results.append(dict(size=n,case=case,ops=20000,inplace=nums[0],preceding=nums[1],following=nums[2],pack=nums[3]))
 save(OUT/'census.json',results);print('census complete',flush=True)
def profile():
 for i in range(2):run([BUILD/'sampler-calibration'],f'calibration-{i}','profile')
 for n in (10000,100000,1000000):
  for case in ('preserve','distant'):run(args('update-profile',case,n,1000000),f'n{n}-{case}','profile')
 for name in ('update','update-profile'):
  r=run(['otool','-tvV',BUILD/name],name+'-assembly','profile');lines=r.stdout.splitlines()
  for func in ('zbtreeUpdateScore','zbtreeFindForAdd'):
   start=next(i for i,l in enumerate(lines) if l.strip()=='_'+func+':');end=next(i for i in range(start+1,len(lines)) if lines[i].startswith('_') and lines[i].endswith(':'))
   (OUT/'profile'/(name+'-'+func+'.asm')).write_text('\n'.join(lines[start:end])+'\n')
  src=OUT/'profile'/(name+'-assembly.stdout');src.rename(Path('scratch/m6-update')/(name+'-assembly.txt'))
 print('profiles complete',flush=True)
def measure(n,case,ops,seed,name,folder='raw'):
 r=run(args('update',case,n,ops,seed),name,folder);rows=list(csv.DictReader(io.StringIO(r.stdout)));assert len(rows)==1;x=rows[0];assert int(x['ops'])==ops and int(x['size'])==n and x['case']==case
 return dict(name=name,size=n,case=case,ops=ops,seed=seed,elapsed_ns=int(x['elapsed_ns']),ns_op=int(x['elapsed_ns'])/ops,checksum=x['checksum'],tree_bytes=int(x['tree_bytes']),file=folder+'/'+name+'.stdout',sha256=sha(OUT/folder/(name+'.stdout')))
def calibrate():
 assert not (OUT/'calibration.json').exists();d=dict(started_utc=utc(),publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()),observations=[],fixed_ops={},binary_sha256=sha(BUILD/'update'))
 for n in SIZES:
  for case in CASES:
   rs=[measure(n,case,200000,1,f'cal-n{n}-{case}-{i}') for i in range(3)];d['observations']+=rs
   d['fixed_ops'][f'{n}-{case}']=min(100000000,math.ceil(50000000/min(r['ns_op'] for r in rs)))
 d['finished_utc']=utc();save(OUT/'calibration.json',d);print('calibrated 25 cells',flush=True)
def qualify():
 assert not (OUT/'qualification.json').exists();cal=json.loads((OUT/'calibration.json').read_text());assert sha(BUILD/'update')==cal['binary_sha256'];d=dict(started_utc=utc(),runs=[],results=[],status='running',publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()))
 total=0
 try:
  for block,seed in enumerate((1,2,3,1,2,3)):
   sizes=(100000,1000000) if block%2==0 else (1000000,100000)
   for n in sizes:
    for step,label in enumerate('ABBA'):
     assert total<300;r=measure(n,'preserve',cal['fixed_ops'][f'{n}-preserve'],seed,f'b{block}-n{n}-{step}-{label}');r.update(block=block,step=step,label=label);d['runs'].append(r);total+=r['elapsed_ns']/1e9;save(OUT/'qualification.json',d)
   print('block',block+1,flush=True)
  for n in (100000,1000000):
   effects=[]
   for block in range(6):
    rs=[r for r in d['runs'] if r['size']==n and r['block']==block];assert len(rs)==4 and len({r['checksum'] for r in rs})==1 and len({r['tree_bytes'] for r in rs})==1
    a=statistics.mean(r['ns_op'] for r in rs if r['label']=='A');b=statistics.mean(r['ns_op'] for r in rs if r['label']=='B');effects.append(100*(b/a-1))
   rs=[r for r in d['runs'] if r['size']==n];short=min(r['elapsed_ns'] for r in rs)/1e6
   d['results'].append(dict(size=n,effects_pct=effects,shortest_ms=short,qualified=max(map(abs,effects))<=1 and short>=10))
  d['status']='complete'
 finally:d['timing_seconds']=total;d['finished_utc']=utc();save(OUT/'qualification.json',d)
 print(json.dumps(d['results']),flush=True)
if __name__=='__main__':globals()[sys.argv[1]]()
