#!/usr/bin/env python3
"""Independently reconstruct immutable native frontend diagnostic rows."""
import argparse,collections,csv,datetime,decimal,hashlib,io,json,subprocess,tarfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('revision');p.add_argument('phase',choices=['native-AA','native-comparison']);p.add_argument('--out',required=True,type=Path);a=p.parse_args()
prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis/'
with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',a.revision,prefix]))) as t:
 files={m.name[len(prefix):]:t.extractfile(m).read() for m in t if m.isfile()}
j=lambda n:json.loads(files[n]);sha=lambda b:hashlib.sha256(b).hexdigest();dt=datetime.datetime.fromisoformat
D=decimal.Decimal;decimal.getcontext().prec=40
freeze=j('native-execution-freeze.json');ids=j('identities.json');cells={x['id']:x for x in j('cells.json')};oracle=j('fixture-oracle.json')
for n,h in freeze['files'].items():assert sha(files[n])==h,n
s=j(a.phase+'/result.json');schedule=j('schedules.json')[a.phase];claimed=j(a.phase+'/audit.json')
assert s['status']=='complete' and len(s['runs'])==len(schedule)==144
assert s['cpu']==2 and s['freeze_sha256']==sha(files['native-execution-freeze.json'])
assert s['identities_before']==s['identities_after']
assert s['identities_before']['binaries']=={k:v['sha256'] for k,v in ids['binaries'].items()}
assert set(s['identities_before']['sources'])==set(ids['binaries'])
for name,values in s['identities_before']['sources'].items():
 expected=dict(ids['source_hashes'])
 if name.endswith('-A'):expected['src/zset_btree.c']=ids['candidate_source_sha256']
 if name.startswith('h4-'):expected['bench/iterator_modes.c']=sha(files['inputs/iterator_modes.c'])
 assert values==expected
assert s['deadline']=='2026-10-19T11:45:00+00:00'
assert 0<float(s['elapsed_seconds'])<=600
assert 0<(dt(s['finished_utc'])-dt(s['started_utc'])).total_seconds()<=600
assert (dt(s['deadline'])-dt(s['started_utc'])).total_seconds()>=620
assert dt(s['finished_utc'])<dt(s['deadline'])
assert claimed['result_sha256']==sha(files[a.phase+'/result.json'])
assert len(claimed['raw_files_sha256'])==288
for n,h in claimed['raw_files_sha256'].items():assert sha(files[a.phase+'/'+n])==h
seal=j(a.phase+'-evidence-seal.json')['files']
for n,h in seal.items():assert sha(files[n])==h,n
publication=j(a.phase+'/PUBLICATION.json')
for n,v in publication.items():assert sha(files[a.phase+'/'+n])==v['public_sha256'],n
post=j(a.phase+'-postcheck.json');preflight=j(a.phase+'-preflight.json')
assert not post['owned_units'] and not post['owned_cgroup_pids']
assert post['identities']==preflight['identities']==s['identities_before']
assert post['lease_sha256']==preflight['lease_sha256']==s['lease_sha256']
assert post['native_freeze_sha256']==preflight['native_freeze_sha256']==s['freeze_sha256']
assert post['frozen_inputs']==preflight['frozen_inputs']==freeze['files']
assert dt(preflight['checked_utc'])<dt(s['started_utc'])<dt(s['finished_utc'])<dt(post['checked_utc'])
assert preflight['remaining_seconds']>=620 and preflight['release_timer_active']=='active'
assert preflight['coordinator_status']['returncode']==3 and 'STOPPED' in preflight['coordinator_status']['stdout']
assert preflight['coordinator_pid']['returncode']==7 and preflight['coordinator_pid']['stdout']=='0'
assert preflight['containers']==dict(returncode=0,stdout='',stderr='')
refs={};aa=None
if a.phase=='native-comparison':
 aa=j('native-AA/audit.json');ar=j('native-AA/result.json')
 assert ar['status']=='complete' and len(ar['runs'])==144 and aa['status']=='integrity_pass'
 assert s['AA_result_sha256']==aa['result_sha256']==sha(files['native-AA/result.json'])
 assert s['AA_audit_sha256']==sha(files['native-AA/audit.json'])
 assert ar['identities_before']==ar['identities_after']==s['identities_before']
 assert ar['freeze_sha256']==s['freeze_sha256'] and ar['lease_sha256']==s['lease_sha256']
 assert dt(ar['finished_utc'])<=dt(s['started_utc'])
 for n,h in aa['raw_files_sha256'].items():assert sha(files['native-AA/'+n])==h
 for r in ar['runs']:refs[(r['cell'],r['seed'])]=list(csv.DictReader(files['native-AA/'+r['stdout']].decode().splitlines()))[0]
