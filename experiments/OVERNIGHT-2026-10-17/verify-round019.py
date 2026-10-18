from pathlib import Path
import ast,collections,csv,datetime,hashlib,json,math,re,statistics
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=0;windows=[];patches=0;intervals=0;profile_captures=0;calibrations=0;branch_mappings=0
T=ast.parse((P/'verify-round016.py').read_text());fun=next(n for n in T.body if isinstance(n,ast.FunctionDef) and n.name=='apply_unified');scope={'re':re};exec(compile(ast.Module(body=[fun],type_ignores=[]),'<prior-patch-auditor>','exec'),scope);apply=scope['apply_unified']
def check(p,h):
 global checks
 assert sha(p)==h,str(p.relative_to(R));checks+=1
def runs(manifest):
 m=json.loads(manifest.read_text())
 for r in m.get('runs',[]):
  windows.append((datetime.datetime.fromisoformat(r['started_utc']),datetime.datetime.fromisoformat(r['ended_utc']),str(manifest.relative_to(R)),r['name']))
  for k in ['stdout','stderr']:
   if k in r:check(R/r[k],r[k+'_sha256'])
 return m
mutable={'.workspace-memory/LIVE-STATUS.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md'}
prior=json.loads((P/'ROUND-018-SHA256.json').read_text())
for n,h in prior.items():
 if n not in mutable:check(R/n,h)
for e in range(2,7):
 E=R/f'experiments/EXP-{e:03d}';f=json.loads((E/'freeze.json').read_text());B=R/f['snapshot_root'];old=(B/'control/src/zset_btree.c').read_text()
 for v,files in f['files'].items():
  for n,h in files.items():check(B/v/n,h)
 for v in ['A','B','C']:
  assert apply(old,(E/'variants'/v/'candidate.patch').read_text())==(B/v/'src/zset_btree.c').read_text();patches+=1
 assert (R/'src/zset_btree.c').read_text()==old
F6=json.loads((R/'experiments/EXP-006/freeze.json').read_text())
# Sampling: reconstruct symbols/counts from raw PCs and atos results.
for variant in ['control','C']:
 Q=P/'PROFILE-005'/variant;m=runs(Q/'manifest.json');assert m['status']=='complete';B=R/m['snapshot']
 for n,h in m['files'].items():check(B/n,h)
 for n,h in m['binaries'].items():check(B/'build'/n,h)
 baseline=(R/'scratch/overnight-harness-007-attempt2/base/bench/batch_lookup.c').read_text();assert apply(baseline,(Q/'profile.patch').read_text())==(B/'bench/batch_lookup.c').read_text();patches+=1
 by={r['name']:r for r in m['runs']}
 for tag,binary,expected in [(f'cal-{interval}','calibrate',m['calibrations'][i]) for i,interval in enumerate([1000,3001])]+[(c['name'],'batch-profile',c) for c in m['captures']]:
  pcs=list(csv.reader((R/by[tag]['stderr']).open()));header=[x for x in pcs if x[0]=='PROFILE'];pcs=[x for x in pcs if x[0]=='PC'];assert len(header)==1 and int(header[0][3])==len(pcs) and header[0][4]=='0'
  addresses=sorted({x[2] for x in pcs if x[1]==binary});syms=(R/by[tag+'-symbols']['stdout']).read_text().splitlines();assert len(addresses)==len(syms);mapping=dict(zip(addresses,syms));counts=collections.Counter(mapping[x[2]].split(' (in ')[0] if x[1]==binary else x[4] for x in pcs);assert dict(counts)==expected['counts'] and len(pcs)==expected['samples'];assert expected.get('pass',expected.get('sufficient'))
  if binary=='calibrate':calibrations+=1
  else:profile_captures+=1
