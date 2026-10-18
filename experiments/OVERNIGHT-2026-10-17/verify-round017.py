from pathlib import Path
import ast,datetime,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
validated=0;windows=[];faults=[];failures=[];manifests=[];captures=[]
def same(p,h):
 global validated
 assert p.is_file(),str(p);assert sha(p)==h,str(p);validated+=1
def rowcheck(base,row,tag):
 out=R/row['stdout'] if 'stdout' in row else base/(tag+'.stdout');err=base/(tag+'.stderr')
 same(out,row['stdout_sha256']);same(err,row['stderr_sha256'])
 if 'raw_stderr' in row:
  raw=R/row['raw_stderr'];same(raw,row['raw_stderr_sha256']);assert raw.read_text().replace(str(R),'<workspace>')==err.read_text()
 a=datetime.datetime.fromisoformat(row['started_utc']);b=datetime.datetime.fromisoformat(row['ended_utc']);assert 0<=(b-a).total_seconds()<125
 windows.append((a,b,str(base.relative_to(R))+'/'+tag,row['returncode']))
 if row['returncode']!=0:failures.append(dict(name=windows[-1][2],returncode=row['returncode']))
 if tag.endswith('-capture'):captures.append(tag)
for root in [P/'BOUNDARY-024',P/'COUNTERS-010',P/'ROUND-017-CONFIRMATION']:
 for f in sorted(root.rglob('manifest.json')):
  d=json.loads(f.read_text());base=f.parent;manifests.append(str(f.relative_to(R)))
  if isinstance(d,list):
   for item in d:
    B=R/item['snapshot'];same(B/'src/zset_btree.c',item['source_sha256']);same(B/'build/fault',item['binary_sha256'])
    faults.append(dict(scope=str(base.relative_to(R)),name=item['name'],detected=item['detected'],outcome=item['outcome']))
    for row in item['runs']:rowcheck(base,row,item['name']+'-'+row['stage'])
    assert item['runs'][0]['returncode']==0
    rc=item['runs'][-1]['returncode'];stderr=(base/(item['name']+'-run.stderr')).read_text()
    assert item['detected']==(rc!=0 and any(x in stderr for x in ['live-score','AddressSanitizer','Assertion','src/zset_btree.c:']))
  else:
   assert d['status']=='complete';same(base/'PLAN.md',d['plan_sha256'])
   for v,desc in d.get('snapshots',{}).items():
    B=R/desc['path']
    for n,h in desc['files'].items():same(B/n,h)
    for n,h in desc.get('binaries',{}).items():same(B/'build'/n,h)
   for k,h in d.get('binaries',{}).items():
    v,kind=k.split('-');same(R/d['snapshots'][v]['path']/'build'/kind,h)
   for name,desc in d.get('cases',{}).items():
    B=R/desc['snapshot']
    for n,h in desc['files'].items():same(B/n,h)
    for n,k in [('build/census','binary_sha256'),('counts.profraw','raw_sha256'),('counts.profdata','profdata_sha256'),('export.json','export_sha256')]:same(B/n,desc[k])
    same(base/(name+'-counts.json'),desc['counts_sha256'])
   for row in d['runs']:rowcheck(base,row,row['name'])
windows.sort();assert all(a[1]<=b[0] for a,b in zip(windows,windows[1:]));assert len(windows)==286;assert len(captures)==4
mutable={'.workspace-memory/LIVE-STATUS.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/token-ledger.tsv','experiments/NEXT-STEPS.md'}
oldmanifest=P/'ROUND-016-SHA256.json';old=json.loads(oldmanifest.read_text());seal=json.loads((P/'ROUND-016-SEAL.json').read_text())
initial=dict(old);initial[seal['changed_file']]=seal['initial_sha256'];del initial[str((P/'ROUND-016-SEAL.json').relative_to(R))];del initial[str((P/'seal-round016.py').relative_to(R))];assert hashlib.sha256((json.dumps({str(k):initial[str(k)] for k in sorted(Path(k) for k in initial)},indent=2)+'\n').encode()).hexdigest()==seal['initial_manifest_sha256']
for n,h in old.items():
 if n in mutable:continue
 if n==seal['changed_file']:assert h==seal['closed_sha256']
 same(R/n,h)
