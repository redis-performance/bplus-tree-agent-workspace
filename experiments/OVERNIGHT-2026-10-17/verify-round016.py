from pathlib import Path
import datetime,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
windows=[];validated=0;faults=[];failures=[];captures=[];manifests=[]
def same(p,h):
 global validated
 assert p.is_file(),str(p);assert sha(p)==h,str(p);validated+=1
def rowcheck(base,row,tag):
 out=R/row['stdout'] if 'stdout' in row else base/(tag+'.stdout');err=base/(tag+'.stderr');same(out,row['stdout_sha256']);same(err,row['stderr_sha256'])
 if 'raw_stderr' in row:
  raw=R/row['raw_stderr'];same(raw,row['raw_stderr_sha256']);assert raw.read_text().replace(str(R),'<workspace>')==err.read_text()
 a=datetime.datetime.fromisoformat(row['started_utc']);b=datetime.datetime.fromisoformat(row['ended_utc']);assert b>=a;assert (b-a).total_seconds()<125
 windows.append((a,b,str(base.relative_to(R))+'/'+tag,row['returncode']))
 if row['returncode']!=0:failures.append(dict(name=windows[-1][2],returncode=row['returncode']))
 if tag.endswith('-capture'):captures.append((a,b,tag))
roots=[P/'BOUNDARY-023',P/'COUNTERS-009',P/'ROUND-016-CONFIRMATION']
for root in roots:
 for f in sorted(root.rglob('manifest.json')):
  d=json.loads(f.read_text());base=f.parent;manifests.append(str(f.relative_to(R)))
  if isinstance(d,list):
   for item in d:
    B=R/item['snapshot'];same(B/'src/zset_btree.c',item['source_sha256']);same(B/'build/fault',item['binary_sha256']);faults.append(dict(scope=str(base.relative_to(R)),name=item['name'],detected=item['detected'],outcome=item['outcome']))
    for row in item['runs']:rowcheck(base,row,item['name']+'-'+row['stage'])
  else:
   same(base/'PLAN.md',d['plan_sha256'])
   for v,desc in d.get('snapshots',{}).items():
    B=R/desc['path']
    for n,h in desc['files'].items():same(B/n,h)
    for n,h in desc.get('binaries',{}).items():same(B/'build'/n,h)
   for key,h in d.get('binaries',{}).items():
    v,kind=key.split('-');same(R/d['snapshots'][v]['path']/'build'/kind,h)
   for name,desc in d.get('cases',{}).items():
    B=R/desc['snapshot']
    for n,h in desc['files'].items():same(B/n,h)
    for n,k in [('build/census','binary_sha256'),('counts.profraw','raw_sha256'),('counts.profdata','profdata_sha256'),('export.json','export_sha256')]:same(B/n,desc[k])
    same(base/(name+'-counts.json'),desc['counts_sha256'])
   for row in d['runs']:rowcheck(base,row,row['name'])
windows.sort();assert all(a[1]<=b[0] for a,b in zip(windows,windows[1:])),[(a[2],b[2]) for a,b in zip(windows,windows[1:]) if a[1]>b[0]]
assert len(captures)==6
mutable={'.workspace-memory/LIVE-STATUS.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/token-ledger.tsv','experiments/NEXT-STEPS.md'}
old=json.loads((P/'ROUND-015-SHA256.json').read_text())
for n,h in old.items():
 if n not in mutable:same(R/n,h)
for e in json.loads((R/'source-manifest.json').read_text())['files']:same(R/e['path'],e['sha256'])
counts={}
for base in [P/'COUNTERS-009',P/'COUNTERS-009/extensions']:
 census=json.loads((base/'manifest.json').read_text());assert census['status']=='complete'
 for name,desc in census['cases'].items():
  B=R/desc['snapshot'];data=json.loads((B/'export.json').read_text());fs=[f for d in data['data'] for f in d['functions']];curated=json.loads((base/(name+'-counts.json')).read_text())
  for c in curated:
   f=next(f for f in fs if f['name']==c['name'] or f['name'].endswith(':'+c['name']));assert f['count']==c['count'];assert len(f['branches'])==len(c['branches'])
   for b,cb in zip(f['branches'],c['branches']):
    file=Path(f['filenames'][b[6]]);snippet='\n'.join(file.read_text().splitlines()[b[0]-1:b[2]])
    assert (b[0],b[1],b[2],b[3],b[4],b[5],str(file.relative_to(B)),snippet)==(cb['start_line'],cb['start_column'],cb['end_line'],cb['end_column'],cb['true'],cb['false'],cb['file'],cb['source'])
  def value(fn,line,col):
   f=next(f for f in fs if f['name']==fn or f['name'].endswith(':'+fn));bs=[b for b in f['branches'] if b[0]==line and b[1]==col and Path(f['filenames'][b[6]]).name=='zset_btree.c'];assert len(bs)==1;return dict(true=bs[0][4],false=bs[0][5])
  reported=json.loads((base/'summary.json').read_text())['observations'][name]
  if name in ['base','mode0','mode1','mode2']:
   actual={label:value(fn,line,col) for label,fn,line,col in [('narrow_wide_read','zbtIndexGetId',1775,9),('resize_finish','zbtIndexRehashStep',2123,13),('active_scan','zbtreeScan',4335,9),('active_clone','zbtreeDup',2901,9),('active_defrag_start','zbtreeDefragStart',3027,9),('declined_plain','zbtDefragPlainAllocation',3004,9),('declined_node','zbtDefragScoreNode',3052,9),('leaf_move','zbtDefragScoreNode',3061,9)]}
  elif name=='external':
   f=next(f for f in fs if f['name'].endswith(':zbtDefragExternalMember') or f['name']=='zbtDefragExternalMember');v=value('zbtDefragExternalMember',3089,9);actual=dict(external_calls=f['count'],accepted=v['true'],declined=v['false'])
  else:
   actual={label:next(f['count'] for f in fs if f['name']==fn or f['name'].endswith(':'+fn)) for label,fn in [('renumber','zbtScoreRenumberLeaves'),('rebuild','zbtIndexRebuild')]}
  assert all(reported[k]==v for k,v in actual.items());counts[name]=actual
