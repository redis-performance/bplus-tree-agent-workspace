#!/usr/bin/env python3
"""Serial predeclared process/fixture reuse diagnostic."""
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SNAP = ROOT / "scratch/overnight-diag-001/base"
BINARY = SNAP / "build/btree-bench"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
utc = lambda: datetime.now(timezone.utc).isoformat()

def save():
    p = HERE / "manifest.tmp"
    p.write_text(json.dumps(m, indent=2) + "\n")
    p.replace(HERE / "manifest.json")

if (HERE / "manifest.json").exists():
    raise SystemExit("Refusing to overwrite results")
freeze = json.loads((HERE / "freeze.json").read_text())
for name, digest in freeze["files"].items():
    assert sha(SNAP / name) == digest
(HERE / "raw").mkdir()
m = {"started_utc": utc(), "status": "running", "binary_sha256": sha(BINARY),
     "plan_sha256": sha(HERE / "PLAN.md"), "runner_sha256": sha(Path(__file__)),
     "freeze_sha256": sha(HERE / "freeze.json"), "runs": []}
save()
start = time.monotonic()
ok = True
for block in range(1, 7):
    if not ok:
        break
    arms = ["fresh", "reuse"] if block % 2 else ["reuse", "fresh"]
    for arm in arms:
        if not ok:
            break
        for process in range(6 if arm == "fresh" else 1):
            if time.monotonic() - start > 240:
                m["status"] = "budget-exhausted"
                ok = False
                break
            samples = 1 if arm == "fresh" else 6
            args = ["--case", "lookup-hit", "--size", "100000", "--member-bytes", "16",
                    "--seed", "1", "--ops", "10000000", "--warmup-passes", "10", "--samples", str(samples)]
            name = f"block{block}-{arm}-{process}"
            row = {"block": block, "arm": arm, "process": process, "args": args,
                   "csv": f"raw/{name}.csv", "stderr": f"raw/{name}.stderr", "started_utc": utc(), "load_before": os.getloadavg()}
            with (HERE / row["csv"]).open("w") as out, (HERE / row["stderr"]).open("w") as err:
                try:
                    p = subprocess.run([str(BINARY), *args], stdout=out, stderr=err, timeout=120)
                    row["returncode"] = p.returncode
                except subprocess.TimeoutExpired:
                    row["returncode"] = "timeout"
            row.update(ended_utc=utc(), load_after=os.getloadavg(), csv_sha256=sha(HERE / row["csv"]), stderr_sha256=sha(HERE / row["stderr"]))
            if row["returncode"] == 0:
                rows = list(csv.DictReader(io.StringIO((HERE / row["csv"]).read_text())))
                if len(rows) != samples or [int(r["sample_index"]) for r in rows] != list(range(samples)):
                    row["returncode"] = "invalid-output"
            m["runs"].append(row)
            save()
            if row["returncode"] != 0:
                m["status"] = "failed"
                ok = False
                break
        print(f"block {block} {arm}: {len(m['runs'])}/42 processes; ok={ok}", flush=True)
for name, digest in freeze["files"].items():
    assert sha(SNAP / name) == digest
m.update(ended_utc=utc(), elapsed_seconds=time.monotonic()-start, binary_sha256_after=sha(BINARY))
assert m["binary_sha256"] == m["binary_sha256_after"]
if ok:
    m["status"] = "complete"
save()
print(m["status"], flush=True)
