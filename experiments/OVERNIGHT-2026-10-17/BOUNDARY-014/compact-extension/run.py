from pathlib import Path
import json,hashlib,shutil,subprocess,datetime
P=Path(__file__).resolve().parent;R=P.parents[3];F=json.loads((R/'experiments/EXP-004/ordered-guards/freeze.json').read_text());S=R/'scratch/overnight-boundary-014-compact';assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();M=dict(status='preparing',base_commit=F['base_commit'],plan_sha256=sha(P/'PLAN.md'),snapshots={},runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for v,files in F['files'].items():
 B=S/v;B.mkdir()
 for n,h in files.items():
  src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 shutil.copy2(P/'compact_zero.c',B/'tests/compact_zero.c');M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
M['status']='running';save()
for v,desc in M['snapshots'].items():
 B=R/desc['path']
 for kind in ['release','sanitize']:
  flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags,'tests/compact_zero.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}']
  for stage,args in [('build',cmd),('run',[f'build/{kind}'])]:
   name=f'{v}-{kind}-{stage}';row=dict(name=name,variant=v,kind=kind,stage=stage,command=args,started_utc=utc())
   with (P/f'{name}.stdout').open('w') as so,(P/f'{name}.stderr').open('w') as se:
    try:rc=subprocess.run(args,cwd=B,stdout=so,stderr=se,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
   row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/f'{name}.stdout'),stderr_sha256=sha(P/f'{name}.stderr'));M['runs'].append(row);save();assert rc==0,name
  print(v,kind,'PASS',flush=True)
for v,desc in M['snapshots'].items():
 for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
outputs=[(P/f'{v}-{k}-run.stdout').read_text() for v in M['snapshots'] for k in ['release','sanitize']];assert len(set(outputs))==1
M['status']='pass';save();print(outputs[0].splitlines()[-1],flush=True)
