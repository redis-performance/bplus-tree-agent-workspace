from pathlib import Path
import datetime,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1];F=json.loads((P/'freeze.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
for v in ['control','A','B','C']:
 B=R/F['snapshot_root']/v;out=P/'profile-results'/(v+'-assembly-build.stdout');err=P/'profile-results'/(v+'-assembly-build.stderr');cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O3','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG','-S','src/zset_btree.c','-o','build/source.s'];r=dict(variant=v,command=cmd,cwd=str(B.relative_to(R)),started_utc=utc())
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=B,stdout=o,stderr=e,timeout=120).returncode
 r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err),assembly_sha256=sha(B/'build/source.s'),assembly=str((B/'build/source.s').relative_to(R)));assert rc==0
 s=(B/'build/source.s').read_text();start=s.index('_zbtScoreLeafFindMember:');end=s.index('.cfi_endproc',start);body=s[start:end];calls=re.findall(r'\bbl\s+(_\w+)',body);r['leaf_calls']=calls;r['memchr_calls']=sum(x=='_memchr' for x in calls)
 (P/'profile-results'/(v+'-leaf-assembly.txt')).write_text(body+'\n');r['leaf_assembly_sha256']=sha(P/'profile-results'/(v+'-leaf-assembly.txt'));rows.append(r)
 assert r['memchr_calls']==(1 if v=='control' else 0)
(P/'profile-results/codegen.json').write_text(json.dumps(rows,indent=2)+'\n');print('codegen: control memchr call present; all three candidate calls absent')
