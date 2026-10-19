import pathlib,json,csv,hashlib,datetime,decimal,sys,subprocess,statistics
p=pathlib.Path(sys.argv[1]);j=lambda n:json.loads((p/n).read_text());sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest();D=decimal.Decimal;decimal.getcontext().prec=40
r=j('primary-replication/result.json');freeze=j('timing-freeze.json');receipt=j('composite-correctness.json');seal=j('primary-replication-evidence-seal.json');pub=j('primary-replication/PUBLICATION.json');schedule=j('schedules/primary-replication.json');post=j('primary-replication-post-identity-idle.json');audit=j('primary-replication/audit.json')
for n,h in seal.items():assert sha(p/n)==h,n
for n,h in freeze['files'].items():assert sha(p/n)==h,n
for n,h in pub.items():assert sha(p/'primary-replication'/n)==h['public_sha256'],n
for n,h in audit['raw_sha256'].items():assert pub[n]['raw_sha256']==h,n
assert r['timing_freeze_sha256']==sha(p/'timing-freeze.json') and r['schedule_sha256']==sha(p/'schedules/primary-replication.json') and r['composite_receipt_sha256']==sha(p/'composite-correctness.json')
assert r['status']=='complete' and r['phase']=='primary-replication' and r['cpu']==2 and r['cap_seconds']==300 and 0<r['elapsed_seconds']<300 and len(r['runs'])==len(schedule)==48
for a,b in [('protected_before','protected_after'),('sources_before','sources_after'),('guard_binaries_before','guard_binaries_after'),('composite_before','composite_after')]:assert r[a]==r[b]
assert r['protected_before']==receipt['protected_binaries'] and r['guard_binaries_before']==receipt['guard_binary_sha256']
for variant,hashes in r['sources_before'].items():assert hashes==dict(receipt['source_hashes'],**({'src/zset_btree.c':receipt['candidate_source_sha256']} if variant in ['actualA','A'] else {}))
cb=r['composite_before'];assert cb['receipt_sha256']==r['composite_receipt_sha256'] and cb['original_status']=='failed' and cb['snapshots']==receipt['snapshots_before']
for f in ['binding_sha256','original_raw_result_sha256','suffix_raw_result_sha256','protected_binaries','guard_binary_sha256']:assert cb[f]==receipt[f]
t0=datetime.datetime.fromisoformat(r['started_utc']);t1=datetime.datetime.fromisoformat(r['finished_utc']);deadline=datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc);assert 0<(t1-t0).total_seconds()<300 and (deadline-t0).total_seconds()>=300 and t1<deadline
candidate='scratch/arm-exp005A-replication-13e459ff8/A/build/adapter-requalification/btree-bench';assert receipt['protected_binaries'][candidate]=='b1cb9e4b2a1df204a75b4b4a3264364c3f0b5b46dbf475bae72c3c9a3ee5811d'
prev=t0;groups={};baseline='scratch/adapter-worktree-13e459ff8/build/adapter-requalification/btree-bench';assert receipt['protected_binaries'][baseline]=='330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc'
for x,c in zip(r['runs'],schedule):
 assert all(x[k]==v for k,v in c.items()) and x['returncode']==0 and x['checked']
 assert x['variant']==('control' if x['position'] in [0,3] else 'A') and x['command'][0]=='<checkout>/'+(baseline if x['position'] in [0,3] else candidate) and x['seed']==1101+x['block']%3 and x['label']==['A','B','B','A'][x['position']]
 a=datetime.datetime.fromisoformat(x['started_utc']);b=datetime.datetime.fromisoformat(x['finished_utc']);assert prev<=a<=b<=t1 and (b-a).total_seconds()<=60;prev=b
 rows=list(csv.DictReader((p/'primary-replication'/(x['name']+'.csv')).read_text().splitlines()));assert rows==x['rows'] and len(rows)==1;z=rows[0];n=x['cell']['size'];assert n in [100000,1000000]
 expected={'size':n,'requested_ops':50000000,'member_bytes':16,'seed':x['seed'],'operations':50000000,'checksum':50000000*(n-1)//2,'traversals':50000000//n,'warmup_passes':1}
 assert z['case']=='iterate' and z['cpu_start']==z['cpu_end']=='2' and int(z['tree_bytes'])>0 and int(z['elapsed_ns'])>=10000000
 for k,v in expected.items():assert int(z[k])==v,(k,x['name'])
 groups.setdefault((n,x['block']),[]).append((x,z))
assert len(groups)==12;result={}
for (n,block),v in groups.items():
 assert [x['position'] for x,z in v]==[0,1,2,3]
 for f in ['case','size','requested_ops','member_bytes','seed','operations','checksum','tree_bytes','traversals','warmup_passes']:assert len({z[f] for x,z in v})==1
 ns=[int(z['elapsed_ns']) for x,z in v];effect=(D(ns[1]+ns[2])/D(ns[0]+ns[3])-1)*100;assert effect<=-2
 result.setdefault(n,[]).append({'block':block,'effect_pct':str(effect),'minimum_window_ns':min(ns)})
 reported=next(c for c in audit['cells'] if c['size']==n);assert reported['qualified'] and reported['decision']=='PRIMARY_PASS';rb=next(b for b in reported['blocks'] if b['block']==block);assert D(rb['effect_pct'])==effect and rb['minimum_window_ns']==min(ns)
assert audit['all_required_qualified'] and audit['decision']=='PHASE_PASS_NOT_ACCEPTANCE' and audit['all_primary_pass']
for k in ['protected_binaries','guard_binary_sha256']:assert post[k]==receipt[k]
assert post['snapshots']==receipt['snapshots_before'] and post['timing_inputs']==freeze['files'] and post['timing_freeze_sha256']==sha(p/'timing-freeze.json')
assert post['actual_sources']=={k:v for k,v in r['sources_before'].items() if k in ['actual','actualA']}
assert post['owned_units']==post['owned_cgroup_pids']==[] and datetime.datetime.fromisoformat(post['checked_utc'])>t1
# Independently pin the complete fresh AA evidence directory to the reviewed revision.
base='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/'
trees={v:subprocess.check_output(['git','rev-parse',v+':'+base+'primary-AA']).decode().strip() for v in ['53e193c5b','451456c2f']};assert len(set(trees.values()))==1
aar=j('primary-AA/result.json');aaa=j('primary-AA/audit.json');aap=j('primary-AA/PUBLICATION.json');assert aaa['all_required_qualified']
for name,h in j('primary-AA-evidence-seal.json').items():assert sha(p/name)==h
for name,h in aaa['raw_sha256'].items():assert aap[name]['raw_sha256']==h
for ar,br in zip(aar['runs'],r['runs']):
 assert (ar['block'],ar['cell'],ar['seed'],ar['position'])==(br['block'],br['cell'],br['seed'],br['position'])
 for field in ['case','size','requested_ops','member_bytes','seed','operations','checksum','tree_bytes','traversals','warmup_passes']:assert ar['rows'][0][field]==br['rows'][0][field],field
for field in ['timing_freeze_sha256','composite_receipt_sha256','protected_before','sources_before','guard_binaries_before','composite_before']:assert aar[field]==r[field]
assert datetime.datetime.fromisoformat(aar['finished_utc'])<t0
print(json.dumps(dict(revision='451456c2f',status='FRESH_PRIMARY_REPLICATION_GATE_PASS',fresh_AA_tree_ids=trees,seal_entries=len(seal),public_artifacts=len(pub),frozen_inputs=len(freeze['files']),rows=48,blocks=12,elapsed_seconds=r['elapsed_seconds'],results={n:dict(blocks=v,minimum_effect_pct=str(min(D(b['effect_pct']) for b in v)),maximum_effect_pct=str(max(D(b['effect_pct']) for b in v)),median_effect_pct=str(statistics.median(D(b['effect_pct']) for b in v)),minimum_window_ms=min(b['minimum_window_ns'] for b in v)/1e6) for n,v in result.items()},original_preparation_status='FAILED',baseline_sha256=receipt['protected_binaries'][baseline],source_selection='NONE',remote_access=False,scope='Primary-only exact historical A replication; no guard, profile, confirmation or acceptance claim'),indent=2))
