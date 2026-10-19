#!/usr/bin/env python3
"""Serial process-level ABBA for the frozen DECODE-001 private decoder."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import statistics
import subprocess
import tarfile
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
CELLS = [(w, r, n) for w in (0, 8, 57, 59, 60, 63, 64)
         for r in (0, 1) for n in (1, 2, 4, 16, 96)]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--build", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--phase", choices=("aa", "A", "B", "C"), required=True)
    p.add_argument("--budget-seconds", type=int, default=300)
    p.add_argument("--fresh", action="store_true")
    a = p.parse_args()
    if a.fresh and a.phase == "aa":
        pass
    build = Path(a.build).resolve()
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    raw = out / "raw"
    raw.mkdir()
    bm = json.loads((build / "build.json").read_text())
    if bm["sanitizers"]:
        raise SystemExit("Release build required for timing")
    for name, expected in bm["inputs"].items():
        if sha(ROOT / name) != expected:
            raise SystemExit(f"Stale input: {name}")
    for v in ("base", "A", "B", "C"):
        if sha(build / v / "decoder-bench") != bm["variants"][v]["binary_sha256"]:
            raise SystemExit(f"Stale binary: {v}")
    rotated = []
    for block in range(6):
        cells = CELLS[block % len(CELLS):] + CELLS[:block % len(CELLS)]
        for width, reverse, count in cells:
            for step, label in enumerate("ABBA"):
                variant = "base" if a.phase == "aa" or label == "A" else a.phase
                rotated.append(dict(block=block, width=width, reverse=reverse,
                                    count=count, step=step, label=label,
                                    variant=variant,
                                    seed=(82037, 82051)[block % 2] if a.fresh else
                                         (81031, 81041)[block % 2]))
    manifest = dict(status="running", started_utc=now(), phase=a.phase, fresh=a.fresh,
                    build_manifest_sha256=sha(build / "build.json"),
                    runner_sha256=sha(__file__), cell_count=len(CELLS),
                    blocks=6, samples_per_process=129, schedule=rotated,
                    runs=[], summaries=[],
                    scope="private decoder array throughput; no public iterator claim")
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    start = time.monotonic()
    fixtures = {}
    try:
        for index, item in enumerate(rotated):
            elapsed = time.monotonic() - start
            if elapsed >= a.budget_seconds:
                raise TimeoutError("Phase budget exhausted")
            name = f"{index:04d}-b{item['block']}-w{item['width']}-r{item['reverse']}-n{item['count']}-{item['label']}"
            binary = build / item["variant"] / "decoder-bench"
            count = item["count"]
            command = [str(binary), "--width", str(item["width"]),
                       "--reversed", str(item["reverse"]), "--count", str(count),
                       "--seed", str(item["seed"]), "--leaves", "8",
                       "--rounds", str(math.ceil(49152 / (count * 8))),
                       "--samples", "129", "--warmup", "16"]
            q = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                               timeout=min(30, max(.01, a.budget_seconds - elapsed)))
            csvpath, errpath = raw / f"{name}.csv", raw / f"{name}.stderr"
            csvpath.write_text(q.stdout)
            errpath.write_text(q.stderr)
            record = dict(item, name=name, returncode=q.returncode,
                          csv_sha256=sha(csvpath), stderr_sha256=sha(errpath))
            manifest["runs"].append(record)
            if q.returncode:
                raise RuntimeError(f"Child failed {name}: {q.stderr}")
            rows = list(csv.DictReader(io.StringIO(q.stdout)))
            if len(rows) != 129 or any(row["kind"] != "time" or None in row for row in rows):
                raise ValueError(f"Bad output rows: {name}")
            fields = ("operations", "leaf_bytes", "offset_mask", "crossings_per_round",
                      "fixture_hash", "checksum")
            invariant = tuple(rows[0][key] for key in fields)
            if any(tuple(row[key] for key in fields) != invariant for row in rows):
                raise ValueError(f"Internal checksum changed: {name}")
            if int(rows[0]["operations"]) != count * 8 * math.ceil(49152 / (count * 8)):
                raise ValueError(f"Wrong operation count: {name}")
            key = (item["width"], item["reverse"], count, item["seed"])
            if fixtures.setdefault(key, invariant) != invariant:
                raise ValueError(f"Fixture differs across variants: {name}")
            vals = [float(row["ns_per_decode"]) for row in rows]
            manifest["summaries"].append(dict(item, name=name, min_ns=min(vals),
                median_ns=statistics.median(vals), max_ns=max(vals),
                min_window_ms=min(float(row["elapsed_ns"]) for row in rows) / 1e6,
                endpoint_migrations=sum(row["cpu_start"] != row["cpu_end"] for row in rows)))
            if (index + 1) % 70 == 0:
                (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
                print(f"{a.phase}: {index+1}/{len(rotated)}", flush=True)
        manifest["status"] = "complete"
    except BaseException as error:
        manifest["status"] = "failed"
        manifest["error"] = str(error)
        raise
    finally:
        manifest["finished_utc"] = now()
        manifest["elapsed_seconds"] = time.monotonic() - start
        (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    with tarfile.open(out / "raw.tar.gz", "w:gz") as tar:
        for file in sorted(raw.iterdir()):
            tar.add(file, arcname=file.name)
    manifest["raw_archive_sha256"] = sha(out / "raw.tar.gz")
    with tarfile.open(out / "raw.tar.gz", "r:gz") as tar:
        if len(tar.getmembers()) != 2 * len(rotated):
            raise ValueError("Incomplete raw archive")
        for record in manifest["runs"]:
            for kind in ("csv", "stderr"):
                member = tar.extractfile(f"{record['name']}.{kind}")
                if hashlib.sha256(member.read()).hexdigest() != record[f"{kind}_sha256"]:
                    raise ValueError("Archive hash mismatch")
    for file in raw.iterdir():
        file.unlink()
    raw.rmdir()
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"complete {len(rotated)} serial processes in {manifest['elapsed_seconds']:.2f}s")


if __name__ == "__main__":
    main()
