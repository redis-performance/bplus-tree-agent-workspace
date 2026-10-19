set -eu
cd @REPO@
out=scratch/amd-delete-offset-census
clang -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -Isrc -Icompat -Ivendor/redis "$out/census-bench.c" "$out/zset_btree.c" compat/standalone.c vendor/redis/siphash.c -lm -o "$out/census" > "$out/build.stdout" 2> "$out/build.stderr"
python3 - <<'PY'
from pathlib import Path
import subprocess,json,csv,datetime,os,hashlib
p=Path('scratch/amd-delete-offset-census');rows=[];records=[]
for i,(n,seed) in enumerate([(100000,1)]+[(n,s) for s in [1,2,3] for n in [100000,1000000]]):
 label=('disabled-' if i==0 else '')+f'delete-n{n}-s{seed}';env=os.environ.copy()
 if i==0:env['CENSUS_DISABLED']='1'
 cmd=[str(p/'census'),'--case','delete','--size',str(n),'--ops','1000000','--member-bytes','16','--seed',str(seed)];start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,env=env,capture_output=True,text=True,timeout=30)
 (p/(label+'.csv')).write_text(r.stdout);(p/(label+'.stderr')).write_text(r.stderr)
 records.append(dict(label=label,command=cmd,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
 counts=json.loads(r.stderr);row=list(csv.DictReader(r.stdout.splitlines()))[0];ref=list(csv.DictReader(Path(f'scratch/amd-delete-profile/delete-n{n}-s{seed}.csv').read_text().splitlines()))[0]
 for k in ['checksum','tree_bytes','operations','seed','size']:assert row[k]==ref[k],(label,k)
 if i==0:assert all(sum(x)==0 if isinstance(x,list) else x==0 for x in counts.values())
 rows.append(dict(label=label,size=n,seed=seed,counts=counts,checksum=row['checksum'],tree_bytes=row['tree_bytes'],operations=row['operations']))
(p/'summary.json').write_text(json.dumps(rows,indent=2)+'\n');(p/'hashes.json').write_text(json.dumps({f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in ['census','zset_btree.c','census-bench.c']},indent=2)+'\n')
PY
