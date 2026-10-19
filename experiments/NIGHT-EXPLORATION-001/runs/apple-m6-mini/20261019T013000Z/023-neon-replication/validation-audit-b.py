#!/usr/bin/env python3
"""Independent retained-data reconstruction; imports no launcher and runs no child."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,shlex,signal,difflib
R=Path.cwd();E=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def check_hashes(table):
 for p,h in table.items():assert sha(p)==h,p
 return len(table)
def main():
 result=load(E/'validation/result.json');plan=load(E/'PLAN.json');manifest=load(E/'source-manifest.json');freeze=load(E/'validation-freeze.json');bf=load(E/'validation/binary-freeze.json')
 assert result['status']=='PASS';assert len(freeze['files_sha256'])==322;check_hashes(freeze['files_sha256'])
 rows=result['commands'];assert len(rows)==141;assert len({r['name'] for r in rows})==141
 expected=[];native=plan['native_flags'];san=plan['sanitize_flags'];inc=['-Isrc','-Icompat','-Ivendor/redis'];common=['compat/standalone.c','vendor/redis/siphash.c','-lm'];oracle_seeds=[('all_match_guard_oracle_v2',[[]]),('scan_interval_oracle',[[]]),('wide_scan_oracle',[['7'],['19']]),('live_widen_scan_oracle',[['7'],['19']]),('resize_generation_oracle',[[]])]
 def add(name,cmd,cwd,negative=False):expected.append((name,cmd,cwd,negative))
 add('compiler',['clang','--version'],'.')
 for v in ['base','A','B','C']:
  tree=manifest['variants'][v]['worktree'];add(v+'-native-macros',['clang',*native,*inc,'-dM','-E','src/zset_btree.c'],tree)
  for mode,flags in [('native',native),('san',san)]:
   build='build/'+mode;add(v+'-'+mode+'-original43',['make','CC=clang','BUILD='+build,'CFLAGS='+' '.join(flags),'LDFLAGS='+('-fsanitize=address,undefined' if mode=='san' else ''),'all','check'],tree)
   for oracle,seeds in oracle_seeds:
    binary=build+'/'+oracle;prefix=v+'-'+mode+'-'+oracle;add(prefix+'-build',['clang',*inc,*flags,'tests/'+oracle+'.c',*common,'-o',binary],tree)
    for seed in seeds:add(prefix+('-'+seed[0] if seed else ''),[binary,*seed],tree)
   if v!='base':
    binary=build+'/portable-v2';add(v+'-'+mode+'-portable-build',['clang',*inc,*flags,'-D'+manifest['variants'][v]['portable_macro'],'tests/all_match_guard_oracle_v2.c',*common,'-o',binary],tree);add(v+'-'+mode+'-portable-v2',[binary],tree)
  add(v+'-native-codegen',['otool','-tvV','build/native/btree-bench'],tree)
 for fault in ['fold','order','tail','overread']:
  for mode,flags in [('native',native),('san',san)]:
   cwd='scratch/m6-neon-validation/fault-'+fault;name='fault-'+fault+'-'+mode;add(name+'-build',['clang',*inc,*flags,'tests/all_match_guard_oracle_v2.c',*common,'-o','build/'+mode],cwd);add(name,['build/'+mode],cwd,True)
 assert len(expected)==141
 previous=None;streams=[];faults=[];outputs={};positive=portable=originals=0
 for r,(name,cmd,cwd,negative) in zip(rows,expected):
  assert (r['name'],r['command'],r['cwd'],r['negative_control'])==(name,cmd,cwd,negative)
  start=datetime.fromisoformat(r['started_utc']);finish=datetime.fromisoformat(r['finished_utc']);assert start<=finish
  if previous:assert previous<=start,'overlapping child intervals'
  previous=finish;assert not r['timed_out'] and r['child_reaped'] and r['owned_group_empty'] and r['release_safe']
  assert 0<r['timeout_seconds']<=120 and r['wall_seconds']<r['timeout_seconds']+10
  text={}
  for channel,meta in r['raw'].items():
   raw=Path(meta['path']).read_bytes();public=Path(meta['public_path']).read_bytes();assert len(raw)==meta['bytes'] and sha(meta['path'])==meta['sha256'] and sha(meta['public_path'])==meta['public_sha256']
   expected_public=re.sub(r'/(?:Users|home)/[^/\s]+','<user-home>',raw.decode(errors='replace').replace(str(R),'<workspace>')).encode();assert public==expected_public
   assert not re.search(rb'/(?:Users|home)/[^/\s]+',public);text[channel]=raw.decode(errors='replace');streams.append({'name':name,'channel':channel,'raw_sha256':meta['sha256'],'public_sha256':meta['public_sha256'],'bytes':len(raw)})
  outputs[name]=text
  if negative:
   assert r['returncode']==-signal.SIGABRT
   match=re.fullmatch(r'tests/all_match_guard_oracle_v2\.c:(38|40): (got == want && actual\[0\] == canary|actual\[i \+ 1\] == expected\[i\])\n',text['stderr']);assert match and text['stdout']==''
   faults.append({'name':name,'returncode':r['returncode'],'diagnostic':text['stderr'].strip(),'actual_detection':'V2 assertion; no ASan/UBSan memory diagnostic and no guard-page signal'})
  else:
   assert r['returncode']==0 and text['stderr']=='',name
  if name.endswith('-original43'):
   assert '43 passed' in text['stdout'] and '0 failed, 43 total' in text['stdout'];assert [int(x) for x in re.findall(r'^(\d+) - .*PASSED',text['stdout'],re.M)]==list(range(1,44))
   # Reconstruct the two actual compiler commands emitted by make, not just its argv.
   v,mode,_=name.split('-',2);flags=native if mode=='native' else san;link=[] if mode=='native' else ['-fsanitize=address,undefined'];lines=[shlex.split(x) for x in text['stdout'].splitlines() if x.startswith('clang ')]
   assert lines==[['clang',*inc,*flags,*link,'bench/microbench.c','src/zset_btree.c',*common,'-o','build/'+mode+'/btree-bench'],['clang',*inc,*flags,'-DREDIS_TEST','-DREDIS_DEBUG',*link,'tests/upstream.c','src/zset_btree.c',*common,'-o','build/'+mode+'/btree-test']]
   originals+=1
  if name.endswith('-portable-v2'):portable+=1
  if not negative and not name.endswith('-build') and any(('-'+o in name) for o,_ in oracle_seeds):positive+=1
 assert originals==8 and positive==56 and portable==6
 for mode in ['native','san']:
  for oracle,seeds in oracle_seeds:
   for seed in seeds:
    suffix='-'+mode+'-'+oracle+('-'+seed[0] if seed else '');reference=outputs['base'+suffix]['stdout'];assert re.search(r'^PASS(?: |$)',reference,re.M)
    for v in ['A','B','C']:assert outputs[v+suffix]['stdout']==reference
  reference=outputs['base-'+mode+'-all_match_guard_oracle_v2']['stdout'];assert reference=='PASS checks=299664 positions=79864 zero_spans=3072 digest=39f4d4c13e2fdc15\n'
  for v in ['A','B','C']:assert outputs[v+'-'+mode+'-portable-v2']['stdout']==reference
 codegen={};sources=0
 for v,e in manifest['variants'].items():
  for rel,h in e['source_hashes'].items():assert sha(Path(e['worktree'])/rel)==h;sources+=1
  assert e['source_hashes']['src/zset_btree.c']==e['target_c_sha256'];assert sha(Path(e['worktree'])/'src/zset_btree.h')=='496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83'
  macros=outputs[v+'-native-macros']['stdout'];assert '#define __aarch64__ 1\n' in macros and '#define __ARM_NEON 1\n' in macros
  if v!='base':assert '#define '+('ZBT_NATIVE_LEAF_TAGS_C' if v=='C' else 'ZBT_LEAF_TAG_MATCHES_NEON')+' 1\n' in macros
  asm=outputs[v+'-native-codegen']['stdout'];match=re.search(r'^_zbtIndexScanSlot:\n(.*?)(?=^_[A-Za-z0-9_.$]+:|\Z)',asm,re.M|re.S);assert match
  instructions=match[1];counts={k:len(re.findall(k,instructions)) for k in [r'\bcmeq\b',r'\bshrn\b',r'\bv\d+\b']}
  if v!='base':assert all(counts.values())
  codegen[v]={'source_sha256':e['target_c_sha256'],'native_guard_proved':v!='base','scan_slot_instruction_matches':counts,'timing_binary_sha256':sha(Path(e['worktree'])/'build/native/btree-bench')}
  snapshot=bf['snapshots'][v];assert snapshot['source_hashes']==e['source_hashes']
  for rel,h in snapshot['binaries'].items():assert sha(Path(e['worktree'])/rel)==h
  assert codegen[v]['timing_binary_sha256']==snapshot['timing_binary_sha256']
 check_hashes(result['final_build_artifacts']);check_hashes(result['fault_build_artifacts'])
 for fault,h in result['fault_source_sha256'].items():
  source=R/'scratch/m6-neon-validation'/('fault-'+fault)/'src/zset_btree.c';assert sha(source)==h
  a=(R/manifest['variants']['A']['worktree']/'src/zset_btree.c').read_text();b=source.read_text();patch=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c'));assert (E/'validation'/('fault-'+fault+'.patch')).read_text()==patch
 elapsed=(datetime.fromisoformat(result['finished_utc'])-datetime.fromisoformat(result['started_utc'])).total_seconds();assert elapsed<600 and result['wall_seconds']<600 and previous<=datetime.fromisoformat(result['finished_utc'])<datetime(2026,10,19,7,15,tzinfo=timezone.utc)
 owner={}
 for channel in ['stdout','stderr']:
  path=R/('scratch/m6-neon-validation-owner.'+channel);assert path.is_file();owner[channel]={'sha256':sha(path),'bytes':path.stat().st_size}
 assert owner['stderr']['bytes']==0
 report={'status':'PASS','participant':'/root/followup_proposal_b','backend':'Inherited Codex/GPT-6 family; exact model/token/currency costs unknown','audit_type':'Independent retained-data reconstruction; no launcher import/subprocess/native build/test/profile/timing execution','command_count':len(rows),'raw_streams_verified':len(streams),'serial_intervals':True,'original43_invocations':originals,'positive_semantic_runs':positive,'forced_portable_runs':portable,'negative_runs':faults,'frozen_input_entries_verified':len(freeze['files_sha256']),'source_entries_verified':sources,'produced_artifact_entries_verified':len(result['final_build_artifacts']),'fault_binary_entries_verified':len(result['fault_build_artifacts']),'phase_wall_seconds_reported':result['wall_seconds'],'phase_utc_interval_seconds':elapsed,'all_recorded_child_reaped_group_empty_release_safe':True,'codegen':codegen,'compiler':result['compiler'],'owner_logs':owner,'source_binary_referee_mutation':False,'audit_parser_revision_notes':['Initial audit expected actual ANSI escape after testPASSED; retained output uses literal unicode escapes. Final check reconstructs exact numbered test sequence1..43.','Initial audit expected PASS at stdout start; unchanged oracles print fixture progress before PASS. Final check requires a separate PASS line and exact source/build parity.','Initial audit expected vector lane suffix on operand register; Apple otool places it on mnemonic. Final actual register/mnemonic checks support that syntax.','All three failed audit drafts are preserved under pre-review; no native command rerun or validation gate relaxation occurred.'],'source_adoption':'NONE','limits':['Reap/group disappearance are historical launcher observations checked for all commands and against reviewed cleanup logic; audit does not independently observe past kernel process state.','Native and sanitizer negatives all reached V2 assertions. No actual ASan/UBSan memory diagnostic or protected-page fault was observed, including the overread mutation.','No benchmark workload executed; correctness and emitted NEON do not establish speed, causal cost, guard performance or acceptance.'],'streams':streams,'provenance':{str(x.relative_to(R)):sha(x) for x in [E/'validation-freeze.json',E/'source-manifest.json',E/'PLAN.json',E/'validate.py',E/'validation/result.json',E/'validation/binary-freeze.json',Path(__file__).resolve()]}}
 (E/'VALIDATION-AUDIT-B.json').write_text(json.dumps(report,indent=2)+'\n')
 (E/'VALIDATION-AUDIT-B.md').write_text(f'''# Independent retained-data validation audit — PASS\n\nAll 141 exact command records were reconstructed from the frozen contract, with 282 raw/public stream pairs checked by hash and exact redaction. The actual make-emitted compiler argv matches native/sanitizer flags and relative source paths. The audit imports no validator and executes no native binary, build, test, sampler or timing. Run from root: `python3 <023>/validation-audit-b.py`.\n\nCoverage is 8 × 43 original tests, 56 unchanged positive oracle runs and 6 forced-portable runs. Every positive oracle matches baseline byte-for-byte within mode. All eight negative runs abort at the expected V2 cardinality/canary/order assertions; none reports an actual ASan/UBSan memory error or guard-page signal. In particular both overread mutations fail the cardinality assertion before any demonstrated guard-page event. This is fault detection evidence with that explicit limit.\n\nActual macro logs prove AArch64/NEON and the designated candidate guards. Retained linked ScanSlot disassembly contains vector equality and narrowing for all three candidates. All 322 frozen input entries, 244 source entries, 248 produced artifact entries and 8 isolated fault binaries match current hashes. Exact native identities and per-source codegen observations are in VALIDATION-AUDIT-B.json.\n\nThe 141 recorded child intervals are serial; every record reports no timeout, direct-child reap, empty owned group and safe release. Total reported phase wall is {result['wall_seconds']:.6f}s; UTC interval independently reconstructs to {elapsed:.6f}s, below 600s and 07:15 UTC. Historical kernel cleanup observations cannot be independently replayed from logs; this audit validates their complete record and reviewed cleanup mechanism rather than claiming new live process observations. Owner stderr is empty and both owner logs are hashed.\n\nThree initial audit-only parser assumptions (literal test color escapes, progress before PASS, and Apple otool vector-register syntax) failed closed and were corrected after inspecting retained raw text. All failed drafts are preserved under pre-review; no native command was rerun or source validation gate changed.

No target/referee or retained input mutation found. This audit establishes retained correctness/build evidence, not a performance qualification or source adoption. Participant /root/followup_proposal_b; exact serving model/token/currency costs unknown.\n''')
 print('PASS independent141-command validation reconstruction; no execution')
if __name__=='__main__':main()
