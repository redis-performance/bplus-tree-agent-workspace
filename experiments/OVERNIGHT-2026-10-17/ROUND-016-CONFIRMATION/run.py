from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-round016-confirmation';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
cases=[('external','BOUNDARY-023/external-extension','live_widen_external_oracle',[[str(seed),str(mode)] for seed in [69501,69503] for mode in range(3)]),('narrow','BOUNDARY-023/narrowing-extension/attempt-002','live_widen_narrow_oracle',[[str(seed)] for seed in [69521,69541]])]
M=dict(status='preparing',plan_sha256=sha(P/'PLAN.md'),provenance='uncommitted exact snapshots; fresh input seeds; debug flag omitted; no timings',snapshots={},runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for case,parent,oracle,arguments in cases:
 F=json.loads((P.parent/parent/'manifest.json').read_text());assert F['status']=='complete'
 for v in ['control','A','B','C']:
  key=case+'-'+v;desc=F['snapshots'][v];B=S/key;B.mkdir()
  for n,h in desc['files'].items():
   src=R/desc['path']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
  M['snapshots'][key]=dict(path=str(B.relative_to(R)),case=case,variant=v,oracle=oracle,base_commit=F['base_commit'],source_manifest_sha256=sha(P.parent/parent/'manifest.json'),arguments=arguments,files=desc['files']);(B/'build').mkdir()
M['status']='frozen';M['frozen_utc']=utc();save();start=time.monotonic()
for key,desc in M['snapshots'].items():
 B=R/desc['path']
 for kind in ['release','sanitize']:
  if time.monotonic()-start>600:M['status']='budget-exhausted';save();raise SystemExit(3)
  binary='build/'+kind;flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer',*flags,'tests/'+desc['oracle']+'.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
  for stage,args in [('build',cmd)]+[('-'.join(a),[binary,*a]) for a in desc['arguments']]:
   tag=key+'-'+kind+'-'+stage;row=dict(name=tag,snapshot=key,case=desc['case'],variant=desc['variant'],kind=kind,debug=False,stage=stage,command=args,cwd=desc['path'],started_utc=utc())
   with (P/(tag+'.stdout')).open('w') as out,(P/(tag+'.stderr')).open('w') as err:
    try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
   row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(tag+'.stdout')),stderr_sha256=sha(P/(tag+'.stderr')));M['runs'].append(row);save()
   if rc!=0:M['status']='failed';save();raise SystemExit(tag+' failed '+str(rc))
   print(tag,'PASS',flush=True)
  desc.setdefault('binaries',{})[kind]=sha(B/binary);save()
for desc in M['snapshots'].values():
 for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
summary={}
for case,parent,oracle,arguments in cases:
 for a in arguments:
  label='-'.join(a);rows=[r for r in M['runs'] if r['case']==case and r['stage']==label];assert len(rows)==8
  outputs=[(P/(r['name']+'.stdout')).read_text() for r in rows];digests=[s.split('digest=')[-1].strip() for s in outputs];assert len(set(digests))==1
  assert all((P/(r['name']+'.stderr')).stat().st_size==0 for r in rows)
  summary[case+'-'+label]=dict(cells=8,digest=digests[0],identical_output=len(set(outputs))==1,pass_line=next(s for s in outputs[0].splitlines() if s.startswith('PASS ')))
M['status']='complete';save();(P/'summary.json').write_text(json.dumps(dict(status='pass',cells=64,observations=summary),indent=2)+'\n')
