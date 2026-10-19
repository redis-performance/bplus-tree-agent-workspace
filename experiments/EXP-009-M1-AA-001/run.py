#!/usr/bin/env python3
"""One frozen, same-binary Apple M1 lookup A/A schedule; no candidate."""

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
DIR = Path(__file__).resolve().parent
OUT = DIR / "results"
BIN = ROOT / "build/m1-lookup-aa/lookup"
SAN = ROOT / "build/m1-lookup-aa/lookup-san"
ENV = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "LANG": "C", "LC_ALL": "C", "TZ": "UTC"}
IDENTITIES = {
    "src/zset_btree.c": "d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2",
    "src/zset_btree.h": "496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83",
    "compat/server.h": "468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7",
    "compat/standalone.c": "c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3",
    "experiments/EXP-009/harness/lookup.c": "7569d802357a8ca937ba8eaa668f9fe2c17652b6cd8b957d952129b6cab87cf5",
}
FLAGS = ["-std=c11", "-O3", "-g", "-Wall", "-Wextra", "-Werror", "-fno-omit-frame-pointer", "-fno-lto"]
SOURCES = ["experiments/EXP-009/harness/lookup.c", "src/zset_btree.c", "compat/standalone.c", "vendor/redis/siphash.c"]


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def verify_sources():
    for name, expected in IDENTITIES.items():
        actual = sha(ROOT / name)
        if actual != expected:
            raise RuntimeError(f"frozen source mismatch: {name}: {actual}")


