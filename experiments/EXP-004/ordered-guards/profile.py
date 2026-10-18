from pathlib import Path
import json,hashlib,shutil,subprocess,time,os,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'freeze.json').read_text());G=json.loads((R/'experiments/OVERNIGHT-2026-10-17/PROFILE-003/freeze.json').read_text());S=R/'scratch/exp-004-ordered-profiles';assert not S.exists();S.mkdir();D=P/'profiles';D.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();M=dict(status='preparing',plan_sha256=sha(P/'PLAN.md'),sources={},preparation=[],calibrations=[],runs=[])
def save():(D/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def command(name,cmd,cwd,section,meta=None,env=None):
 out=S/(name+'.stdout');err=S/(name+'.stderr');row=dict(name=name,command=cmd,cwd=str(cwd.relative_to(R)),started_utc=utc(),**(meta or {}))
 with out.open('w') as so,err.open('w') as se:
  try:q=subprocess.run(cmd,cwd=cwd,stdout=so,stderr=se,timeout=120,env=env);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));M[section].append(row);save();assert rc==0,name
 return row
for v,files in F['files'].items():
 B=S/v;B.mkdir()
 for n,h in files.items():
  src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for n in ['bench/self_sampler.h','bench/calibrate.c']:
  src=R/G['snapshot']/n;assert sha(src)==G['files'][n];shutil.copy2(src,B/n)
 p=B/'bench/iterator_modes.c';s=p.read_text();pairs=[('#include <math.h>','#include <math.h>\n#include "self_sampler.h"'),('    uint64_t rng=seed;','    sample_init();\n    uint64_t rng=seed;'),('int64_t t0=thread_ns();uint64_t w0=now_ns();','sample_start();int64_t t0=thread_ns();uint64_t w0=now_ns();'),('int64_t t1=thread_ns();int cpu1=cpu_id();','int64_t t1=thread_ns();sample_stop();int cpu1=cpu_id();'),('    serverAssert(checksum==expected*traversals','    sample_dump("iterator-modes");\n    serverAssert(checksum==expected*traversals')]
 for a,b in pairs:assert s.count(a)==1;s=s.replace(a,b)
 p.write_text(s);M['sources'][v]={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()};(B/'build/release').mkdir(parents=True)
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3','bench/iterator_modes.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/release/iterator-modes']
 command(v+'-build',cmd,B,'preparation');command(v+'-dsym',['dsymutil','build/release/iterator-modes'],B,'preparation');command(v+'-assembly',['otool','-tvV','build/release/iterator-modes'],B,'preparation')
B=S/'control';command('calibrate-build',['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O3','-fno-omit-frame-pointer','bench/calibrate.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/release/calibrate'],B,'preparation');command('calibrate-dsym',['dsymutil','build/release/calibrate'],B,'preparation')
M['status']='running';save();env=dict(os.environ,PROFILE_USEC='1000')
for i in range(2):
 command(f'calibrate-{i}',[str((B/'build/release/calibrate').relative_to(R)),'400000000'],R,'calibrations',dict(binary=str((B/'build/release/calibrate').relative_to(R)),binary_sha256=sha(B/'build/release/calibrate')),env)
cells=[('int-desc-r4','integer','descending','reverse',4),('zero-desc-f4','alternating-zero','descending','forward',4),('zero-desc-f6','alternating-zero','descending','forward',6)]
for name,encoding,construction,direction,mask in cells:
 for v in ['control','A','B','C']:
  binary=S/v/'build/release/iterator-modes';cmd=[str(binary.relative_to(R)),'--size','100000','--ops','100000000','--seed','31031','--warmup-passes','3','--direction',direction,'--encoding',encoding,'--construction',construction,'--member-bytes','16','--mask',str(mask)]
  command(f'{v}-{name}',cmd,R,'runs',dict(variant=v,cell=name,encoding=encoding,construction=construction,direction=direction,mask=mask,binary=str(binary.relative_to(R)),binary_sha256=sha(binary),environment_overrides={'PROFILE_USEC':'1000'}),env)
for v,files in M['sources'].items():
 for n,h in files.items():assert sha(S/v/n)==h
M['status']='complete';save();print('12 matched captures and2 calibrations complete')
