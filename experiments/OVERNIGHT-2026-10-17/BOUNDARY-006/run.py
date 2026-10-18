from pathlib import Path
import subprocess,hashlib,json,time,difflib,shutil
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-boundary-006/base'
assert not B.exists() and not (P/'manifest.json').exists();B.mkdir(parents=True)
F=json.loads((P.parent/'HARNESS-001/freeze.json').read_text())
for name,digest in F['files'].items():
 src=R/F['snapshot']/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==digest
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
for name in ['tests/boundary_oracle.c','tests/bulk_delete_oracle.c']:shutil.copy2(R/name,B/name)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m={'base_commit':F['base_commit'],'snapshot':str(B.relative_to(R)),'provenance':'uncommitted new oracle; tree/referee identical to HARNESS-001','sources':{str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()},'runs':[]}
(P/'oracle.patch').write_text(''.join(difflib.unified_diff([], (R/'tests/bulk_delete_oracle.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/tests/bulk_delete_oracle.c')))
def save():(P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
save()
for kind in ['release','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG']
 flags+=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
 binary=f'build/{kind}';(B/'build').mkdir(exist_ok=True)
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags,'tests/bulk_delete_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
 for step,command in [('build',cmd),('run',[binary])]:
  name=f'{kind}-{step}';start=time.monotonic()
  with (P/f'{name}.stdout').open('w') as so,(P/f'{name}.stderr').open('w') as se:
   try:r=subprocess.run(command,cwd=B,stdout=so,stderr=se,timeout=120);code=r.returncode
   except subprocess.TimeoutExpired:code='timeout'
  row=dict(name=name,command=command,cwd=str(B.relative_to(R)),returncode=code,elapsed_seconds=time.monotonic()-start)
  for out in ['stdout','stderr']:row[out+'_sha256']=sha(P/f'{name}.{out}')
  if step=='run':row['binary_sha256']=sha(B/binary)
  m['runs'].append(row);save();print(name,code,flush=True)
  if code!=0:raise SystemExit(1)
for name,h in m['sources'].items():assert sha(B/name)==h
m['status']='pass';save()
