set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/010-scan-native
D=scratch/arm-scan-native/base
mkdir -p "$P/raw" "$D"
cat > "$P/run-aa.py" <<'FROZEN_FILE_EOF'
from pathlib import Path
import csv,datetime,json,subprocess,time
p=Path(__file__).parent;out=p/'aa.json';assert not out.exists();start=time.monotonic();m=dict(status='running',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=[])
for block in range(6):
 for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
  seed=101+block%3
  for position in range(4):
   assert time.monotonic()-start<300
   cmd=['scratch/arm-scan-native/base/build/btree-bench','--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed',str(seed)]
   t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(60,300-(time.monotonic()-start)));tag=f'aa-{len(m["rows"]):03d}'
   (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
   rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==1;row=rows[0];assert row['cpu_start']==row['cpu_end']=='2'
   m['rows'].append(dict(size=n,seed=seed,block=block,position=position,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=row));out.write_text(json.dumps(m,indent=2)+'\n')
effects=[]
for i in range(0,len(m['rows']),4):
 r=m['rows'][i:i+4];assert len({(x['row']['checksum'],x['row']['operations'],x['row']['tree_bytes']) for x in r})==1
 v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in r];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);minimum=min(int(x['row']['elapsed_ns']) for x in r)
 effects.append(dict(size=r[0]['size'],seed=r[0]['seed'],block=r[0]['block'],percent=effect,min_window_ns=minimum,qualified=abs(effect)<=1 and minimum>=10000000))
m.update(status='complete',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,effects=effects);out.write_text(json.dumps(m,indent=2)+'\n');print('PASS48 serial rows; qualification:',{n:all(x['qualified'] for x in effects if x['size']==n) for n in [100000,1000000]})
FROZEN_FILE_EOF
cat > "$P/audit-aa.py" <<'FROZEN_FILE_EOF'
from pathlib import Path
import csv,datetime,hashlib,json,statistics
p=Path(__file__).parent;m=json.loads((p/'aa.json').read_text());rows=m['rows'];expected=[]
for block in range(6):
 for size in ([100000,1000000] if block%2==0 else [1000000,100000]):
  for position in range(4):expected.append((size,101+block%3,block,position))
assert len(rows)<=48;last=None
for i,r in enumerate(rows):
 assert (r['size'],r['seed'],r['block'],r['position'])==expected[i]
 raw=list(csv.DictReader((p/'raw'/f'aa-{i:03d}.stdout').open()));assert raw==[r['row']]
 assert r['row']['cpu_start']==r['row']['cpu_end']=='2'
 assert r['row']['case']=='scan' and r['row']['requested_ops']=='5000000' and r['row']['member_bytes']=='16'
 start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert start<=end
 if last is not None:assert last<=start
 last=end
effects=[]
for i in range(0,len(rows)-3,4):
 r=rows[i:i+4];assert len({(x['row']['checksum'],x['row']['operations'],x['row']['tree_bytes']) for x in r})==1
 v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in r];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);minimum=min(int(x['row']['elapsed_ns']) for x in r)
 effects.append(dict(size=r[0]['size'],seed=r[0]['seed'],block=r[0]['block'],percent=effect,min_window_ns=minimum,qualified=abs(effect)<=1 and minimum>=10000000))
if m['status']=='complete':assert len(rows)==48 and effects==m['effects']
summary=[]
for size in [100000,1000000]:
 group=[x for x in effects if x['size']==size];values=[x['percent'] for x in group]
 if group:summary.append(dict(size=size,blocks=len(group),minimum=min(values),maximum=max(values),median=statistics.median(values),min_window_ns=min(x['min_window_ns'] for x in group),qualified=len(group)==6 and all(x['qualified'] for x in group),effects=values))
freeze=json.loads((p/'comparison-freeze.json').read_text());assert hashlib.sha256((p/'run-aa.py').read_bytes()).hexdigest()==freeze['aa_driver_sha256']
result=dict(status='pass',phase_status=m['status'],raw_rows=len(rows),complete_blocks=len(effects),partial_rows=len(rows)%4,serial_windows=True,fixture_identity=True,owned_bytes_equal=True,schedule_prefix_exact=True,summary=summary)
(p/'aa-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
FROZEN_FILE_EOF
git archive 8fab511e src compat vendor/redis bench Makefile | tar -x -C "$D"
make -C "$D" CC=clang BUILD=build OPT=-O3 build/btree-bench > "$P/build.stdout" 2> "$P/build.stderr"
clang --version > "$P/compiler.txt"
python3 - <<'FREEZE_PY'
from pathlib import Path
import hashlib,json
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/010-scan-native');d=Path('scratch/arm-scan-native/base')
f={'source_commit':'8fab511e0e6ec7d4808546cd50064c6bf299e695','build_command':'make CC=clang BUILD=build OPT=-O3 build/btree-bench','compiler':(p/'compiler.txt').read_text(),'sha256':{str(x.relative_to(d)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [d/'src/zset_btree.c',d/'src/zset_btree.h',d/'bench/microbench.c',d/'compat/standalone.c',d/'vendor/redis/siphash.c',d/'build/btree-bench']},'aa_driver_sha256':hashlib.sha256((p/'run-aa.py').read_bytes()).hexdigest(),'requested_ops':5000000,'sizes':[100000,1000000],'member_bytes':16,'seeds':[101,102,103,101,102,103],'blocks_per_size':6,'processes':48,'budget_seconds':300,'minimum_window_ns':10000000,'absolute_effect_limit_percent':1,'candidate_timing_started':False}
(p/'comparison-freeze.json').write_text(json.dumps(f,indent=2)+'\n')
FREEZE_PY
