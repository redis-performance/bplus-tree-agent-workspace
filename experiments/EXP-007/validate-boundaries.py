#!/usr/bin/env python3
import subprocess,json,pathlib
out=pathlib.Path('experiments/EXP-007/validation/boundary-bases.json');results=[]
for mode in ('exp007','exp007-sanitize'):
 for v in ('base','A','B','C'):
  for w in (0,8,58,59,60,61,62,63,64):
   for rev in (0,1):
    for shift in sorted({0,min(63,64-w)}):
     cmd=[f'build/{mode}/{v}/decoder-bench','--width',str(w),'--score-shift',str(shift),'--reversed',str(rev),'--count','7','--leaves','8','--samples','1','--rounds','1','--warmup','1']
     q=subprocess.run(cmd,capture_output=True,text=True,timeout=10)
     results.append(dict(command=cmd,returncode=q.returncode,stdout=q.stdout,stderr=q.stderr))
     if q.returncode:
      out.write_text(json.dumps(results,indent=2)+'\n');raise SystemExit('boundary validation failed')
out.write_text(json.dumps(results,indent=2)+'\n');print('PASS explicit boundary bases:',len(results),'commands')
