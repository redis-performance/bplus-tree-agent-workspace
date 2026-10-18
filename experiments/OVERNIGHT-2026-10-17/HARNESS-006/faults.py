from pathlib import Path
import json,subprocess,hashlib,time,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-harness-006/base';D=R/'scratch/overnight-harness-006/faults';D.mkdir();source=(S/'src/zset_btree.c').read_text();start=source.index('int zbtreeIteratorNext(');end=source.index('/* Return the rank where a score bound',start);body=source[start:end];rows=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,old,new,mask,direction in [('length','if (len) *len = elelen;','if (len) *len = elelen + 1;',2,'forward'),('zero-sign','if (score) *score = zbtScoreLeafScore(leaf, pos);','if (score) *score = fabs(zbtScoreLeafScore(leaf, pos));',4,'forward'),('state','iter->pos--;','iter->pos = 0;',0,'reverse')]:
 assert old in body;C=D/(name+'.c');C.write_text(source[:start]+body.replace(old,new,1)+source[end:]);B=D/name
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all','-g','-fno-omit-frame-pointer','bench/iterator_modes.c','../faults/'+C.name,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o','../faults/'+B.name]
 build=subprocess.run(cmd,cwd=S,capture_output=True,text=True,timeout=120)
 for k in ['stdout','stderr']:(P/'validation'/f'fault-{name}-build.{k}').write_text(getattr(build,k))
 assert build.returncode==0
 args=['../faults/'+B.name,'--size','95','--ops','191','--mask',str(mask),'--direction',direction,'--encoding','alternating-zero','--construction','trimmed']
 q=subprocess.run(args,cwd=S,capture_output=True,text=True,timeout=30)
 for k in ['stdout','stderr']:(P/'validation'/f'fault-{name}.{k}').write_text(getattr(q,k))
 rows.append(dict(name=name,build_command=cmd,run_command=args,returncode=q.returncode,source_sha256=sha(C),binary_sha256=sha(B),detected=q.returncode!=0,stderr=q.stderr));(P/'faults.json').write_text(json.dumps(rows,indent=2)+'\n');assert q.returncode==-6 and 'bench/iterator_modes.c:' in q.stderr,name
print('3 referee sensitivity faults detected')