for e in json.loads((R/'source-manifest.json').read_text())['files']:same(R/e['path'],e['sha256'])
counts={}
for base in [P/'COUNTERS-010',P/'COUNTERS-010/ties']:
 census=json.loads((base/'manifest.json').read_text());assert census['status']=='complete'
 for name,desc in census['cases'].items():
  B=R/desc['snapshot'];data=json.loads((B/'export.json').read_text());fs=[f for d in data['data'] for f in d['functions']]
  curated=json.loads((base/(name+'-counts.json')).read_text())
  for c in curated:
   f=next(f for f in fs if f['name']==c['name'] or f['name'].endswith(':'+c['name']));assert f['count']==c['count'];assert len(f['branches'])==len(c['branches'])
   for b,cb in zip(f['branches'],c['branches']):
    file=Path(f['filenames'][b[6]]);snippet='\n'.join(file.read_text().splitlines()[b[0]-1:b[2]])
    assert (b[0],b[1],b[2],b[3],b[4],b[5],str(file.relative_to(B)),snippet)==(cb['start_line'],cb['start_column'],cb['end_line'],cb['end_column'],cb['true'],cb['false'],cb['file'],cb['source'])
  def count(fn):return next(f['count'] for f in fs if f['name']==fn or f['name'].endswith(':'+fn))
  def branch(fn,line):
   f=next(f for f in fs if f['name']==fn or f['name'].endswith(':'+fn));bs=[b for b in f['branches'] if b[0]==line and Path(f['filenames'][b[6]]).name=='zset_btree.c'];assert len(bs)==1;return dict(true=bs[0][4],false=bs[0][5])
  reported=json.loads((base/'summary.json').read_text())['observations'][name]
  if name in ['inline','external']:
   actual=dict(updates=count('zbtreeUpdateScore'),inplace=branch('zbtreeUpdateScore',3655),external=branch('zbtreeUpdateScore',3668),cross_leaf=branch('zbtreeUpdateScore',3681),detach=count('zbtBuildElementDetach'),copied_target=branch('zbtIndexMove',2379),new_vs_old_source=branch('zbtIndexMove',2382))
  else:
   actual=dict(updates=count('zbtreeUpdateScore'),lower_reject=branch('zbtScoreUpdateInPlace',3561),upper_reject=branch('zbtScoreUpdateInPlace',3574))
  assert actual==reported,(name,actual,reported);counts[name]=actual
matrices=[]
for rel,cells in [('BOUNDARY-024',16),('BOUNDARY-024/external-extension',16),('BOUNDARY-024/finite-ties',16),('BOUNDARY-024/tie-neighbors',16),('ROUND-017-CONFIRMATION',64),('BOUNDARY-024/batch-promotion',8),('BOUNDARY-024/batch-promotion/confirmation',8),('BOUNDARY-024/batch-promotion/attempt-002',8),('BOUNDARY-024/batch-promotion/attempt-002/confirmation',8)]:
 base=P/rel;d=json.loads((base/'manifest.json').read_text());rows=[r for r in d['runs'] if r['stage']!='build'];assert len(rows)==cells;group={}
 for row in rows:
  txt=(base/(row['name']+'.stdout')).read_text();line=next(s for s in txt.splitlines() if s.startswith('PASS '));v=dict(re.findall(r'(\w+)=([^ ]+)',line));assert int(v['checks'])==6 and int(v['active'])>0;assert (base/(row['name']+'.stderr')).stat().st_size==0
  group.setdefault(row.get('case','single')+'/'+row['stage'],[]).append(v['digest'])
  assert 'MIXED seed=' in txt and 'WIDE seed=' in txt
  live=dict(re.findall(r'(\w+)=([^ ]+)',next(s for s in txt.splitlines() if s.startswith('LIVE '))))
  assert int(live['old_new'])>0 and int(live['new_old'])>0 and int(live['zeros'])==2 and int(live['calls'])<=int(live['max_groups'])+1
  scope=row.get('case',rel)
  if 'external' in scope or 'batch-promotion' in scope:
   ext=dict(re.findall(r'(\w+)=([^ ]+)',next(s for s in txt.splitlines() if s.startswith('EXTERNAL '))));assert int(ext['transfers'])==260 and int(ext['buffers'])==(int(v['final'])-1)//127+3
  if 'batch-promotion' in scope:
   batch=dict(re.findall(r'(\w+)=([^ ]+)',next(s for s in txt.splitlines() if s.startswith('BATCHES '))));assert int(batch['promotions'])==1 and int(batch['active'])>0 and 'lanes=16 mask=7777' in txt
  if 'finite' in scope:assert 'checks=288\n' in txt
  if 'neighbor' in scope:
   assert 'checks=336\n' in txt
   for ident in ['256','511']:
    move=next(dict(re.findall(r'(\w+)=([^ ]+)',line)) for line in txt.splitlines() if line.startswith('MOVE ') and 'id='+ident+' ' in line);assert move['old']==move['new']
 for ds in group.values():assert len(ds)==8 and len(set(ds))==1
 matrices.append(dict(scope=rel,cells=cells,full_sorted_models_per_cell=6,groups=len(group)))
