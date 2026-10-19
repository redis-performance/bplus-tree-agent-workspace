from pathlib import Path
import subprocess,json,time,hashlib
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parents[1];LOG=OUT/'lookup-batch-logs';P=OUT/'lookup-batch-validation.json';r=json.loads(P.read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
for kind in ('lookup','batch'):
 for san in (False,True):
  label=kind+('-san' if san else '')+'-strict';binary='scratch/m6-caller/harness-lookup/'+label
  cmd=['clang','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer',*(['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if san else ['-O3']),'-Isrc','-Icompat','-Ivendor/redis',str(OUT/(kind+'.c')),'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
  start=datetime.now(timezone.utc).isoformat();t=time.monotonic();run=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
  for chan,data in [('stdout',run.stdout),('stderr',run.stderr)]:(LOG/(label+'.'+chan)).write_text(data)
  r['commands'].append(dict(name='build-'+label,command=[str(arg).replace(str(Path.cwd())+'/', '') for arg in cmd],cwd='workspace-root',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.monotonic()-t,returncode=run.returncode,stdout_sha256=sha(LOG/(label+'.stdout')),stderr_sha256=sha(LOG/(label+'.stderr'))));assert run.returncode==0,label
r['strict_builds']='PASS: both frontends native+ASan/UBSan compile with -Wall -Wextra -Werror';P.write_text(json.dumps(r,indent=2)+'\n');print(r['strict_builds'])
