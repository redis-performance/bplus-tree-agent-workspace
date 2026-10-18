from pathlib import Path
import subprocess,json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-harness-002/base'
assert not (P/'validation.json').exists();records=[]
for kind in ['release','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']
 flags+=['-O3'] if kind=='release' else ['-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all']
 (B/f'build/{kind}').mkdir(parents=True)
 common=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags]
 support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
 binary=f'build/{kind}/btree-bench';test=f'build/{kind}/btree-test'
 commands=[('build',common+['bench/microbench.c',*support,'-o',binary]),('build-tests',common+['-DREDIS_TEST','-DREDIS_DEBUG','tests/upstream.c',*support,'-o',test]),('upstream',[test]),('existing-referee',['python3','tests/test_microbench.py',binary,'-v']),('query-oracle',['python3',str((P/'test_query.py').relative_to(R)),str((B/binary).relative_to(R))])]
 for step,cmd in commands:
  cwd=R if step=='query-oracle' else B
  row=dict(kind=kind,step=step,command=cmd,cwd=str(cwd.relative_to(R)),stdout=f'{kind}-{step}.stdout',stderr=f'{kind}-{step}.stderr')
  with (P/row['stdout']).open('w') as so,(P/row['stderr']).open('w') as se:
   try:p=subprocess.run(cmd,cwd=cwd,stdout=so,stderr=se,timeout=120);row['returncode']=p.returncode
   except subprocess.TimeoutExpired:row['returncode']='timeout'
  for f in ['stdout','stderr']:row[f+'_sha256']=hashlib.sha256((P/row[f]).read_bytes()).hexdigest()
  records.append(row);(P/'validation.json').write_text(json.dumps(records,indent=2)+'\n')
  print(kind,step,row['returncode'],flush=True);assert row['returncode']==0
