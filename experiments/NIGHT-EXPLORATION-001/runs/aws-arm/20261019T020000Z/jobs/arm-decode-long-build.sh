set -eu
cd @REPO@
python3 - <<'PY'
import subprocess,json,hashlib
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode');out=p/'build-long';out.mkdir(exist_ok=False);rows=[]
for mode in ('native','sanitize'):
 flags=['-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-Isrc','-Icompat','-Ivendor/redis','-Ibench','-O3' if mode=='native' else '-O1']
 if mode=='sanitize':flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
 driver=out/('driver-'+mode+'.o');cmd=['clang']+flags+['-c',str(p/'duration-driver.c'),'-o',str(driver)];subprocess.run(cmd,check=True);rows.append(cmd)
 for v in ['base','root','A','B','C']:
  (out/v).mkdir(exist_ok=True)
  objects=[str(driver),str(p/'build/shared'/('standalone-'+mode+'.o')),str(p/'build/shared'/('siphash-'+mode+'.o')),str(p/'build'/v/('kernel-'+mode+'.o'))]
  cmd=['clang']+flags+objects+['-lm','-o',str(out/v/('decoder-'+mode))];subprocess.run(cmd,check=True);rows.append(cmd)
(p/'build-info/duration-commands.json').write_text(json.dumps(rows,indent=2)+'\n')
(p/'build-info/duration-hashes.json').write_text(json.dumps({str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in out.rglob('*') if f.is_file()},indent=2)+'\n')
PY
