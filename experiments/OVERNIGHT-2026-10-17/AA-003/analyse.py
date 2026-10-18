#!/usr/bin/env python3
"""Preregistered A/A wall-time precision analysis with scheduling diagnostics."""
import csv
import hashlib
import json
import math
from pathlib import Path
import statistics as st

HERE = Path(__file__).resolve().parent
m = json.loads((HERE / "manifest.json").read_text())
results = []
for cell, case, size, ops in m["cells"]:
    rows = []
    failures = []
    for run in m["runs"]:
        if run["cell"] != cell:
            continue
        for field in ("csv", "stderr"):
            assert hashlib.sha256((HERE / run[field]).read_bytes()).hexdigest() == run[field + "_sha256"]
        if run["returncode"] != 0:
            failures.append(run)
            continue
        for row in csv.DictReader((HERE / run["csv"]).open()):
            row.update(block=run["block"], label=run["label"])
            rows.append(row)
    if not rows:
        results.append({"cell": cell, "rows": 0, "qualified": False, "failures": failures})
        continue
    def ns(r):
        return int(r["elapsed_ns"]) / int(r["operations"])
    effects = []
    for block in range(1, 7):
        ab = {label: [ns(r) for r in rows if r["block"] == block and r["label"] == label] for label in "AB"}
        if all(len(x) == 2 for x in ab.values()):
            effects.append(100 * (st.mean(ab["B"]) / st.mean(ab["A"]) - 1))
    mean = st.mean(effects) if effects else None
    half = 2.5705818366147395 * st.stdev(effects) / math.sqrt(6) if len(effects) == 6 else None
    lo, hi = (mean-half, mean+half) if half is not None else (None, None)
    invariant = all(len({r[k] for r in rows}) == 1 for k in ("checksum", "operations", "tree_bytes", "construction_fingerprint", "query_fingerprint", "query_seed", "query_order"))
    expected_checksum = (ops//100000)*100000*99999//2 if case=='lookup-hit' else 0
    invariant &= all(int(r['operations'])==ops and int(r['checksum'])==expected_checksum and int(r['seed'])==503 and r['query_order']=='independent' and r['query_seed']=='701' and int(r['size'])==100000 and int(r['member_bytes'])==size for r in rows)
    shortest = min(int(r["elapsed_ns"]) for r in rows)
    good = len(rows) == 24 and not failures and invariant and half is not None and lo >= -1 and hi <= 1 and shortest >= 10000000
    values = [ns(r) for r in rows]
    shares = [int(r["thread_elapsed_ns"]) / int(r["elapsed_ns"]) for r in rows if int(r["thread_elapsed_ns"]) >= 0 and int(r["elapsed_ns"]) > 0]
    results.append({"cell": cell, "case": case, "rows": len(rows), "failures": failures,
                    "qualified": good, "invariants_stable": invariant,
                    "median_ns_op": st.median(values), "min_ns_op": min(values), "max_ns_op": max(values),
                    "cv_pct": 100*st.stdev(values)/st.mean(values) if len(values)>1 else None,
                    "block_effects_pct": effects, "aa_mean_pct": mean, "ci95_low_pct": lo, "ci95_high_pct": hi,
                    "min_wall_ms": shortest/1e6,
                    "thread_wall_ratio_min": min(shares) if shares else None,
                    "thread_wall_ratio_median": st.median(shares) if shares else None,
                    "thread_wall_ratio_max": max(shares) if shares else None,
                    "boundary_cpu_ids": sorted({int(r[k]) for r in rows for k in ("cpu_start", "cpu_end")}),
                    "different_boundary_ids": sum(r["cpu_start"] != r["cpu_end"] for r in rows),
                    "qos_reported": sorted({r[k] for r in rows for k in ("qos_reported_start", "qos_reported_end")}),
                    "tree_bytes": sorted({int(r["tree_bytes"]) for r in rows}),
                    "checksums": sorted({int(r["checksum"]) for r in rows}),
                    "operations": sorted({int(r["operations"]) for r in rows})})
(HERE / "summary.json").write_text(json.dumps(results, indent=2) + "\n")
lines = ["# AA-003 descriptive control results", "", "Wall time is primary; identical executable A/B.",
         "No rows removed. 95% Student-t intervals across six ABBA block effects (df=5); independence/normality assumed.",
         "These are local precision controls, not speedups. Frequency/effective QoS and within-window residency unknown.", "",
         "| Cell | Rows | B/A mean % [95% interval] | Min wall ms | CPU/wall min–max | Boundary IDs differ | Qualified |",
         "|---|---:|---|---:|---|---:|---|"]
for r in results:
    if not r["rows"]:
        lines.append(f"| {r['cell']} | 0 | incomplete | — | — | — | no |")
        continue
    interval = f"{r['aa_mean_pct']:+.3f} [{r['ci95_low_pct']:+.3f}, {r['ci95_high_pct']:+.3f}]" if r["ci95_low_pct"] is not None else "incomplete"
    ratio = f"{r['thread_wall_ratio_min']:.4f}–{r['thread_wall_ratio_max']:.4f}" if r["thread_wall_ratio_min"] is not None else "unknown"
    lines.append(f"| {r['cell']} | {r['rows']} | {interval} | {r['min_wall_ms']:.1f} | {ratio} | {r['different_boundary_ids']} | {'yes' if r['qualified'] else 'no'} |")
(HERE / "SUMMARY.md").write_text("\n".join(lines) + "\n")
print(json.dumps({"status": m["status"], "processes": len(m["runs"]), "qualified": sum(r["qualified"] for r in results), "cells": len(results)}, indent=2))
