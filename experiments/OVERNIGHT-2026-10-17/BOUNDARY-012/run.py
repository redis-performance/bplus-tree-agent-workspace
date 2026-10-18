from pathlib import Path
import json,hashlib,shutil,subprocess,time,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((R/'experiments/EXP-002/guard-extension/freeze.json').read_text());S=R/'scratch/overnight-boundary-012';assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();M=dict(status='preparing',base_commit=F['base_commit'],parent_freeze_sha256=sha(R/'experiments/EXP-002/guard-extension/freeze.json'),provenance='uncommitted new oracle over exact control/A/B/C snapshots; root source untouched',sources={},runs=[])
(P/'oracle.patch').write_text(''.join(difflib.unified_diff([], (R/'tests/iterator_mutation_oracle.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/tests/iterator_mutation_oracle.c')))
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for v,files in F['files'].items():
 B=S/v;B.mkdir()
 for n,h in files.items():
  src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 shutil.copy2(R/'tests/iterator_mutation_oracle.c',B/'tests/iterator_mutation_oracle.c');M['sources'][v]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()};save()
 for kind in ['release','sanitize']:
  (B/f'build/{kind}').mkdir(parents=True);flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG']+(['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']);binary=f'build/{kind}/oracle';cmd=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags,'tests/iterator_mutation_oracle.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
  for step,command in [('build',cmd),('run',[binary])]:
   name=f'{v}-{kind}-{step}';out=P/(name+'.stdout');err=P/(name+'.stderr');start=time.monotonic()
   with out.open('w') as so,err.open('w') as se:
    try:q=subprocess.run(command,cwd=B,stdout=so,stderr=se,timeout=120);rc=q.returncode
    except subprocess.TimeoutExpired:rc='timeout'
   row=dict(variant=v,kind=kind,step=step,command=command,cwd=str(B.relative_to(R)),returncode=rc,seconds=time.monotonic()-start,stdout=str(out.relative_to(P)),stderr=str(err.relative_to(P)),stdout_sha256=sha(out),stderr_sha256=sha(err))
   if step=='run':row['binary_sha256']=sha(B/binary)
   M['runs'].append(row);save();print(name,rc,flush=True)
   if rc!=0:M['status']='failed';save();raise SystemExit(1)
for v,files in M['sources'].items():
 for n,h in files.items():assert sha(S/v/n)==h
M['status']='pass';save()
