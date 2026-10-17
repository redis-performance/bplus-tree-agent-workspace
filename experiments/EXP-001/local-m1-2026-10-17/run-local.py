#!/usr/bin/env python3
"""Run the preregistered serial A/A matrix; no candidate or source mutations."""
import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BINARY = ROOT / "build/btree-bench"
cells = [("n1k-b16",1000,16,1000000,"all"),
         ("n100k-b16",100000,16,1000000,"all"),
         ("n100k-b319",100000,319,1000000,"all"),
         ("n100k-b320",100000,320,1000000,"all"),
         ("n100k-b321",100000,321,1000000,"all"),
         ("n1m-b16-hit",1000000,16,10000000,"lookup-hit")]
def run_text(args):
    return subprocess.run(args,capture_output=True,text=True).stdout.strip()
manifest = {"utc_start":datetime.now(timezone.utc).isoformat(),
            "source_commit":run_text(["git","-C",str(ROOT),"rev-parse","HEAD"]),
            "binary_sha256":hashlib.sha256(BINARY.read_bytes()).hexdigest(),
            "compiler":run_text(["cc","--version"]).splitlines()[0],
            "flags":"-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 -lm",
            "cpu":run_text(["sysctl","-n","machdep.cpu.brand_string"]),
            "os":run_text(["sw_vers","-productVersion"]),
            "cores":"4P+4E; one benchmark thread; placement unobserved; no SMT",
            "frequency":"DVFS not controlled or measured; turbo state unknown",
            "affinity":"none; default inherited QoS, not verified",
            "allocator":"system libc usable-size adapter",
            "cells":cells,"blocks":6,"seed":1,"baseline":"A and B are same binary",
            "runs":[]}
path=HERE/"manifest.json"
if path.exists(): raise SystemExit("Refusing to overwrite existing matrix")
start=time.monotonic()
try:
    for block in range(1,7):
        ordered=cells[(block-1)%len(cells):]+cells[:(block-1)%len(cells)]
        for name,n,size,ops,case in ordered:
            for step,label in enumerate("ABBA",1):
                if time.monotonic()-start > 600: raise RuntimeError("Matrix budget exhausted")
                dest=HERE/"raw"/f"{name}-block{block}-step{step}-{label}.csv"
                args=[str(BINARY),"--size",str(n),"--ops",str(ops),"--member-bytes",str(size),"--seed","1","--case",case]
                rec={"cell":name,"block":block,"step":step,"label":label,
                     "load_before":os.getloadavg(),"utc":datetime.now(timezone.utc).isoformat()}
                begin=time.monotonic()
                with dest.open("x") as out, dest.with_suffix(".stderr").open("x") as err:
                    result=subprocess.run(args,stdout=out,stderr=err,timeout=90)
                rec.update(returncode=result.returncode,wall_seconds=time.monotonic()-begin,
                           load_after=os.getloadavg(),csv=dest.relative_to(HERE).as_posix())
                manifest["runs"].append(rec)
                if result.returncode: raise RuntimeError(f"{name}: exit {result.returncode}")
                rows=list(csv.DictReader(dest.open()))
                if len(rows)!=(8 if case=="all" else 1): raise RuntimeError("Missing benchmark rows")
                path.write_text(json.dumps(manifest,indent=2)+"\n")
            print(f"block {block}/6 {name}: PASS ({time.monotonic()-start:.1f}s elapsed)",flush=True)
    manifest["status"]="COMPLETE"
except BaseException as exc:
    manifest["status"]="INCOMPLETE"
    manifest["error"]=str(exc)
    raise
finally:
    manifest["elapsed_seconds"]=time.monotonic()-start
    manifest["utc_end"]=datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(manifest,indent=2)+"\n")
