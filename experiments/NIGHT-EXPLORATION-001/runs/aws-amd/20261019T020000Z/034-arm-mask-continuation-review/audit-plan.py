import pathlib,json,hashlib,subprocess,collections,itertools,sys
revision=sys.argv[1];prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/'
def blob(n,rev=revision):return subprocess.check_output(['git','show',rev+':'+n])
def read(n):return json.loads(blob(prefix+n))
def sha(b):return hashlib.sha256(b).hexdigest()
f=read('plan-freeze.json')
for n,h in f['files'].items():assert sha(blob(prefix+n))==h,n
imports=read('existing-artifacts.json')
for n,h in imports.items():assert sha(blob(n))==h,n
ids=read('identities.json')
for n,h in ids['source_hashes'].items():assert sha(blob(n,ids['source_commit']))==h,n
g=read('iterator-guards.json');o=read('original-guards.json');seeds=read('seed-reservations.json');budget=read('phase-budgets.json')
assert len(g)==82 and len({x['id'] for x in g})==82 and all(x['required_for_acceptance'] for x in g)
keys=lambda x:(x['size'],x['member_bytes'],x['encoding'],x['direction'],x['mask'],x.get('construction','shuffled'))
assert len({keys(x) for x in g})==82
families=collections.Counter(x['family'] for x in g)
assert sorted(families.values())==[6,20,24,32]
actual={(x['size'],x['direction'],x['mask']) for x in g if x['family']=='all-output-masks'}
assert actual==set(itertools.product([100000,1000000],['forward','reverse'],range(8)))
assert len([x for x in g if x['requested_ops']==50000000])==4
assert all(x['requested_ops']==(50000000 if x['family']=='all-output-masks' and x['mask']==6 else 20000000) and x['warmup_passes']==3 for x in g)
assert len(o)==40 and len({(x['size'],x['case']) for x in o})==40
for x in o:
 assert x['required_for_acceptance']==(x['case'] in ['lookup-hit','lookup-miss','rank','scan','update'] or x['case'] in ['insert','delete'] and x['size']>=100000)
assert sum(x['required_for_acceptance'] for x in o)==29
assert sum(x['cap_seconds'] for x in budget['phases'])==budget['sum_cap_seconds']==6600
assert budget['total_target_seconds']==budget['sum_cap_seconds']+budget['review_handoff_reserve_seconds']==7200
seen=set()
for k,s in seeds.items():assert not seen&set(s),k;seen.update(s)
print(json.dumps({'revision':revision,'freeze_inputs':len(f['files']),'imports':len(imports),'source_hashes':len(ids['source_hashes']),'iterator_guards':len(g),'families':dict(families),'iterator_rows_per_phase':len(g)*24,'original_cells':len(o),'original_required':29,'original_diagnostic':11,'phase_cap_sum':6600,'review_reserve':600,'disjoint_seed_groups':True,'execution_drivers_frozen':f['execution_drivers_frozen'],'status':'structural_plan_checks_pass_decision_clarification_pending'},indent=2))
