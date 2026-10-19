#!/usr/bin/env python3
import argparse,collections,hashlib,json,pathlib,re,subprocess
p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();r=a.evidence;load=lambda n:json.loads((r/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();inputs=load('inputs-freeze.json');validation=load('validation/result.json');vfreeze=load('validation/freeze.json');comparison=load('comparison-freeze.json');count=0
for manifest in ['validation-plan-freeze.json','screen-plan-freeze.json','validation-evidence-sha256.json']:
 for f,h in load(manifest).items():assert sha(r/f)==h,(manifest,f);count+=1
assert inputs['source_commit']==comparison['source_commit']==vfreeze['source_commit']=='13e459ff8800be3f02b6b45c87dd7b0c39453fa9'
for f,h in inputs['source_sha256'].items():assert hashlib.sha256(subprocess.check_output(['git','show',inputs['source_commit']+':'+f])).hexdigest()==h,f
assert inputs['v2_oracle_sha256']==sha(r/'all_match_guard_oracle_v2.c')=='b01a762f925a679a6342f5258824ca4743b0020a47982f015be4916050953ded';assert validation['status']=='complete' and validation['elapsed_seconds']<=600 and len(validation['commands'])==145;assert all(v['eligible'] for v in validation['variants'].values());assert validation['aa_binary_before']==validation['aa_binary_after']==inputs['aa_binary_sha256']==comparison['sources']['base']['binary_sha256']=='869425ed06643058e561df05177d1b85c42c9f662c5a80654c25caca02349055';assert vfreeze['cpu_affinity']==[2] and comparison['cpu']==2
native=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3'];san=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];assert vfreeze['native_flags']==comparison['native_flags']==native and vfreeze['sanitize_flags']==san;assert comparison['input_freeze_sha256']==sha(r/'inputs-freeze.json') and comparison['validation_freeze_sha256']==sha(r/'validation/freeze.json');assert all(inputs['source_sha256'][f]==h for f,h in comparison['sources']['base']['source_hashes'].items());assert comparison['driver_sha256']==sha(r/'run-screen.py') and comparison['schedule_sha256']==sha(r/'screen-schedule.json')
byname={};negative=[]
for i,c in enumerate(validation['commands']):
 assert c['started_utc']<=c['finished_utc']
 if i:assert validation['commands'][i-1]['finished_utc']<=c['started_utc']
 if c['negative_control']:assert c['returncode'] not in [0,124] and c['ASAN_OPTIONS']=='symbolize=0';negative.append(c['name'])
 else:assert c['returncode']==0 and 'ASAN_OPTIONS' not in c
 assert c['name'] not in byname;byname[c['name']]=c;assert (r/'validation'/(c['name']+'.stdout')).exists() and (r/'validation'/(c['name']+'.stderr')).exists()
assert len(negative)==8;schedule=['compiler'];oracle={'all_match_guard_oracle_v2':[[]],'scan_interval_oracle':[[]],'wide_scan_oracle':[['7'],['19']],'live_widen_scan_oracle':[['7'],['19']],'resize_generation_oracle':[[]]};original=0;semantic=0;fallback=0
for v in ['base','A','B','C']:
 expected=dict(inputs['source_sha256']);expected['tests/all_match_guard_oracle_v2.c']=inputs['v2_oracle_sha256']
 if v!='base':
  schedule.append(v+'-patch');expected['src/zset_btree.c']=inputs['variants'][v]['source_sha256'];assert sha(r/'variants'/v/'candidate.patch')==inputs['variants'][v]['patch_sha256']
 snapshot=vfreeze['snapshots'][v];assert snapshot['source_hashes']==expected
 if v!='base':
  assert comparison['sources'][v]['source_hashes']==expected and comparison['sources'][v]['binary_sha256']==snapshot['timing_binary_sha256']==snapshot['binaries']['build/btree-bench'];assembly=(r/'validation'/(v+'-native-codegen.stdout')).read_text();assert re.search(r'\bcmeq\b',assembly) and re.search(r'\bshrn\b',assembly)
 for mode,flags,build in [('native',native,'build'),('san',san,'build/san')]:
  prefix=v+'-'+mode;name=prefix+'-original43';schedule.append(name);text=re.sub(r'\x1b\[[0-9;]*m','',(r/'validation'/(name+'.stdout')).read_text());assert '43 passed, 0 failed, 43 total' in text;assert byname[name]['command']==['make','CC=clang','BUILD='+build,'CFLAGS='+' '.join(flags),'LDFLAGS='+('-fsanitize=address,undefined' if mode=='san' else ''),'all','check'];original+=1
  for o,seeds in oracle.items():
   name=prefix+'-'+o+'-build';schedule.append(name);assert byname[name]['command']==['clang','-Isrc','-Icompat','-Ivendor/redis',*flags,'tests/'+o+'.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',build+'/'+o]
   for seed in seeds:
    name=prefix+'-'+o+('-'+seed[0] if seed else '');schedule.append(name);assert byname[name]['command']==[build+'/'+o,*seed];data=(r/'validation'/(name+'.stdout')).read_bytes();assert b'PASS' in data;assert data==(r/'validation'/('base-'+mode+'-'+o+('-'+seed[0] if seed else '')+'.stdout')).read_bytes();semantic+=1
  if v!='base':
   schedule += [prefix+'-portable-build',prefix+'-portable-v2'];cmd=byname[prefix+'-portable-build']['command'];assert '-D'+inputs['variants'][v]['portable_macro'] in cmd;assert (r/'validation'/(prefix+'-portable-v2.stdout')).read_bytes()==(r/'validation'/('base-'+mode+'-all_match_guard_oracle_v2.stdout')).read_bytes();fallback+=1
 schedule += [v+'-native-codegen',v+'-text-section']
for fault in ['fold','order','tail','overread']:
 for mode in ['native','san']:
  schedule += ['fault-'+fault+'-'+mode+'-build','fault-'+fault+'-'+mode];assert 'fault-'+fault+'-'+mode in negative;assert ('actual[i + 1] == expected[i]' if fault=='order' else 'got == want && actual[0] == canary') in (r/'validation'/('fault-'+fault+'-'+mode+'.stderr')).read_text()
schedule.append('aa-text-section');assert [c['name'] for c in validation['commands']]==schedule
# The immutable completed validation driver directly asserts whole .text equality;
# binary section bytes are not present in this public evidence archive.
script=(r/'validate.py').read_text();assert "assert snapshots['base']['text_sha256']==sha(root/'aa-text.bin')" in script;assert byname['aa-text-section']['command'][-1].endswith('/scratch/arm-corrected-scan/base/build/btree-bench');assert vfreeze['snapshots']['base']['text_sha256'] in comparison['same_text_groups'];assert comparison['same_text_groups'][vfreeze['snapshots']['base']['text_sha256']]==['base']
screen=[]
for block in range(6):
 variants='ABC'[block%3:]+'ABC'[:block%3]
 for v in variants:
  for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
   for pos,side in enumerate(['baseline','candidate','candidate','baseline']):screen.append(dict(index=len(screen),block=block,variant=v,size=n,seed=401+block%3,position=pos,side=side))
assert load('screen-schedule.json')==screen and len(screen)==comparison['rows']==144;assert comparison['budget_seconds']==300 and comparison['primary_gate_every_block_pct']==-2 and comparison['minimum_window_ns']==10000000 and comparison['requested_ops']==5000000 and comparison['member_bytes']==16;assert comparison['maintenance_order']==['B','C','A'] and comparison['maintenance_counts']=={'A':28,'B':26,'C':26};assert comparison['candidate_timings_started'] is False
result=dict(status='pass',timing_blocker_found=False,validation_commands=145,positive_commands=137,detected_negative_commands=8,original43_passes=original,semantic_oracle_passes=semantic,portable_passes=fallback,manifest_entries_verified=count,all_144_schedule_rows_reconstructed=True,actual_aa_binary_pin=inputs['aa_binary_sha256'],text_identity_evidence='immutable completed driver assertion, pinned actual AA binary, successful objcopy; raw sections not independently rehashed by this reviewer',reviewer_disclosure='AMD authored C; this review independently audits validation/freeze, not independent authorship of C semantics',source_selection='NONE');a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
