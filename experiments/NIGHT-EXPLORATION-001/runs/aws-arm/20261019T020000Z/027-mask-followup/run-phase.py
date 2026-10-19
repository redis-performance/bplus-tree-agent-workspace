#!/usr/bin/env python3
"""Exact fixed phase runner. No schedule changes, calibration or retries."""
import argparse,csv,datetime,hashlib,json,math,os,pathlib,struct,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--checkout',type=pathlib.Path,required=True);p.add_argument('--phase',choices=['primary-AA','primary-replication','original-AA','original-comparison','iterator-AA','iterator-comparison'],required=True);a=p.parse_args()
here=pathlib.Path(__file__).resolve().parent;out=here/a.phase;out.mkdir();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();start=time.monotonic();assert sorted(os.sched_getaffinity(0))==[2]
assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc)
freeze=json.loads((here/'timing-freeze.json').read_text());e=json.loads((here/'expected.json').read_text());ids=json.loads((here/'identities.json').read_text());budgets=json.loads((here/'phase-budgets.json').read_text());cap=next(x['cap_seconds'] for x in budgets['phases'] if x['name']==a.phase);schedule=json.loads((here/'schedules'/(a.phase+'.json')).read_text());family=a.phase.split('-')[0]
for n,h in freeze['files'].items():assert sha(here/n)==h,n
validation=json.loads((here/'validation/result.json').read_text());assert validation['status']=='correctness_complete';binding=json.loads((here/'validation-approval.json').read_text());assert binding['status']=='PASS' and binding['validation_result_sha256']==sha(here/'validation/result.json') and binding['preparation_freeze_sha256']==sha(here/'preparation-freeze.json')
if a.phase=='primary-replication':assert json.loads((here/'primary-AA/audit.json').read_text())['all_required_qualified']
if family!='primary':
 assert json.loads((here/'primary-AA/audit.json').read_text())['all_required_qualified']
 assert json.loads((here/'primary-replication/audit.json').read_text())['all_primary_pass']
if a.phase.endswith('comparison'):assert json.loads((here/(family+'-AA')/'audit.json').read_text())['complete']
protected_before={n:sha(a.checkout/n) for n in e['protected_binaries']};assert protected_before==e['protected_binaries']
def sources():
 result={}
 for v,root in [('actual',a.checkout/'scratch/adapter-worktree-13e459ff8'),('actualA',a.checkout/'scratch/arm-exp005A-replication-13e459ff8/A'),('control',here/'control'),('A',here/'A')]:
  result[v]={n:sha(root/n) for n in e['source_hashes']};expected=dict(e['source_hashes'])
  if v in ['A','actualA']:expected['src/zset_btree.c']=e['candidate_source_sha256']
  assert result[v]==expected
 return result
