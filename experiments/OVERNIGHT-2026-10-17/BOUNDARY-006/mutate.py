from pathlib import Path
import subprocess,hashlib,json,time,difflib,shutil
P=Path(__file__).resolve().parent;R=P.parents[2];BASE=R/'scratch/overnight-boundary-006/base'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
F=json.loads((P/'manifest.json').read_text());M=P/'mutations';M.mkdir()
source=(BASE/'src/zset_btree.c').read_text()
faults={
 'skip-rebuild':('        zbtIndexRebuild(zs);\n        return deleted;', '        /* intentional fault: omitted rebuild */\n        return deleted;'),
 'endpoint-clip':('    if (end >= zs->length) end = zs->length - 1;', '    if (end >= zs->length) end = zs->length - 2; /* intentional fault */')}

records=[]
for name,(old,new) in faults.items():
 assert source.count(old)==1;B=R/f'scratch/overnight-boundary-006/{name}';assert not B.exists();B.mkdir()
 for f,h in F['sources'].items():
  assert sha(BASE/f)==h;dst=B/f;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(BASE/f,dst)
 changed=source.replace(old,new);(B/'src/zset_btree.c').write_text(changed)
 patch=M/f'{name}.patch';patch.write_text(''.join(difflib.unified_diff(source.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/bulk_delete_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','fault-test']
 item=dict(name=name,snapshot=str(B.relative_to(R)),source_sha256=sha(B/'src/zset_btree.c'),patch_sha256=sha(patch),runs=[])
 for step,command in [('build',cmd),('run',['./fault-test'])]:
  tag=f'{name}-{step}';t=time.monotonic()
  with (M/f'{tag}.stdout').open('w') as so,(M/f'{tag}.stderr').open('w') as se:
   try:q=subprocess.run(command,cwd=B,stdout=so,stderr=se,timeout=120);code=q.returncode
   except subprocess.TimeoutExpired:code='timeout'
  row=dict(step=step,command=command,returncode=code,elapsed_seconds=time.monotonic()-t)
  for out in ['stdout','stderr']:row[out+'_sha256']=sha(M/f'{tag}.{out}')
  item['runs'].append(row)
  print(name,step,code,flush=True)
  if step=='build' and code!=0:break
 item['binary_sha256']=sha(B/'fault-test') if (B/'fault-test').exists() else None
 records.append(item);(M/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