matrices=[]
for rel,cells in [('BOUNDARY-023',16),('BOUNDARY-023/relocation-extension',48),('BOUNDARY-023/external-extension',48),('BOUNDARY-023/narrowing-extension/attempt-002',16),('ROUND-016-CONFIRMATION',64)]:
 base=P/rel;d=json.loads((base/'manifest.json').read_text());assert d['status']=='complete';rows=[r for r in d['runs'] if r['stage']!='build'];assert len(rows)==cells;group={}
 for row in rows:
  txt=(base/(row['name']+'.stdout')).read_text();line=next(s for s in txt.splitlines() if s.startswith('PASS '));v=dict(re.findall(r'(\w+)=([^ ]+)',line));assert int(v['checks'])==3 and int(v['active'])>0;assert (base/(row['name']+'.stderr')).stat().st_size==0
  group.setdefault(row.get('case','single')+'/'+row['stage'],[]).append(v['digest'])
  assert 'MIXED seed=' in txt and 'WIDE seed=' in txt
  if 'narrow' in row.get('case',rel).lower():assert 'NARROW seed=' in txt and int(v['final'])==4096
 for ds in group.values():assert len(ds)==8 and len(set(ds))==1
 matrices.append(dict(scope=rel,cells=cells,full_models_per_cell=3,groups=len(group)))
assert len(faults)==6
assert sum(x['detected'] for x in faults)==5 # one original matcher error, corrected below without rerun
review=json.loads((P/'BOUNDARY-023/faults/audit.json').read_text());assert review['status']=='pass'
assert all(x['audited_outcome']=='detected' for x in review['results'])
assert len(failures)==7 # six deliberate fault runs and one compile-only error
# Patch reconstruction; no git metadata writes.
def apply_unified(original,patch):
 src=original.splitlines(True);lines=patch.splitlines(True);out=[];at=0;i=2
 assert lines[0].startswith('--- ') and lines[1].startswith('+++ ')
 while i<len(lines):
  m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i]);assert m,lines[i]
  target=int(m[1])-1 if int(m[1]) else 0;assert target>=at;out.extend(src[at:target]);at=target;i+=1;consumed=produced=0
  while i<len(lines) and not lines[i].startswith('@@ '):
   line=lines[i];i+=1;op=line[0];body=line[1:];assert op in ' +-'
   if op in ' -':assert src[at]==body;at+=1;consumed+=1
   if op in ' +':out.append(body);produced+=1
  assert consumed==int(m[2] or 1) and produced==int(m[4] or 1)
 out.extend(src[at:]);return ''.join(out)
patches_checked=0
for patch in (P/'BOUNDARY-023').rglob('oracle.patch'):
 d=json.loads((patch.parent/'manifest.json').read_text());B=R/d['snapshots']['control']['path'];dest=patch.read_text().splitlines()[1][6:];assert apply_unified('',patch.read_text())==(B/dest).read_text();patches_checked+=1
for mf in (P/'BOUNDARY-023').rglob('faults/manifest.json'):
 parent=json.loads((mf.parent.parent/'manifest.json').read_text());source=(R/parent['snapshots']['control']['path']/'src/zset_btree.c').read_text()
 for f in json.loads(mf.read_text()):assert apply_unified(source,(mf.parent/(f['name']+'.patch')).read_text())==(R/f['snapshot']/'src/zset_btree.c').read_text();patches_checked+=1
assert patches_checked==11
# Explicitly check the compiler-only correction changed no condition.
parent=P/'BOUNDARY-023/narrowing-extension';a=json.loads((parent/'manifest.json').read_text());b=json.loads((parent/'attempt-002/manifest.json').read_text());old=(R/a['snapshots']['control']['path']/'tests/live_widen_narrow_oracle.c').read_text();new=(R/b['snapshots']['control']['path']/'tests/live_widen_narrow_oracle.c').read_text();assert old.replace('survivor_id=anchor_it.leaf->id','survivor_id=((zbtScoreLeaf*)anchor_it.leaf)->id')==new
checks=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check']),('compiler',['cc','--version']),('arch',['uname','-m'])]:
 out=P/('ROUND-016-audit2-'+name+'.stdout');err=P/('ROUND-016-audit2-'+name+'.stderr');assert not out.exists();row=dict(name=name,command=cmd,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 row.update(returncode=rc,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),stdout_sha256=sha(out),stderr_sha256=sha(err));checks.append(row);assert rc==0
result=dict(status='pass',validated_hashes=validated,reconstructed_patches=patches_checked,serial_command_windows=len(windows),whole_oracle_count_captures=len(captures),timing_benchmarks=0,manifests=manifests,matrices=matrices,semantic_cells=192,fresh_confirmation_cells=64,retained_failures=failures,faults=faults,audited_fault_detections=6,new_distinct_fault_types=3,raw_recomputed_counts=counts,checks=checks,backend='unknown',model='unknown',token_cost='unknown',review='sequential; reviewer startup failed')
(P/'ROUND-016-VERIFY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','validated_hashes','reconstructed_patches','serial_command_windows','whole_oracle_count_captures','semantic_cells','fresh_confirmation_cells']},indent=2))
