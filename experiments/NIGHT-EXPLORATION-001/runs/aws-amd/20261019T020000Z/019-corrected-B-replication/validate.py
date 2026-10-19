#!/usr/bin/env python3
import argparse,datetime,hashlib,io,json,os,pathlib,shutil,subprocess,tarfile,time
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);p.add_argument('--baseline',required=True,type=pathlib.Path);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;out=here/'validation';out.mkdir();expected=json.loads((here/'expected.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic();records=[];state={'status':'running','started_utc':now(),'commands':records};assert sorted(os.sched_getaffinity(0))==[2]
def save():(out/'result.json').write_text(json.dumps(state,indent=2)+'\n')
def run(cmd,name,cwd):
 left=600-(time.monotonic()-start);assert left>0;rec={'name':name,'command':[str(x).replace(str(a.checkout),'<checkout>') for x in cmd],'started_utc':now()};records.append(rec);save()
 try:r=subprocess.run(cmd,cwd=cwd,capture_output=True,timeout=min(left,120));stdout,stderr,code=r.stdout,r.stderr,r.returncode
 except subprocess.TimeoutExpired as e:stdout,stderr,code=e.stdout or b'',e.stderr or b'',124
 for suffix,data in [('stdout',stdout),('stderr',stderr)]:
  text=data.decode(errors='replace').replace(str(a.checkout),'<checkout>');(out/(name+'.'+suffix)).write_text(text)
 rec.update(finished_utc=now(),returncode=code);save();assert code==0,(name,code);return stdout
files=list(expected['source_hashes']);original_bin=a.baseline/'build/adapter-requalification/btree-bench'
try:
 assert sha(here/'candidate.patch')==expected['patch_sha256'];assert sha(here/'all_match_guard_oracle_v2.c')==expected['oracle_sha256'];assert sha(original_bin)==expected['aa_binary_sha256'];state['baseline_before']={f:sha(a.baseline/f) for f in files};assert state['baseline_before']==expected['source_hashes'];state['baseline_binary_before']=sha(original_bin)
 compiler=run(['clang','--version'],'compiler',a.checkout).decode();assert 'clang version 18.1.3' in compiler
 archive=run(['git','archive',expected['commit'],'src','compat','vendor','bench','tests','Makefile'],'archive',a.checkout)
 # Git archive contains only tracked inputs from the explicitly pinned source.
 (out/'archive.stdout').unlink();state['archive_sha256']=hashlib.sha256(archive).hexdigest()
 oracles={'all_match_guard_oracle':[[]],'scan_interval_oracle':[[]],'wide_scan_oracle':[['7'],['19']],'live_widen_scan_oracle':[['7'],['19']],'resize_generation_oracle':[[]]}
 native=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3'];san=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];snapshots={}
 for variant in ['base','B']:
  source=here/variant;source.mkdir();tarfile.open(fileobj=io.BytesIO(archive)).extractall(source,filter='data');assert {f:sha(source/f) for f in files}==expected['source_hashes'];shutil.copyfile(here/'all_match_guard_oracle_v2.c',source/'tests/all_match_guard_oracle.c')
  if variant=='B':run(['patch','-p1','-i',str(here/'candidate.patch')],variant+'-patch',source);assert sha(source/'src/zset_btree.c')==expected['candidate_c_sha256']
  before={f:sha(source/f) for f in files+['tests/all_match_guard_oracle.c']}
  for mode,flags in [('native',native),('san',san)]:
   run(['make','CC=clang','BUILD=build/'+mode,'CFLAGS='+' '.join(flags),'LDFLAGS='+('-fsanitize=address,undefined' if mode=='san' else ''),'all','check'],variant+'-'+mode+'-original43',source)
   for oracle,seeds in oracles.items():
    run(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis','tests/'+oracle+'.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+mode+'/'+oracle],variant+'-'+mode+'-'+oracle+'-build',source)
    for seed in seeds:run(['build/'+mode+'/'+oracle,*seed],variant+'-'+mode+'-'+oracle+('-'+seed[0] if seed else ''),source)
   if variant=='B':
    run(['clang',*flags,'-DZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE','-Isrc','-Icompat','-Ivendor/redis','tests/all_match_guard_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+mode+'/portable'],variant+'-'+mode+'-portable-build',source);run(['build/'+mode+'/portable'],variant+'-'+mode+'-portable',source)
  assert {f:sha(source/f) for f in before}==before;snapshots[variant]={'source_hashes':before,'binaries':{str(f.relative_to(source)):sha(f) for f in (source/'build').rglob('*') if f.is_file()}}
 assembly=run(['objdump','-d','--disassemble=zbtIndexScanSlot','build/native/btree-bench'],'B-native-codegen',here/'B').decode();assert all(x in assembly for x in ['movdqu','pcmpeqb','pmovmskb']);state['baseline_after']={f:sha(a.baseline/f) for f in files};state['baseline_binary_after']=sha(original_bin);assert state['baseline_after']==state['baseline_before'];assert state['baseline_binary_after']==state['baseline_binary_before'];freeze={'commit':expected['commit'],'compiler':compiler,'cpu_affinity':sorted(os.sched_getaffinity(0)),'baseline_binary':expected['aa_binary_sha256'],'snapshots':snapshots};(out/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n');state['status']='complete'
except BaseException as e:state.update(status='failed',error=type(e).__name__+': '+str(e));raise
finally:state.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
