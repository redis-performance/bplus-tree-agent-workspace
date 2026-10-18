from pathlib import Path
import ast,collections,datetime,hashlib,json,re
P=Path(__file__).resolve().parent;R=P.parents[1];E=R/'experiments/EXP-006';checks=0;windows=[];patches=0
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def check(p,h):
 global checks
 assert sha(p)==h,str(p.relative_to(R));checks+=1
T=ast.parse((P/'verify-round016.py').read_text());fun=next(n for n in T.body if isinstance(n,ast.FunctionDef) and n.name=='apply_unified');scope={'re':re};exec(compile(ast.Module(body=[fun],type_ignores=[]),'<prior-unified-patch-reader>','exec'),scope);apply=scope['apply_unified']
mutable={'.workspace-memory/LIVE-STATUS.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md'}
for n,h in json.loads((P/'ROUND-019-SHA256.json').read_text()).items():
 if n not in mutable:check(R/n,h)
for num in range(2,7):
 D=R/f'experiments/EXP-{num:03d}';f=json.loads((D/'freeze.json').read_text());base=R/f['snapshot_root'];old=(base/'control/src/zset_btree.c').read_text()
 for v,files in f['files'].items():
  for n,h in files.items():check(base/v/n,h)
 for v in ['A','B','C']:
  assert apply(old,(D/'variants'/v/'candidate.patch').read_text())==(base/v/'src/zset_btree.c').read_text();patches+=1
 assert (R/'src/zset_btree.c').read_text()==old

def commands(Q,rs):
 for r in rs:
  assert isinstance(r['returncode'],int)
  windows.append((datetime.datetime.fromisoformat(r['started_utc']),datetime.datetime.fromisoformat(r['ended_utc']),str(Q.relative_to(R)),r.get('name',r.get('stage'))))
  for k in ['stdout','stderr']:
   path=R/r[k] if k in r else Q/(r['name']+'.'+k)
   check(path,r[k+'_sha256'])
  if 'raw_stderr' in r:check(R/r['raw_stderr'],r['raw_stderr_sha256'])
def snapshots(m):
 for d in m['snapshots'].values():
  for n,h in d['files'].items():check(R/d['path']/n,h)
 for n,h in m.get('binaries',{}).items():check(R/n,h)

def fields(s):return dict(re.findall(r'(\w+)=([^\s]+)',s))
summary={}
Q=E/'cross-boundary-round020';m=json.loads((Q/'manifest.json').read_text());assert m['status']=='complete' and len(m['runs'])==128
check(Q/'PLAN.md',m['plan_sha256']);check(Q/'run.py',m['driver_sha256']);snapshots(m);commands(Q,m['runs'])
for n,h in m['root_hashes'].items():check(R/n,h)
expected=[]
for phase,seed,debug in [('discovery',92503,True),('confirmation',92521,False)]:
 for v in ['control','A','B','C']:
  for kind in ['native','sanitize']:
   for oracle in ['partial-promotion','narrowing','external-relocation']:
    expected.append((phase,seed,debug,v,kind,oracle,'build',None))
    for mode in ([0,1,2] if oracle=='external-relocation' else [None]):expected.append((phase,seed,debug,v,kind,oracle,'run',mode))
assert [(r['phase'],r['seed'],r['debug'],r['variant'],r['kind'],r['oracle'],r['stage'],r['mode']) for r in m['runs']]==expected
assert all(r['returncode']==0 for r in m['runs'])
groups=collections.defaultdict(list)
for r in m['runs']:
 if r['stage']=='run':
  lines=(Q/(r['name']+'.stdout')).read_text().splitlines();assert lines[-1].startswith('PASS ');groups[(r['seed'],r['oracle'],r['mode'])].append(fields(lines[-1]))
