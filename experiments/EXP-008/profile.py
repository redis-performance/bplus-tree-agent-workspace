#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,hashlib,sys,argparse
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('variant',choices=('base','A','B','C'));parser.add_argument('--out-dir',default='experiments/EXP-008/profile-results');a=parser.parse_args()
v=a.variant;out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);binary=Path('build/exp008')/v/'decoder-bench'
cmd=[str(binary),'--width','60','--count','16','--leaves','8','--rounds','65536','--samples','64','--warmup','16','--seed','81031']
with (out/(v+'-profile.csv')).open('w') as so,(out/(v+'-profile.stderr')).open('w') as se:
 child=subprocess.Popen(cmd,stdout=so,stderr=se);sampler=['/usr/bin/sample',str(child.pid),'1','1','-file',str(out/(v+'-sample.txt'))]
 p=subprocess.run(sampler,capture_output=True,text=True,timeout=10);rc=child.wait(timeout=20)
record=dict(sampler_returncode=p.returncode,sampler_stderr=p.stderr,binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),command=cmd,sampler_command=sampler,child_returncode=rc,scope='Whole process including setup and warmup; excluded from timing matrix')
(out/(v+'-sampling.json')).write_text(json.dumps(record,indent=2)+'\n');print(v,p.returncode,rc)
