from pathlib import Path
import json,subprocess,hashlib,shutil,time
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-harness-004/base';D=R/'scratch/overnight-harness-004/faults';D.mkdir();source=(S/'src/zset_btree.c').read_text();start=source.index('int zbtreeIteratorNext(');end=source.index('/* Return the rank where a score bound',start);body=source[start:end];rows=[]
for name,old,new,mask,direction in [('length','if (len) *len = elelen;','if (len) *len = elelen + 1;',2,'forward'),('score','if (score) *score = zbtScoreLeafScore(leaf, pos);','if (score) *score = zbtScoreLeafScore(leaf, pos) + 1.0;',4,'forward'),('state','iter->pos--;','iter->pos = 0;',0,'reverse')]:
 assert old in body;C=D/(name+'.c');C.write_text(source[:start]+body.replace(old,new,1)+source[end:]);B=D/name
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-O1','-g','-fno-omit-frame-pointer','bench/iterator_modes.c',str(C),'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',str(B)]
 build=subprocess.run(cmd,cwd=S,capture_output=True,text=True,timeout=120);(P/'validation'/f'fault-{name}-build.stdout').write_text(build.stdout);(P/'validation'/f'fault-{name}-build.stderr').write_text(build.stderr);assert build.returncode==0
 args=[str(B),'--size','129','--ops','259','--mask',str(mask),'--direction',direction,'--encoding','fraction']
 q=subprocess.run(args,cwd=S,capture_output=True,text=True,timeout=30);(P/'validation'/f'fault-{name}.stdout').write_text(q.stdout);(P/'validation'/f'fault-{name}.stderr').write_text(q.stderr)
 rows.append(dict(name=name,build_command=cmd,run_command=args,returncode=q.returncode,source_sha256=hashlib.sha256(C.read_bytes()).hexdigest(),detected=q.returncode!=0,stderr=q.stderr));(P/'faults.json').write_text(json.dumps(rows,indent=2)+'\n');assert q.returncode!=0,name
print('3 harness sensitivity faults detected')
