"""Read-only audit of frozen secondary-host results and scope arithmetic."""
import collections,csv,hashlib,json,math
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parent.parent
D=R/'scratch/intel-followup/harvest/results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
P=load(H/'protocol.json');gate=load(H/'INDEPENDENT-PROBE-GATES.json')
assert sha(H/'INDEPENDENT-PROBE-GATES.json')=='746f828b6864afa3c27b828f175e63b6c308b4d2e2147820c3a0aed0a9c6097f'
for name,digest in load(H/'PREEXEC-HASHES.json')['files'].items():assert sha(H/name)==digest
approval=load(D/'probes-reviewed.json')
assert approval['protocol_sha256']==sha(H/'protocol.json')
assert approval['reviewer_evidence_sha256']==sha(H/'INDEPENDENT-PROBE-GATES.json')
assert approval['pebs'] is False and approval['lbr'] is False
for kind in ['pebs','lbr']:assert approval['raw_sha256'][kind]==gate['probes'][kind]['raw_sha256']
builds=load(D/'build-sha256.json')
assert builds==load(R/'experiments/INTEL-PARKED-PROFILES-001/results/build-sha256.json')
assert len(builds)==265 and sum(name.startswith('build/') for name in builds)==44
for name,digest in builds.items():
 path=R/('scratch/intel-parked-symfs/tmp/bplus-intel-parked-001' if name.startswith('build/') else 'scratch/intel-parked-profiles-inputs')/name
 assert sha(path)==digest
commands=load(D/'validation-commands.json')
assert len(commands)==73 and all(x['returncode']==0 for x in commands)
for variant in ['base','itA','itB','scanB']:
 for mode in ['native','sanitize']:
  text=(D/f'{variant}-tests-{mode}.stdout').read_text()
  assert '43 passed' in text and '0 failed, 43 total' in text
  if variant!='scanB':
   for oracle,n in [('cache-oracle',28192),('cache-oracle-additive',89428)]:
    assert (D/f'{variant}-{oracle}-{mode}.stdout').read_text().strip()==f'PASS {n} iterator state checks sizeof={24 if variant=="itA" else 16}'
ignored={'elapsed_ns','ns_per_op','ops_per_sec','thread_elapsed_ns','cpu_start','cpu_end','start_cpu','end_cpu','qos_reported_start','qos_reported_end','qos_relpri_start','qos_relpri_end','qos_effective','warmup_elapsed_ns'}
def semantic(path,driver):
 text=path.read_text()
 row=json.loads(text) if driver=='guard' else list(csv.DictReader(text.splitlines()))[0]
 return {k:str(v) for k,v in row.items() if k not in ignored}
semantic_cases=0
for cell in P['cells']:
 per_mode=collections.defaultdict(list)
 for variant in cell['variants']:
  tag='check-'+cell['id']+'-'+variant
  original=semantic(D/(tag+'-original.stdout'),cell['driver'])
  native=semantic(D/(tag+'-profile.stdout'),cell['driver'])
  sanitized=semantic(D/(tag+'-sanitize.stdout'),cell['driver'])
  assert original==native
  assert {k:v for k,v in native.items() if k!='tree_bytes'}=={k:v for k,v in sanitized.items() if k!='tree_bytes'}
  per_mode['native'].append(native);per_mode['sanitize'].append(sanitized);semantic_cases+=1
 assert all(all(x==rows[0] for x in rows) for rows in per_mode.values())
