"""Independent raw statistics/identity audit; fixture models also reviewed by Intel."""
import subprocess,tarfile,io,json,csv,hashlib,datetime,decimal,collections,sys
from pathlib import Path
D=decimal.Decimal;decimal.getcontext().prec=40
rev,phase=sys.argv[1:3];assert phase in ('original-AA','original-comparison','iterator-AA','iterator-comparison')
fam=phase.split('-')[0];aa=phase.endswith('AA');prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/'
with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',rev,prefix]))) as t:f={m.name[len(prefix):]:t.extractfile(m).read() for m in t if m.isfile()}
j=lambda n:json.loads(f[n]);sha=lambda b:hashlib.sha256(b).hexdigest()
r=j(phase+'/result.json');schedule=j('schedules/'+phase+'.json');e=j('expected.json');freeze=j('timing-freeze.json');seal=j(phase+'-evidence-seal.json');post=j(phase+'-post-identity-idle.json');claim=j(phase+'/audit.json');publication=j(phase+'/PUBLICATION.json')
for n,h in freeze['files'].items():assert sha(f[n])==h
for n,h in seal.items():assert sha(f[n])==h
for n,x in publication.items():assert sha(f[phase+'/'+n])==x['public_sha256']
cap=600 if fam=='original' else 1500;expected_processes=120 if fam=='original' else 1968
assert r['status']=='complete' and len(r['runs'])==len(schedule)==expected_processes and r['elapsed_seconds']<=cap
assert r['timing_freeze_sha256']==post['timing_freeze_sha256']==sha(f['timing-freeze.json']) and post['timing_inputs']==freeze['files']
assert r['protected_before']==r['protected_after']==post['protected_binaries']==e['protected_binaries']
assert r['sources_before']==r['sources_after'] and r['guard_binaries_before']==r['guard_binaries_after']==post['guard_binary_sha256']
assert r['composite_before']==r['composite_after'] and post['snapshots']==r['composite_after']['snapshots']
assert post['owned_units']==post['owned_cgroup_pids']==[]
assert post['prior_raw_artifacts']=={n:x['raw_sha256'] for n,x in j('validation/PUBLICATION.json').items()}
for v,x in r['sources_before'].items():
 expected=dict(e['source_hashes'])
 if v in ('A','actualA'):expected['src/zset_btree.c']=e['candidate_source_sha256']
 assert x==expected