# Diagnostic sources, validation and fixed raw-row schedule.
for Q in [P/'DIAG-019',P/'DIAG-019/attempt-002']:
 f=json.loads((Q/'freeze.json').read_text());B=R/f['snapshot'];m=runs(Q/'validation.json')
 check(Q/'PLAN.md',f['plan_sha256']);check(Q/'run.py',f['runner_sha256'])
 for v,files in f['files'].items():
  for n,h in files.items():check(B/v/n,h)
  source=v.split('-')[0];old=(R/F6['snapshot_root']/source/'src/zset_btree.c').read_text();patch=(Q/(v+'.patch')).read_text();assert (apply(old,patch) if patch else old)==(B/v/'src/zset_btree.c').read_text();patches+=1
 for n,h in m.get('binaries',{}).items():
  source,kind,exe=n.rsplit('-',2);check(B/source/'build'/f'{kind}-{exe}',h)
Q=P/'DIAG-019/attempt-002';check(Q/'analyse.py',json.loads((Q/'analysis-freeze.json').read_text())['sha256'])
def interval(x):
 avg=statistics.mean(x);half=2.570581835636305*statistics.stdev(x)/math.sqrt(len(x));return dict(effects=x,mean=avg,low=avg-half,high=avg+half)
def compare(got,expected):
 global intervals
 assert got==expected,(got,expected);intervals+=1
allrows=0;AA=None
for phase in ['aa','discovery','confirm']:
 m=runs(Q/phase/'manifest.json');s=json.loads((Q/phase/'summary.json').read_text());assert m['status']=='complete' and len(m['runs'])==192;allrows+=len(m['runs']);loaded=[]
 for r in m['runs']:
  assert r['returncode']==0;v=next(csv.DictReader((R/r['stdout']).open()));assert int(v['operations'])==2000000 and int(v['hits'])==2000000 and int(v['elapsed_ns'])>=10000000;loaded.append((r,v))
 expected_cells=[tuple(x) for x in m['cells']];schedule=[]
 for block in range(1,7):
  offset=(block-1)%4
  for seed,qseed in (m['seeds'] if block%2 else m['seeds'][::-1]):
   for mode,batch in expected_cells[offset:]+expected_cells[:offset]:
    schedule.extend((block,seed,qseed,mode,batch,i,l) for i,l in enumerate('ABBA',1))
 assert [(r['block'],r['seed'],r['query_seed'],r['placement'],r['batch'],r['step'],r['label']) for r,_ in loaded]==schedule
 for z in s['results']:
  rs=[(r,v) for r,v in loaded if r['placement']==z['placement'] and r['batch']==z['batch'] and r['seed']==z['seed']]
  for key,field in [('elapsed_ns','wall_percent'),('thread_elapsed_ns','thread_percent')]:
   effects=[]
   for block in range(1,7):
    t=[int(v[key]) for r,v in rs if r['block']==block];assert len(t)==4;effects.append(100*((t[1]+t[2])/(t[0]+t[3])-1))
   compare(interval(effects),z[field])
 if phase=='aa':AA=s;assert s['joint_aa_qualifies']==all(z['wall_percent']['low']>=-1 and z['wall_percent']['high']<=1 for z in s['results'])
 else:
  for z in s['interactions']:
   c={(x['placement'],x['batch']):x['wall_percent']['effects'] for x in s['results'] if x['seed']==z['seed']};on=[a-b for a,b in zip(c['on',1],c['on',16])];off=[a-b for a,b in zip(c['off',1],c['off',16])];interaction=[a-b for a,b in zip(on,off)]
   for values,k in [(on,'on_batch_gap_points'),(off,'off_batch_gap_points'),(interaction,'interaction_points')]:compare(interval(values),z[k])
   assert not z['passes_interaction']
