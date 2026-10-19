#!/usr/bin/env python3
"""Reconstruct every complete phase; preserve qualification and diagnostic distinctions."""
import argparse,csv,datetime,decimal,hashlib,json,pathlib,struct
D=decimal.Decimal;decimal.getcontext().prec=40
p=argparse.ArgumentParser();p.add_argument('--phase',required=True);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;out=here/a.phase;state=json.loads((out/'result.json').read_text());schedule=json.loads((here/'schedules'/(a.phase+'.json')).read_text());family=a.phase.split('-')[0];aa=a.phase.endswith('AA');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
budget=next(x['cap_seconds'] for x in json.loads((here/'phase-budgets.json').read_text())['phases'] if x['name']==a.phase)
phase_start=datetime.datetime.fromisoformat(state['started_utc']);phase_end=datetime.datetime.fromisoformat(state['finished_utc']);deadline=datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc)
assert state['cap_seconds']==budget and 0<=state['elapsed_seconds']<=budget
assert 0<=(phase_end-phase_start).total_seconds()<=budget and phase_end<=deadline
assert (deadline-phase_start).total_seconds()>=budget
# Independent numeric model, not an import or call into the producer's check function.
score_totals={}
def check_fixture(z,run):
 c=run['cell'];n=c['size'];requested=c['requested_ops'];case=z['case']
 for k,want in [('size',n),('seed',run['seed']),('requested_ops',requested),('member_bytes',c['member_bytes'])]:assert int(z[k])==want,(k,z)
 assert int(z['tree_bytes'])>0 and z['cpu_start']==z['cpu_end']=='2' and int(z['elapsed_ns'])>0
 count=int(z['operations']);checksum=int(z['checksum']);traversals=int(z['traversals']);warmup=int(z['warmup_passes'])
 if family=='iterator':
  assert case=='iterator-modes' and traversals==(requested+n-1)//n and count==traversals*n
  for k in ['direction','mask','encoding','warmup_passes']:assert z[k]==str(c[k]),k
  if c.get('construction'):assert z['construction']==c['construction']
  assert 0<=int(z['construction_fingerprint'])<2**64
  key=(n,c['encoding'],c['referee'])
  if key not in score_totals:
   total=0
   for i in range(n):
    enc=c['encoding']
    if enc=='alternating-zero':bits=(i%2)*2**63
    else:
     if enc=='fraction':value=i-n//2+0.25
     elif enc=='wide':value=float(2**53)+2*i
     elif enc=='zero':value=float(i) if i else -0.0
     else:value=float(i-n//2)
     bits=int.from_bytes(struct.pack('<d',value),'little')
    total+=bits^(bits>>32) if c['referee']=='HARNESS-005' else bits
   score_totals[key]=total
  total=n;mask=c['mask']
  if mask&1 and c['encoding']!='alternating-zero':total+=sum(range(256))*(n//256)+sum(range(n%256))
  if mask&2:total+=n*c['member_bytes']
  if mask&4:total+=score_totals[key]
  assert checksum==int(z['expected_checksum'])==(total*traversals)%2**64
 else:
  assert case in ['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
  assert warmup==(0 if case=='insert' else 1)
  expected_traversals=(requested+n-1)//n if case in ['iterate','scan'] else 0
  assert traversals==expected_traversals
  if case=='scan':
   # Frozen referee checks every distinct member and exact callback score/bytes.
   # Legitimate duplicates prohibit a unique-member checksum equality assumption.
   assert count>=n*traversals and count%traversals==0 and checksum%traversals==0
   assert traversals*n*(n-1)//2<=checksum<=count*(n-1)
  else:
   expected_count=n if case in ['insert','delete'] else (traversals*n if case=='iterate' else requested)
   assert count==expected_count
   assert requested%n==0  # Fixed schedule uses complete shuffled-key cycles.
   expected={'insert':0,'lookup-hit':requested*(n-1)//2,'lookup-miss':0,'rank':requested*(n-1)//2,'iterate':expected_count*(n-1)//2,'update':requested,'delete':n}[case]
   assert checksum==expected
  if family=='primary':assert case=='iterate' and c['case']=='iterate'
assert state['status']=='complete'  and len(state['runs'])==len(schedule)
assert state['schedule_sha256']==sha(here/'schedules'/(a.phase+'.json'))
for before,after in [('protected_before','protected_after'),('sources_before','sources_after'),('guard_binaries_before','guard_binaries_after')]:assert state[before]==state[after]
freeze=json.loads((here/'timing-freeze.json').read_text())
for n,h in freeze['files'].items():assert sha(here/n)==h,n
assert state['timing_freeze_sha256']==sha(here/'timing-freeze.json')
receipt=json.loads((here/'composite-correctness.json').read_text());assert receipt['status']=='PASS_COMPOSITE_CORRECTNESS' and receipt['original_attempt_status']=='failed'
assert state['composite_receipt_sha256']==sha(here/'composite-correctness.json')
assert state['composite_before']==state['composite_after']
joined=state['composite_before']
assert joined['receipt_sha256']==state['composite_receipt_sha256'] and joined['binding_sha256']==receipt['binding_sha256']
assert joined['original_status']=='failed' and joined['suffix_status']=='six_command_suffix_complete_pending_independent_closure'
for field in ['original_raw_result_sha256','suffix_raw_result_sha256','guard_binary_sha256','protected_binaries']:assert joined[field]==receipt[field]
assert joined['snapshots']==receipt['snapshots_before']
assert state['protected_before']==receipt['protected_binaries'] and state['guard_binaries_before']==receipt['guard_binary_sha256']
expected_sources={}
for variant in ['actual','actualA','control','A']:
 expected_sources[variant]=dict(receipt['source_hashes'])
 if variant in ['actualA','A']:expected_sources[variant]['src/zset_btree.c']=receipt['candidate_source_sha256']
assert state['sources_before']==expected_sources

groups={};previous=None
for run,contract in zip(state['runs'],schedule):
 assert all(run[k]==v for k,v in contract.items()) and run['returncode']==0 and run['checked']
 start=datetime.datetime.fromisoformat(run['started_utc']);end=datetime.datetime.fromisoformat(run['finished_utc']);assert phase_start<=start<=end<=phase_end and (end-start).total_seconds()<=60
 if previous is not None:assert previous<=start
 previous=end
 rows=list(csv.DictReader((out/(run['name']+'.csv')).read_text().splitlines()));assert rows==run['rows']
 assert len(rows)==(8 if family=='original' else 1)
 if family=='original':assert [z['case'] for z in rows]==['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
 for row in rows:
  check_fixture(row,run)
  key=(run['cell']['id'],row['case']);groups.setdefault(key,{}).setdefault(run['block'],[]).append((run,row))
original={(x['size'],x['case']):x for x in json.loads((here/'original-guards.json').read_text())};cells=[]
qualification={};aa_reference={}
if not aa:
 q=json.loads((here/(family+'-AA')/'audit.json').read_text());assert q['complete'];qualification={x['id']:x['qualified'] for x in q['cells']}
 for name,h in q['raw_sha256'].items():assert sha(here/(family+'-AA')/name)==h
 aa_state=json.loads((here/(family+'-AA')/'result.json').read_text())
 for r in aa_state['runs']:
  for z in r['rows']:aa_reference[(r['block'],r['cell']['id'],z['case'])]=z
for (cid,case),blocks in groups.items():
 assert set(blocks)==set(range(6));size=blocks[0][0][0]['cell']['size'];required=original[(size,case)]['required_for_acceptance'] if family=='original' else True;effects=[]
 for block,runs in sorted(blocks.items()):
  assert [r['position'] for r,z in runs]==[0,1,2,3] and [r['label'] for r,z in runs]==['A','B','B','A']
  for field in ['size','seed','member_bytes','requested_ops','operations','checksum','tree_bytes','traversals','warmup_passes']:assert len({z[field] for r,z in runs})==1,(cid,case,field)
  if family=='iterator':
   for field in ['direction','mask','encoding','construction_fingerprint','expected_checksum']:assert len({z[field] for r,z in runs})==1
  if not aa:
   reference=aa_reference[(block,cid,case)]
   for r,z in runs:
    for field in ['size','seed','member_bytes','requested_ops','operations','checksum','tree_bytes','traversals','warmup_passes']:assert z[field]==reference[field],(cid,case,field,'AA reference')
    if family=='iterator':
     for field in ['direction','mask','encoding','construction_fingerprint','expected_checksum']:assert z[field]==reference[field]
  ns=[int(z['elapsed_ns']) for r,z in runs];effect=(D(ns[1]+ns[2])/D(ns[0]+ns[3])-1)*100
  effects.append(dict(block=block,seed=runs[0][0]['seed'],effect_pct=str(effect),minimum_window_ns=min(ns)))
 cellid=cid+'/'+case;windows=all(x['minimum_window_ns']>=10000000 for x in effects)
 if aa:qualified=windows and all(abs(D(x['effect_pct']))<=1 for x in effects);decision='QUALIFIED' if qualified else ('PARK' if required else 'UNQUALIFIED_DIAGNOSTIC')
 else:
  qualified=qualification[cellid] and windows
  values=[D(x['effect_pct']) for x in effects]
  if not qualified:decision='PARK' if required else 'UNQUALIFIED_DIAGNOSTIC'
  elif family=='primary':decision='PRIMARY_PASS' if all(v<=-2 for v in values) else 'REJECT'
  elif all(v<=1 for v in values):decision='GUARD_PASS'
  elif all(v>1 for v in values):decision='REJECT'
  else:decision='PARK'
 cells.append(dict(id=cellid,size=size,case=case,required_for_acceptance=required,qualified=qualified,decision=decision,blocks=effects))
allrequired=all(x['qualified'] for x in cells if x['required_for_acceptance']);reject=any(x['decision']=='REJECT' for x in cells);park=any(x['decision']=='PARK' for x in cells)
result=dict(complete=True,phase=a.phase,processes=len(schedule),rows=sum(len(r['rows']) for r in state['runs']),cells=cells,all_required_qualified=allrequired,qualified_cells=sum(x['qualified'] for x in cells),required_cells=sum(x['required_for_acceptance'] for x in cells),all_primary_pass=(not aa and family=='primary' and all(x['decision']=='PRIMARY_PASS' for x in cells)),all_required_guards_pass=(not aa and family!='primary' and all(x['decision']=='GUARD_PASS' for x in cells if x['required_for_acceptance']) and not reject and not park),decision='REJECT' if reject else ('PARK' if park else ('QUALIFIED' if aa else 'PHASE_PASS_NOT_ACCEPTANCE')),source_selection='NONE',raw_sha256={f.name:sha(f) for f in sorted(out.iterdir()) if f.is_file() and f.name!='audit.json'})
(out/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['cells','raw_sha256']}))