source_before=sources();guard_before={v:{h:sha(here/v/'build/native'/h) for h in ['modes','modes5']} for v in ['control','A']};assert guard_before==validation['guard_binary_sha256']
state=dict(status='running',phase=a.phase,started_utc=now(),cap_seconds=cap,cpu=2,timing_freeze_sha256=sha(here/'timing-freeze.json'),validation_approval_sha256=sha(here/'validation-approval.json'),schedule_sha256=sha(here/'schedules'/(a.phase+'.json')),protected_before=protected_before,sources_before=source_before,guard_binaries_before=guard_before,runs=[])
def save():(out/'result.json').write_text(json.dumps(state,indent=2)+'\n')
def expand(s):return s.replace('<checkout>',str(a.checkout)).replace('<job>',str(here))
score_sums={}
def independent_mode_checksum(cell):
 n=cell['size'];encoding=cell['encoding'];fold=cell['referee']=='HARNESS-005';key=(n,encoding,fold)
 if key not in score_sums:
  if encoding=='alternating-zero':score_sums[key]=(n//2)*((1<<63)^(1<<31))
  else:
   total=0
   for i in range(n):
    if encoding=='fraction':value=float(i)-float(n//2)+0.25
    elif encoding=='wide':value=float(2**53)+2.0*i
    elif encoding=='zero':value=float(i) if i else -0.0
    else:value=float(i)-float(n//2)
    bits=struct.unpack('<Q',struct.pack('<d',value))[0];total+=(bits^(bits>>32)) if fold else bits
   score_sums[key]=total
 mask=cell['mask'];value=n
 if mask&1:
  value+=0 if encoding=='alternating-zero' else (n//256)*32640+(n%256)*(n%256-1)//2
 if mask&2:value+=n*cell['member_bytes']
 if mask&4:value+=score_sums[key]
 return (value*((cell['requested_ops']+n-1)//n))&((1<<64)-1)
def check(row,contract):
 cell=contract['cell'];n=cell['size'];ops=cell['requested_ops'];case=row['case'];assert row['cpu_start']==row['cpu_end']=='2' and int(row['elapsed_ns'])>0
 for k,v in [('size',n),('requested_ops',ops),('member_bytes',cell['member_bytes']),('seed',contract['seed'])]:assert row[k]==str(v),(k,row)
 if family=='iterator':
  visits=((ops+n-1)//n)*n;expected=independent_mode_checksum(cell)
  assert case=='iterator-modes' and int(row['operations'])==visits and int(row['traversals'])==visits//n
  assert int(row['checksum'])==int(row['expected_checksum'])==expected
  for k in ['direction','mask','encoding','warmup_passes']:assert row[k]==str(cell[k])
  if cell.get('construction'):assert row['construction']==cell['construction']
 else:
  assert case in ['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
  count=n if case in ['insert','delete'] else ops;traversals=(ops+n-1)//n if case in ['iterate','scan'] else 0
  if case in ['iterate','scan']:count=traversals*n
  assert int(row['traversals'])==traversals and int(row['warmup_passes'])==(0 if case=='insert' else 1)
  if case=='scan':assert int(row['operations'])>=count
  else:assert int(row['operations'])==count
  checksums={'insert':0,'lookup-hit':ops*(n-1)//2,'lookup-miss':0,'rank':ops*(n-1)//2,'iterate':count*(n-1)//2,'update':ops,'delete':n}
  if case in checksums:assert int(row['checksum'])==checksums[case]
  if family=='primary':assert case=='iterate'
save()
try:
 for contract in schedule:
  left=cap-(time.monotonic()-start);assert left>0,'fixed phase cap exhausted';record=dict(contract,started_utc=now());state['runs'].append(record);save()
  try:r=subprocess.run([expand(x) for x in contract['command']],cwd=a.checkout,capture_output=True,text=True,timeout=min(60,left))
  except subprocess.TimeoutExpired as ex:
   record.update(finished_utc=now(),returncode=124)
   for suffix,value in [('csv',ex.stdout),('stderr',ex.stderr)]:
    (out/(record['name']+'.'+suffix)).write_text((value.decode(errors='replace') if isinstance(value,bytes) else value) or '')
   save();raise
  record.update(finished_utc=now(),returncode=r.returncode);(out/(record['name']+'.csv')).write_text(r.stdout);(out/(record['name']+'.stderr')).write_text(r.stderr);save();r.check_returncode();rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==(8 if family=='original' else 1)
  if family=='original':assert [z['case'] for z in rows]==['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
  for z in rows:check(z,contract)
  record['rows']=rows
  if contract['position']:
   prior=state['runs'][-2]['rows'];assert len(prior)==len(rows)
   for z,other in zip(rows,prior):
    for k in ['case','operations','checksum','tree_bytes','traversals','warmup_passes']:assert z[k]==other[k],(k,contract['name'])
    if family=='iterator':assert z['construction_fingerprint']==other['construction_fingerprint']
  record['checked']=True;save()
 assert len(state['runs'])==len(schedule)
 state['protected_after']={n:sha(a.checkout/n) for n in e['protected_binaries']};assert state['protected_after']==protected_before
 state['sources_after']=sources();assert state['sources_after']==source_before
 state['guard_binaries_after']={v:{h:sha(here/v/'build/native'/h) for h in ['modes','modes5']} for v in ['control','A']};assert state['guard_binaries_after']==guard_before
 state['status']='complete'
except BaseException as ex:state.update(status='failed',error=type(ex).__name__+': '+str(ex));raise
finally:state.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
