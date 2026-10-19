#!/usr/bin/env python3
"""Independent offline raw reconstruction; no campaign module imports/native children."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
import array, collections, csv, hashlib, io, json, re, sys
W=Path(__file__).resolve().parents[3];E=W/'experiments/M6-CLOCK-BRACKET-001';ROOT=W.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def utc(s):return datetime.fromisoformat(s)
def csvrows(p,header):
 r=csv.DictReader(io.StringIO(p.read_text()));out=list(r)
 assert r.fieldnames==header and all(None not in x and all(v is not None for v in x.values()) for x in out)
 for x in out:
  for k,v in x.items():
   if k in ['case','control','qos_reported_start','qos_reported_end','qos_effective']:assert re.fullmatch('[A-Za-z0-9_-]+',v)
   elif k in ['ns_per_op','ops_per_sec']:assert re.fullmatch(r'(0|[1-9][0-9]*)\.[0-9]{3}',v)
   else:assert re.fullmatch(r'-?(0|[1-9][0-9]*)',v) and v!='-0'
 return out
LOOK='case,size,requested_ops,member_bytes,seed,operations,elapsed_ns,ns_per_op,ops_per_sec,tree_bytes,checksum,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,traversals,warmup_passes,warmup_elapsed_ns'.split(',')
CLOCK='w0_ns,t0_ns,w1_ns,w2_ns,t1_ns,w3_ns,wall_resolution_ns,thread_resolution_ns'.split(',')
CONTROL='control,repetition,iterations,requested_block_ns,sleep_wall_ns,sleep_interruptions,checksum'.split(',')+CLOCK
plan=load(E/'PLAN.json');stop=utc(plan['absolute_stop_utc']);inputs=load(E/'inputs.json')['files_sha256']
checks=[];pinhashes={}
for name,table in [('inputs',inputs),('build',load(E/'results/build/build-manifest.json')['files_sha256'])]+[(p+'-evidence',load(E/'results'/p/'evidence-manifest.json')['files_sha256']) for p in ['build','controls','aa']]:
 for k,v in table.items():
  assert not Path(k).is_absolute() and '..' not in Path(k).parts and sha(W/k)==v,(name,k)
  assert k not in pinhashes or pinhashes[k]==v
  pinhashes[k]=v
 checks.append(dict(manifest=name,pins=len(table),all_match=True))
assert all(load(E/'results/build/build-manifest.json')['files_sha256'][k]==v for k,v in inputs.items())
journals={};allcommands=[];streamcounts={};prior=None
for phase,count in [('build',85),('controls',1),('aa',48)]:
 out=E/'results'/phase;st=load(out/'status.json');assert st['status']=='COMPLETE' and st['release_safe'] and st['journaled_commands']==count
 assert st['input_manifest_sha256']==sha(E/'inputs.json') and st['source_selection']=='NONE' and st['physical_attribution']=='UNVALIDATED'
 assert utc(st['finished_utc'])<stop and st['wall_seconds']<plan['phase_wall_caps_seconds'][phase]
 if phase!='build':assert st['native_lock_released']
 rows=[json.loads(l) for l in (out/'commands.jsonl').read_text().splitlines()];assert len(rows)==count
 streams=set()
 for j in rows:
  assert j['returncode']==0 and not j['timed_out'] and j['child_reaped'] and j['owned_group_empty'] and j['release_safe']
  assert j['cwd']=='.' and j['environment']=={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
  a,b=utc(j['started_utc']),utc(j['finished_utc']);assert utc(st['started_utc'])<=a<=b<=utc(st['finished_utc'])<stop
  assert prior is None or prior<=a;prior=b
  assert 0<j['wall_seconds']<=j['timeout_seconds'] and j['timeout_seconds']<=120
  for channel in ['stdout','stderr']:
   raw=j['raw'][channel];p=W/raw['path'];assert not Path(raw['path']).is_absolute()
   assert sha(p)==raw['sha256'] and p.stat().st_size==raw['bytes'] and raw['path'] not in streams
   if channel=='stderr':assert raw['bytes']==0
   streams.add(raw['path'])
  allcommands.append(dict(phase=phase,name=j['name'],started_utc=j['started_utc'],finished_utc=j['finished_utc'],release_safe=True))
 assert streams=={str(p.relative_to(W)) for p in (out/'raw').iterdir() if p.is_file()}
 journals[phase]=rows;streamcounts[phase]=len(streams)
assert len(allcommands)==134
# Independently verify the prescribed build command coverage and resulting smoke contracts.
bs=journals['build'];names=[x['name'] for x in bs]
expected_names=[]
for mode in ['native','san']:
 for n in ['lookup','controls','old-lookup','original43']:expected_names.append('compile-'+mode+'-'+n)
 expected_names.append(mode+'-original43')
 for m in [8,16,319,320,321,1024]:
  for c in ['lookup-hit','lookup-miss','lookup-mixed']:
   expected_names.extend([f'{mode}-{c}-m{m}',f'{mode}-{c}-m{m}-referee'])
expected_names.extend(['compiler','lookup-assembly','controls-assembly']);assert names==expected_names
native=['-std=c11','-O3','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto']
sanitized=['-std=c11','-O1','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-fsanitize=address,undefined','-fno-sanitize-recover=all']
compiler=load(E/'results/build/compiler.json')
assert compiler['native_flags']==native
# Record actual sanitizer options as frozen metadata rather than infer unprovided flags.
assert '-fsanitize=address,undefined' in compiler['san_flags'] and '-O1' in compiler['san_flags']
for j in bs:
 if j['name'].startswith('compile-'):
  flags=compiler['native_flags'] if j['name'].startswith('compile-native-') else compiler['san_flags']
  assert j['command'][0]=='clang' and j['command'][1:1+len(flags)]==flags
  assert '-DNDEBUG' not in j['command'] and '-flto' not in j['command']
for mode in ['native','san']:
 p=E/'results/build/raw'/f'{mode}-original43.stdout';text=p.read_text();assert '43 passed' in text and '0 failed, 43 total' in text
 for m in [8,16,319,320,321,1024]:
  for c in ['lookup-hit','lookup-miss','lookup-mixed']:
   prefix=f'{mode}-{c}-m{m}'
   a=csvrows(E/'results/build/raw'/f'{prefix}.stdout',LOOK+CLOCK);b=csvrows(E/'results/build/raw'/f'{prefix}-referee.stdout',LOOK)
   assert len(a)==len(b)==1
   for k in ['operations','checksum','tree_bytes','requested_ops','size','seed','member_bytes','warmup_passes','case','traversals']:assert a[0][k]==b[0][k]
   assert a[0]['case']==c and int(a[0]['size'])==1000 and int(a[0]['operations'])==2003 and int(a[0]['member_bytes'])==m
# Query permutation reconstructed from C splitmix64/Fisher-Yates, no imports from driver.
mask=(1<<64)-1
fixtures={}
for n in plan['sizes']:
 for seed in [1,2,3]:
  values=list(range(n));state=seed^0xd02703a89f4c51e7
  for i in range(n-1,0,-1):
   state=(state+0x9e3779b97f4a7c15)&mask;z=state
   z=((z^(z>>30))*0xbf58476d1ce4e5b9)&mask;z=((z^(z>>27))*0x94d049bb133111eb)&mask;z^=z>>31
   k=z%(i+1);values[i],values[k]=values[k],values[i]
  packed=array.array('Q',values)
  if sys.byteorder!='little':packed.byteswap()
  q,r=divmod(plan['operations'][str(n)],n)
  fixtures[f'{n}-{seed}']=dict(checksum=(q*n*(n-1)//2+sum(values[:r]))&mask,query_order_sha256_le_u64=hashlib.sha256(packed.tobytes()).hexdigest())
assert fixtures==load(E/'fixtures.json')
def bracket(r):
 v={k:int(r[k]) for k in CLOCK};assert v['wall_resolution_ns']>=0 and v['thread_resolution_ns']>=0
 assert 0<=v['w0_ns']<=v['w1_ns']<=v['w2_ns']<=v['w3_ns'] and 0<=v['t0_ns']<=v['t1_ns']
 i=v['w2_ns']-v['w1_ns'];t=v['t1_ns']-v['t0_ns'];m=v['w1_ns']-v['w0_ns']+v['w3_ns']-v['w2_ns'];lo=max(0,t-m);hi=min(t,i)
 return dict(inner_wall_ns=i,outer_thread_ns=t,wall_margins_ns=m,recorded_residual_ns=i-t,conditional_cpu_lower_ns=lo,conditional_cpu_upper_ns=hi,conditional_zero_error_model_nonempty=lo<=hi,physical_attribution='UNVALIDATED: unknown clock accuracy/accounting error')
# Affine composition via binary exponentiation; independent of executing the 2M C loop.
a,b=1664525,1013904223;p,q=1,0;steps=2000000
while steps:
 if steps&1:p,q=(p*a)&mask,(p*b+q)&mask
 a,b=(a*a)&mask,(a*b+b)&mask;steps//=2
cpu_checksum=(p+q)&mask
controls=csvrows(E/'results/controls/raw/controls.stdout',CONTROL);assert len(controls)==72
cderived=[];empty=[]
for index,r in enumerate(controls):
 kind=plan['control_order'][index%3];assert r['control']==kind and int(r['repetition'])==index//3
 assert int(r['iterations'])==(2000000 if kind=='cpu' else 0) and int(r['requested_block_ns'])==(20000000 if kind=='block' else 0)
 assert int(r['checksum'])==(cpu_checksum if kind=='cpu' else 1)
 br=bracket(r);sense=kind!='block' or (int(r['sleep_wall_ns'])>=20000000 and br['recorded_residual_ns']>=18000000)
 assert sense and int(r['sleep_interruptions'])>=0
 if kind!='block':assert int(r['sleep_wall_ns'])==0 and int(r['sleep_interruptions'])==0
 if index:assert int(controls[index-1]['w3_ns'])<=int(r['w0_ns'])
 if not br['conditional_zero_error_model_nonempty']:empty.append(dict(index=index,kind=kind,repetition=index//3,**br))
 cderived.append(dict(raw=r,bracket=br,sensitivity_pass=sense))
cs=load(E/'results/controls/summary.json');assert cs['rows']==cderived and cs['expected_cpu_checksum']==cpu_checksum and cs['model_empty_intervals']==len(empty) and cs['sensitivity_pass']
# All 48 AA processes in fixed block/size/ABBA order, preserving every CSV observation.
rawrows=[];blocks=[];memory=collections.defaultdict(set);idx=0
for block,seed in enumerate([1,2,3,1,2,3]):
 for size in ([100000,1000000] if block%2==0 else [1000000,100000]):
  group=[];ops=plan['operations'][str(size)]
  for position,side in enumerate('ABBA'):
   j=journals['aa'][idx];assert j['name']==f'{idx:03}'
   assert j['command']==['build/m6-clock-bracket-001/native/lookup','--case','lookup-hit','--size',str(size),'--ops',str(ops),'--seed',str(seed),'--member-bytes','16','--warmup-passes','1']
   rows=csvrows(W/j['raw']['stdout']['path'],LOOK+CLOCK);assert len(rows)==1;r=rows[0]
   for k,v in dict(case='lookup-hit',size=size,operations=ops,requested_ops=ops,seed=seed,member_bytes=16,warmup_passes=1,traversals=0).items():assert r[k]==str(v)
   fixture=fixtures[f'{size}-{seed}'];assert int(r['checksum'])==fixture['checksum'] and int(r['tree_bytes'])>0
   br=bracket(r);assert int(r['elapsed_ns'])==br['inner_wall_ns'] and int(r['thread_elapsed_ns'])==br['outer_thread_ns']
   assert abs(Decimal(r['ns_per_op'])-Decimal(br['inner_wall_ns'])/ops)<=Decimal('.0006')
   assert abs(Decimal(r['ops_per_sec'])-Decimal(ops)*1000000000/br['inner_wall_ns'])<=Decimal('.0006')
   memory[(size,seed)].add(int(r['tree_bytes']))
   item=dict(csv=r,bracket=br,query_order_sha256_le_u64=fixture['query_order_sha256_le_u64'],index=idx,block=block,seed=seed,size=size,position=position,side=side)
   rawrows.append(item);group.append(item);idx+=1
  assert all(len({r['csv'][k] for r in group})==1 for k in ['checksum','operations','tree_bytes'])
  A=sum(int(group[i]['csv']['elapsed_ns']) for i in [0,3]);B=sum(int(group[i]['csv']['elapsed_ns']) for i in [1,2]);T0=sum(int(group[i]['csv']['thread_elapsed_ns']) for i in [0,3]);T1=sum(int(group[i]['csv']['thread_elapsed_ns']) for i in [1,2]);minimum=min(int(r['csv']['elapsed_ns']) for r in group)
  blocks.append(dict(block=block,seed=seed,size=size,wall_A_ns=A,wall_B_ns=B,thread_A_ns=T0,thread_B_ns=T1,wall_effect_percent=100*(B-A)/A,thread_effect_percent_diagnostic=100*(T1-T0)/T0,minimum_elapsed_ns=minimum,qualified=abs(B-A)*100<=A and minimum>=10000000))
assert idx==48 and all(len(s)==1 for s in memory.values())
asum=load(E/'results/aa/summary.json');assert asum['rows']==rawrows and asum['blocks']==blocks and asum['complete'] and asum['decision']=='PARK' and asum['source_selection']=='NONE'
release=load(E/'native-release.json');assert release['status']=='RELEASED' and release['phase_release_safe'] and not release['known_target_processes'] and not release['owned_lock_exists'] and not release['queued_work']
assert release['controls_status_sha256']==sha(E/'results/controls/status.json') and release['aa_status_sha256']==sha(E/'results/aa/status.json')
assert not (ROOT/'scratch/m6-clock-bracket-native.lock').exists()
reservation=load(E/'native-reservation-start.json');assert reservation['input_manifest_sha256']==sha(E/'inputs.json') and utc(reservation['observed_utc'])<utc(allcommands[85]['started_utc']) and utc(release['observed_utc'])>utc(allcommands[-1]['finished_utc'])
consult=ROOT/'scratch/cpu-perf-m6-bracket-20261019/results/results-calls.jsonl';calls=[]
for l in consult.read_text().splitlines():
 c=json.loads(l);calls.append(dict(method=c['method'],tool=c['params'].get('name'),started_utc=c['started_utc'],finished_utc=c['finished_utc'],request_sha256=hashlib.sha256(json.dumps(c['params'],sort_keys=True).encode()).hexdigest(),response_sha256=hashlib.sha256(json.dumps(c['response'],sort_keys=True).encode()).hexdigest()))
report=dict(status='PASS',campaign_decision='PARK',scope='Raw integrity/reconstruction only; not candidate confirmation or physical clock qualification',reviewer='/root/followup_proposal_b',model='Inherited Codex/GPT-6 family; exact serving backend/token/currency costs unknown',created_utc=datetime.now(timezone.utc).isoformat(),native_execution=False,peer_new_postreviews_read=False,manifests=checks,overlapping_pins=sum(x['pins'] for x in checks),unique_pinned_paths=len(pinhashes),journals=dict(commands=134,per_phase={p:len(x) for p,x in journals.items()},streams=streamcounts,all_hash_size_joins=True,all_success_reaped_group_empty=True,serial_utc_intervals=True,within_phase_and_absolute_deadlines=True,chronology=allcommands),build=dict(original43_native_and_sanitizer=True,paired_smokes=36,compile_commands=8,command_coverage_exact=True,native_flags=compiler['native_flags'],sanitizer_flags=compiler['san_flags']),fixtures=dict(independently_rebuilt=fixtures,scope='Aggregate raw checksum and intended query permutation match; CSV does not trace every executed query. Query-order SHA is reconstructed metadata, not a native per-query trace.'),aa=dict(rows=rawrows,blocks=blocks,qualified_by_size={str(n):sum(b['qualified'] for b in blocks if b['size']==n) for n in [100000,1000000]},minimum_elapsed_ns=min(int(r['csv']['elapsed_ns']) for r in rawrows),maximum_elapsed_ns=max(int(r['csv']['elapsed_ns']) for r in rawrows),minimum_margin_ns=min(r['bracket']['wall_margins_ns'] for r in rawrows),maximum_margin_ns=max(r['bracket']['wall_margins_ns'] for r in rawrows),all48retained=True),controls=dict(rows=cderived,rows_count=72,cpu_checksum=cpu_checksum,sensitivity_all_pass=True,empty_conditional_model_intervals=empty,physical_accuracy='UNVALIDATED'),release=dict(evidence_status='RELEASED',lock_currently_absent=True,known_process_scope='Recorded owned-child/group continuity and parent release metadata; not an independent historical OS process monitor'),mcp=dict(own_availability_check_utc='2026-10-19T15:17:51Z',own_exposed_matching_tools=[],consultation='Explicitly shared root stdio actual results consultation, not B-owned ask',journal_generic='scratch/cpu-perf-m6-bracket-20261019/results/results-calls.jsonl',journal_sha256=sha(consult),calls=calls,coverage='2/287 indexed sources;93passages;keyword only',excluded_parser_claim='CSV misclassified as perf stat -x; QoS string falsely interpreted as 0% counter multiplexing. No counters were collected; all inferred multiplexing/top-down claims excluded.'),limits=['Physical clock accuracy/accounting lag remains UNVALIDATED; recorded margins are not worst-case error bounds.','Thread contrasts/conditional intervals are diagnostic only; no causal descheduling, DVFS, placement or source-speed claim.','Journal reap/group flags attest supervision observations, not independently replayable OS history.','No omitted/retried native rows and no source candidate adoption are recorded within this campaign.'])
report['provenance_sha256']={str(p.relative_to(W)):sha(p) for p in [E/'inputs.json',E/'PLAN.json',E/'driver.py',E/'fixtures.json',E/'native-release.json',E/'native-reservation-start.json']+[E/'results'/phase/name for phase in ['build','controls','aa'] for name in ['commands.jsonl','status.json','evidence-manifest.json']]+[E/'results/build/build-manifest.json',E/'results/controls/summary.json',E/'results/aa/summary.json']}
report['current_source_sha256']={k:sha(W/k) for k in ['src/zset_btree.c','src/zset_btree.h','compat/server.h','compat/standalone.c']}
report['produced_binary_sha256']={str(p.relative_to(W)):sha(p) for mode in ['native','san'] for p in (W/'build/m6-clock-bracket-001'/mode).iterdir() if p.is_file()}
assert all(sha(W/k)==v for k,v in pinhashes.items())
report['post_audit_all388_hashes_match']=True
(E/'review/RAW-AUDIT-B.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','campaign_decision','manifests','overlapping_pins','unique_pinned_paths']},indent=2))
print('AA',report['aa']['qualified_by_size'],'windows',report['aa']['minimum_elapsed_ns'],report['aa']['maximum_elapsed_ns'],'empty',len(empty))
for b in blocks:print(b['size'],b['block'],b['wall_effect_percent'],b['qualified'],b['thread_effect_percent_diagnostic'])
