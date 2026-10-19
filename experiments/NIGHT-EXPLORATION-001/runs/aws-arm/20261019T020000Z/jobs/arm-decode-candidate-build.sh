set -eu
cd @REPO@
python3 - <<'PY'
import os,json,subprocess,hashlib,shutil
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode');rows=[]
for v in 'ABC':
 d=p/'build'/v;(d/'src').mkdir(parents=True,exist_ok=True);shutil.copyfile('scratch/arm-decoder-'+v+'.c',d/'src/zset_btree.c');shutil.copyfile('src/zset_btree.h',d/'src/zset_btree.h')
 for mode in ('native','sanitize'):
  flags=['-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-Isrc','-Icompat','-Ivendor/redis','-Ibench','-O3' if mode=='native' else '-O1']
  if mode=='sanitize':flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
  inc=os.path.relpath(d/'src/zset_btree.c','experiments/EXP-008/referee');obj=d/('kernel-'+mode+'.o')
  cmd=['clang']+flags+['-DDECODER_TREE_SOURCE="'+inc+'"','-c','experiments/EXP-008/referee/kernel.c','-o',str(obj)];subprocess.run(cmd,check=True);rows.append(cmd)
  objects=[str(p/'build/shared'/(name+'-'+mode+'.o')) for name in ('driver','standalone','siphash')]
  cmd=['clang']+flags+objects+[str(obj),'-lm','-o',str(d/('decoder-'+mode))];subprocess.run(cmd,check=True);rows.append(cmd)
(p/'build-info/candidate-commands.json').write_text(json.dumps(rows,indent=2)+'\n')
(p/'build-info/candidate-hashes.json').write_text(json.dumps({str(f):hashlib.sha256(f.read_bytes()).hexdigest() for v in 'ABC' for f in (p/'build'/v).rglob('*') if f.is_file()},indent=2)+'\n')
PY
