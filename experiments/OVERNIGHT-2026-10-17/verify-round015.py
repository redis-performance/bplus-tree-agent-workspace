from pathlib import Path
import datetime,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
windows=[];validated=0;faults=[];failures=[];profiles=[];manifests=[];failed_binaries={}
def same(p,h):
 global validated
 assert p.is_file(),str(p);assert sha(p)==h,str(p);validated+=1
def rowcheck(base,row,tag):
 out=R/row['stdout'] if 'stdout' in row else base/(tag+'.stdout');err=base/(tag+'.stderr');same(out,row['stdout_sha256']);same(err,row['stderr_sha256'])
 a=datetime.datetime.fromisoformat(row['started_utc']);b=datetime.datetime.fromisoformat(row['ended_utc']);assert b>=a
 windows.append((a,b,str(base.relative_to(R))+'/'+tag,row['returncode']))
 if row['returncode']!=0:failures.append(dict(name=windows[-1][2],returncode=row['returncode']))
 if tag.endswith('-capture'):profiles.append((a,b,tag))
roots=[P/'BOUNDARY-021/growth-extension',P/'BOUNDARY-021/batch-extension',P/'BOUNDARY-022',P/'COUNTERS-008',P/'ROUND-015-CONFIRMATION']
for root in roots:
 for f in sorted(root.rglob('manifest.json')):
  d=json.loads(f.read_text());base=f.parent;manifests.append(str(f.relative_to(R)))
  if isinstance(d,list):
   for item in d:
    B=R/item['snapshot'];same(B/'src/zset_btree.c',item['source_sha256']);same(B/'build/fault',item['binary_sha256']);faults.append(dict(scope=str(base.relative_to(R)),name=item['name'],detected=item['detected'],outcome=item['outcome']))
    for row in item['runs']:rowcheck(base,row,item['name']+'-'+row['stage'])
  else:
   for v,desc in d.get('snapshots',{}).items():
    B=R/desc['path']
    for n,h in desc['files'].items():same(B/n,h)
    for n,h in desc.get('binaries',{}).items():same(B/'build'/n,h)
   for key,h in d.get('binaries',{}).items():
    v,kind=key.split('-');same(R/d['snapshots'][v]['path']/'build'/kind,h)
   if d.get('status')=='failed':
    for row in d['runs']:
     if row.get('stage')=='run':
      binary=R/row['cwd']/row['command'][0]
      if binary.exists():failed_binaries[str(binary.relative_to(R))]=sha(binary)
   for name,desc in d.get('cases',{}).items():
    B=R/desc['snapshot']
    for n,h in desc['files'].items():same(B/n,h)
    for n,k in [('build/census','binary_sha256'),('counts.profraw','raw_sha256'),('counts.profdata','profdata_sha256'),('export.json','export_sha256')]:same(B/n,desc[k])
    same(base/(name+'-counts.json'),desc['counts_sha256'])
   for row in d['runs']:rowcheck(base,row,row['name'])
windows.sort();assert all(a[1]<=b[0] for a,b in zip(windows,windows[1:])),[(a[2],b[2]) for a,b in zip(windows,windows[1:]) if a[1]>b[0]]
assert len(profiles)==3
# Full static evidence of prior round remains immutable except explicitly shared ledgers.
mutable={'.workspace-memory/LIVE-STATUS.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/token-ledger.tsv','experiments/NEXT-STEPS.md'}
old=json.loads((P/'ROUND-014-SHA256.json').read_text())
for n,h in old.items():
 if n not in mutable:same(R/n,h)
for e in json.loads((R/'source-manifest.json').read_text())['files']:same(R/e['path'],e['sha256'])
# Recompute coverage from the raw export, including actual filename IDs.
counts={};census=json.loads((P/'COUNTERS-008/manifest.json').read_text())
for name,desc in census['cases'].items():
 B=R/desc['snapshot'];data=json.loads((B/'export.json').read_text());fs=[f for d in data['data'] for f in d['functions']];curated=json.loads((P/'COUNTERS-008'/(name+'-counts.json')).read_text())
 for c in curated:
  f=next(f for f in fs if f['name']==c['name'] or f['name'].endswith(':'+c['name']));assert f['count']==c['count'];assert len(f['branches'])==len(c['branches'])
  for b,cb in zip(f['branches'],c['branches']):
   file=Path(f['filenames'][b[6]]);snippet='\n'.join(file.read_text().splitlines()[b[0]-1:b[2]])
   assert (b[0],b[1],b[2],b[3],b[4],b[5],str(file.relative_to(B)),snippet)==(cb['start_line'],cb['start_column'],cb['end_line'],cb['end_column'],cb['true'],cb['false'],cb['file'],cb['source'])
 def value(fn,line,col):
  f=next(f for f in fs if f['name']==fn or f['name'].endswith(':'+fn));bs=[b for b in f['branches'] if b[0]==line and b[1]==col and Path(f['filenames'][b[6]]).name=='zset_btree.c'];assert len(bs)==1;return bs[0][4]
 counts[name]=dict(natural_wrap=value('zbtIndexStartResize',2075,9),active_batch_flush=value('zbtreeAppendBatchFlush',3426,9),active_scan=value('zbtreeScan',4335,9),displaced_slot=value('zbtIndexScanSlot',4170,9),multiple_leaf_tags=value('zbtIndexScanSlot',4207,13),probe_reach_rejection=value('zbtIndexScanSlot',4212,30))
 reported=json.loads((P/'COUNTERS-008/summary.json').read_text())['observations'][name]
 assert all(reported[k]==v for k,v in counts[name].items())
