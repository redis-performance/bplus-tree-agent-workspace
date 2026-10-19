set -eu
cd @REPO@
OUT=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode
mkdir -p "$OUT/validation-long"
for V in base root A B C; do
 for MODE in native sanitize; do
  python3 tests/test_decoder.py "$OUT/build-long/$V/decoder-$MODE" > "$OUT/validation-long/$V-$MODE.stdout" 2> "$OUT/validation-long/$V-$MODE.stderr"
 done
done
python3 - <<'PY'
from pathlib import Path
import subprocess,csv,json,time
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode');rows=[]
for v in ['base','root','A','B','C']:
 for mode in ['native','sanitize']:
  binary=str(p/'build-long'/v/('decoder-'+mode))
  for value,expected in [(65537,0),(100000000,0),(100000001,2)]:
   cmd=[binary,'--rounds',str(value),'--help'];start=time.time();r=subprocess.run(cmd,capture_output=True,text=True,timeout=30);end=time.time();rows.append(dict(command=cmd,expected=expected,actual=r.returncode,started=start,finished=end,stdout=r.stdout,stderr=r.stderr));assert r.returncode==expected
  cmd=[binary,'--width','60','--count','1','--leaves','1','--rounds','65537','--samples','1','--warmup','1'];start=time.time();r=subprocess.run(cmd,capture_output=True,text=True,timeout=30);end=time.time();rows.append(dict(command=cmd,expected=0,actual=r.returncode,started=start,finished=end,stdout=r.stdout,stderr=r.stderr));assert r.returncode==0
  row=list(csv.DictReader(r.stdout.splitlines()))[0];assert row['operations']=='65537'
(p/'validation-long/cap-boundary.json').write_text(json.dumps(rows,indent=2)+'\n');print('cap boundary checks',len(rows),'PASS')
PY