assert len(faults)==7 and sum(x['detected'] for x in faults)==6
assert len(failures)==6 and all(x['returncode']!=0 for x in failures)
assert next(x for x in faults if '/finite-ties/' in x['scope'])['outcome']=='SURVIVED'
# Reconstruct patches without git metadata writes.
tree=ast.parse((P/'verify-round016.py').read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='apply_unified');scope={'re':re};exec(compile(ast.Module(body=[fn],type_ignores=[]),'<patch-auditor>','exec'),scope);apply_unified=scope['apply_unified']
patches=0
for patch in (P/'BOUNDARY-024').rglob('oracle.patch'):
 d=json.loads((patch.parent/'manifest.json').read_text());B=R/d['snapshots']['control']['path'];dest=patch.read_text().splitlines()[1][6:];assert apply_unified('',patch.read_text())==(B/dest).read_text();patches+=1
for mf in (P/'BOUNDARY-024').rglob('faults/manifest.json'):
 d=json.loads((mf.parent.parent/'manifest.json').read_text());original=(R/d['snapshots']['control']['path']/'src/zset_btree.c').read_text()
 for f in json.loads(mf.read_text()):assert apply_unified(original,(mf.parent/(f['name']+'.patch')).read_text())==(R/f['snapshot']/'src/zset_btree.c').read_text();patches+=1
assert patches==15
# Only the documented lane expression changed between retained and final batch recipes.
batch=P/'BOUNDARY-024/batch-promotion';initial=json.loads((batch/'manifest.json').read_text());final=json.loads((batch/'attempt-002/manifest.json').read_text());fresh=json.loads((batch/'attempt-002/confirmation/manifest.json').read_text())
name='tests/live_widen_batch_score_oracle.c';old=(R/initial['snapshots']['control']['path']/name).read_text();new=(R/final['snapshots']['control']['path']/name).read_text();assert old.replace('1+i%2','1+(i/4)%2')==new;assert old!=new;assert (R/name).read_text()==new
for v in ['control','A','B','C']:assert final['snapshots'][v]['files'][name]==fresh['snapshots'][v]['files'][name]
checks=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check']),('compiler',['cc','--version']),('arch',['uname','-m'])]:
 out=P/('ROUND-017-'+name+'.stdout');err=P/('ROUND-017-'+name+'.stderr');assert not out.exists();row=dict(name=name,command=cmd,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 row.update(returncode=rc,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),stdout_sha256=sha(out),stderr_sha256=sha(err));checks.append(row);assert rc==0
result=dict(status='pass',validated_hashes=validated,reconstructed_patches=patches,serial_command_windows=len(windows),whole_oracle_count_captures=len(captures),timing_benchmarks=0,manifests=manifests,matrices=matrices,semantic_cells=160,fresh_confirmation_cells=80,retained_failures=failures,faults=faults,fault_detections=6,fault_survivors=1,new_distinct_fault_types=5,raw_recomputed_counts=counts,checks=checks,backend='unknown',model='unknown',token_cost='unknown',review='sequential; reviewer startup failed')
(P/'ROUND-017-VERIFY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','validated_hashes','reconstructed_patches','serial_command_windows','whole_oracle_count_captures','semantic_cells','fresh_confirmation_cells']},indent=2))
