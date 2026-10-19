set -eu
cd @REPO@
python3 - <<'PY'
import subprocess,json,hashlib,os
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/004-update');(p/'build').mkdir(exist_ok=False);(p/'validation').mkdir(exist_ok=True);rows=[]
assert hashlib.sha256(Path('src/zset_btree.c').read_bytes()).hexdigest()=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2'
assert hashlib.sha256((p/'update-path-bench.c').read_bytes()).hexdigest()==json.load(open(p/'harness-origin.json'))['sha256']
for mode in ['native','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-Isrc','-Icompat','-Ivendor/redis','-O3' if mode=='native' else '-O1']
 if mode=='sanitize':flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
 cmd=['clang']+flags+[str(p/'update-path-bench.c'),'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',str(p/'build'/('update-'+mode))];subprocess.run(cmd,check=True,timeout=120);rows.append(cmd)
 for n in ([100,1000,10000,100000,1000000] if mode=='native' else [100,1000,10000]):
  for case in ['same','preserve','nearby','distant','plus-n']:
   cmd=[str(p/'build'/('update-'+mode)),'--case',case,'--size',str(n),'--ops','1000','--seed','1'];name=f'{mode}-{n}-{case}'
   with (p/'validation'/(name+'.csv')).open('w') as out,(p/'validation'/(name+'.stderr')).open('w') as err:subprocess.run(cmd,stdout=out,stderr=err,check=True,timeout=120)
   rows.append(cmd)
(p/'commands.json').write_text(json.dumps(rows,indent=2)+'\n');(p/'binary-hashes.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'build').iterdir()},indent=2)+'\n')
PY
