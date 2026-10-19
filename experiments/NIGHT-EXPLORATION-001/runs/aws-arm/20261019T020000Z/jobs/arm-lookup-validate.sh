set -eu
cd @REPO@
python3 - <<'PY'
import subprocess,json,time
from pathlib import Path
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup');out=p/'validation';out.mkdir(exist_ok=True);rows=[]
cells=[(n,16) for n in (100,1000,10000,100000,1000000)]+[(100000,k) for k in (8,319,320,321,1024)]
for binary in ('base','base-san'):
 for n,k in cells:
  for seed in (1,101):
   for case in ('lookup-hit','lookup-miss'):
    name=f'{binary}-n{n}-k{k}-s{seed}-{case}'
    cmd=[str(p/'build'/binary),'--size',str(n),'--ops','2001','--member-bytes',str(k),'--seed',str(seed),'--case',case]
    start=time.time();r=subprocess.run(cmd,capture_output=True,text=True,timeout=60);stop=time.time()
    (out/(name+'.csv')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr)
    rows.append(dict(name=name,command=cmd,start=start,stop=stop,returncode=r.returncode))
    (out/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
    if r.returncode:raise SystemExit(r.returncode)
print('passed',len(rows))
PY
