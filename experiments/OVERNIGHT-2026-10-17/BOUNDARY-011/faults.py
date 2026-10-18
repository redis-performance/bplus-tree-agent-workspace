from pathlib import Path
import json,hashlib,shutil,subprocess,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'manifest.json').read_text());B=R/F['snapshot'];S=B.parent
assert not (P/'faults.json').exists();records=[];original=(B/'src/zset_btree.c').read_text()
start=original.index('zbtreeSet *zbtreeDup(');end=original.index('/* Free the score tree',start)
faults=[('omit-active-resize',original[:start]+original[start:end].replace('if (source->member_rehash) {','if (0 && source->member_rehash) {')+original[end:],'!!a->member_rehash==!!b->member_rehash'),('shallow-external',original.replace('unsigned char *newptr = zbtAlloc(dst, len);','unsigned char *newptr = oldptr;'),'oa->ptr[i]!=ob->ptr[j]')]
for name,changed,expected in faults:
 assert changed!=original;D=S/name;assert not D.exists();D.mkdir()
 for path,h in F['sources'].items():
  src=B/path;assert hashlib.sha256(src.read_bytes()).hexdigest()==h;dst=D/path;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 (D/'src/zset_btree.c').write_text(changed);(P/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 commands=[('build',['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O3','-Wall','-Wextra','-DREDIS_DEBUG','tests/clone_resize_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','fault-test']),('run',['./fault-test'])]
 for step,cmd in commands:
  out=P/f'{name}-{step}.stdout';err=P/f'{name}-{step}.stderr'
  with out.open('w') as so,err.open('w') as se:
   try:p=subprocess.run(cmd,cwd=D,stdout=so,stderr=se,timeout=120);code=p.returncode
   except subprocess.TimeoutExpired:code='timeout'
  row=dict(fault=name,step=step,command=cmd,cwd=str(D.relative_to(R)),returncode=code,stdout=out.name,stderr=err.name,stdout_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),stderr_sha256=hashlib.sha256(err.read_bytes()).hexdigest(),source_sha256=hashlib.sha256((D/'src/zset_btree.c').read_bytes()).hexdigest())
  records.append(row);(P/'faults.json').write_text(json.dumps(records,indent=2)+'\n')
  assert code==0 if step=='build' else isinstance(code,int) and code!=0
  if step=='run':assert expected in err.read_text()
  print(name,step,code,flush=True)