groups=collections.defaultdict(list);last=dt(s['started_utc'])
semantic=['case','size','seed','requested_ops','member_bytes','operations','traversals','checksum','warmup_passes','tree_bytes','direction','mask','encoding','expected_checksum','construction_fingerprint']
for i,(r,c) in enumerate(zip(s['runs'],schedule)):
 assert c['index']==i and c['position']==i%4 and c['block']==i//24
 assert c['seed']==1601+c['block']%3
 assert c['source']==('control' if a.phase=='native-AA' or i%4 in (0,3) else 'A')
 assert all(r[k]==v for k,v in c.items()) and r['checked'] and r['returncode']==0
 assert last<=dt(r['started_utc'])<dt(r['finished_utc'])<=dt(s['finished_utc'])
 assert (dt(r['finished_utc'])-dt(r['started_utc'])).total_seconds()<=60;last=dt(r['finished_utc'])
 assert not files[a.phase+'/'+r['stderr']].strip()
 rows=list(csv.DictReader(files[a.phase+'/'+r['stdout']].decode().splitlines()));assert len(rows)==1;z=rows[0]
 cell=cells[c['cell']];n=cell['size'];visits=cell['requested_ops'];traversals=visits//n
 checksum=(visits*(n-1)//2 if cell['frontend']=='primary' else oracle[f'{n}/{c["seed"]}']['h4_one_traversal_checksum']*traversals)&((1<<64)-1)
 expected=dict(case='iterate' if cell['frontend']=='primary' else 'iterator-modes',size=n,seed=c['seed'],requested_ops=visits,member_bytes=16,operations=visits,traversals=traversals,checksum=checksum,warmup_passes=cell['warmup_passes'],cpu_start=2,cpu_end=2)
 if cell['frontend']=='h4':expected.update(direction=cell['direction'],mask=4,encoding='integer',expected_checksum=checksum,construction_fingerprint=oracle[f'{n}/{c["seed"]}']['h4_construction_fingerprint'])
 for k,v in expected.items():assert z[k]==str(v),(i,k,z[k],v)
 for k in ['elapsed_ns','thread_elapsed_ns','tree_bytes','warmup_elapsed_ns']:assert int(z[k])>0
 ref=refs.setdefault((c['cell'],c['seed']),z)
 assert all(z.get(k)==ref.get(k) for k in semantic)
 groups[(c['cell'],c['block'])].append(z)
effects=[];qualification={}
for (cell,block),rows in sorted(groups.items()):
 assert len(rows)==4
 v=[D(z['elapsed_ns'])/D(z['operations']) for z in rows];effect=((v[1]+v[2])/(v[0]+v[3])-1)*100
 minimum=min(int(z['elapsed_ns']) for z in rows)
 effects.append(dict(cell=cell,block=block,seed=1601+block%3,effect_pct=str(effect),minimum_window_ns=minimum))
assert len(effects)==36
for cell in cells:
 own=[e for e in effects if e['cell']==cell]
 qualified=all(e['minimum_window_ns']>=10000000 for e in own)
 qualified &= all(abs(D(e['effect_pct']))<=1 for e in own) if aa is None else next(x['qualified'] for x in aa['cells'] if x['id']==cell)
 qualification[cell]=qualified;cc=next(x for x in claimed['cells'] if x['id']==cell)
 assert cc['qualified']==qualified
 for e,b in zip(own,cc['blocks']):assert e['block']==b['block'] and D(e['effect_pct'])==D(b['effect_pct']) and e['minimum_window_ns']==b['minimum_window_ns']
report=dict(audit_status='PASS',revision=a.revision,phase=a.phase,reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),processes=144,blocks=36,elapsed_seconds=s['elapsed_seconds'],qualified_cells=qualification,effects=effects,source_selection='NONE',prior_candidate_decision='REJECT',sealed_files=len(seal),post_identity_idle_checked_at=post['checked_utc'],scope='Independent raw reconstruction; H4 fixture oracle independently reviewed separately. No causal or acceptance claim.')
a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['audit_status','phase','processes','qualified_cells']}))
