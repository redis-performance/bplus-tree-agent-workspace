#!/usr/bin/env python3
"""Sample only our own benchmark children, serially, outside timing controls."""
import json
from pathlib import Path
import re
import subprocess
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SCRATCH=ROOT/"scratch/exp001"
CASES=[("hit-100k-16", "lookup-hit",100000,16,100000000),
       ("update-100k-16","update",100000,16,20000000),
       ("hit-100k-320","lookup-hit",100000,320,30000000),
       ("hit-1m-16","lookup-hit",1000000,16,30000000)]
manifest=[]
for name,case,n,size,ops in CASES:
    args=[str(ROOT/"build/btree-bench"),"--case",case,"--size",str(n),"--ops",str(ops),"--member-bytes",str(size),"--seed","1"]
    dest=HERE/"profiles"/name
    raw=SCRATCH/f"{name}.sample.txt"
    with dest.with_suffix(".csv").open("x") as out, dest.with_suffix(".stderr").open("x") as err:
        proc=subprocess.Popen(args,stdout=out,stderr=err)
        try:
            time.sleep(1)
            sampled=subprocess.run(["sample",str(proc.pid),"5","1","-mayDie","-file",str(raw)],capture_output=True,text=True,timeout=25)
            rc=proc.wait(timeout=60)
        finally:
            if proc.poll() is None:
                proc.terminate()
                try: proc.wait(timeout=5)
                except subprocess.TimeoutExpired: proc.kill(); proc.wait()
    report=raw.read_text() if raw.exists() else sampled.stdout+sampled.stderr
    # Keep stacks and flat counts, excluding machine identifiers and image paths.
    if "Call graph:" in report:
        report="Call graph:"+report.split("Call graph:",1)[1].split("Binary Images:",1)[0]
    report=report.replace(str(ROOT),"<workspace>")
    report=re.sub(r"/Users/[^/\s]+","<user-home>",report)
    dest.with_suffix(".sample.txt").write_text(report.rstrip()+"\n")
    manifest.append({"name":name,"args":args[1:],"sample_duration_seconds":5,"interval_ms":1,
        "delay_seconds":1,"sample_returncode":sampled.returncode,"benchmark_returncode":rc,
        "scope":"whole child process; setup/cleanup not instrumented out; timings excluded from controls"})
    (HERE/"profiles/manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(f"{name}: sample exit {sampled.returncode}, benchmark exit {rc}",flush=True)
