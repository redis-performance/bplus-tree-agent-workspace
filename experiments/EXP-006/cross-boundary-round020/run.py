from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/experiment006-cross-boundary-round020'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((P.parent/'freeze.json').read_text())
Q=R/'experiments/OVERNIGHT-2026-10-17/ROUND-019-NEXT-PREFLIGHT.json';PRE=json.loads(Q.read_text())
assert not S.exists();assert not (P/'manifest.json').exists();S.mkdir()
M=dict(status='preparing',base_commit=F['base_commit'],provenance='uncommitted isolated exact source snapshots',started_utc=utc(),plan_sha256=sha(P/'PLAN.md'),driver_sha256=sha(Path(__file__)),parent_freeze_sha256=sha(P.parent/'freeze.json'),preflight_sha256=sha(Q),snapshots={},binaries={},runs=[],root_hashes={n:sha(R/n) for n in ['src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','tests/upstream.c']})
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for item in PRE['items']:
 assert sha(R/item['source'])==item['oracle_sha256']
 assert sha(R/item['parent_manifest'])==item['parent_manifest_sha256']
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'][v].items():
  src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for item in PRE['items']:shutil.copy2(R/item['source'],B/'tests'/item['oracle'])
 M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
M.update(status='frozen',frozen_utc=utc());save();start=time.monotonic()
cutoff=datetime.datetime.fromisoformat('2026-10-18T06:27:00+00:00')
for phase,seed,debug in [('discovery',92503,True),('confirmation',92521,False)]:
 for v,desc in M['snapshots'].items():
  B=R/desc['path']
  for kind in ['native','sanitize']:
   flags=['-O3'] if kind=='native' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
   for item in PRE['items']:
    name=item['name'];binary='build/'+phase+'-'+kind+'-'+name
    cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer']+(['-DREDIS_DEBUG'] if debug else [])+flags+['tests/'+item['oracle'],'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
    modes=[0,1,2] if name=='external-relocation' else [None]
    commands=[('build',None,cmd)]+[('run',mode,[binary,str(seed)]+([] if mode is None else [str(mode)])) for mode in modes]
    for stage,mode,args in commands:
     if time.monotonic()-start>1050 or datetime.datetime.now(datetime.timezone.utc)>=cutoff:
      M.update(status='budget-exhausted',ended_utc=utc());save();raise SystemExit(3)
     tag='-'.join([phase,v,kind,name,stage]+([] if mode is None else [str(mode)]))
     row=dict(name=tag,phase=phase,variant=v,kind=kind,oracle=name,stage=stage,mode=mode,seed=seed,debug=debug,command=args,cwd=desc['path'],started_utc=utc())
     M['active_command']=row;save()
     with (P/(tag+'.stdout')).open('w') as out,(P/(tag+'.stderr')).open('w') as err:
      try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
      except subprocess.TimeoutExpired:rc='timeout'
     row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(tag+'.stdout')),stderr_sha256=sha(P/(tag+'.stderr')));M['runs'].append(row);M.pop('active_command');save()
     if rc!=0:M.update(status='failed',ended_utc=utc());save();raise SystemExit(tag+' failed '+str(rc))
     if stage=='run':
      lines=(P/(tag+'.stdout')).read_text().splitlines();assert lines and lines[-1].startswith('PASS seed='+str(seed)+' '),tag
     else:M['binaries'][str((B/binary).relative_to(R))]=sha(B/binary);save()
     print(tag,'PASS',flush=True)
 for item in PRE['items']:
  for mode in ([0,1,2] if item['name']=='external-relocation' else [None]):
   rows=[r for r in M['runs'] if r['phase']==phase and r['oracle']==item['name'] and r['stage']=='run' and r['mode']==mode]
   assert len(rows)==8
   digests=[(P/(r['name']+'.stdout')).read_text().split('digest=')[-1].strip() for r in rows]
   assert len(set(digests))==1,(phase,item['name'],mode,digests)
 M[phase+'_complete_utc']=utc();save()
for desc in M['snapshots'].values():
 for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
for n,h in M['root_hashes'].items():assert sha(R/n)==h
M.update(status='complete',ended_utc=utc(),semantic_cells=sum(r['stage']=='run' for r in M['runs']),builds=sum(r['stage']=='build' for r in M['runs']));save()
assert M['semantic_cells']==80 and M['builds']==48
print('COMPLETE 80 semantic cells, 48 builds; no timing claim',flush=True)
