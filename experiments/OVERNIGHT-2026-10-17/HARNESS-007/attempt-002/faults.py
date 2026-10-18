from pathlib import Path
import csv,datetime,difflib,hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[3];F=json.loads((P/'freeze.json').read_text());assert json.loads((P/'validation.json').read_text())['status']=='complete'
D=P/'faults';D.mkdir();S=R/'scratch/overnight-harness-007-faults';S.mkdir();base=R/F['snapshot'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
original=(base/'bench/batch_lookup.c').read_text()
for name,a,b,field in [('effective-count','batch,ops,r.calls','batch,ops+1,r.calls','operations'),('query-fingerprint','warmups,we,cfp,qfp,','warmups,we,cfp,qfp^1,','query_fingerprint'),('checksum','owned,r.checksum,ts','owned,r.checksum+1,ts','checksum')]:
 assert original.count(a)==1;changed=original.replace(a,b);B=S/name;B.mkdir()
 for n,h in F['files'].items():
  src=base/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 (B/'bench/batch_lookup.c').write_text(changed);(B/'build').mkdir();(D/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/bench/batch_lookup.c',tofile='b/bench/batch_lookup.c')))
 row=dict(name=name,field=field,snapshot=str(B.relative_to(R)),source_sha256=sha(B/'bench/batch_lookup.c'),runs=[])
 args=['--size','1','--ops','4','--member-bytes','320','--batch-size','3','--layout','mixed','--seed','80603','--query-seed','80611','--warmup-passes','2']
 build=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O3','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG','bench/batch_lookup.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/fault']
 for stage,cmd in [('build',build),('run',['build/fault',*args])]:
  tag=name+'-'+stage;r=dict(name=tag,stage=stage,command=cmd,cwd=str(B.relative_to(R)),started_utc=utc());out=D/(tag+'.stdout');err=D/(tag+'.stderr')
  with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=B,stdout=o,stderr=e,timeout=120).returncode
  r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));row['runs'].append(r);assert rc==0
 result=next(csv.DictReader(out.open()));expected={'operations':4,'checksum':2,'query_fingerprint':12638153115695167455}
 row.update(detected=int(result[field])!=expected[field],actual=int(result[field]),expected=expected[field],binary_sha256=sha(B/'build/fault'));rows.append(row);(D/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n');assert row['detected'];print(name,'DETECTED',flush=True)
(D/'summary.json').write_text(json.dumps(dict(status='pass',detected=len(rows)),indent=2)+'\n')