matrices=[]
for rel,cells,fixtures,checks in [('BOUNDARY-021/growth-extension',8,2,131094),('BOUNDARY-021/batch-extension/attempt-002',8,4,262188),('BOUNDARY-022',8,2,20),('BOUNDARY-022/cleanup-extension/attempt-002',8,2,10)]:
 base=P/rel;d=json.loads((base/'manifest.json').read_text());assert d['status']=='complete';rows=[r for r in d['runs'] if r['stage']=='run'];assert len(rows)==cells;outputs=[]
 for row in rows:
  txt=(base/(row['name']+'.stdout')).read_text();outputs.append(txt);line=next(s for s in txt.splitlines() if s.startswith('PASS '));v=dict(re.findall(r'(\w+)=([^ ]+)',line));assert int(v['fixtures'])==fixtures and int(v['checks'])==checks
  assert (base/(row['name']+'.stderr')).stat().st_size==0
 assert len(set(s.split('digest=')[-1].strip() for s in outputs))==1
 matrices.append(dict(scope=rel,cells=cells,fixtures_per_cell=fixtures,checks_per_cell=checks,pass_line=line,identical_output=len(set(outputs))==1))
base=P/'ROUND-015-CONFIRMATION';d=json.loads((base/'manifest.json').read_text());assert d['status']=='complete';rows=[r for r in d['runs'] if r['stage']=='run'];assert len(rows)==48
for case,nf,nc in [('wrap',4,262188),('scan',2,20),('cleanup',2,10)]:
 group=[r for r in rows if r['case']==case];assert len(group)==16;digests=[]
 for row in group:
  txt=(base/(row['name']+'.stdout')).read_text();line=next(s for s in txt.splitlines() if s.startswith('PASS '));v=dict(re.findall(r'(\w+)=([^ ]+)',line));assert int(v['fixtures'])==nf and int(v['checks'])==nc;digests.append(v['digest']);assert (base/(row['name']+'.stderr')).stat().st_size==0
 assert len(set(digests))==1
# Four new distinct types: batch1,scan2,cleanup1; allow-zero is repeated twice.
assert len(faults)==7 and sum(x['detected'] for x in faults)==6 and sum(not x['detected'] for x in faults)==1
assert len(failures)==8 # two invalid new-fixture preconditions, six deliberate detected fault runs
# Reconstruct every new oracle/fault/seed patch against its exact saved input.
def apply_unified(original,patch):
 src=original.splitlines(True);lines=patch.splitlines(True);out=[];at=0;i=2
 assert lines[0].startswith('--- ') and lines[1].startswith('+++ ')
 while i<len(lines):
  match=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i]);assert match,lines[i]
  old_start=int(match[1]);old_count=int(match[2] or 1);new_count=int(match[4] or 1);target=old_start-1 if old_start else 0
  assert target>=at;out.extend(src[at:target]);at=target;i+=1;consumed=produced=0
  while i<len(lines) and not lines[i].startswith('@@ '):
   line=lines[i];i+=1;op=line[0];body=line[1:];assert op in ' +-'
   if op in ' -':assert src[at]==body;(at:=at+1);consumed+=1
   if op in ' +':out.append(body);produced+=1
  assert consumed==old_count and produced==new_count
 out.extend(src[at:]);return ''.join(out)
patches_checked=0
for root in roots:
 for patch in root.rglob('oracle.patch'):
  d=json.loads((patch.parent/'manifest.json').read_text());B=R/d['snapshots']['control']['path'];dest=patch.read_text().splitlines()[1][6:]
  assert apply_unified('',patch.read_text())==(B/dest).read_text();patches_checked+=1
 for mf in root.rglob('faults/manifest.json'):
  parent=json.loads((mf.parent.parent/'manifest.json').read_text());base=R/parent['snapshots']['control']['path']/'src/zset_btree.c'
  for fault in json.loads(mf.read_text()):
   patch=mf.parent/(fault['name']+'.patch');assert apply_unified(base.read_text(),patch.read_text())==(R/fault['snapshot']/'src/zset_btree.c').read_text();patches_checked+=1
confirmation=json.loads((P/'ROUND-015-CONFIRMATION/manifest.json').read_text())
for case,parent in [('wrap','BOUNDARY-021/batch-extension/attempt-002'),('scan','BOUNDARY-022'),('cleanup','BOUNDARY-022/cleanup-extension/attempt-002')]:
 desc=confirmation['snapshots'][case+'-control'];old=json.loads((P/parent/'manifest.json').read_text())['snapshots']['control'];oracle='tests/'+desc['oracle']+'.c';patch=P/'ROUND-015-CONFIRMATION'/(case+'-seeds.patch')
 assert apply_unified((R/old['path']/oracle).read_text(),patch.read_text())==(R/desc['path']/oracle).read_text();patches_checked+=1
assert patches_checked==16,patches_checked
checks=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check']),('compiler',['cc','--version']),('arch',['uname','-m'])]:
 out=P/('ROUND-015-'+name+'.stdout');err=P/('ROUND-015-'+name+'.stderr');assert not out.exists();row=dict(name=name,command=cmd,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 row.update(returncode=rc,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),stdout_sha256=sha(out),stderr_sha256=sha(err));checks.append(row);assert rc==0
result=dict(status='pass',validated_hashes=validated,reconstructed_patches=patches_checked,serial_command_windows=len(windows),whole_oracle_count_captures=len(profiles),timing_benchmarks=0,manifests=manifests,matrices=matrices,fresh_confirmation_cells=48,retained_failures=failures,faults=faults,failed_snapshot_binary_hashes=failed_binaries,raw_recomputed_counts=counts,checks=checks,backend='unknown',model='unknown',token_cost='unknown',review='sequential; reviewer startup failed')
(P/'ROUND-015-VERIFY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','validated_hashes','serial_command_windows','whole_oracle_count_captures','fresh_confirmation_cells']},indent=2))
