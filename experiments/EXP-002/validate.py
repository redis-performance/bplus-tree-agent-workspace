from pathlib import Path
import subprocess,json,hashlib,time
P=Path(__file__).resolve().parent;R=P.parents[1];S=R/'scratch/exp-002';assert not (P/'validation.json').exists();rows=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for v in ['control','A','B','C']:
 B=S/v
 for kind in ['release','sanitize']:
  flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
  (B/f'build/{kind}').mkdir(parents=True);common=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags];support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
  jobs=[('bench','bench/microbench.c',[]),('upstream','tests/upstream.c',['-DREDIS_TEST','-DREDIS_DEBUG']),('lex','tests/lex_boundary_oracle.c',['-DREDIS_DEBUG']),('score','tests/score_boundary_oracle.c',['-DREDIS_DEBUG'])]
  for job,source,extra in jobs:
   binary=f'build/{kind}/{job}';commands=[('build',common+extra+[source,*support,'-o',binary])]
   if job!='bench':commands.append(('run',[binary]))
   else:commands.append(('smoke',[binary,'--size','1000','--ops','2501','--member-bytes','320','--query-order','independent']))
   for step,cmd in commands:
    name=f'{v}-{kind}-{job}-{step}';out=P/'review'/(name+'.stdout');err=P/'review'/(name+'.stderr');begin=time.monotonic()
    with out.open('w') as so,err.open('w') as se:
     try:q=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120);rc=q.returncode
     except subprocess.TimeoutExpired:rc='timeout'
    row=dict(variant=v,kind=kind,job=job,step=step,command=cmd,cwd=str(B.relative_to(R)),returncode=rc,elapsed_seconds=time.monotonic()-begin,stdout=str(out.relative_to(P)),stderr=str(err.relative_to(P)),stdout_sha256=sha(out),stderr_sha256=sha(err))
    if step!='build':row['binary_sha256']=sha(B/binary)
    rows.append(row);(P/'validation.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==0,name
  print(v,kind,'PASS',flush=True)
