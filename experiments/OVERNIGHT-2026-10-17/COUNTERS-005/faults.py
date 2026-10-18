from pathlib import Path
import json,hashlib,shutil,subprocess,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());S=R/M['snapshot'];D=R/'scratch/overnight-counters-005/faults';D.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
for name,old,new,needle in [('no-reversal','        zbtScoreLeafReverseForPop(leaf);','        (void)leaf;','leaves==1 && reversed==(trimmed?n:0)'),('zero-sign','if (score) *score = zbtScoreLeafScore(leaf, pos);','if (score) *score = fabs(zbtScoreLeafScore(leaf, pos));','score_bits(score) == score_bits(model_score')]:
 B=D/name;B.mkdir()
 for n,h in M['sources'].items():
  src=S/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 p=B/'src/zset_btree.c';s=p.read_text();assert s.count(old)==1;s=s.replace(old,new);p.write_text(s)
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-O1','-g','-DREDIS_DEBUG','-fno-omit-frame-pointer','bench/census.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','fault']
 q=subprocess.run(cmd,cwd=B,capture_output=True,text=True,timeout=120)
 for k in ['stdout','stderr']:(P/f'fault-{name}-build.{k}').write_text(getattr(q,k))
 assert q.returncode==0
 args=['./fault','31','16','31101','alternating-zero','trimmed'];r=subprocess.run(args,cwd=B,capture_output=True,text=True,timeout=30)
 for k in ['stdout','stderr']:(P/f'fault-{name}.{k}').write_text(getattr(r,k))
 row=dict(name=name,build_command=cmd,run_command=args,returncode=r.returncode,source_sha256=sha(p),binary_sha256=sha(B/'fault'),detected=r.returncode==-6 and needle in r.stderr,stdout_sha256=sha(P/f'fault-{name}.stdout'),stderr_sha256=sha(P/f'fault-{name}.stderr'),stderr=r.stderr);rows.append(row);(P/'faults.json').write_text(json.dumps(rows,indent=2)+'\n');assert row['detected']
print('2 structural/exact-bit sensitivity faults detected')
