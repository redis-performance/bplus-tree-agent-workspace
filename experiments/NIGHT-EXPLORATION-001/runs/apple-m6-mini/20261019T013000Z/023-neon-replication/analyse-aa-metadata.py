#!/usr/bin/env python3
"""Describe existing raw clock/endpoint metadata; never requalify the experiment."""
import csv
from fractions import Fraction
import hashlib
import json
from pathlib import Path

P = Path(__file__).resolve().parent
schedule = json.loads((P / "aa-schedule.json").read_text())
assert len(schedule) == 48
rows = []
raw_hashes = {}
for item in schedule:
    path = P / "aa/raw" / f'{item["index"]:03d}.stdout'
    raw_hashes[str(path.relative_to(P))] = hashlib.sha256(path.read_bytes()).hexdigest()
    parsed = list(csv.DictReader(path.read_text().splitlines()))
    assert len(parsed) == 1
    r = parsed[0]
    assert int(r["size"]) == item["size"] and int(r["seed"]) == item["seed"]
    assert int(r["thread_elapsed_ns"]) > 0
    rows.append((item, r))
blocks = []
for index in range(0, 48, 4):
    q = rows[index:index + 4]
    def paired(field):
        values = [int(r[field]) for _, r in q]
        a, b = values[0] + values[3], values[1] + values[2]
        return Fraction(100 * (b - a), a)
    wall, thread = paired("elapsed_ns"), paired("thread_elapsed_ns")
    blocks.append(dict(size=q[0][0]["size"], block=q[0][0]["block"], seed=q[0][0]["seed"],
                       wall_percent=float(wall), thread_clock_percent=float(thread),
                       wall_gate_qualified=abs(wall) <= 1,
                       cpu_endpoints=[[int(r["cpu_start"]), int(r["cpu_end"])] for _, r in q]))
output = dict(scope="Descriptive analysis of existing raw metadata only; no new workload",
              primary_clock="elapsed_ns; original wall-clock decision remains PARK",
              thread_clock_used_for_qualification=False,
              bracket="thread_start precedes wall_start; wall_end precedes thread_end in frozen microbench",
              limitations="Endpoints do not prove full residency or count migrations. No cycle, frequency, cache, preemption or causal attribution.",
              source_microbench_sha256="b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde",
              raw_hashes=raw_hashes, blocks=blocks,
              endpoint_pairs=sorted({(int(r["cpu_start"]), int(r["cpu_end"])) for _, r in rows}),
              runs_with_different_cpu_endpoints=sum(r["cpu_start"] != r["cpu_end"] for _, r in rows),
              qos_pairs=sorted({(r["qos_reported_start"], r["qos_reported_end"]) for _, r in rows}))
(P / "AA-METADATA-DIAGNOSIS.json").write_text(json.dumps(output, indent=2) + "\n")
lines = ["# Existing A/A clock and endpoint metadata", "",
         "No workload ran. The primary wall-clock decision remains PARK; thread time is descriptive and does not qualify or rescue any control.", "",
         "| Size | Block (zero-based) | Wall difference | Thread-clock difference |", "|---:|---:|---:|---:|"]
for b in blocks:
    lines.append(f'| {b["size"]:,} | {b["block"]} | {b["wall_percent"]:+.6f}% | {b["thread_clock_percent"]:+.6f}% |')
lines += ["", f'{output["runs_with_different_cpu_endpoints"]}/48 runs have different CPU endpoints. Observed IDs are 6 and 7; endpoints do not establish full residency or the number of migrations. Every QoS endpoint pair is user-interactive/user-interactive.', "",
          "The same two 1M blocks have thread-clock differences of −1.440359% and +1.587803%. The two clock brackets differ slightly, as documented in the frozen benchmark. These observations establish no frequency, cache, preemption or scheduler cause. No alternative metric gate, count change or retry is proposed.", ""]
(P / "AA-METADATA-DIAGNOSIS.md").write_text("\n".join(lines))
print(f'Described 48 existing rows / 12 blocks; {output["runs_with_different_cpu_endpoints"]} differing endpoint pairs; original PARK unchanged')
