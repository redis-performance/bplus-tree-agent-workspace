#!/usr/bin/env python3
"""Independent reconstruction from write-once CSV streams and command hashes."""

import csv
import hashlib
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    records = [json.loads(line) for line in (OUT / "commands.jsonl").read_text().splitlines()]
    reported = json.loads((OUT / "summary.json").read_text())
    calibration = json.loads((OUT / "calibration.json").read_text())
    assert len(records) == 58 and len({r["name"] for r in records}) == 58
    assert all(r["returncode"] == 0 and r["child_reaped"] and not r.get("timed_out") for r in records)
    for previous, current in zip(records, records[1:]):
        assert previous["finished_utc"] <= current["started_utc"], "overlapping native commands"
    streams = 0
    for record in records:
        for channel in ("stdout", "stderr"):
            path = OUT / "raw" / (record["name"] + "." + channel)
            assert path.is_file()
            assert digest(path) == record["raw"][channel]["sha256"]
            assert path.stat().st_size == record["raw"][channel]["bytes"]
            streams += 1
        if record["name"].startswith("aa-"):
            assert record["raw"]["stderr"]["bytes"] == 0
    assert streams == 116
    reconstructed = []
    blocks = []
    for index in range(48):
        record = records[index + 10]
        assert record["name"] == f"aa-{index:03d}"
        lines = list(csv.DictReader(io.StringIO((OUT / "raw" / f"aa-{index:03d}.stdout").read_text())))
        assert len(lines) == 1
        row = lines[0]
        expected = reported["rows"][index]
        n = expected["size"]
        block_index = index // 8
        size_order = (100000, 1000000) if block_index % 2 == 0 else (1000000, 100000)
        assert expected["block"] == block_index and n == size_order[(index % 8) // 4]
        assert expected["position"] == index % 4
        seed = (1, 2, 3, 1, 2, 3)[expected["block"]]
        operations = calibration["fixed"][str(n)]["operations"]
        assert expected["index"] == index and expected["seed"] == seed
        assert expected["side"] == "ABBA"[expected["position"]]
        assert record["command"] == ["build/m1-lookup-aa/lookup", "--case", "lookup-hit", "--size", str(n),
                                     "--ops", str(operations), "--seed", str(seed), "--member-bytes", "16", "--warmup-passes", "1"]
        for key in ("case", "size", "requested_ops", "member_bytes", "seed", "operations", "elapsed_ns",
                    "tree_bytes", "checksum", "thread_elapsed_ns", "cpu_start", "cpu_end", "warmup_passes"):
            assert row[key] == expected["csv"][key]
        assert row["case"] == "lookup-hit" and row["warmup_passes"] == "1"
        assert int(row["elapsed_ns"]) > 0 and int(row["tree_bytes"]) > 0
        reconstructed.append(row)
        if index % 4 == 3:
            four = reconstructed[-4:]
            assert len({(r["checksum"], r["tree_bytes"], r["size"], r["seed"], r["operations"]) for r in four}) == 1
            a = int(four[0]["elapsed_ns"]) + int(four[3]["elapsed_ns"])
            b = int(four[1]["elapsed_ns"]) + int(four[2]["elapsed_ns"])
            minimum = min(int(r["elapsed_ns"]) for r in four)
            prior = reported["blocks"][len(blocks)]
            qualified = abs(b - a) * 100 <= a and minimum >= 10000000
            assert (prior["A_elapsed_sum_ns"], prior["B_elapsed_sum_ns"], prior["minimum_window_ns"], prior["qualified"]) == (a, b, minimum, qualified)
            blocks.append({"block": prior["block"], "size": n, "qualified": qualified,
                           "effect_percent": (b - a) * 100 / a, "minimum_window_ns": minimum})
    qualified_by_size = {str(n): sum(b["qualified"] for b in blocks if b["size"] == n) for n in (100000, 1000000)}
    assert qualified_by_size == {"100000": 1, "1000000": 2}
    assert reported["decision"] == "PARK_AA_PRECISION" and reported["candidate_timing"] == 0
    audit = {"status": "PASS", "commands": len(records), "raw_streams": streams, "timing_rows": len(reconstructed),
             "blocks": len(blocks), "all_windows_at_least_10ms": all(b["minimum_window_ns"] >= 10000000 for b in blocks),
             "qualified_by_size": qualified_by_size, "all_command_hashes_match": True,
             "serial_order": True, "all_children_reaped": True, "candidate_timing": 0}
    target = OUT / "AUDIT.json"
    with target.open("x") as stream:
        json.dump(audit, stream, indent=2)
        stream.write("\n")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
