from pathlib import Path
import json,hashlib,shutil,subprocess,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-boundary-012';F=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();original=(S/'C/src/zset_btree.c').read_text();rows=[]
for name,old,new in [('nonboolean-reverse','if (!reverse && ele == NULL && len == NULL && score != NULL)','if (reverse != 1 && ele == NULL && len == NULL && score != NULL)'),('next-leaf-position','else { iter->leaf = leaf->next; iter->pos = 0; }','else { iter->leaf = leaf->next; iter->pos = 1; }')]:
 B=S/'faults'/name;B.mkdir(parents=True)
 for n,h in F['sources']['C'].items():
  src=S/'C'/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 assert original.count(old)==1;changed=original.replace(old,new,1);(B/'src/zset_btree.c').write_text(changed);(P/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-O1','-g','-DREDIS_DEBUG','tests/iterator_mutation_oracle.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','fault']
 for step,command in [('build',cmd),('run',['./fault'])]:
  out=P/(name+'-'+step+'.stdout');err=P/(name+'-'+step+'.stderr')
  with out.open('w') as so,err.open('w') as se:
   try:q=subprocess.run(command,cwd=B,stdout=so,stderr=se,timeout=120);rc=q.returncode
   except subprocess.TimeoutExpired:rc='timeout'
  row=dict(name=name,step=step,command=command,cwd=str(B.relative_to(R)),returncode=rc,stdout=str(out.relative_to(P)),stderr=str(err.relative_to(P)),stdout_sha256=sha(out),stderr_sha256=sha(err),source_sha256=sha(B/'src/zset_btree.c'));rows.append(row);(P/'faults.json').write_text(json.dumps(rows,indent=2)+'\n')
  if step=='build':assert rc==0
  else:assert rc==-6 and 'Assertion failed' in err.read_text(),(rc,err.read_text())
print('Both C faults detected by aborting model assertions')
