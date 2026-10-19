#!/usr/bin/env python3
"""Fixed600s correctness only. No performance windows are launched."""
from pathlib import Path
import datetime,difflib,hashlib,io,json,os,resource,shutil,subprocess,tarfile,time
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
repo=Path.cwd();p=Path(__file__).resolve().parent;out=p/'validation';out.mkdir();root=repo/'scratch/arm-corrected-neon';root.mkdir();f=json.loads((p/'inputs-freeze.json').read_text());start=time.monotonic();state={'status':'running','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':[],'variants':{}};refs={};snapshots={}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def save():(out/'result.json').write_text(json.dumps(state,indent=2)+'\n')
def run(cmd,name,cwd,negative=False):
 left=600-(time.monotonic()-start);assert left>0
 rec={'name':name,'command':[str(x).replace(str(repo),'<repo>')for x in cmd],'cwd':str(cwd.relative_to(repo)),'started_utc':now(),'negative_control':negative};state['commands'].append(rec);save();env=os.environ.copy()
 if negative:env['ASAN_OPTIONS']='symbolize=0';rec['ASAN_OPTIONS']='symbolize=0'
 try:r=subprocess.run(cmd,cwd=cwd,capture_output=True,timeout=min(left,120),env=env);stdout,stderr,code=r.stdout,r.stderr,r.returncode
 except subprocess.TimeoutExpired as e:stdout,stderr,code=e.stdout or b'',e.stderr or b'',124
 for suffix,data in [('stdout',stdout),('stderr',stderr)]:
  (out/(name+'.'+suffix)).write_text(data.decode(errors='replace').replace(str(repo),'<repo>'))
 rec.update(finished_utc=now(),returncode=code);save()
 if negative:assert code not in [0,124],(name,code)
 else:assert code==0,(name,code)
 return stdout
