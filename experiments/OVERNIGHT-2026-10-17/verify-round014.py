from pathlib import Path
import datetime,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
windows=[];validated_files=0;manifests=[];failed=[];profile_windows=[]
def same(path,want):
 global validated_files
 assert path.is_file(),str(path);assert sha(path)==want,str(path);validated_files+=1
def rowcheck(base,row,tag):
 if 'stdout' in row:out=R/row['stdout']
 else:out=base/(tag+'.stdout')
 err=base/(tag+'.stderr');same(out,row['stdout_sha256']);same(err,row['stderr_sha256'])
 a=datetime.datetime.fromisoformat(row['started_utc']);b=datetime.datetime.fromisoformat(row['ended_utc']);assert b>=a
 windows.append((a,b,str(base.relative_to(R))+'/'+tag,row['returncode']))
 if row['returncode']!=0:failed.append(dict(name=windows[-1][2],returncode=row['returncode']))
 if tag.endswith('-capture'):profile_windows.append((a,b,tag))
roots=[P/'BOUNDARY-019',P/'BOUNDARY-020',P/'BOUNDARY-021',P/'COUNTERS-007']
for root in roots:
 for f in sorted(root.rglob('manifest.json')):
  d=json.loads(f.read_text());manifests.append(str(f.relative_to(R)));base=f.parent
  if isinstance(d,list):
   for item in d:
    if 'runs' in item:
     B=R/item['snapshot'];same(B/'src/zset_btree.c',item['source_sha256']);same(B/'build/fault',item['binary_sha256']);assert item['detected']
     for row in item['runs']:rowcheck(base,row,item['name']+'-'+row['stage'])
    else:rowcheck(base,item,item['name'])
  else:
   for v,desc in d.get('snapshots',{}).items():
    B=R/desc['path']
    for n,h in desc['files'].items():same(B/n,h)
   for key,h in d.get('binaries',{}).items():
    v,kind=key.split('-');same(R/d['snapshots'][v]['path']/'build'/kind,h)
   if 'cases' in d:
    for name,desc in d['cases'].items():
     B=R/desc['snapshot']
     for n,h in desc['files'].items():same(B/n,h)
     same(B/'build/census',desc['binary_sha256']);same(B/'counts.profraw',desc['raw_sha256']);same(B/'counts.profdata',desc['profdata_sha256']);same(B/'export.json',desc['export_sha256'])
   for row in d['runs']:rowcheck(base,row,row['name'])
windows.sort();assert all(a[1]<=b[0] for a,b in zip(windows,windows[1:])),[(a[2],b[2]) for a,b in zip(windows,windows[1:]) if a[1]>b[0]]
assert len(profile_windows)==4
# Original source/support and all old evidence remain unchanged except shared ledgers.
old=json.loads((P/'ROUND-013-SHA256.json').read_text());mutable={'.workspace-memory/LIVE-STATUS.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/token-ledger.tsv'}
for n,h in old.items():
 if n not in mutable:same(R/n,h)
source=json.loads((R/'source-manifest.json').read_text())
for e in source['files']:same(R/e['path'],e['sha256'])
# Recompute semantic PASS summaries directly from retained stdout; no reruns.
matrices=[('BOUNDARY-019/attempt-002',8,4,32,293132),('BOUNDARY-020',8,4,32,284714),('BOUNDARY-020/mutation-extension/attempt-002',8,8,448,15054526),('BOUNDARY-019/shrink-extension',8,4,88,574384),('BOUNDARY-021',2,2,274,10960)]
models=[]
for rel,cells,fixtures,checks,results in matrices:
 base=P/rel;d=json.loads((base/'manifest.json').read_text());assert d['status']=='complete';runs=[r for r in d['runs'] if r['stage']=='run'];assert len(runs)==cells
 outputs=[]
 for row in runs:
  txt=(base/(row['name']+'.stdout')).read_text();outputs.append(txt)
  line=next(s for s in txt.splitlines() if s.startswith('PASS '));fields=dict(re.findall(r'(\w+)=([^ ]+)',line))
  assert (int(fields['fixtures']),int(fields['checks']),int(fields['results']))==(fixtures,checks,results)
 assert len(set(outputs))==1
 models.append(dict(matrix=rel,cells=cells,fixtures_per_cell=fixtures,checks_per_cell=checks,results_per_cell=results,identical_outputs=True))
# Every original test cell reports43passed, no failure.
base=P/'BOUNDARY-019/original-tests';orig=json.loads((base/'manifest.json').read_text());oruns=[r for r in orig if r['name'].endswith('-run')];assert len(oruns)==8
for row in oruns:
 txt=re.sub(r'\x1b\[[0-9;]*m','',(base/(row['name']+'.stdout')).read_text());assert '43 passed, 0 failed, 43 total' in txt
# Independent raw LLVM branch extraction, using file IDs rather than misleading initial snippets.
observations={}
for rel in ['COUNTERS-007','COUNTERS-007/shrink-extension']:
 base=P/rel;d=json.loads((base/'manifest.json').read_text());summary=json.loads((base/'summary.json').read_text())['observations']
 for name,desc in d['cases'].items():
  data=json.loads((R/desc['snapshot']/'export.json').read_text());fs=[f for group in data['data'] for f in group['functions']]
  def value(fn,line,col):
   f=next(f for f in fs if f['name']==fn or f['name'].endswith(':'+fn));bs=[b for b in f['branches'] if b[0]==line and b[1]==col];assert len(bs)==1;return bs[0][4]
  got=dict(member_cursor_repair=value('zbtScoreRemoveLeaf',1114,9),reuse_after_free=value('zbtScoreRegisterLeaf',803,39),freed_member_cursor=value('zbtIndexRehashStep',203,34),member_cursor_fallback=value('zbtIndexRehashStep',2121,13),retired_defrag_cursor=value('zbtreeDefragStep',3143,13),defrag_tree_reset=value('zbtreeDefragStep',3133,9))
  for k,v in got.items():assert summary[name][k]==v
  observations[name]=got
assert observations['shrink']['member_cursor_fallback']==8 and all(d['freed_member_cursor']==0 for d in observations.values())
# Keep initial failures; they do not count as successful cells or measured samples.
assert len(failed)==10,failed # two initial oracle failures plus eight deliberate fault runs
checks=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check'])]:
 out=P/('ROUND-014-'+name+'.stdout');err=P/('ROUND-014-'+name+'.stderr');start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 checks.append(dict(name=name,command=cmd,started_utc=start,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=rc,stdout_sha256=sha(out),stderr_sha256=sha(err)));assert rc==0
result=dict(status='pass',validated_file_hashes=validated_files,manifests=manifests,serial_command_windows=len(windows),profile_captures=len(profile_windows),timing_benchmark_windows=0,retained_nonzero_exits=failed,matrices=models,original_test_cells=8,original_tests_per_cell=43,raw_recomputed_branches=observations,checks=checks,backend='unknown',model='unknown',token_cost='unknown',review='sequential; independent reviewer startup failed')
(P/'ROUND-014-VERIFY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k in ['status','validated_file_hashes','serial_command_windows','profile_captures','timing_benchmark_windows','original_test_cells']},indent=2))