for key,rows in groups.items():assert len(rows)==8 and len({r['digest'] for r in rows})==1
summary['cross_boundary']=dict(semantic_cells=80,builds=48,groups=[dict(seed=k[0],oracle=k[1],mode=k[2],cells=len(rows),reported=rows[0],complete_fields_equal=all(r==rows[0] for r in rows)) for k,rows in groups.items()])
D=Q/'faults';f=json.loads((D/'manifest.json').read_text());assert f['status']=='complete' and len(f['runs'])==5;check(Q/'FAULT-PLAN.md',f['plan_sha256']);check(Q/'faults.py',f['driver_sha256']);check(Q/'manifest.json',f['parent_manifest_sha256'])
for x in f['runs']:
 for n,h in x['files'].items():check(R/x['path']/n,h)
 check(R/x['path']/'build/fault',x['binary_sha256']);check(D/(x['name']+'.patch'),x['patch_sha256'])
 assert apply((R/m['snapshots']['C']['path']/'src/zset_btree.c').read_text(),(D/(x['name']+'.patch')).read_text())==(R/x['path']/'src/zset_btree.c').read_text();patches+=1
 rs=[]
 for r in x['commands']:rs.append(dict(r,name=x['name']+'-'+r['stage']))
 commands(D,rs);assert x['commands'][0]['returncode']==0 and x['outcome']=='detected'
summary['transferred_faults']={x['name']:x['outcome'] for x in f['runs']}
Q=E/'scalar-fallback-round020';m=json.loads((Q/'manifest.json').read_text());assert m['status']=='complete';check(Q/'PLAN.md',m['plan_sha256']);check(Q/'run.py',m['driver_sha256']);snapshots(m);commands(Q,m['runs']);assert len(m['preprocessing'])==8 and m['fault_outcome']=='detected'
assert len(m['runs'])==50
for v in ['control','A','B','C']:
 for oracle in ['tag_search_oracle.c','tag_guard_oracle.c']:
  rs=[r for r in m['runs'] if r['name'].startswith(v+'-'+oracle+'-preprocess-')];assert len(rs)==2
  output=[(R/r['stdout']).read_text() for r in rs]
  if v in ['B','C']:
   pat=r'static inline uint8_t \*zbtInlineTagSearch\([^\n]+\{.*?\n\}';h=[re.search(pat,s,re.S).group(0) for s in output]
   assert output[0].replace(h[0],'HELPER')==output[1].replace(h[1],'HELPER');assert 'while (n--)' in h[1] and all(x not in h[1] for x in ['memcpy','matches','ctz'])
  else:assert output[0]==output[1]
for oracle,count in [('tag_search_oracle.c',1585152),('tag_guard_oracle.c',198144)]:
 rs=[r for r in m['runs'] if r['name'].endswith(oracle+'-run')];assert len(rs)==8 and all(r['returncode']==0 for r in rs)
 outs={(R/r['stdout']).read_text() for r in rs};assert len(outs)==1 and str(count) in next(iter(outs))
old=(R/m['snapshots']['C']['path']/'src/zset_btree.c').read_text();assert apply(old,(Q/'zero-span-read.patch').read_text())==(R/m['snapshots']['fault']['path']/'src/zset_btree.c').read_text();patches+=1
summary['scalar_fallback']=dict(semantic_cells=16,builds=16,preprocess_commands=16,fault='detected',actual_big_endian_tested=False)
Q=E/'dense-promotion-round020';m=json.loads((Q/'manifest.json').read_text());assert m['status']=='complete';check(Q/'PLAN.md',m['plan_sha256']);check(Q/'run.py',m['driver_sha256']);check(Q/'dense_promotion_oracle.c',m['oracle_sha256']);check(Q/'oracle.patch',m['patch_sha256']);check(R/m['parent_oracle'],m['parent_oracle_sha256']);snapshots(m);commands(Q,m['runs']);assert len(m['runs'])==16 and all(r['returncode']==0 for r in m['runs'])
assert apply((R/m['parent_oracle']).read_text(),(Q/'oracle.patch').read_text())==(Q/'dense_promotion_oracle.c').read_text();patches+=1
groups=collections.defaultdict(list)
for r in m['runs']:
 if r['stage']=='run':
  lines=(Q/(r['name']+'.stdout')).read_text().splitlines();matrix=[fields(l) for l in lines if l.startswith('MATRIX ')];assert len(matrix)==36 and matrix[-1]['dense_hits']=='68'
  assert {(x['family'],int(x['lanes']),x['mode']) for x in matrix}=={(str(f),c,str(mode)) for f in range(2) for c in [1,2,3,7,15,16] for mode in range(3)}
  assert lines[-1].startswith('PASS ');groups[r['seed']].append(fields(lines[-1]))