def call(name, command, timeout=90):
    raw = OUT / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    stdout_path, stderr_path = raw / f"{name}.stdout", raw / f"{name}.stderr"
    if stdout_path.exists() or stderr_path.exists():
        raise FileExistsError(f"write-once raw output: {name}")
    started = time.monotonic()
    record = {"name": name, "command": command, "started_utc": utc(), "environment": ENV}
    with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
        child = subprocess.Popen(command, cwd=ROOT, env=ENV, stdout=stdout, stderr=stderr, start_new_session=True)
        try:
            code = child.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            child.wait()
            code = child.returncode
            record["timed_out"] = True
    record.update(returncode=code, finished_utc=utc(), wall_seconds=time.monotonic() - started,
                  child_reaped=True, raw={"stdout": {"sha256": sha(stdout_path), "bytes": stdout_path.stat().st_size},
                                          "stderr": {"sha256": sha(stderr_path), "bytes": stderr_path.stat().st_size}})
    with (OUT / "commands.jsonl").open("a") as stream:
        stream.write(json.dumps(record) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    if code != 0 or record.get("timed_out"):
        raise RuntimeError(f"command failed: {name}, exit {code}")
    return {"stdout": stdout_path, "stderr": stderr_path}


def driver():
    path = ROOT / "experiments/EXP-009/driver.py"
    spec = importlib.util.spec_from_file_location("exp009_driver", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lookup_command(binary, n, ops, seed):
    return [str(binary.relative_to(ROOT)), "--case", "lookup-hit", "--size", str(n),
            "--ops", str(ops), "--seed", str(seed), "--member-bytes", "16", "--warmup-passes", "1"]


def build():
    verify_sources()
    if OUT.exists():
        raise FileExistsError("build output already exists; do not overwrite")
    OUT.mkdir(parents=True)
    BIN.parent.mkdir(parents=True, exist_ok=True)
    if BIN.exists() or SAN.exists():
        raise FileExistsError("binary already exists; do not overwrite")
    common = ["-I.", "-Isrc", "-Icompat", "-Ivendor/redis", *SOURCES, "-lm"]
    call("compile-native", ["clang", *FLAGS, *common, "-o", str(BIN.relative_to(ROOT))], 120)
    san_flags = ["-std=c11", "-O1", "-g", "-Wall", "-Wextra", "-Werror", "-fno-omit-frame-pointer",
                 "-fno-lto", "-fsanitize=address,undefined", "-fno-sanitize-recover=all"]
    call("compile-sanitizer", ["clang", *san_flags, *common, "-o", str(SAN.relative_to(ROOT))], 120)
    check = driver()
    for name, binary in [("native", BIN), ("sanitizer", SAN)]:
        raw = call(f"smoke-{name}", lookup_command(binary, 1000, 2003, 1))
        check.parse_csv(raw, 1000, 2003, 1)
    calibration = []
    counts = {}
    for n in (100000, 1000000):
        elapsed = []
        for rep in range(3):
            raw = call(f"calibrate-n{n}-r{rep}", lookup_command(BIN, n, 200000, 1))
            row = check.parse_csv(raw, n, 200000, 1)
            elapsed.append(row["elapsed_ns"])
            calibration.append({"size": n, "replicate": rep, **row})
        uncapped = math.ceil(600000000 * 200000 / min(elapsed))
        counts[str(n)] = {"operations": min(uncapped, 100000000), "uncapped": uncapped,
                          "capped": uncapped > 100000000, "fastest_calibration_elapsed_ns": min(elapsed)}
    write(OUT / "build.json", {"status": "COMPLETE", "started_from": "4bc71bd73ae7be8e68761269b9bdfd5a8df11495",
                               "source_sha256": IDENTITIES, "binary_sha256": sha(BIN), "sanitizer_sha256": sha(SAN),
                               "driver_sha256": sha(ROOT / "experiments/EXP-009/driver.py"),
                               "compiler_version": subprocess.check_output(["clang", "--version"], env=ENV, text=True).splitlines()[0],
                               "flags": FLAGS, "environment": ENV, "completed_utc": utc()})
    write(OUT / "calibration.json", {"status": "COMPLETE", "observations": calibration, "fixed": counts,
                                     "target_elapsed_ns": 600000000, "method": "integer ceil from fastest of three 200K runs"})


def aa():
    verify_sources()
    build_record = json.loads((OUT / "build.json").read_text())
    calibration = json.loads((OUT / "calibration.json").read_text())
    if build_record["status"] != "COMPLETE" or calibration["status"] != "COMPLETE" or sha(BIN) != build_record["binary_sha256"]:
        raise RuntimeError("build/calibration identity mismatch")
    if (OUT / "summary.json").exists():
        raise FileExistsError("A/A already complete; no retry")
    check = driver()
    rows, blocks = [], []
    for block, seed in enumerate((1, 2, 3, 1, 2, 3)):
        for n in ((100000, 1000000) if block % 2 == 0 else (1000000, 100000)):
            ops = calibration["fixed"][str(n)]["operations"]
            four = []
            for position, side in enumerate("ABBA"):
                index = len(rows)
                raw = call(f"aa-{index:03d}", lookup_command(BIN, n, ops, seed))
                row = check.parse_csv(raw, n, ops, seed)
                row.update(index=index, block=block, size=n, seed=seed, position=position, side=side)
                rows.append(row)
                four.append(row)
            if any(r["fingerprint"] != four[0]["fingerprint"] for r in four):
                raise RuntimeError("A/A output or memory mismatch")
            a = four[0]["elapsed_ns"] + four[3]["elapsed_ns"]
            b = four[1]["elapsed_ns"] + four[2]["elapsed_ns"]
            minimum = min(r["elapsed_ns"] for r in four)
            blocks.append({"block": block, "seed": seed, "size": n, "A_elapsed_sum_ns": a,
                           "B_elapsed_sum_ns": b, "effect_percent_display_only": (b - a) * 100 / a,
                           "minimum_window_ns": minimum,
                           "qualified": abs(b - a) * 100 <= a and minimum >= 10000000})
    qualified = all(b["qualified"] for b in blocks)
    write(OUT / "summary.json", {"status": "COMPLETE", "decision": "AA_QUALIFIED_ONLY" if qualified else "PARK_AA_PRECISION",
                                 "candidate_timing": 0, "source_selection": "NONE", "processes": len(rows),
                                 "rows": rows, "blocks": blocks, "completed_utc": utc()})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("build", "aa"))
    args = parser.parse_args()
    os.chdir(ROOT)
    (build if args.phase == "build" else aa)()
