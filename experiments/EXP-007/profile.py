#!/usr/bin/env python3
"""Bounded external sampling of the actual release binary; no timing claims."""
from pathlib import Path
import subprocess,json,hashlib,sys
v=sys.argv[1];assert v in ('base','A','B','C')
out=Path('experiments/EXP-007/profile-results');binary=Path('build/exp007')/v/'decoder-bench'
cmd=[str(binary),'--width','60','--count','96','--leaves','8','--rounds','65536','--samples','64','--warmup','16','--seed','81031']
with (out/(v+'-profile.csv')).open('w') as so,(out/(v+'-profile.stderr')).open('w') as se:
    child=subprocess.Popen(cmd,stdout=so,stderr=se)
    samplecmd=['/usr/bin/sample',str(child.pid),'1','1','-file',str(out/(v+'-sample.txt'))]
    try:
        p=subprocess.run(samplecmd,capture_output=True,text=True,timeout=10)
        record=dict(sample_returncode=p.returncode,stdout=p.stdout,stderr=p.stderr)
        childrc=child.wait(timeout=20)
    except BaseException:
        child.kill();child.wait();raise
record.update(binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),command=cmd,sampler_command=samplecmd,child_returncode=childrc,scope='Whole process including warmup; profiled timing rows excluded from comparison')
(out/(v+'-sampling.json')).write_text(json.dumps(record,indent=2)+'\n')
print(v,'sampler',p.returncode,'child',childrc)
