from pathlib import Path
import subprocess,json,csv,os,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-006/base'
assert not (P/'validation.json').exists();rows=[]
for kind in ['release','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
 binary=f'build/{kind}/btree-bench';(B/Path(binary).parent).mkdir(parents=True)
 commands=[('build',['cc','-Isrc','-Icompat','-Ivendor/redis',*flags,'bench/microbench.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary],None)]
 for mode in ['0','1000']:commands.append(('smoke-'+mode,[binary,'--size','1000','--ops','2501','--member-bytes','320','--query-order','independent'],mode))
 for step,cmd,mode in commands:
  out=P/f'{kind}-{step}.stdout';err=P/f'{kind}-{step}.stderr'
  with out.open('w') as so,err.open('w') as se:r=subprocess.run(cmd,cwd=B,env=dict(os.environ,PROFILE_USEC=mode) if mode else None,stdout=so,stderr=se,timeout=120)
  row=dict(kind=kind,step=step,command=cmd,cwd=str(B.relative_to(R)),profile_usec=mode,returncode=r.returncode,stdout=out.name,stderr=err.name,stdout_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),stderr_sha256=hashlib.sha256(err.read_bytes()).hexdigest());rows.append(row);(P/'validation.json').write_text(json.dumps(rows,indent=2)+'\n');assert r.returncode==0
  if mode:assert len(list(csv.DictReader(out.open())))==8
  print(kind,step,r.returncode,flush=True)