assert post['actual_sources']=={k:r['sources_after'][k] for k in ('actual','actualA')}
original={(x['size'],x['case']):x for x in j('original-guards.json')};groups=collections.defaultdict(list);prior_end=None
fields=['case','size','seed','requested_ops','member_bytes','operations','traversals','checksum','warmup_passes','tree_bytes']
if fam=='iterator':fields+=['mask','direction','encoding','construction_fingerprint','expected_checksum']
for run,c in zip(r['runs'],schedule):
 assert all(run[k]==v for k,v in c.items()) and run['returncode']==0 and run['checked']
 start=datetime.datetime.fromisoformat(run['started_utc']);end=datetime.datetime.fromisoformat(run['finished_utc']);assert 0<=(end-start).total_seconds()<=60
 if prior_end:assert prior_end<=start
 prior_end=end
 assert c['seed']==1301+c['block']%3 and c['label']=='ABBA'[c['position']]
 assert c['variant']==('control' if aa or c['label']=='A' else 'A')
 rows=list(csv.DictReader(f[phase+'/'+run['name']+'.csv'].decode().splitlines()));assert rows==run['rows'] and len(rows)==(8 if fam=='original' else 1)
 assert not f[phase+'/'+run['name']+'.stderr'].strip()
 for row in rows:
  for key in ['size','requested_ops','member_bytes']:assert row[key]==str(c['cell'][key])
  assert row['seed']==str(c['seed']) and row['cpu_start']==row['cpu_end']=='2' and int(row['elapsed_ns'])>0 and int(row['tree_bytes'])>0
  if fam=='iterator':
   for key in ['mask','direction','encoding','warmup_passes']:assert row[key]==str(c['cell'][key])
   n=c['cell']['size'];visits=((c['cell']['requested_ops']+n-1)//n)*n;assert int(row['operations'])==visits and int(row['traversals'])==visits//n and row['checksum']==row['expected_checksum']
  groups[(c['cell']['id'],row['case'],c['block'])].append((c,row))
assert r['finished_utc']<'2026-10-19T10:15:00'
qualified={};reference={}
if not aa:
 for n,h in j(fam+'-AA-evidence-seal.json').items():assert sha(f[n])==h
 aa_claim=j(fam+'-AA/audit.json');qualified={x['id']:x['qualified'] for x in aa_claim['cells']}
 for run in j(fam+'-AA/result.json')['runs']:
  for z in run['rows']:reference[(run['cell']['id'],z['case'],run['block'])]=z
cells={}
for (cid,case,block),pairs in sorted(groups.items()):
 assert [c['position'] for c,z in pairs]==list(range(4)) and [c['label'] for c,z in pairs]==list('ABBA')
 for field in fields:assert len({z[field] for c,z in pairs})==1
 if not aa:
  for c,z in pairs:
   for field in fields:assert z[field]==reference[(cid,case,block)][field]
 ns=[int(z['elapsed_ns']) for c,z in pairs];effect=(D(ns[1]+ns[2])/D(ns[0]+ns[3])-1)*100;n=pairs[0][0]['cell']['size'];cellid=cid+'/'+case
 cell=cells.setdefault(cellid,dict(id=cellid,size=n,case=case,required_for_acceptance=(original[(n,case)]['required_for_acceptance'] if fam=='original' else True),blocks=[]))
 cell['blocks'].append(dict(block=block,seed=1301+block%3,effect_pct=str(effect),minimum_window_ns=min(ns)))
for cell in cells.values():
 assert [b['block'] for b in cell['blocks']]==list(range(6));windows=all(b['minimum_window_ns']>=10000000 for b in cell['blocks']);values=[D(b['effect_pct']) for b in cell['blocks']]
 q=windows and (all(abs(v)<=1 for v in values) if aa else qualified[cell['id']]);cell['qualified']=q
 if not q:decision='PARK' if cell['required_for_acceptance'] else 'UNQUALIFIED_DIAGNOSTIC'
 elif aa:decision='QUALIFIED'
 elif all(v<=1 for v in values):decision='GUARD_PASS'
 elif all(v>1 for v in values):decision='REJECT'
 else:decision='PARK'
 cell['decision']=decision
for claimed in claim['cells']:
 own=cells[claimed['id']]
 for key in ['id','size','case','required_for_acceptance','qualified','decision','blocks']:assert own[key]==claimed[key],(claimed['id'],key)
assert len(cells)==(40 if fam=='original' else 82)
reject=any(c['decision']=='REJECT' for c in cells.values());park=any(c['decision']=='PARK' for c in cells.values());decision='REJECT' if reject else ('PARK' if park else ('QUALIFIED' if aa else 'PHASE_PASS_NOT_ACCEPTANCE'))
assert claim['decision']==decision
report=dict(audit_status='PASS',phase=phase,revision=rev,reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),processes=expected_processes,rows=sum(len(x['rows']) for x in r['runs']),phase_seconds=r['elapsed_seconds'],sealed_public_artifacts=len(seal),cells=list(cells.values()),qualified_cells=sum(c['qualified'] for c in cells.values()),required_cells=sum(c['required_for_acceptance'] for c in cells.values()),qualified_required_cells=sum(c['qualified'] and c['required_for_acceptance'] for c in cells.values()),decision=decision,source_selection='NONE',all_identity_and_same_fixture_memory_joins_pass=True,post_identity_idle_verified_at=post['checked_utc'],scope='Independent raw statistics/identity/metadata audit; detailed numeric fixture models require a separate Intel independent-auditor result.')
Path('experiments/ARM-MASK-FOLLOWUP-001/'+phase.upper()+'-ROOT-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='cells'},indent=2))
