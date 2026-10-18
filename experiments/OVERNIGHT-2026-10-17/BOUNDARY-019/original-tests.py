from pathlib import Path
import datetime,hashlib,json,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'attempt-002/manifest.json').read_text());D=P/'original-tests';D.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
for v,desc in M['snapshots'].items():
 B=R/desc['path']
 for kind in ['release','sanitize']:
  for n,h in desc['files'].items():assert sha(B/n)==h
  flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  binary='build/original-'+kind
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG','-DREDIS_TEST',*flags,'tests/upstream.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
  for stage,args in [('build',cmd),('run',[binary])]:
   tag=v+'-'+kind+'-'+stage;row=dict(name=tag,command=args,cwd=desc['path'],started_utc=utc())
   with (D/(tag+'.stdout')).open('w') as out,(D/(tag+'.stderr')).open('w') as err:
    try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
   row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(D/(tag+'.stdout')),stderr_sha256=sha(D/(tag+'.stderr')));rows.append(row)
   (D/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==0
  print(v,kind,'original PASS',flush=True)
