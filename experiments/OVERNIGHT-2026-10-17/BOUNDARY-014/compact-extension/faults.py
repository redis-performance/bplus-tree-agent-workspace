from pathlib import Path
import json,hashlib,shutil,subprocess,datetime
P=Path(__file__).resolve().parent;R=P.parents[3];M=json.loads((P/'manifest.json').read_text());base=R/M['snapshots']['control']['path'];old=json.loads((P.parent/'faults.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
for previous in old:
 name=previous['name'];B=base.parent/name;B.mkdir()
 for n,h in M['snapshots']['control']['files'].items():
  src=base/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 src=R/previous['snapshot']/'src/zset_btree.c';assert sha(src)==previous['source_sha256'];shutil.copy2(src,B/'src/zset_btree.c');(B/'build').mkdir()
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all','tests/compact_zero.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault'];r=dict(name=name,snapshot=str(B.relative_to(R)),source_sha256=sha(B/'src/zset_btree.c'),commands=[])
 for stage,args in [('build',cmd),('run',['build/fault'])]:
  started=utc();out=P/f'fault-{name}-{stage}.stdout';err=P/f'fault-{name}-{stage}.stderr'
  with out.open('w') as so,err.open('w') as se:
   try:rc=subprocess.run(args,cwd=B,stdout=so,stderr=se,timeout=120).returncode
   except subprocess.TimeoutExpired:rc='timeout'
  r['commands'].append(dict(stage=stage,command=args,returncode=rc,started_utc=started,ended_utc=utc(),stdout=str(out.relative_to(P)),stderr=str(err.relative_to(P)),stdout_sha256=sha(out),stderr_sha256=sha(err)))
  assert rc==0 if stage=='build' else isinstance(rc,int) and rc!=0
  if stage=='run':
   s=err.read_text();assert 'exact-score' in s or 'zbtScoreToOrdered(zbtScoreLeafScore(leaf, i))' in s;r['detected']=True;r['binary_sha256']=sha(B/'build/fault')
 rows.append(r);(P/'faults.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,'DETECTED',flush=True)
