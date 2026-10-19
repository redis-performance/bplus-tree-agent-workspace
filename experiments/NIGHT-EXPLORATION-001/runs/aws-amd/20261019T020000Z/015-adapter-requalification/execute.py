#!/usr/bin/env python3
"""One bounded corrected-adapter baseline, isolated from original timing checkout."""
import argparse,pathlib,json,subprocess,hashlib,datetime,os,sys
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);a=p.parse_args();checkout=a.checkout.resolve();here=pathlib.Path(__file__).resolve().parent;source=here/'source';assert not source.exists();expected=json.loads((here/'expected-inputs.json').read_text());commit=expected['commit'];now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();record={'started_utc':now(),'original_head_before':subprocess.check_output(['git','rev-parse','HEAD'],cwd=checkout,text=True).strip(),'inherited_affinity':sorted(os.sched_getaffinity(0))};assert record['inherited_affinity']==[2]
subprocess.run(['git','fetch','--no-tags','https://github.com/redis-performance/bplus-tree-agent-workspace.git',commit],cwd=checkout,check=True)
subprocess.run(['git','worktree','add','--detach',str(source),commit],cwd=checkout,check=True)
record['source_commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip();assert record['source_commit']==commit
hashes=lambda:{name:hashlib.sha256((source/name).read_bytes()).hexdigest() for name in expected['files']}
record['input_hashes_before']=hashes();assert record['input_hashes_before']==expected['files'];assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=checkout,text=True).strip()==record['original_head_before']
command=['python3','scripts/run-size-matrix.py','--build','build/adapter-requalification','--out','scratch/adapter-requalification-results','--ops','1000000','--member-bytes','16','--budget-seconds','1200'];record['command']=command;record['matrix_started_utc']=now();code=1
try:
 code=subprocess.run(command,cwd=source).returncode
finally:
 record['matrix_finished_utc']=now();record['returncode']=code;record['input_hashes_after']=hashes();record['original_head_after']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=checkout,text=True).strip();record['source_commit_after']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip();binary=source/'build/adapter-requalification/btree-bench';record['binary_sha256_after']=hashlib.sha256(binary.read_bytes()).hexdigest() if binary.exists() else None;out=source/'scratch/adapter-requalification-results';out.mkdir(parents=True,exist_ok=True);(out/'operational-provenance.json').write_text(json.dumps(record,indent=2)+'\n')
assert record['input_hashes_after']==expected['files'];assert record['original_head_before']==record['original_head_after'];assert record['source_commit_after']==commit
sys.exit(code)