native=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3'];san=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];inc=['-Isrc','-Icompat','-Ivendor/redis'];common=['compat/standalone.c','vendor/redis/siphash.c','-lm'];oracles={'all_match_guard_oracle_v2':[[]],'scan_interval_oracle':[[]],'wide_scan_oracle':[['7'],['19']],'live_widen_scan_oracle':[['7'],['19']],'resize_generation_oracle':[[]]}
aa=repo/'scratch/arm-corrected-scan/base';aa_binary=aa/'build/btree-bench';files=list(f['source_sha256'])
try:
 assert sorted(os.sched_getaffinity(0))==[2];assert sha(aa_binary)==f['aa_binary_sha256'];state['aa_binary_before']=sha(aa_binary)
 for name in ['src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','compat/server.h','vendor/redis/siphash.c']:assert sha(aa/name)==f['source_sha256'][name]
 assert sha(p/'all_match_guard_oracle_v2.c')==f['v2_oracle_sha256']
 state['compiler']=run(['clang','--version'],'compiler',repo).decode()
 archive=subprocess.check_output(['git','archive',f['source_commit'],'src','compat','vendor','bench','tests','Makefile'],cwd=repo,timeout=30);state['archive_sha256']=hashlib.sha256(archive).hexdigest()
 for variant in ['base','A','B','C']:
  source=root/variant;source.mkdir();tarfile.open(fileobj=io.BytesIO(archive)).extractall(source,filter='data');assert {x:sha(source/x)for x in files}==f['source_sha256'];shutil.copyfile(p/'all_match_guard_oracle_v2.c',source/'tests/all_match_guard_oracle_v2.c')
  if variant!='base':
   v=f['variants'][variant];assert sha(p/'variants'/variant/'candidate.patch')==v['patch_sha256'];run(['patch','-p1','-i',str(p/'variants'/variant/'candidate.patch')],variant+'-patch',source);assert sha(source/'src/zset_btree.c')==v['source_sha256']
  before={x:sha(source/x)for x in files+['tests/all_match_guard_oracle_v2.c']}
  try:
   for mode,flags,build in [('native',native,'build'),('san',san,'build/san')]:
    output=run(['make','CC=clang','BUILD='+build,'CFLAGS='+' '.join(flags),'LDFLAGS='+('-fsanitize=address,undefined'if mode=='san'else ''),'all','check'],variant+'-'+mode+'-original43',source);assert b'43 passed' in output and b'0 failed, 43 total' in output
    for oracle,seeds in oracles.items():
     binary=build+'/'+oracle;run(['clang',*inc,*flags,'tests/'+oracle+'.c',*common,'-o',binary],variant+'-'+mode+'-'+oracle+'-build',source)
     for seed in seeds:
      label=variant+'-'+mode+'-'+oracle+('-'+seed[0]if seed else '');output=run([binary,*seed],label,source);key=(mode,oracle,tuple(seed))
      assert b'PASS' in output
      if variant=='base':refs[key]=output
      else:assert output==refs[key],('semantic-output-mismatch',label)
    if variant!='base':
     binary=build+'/portable-v2';run(['clang',*inc,*flags,'-D'+f['variants'][variant]['portable_macro'],'tests/all_match_guard_oracle_v2.c',*common,'-o',binary],variant+'-'+mode+'-portable-build',source);assert run([binary],variant+'-'+mode+'-portable-v2',source)==refs[mode,'all_match_guard_oracle_v2',()]
   run(['objdump','-dSl','--disassemble=zbtIndexScanSlot','build/btree-bench'],variant+'-native-codegen',source)
   run(['objcopy','--dump-section','.text=build/text.bin','build/btree-bench'],variant+'-text-section',source)
   assert {x:sha(source/x)for x in before}==before
   snapshots[variant]={'source_hashes':before,'timing_binary_sha256':sha(source/'build/btree-bench'),'text_sha256':sha(source/'build/text.bin'),'binaries':{str(x.relative_to(source)):sha(x)for x in (source/'build').rglob('*')if x.is_file()}}
   state['variants'][variant]={'eligible':True}
  except BaseException as e:
   state['variants'][variant]={'eligible':False,'error':type(e).__name__+': '+str(e)};save()
   if variant=='base':raise
 # Fault controls are isolated from every original candidate source/build.
 source=(root/'A/src/zset_btree.c').read_text();mutations={
  'fold':('            if (tag == 1)\n                equal = vorrq_u8(equal, vceqq_u8(bytes, vdupq_n_u8(0)));','            /* Deliberate fault: omit folded-zero equality. */'),
  'order':('first_word * 8 + (__builtin_ctzll(mask) >> 2)','first_word * 8 + 15U - (__builtin_ctzll(mask) >> 2)'),
  'tail':('    for (unsigned int w = first_word; w < words; w++) {','    if (first_word) return found; /* Deliberate omitted residual. */\n    for (unsigned int w = first_word; w < words; w++) {'),
  'overread':('first_word + 2 <= words','first_word < words')}
 for name,(old,new)in mutations.items():
  assert source.count(old)==1,(name,source.count(old));changed=source.replace(old,new);dest=root/('fault-'+name);dest.mkdir();tarfile.open(fileobj=io.BytesIO(archive)).extractall(dest,filter='data');(dest/'src/zset_btree.c').write_text(changed);shutil.copyfile(p/'all_match_guard_oracle_v2.c',dest/'tests/all_match_guard_oracle_v2.c');(dest/'build').mkdir()
  (out/('fault-'+name+'.patch')).write_text(''.join(difflib.unified_diff(source.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  for mode,flags in [('native',native),('san',san)]:
   binary='build/'+mode;run(['clang',*inc,*flags,'tests/all_match_guard_oracle_v2.c',*common,'-o',binary],'fault-'+name+'-'+mode+'-build',dest);run([binary],'fault-'+name+'-'+mode,dest,negative=True)
 run(['objcopy','--dump-section','.text='+str(root/'aa-text.bin'),str(aa_binary)],'aa-text-section',repo)
 assert snapshots['base']['text_sha256']==sha(root/'aa-text.bin');assert sha(aa_binary)==state['aa_binary_before'];state['aa_binary_after']=sha(aa_binary)
 for variant,entry in snapshots.items():assert {x:sha(root/variant/x)for x in entry['source_hashes']}==entry['source_hashes']
 (out/'freeze.json').write_text(json.dumps({'source_commit':f['source_commit'],'compiler':state['compiler'],'cpu_affinity':sorted(os.sched_getaffinity(0)),'baseline_binary':f['aa_binary_sha256'],'snapshots':snapshots,'timing_frontend_relative_paths_identical':True,'native_flags':native,'sanitize_flags':san},indent=2)+'\n');state['status']='complete'
except BaseException as e:state.update(status='failed',error=type(e).__name__+': '+str(e));raise
finally:state.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
