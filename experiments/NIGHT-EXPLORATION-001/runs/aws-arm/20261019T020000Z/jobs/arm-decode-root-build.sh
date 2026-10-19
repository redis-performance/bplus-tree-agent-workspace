set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode
mkdir -p "$OUT/build/root/src"
cat src/zset_btree.c experiments/EXP-007/referee/control.inc experiments/EXP-008/referee/policy-control.inc > "$OUT/build/root/src/zset_btree.c"
cp src/zset_btree.h "$OUT/build/root/src/"
python3 - <<'PY'
import os,subprocess,json,hashlib
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode');rows=[]
for mode in ('native','sanitize'):
 flags=['-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-Isrc','-Icompat','-Ivendor/redis','-Ibench','-O3' if mode=='native' else '-O1']
 if mode=='sanitize':flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
 inc=os.path.relpath(p/'build/root/src/zset_btree.c','experiments/EXP-008/referee');obj=p/'build/root'/('kernel-'+mode+'.o')
 cmd=['clang']+flags+['-DDECODER_TREE_SOURCE="'+inc+'"','-c','experiments/EXP-008/referee/kernel.c','-o',str(obj)];subprocess.run(cmd,check=True);rows.append(cmd)
 objects=[str(p/'build/shared'/(name+'-'+mode+'.o')) for name in ('driver','standalone','siphash')]
 cmd=['clang']+flags+objects+[str(obj),'-lm','-o',str(p/'build/root'/('decoder-'+mode))];subprocess.run(cmd,check=True);rows.append(cmd)
(p/'build-info/root-commands.json').write_text(json.dumps(rows,indent=2)+'\n')
(p/'build-info/root-hashes.json').write_text(json.dumps({str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'build/root').rglob('*') if f.is_file()},indent=2)+'\n')
PY
