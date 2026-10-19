"""Independent frozen ARM024 A/A reconstruction, no worker analyzer imports."""
import collections,csv,datetime,decimal,hashlib,json,pathlib,subprocess,sys
r=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);p=r/'aa';j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();x=j(p/'result.json');e=j(r/'expected.json');seal=j(r/'aa-evidence-seal.json');profile=j(r/'profile-evidence-seal.json');pub=j(p/'PUBLICATION.json')
assert x['status']=='complete' and len(x['runs'])==48 and x['elapsed_seconds']<=300
assert seal['execution_freeze_sha256']==x['execution_freeze_sha256']==sha(r/'execution-freeze.json')=='52169964c692b8accb350efaeebfa95d7ca87832db306722114254ca40a6ffe4'
for n,h in j(r/'execution-freeze.json')['files'].items():assert sha(r/n)==h,n
for n,h in seal['files'].items():assert sha(r/n)==h,n
for n,v in pub.items():assert sha(p/n)==v['public_sha256'],n
assert seal['profile_evidence_seal_sha256']==sha(r/'profile-evidence-seal.json')
old_seal=subprocess.check_output(['git','show','4e43c9f59:experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/024-corrected-iterator/profile-evidence-seal.json']);assert hashlib.sha256(old_seal).hexdigest()==sha(r/'profile-evidence-seal.json')
for n,h in profile['files'].items():assert sha(r/n)==h,n
assert x['source_hashes_before']==x['source_hashes_after']==e['source_hashes'];assert x['binary_sha256_before']==x['binary_sha256_after']==e['aa_binary_sha256']=='330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc'
profile_pub=j(r/'profile/PUBLICATION.json')
for k,n in [('profile_audit_sha256','audit.json'),('profile_mapping_sha256','code-map.json')]:assert x[k]==profile_pub[n]['raw_sha256']==profile_pub[n]['public_sha256']==sha(r/'profile'/n)
assert j(r/'profile/audit.json')['status']=='pass' and j(r/'profile/code-map.json')['status']=='mapped'
schedule=[]
for b in range(6):
 for n in ([100000,1000000] if b%2==0 else [1000000,100000]):
  for pos,label in enumerate('ABBA'):schedule.append(dict(index=len(schedule),block=b,size=n,seed=701+b%3,position=pos,label=label,case='iterate',requested_ops=50000000,member_bytes=16,binary='baseline'))
assert schedule==j(r/'aa-schedule.json');groups=collections.defaultdict(list);memory=collections.defaultdict(set);previous=datetime.datetime.fromisoformat(x['started_utc'])
for s,run in zip(schedule,x['runs']):
 for k in ['block','size','seed','position','label']:assert run[k]==s[k]
 assert run['name']==f'b{s["block"]}-n{s["size"]}-p{s["position"]}-{s["label"]}' and run['returncode']==0
 t0=datetime.datetime.fromisoformat(run['started_utc']);t1=datetime.datetime.fromisoformat(run['finished_utc']);assert previous<=t0<=t1 and (t1-t0).total_seconds()<=30;previous=t1
 expected_cmd=['<corrected-baseline>/build/adapter-requalification/btree-bench','--case','iterate','--size',str(s['size']),'--ops','50000000','--member-bytes','16','--seed',str(s['seed'])];assert run['command']==expected_cmd
 rows=list(csv.DictReader((p/(run['name']+'.csv')).read_text().splitlines()));assert rows==[run['row']];z=rows[0];assert not (p/(run['name']+'.stderr')).read_text().strip()
 n=s['size'];values={'case':'iterate','size':n,'requested_ops':50000000,'member_bytes':16,'seed':s['seed'],'operations':50000000,'checksum':(n*(n-1)//2)*(50000000//n),'traversals':50000000//n,'warmup_passes':1,'cpu_start':2,'cpu_end':2}
 for k,v in values.items():assert z[k]==str(v),(run['name'],k)
 assert int(z['elapsed_ns'])>0 and int(z['tree_bytes'])>0;groups[(n,s['block'])].append(z);memory[(n,s['seed'])].add(z['tree_bytes'])
assert previous<=datetime.datetime.fromisoformat(x['finished_utc']);assert all(len(v)==1 for v in memory.values())
effects=[]
for (n,b),rows in sorted(groups.items()):
 assert len(rows)==4 and len({z['tree_bytes'] for z in rows})==1
 t=[decimal.Decimal(z['elapsed_ns'])/decimal.Decimal(z['operations']) for z in rows];effect=100*((t[1]+t[2])/(t[0]+t[3])-1);minimum=min(int(z['elapsed_ns']) for z in rows);effects.append(dict(size=n,block=b,seed=701+b%3,effect_pct=float(effect),min_window_ns=minimum,qualified=abs(effect)<=1 and minimum>=10000000))
summary={str(n):dict(qualified=all(z['qualified'] for z in effects if z['size']==n),max_abs_pct=max(abs(z['effect_pct']) for z in effects if z['size']==n),minimum_window_ns=min(z['min_window_ns'] for z in effects if z['size']==n)) for n in [100000,1000000]}
worker=j(p/'audit.json')
for name,h in worker['raw_sha256'].items():
 assert pub[name]['raw_sha256']==h
 if name.endswith('.csv') or name=='result.json':assert sha(p/name)==h
 elif name.endswith('.stderr'):assert h==hashlib.sha256(b'').hexdigest() and not (p/name).read_text().strip()
assert worker['both_sizes_qualified']==all(z['qualified'] for z in summary.values())
for z,w in zip(effects,worker['effects']):
 assert all(z[k]==w[k] for k in ['size','block','seed','min_window_ns','qualified']);assert abs(z['effect_pct']-w['effect_pct'])<1e-10
result=dict(status='pass',revision='73c9e313f',public_artifact_hashes=len(pub),aa_seal_hashes=len(seal['files']),profile_seal_hashes=len(profile['files']),profile_seal_unchanged_from='4e43c9f59',processes=48,blocks=12,both_sizes_qualified=all(z['qualified'] for z in summary.values()),summary=summary,effects=effects,fixture_owned_bytes={f'{n}/{seed}':list(v)[0] for (n,seed),v in memory.items()},actual_binary_sha256=e['aa_binary_sha256'],source_commit=e['commit'],source_selection='NONE',limits=['Independent raw auditor; reviewer authored imported AMD base harness','No runner access or new measurement','A/A establishes fixture/session precision, not an optimization effect','No timing transfer from AMD or previous ARM identities'])
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
