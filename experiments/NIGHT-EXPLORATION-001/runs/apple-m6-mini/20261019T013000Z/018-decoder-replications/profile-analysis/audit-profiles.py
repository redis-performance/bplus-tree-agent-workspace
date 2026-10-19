#!/usr/bin/env python3
"""Read-only audit of existing canonical private profiles; no subprocesses."""
import csv
import hashlib
import json
from pathlib import Path
import re

OUT = Path(__file__).resolve().parent
BASE = OUT.parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


captures = json.loads((BASE / "PROFILE-CAPTURE.json").read_text())
results = []
for experiment, variant in (("007", "base"), ("007", "B"), ("008", "base")):
    worktree = Path("worktrees/m6-replica-exp" + experiment)
    profile_dir = worktree / ("build/m6-replications/EXP" + experiment + "/profiles")
    sampling = profile_dir / (variant + "-sampling.json")
    record = json.loads(sampling.read_text())
    manifest = json.loads((worktree / ("build/exp" + experiment + "/build.json")).read_text())
    freeze_path = (worktree / "experiments/EXP-007/freeze.json" if experiment == "007"
                   else BASE / "EXP-008/PREPARATION.json")
    canonical_freeze = json.loads(freeze_path.read_text())
    assert all(sha(worktree / p) == h for p, h in manifest["files"].items())
    frozen_files = canonical_freeze["files"] if experiment == "007" else canonical_freeze["frozen_files_sha256"]
    assert all(sha(worktree / p) == h for p, h in frozen_files.items())
    binary = worktree / manifest["variants"][variant]["binary"]
    assert sha(binary) == record["binary_sha256"] == manifest["variants"][variant]["binary_sha256"]
    entry = next(r for r in captures if r["experiment"] == experiment and r["variant"] == variant)
    assert all(sha(p) == h for p, h in entry["raw_files"].items())
    sampler_rc = record.get("sample_returncode", record.get("sampler_returncode"))
    assert sampler_rc == record["child_returncode"] == 0
    count = 96 if experiment == "007" else 16
    command = ["build/exp" + experiment + "/" + variant + "/decoder-bench",
               "--width", "60", "--count", str(count), "--leaves", "8", "--rounds", "65536",
               "--samples", "64", "--warmup", "16", "--seed", "81031"]
    assert record["command"] == command
    sample_command = record["sampler_command"]
    assert sample_command[0] == "/usr/bin/sample" and sample_command[2:5] == ["1", "1", "-file"]
    assert sample_command[1].isdigit()
    rows = list(csv.DictReader((profile_dir / (variant + "-profile.csv")).read_text().splitlines()))
    assert len(rows) == 64
    invariant_fields = ("width", "score_shift", "reversed", "count", "leaves", "rounds", "seed", "operations", "leaf_bytes", "offset_mask", "crossings_per_round", "fixture_hash", "checksum")
    invariant = {k: rows[0][k] for k in invariant_fields}
    assert all(r["kind"] == "time" and int(r["sample"]) == i
               and all(r[k] == v for k, v in invariant.items())
               and r["cycles"] == r["instructions"] == "" for i, r in enumerate(rows))
    assert int(invariant["operations"]) == count * 8 * 65536
    assert tuple(int(invariant[k]) for k in ("width", "score_shift", "reversed", "count", "leaves", "rounds", "seed")) == (60, 0, 0, count, 8, 65536, 81031)
    text = (profile_dir / (variant + "-sample.txt")).read_text()
    graph = text.split("Call graph:", 1)[1].split("Total number in stack", 1)[0]
    nodes = []
    for line in graph.splitlines():
        match = re.match(r"^([ +|!:]*)(\d+) (.+)$", line)
        if match:
            tail = match[3]
            symbol = tail.split("  (in ", 1)[0]
            nodes.append(dict(depth=len(match[1]), count=int(match[2]), symbol=symbol))
    assert nodes
    leaves = [node for i, node in enumerate(nodes) if i + 1 == len(nodes) or nodes[i + 1]["depth"] <= node["depth"]]
    total = sum(node["count"] for node in nodes if node["depth"] == min(n["depth"] for n in nodes))
    assert sum(node["count"] for node in leaves) == total
    bins = {}
    for node in leaves:
        symbol = node["symbol"]
        key = symbol if symbol in ("decoder_batch", "zbtScoreLeafDecodeRange", "zbtScoreLeafDecodePolicy") else "non-decoder/printing"
        bins[key] = bins.get(key, 0) + node["count"]
    target = sum(value for key, value in bins.items() if key != "non-decoder/printing")
    results.append(dict(experiment="EXP-" + experiment, variant=variant,
        sampler_returncode=sampler_rc, child_returncode=record["child_returncode"],
        binary_sha256=sha(binary), binary_matches_sampling_and_build_manifest=True,
        canonical_source_referee_freeze_verified=True,
        raw_files_sha256={Path(p).name: h for p, h in entry["raw_files"].items()},
        build_manifest_sha256=sha(worktree / ("build/exp" + experiment + "/build.json")),
        source_referee_freeze_evidence_sha256=sha(freeze_path),
        source_referee_freeze_evidence=("canonical EXP-007/freeze.json" if experiment == "007" else "018/EXP-008/PREPARATION.json"),
        profile_driver_sha256=sha(worktree / ("experiments/EXP-" + experiment + "/profile.py")),
        canonical_profile_invocation=["python3", "experiments/EXP-" + experiment + "/profile.py", variant,
            "--out-dir", "build/m6-replications/EXP" + experiment + "/profiles"],
        target_command=command,
        generic_sampler_command=["/usr/bin/sample", "<owned-pid>", "1", "1", "-file", "<private-profile>/" + variant + "-sample.txt"],
        sample_scope="Whole process, including construction/setup, warmup, measured work and output; not time-scoped to the decoder",
        retained_csv_rows=64, csv_fixture_metadata=invariant,
        csv_timing_rows_excluded_from_comparisons=True,
        stack_root_observations=total, exclusive_leaf_observations=bins,
        target_leaf_observations=target, exclusive_collapsed_leaf_records=len(leaves),
        sufficiency="Sufficient descriptive support that this fixed capture reached the decoder region; not a precision/cycle/instruction-cost qualification",
        method="Leaf counts reconstruct call-graph prefix depth; inclusive parents are never added. A collapsed record can combine several PC offsets; these are not counts of distinct instructions.",
        source_regions=(["EXP-007/referee/kernel.c decoder_batch: round/leaf loop, materialization, unsigned checksum consumption",
                         "EXP-007/referee/control.inc scalar range decode inlined into decoder_batch"] if experiment == "007" and variant == "base" else
                        ["EXP-007/variants/B/decoder.inc zbtScoreLeafDecodeRange: geometry-specialized decode/output stores",
                         "EXP-007/referee/kernel.c decoder_batch: caller/round/leaf/checksum work"] if experiment == "007" else
                        ["EXP-008/referee/kernel.c decoder_batch: caller/round/leaf/checksum work",
                         "EXP-008/referee/policy-control.inc zbtScoreLeafDecodePolicy: baseline bulk policy decode/output stores"]),
        exact_source_line_attribution="Unavailable from collapsed symbol+offset sample report; no invented per-line instruction/cycle cost",
        counters_requested=False))
assert results[0]["csv_fixture_metadata"] == results[1]["csv_fixture_metadata"]
report = dict(status="THREE CAPTURE AUDITS PASS; DESCRIPTIVE SOFTWARE LOCATIONS ONLY",
    captures=results, capture_count=len(results),
    profile_capture_manifest_sha256=sha(BASE / "PROFILE-CAPTURE.json"), audit_script_sha256=sha(__file__),
    no_rerun_build_test_profile_or_timing=True, raw_path_bearing_files_remain_private=True,
    analysis_preparation_note="Initial read requested nonexistent EXP-008/freeze.json; corrected to its published PREPARATION.json frozen-file map. No captured data changed or experiment rerun.",
    interpretation="No pooling of experiments/hosts or inference of relative speed, cycles, CPI/IPC, stalls, latency, setup cost or source-optimization acceptance. Counts describe captured locations; timer-based sample can alias.",
    participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact serving model/token/cost unknown")
(OUT / "PROFILE-ANALYSIS.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"status": report["status"], "counts": [(r["experiment"], r["variant"], r["exclusive_leaf_observations"]) for r in results]}))
