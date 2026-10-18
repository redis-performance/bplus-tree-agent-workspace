from pathlib import Path
import csv,datetime,difflib,hashlib,json,os,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-counters-011';S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();D=P/'raw';D.mkdir()
F=json.loads((P.parent/'DIAG-019/attempt-002/freeze.json').read_text());variants=['control-on','C-on','control-off','C-off'];M=dict(status='preparing',base_commit=F['base_commit'],scope='reset/dump execution counters, not timings',plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),snapshots={},runs=[],captures=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,args,B,out=None,env=None):
 assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,18,6,2,tzinfo=datetime.timezone.utc)
 out=out or D/(tag+'.stdout');err=D/(tag+'.stderr');r=dict(name=tag,command=[x.replace(str(R),'<workspace>') for x in args],cwd=str(B.relative_to(R)),started_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)))
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(args,cwd=B,stdout=o,stderr=e,env=env,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(r);save();assert rc==0,(tag,rc)
 return out
header=Path('/Library/Developer/CommandLineTools/usr/lib/clang/17/include/profile/instr_prof_interface.h');M['local_interface_sha256']=sha(header);M['interface']=dict(header='Clang17 profile/instr_prof_interface.h',reset='void __llvm_profile_reset_counters(void)',dump='int __llvm_profile_dump(void)',scope='dump prevents process-exit redump; reset clears counters and dumped flag')
for v in variants:
 B=S/v;B.mkdir()
 for n,h in F['files'][v].items():
  src=R/F['snapshot']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 p=B/'bench/batch_lookup.c';old=p.read_text();s=old.replace('#include <errno.h>','#include <errno.h>\n#include <profile/instr_prof_interface.h>\n#ifndef __LLVM_INSTR_PROFILE_GENERATE\n#error Instrumentation required\n#endif')
 s=s.replace('uint64_t start=now_ns();','__llvm_profile_reset_counters();uint64_t start=now_ns();').replace(' serverAssert(r.checksum==expected',' serverAssert(__llvm_profile_dump()==0);\n serverAssert(r.checksum==expected');assert s!=old;p.write_text(s)
 (P/(v+'-scope.patch')).write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='a/bench/batch_lookup.c',tofile='b/bench/batch_lookup.c')))
 M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
B=S/'calibration';B.mkdir();(B/'calibrate.c').write_text('''#include <profile/instr_prof_interface.h>
#include <stdio.h>
#ifndef __LLVM_INSTR_PROFILE_GENERATE
#error Instrumentation required
#endif
static volatile unsigned sink;
__attribute__((noinline)) void known_before(void){sink++;}
__attribute__((noinline)) void known_scope(void){sink++;}
__attribute__((noinline)) void known_after(void){sink++;}
int main(void){for(unsigned i=0;i<10;i++)known_before();__llvm_profile_reset_counters();for(unsigned i=0;i<20;i++)known_scope();if(__llvm_profile_dump())return 2;for(unsigned i=0;i<30;i++)known_after();printf("PASS sink=%u\\n",sink);return sink!=60;}
''');M['calibration_source_sha256']=sha(B/'calibrate.c');M['status']='frozen';M['frozen_utc']=utc();save()
flags=['cc','-std=c11','-g','-O3','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG','-fprofile-instr-generate','-fcoverage-mapping']
run('cal-build',flags+['calibrate.c','-o','calibrate'],B);M['calibration_binary_sha256']=sha(B/'calibrate');save()
for v in variants:
 B=S/v;run(v+'-build',flags+['-Isrc','-Icompat','-Ivendor/redis','bench/batch_lookup.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/census'],B);M['snapshots'][v]['binary_sha256']=sha(B/'build/census');save()
def export(tag,B,binary,args):
 raw=B/(tag+'.profraw');data=B/(tag+'.profdata');j=B/(tag+'-export.json');out=run(tag+'-capture',[binary,*args],B,env=dict(os.environ,LLVM_PROFILE_FILE=str(raw)))
 run(tag+'-merge',['xcrun','llvm-profdata','merge','-sparse',str(raw),'-o',str(data)],B)
 run(tag+'-export',['xcrun','llvm-cov','export',str(B/binary),'-instr-profile='+str(data)],B,out=j)
 fs=[f for d in json.loads(j.read_text())['data'] for f in d['functions']];return out,fs,dict(raw=str(raw.relative_to(R)),raw_sha256=sha(raw),profdata=str(data.relative_to(R)),profdata_sha256=sha(data),export=str(j.relative_to(R)),export_sha256=sha(j))
def select(fs,name):
 hits=[f for f in fs if f['name']==name or f['name'].endswith(':'+name)];assert len(hits)==1,(name,len(hits));return hits[0]
B=S/'calibration';out,fs,meta=export('cal',B,'./calibrate',[]);assert 'PASS sink=60' in out.read_text();counts={n:select(fs,n)['count'] for n in ['known_before','known_scope','known_after']};assert counts==dict(known_before=0,known_scope=20,known_after=0);M['calibration']=dict(counts=counts,**meta);save();print('scope control PASS',flush=True)
for v in variants:
 B=S/v
 for seed,qseed in [(83103,83119),(83111,83123)]:
  for batch in [1,16]:
   tag=f'{v}-s{seed}-b{batch}';args=['--size','8192','--ops','32768','--member-bytes','16','--batch-size',str(batch),'--layout','hit','--seed',str(seed),'--query-seed',str(qseed),'--warmup-passes','3'];out,fs,meta=export(tag,B,'build/census',args);row=next(csv.DictReader(out.open()));assert int(row['operations'])==32768 and int(row['hits'])==32768 and int(row['checksum'])==4*8192*8193//2
   required=dict(zbtreeScores=32768//batch,dictGenHashFunction=32768,zbtreeInsertNew=0,zbtreeFree=0,work=1)
   for n,c in required.items():assert select(fs,n)['count']==c,(tag,n,select(fs,n)['count'],c)
   names=['zbtreeScores','zbtIndexFind','zbtScoreLeafFindMember','dictGenHashFunction','siphash','zbtreeInsertNew','zbtreeFree','work']+(['zbtInlineTagSearch'] if v.startswith('C-') else []);selected=[]
   for name in names:
    f=select(fs,name);branches=[]
    for b in f['branches']:
     file=Path(f['filenames'][b[6]]);snippet='\n'.join(file.read_text().splitlines()[b[0]-1:b[2]]);branches.append(dict(start_line=b[0],start_column=b[1],end_line=b[2],end_column=b[3],true=b[4],false=b[5],file=str(file.relative_to(B)),source=snippet))
    selected.append(dict(name=name,count=f['count'],branches=branches))
   target=P/(tag+'-counts.json');target.write_text(json.dumps(selected,indent=2)+'\n');M['captures'].append(dict(variant=v,seed=seed,query_seed=qseed,batch=batch,counts=str(target.relative_to(R)),counts_sha256=sha(target),csv=str(out.relative_to(R)),tree_bytes=int(row['tree_bytes']),**meta));save();print(tag,'scoped counts PASS',flush=True)
for v,d in M['snapshots'].items():
 B=R/d['path'];assert sha(B/'build/census')==d['binary_sha256']
 for n,h in d['files'].items():assert sha(B/n)==h
M['status']='complete';save()
