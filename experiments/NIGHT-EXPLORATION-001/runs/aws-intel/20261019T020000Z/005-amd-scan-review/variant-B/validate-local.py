import subprocess,json,datetime,platform,hashlib
from pathlib import Path
p=Path(__file__).parent;d=Path('scratch/amd-scan-B');out=p/'local-correctness';out.mkdir(exist_ok=True);records=[]
for mode in ['native','sanitize','portable-native','portable-sanitize']:
 flags=['-O3'] if 'sanitize' not in mode else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
 if mode.startswith('portable'):flags+=['-DZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE']
 for name in ['upstream','all_match_guard_oracle']:
  cmd=['clang','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer']+flags+['-I'+str(d/'src'),'-I'+str(d/'compat'),'-I'+str(d/'vendor/redis')]
  if name=='upstream':cmd+=['-DREDIS_TEST','-DREDIS_DEBUG',str(d/'tests/upstream.c'),str(d/'src/zset_btree.c')]
  else:cmd+=[str(d/'tests/all_match_guard_oracle.c')]
  binary=d/(mode+'-'+name);cmd+=[str(d/'compat/standalone.c'),str(d/'vendor/redis/siphash.c'),'-lm','-o',str(binary)]
  tag=mode+'-'+name
  with (out/(tag+'-build.stdout')).open('w') as stdout,(out/(tag+'-build.stderr')).open('w') as stderr:subprocess.run(cmd,check=True,timeout=90,stdout=stdout,stderr=stderr)
  with (out/(tag+'.stdout')).open('w') as stdout,(out/(tag+'.stderr')).open('w') as stderr:result=subprocess.run([str(binary)],timeout=60,stdout=stdout,stderr=stderr)
  records.append(dict(mode=mode,test=name,compile_command=cmd,returncode=result.returncode,binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest()))
  (out/'results.json').write_text(json.dumps(dict(scope='local bounded correctness only; no performance measurements',architecture=platform.machine(),compiler=subprocess.check_output(['clang','--version'],text=True).splitlines()[0],rows=records),indent=2)+'\n')
  assert result.returncode==0
print('PASS eight local correctness executables')
