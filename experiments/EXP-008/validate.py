#!/usr/bin/env python3
import subprocess,json,pathlib
out=pathlib.Path('experiments/EXP-008/validation/boundary-matrix.json');results=[]
widths=range(65);counts=(1,2,4,7,8,16,32,96)
for mode in ('exp008','exp008-sanitize'):
 for v in ('base','A','B','C'):
  for w in widths:
   for rev in (0,1):
    for count in counts:
     shifts=sorted({0,min(63,64-w)})
     for shift in shifts:
      cmd=[f'build/{mode}/{v}/decoder-bench','--width',str(w),'--score-shift',str(shift),'--reversed',str(rev),'--count',str(count),'--leaves','8','--samples','1','--rounds','1','--warmup','1']
      q=subprocess.run(cmd,capture_output=True,text=True,timeout=10)
      results.append(dict(command=cmd,returncode=q.returncode,stderr=q.stderr))
      if q.returncode:
       out.write_text(json.dumps(results,indent=2)+'\n');raise SystemExit(f'validation failed: {cmd}: {q.stderr}')
out.write_text(json.dumps(results,indent=2)+'\n');print('PASS:',len(results),'width/direction/count/shift native+sanitizer cells')
