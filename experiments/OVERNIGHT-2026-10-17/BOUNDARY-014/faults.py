from pathlib import Path
import json,hashlib,shutil,subprocess,difflib,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'attempt-002/manifest.json').read_text());base=R/M['snapshots']['control']['path'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
original=(base/'src/zset_btree.c').read_text()
a=original.index('static void zbtScoreLeafReverseForPop(');b=original.index('/* Delete one score-tree element',a);body=original[a:b]
old='''    uint64_t base = zbtScoreToOrdered(scores[0]);
    for (unsigned int i = 1; i < count; i++) {
        uint64_t ordered = zbtScoreToOrdered(scores[i]);
        if (ordered > base) base = ordered;
    }'''
assert body.count(old)==1
fault1=original[:a]+body.replace(old,'    uint64_t base = zbtScoreToOrdered(scores[count - 1]);')+original[b:]
a=original.index('static int zbtScoreUpdateInPlace(');b=original.index('{',a)+1
fault2=original[:b]+'\n    if (zbtScoreLeafScore(leaf, pos) == score) return 1;\n'+original[b:]
for name,changed in [('last-zero-base',fault1),('equal-zero-update',fault2)]:
 S=base.parent/name;assert not S.exists();shutil.copytree(base,S,ignore=shutil.ignore_patterns('build'));(S/'build').mkdir();(S/'src/zset_btree.c').write_text(changed);(P/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 row=dict(name=name,snapshot=str(S.relative_to(R)),source_sha256=sha(S/'src/zset_btree.c'),commands=[])
 command=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/zero_physical_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
 for stage,cmd in [('build',command),('run',['build/fault'])]:
  name2=name+'-'+stage
  with (P/(name2+'.stdout')).open('w') as so,(P/(name2+'.stderr')).open('w') as se:
   try:rc=subprocess.run(cmd,cwd=S,stdout=so,stderr=se,timeout=120).returncode
   except subprocess.TimeoutExpired:rc='timeout'
  row['commands'].append(dict(command=cmd,returncode=rc,stdout_sha256=sha(P/(name2+'.stdout')),stderr_sha256=sha(P/(name2+'.stderr'))))
  assert rc==0 if stage=='build' else isinstance(rc,int) and rc!=0
  if stage=='run':
   text=(P/(name2+'.stderr')).read_text();assert 'exact-score' in text or 'zbtScoreToOrdered(zbtScoreLeafScore(leaf, i))' in text;row['detected']=True
 rows.append(row);(P/'faults.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,'DETECTED',flush=True)
