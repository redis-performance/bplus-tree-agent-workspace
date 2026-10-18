#!/usr/bin/env python3
"""Fixed serial schedule from PLAN.md. Refuses to overwrite its manifest."""
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import subprocess
import time
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BINARY = ROOT / "scratch/overnight-harness-003/base/build/release/btree-bench"
CELLS = [("hit16", "lookup-hit", 16, 20000000),
         ("miss16", "lookup-miss", 16, 20000000),
         ("hit320", "lookup-hit", 320, 5000000),
         ("miss320", "lookup-miss", 320, 5000000)]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def utc():
    return datetime.now(timezone.utc).isoformat()

def save():
    tmp = HERE / "manifest.tmp"
    tmp.write_text(json.dumps(manifest, indent=2) + "\n")
    tmp.replace(HERE / "manifest.json")

def run(cell, block, step, label, warmup=False):
    name, case, size, ops = cell
    args = ["--case", case, "--size", "100000", "--ops", str(ops),
            "--member-bytes", str(size), "--seed", "2503", "--warmup-passes", "10", "--query-order", "independent", "--query-seed", "2707"]
    prefix = "warmup" if warmup else f"{name}-block{block}-step{step}-{label}"
    row = {"cell": name, "block": block, "step": step, "label": label,
           "args": args, "started_utc": utc(), "load_before": os.getloadavg(),
           "csv": f"raw/{prefix}.csv", "stderr": f"raw/{prefix}.stderr"}
    begin = time.monotonic()
    with (HERE / row["csv"]).open("w") as stdout, (HERE / row["stderr"]).open("w") as stderr:
        try:
            p = subprocess.run([str(BINARY.relative_to(ROOT)), *args], cwd=ROOT, stdout=stdout, stderr=stderr, timeout=120 if warmup else min(120,max(0.01,600-(time.monotonic()-start))))
            row["returncode"] = p.returncode
        except subprocess.TimeoutExpired:
            row["returncode"] = "timeout"
    row.update(elapsed_seconds=time.monotonic()-begin, ended_utc=utc(), load_after=os.getloadavg())
    row["csv_sha256"] = sha(HERE / row["csv"])
    row["stderr_sha256"] = sha(HERE / row["stderr"])
    if row["returncode"] == 0:
        rows = list(csv.DictReader(io.StringIO((HERE / row["csv"]).read_text())))
        if len(rows) != 1 or rows[0]["case"] != case:
            row["returncode"] = "invalid-output"
    manifest["warmup" if warmup else "runs"].append(row)
    save()
    return row["returncode"] == 0

if (HERE / "manifest.json").exists():
    raise SystemExit("Refusing to overwrite existing evidence")
(HERE / "raw").mkdir()
freeze = json.loads((HERE.parent / "HARNESS-003/freeze.json").read_text())
snapshot = ROOT / freeze["snapshot"]
for name, digest in freeze["files"].items():
    assert sha(snapshot / name) == digest, name
manifest = {"started_utc": utc(), "status": "running", "binary_sha256": sha(BINARY),
            "binary": str(BINARY.relative_to(ROOT)), "base_commit": freeze["base_commit"],
            "provenance": freeze["provenance"], "plan_sha256": sha(HERE / "PLAN.md"),
            "runner_sha256": sha(Path(__file__)), "freeze_sha256": sha(HERE.parent / "HARNESS-003/freeze.json"),
            "system": platform.system(), "release": platform.release(), "arch": platform.machine(),
            "blocks": 6, "cells": CELLS, "warmup": [], "runs": []}
save()
ok = run(("hit16", "lookup-hit", 16, 1000000), 0, 0, "warmup", True)
start = time.monotonic()
for block in range(1, 7):
    if not ok:
        break
    offset = (block-1) % len(CELLS)
    cells = CELLS[offset:] + CELLS[:offset]
    for cell in cells:
        for step, label in enumerate("ABBA", 1):
            if time.monotonic() - start > 600:
                manifest["status"] = "budget-exhausted"
                ok = False
                break
            ok = run(cell, block, step, label)
            if not ok:
                manifest["status"] = "failed"
                break
        print(f"block {block} cell {cell[0]}: {len(manifest['runs'])}/96 rows; ok={ok}", flush=True)
        if not ok:
            break
manifest.update(ended_utc=utc(), elapsed_seconds=time.monotonic()-start,
                binary_sha256_after=sha(BINARY))
assert manifest["binary_sha256"] == manifest["binary_sha256_after"]
for name, digest in freeze["files"].items():
    assert sha(snapshot / name) == digest, name
if ok:
    manifest["status"] = "complete"
save()
print(manifest["status"], flush=True)
