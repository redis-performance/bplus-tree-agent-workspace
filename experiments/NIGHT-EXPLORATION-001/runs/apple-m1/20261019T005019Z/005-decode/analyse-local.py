#!/usr/bin/env python3
"""Reconstruct DECODE-001 process statistics and paired blocks from raw archives."""
import csv
import hashlib
import io
import json
from pathlib import Path
import statistics
import tarfile
from collections import defaultdict

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def one(folder):
    manifest = json.loads((folder / "manifest.json").read_text())
    assert manifest["status"] == "complete"
    assert len(manifest["runs"]) == 1680
    assert len(manifest["summaries"]) == 1680
    assert sha(folder / "raw.tar.gz") == manifest["raw_archive_sha256"]
    pairs = defaultdict(lambda: defaultdict(lambda: {"A": [], "B": []}))
    cell_windows = defaultdict(list)
    migrations = 0
    min_window_ms = float("inf")
    max_window_ms = 0
    with tarfile.open(folder / "raw.tar.gz", "r:gz") as tar:
        assert len(tar.getmembers()) == 3360
        for record, summary in zip(manifest["runs"], manifest["summaries"]):
            assert record["name"] == summary["name"]
            raw = tar.extractfile(record["name"] + ".csv").read()
            err = tar.extractfile(record["name"] + ".stderr").read()
            assert hashlib.sha256(raw).hexdigest() == record["csv_sha256"]
            assert hashlib.sha256(err).hexdigest() == record["stderr_sha256"]
            rows = list(csv.DictReader(io.StringIO(raw.decode())))
            assert len(rows) == 129
            assert all(row["kind"] == "time" and None not in row for row in rows)
            values = [float(row["ns_per_decode"]) for row in rows]
            median = statistics.median(values)
            assert abs(median - summary["median_ns"]) < 1e-8
            assert min(values) == summary["min_ns"] and max(values) == summary["max_ns"]
            assert all(row["fixture_hash"] == rows[0]["fixture_hash"] and
                       row["checksum"] == rows[0]["checksum"] for row in rows)
            assert [int(row["sample"]) for row in rows] == list(range(129))
            key = (record["width"], record["reverse"], record["count"])
            pairs[key][record["block"]][record["label"]].append(median)
            cell_windows[key].append(summary["min_window_ms"])
            migrations += summary["endpoint_migrations"]
            min_window_ms = min(min_window_ms, summary["min_window_ms"])
            max_window_ms = max(max_window_ms, summary["min_window_ms"])
    effects = {}
    qualified = 0
    for key, blocks in pairs.items():
        assert len(blocks) == 6
        values = []
        for block in range(6):
            a, b = blocks[block]["A"], blocks[block]["B"]
            assert len(a) == len(b) == 2
            values.append(100 * (statistics.mean(b) / statistics.mean(a) - 1))
        effects["w%d-r%d-n%d" % key] = dict(block_effects=values,
            median_effect=statistics.median(values), min_effect=min(values),
            max_effect=max(values))
        if all(abs(v) <= 1 for v in values) and min(cell_windows[key]) >= 10:
            qualified += 1
    assert len(effects) == 70
    return dict(status="PASS", phase=manifest["phase"], processes=1680,
                rows=1680 * 129, cells=70, qualified_cells=qualified,
                endpoint_migrations=migrations, minimum_window_ms=min_window_ms,
                maximum_process_min_window_ms=max_window_ms,
                archive_sha256=manifest["raw_archive_sha256"], effects=effects)


def main():
    data = {phase: one(HERE / folder) for phase, folder in
            (("aa", "aa"), ("A", "discovery-A"),
             ("B", "discovery-B"), ("C", "discovery-C"))}
    (HERE / "AUDIT.json").write_text(json.dumps(data, indent=2) + "\n")
    for phase, result in data.items():
        print(phase, result["status"], result["processes"], result["rows"],
              "qualified", result["qualified_cells"],
              "min_window_ms", round(result["minimum_window_ms"], 3))


if __name__ == "__main__":
    main()
