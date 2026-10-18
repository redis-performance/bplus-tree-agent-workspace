from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-round015-confirmation';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
cases=[('wrap','BOUNDARY-021/batch-extension/attempt-002','batch_generation_oracle',[(61543,64513),(61559,64553)]),('scan','BOUNDARY-022','scan_interval_oracle',[(62507,64567),(62533,64577)]),('cleanup','BOUNDARY-022/cleanup-extension/attempt-002','cleanup_interval_oracle',[(63503,64579),(63521,64601)])]
M=dict(status='preparing',plan_sha256=sha(P/'PLAN.md'),provenance='uncommitted isolated snapshots; fresh seeds; debug flag factorial; no timings',snapshots={},runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for case,parent,oracle,seeds in cases:
 F=json.loads((P.parent/parent/'manifest.json').read_text());assert F['status']=='complete'
 for v in ['control','A','B','C']:
  key=case+'-'+v;desc=F['snapshots'][v];B=S/key;B.mkdir()
  for n,h in desc['files'].items():
   src=R/desc['path']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
  file=B/'tests'/(oracle+'.c');old=file.read_text();new=old
  for a,b in seeds:new=new.replace(str(a),str(b))
  assert new!=old;file.write_text(new)
  if v=='control':(P/(case+'-seeds.patch')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='a/tests/'+oracle+'.c',tofile='b/tests/'+oracle+'.c')))
  M['snapshots'][key]=dict(path=str(B.relative_to(R)),case=case,variant=v,oracle=oracle,base_commit=F['base_commit'],source_manifest_sha256=sha(P.parent/parent/'manifest.json'),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
M['status']='frozen';M['frozen_utc']=utc();save();start=time.monotonic()
for key,desc in M['snapshots'].items():
 B=R/desc['path']
 for kind in ['release','sanitize']:
  for debug in [True,False]:
   if time.monotonic()-start>600:M['status']='budget-exhausted';save();raise SystemExit(3)
   label=kind+('-debug' if debug else '-nodebug');binary='build/'+label
   flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
   cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer',*flags,*(['-DREDIS_DEBUG'] if debug else []),'tests/'+desc['oracle']+'.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
   for stage,args in [('build',cmd),('run',[binary])]:
    tag=key+'-'+label+'-'+stage;row=dict(name=tag,snapshot=key,case=desc['case'],variant=desc['variant'],kind=kind,debug=debug,stage=stage,command=args,cwd=desc['path'],started_utc=utc())
    with (P/(tag+'.stdout')).open('w') as out,(P/(tag+'.stderr')).open('w') as err:
     try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
     except subprocess.TimeoutExpired:rc='timeout'
    row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(tag+'.stdout')),stderr_sha256=sha(P/(tag+'.stderr')));M['runs'].append(row);save()
    if rc!=0:M['status']='failed';save();raise SystemExit(tag+' failed '+str(rc))
   desc.setdefault('binaries',{})[label]=sha(B/binary);save();print(key,label,'PASS',flush=True)
for desc in M['snapshots'].values():
 for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
M['status']='complete';save();summary={}
for case,_,_,_ in cases:
 runs=[r for r in M['runs'] if r['case']==case and r['stage']=='run'];assert len(runs)==16
 outputs=[(P/(r['name']+'.stdout')).read_text() for r in runs];assert all('PASS fixtures=' in s for s in outputs)
 digests=[s.split('digest=')[-1].strip() for s in outputs];assert len(set(digests))==1
 assert all((P/(r['name']+'.stderr')).stat().st_size==0 for r in runs)
 summary[case]=dict(cells=16,logical_digest=digests[0],identical_output=len(set(outputs))==1,pass_line=next(s for s in outputs[0].splitlines() if s.startswith('PASS ')))
(P/'summary.json').write_text(json.dumps(dict(status='pass',cells=48,observations=summary),indent=2)+'\n')
