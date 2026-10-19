#!/usr/bin/env python3
"""Preparation only. Never execute enabled profile binary."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,os,re,shlex,time,csv,io,statistics
R=Path.cwd();E=Path(__file__).resolve().parent;S=R/'scratch/m6-corrected-member-index-profile';BASE=E.parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def generic(s):
 s=s.replace(str(R),'<workspace>')
 s=re.sub('/'+'Users/[^\\s\"\']+','<user-path>',s)
 return re.sub('/'+'(?:private/)?var/folders/[^\\s\"\']+','<compiler-temp>',s)
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
assert not (E/'PREPARATION.json').exists(),'no overwrite'
S.mkdir(exist_ok=True);(S/'logs').mkdir(exist_ok=True)
start=time.monotonic();records=[]
def command(args,name,bound=180):
 assert time.monotonic()-start<720
 assert not (S/'logs'/(name+'.stdout')).exists()
 t=time.monotonic();before=utc()
 try:p=subprocess.run(list(map(str,args)),capture_output=True,timeout=min(bound,720-(time.monotonic()-start)));out,err,rc=p.stdout,p.stderr,p.returncode;timeout=False
 except subprocess.TimeoutExpired as ex:out,err,rc,timeout=ex.stdout or b'',ex.stderr or b'',None,True
 rec=dict(name=name,command=[generic(str(x)) for x in args],bound_seconds=bound,started_utc=before,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=rc,timed_out=timeout,raw={})
 for ch,data in [('stdout',out),('stderr',err)]:
  p=S/'logs'/(name+'.'+ch);p.write_bytes(data);rec['raw'][ch]=dict(path=str(p.relative_to(R)),sha256=sha(p))
 records.append(rec);save(E/'commands.json',records)
 assert rc==0 and not timeout,(name,rc,generic(err.decode(errors='replace')))
 return out.decode(),err.decode()
source=Path('bench/microbench.c').read_text();hooks={
 '#endif\n\nstatic volatile uint64_t sink;':'#endif\n\n#ifdef PROFILE_SAMPLE\n#include "night-rank-sampler.h"\n#endif\n\nstatic volatile uint64_t sink;',
 '        uint64_t start = now_ns();\n':'        uint64_t start = now_ns();\n#ifdef PROFILE_SAMPLE\n        sample_init();\n        sample_start();\n#endif\n',
 '        uint64_t elapsed = now_ns() - start;\n':'#ifdef PROFILE_SAMPLE\n        sample_stop(cases[c]);\n#endif\n        uint64_t elapsed = now_ns() - start;\n'}
diag=source
for old,new in hooks.items():assert diag.count(old)==1;diag=diag.replace(old,new)
restored=diag
for old,new in reversed(list(hooks.items())):restored=restored.replace(new,old)
assert restored==source
(E/'microbench-profile.c').write_text(diag);(E/'night-rank-sampler.h').write_bytes((BASE/'002-rank/night-rank-sampler.h').read_bytes());save(E/'source-equivalence.json',dict(original_sha256=sha('bench/microbench.c'),diagnostic_sha256=sha(E/'microbench-profile.c'),remove_three_conditional_hook_blocks_restores_exact_bytes=True,sampler_original_sha256=sha(BASE/'002-rank/night-rank-sampler.h'),sampler_copy_sha256=sha(E/'night-rank-sampler.h')))
cc=shlex.split(os.environ.get('CC','cc'));compiler,_=command(cc+['--version'],'compiler')
common=['-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-Isrc','-Icompat','-Ivendor/redis','-Ibench','-I'+str(E),'-ffile-prefix-map='+str(R)+'=<source>','-fdebug-prefix-map='+str(R)+'=<source>','-fdebug-compilation-dir=.']
flags={mode:common+(['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if mode=='sanitize' else ['-O3']) for mode in ['native','sanitize']}
for mode in flags:
 build=S/mode;build.mkdir(exist_ok=True)
 for name,file in [('tree','src/zset_btree.c'),('standalone','compat/standalone.c'),('siphash','vendor/redis/siphash.c')]:command(cc+flags[mode]+['-c',file,'-o',str(build/(name+'.o'))],mode+'-'+name)
binaries={}
for label,mode,file,extra in [('original','native','bench/microbench.c',[]),('disabled','native',str(E/'microbench-profile.c'),[]),('enabled','native',str(E/'microbench-profile.c'),['-DPROFILE_SAMPLE']),('sanitize-disabled','sanitize',str(E/'microbench-profile.c'),[])]:
 build=S/mode;obj=build/(label+'.o');binary=build/label;command(cc+flags[mode]+extra+['-c',file,'-o',str(obj)],label+'-object');command(cc+flags[mode]+[str(obj)]+[str(build/(x+'.o')) for x in ['tree','standalone','siphash']]+['-lm','-o',str(binary)],label+'-link');binaries[label]=str(binary.relative_to(R))
rows=[]
for label in ['original','disabled','sanitize-disabled']:
 for case in ['lookup-hit','lookup-miss','rank','scan']:
  for seed in [1,2]:
   cmd=[binaries[label],'--case',case,'--size','1000','--ops','2003','--member-bytes','16','--seed',str(seed),'--warmup-passes','3'];out,err=command(cmd,f'check-{label}-{case}-{seed}');data=list(csv.DictReader(io.StringIO(out)));assert len(data)==1 and not err;row=data[0];assert row['case']==case and int(row['size'])==1000 and int(row['seed'])==seed and int(row['requested_ops'])==2003 and int(row['member_bytes'])==16 and int(row['warmup_passes'])==3 and int(row['tree_bytes'])>0
   assert int(row['operations'])==2003 if case!='scan' else int(row['operations'])>=3000
   if case=='lookup-miss':assert int(row['checksum'])==0
   if case!='scan':assert int(row['traversals'])==0
   else:assert int(row['traversals'])==3
   row.update(binary=label);rows.append(row)
# Rebuild the exact shuffled order independently for checksum expectations.
def model(n,ops,seed):
 mask=(1<<64)-1
 def rng():
  nonlocal seed
  seed=(seed+0x9e3779b97f4a7c15)&mask;v=seed;v=((v^(v>>30))*0xbf58476d1ce4e5b9)&mask;v=((v^(v>>27))*0x94d049bb133111eb)&mask;return v^(v>>31)
 for _ in range(16):rng()
 order=list(range(n))
 for i in range(n,1,-1):j=rng()%i;order[i-1],order[j]=order[j],order[i-1]
 return sum(order[i%n] for i in range(ops))
for row in rows:
 if row['case'] in ['lookup-hit','rank']:assert int(row['checksum'])==model(1000,2003,int(row['seed']))
 # Scan's unchanged callback verifies exact key/score bits and total coverage, allowing duplicates.
 ref=next(r for r in rows if r['binary']=='original' and r['case']==row['case'] and r['seed']==row['seed'])
 assert all(row[k]==ref[k] for k in ['operations','checksum','traversals'])
 if row['binary']=='disabled':assert row['tree_bytes']==ref['tree_bytes']
save(E/'validation.json',dict(status='PASS',rows=rows,invocations=24,tests='Unchanged built-in benchmark semantic assertions plus independent shuffle/checksum model; scan duplicate semantics preserved',timing_fields_used=False,enabled_profile_binary_executed=False,owned_bytes='Native disabled equals original; sanitizer bytes recorded separately because allocator size classes may differ'))
# Reuse validated 43-test source identity and retained results, without rerunning.
reuse=json.loads((BASE/'013-corrected-iterator-profile/reused-tests.json').read_text());assert all(sha(p)==h for p,h in reuse['source_identity'].items());assert all(sha(BASE/p)==h for p,h in reuse['native_sanitizer_evidence'].items());save(E/'reused-tests.json',reuse)
for label,path in binaries.items():
 command(['/usr/bin/nm','-n',path],label+'-nm');command(['/usr/bin/otool','-tvV',path],label+'-otool')
 command(['/usr/bin/otool','-tvV',str(S/('sanitize' if label=='sanitize-disabled' else 'native')/(label+'.o'))],label+'-frontend-otool')
for mode in flags:command(['/usr/bin/otool','-tvV',str(S/mode/'tree.o')],mode+'-tree-otool')
inputs=['src/zset_btree.c','src/zset_btree.h','compat/server.h','compat/standalone.c','bench/microbench.c','vendor/redis/siphash.c','vendor/redis/sds.h','vendor/redis/testhelp.h','tests/upstream.c']
report=dict(status='BUILDS_AND_BOUNDED_CORRECTNESS_PASS; capture preparation still requires static review/freeze',participant='/root/followup_proposal_c',backend='Inherited Codex/GPT-6 family; exact model/token/currency cost unknown',compiler=generic(compiler),flags={m:[generic(x) for x in f] for m,f in flags.items()},binaries={k:dict(path=v,sha256=sha(v)) for k,v in binaries.items()},inputs_sha256={p:sha(p) for p in inputs},all_build_objects_sha256={str(p.relative_to(R)):sha(p) for p in S.rglob('*.o')},reused_original_tests_per_build=43,correctness_invocations=24,enabled_executed=False,wall_seconds=time.monotonic()-start,source_only_conditional_hooks=True,failures=['Initial attempt to read nonexistent011 top-level validation.json stopped with FileNotFoundError; reused013 pinned43-test mapping instead. No evidence changed.'])
save(E/'PREPARATION.json',report);print('PASS build/correctness; enabled never executed',round(time.monotonic()-start,3),'seconds')
