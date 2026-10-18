from pathlib import Path
import subprocess,json,hashlib,csv
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-003/base'
assert not (P/'validation.json').exists()
records=[]
for kind in ['release','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']
 flags+=['-O3'] if kind=='release' else ['-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all']
 binary=f'build/{kind}/btree-bench';(B/Path(binary).parent).mkdir(parents=True)
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags,'bench/microbench.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
 for name,command in [('build',cmd),('smoke',[binary,'1','1000','10000']),('reverse-smoke',[binary,'2','1000','10000'])]:
  out=P/f'{kind}-{name}.stdout';err=P/f'{kind}-{name}.stderr'
  with out.open('w') as so,err.open('w') as se: result=subprocess.run(command,cwd=B,stdout=so,stderr=se,timeout=120)
  records.append(dict(kind=kind,step=name,command=command,cwd=str(B.relative_to(R)),returncode=result.returncode,stdout=out.name,stderr=err.name))
  (P/'validation.json').write_text(json.dumps(records,indent=2)+'\n')
  assert result.returncode==0
  if name!='build':
   rows=list(csv.DictReader(out.open()));assert len(rows)==4
   assert ''.join(r['arm'] for r in rows)==('RIIR' if name=='smoke' else 'IRRI')
   assert {int(r['operations']) for r in rows}=={10000}
   assert {int(r['checksum']) for r in rows}=={4995000}
   assert len({r['tree_bytes'] for r in rows})==1
   assert len({r['access_fingerprint'] for r in rows})==2
 print(kind,'passed',flush=True)
