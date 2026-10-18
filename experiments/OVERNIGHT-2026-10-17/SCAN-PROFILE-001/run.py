#!/usr/bin/env python3
"""One serial scan profile, excluded from all timing controls."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
binary = ROOT / "scratch/overnight-aa-001/base/build/btree-bench"
raw = ROOT / "scratch/overnight-scan-profile-001/scan.sample.txt"
args = ["--case", "scan", "--size", "100000", "--ops", "100000000",
        "--member-bytes", "16", "--seed", "1", "--warmup-passes", "10"]
with (HERE / "scan.csv").open("x") as out, (HERE / "scan.stderr").open("x") as err:
    proc = subprocess.Popen([str(binary), *args], stdout=out, stderr=err)
    try:
        time.sleep(1)
        sampled = subprocess.run(["sample", str(proc.pid), "5", "1", "-mayDie", "-file", str(raw)], capture_output=True, text=True, timeout=25)
        rc = proc.wait(timeout=90)
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()
report = raw.read_text() if raw.exists() else sampled.stdout + sampled.stderr
if "Call graph:" in report:
    report = "Call graph:" + report.split("Call graph:", 1)[1].split("Binary Images:", 1)[0]
report = report.replace(str(ROOT), "<workspace>")
report = re.sub(r"/Users/[^/\s]+", "<user-home>", report)
(HERE / "scan.sample.txt").write_text(report.rstrip() + "\n")
(HERE / "manifest.json").write_text(json.dumps({"args": args, "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest(),
    "sample_command": ["sample", "<own-child-pid>", "5", "1", "-mayDie", "-file", "<scratch-raw>"],
    "delay_seconds": 1, "sample_returncode": sampled.returncode, "benchmark_returncode": rc,
    "raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest() if raw.exists() else None,
    "scope": "whole process sampled; no timed-loop markers; profile timings excluded from A/A"}, indent=2) + "\n")
print(f"sample={sampled.returncode} benchmark={rc}")
