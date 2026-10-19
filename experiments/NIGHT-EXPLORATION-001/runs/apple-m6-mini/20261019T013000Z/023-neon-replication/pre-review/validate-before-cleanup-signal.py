#!/usr/bin/env python3
"""Authorized, bounded correctness preparation only; never runs benchmark workloads."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,difflib,hashlib,json,os,re,resource,shutil,signal,struct,subprocess,time
R=Path.cwd();E=Path(__file__).resolve().parent
P=E/'validation';S=R/'scratch/m6-neon-validation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def load(p):return json.loads(Path(p).read_text())
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def alive(pid):
 try:os.killpg(pid,0);return True
 except ProcessLookupError:return False
def cancelled(signum,frame):raise KeyboardInterrupt('validation owner cancelled')
def expired(signum,frame):raise TimeoutError('validation total/UTC deadline')
def text_section(binary):
 b=binary.read_bytes();assert struct.unpack_from('<I',b)[0]==0xfeedfacf
 off=32
 for _ in range(struct.unpack_from('<I',b,16)[0]):
  cmd,size=struct.unpack_from('<II',b,off)
  if cmd==0x19:
   for j in range(struct.unpack_from('<I',b,off+64)[0]):
    q=off+72+80*j
    if b[q:q+16].split(b'\0')[0]==b'__text':
     extent=struct.unpack_from('<Q',b,q+40)[0];fileoff=struct.unpack_from('<I',b,q+48)[0];return b[fileoff:fileoff+extent]
  off+=size
 raise AssertionError('Mach-O __text missing')
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--ack',required=True);a=parser.parse_args()
 plan=load(E/'PLAN.json');freeze=load(E/'freeze.json');manifest=load(E/'source-manifest.json');ack=load(Path(a.ack))
 assert ack['status']=='authorized' and re.fullmatch('[0-9a-f]{40}',ack['published_commit'])
 for field,name in [('driver_sha256','validate.py'),('plan_sha256','PLAN.json'),('freeze_sha256','freeze.json')]:assert ack[field]==sha(E/name)
 reviewers={r['reviewer'] for r in ack['reviews'] if r['status']=='PASS'};assert '/root' in reviewers and '/root/followup_proposal_b' in reviewers
 assert not P.exists() and not S.exists(),'preserve all prior attempts; no retry/overwrite'
 P.mkdir();S.mkdir(parents=True);(S/'logs').mkdir()
 state=dict(status='RUNNING',started_utc=utc(),commands=[],variants={},participant='/root/followup_proposal_a',backend='Inherited Codex/GPT-6 family; exact serving model/token/currency costs unknown',benchmark_workloads_executed=0)
 start=time.monotonic();deadline=min(time.time()+600,datetime.fromisoformat(plan['experimental_cutoff_utc']).timestamp(),datetime.fromisoformat(ack.get('absolute_stop_utc',plan['experimental_cutoff_utc'])).timestamp())
 assert deadline-time.time()>20
 resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 for sig in [signal.SIGTERM,signal.SIGHUP]:signal.signal(sig,cancelled)
 signal.signal(signal.SIGALRM,expired);signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.time()-10))
 def persist():save(P/'result.json',state)
 def redacted(data):return data.decode(errors='replace').replace(str(R),'<workspace>')
 def run(cmd,name,cwd,negative=False):
  assert time.monotonic()-start<590 and deadline-time.time()>10
  paths={c:S/'logs'/(name+'.'+c) for c in ['stdout','stderr']};assert not any(p.exists() for p in paths.values())
  cap=min(120,deadline-time.time()-10,590-(time.monotonic()-start));assert cap>0
  rec=dict(name=name,command=list(map(str,cmd)),cwd=str(cwd.relative_to(R)),started_utc=utc(),timeout_seconds=cap,negative_control=negative,timed_out=False,raw={})
  if negative:rec['environment_overrides']={'ASAN_OPTIONS':'symbolize=0'}
  state['commands'].append(rec);persist();child=None;t=time.monotonic()
  try:
   with paths['stdout'].open('xb') as out,paths['stderr'].open('xb') as err:
    env=os.environ.copy()
    if negative:env['ASAN_OPTIONS']='symbolize=0'
    child=subprocess.Popen(cmd,cwd=cwd,stdout=out,stderr=err,env=env,start_new_session=True)
    while child.poll() is None:
     if time.monotonic()-t>=cap or time.time()>=deadline-10:rec['timed_out']=True;break
     time.sleep(.02)
  except BaseException as ex:rec['exception_type']=type(ex).__name__;raise
  finally:
   mask=signal.pthread_sigmask(signal.SIG_BLOCK,{signal.SIGALRM})
   try:
    if child is not None:
     if alive(child.pid):
      try:os.killpg(child.pid,signal.SIGTERM);rec['owned_group_TERM']=True
      except ProcessLookupError:pass
      until=time.monotonic()+1
      while alive(child.pid) and time.monotonic()<until:time.sleep(.02)
      if alive(child.pid):
       try:os.killpg(child.pid,signal.SIGKILL);rec['owned_group_KILL']=True
       except ProcessLookupError:pass
     try:child.wait(timeout=5);rec['child_reaped']=True
     except subprocess.TimeoutExpired:rec['child_reaped']=False
     until=time.monotonic()+3
     while alive(child.pid) and time.monotonic()<until:time.sleep(.02)
     rec.update(owned_group_empty=not alive(child.pid),returncode=child.returncode)
    rec.update(finished_utc=utc(),wall_seconds=time.monotonic()-t)
    for channel,path in paths.items():
     if path.exists():
      raw=path.read_bytes();public=P/(name+'.'+channel);public.write_text(redacted(raw));rec['raw'][channel]=dict(path=str(path.relative_to(R)),sha256=sha(path),bytes=len(raw),public_path=str(public.relative_to(R)),public_sha256=sha(public))
    rec['release_safe']=bool(rec.get('child_reaped') and rec.get('owned_group_empty'));persist()
   finally:signal.pthread_sigmask(signal.SIG_SETMASK,mask)
  assert time.time()<deadline and time.monotonic()-start<600,'post-child deadline'
  assert not rec['timed_out'] and rec['release_safe'],name
  assert (rec['returncode'] not in [0,124,-signal.SIGKILL] if negative else rec['returncode']==0),(name,rec.get('returncode'))
  return paths['stdout'].read_bytes()
 refs={};snapshots={};source_before={};input_before={}
 try:
  input_before={p:sha(p) for p in freeze['files_sha256']};assert input_before==freeze['files_sha256']
  assert plan['validation_cap_seconds']==600
  native=plan['native_flags'];san=plan['sanitize_flags'];inc=['-Isrc','-Icompat','-Ivendor/redis'];common=['compat/standalone.c','vendor/redis/siphash.c','-lm']
  oracles={'all_match_guard_oracle_v2':[[]],'scan_interval_oracle':[[]],'wide_scan_oracle':[['7'],['19']],'live_widen_scan_oracle':[['7'],['19']],'resize_generation_oracle':[[]]}
  state['compiler']=run(['clang','--version'],'compiler',R).decode();state['flags']=dict(native=native,sanitize=san,includes=inc,common=common)
  assert set(manifest['variants'])=={'base','A','B','C'}
  for variant in ['base','A','B','C']:
   entry=manifest['variants'][variant];tree=R/entry['worktree'];assert tree==R/('worktrees/m6-neon-'+variant)
   source_before[variant]={p:sha(tree/p) for p in entry['source_hashes']};assert source_before[variant]==entry['source_hashes']
   assert sha(tree/'tests/all_match_guard_oracle_v2.c')=='b01a762f925a679a6342f5258824ca4743b0020a47982f015be4916050953ded'
   macros=run(['clang',*native,*inc,'-dM','-E','src/zset_btree.c'],variant+'-native-macros',tree).decode()
   assert re.search(r'^#define __aarch64__ 1$',macros,re.M) and re.search(r'^#define __ARM_NEON 1$',macros,re.M)
   if variant!='base':assert re.search(r'^#define '+('ZBT_NATIVE_LEAF_TAGS_C' if variant=='C' else 'ZBT_LEAF_TAG_MATCHES_NEON')+r' 1$',macros,re.M)
   for mode,flags in [('native',native),('san',san)]:
    build='build/'+mode
    output=run(['make','CC=clang','BUILD='+build,'CFLAGS='+' '.join(flags),'LDFLAGS='+('-fsanitize=address,undefined' if mode=='san' else ''),'all','check'],variant+'-'+mode+'-original43',tree)
    assert b'43 passed' in output and b'0 failed, 43 total' in output
    for oracle,seeds in oracles.items():
     binary=build+'/'+oracle
     run(['clang',*inc,*flags,'tests/'+oracle+'.c',*common,'-o',binary],variant+'-'+mode+'-'+oracle+'-build',tree)
     for seed in seeds:
      name=variant+'-'+mode+'-'+oracle+('-'+seed[0] if seed else '')
      output=run([binary,*seed],name,tree);key=(mode,oracle,tuple(seed));assert b'PASS' in output
      if variant=='base':refs[key]=output
      else:assert output==refs[key],('oracle-parity',name)
    if variant!='base':
     binary=build+'/portable-v2';run(['clang',*inc,*flags,'-D'+entry['portable_macro'],'tests/all_match_guard_oracle_v2.c',*common,'-o',binary],variant+'-'+mode+'-portable-build',tree)
     assert run([binary],variant+'-'+mode+'-portable-v2',tree)==refs[(mode,'all_match_guard_oracle_v2',())]
   assembly=run(['otool','-tvV','build/native/btree-bench'],variant+'-native-codegen',tree).decode()
   functions={};label=None
   for line in assembly.splitlines():
    if re.fullmatch(r'_[A-Za-z0-9_.$]+:',line):label=line[:-1];functions[label]=[]
    elif label:functions[label].append(line)
   slot='\n'.join(functions.get('_zbtIndexScanSlot',[]));assert slot,'scan-slot symbol missing'
   if variant!='base':assert re.search(r'\bv\d+\b',slot) and re.search(r'\bshrn',slot) and re.search(r'\bcm(eq|hi|hs)',slot),'native NEON mechanism not established'
   hashes={str(p.relative_to(tree)):sha(p) for p in (tree/'build').rglob('*') if p.is_file() and p.suffix not in ['.o']}
   snapshots[variant]=dict(source_hashes=source_before[variant],binaries=hashes,timing_binary='build/native/btree-bench',timing_binary_sha256=sha(tree/'build/native/btree-bench'),text_sha256=hashlib.sha256(text_section(tree/'build/native/btree-bench')).hexdigest(),native_neon_proved=variant!='base')
   state['variants'][variant]={'eligible':True};persist()
  # Same four original A-derived faults, isolated from candidate trees/builds.
  original=(R/manifest['variants']['A']['worktree']/'src/zset_btree.c').read_text()
  mutations={
   'fold':('            if (tag == 1)\n                equal = vorrq_u8(equal, vceqq_u8(bytes, vdupq_n_u8(0)));','            /* Deliberate fault: omit folded-zero equality. */'),
   'order':('first_word * 8 + (__builtin_ctzll(mask) >> 2)','first_word * 8 + 15U - (__builtin_ctzll(mask) >> 2)'),
   'tail':('    for (unsigned int w = first_word; w < words; w++) {','    if (first_word) return found; /* Deliberate omitted residual. */\n    for (unsigned int w = first_word; w < words; w++) {'),
   'overread':('first_word + 2 <= words','first_word < words')}
  for name,(old,new) in mutations.items():
   assert original.count(old)==1;changed=original.replace(old,new);dest=S/('fault-'+name);dest.mkdir()
   tree=R/manifest['variants']['A']['worktree']
   for relative in source_before['A']:
    target=dest/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(tree/relative,target)
   (dest/'src/zset_btree.c').write_text(changed);(dest/'build').mkdir()
   (P/('fault-'+name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
   for mode,flags in [('native',native),('san',san)]:
    binary='build/'+mode;run(['clang',*inc,*flags,'tests/all_match_guard_oracle_v2.c',*common,'-o',binary],'fault-'+name+'-'+mode+'-build',dest)
    run([binary],'fault-'+name+'-'+mode,dest,negative=True)
  for variant,entry in manifest['variants'].items():assert {p:sha(R/entry['worktree']/p) for p in source_before[variant]}==source_before[variant]
  for variant,snapshot in snapshots.items():assert all(sha(R/manifest['variants'][variant]['worktree']/p)==h for p,h in snapshot['binaries'].items())
  assert {p:sha(p) for p in input_before}==input_before
  assert time.time()<deadline and time.monotonic()-start<600
  save(P/'binary-freeze.json',dict(source_commit=plan['source_commit'],snapshots=snapshots,compiler=state['compiler'],flags=state['flags']))
  state.update(status='PASS',all_original43_invocations=8,positive_semantic_runs=56,forced_portable_runs=6,detected_negative_runs=8,post_input_identities_verified=len(input_before),all_sources_and_binaries_unchanged=True)
 except BaseException as ex:state.update(status='INCOMPLETE_OR_FAILED',error_type=type(ex).__name__,error=str(ex).replace(str(R),'<workspace>'));raise
 finally:
  signal.setitimer(signal.ITIMER_REAL,0)
  post_inputs={p:sha(p) if Path(p).is_file() else None for p in input_before}
  state['post_input_identities_unchanged']=post_inputs==input_before
  state['post_source_identities_unchanged']=all(all((R/manifest['variants'][v]['worktree']/p).is_file() and sha(R/manifest['variants'][v]['worktree']/p)==h for p,h in files.items()) for v,files in source_before.items())
  if not state['post_input_identities_unchanged'] or not state['post_source_identities_unchanged']:state['status']='INCOMPLETE_OR_FAILED'
  state.update(finished_utc=utc(),wall_seconds=time.monotonic()-start,release_safe=all(x.get('release_safe',False) for x in state['commands']),source_snapshots=source_before)
  persist()
if __name__=='__main__':main()