ROOTS={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'}
def scope(tag):
 s=load(D/(tag+'.scope.json'));a=s['before'];b=s['after']
 ds=[y-x for x,y in zip(a['cpu2'],b['cpu2'])];busy=sum(ds)-ds[3]-ds[4]
 ticks=lambda x:sum(int(x['proc'].rsplit(')',1)[1].split()[i]) for i in [11,12])
 work=ticks(b)-ticks(a);error=100*abs(busy-work)/max(1,busy)
 assert abs(error-s['accounting_error_percent'])<1e-9
 valid=a['affinity']==b['affinity']==[2] and a['sibling_offline'] and b['sibling_offline'] and error<=1
 for point in [a,b]:
  assert point['online_sibling_topology'] in ['2','2,50']
  assert point['proc'].rsplit(')',1)[1].split()[0]!='Z'
 assert a['proc'].split()[0]==b['proc'].split()[0]
 assert valid==s['pass']
 return {'pass':valid,'accounting_error_percent':error,'start':a['time'],'end':b['time'],'pid':a['proc'].split()[0],'topology_before':a['online_sibling_topology'],'topology_after':b['online_sibling_topology'],'sibling_offline':a['sibling_offline'] and b['sibling_offline']}
records=[];windows=[]
for index,cell in enumerate(P['cells']):
 variants=cell['variants'] if index%2==0 else list(reversed(cell['variants']))
 for variant in variants:
  tag=cell['id']+'-'+variant;r=load(D/(tag+'.record.json'))
  assert r['cell']==cell['id'] and r['variant']==variant and r['status']=='COLLECTED'
  assert r['binary_sha256']==builds['build/'+variant+'/'+cell['driver']]
  assert r['workload_command']==['numactl','--all','--physcpubind=2','--membind=0','build/'+variant+'/'+cell['driver']]+cell['args']
  assert r['deep']==[]
  if cell['deep']:assert 'probe' in r['deep_skipped']
  assert len(r['captures'])==3
  metrics=collections.defaultdict(list);captures=[]
  for rep,stored in enumerate(r['captures'],1):
   name=tag+f'-L2-{rep}';path=D/(name+'.stderr');assert sha(path)==stored['raw_sha256']
   lines=path.read_text().splitlines();heads=[i for i,l in enumerate(lines) if l.startswith('Timestamp,Area,Value,Unit,')]
   assert len(heads)==1
   rows=[row for row in csv.DictReader(lines[heads[0]:]) if row.get('Area')]
   times=collections.defaultdict(list)
   for row in rows:
    assert math.isfinite(float(row['Value'])) and math.isfinite(float(row['Multiplex']))
    if row['Area'] in ROOTS:times[row['Timestamp']].append(row)
    if row['Unit'] in ['% Slots','% Slots <']:metrics[row['Area']].append(float(row['Value']))
   roots=len(times)==5 and all(len(group)==4 and {x['Area'] for x in group}==ROOTS and all(x['Unit'] in ['% Slots','% Slots <'] and 0<=float(x['Value'])<=100 for x in group) and abs(sum(float(x['Value']) for x in group)-100)<=.3 for group in times.values())
   mux=bool(rows) and all(float(row['Multiplex'])==100 for row in rows)
   sc=scope(name);qualified=roots and mux and sc['pass']
   assert qualified==stored['qualified']
   cmd=stored['command'];assert cmd[cmd.index('-C')+1]=='2' and '-l2' in cmd
   captures.append({'tag':name,'qualified':qualified,'root_partition':roots,'all_mux100':mux,'scope':sc,'raw_sha256':sha(path)})
   windows.append((sc['start'],sc['end']))
  assert len({c['scope']['pid'] for c in captures})==1
  records.append({'cell':cell['id'],'variant':variant,'all_l2_qualified':all(c['qualified'] for c in captures),'captures':captures,'slot_means':{k:sum(v)/len(v) for k,v in metrics.items()},'record_sha256':sha(D/(tag+'.record.json'))})
assert len(records)==16
assert all(a[1]<=b[0] for a,b in zip(windows,windows[1:]))
preflight=load(D/'preflight.json');assert preflight['pass'] and not preflight['errors']
release=load(D/'restore.json');assert release['pass'] and release['marker']['state']=='RELEASED' and release['marker']['original_sibling_online']=='1' and release['marker']['original_sibling_topology']=='2,50' and release['owned_remaining']==[]
result={'reviewer':'/root/intel_b_review','backend':'Codex','model':'unknown','token_cost':'unknown','configurations':records,'qualified_configurations':sum(r['all_l2_qualified'] for r in records),'qualified_windows':sum(c['qualified'] for r in records for c in r['captures']),'completed_semantic_cases':semantic_cases,'validation_commands':len(commands),'native_sanitizer_test_suites':8,'iterator_cache_oracles':12,'transferred_elf_hashes_verified':44,'source_driver_hashes_verified':221,'windows_serial':True,'deep_methods_disabled':True,'gate_evidence_sha256':sha(H/'INDEPENDENT-PROBE-GATES.json'),'preflight_sha256':sha(D/'preflight.json'),'release_sha256':sha(D/'restore.json'),'source_adoption':'NONE','timing_acceptance':False,'limits':['Fresh secondary-host/sibling-offline condition; no cross-host causal comparison.','No per-operation counts; update state evolves.','Release proof read from harvested evidence; no independent SSH by reviewer.','Ambient profiler condition remains disclosed; no claim of physically interference-free host.']}
print(json.dumps(result,indent=2))
