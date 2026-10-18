from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-boundary-014';assert not S.exists();S.mkdir();F=json.loads((R/'experiments/EXP-004/freeze.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
M=dict(base_commit=F['base_commit'],provenance='Uncommitted isolated snapshots; protected git not retried',plan_sha256=sha(P/'PLAN.md'),oracle_sha256=sha(R/'tests/zero_physical_oracle.c'),snapshots={},runs=[])
(P/'oracle.patch').write_text(''.join(difflib.unified_diff([], (R/'tests/zero_physical_oracle.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/tests/zero_physical_oracle.c')))
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'][v].items():
  src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 shutil.copy2(R/'tests/zero_physical_oracle.c',B/'tests/zero_physical_oracle.c');(B/'build').mkdir();M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});save()
 for kind in ['release','sanitize']:
  flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags,'tests/zero_physical_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}']
  for stage,command in [('build',cmd),('run',[f'build/{kind}'])]:
   name=f'{v}-{kind}-{stage}';row=dict(name=name,command=command,started_utc=utc())
   with (P/(name+'.stdout')).open('w') as so,(P/(name+'.stderr')).open('w') as se:
    try:rc=subprocess.run(command,cwd=B,stdout=so,stderr=se,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
   row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(name+'.stdout')),stderr_sha256=sha(P/(name+'.stderr')));M['runs'].append(row);save();print(name,rc,flush=True);assert rc==0,name
  M['snapshots'][v][kind+'_sha256']=sha(B/f'build/{kind}');save()
M['status']='pass';save()