for seed,rows in groups.items():assert len(rows)==4 and len({r['digest'] for r in rows})==1
summary['dense_promotion']=dict(semantic_cells=8,builds=8,groups={seed:rows[0] for seed,rows in groups.items()},matrix_cases_per_cell=36,dense_hit_leaf_checks_per_cell=68)
Q=E/'generation-wrap-round020';m=json.loads((Q/'manifest.json').read_text());assert m['status']=='complete';check(Q/'PLAN.md',m['plan_sha256']);check(Q/'run.py',m['driver_sha256']);check(Q/'batch_generation_oracle.c',m['oracle_sha256']);check(Q/'oracle.patch',m['patch_sha256']);check(R/m['parent']['oracle'],m['parent']['oracle_sha256']);check(R/m['parent']['manifest'],m['parent']['manifest_sha256']);snapshots(m);commands(Q,m['runs']);assert len(m['runs'])==16 and all(r['returncode']==0 for r in m['runs'])
assert apply((R/m['parent']['oracle']).read_text(),(Q/'oracle.patch').read_text())==(Q/'batch_generation_oracle.c').read_text();patches+=1
wrap_outputs=[]
for row in m['runs']:
 if row['stage']=='run':
  lines=(Q/(row['name']+'.stdout')).read_text().splitlines();result=fields(lines[-1]);assert result['fixtures']=='4' and result['checks']=='262188' and result['results']=='24254190' and result['resizes']=='262160' and result['wraps']=='4'
  wraps=[fields(l) for l in lines if l.startswith('WRAP ')];fixtures=[fields(l) for l in lines if l.startswith('FIXTURE ')];assert len(wraps)==4 and len(fixtures)==4
  assert {(int(x['seed']),int(x['batch'])) for x in wraps}=={(s,b) for s in [94503,94521] for b in [2,13]};assert all(x['from']=='65535' and x['to']=='1' for x in wraps)
  wrap_outputs.append(result)
assert len(wrap_outputs)==8 and all(x==wrap_outputs[0] for x in wrap_outputs)
summary['generation_wrap']=dict(semantic_cells=8,builds=8,reported=wrap_outputs[0],fresh_seeds=[94503,94521],debug_enabled=True)
static=json.loads((P/'ROUND-020-STATIC-LEAF-AUDIT.json').read_text());assert static['status']=='PASS'
for row in static['rows']:
 check(R/row['input'],row['input_sha256']);check(R/row['full_assembly'],row['full_assembly_sha256'])
 assert len(row['stack_accesses'])==row['static_stack_load_sites']+row['static_stack_store_sites']
summary['static_inventory']='four already frozen compiler leaf bodies; descriptive only'
checkpoint=json.loads((P/'ROUND-020-CHECKPOINT-INDEX.json').read_text());oldseal=json.loads((P/'ROUND-020-CHECKPOINT-SHA256.json').read_text());assert set(checkpoint['files'])==set(oldseal)
for n,row in checkpoint['files'].items():
 assert row['sha256']==oldseal[n];check(R/row['snapshot'],row['sha256'])
summary['preserved_checkpoint_files']=len(checkpoint['files'])
windows.sort()
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
summary.update(status='PASS',hash_checks=checks,serial_command_windows=len(windows),patch_reconstructions=patches,started_utc=windows[0][0].isoformat(),ended_utc=windows[-1][1].isoformat(),source_adoption='NONE',optimization_decision='C/PARK unchanged',performance_claim=False)
(P/'ROUND-020-VERIFY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:summary[k] for k in ['status','hash_checks','serial_command_windows','patch_reconstructions','ended_utc']}))
