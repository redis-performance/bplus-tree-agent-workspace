from pathlib import Path
import json,hashlib,shutil,subprocess,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());base=R/M['snapshot'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
original=(base/'src/zset_btree.c').read_text();a=original.index('static double zbtScoreLeafScore(');b=original.index('/* Return the raw hash byte',a);body=original[a:b]
replacements={'missing-ninth-byte':('if (shift && bits > 64 - shift)','if (0 && shift && bits > 64 - shift)'), 'width64-mask':('if (bits < 64)\n            delta &= (UINT64_C(1) << bits) - 1;','if (bits == 64) delta &= UINT64_C(0x7fffffffffffffff);\n        else delta &= (UINT64_C(1) << bits) - 1;')}
for name,(old,new) in replacements.items():
 assert body.count(old)==1;S=base.parent/name;assert not S.exists();shutil.copytree(base,S,ignore=shutil.ignore_patterns('build'));(S/'build').mkdir();changed=original[:a]+body.replace(old,new)+original[b:];(S/'src/zset_btree.c').write_text(changed);(P/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/packed_decode_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
 row=dict(name=name,snapshot=str(S.relative_to(R)),source_sha256=sha(S/'src/zset_btree.c'),commands=[])
 for stage,command in [('build',cmd),('run',['build/fault'])]:
  prefix=name+'-'+stage
  with (P/(prefix+'.stdout')).open('w') as so,(P/(prefix+'.stderr')).open('w') as se:
   try:q=subprocess.run(command,cwd=S,stdout=so,stderr=se,timeout=120);rc=q.returncode
   except subprocess.TimeoutExpired:rc='timeout'
  row['commands'].append(dict(command=command,returncode=rc,stdout_sha256=sha(P/(prefix+'.stdout')),stderr_sha256=sha(P/(prefix+'.stderr'))))
  assert (rc==0 if stage=='build' else isinstance(rc,int) and rc!=0)
  if stage=='run':assert 'actual=' in (P/(prefix+'.stderr')).read_text() and 'expected=' in (P/(prefix+'.stderr')).read_text();row['detected']=True
 rows.append(row);(P/'faults.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,'DETECTED',flush=True)