assert not AA['joint_aa_qualifies'] and not json.loads((Q/'decision.json').read_text())['supported']
# Boundary snapshots and full-output consistency, including failed initial build.
semantic_cells=0;faults=0
for Q in [P/'BOUNDARY-026',P/'BOUNDARY-026/attempt-002']:
 f=json.loads((Q/'freeze.json').read_text());B=R/f['snapshot'];check(Q/'PLAN.md',f['plan_sha256']);check(Q/'run.py',f['runner_sha256']);assert apply('',(Q/'oracle.patch').read_text())==(B/'control/tests/heterogeneous_batch_oracle.c').read_text();patches+=1
 for v,files in f['files'].items():
  for n,h in files.items():check(B/v/n,h)
 for phase in ['discovery','confirm','faults']:
  path=Q/phase/'manifest.json'
  if not path.exists():continue
  m=runs(path)
  for key,h in m.get('binaries',{}).items():
   v,build=key.split('-');check(B/v/'build'/f'{phase}-{build}',h)
  if m['status']=='failed':assert Q.name=='BOUNDARY-026';continue
  assert m['status']=='complete'
  if phase!='faults':
   assert len(m['results'])==16;semantic_cells+=16
   by={r['name']:r for r in m['runs']}
   for v in ['A','B','C']:
    for build in ['release','sanitize']:
     for seed in ([82603,82611] if phase=='discovery' else [82703,82711]):assert (R/by[f'{v}-{build}-{seed}']['stdout']).read_text()==(R/by[f'control-{build}-{seed}']['stdout']).read_text()
  else:
   for z in m['results']:
    assert z['detected'];faults+=1;old=(B/'C/src/zset_btree.c').read_text();assert apply(old,(Q/phase/(z['fault']+'.patch')).read_text())==(B/z['fault']/'src/zset_btree.c').read_text();patches+=1
# Scoped census: verify raw exported function/branch mapping against public summaries.
Q=P/'COUNTERS-011';m=runs(Q/'manifest.json');assert m['status']=='complete' and len(m['captures'])==16
for v,d in m['snapshots'].items():
 B=R/d['path']
 for n,h in d['files'].items():check(B/n,h)
 check(B/'build/census',d['binary_sha256']);old=(R/'scratch/overnight-diag-019-attempt2'/v/'bench/batch_lookup.c').read_text();assert apply(old,(Q/(v+'-scope.patch')).read_text())==(B/'bench/batch_lookup.c').read_text();patches+=1
for c in [m['calibration'],*m['captures']]:
 for k in ['raw','profdata','export']:check(R/c[k],c[k+'_sha256'])
 fs=[f for d in json.loads((R/c['export']).read_text())['data'] for f in d['functions']]
 if 'counts' not in c or isinstance(c['counts'],dict):
  counts={n:next(f for f in fs if f['name']==n)['count'] for n in ['known_before','known_scope','known_after']};assert counts==dict(known_before=0,known_scope=20,known_after=0);continue
 check(R/c['counts'],c['counts_sha256']);selected=json.loads((R/c['counts']).read_text());B=R/m['snapshots'][c['variant']]['path']
 for z in selected:
  f=next(f for f in fs if f['name']==z['name'] or f['name'].endswith(':'+z['name']));assert f['count']==z['count'] and len(f['branches'])==len(z['branches'])
  for b,pub in zip(f['branches'],z['branches']):
   file=Path(f['filenames'][b[6]]);assert pub['source']=='\n'.join(file.read_text().splitlines()[b[0]-1:b[2]]) and pub['true']==b[4] and pub['false']==b[5] and pub['file']==str(file.relative_to(B));branch_mappings+=1
assert json.loads((Q/'summary.json').read_text())['all_compared_logical_counts_equal']
# All recorded child commands, including builds/faults/symbolizers, are serial.
windows.sort()
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
result=dict(status='PASS',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),hashes_checked=checks,serial_command_windows=len(windows),timing_rows=allrows,raw_derived_intervals=intervals,sampled_profiles=profile_captures,sampler_calibrations=calibrations,scoped_counter_captures=16,scope_controls=1,raw_branch_mappings=branch_mappings,boundary_cells=semantic_cells,detected_lane_reuse_controls=faults,patch_reconstructions=patches,optimization_patches_preserved=15,source_selection='NONE',last_child_end=windows[-1][1].isoformat(),prior_shared_ledger_exclusions=sorted(mutable))
(P/'ROUND-019-VERIFY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
