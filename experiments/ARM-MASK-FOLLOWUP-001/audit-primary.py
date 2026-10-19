import subprocess,tarfile,io,json,hashlib,csv,datetime,collections,decimal,sys
from pathlib import Path
D=decimal.Decimal;decimal.getcontext().prec=40
rev,phase=sys.argv[1:3];assert phase in ('primary-AA','primary-replication')
prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/'
with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',rev,prefix]))) as t:f={m.name[len(prefix):]:t.extractfile(m).read() for m in t if m.isfile()}
j=lambda n:json.loads(f[n]);sha=lambda b:hashlib.sha256(b).hexdigest()
r=j(phase+'/result.json');schedule=j('schedules/'+phase+'.json');e=j('expected.json');freeze=j('timing-freeze.json');claimed=j(phase+'/audit.json')
for n,h in freeze['files'].items():assert sha(f[n])==h,n
seal=j(phase+'-evidence-seal.json');publication=j(phase+'/PUBLICATION.json');post=j(phase+'-post-identity-idle.json')
for n,h in seal.items():assert sha(f[n])==h,n
for n,x in publication.items():assert sha(f[phase+'/'+n])==x['public_sha256'],n
assert post['timing_inputs']==freeze['files'] and post['timing_freeze_sha256']==sha(f['timing-freeze.json'])
assert post['owned_units']==post['owned_cgroup_pids']==[]
assert post['protected_binaries']==e['protected_binaries'] and post['guard_binary_sha256']==r['guard_binaries_after']
assert r['composite_before']==r['composite_after'] and post['snapshots']==r['composite_after']['snapshots']
assert post['prior_raw_artifacts']=={n:x['raw_sha256'] for n,x in j('validation/PUBLICATION.json').items()}
assert post['actual_sources']=={k:r['sources_after'][k] for k in ['actual','actualA']}

assert r['status']=='complete' and len(r['runs'])==len(schedule)==48 and r['elapsed_seconds']<=300
assert r['protected_before']==r['protected_after']==e['protected_binaries']
assert r['sources_before']==r['sources_after'] and r['guard_binaries_before']==r['guard_binaries_after']
for v,x in r['sources_before'].items():
 expected=dict(e['source_hashes'])
 if v in ('A','actualA'):expected['src/zset_btree.c']=e['candidate_source_sha256']
 assert x==expected
assert r['timing_freeze_sha256']==sha(f['timing-freeze.json']) and r['schedule_sha256']==sha(f['schedules/'+phase+'.json'])
assert r['finished_utc']<'2026-10-19T10:15:00'
aa_reference={}
if phase=='primary-replication':
 aa_result=j('primary-AA/result.json');assert j('primary-AA/audit.json')['all_required_qualified']
 for name,h in j('primary-AA-evidence-seal.json').items():assert sha(f[name])==h
 aa_reference={x['name']:x['rows'][0] for x in aa_result['runs']}
groups=collections.defaultdict(list)
for i,(run,c) in enumerate(zip(r['runs'],schedule)):
 assert all(run[k]==v for k,v in c.items()) and run['checked'] and run['returncode']==0
 start=datetime.datetime.fromisoformat(run['started_utc']);end=datetime.datetime.fromisoformat(run['finished_utc']);assert 0<=(end-start).total_seconds()<=60
 if i:assert r['runs'][i-1]['finished_utc']<=run['started_utc']
 assert c['index']==i and c['position']==i%4 and c['label']=='ABBA'[i%4] and c['block']==i//8
 n=c['cell']['size'];assert n in (100000,1000000) and c['seed']==1101+c['block']%3
 assert c['variant']==('control' if phase=='primary-AA' or c['label']=='A' else 'A')
 raw=f[phase+'/'+run['name']+'.csv'];rows=list(csv.DictReader(raw.decode().splitlines()));assert rows==run['rows'] and len(rows)==1;z=rows[0]
 assert not f[phase+'/'+run['name']+'.stderr'].strip()
 expected=dict(case='iterate',size=n,seed=c['seed'],requested_ops=50000000,member_bytes=16,operations=50000000,traversals=50000000//n,checksum=50000000*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
 for k,v in expected.items():assert z[k]==str(v),(i,k)
 assert int(z['elapsed_ns'])>0
 if aa_reference:
  for field in ['case','size','seed','requested_ops','member_bytes','operations','traversals','checksum','warmup_passes','tree_bytes']:assert z[field]==aa_reference[run['name']][field]
 groups[(n,c['block'])].append((c,z))
effects=[];aa=phase=='primary-AA';allgate=True
for (n,b),pairs in sorted(groups.items()):
 assert len(pairs)==4 and [c['position'] for c,z in pairs]==list(range(4))
 assert len({z['tree_bytes'] for c,z in pairs})==1
 ns=[int(z['elapsed_ns']) for c,z in pairs];eff=(D(ns[1]+ns[2])/D(ns[0]+ns[3])-1)*100;window=min(ns)>=10000000
 gate=window and (abs(eff)<=1 if aa else eff<=-2);allgate &= gate
 effects.append(dict(size=n,block=b,seed=1101+b%3,effect_pct=str(eff),minimum_window_ns=min(ns),gate_pass=gate,tree_bytes=int(pairs[0][1]['tree_bytes'])))
assert len(effects)==12
for cell in claimed['cells']:
 own=[x for x in effects if x['size']==cell['size']]
 for x,y in zip(own,cell['blocks']):assert x['block']==y['block'] and D(x['effect_pct'])==D(y['effect_pct']) and x['minimum_window_ns']==y['minimum_window_ns']
assert allgate==(claimed['all_required_qualified'] if aa else claimed['all_primary_pass'])
report=dict(audit_status='PASS',phase=phase,revision=rev,reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),processes=48,blocks=12,phase_seconds=r['elapsed_seconds'],gate_pass=allgate,decision='QUALIFIED' if aa and allgate else ('PRIMARY_PASS' if allgate else ('PARK' if aa else 'REJECT')),source_selection='NONE',effects=effects,protected_sources_and_binaries_unchanged=True,sealed_public_artifacts=len(seal),post_identity_idle_verified_at=post['checked_utc'])
Path('experiments/ARM-MASK-FOLLOWUP-001/'+phase.upper()+'-ROOT-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
