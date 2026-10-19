#!/usr/bin/env python3
"""Prepare or run a separately authorized matched adapter diagnostic."""
import argparse
import csv
import hashlib
import io
import json
import math
import os
import re
import signal
import statistics
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
REL = OUT.relative_to(ROOT)
BASE = OUT.parent
SCRATCH = Path("scratch/m6-contract-diagnostic")
PLAN = json.loads((OUT / "PLAN.json").read_text())
CELLS = PLAN["cells"]
GLOBAL_STOP = datetime.fromisoformat(PLAN["budgets"]["absolute_stop_utc"]).timestamp()


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(data, indent=2) + "\n")
    temporary.replace(path)


def generic(text):
    text = text.replace(str(ROOT), "<workspace>")
    return re.sub(r"/var/" + r"folders/[^\s]+/T/", "<compiler-temporary-directory>/", text)


def execute(command, name, folder, timeout):
    """Bound and reap a process group; retain stdout/stderr even on timeout."""
    assert timeout > 0, "no remaining child budget"
    destination = OUT / folder
    destination.mkdir(exist_ok=True)
    raw_dir = SCRATCH / "raw-logs"
    raw_dir.mkdir(parents=True, exist_ok=True)
    public_paths = {c: destination / (name + "." + c) for c in ("stdout", "stderr")}
    raw_paths = {c: raw_dir / (name + "." + c) for c in ("stdout", "stderr")}
    assert not any(p.exists() for p in [*public_paths.values(), *raw_paths.values()]), ("no retry/overwrite", name)
    command = list(map(str, command))
    public_command = [generic(argument) for argument in command]
    executable_identity = None
    if Path(command[0]).is_absolute():
        executable_identity = dict(name=Path(command[0]).name, sha256=sha(command[0]))
        public_command[0] = executable_identity["name"]
    (raw_dir / (name + ".command.json")).write_text(json.dumps(dict(command=command, cwd=str(ROOT))) + "\n")
    record = dict(name=name, command=public_command, executable_identity=executable_identity,
                  cwd="workspace-root", started_utc=utc(),
                  timeout_seconds=timeout, timed_out=False, returncode=None)
    start = time.monotonic()
    process = None
    stdout, stderr = "", ""

    def terminate_and_collect():
        if process.poll() is None:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                # The child can finish between poll() and killpg().
                pass
        return process.communicate()

    try:
        process = subprocess.Popen(command, cwd=ROOT, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, start_new_session=True)
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            record["timed_out"] = True
            stdout, stderr = terminate_and_collect()
        record["returncode"] = process.returncode
    except OSError as error:
        record["spawn_error"] = generic(repr(error))
        if process is not None and process.poll() is None:
            stdout, stderr = terminate_and_collect()
            record["returncode"] = process.returncode
    except BaseException as error:
        record["interrupted"] = generic(repr(error))
        if process is not None:
            stdout, stderr = terminate_and_collect()
            record["returncode"] = process.returncode
    finally:
        # communicate() has reaped the child on both normal and timeout paths.
        record.update(finished_utc=utc(), wall_seconds=time.monotonic() - start,
                      process_reaped=process is None or process.poll() is not None)
        record["logs"] = {}
        for channel, data in (("stdout", stdout), ("stderr", stderr)):
            raw_paths[channel].write_text(data)
            public_paths[channel].write_text(generic(data))
            record["logs"][channel] = dict(file=str(public_paths[channel].relative_to(OUT)),
                                            sha256=sha(public_paths[channel]),
                                            original_raw_sha256=sha(raw_paths[channel]),
                                            original_raw="ignored " + str(raw_paths[channel]))
        with (OUT / "commands.jsonl").open("a") as journal:
            journal.write(json.dumps(record) + "\n")
    if (record["timed_out"] or record["returncode"] != 0 or "interrupted" in record
            or not record["process_reaped"]):
        raise RuntimeError(json.dumps(dict(child=name, timed_out=record["timed_out"],
                                           returncode=record["returncode"],
                                           evidence="commands.jsonl + retained stdout/stderr")))
    return stdout, stderr, record


def arguments(binary, cell, seed, small=False):
    return [binary, "--size", 1000 if small else cell["size"],
            "--ops", 2003 if small else PLAN["ops"], "--seed", seed,
            "--member-bytes", PLAN["member_bytes"], "--warmup-passes", 1 if small else PLAN["warmup_passes"],
            "--direction", cell["direction"], "--mask", cell["mask"], "--encoding", cell["encoding"]]


def csv_row(stdout, cell, seed, small=False):
    rows = list(csv.DictReader(io.StringIO(stdout)))
    assert len(rows) == 1, "expected exactly one CSV row"
    row = rows[0]
    size, requested = (1000, 2003) if small else (cell["size"], PLAN["ops"])
    count = (1 + (requested - 1) // size) * size
    assert row["case"] == "iterator-modes"
    assert int(row["size"]) == size and int(row["seed"]) == seed
    assert int(row["requested_ops"]) == requested and int(row["operations"]) == count
    assert int(row["traversals"]) == count // size
    assert int(row["member_bytes"]) == PLAN["member_bytes"]
    assert row["direction"] == cell["direction"] and int(row["mask"]) == cell["mask"]
    assert row["encoding"] == cell["encoding"]
    assert int(row["warmup_passes"]) == (1 if small else PLAN["warmup_passes"])
    assert row["checksum"] == row["expected_checksum"]
    assert int(row["elapsed_ns"]) > 0 and int(row["tree_bytes"]) > 0
    return row


def reused_tests():
    """Reuse only original-test evidence with the exact immutable input identities."""
    old_freeze = json.loads((BASE / "004-lookup/freeze.json").read_text())
    old_validation = json.loads((BASE / "004-lookup/candidate-validation.json").read_text())
    review = json.loads((BASE / "010-assertion-contract-review/review.json").read_text())
    new_manifest = json.loads((BASE / "011-contract-baseline/matrix/manifest.json").read_text())
    assert old_validation["variants"]["0"]["source"] == PLAN["source_c_sha256"]
    assert new_manifest["status"] == "complete"
    records = {}
    for adapter, compat in PLAN["adapters"].items():
        identity = {"src/zset_btree.c": sha("src/zset_btree.c"), "src/zset_btree.h": sha("src/zset_btree.h"),
                    "compat/server.h": sha(Path(compat) / "server.h"),
                    "compat/standalone.c": sha(Path(compat) / "standalone.c"),
                    "vendor/redis/siphash.c": sha("vendor/redis/siphash.c"),
                    "tests/upstream.c": sha("tests/upstream.c")}
        expected = old_freeze["files"] if adapter == "old" else new_manifest["source_hashes"]
        for path, digest in identity.items():
            # 011's manifest pins compiled inputs but omits tests/upstream.c;
            # its exact test identity is independently pinned by 010.
            recorded = (review["private_sources"]["noreturn"][path]
                        if adapter == "new" and path == "tests/upstream.c" else expected[path])
            assert recorded == digest, (adapter, path, "test-identity mismatch")
            assert review["private_sources"]["base" if adapter == "old" else "noreturn"][path] == digest
        logs = [BASE / "004-lookup/candidate-validation" / ("0-upstream" + suffix + ".stdout")
                if adapter == "old" else BASE / "011-contract-baseline/matrix" /
                ("release-build-check.stdout" if not suffix else "sanitize-build-check.stdout")
                for suffix in ("", "-san")]
        for log in logs:
            clean = re.sub(r"\x1b\[[0-9;]*m", "", log.read_text())
            assert "43 passed" in clean and "0 failed" in clean, log
        records[adapter] = dict(source_identity=identity,
                                original_tests_per_build=43,
                                native_sanitizer_evidence={str(p.relative_to(BASE)): sha(p) for p in logs})
    save(OUT / "reused-tests.json", records)


def prepare():
    assert not (OUT / "freeze.json").exists(), "preparation already frozen"
    assert sha("src/zset_btree.c") == PLAN["source_c_sha256"]
    assert sha("src/zset_btree.h") == PLAN["source_h_sha256"]
    for name in ("iterator.c", "microbench.c"):
        assert (OUT / name).read_bytes() == (BASE / "009-iterator-profile" / name).read_bytes()
    reused_tests()
    literal_files = {}
    validation = []
    for adapter, compat in PLAN["adapters"].items():
        directory = SCRATCH / adapter
        directory.mkdir(parents=True, exist_ok=True)
        for sanitized in (False, True):
            flags = PLAN["flags"].copy()
            if sanitized:
                flags[flags.index("-O3")] = "-O1"
                flags += ["-fsanitize=address,undefined", "-fno-sanitize-recover=all"]
            binary = directory / ("iterator-san" if sanitized else "iterator")
            execute(["clang", *flags, "-Isrc", "-I" + compat, "-Ivendor/redis",
                     REL / "iterator.c", "src/zset_btree.c", Path(compat) / "standalone.c",
                     "vendor/redis/siphash.c", "-lm", "-o", binary],
                    "build-" + adapter + ("-san" if sanitized else ""), "build-logs", 120)
            for cell in CELLS[:4]:
                stdout, _, record = execute(arguments(binary, cell, 1, True),
                                             "validate-" + adapter + ("-san-" if sanitized else "-native-") + cell["contract"],
                                             "validation-logs", 120)
                row = csv_row(stdout, cell, 1, True)
                validation.append(dict(adapter=adapter, sanitizer=sanitized, contract=cell["contract"],
                                       operations=int(row["operations"]), checksum=row["checksum"],
                                       tree_bytes=int(row["tree_bytes"]), status="PASS", logs=record["logs"]))
        stdout, _, _ = execute(["otool", "-tvV", directory / "iterator"],
                              "assembly-" + adapter, "build-logs", 120)
        selected, active = [], False
        for line in stdout.splitlines():
            if line.startswith("_") and line.endswith(":"):
                active = line == "_zbtreeIteratorNext:"
            if active:
                selected.append(line)
        (OUT / "build-logs" / (adapter + "-zbtreeIteratorNext.asm")).write_text("\n".join(selected) + "\n")
        strings, _, _ = execute(["otool", "-v", "-s", "__TEXT", "__cstring", directory / "iterator"],
                               "cstring-" + adapter, "build-logs", 120)
        assert PLAN["adapters"]["old"] not in strings, "old adapter __FILE__ prefix was not normalized"
        literals = [line.split(None, 1)[1] for line in strings.splitlines()
                    if re.match(r"^[0-9a-f]{16}\s+", line) and len(line.split(None, 1)) == 2]
        literal_files[adapter] = sorted(s for s in literals if s.endswith((".c", ".h")))
    assert literal_files["old"] == literal_files["new"]
    assert "src/zset_btree.c" in literal_files["old"]
    save(OUT / "validation.json", dict(status="PASS", runs=validation,
                                       native_sanitizer_runs=16, original43tests_reused="reused-tests.json",
                                       panic_filename_literals=literal_files,
                                       same_target_relative_path="src/zset_btree.c",
                                       identical_file_debug_maps=True, no_measured_phase_started=True))
    compiler = execute(["clang", "--version"], "compiler", "build-logs", 120)[0]
    files = ["src/zset_btree.c", "src/zset_btree.h", "vendor/redis/siphash.c", "vendor/redis/sds.h",
             "vendor/redis/testhelp.h", "tests/upstream.c", str(REL / "iterator.c"), str(REL / "microbench.c"),
             str(REL / "PLAN.json"), str(REL / "driver.py"), str(REL / "README.md")]
    files += [str(Path(compat) / name) for compat in PLAN["adapters"].values()
              for name in ("server.h", "standalone.c")]
    save(OUT / "freeze.json", dict(status="PREPARED; root+independent review and publication ACK pending",
                                   frozen_utc=utc(), files_sha256={p: sha(p) for p in files},
                                   binaries_sha256={str(SCRATCH / a / b): sha(SCRATCH / a / b)
                                                   for a in ("old", "new") for b in ("iterator", "iterator-san")},
                                   compiler="\n".join(s for s in compiler.splitlines() if not s.startswith("InstalledDir:")),
                                   source_optimization="NONE", participant="/root/followup_proposal_b",
                                   backend="Inherited Codex/GPT-6 family; exact serving model/token/cost unknown"))
    print("PREPARED:16 bounded semantic runs, reused exact original43test identities, normalized panic filenames; NO TIMING AUTHORIZED")


def verify_freeze():
    frozen = json.loads((OUT / "freeze.json").read_text())
    for path, expected in {**frozen["files_sha256"], **frozen["binaries_sha256"]}.items():
        assert sha(path) == expected, ("frozen identity changed", path)
    return frozen


def check_ack(path, phase):
    ack = json.loads(Path(path).read_text())
    assert ack["status"] == "authorized" and ack["exclusive_runner"] is True
    assert phase in ack["authorized_phases"]
    for key, filename in (("freeze_sha256", "freeze.json"), ("driver_sha256", "driver.py"), ("plan_sha256", "PLAN.json")):
        assert ack[key] == sha(OUT / filename), ("stale authorization", key)
    assert re.fullmatch(r"[0-9a-f]{40}", ack["published_commit"])
    reviews = ack["reviews"]
    assert any(r["reviewer"] == "/root" and r["status"] == "PASS" for r in reviews)
    assert any(r["reviewer"] != "/root" and r["status"] == "PASS" for r in reviews)
    return dict(file=str(Path(path)), sha256=sha(path), evidence=ack)


def derive(runs, phase, controls=None):
    results = []
    adapters = ("old", "new") if phase == "aa" else ("old-vs-new",)
    for adapter in adapters:
        for cell in CELLS:
            effects, memories, shortest = [], [], []
            for block in range(6):
                rows = [r for r in runs if r["cell"] == cell["id"] and r["block"] == block and r["comparison"] == adapter]
                rows.sort(key=lambda r: r["step"])
                assert len(rows) == 4 and [r["label"] for r in rows] == list("ABBA")
                assert len({r["checksum"] for r in rows}) == 1
                assert len({r["operations"] for r in rows}) == 1
                assert len({r["tree_bytes"] for r in rows}) == 1, ("owned memory differs", cell["id"], block)
                assert len({r["csv"]["construction_fingerprint"] for r in rows}) == 1, ("fixture differs", cell["id"], block)
                outer = [r for r in rows if r["label"] == "A"]
                inner = [r for r in rows if r["label"] == "B"]
                effects.append(100 * (statistics.mean(r["ns_op"] for r in inner) / statistics.mean(r["ns_op"] for r in outer) - 1))
                memories.append(100 * (statistics.mean(r["tree_bytes"] for r in inner) / statistics.mean(r["tree_bytes"] for r in outer) - 1))
                shortest.extend(r["elapsed_ns"] / 1e6 for r in rows)
            qualified = max(map(abs, effects)) <= 1 and min(shortest) >= 10 if phase == "aa" else None
            both_controls = None
            if phase == "compare":
                same_cell = [x for x in controls if x["cell"] == cell["id"]]
                assert len(same_cell) == 2
                both_controls = all(x["qualified"] for x in same_cell)
            results.append(dict(comparison=adapter, cell=cell["id"], effects_pct=effects,
                                median_pct=statistics.median(effects), observed_min_pct=min(effects),
                                observed_max_pct=max(effects), shortest_window_ms=min(shortest),
                                memory_effects_pct=memories, qualified=qualified,
                                all_comparison_windows_minimum_met=min(shortest) >= 10,
                                both_adapter_controls_qualified=both_controls,
                                interpretation="A/A control for this adapter" if phase == "aa" else
                                ("matched harness diagnostic effect" if both_controls and min(shortest) >= 10
                                 else "conditional: same-cell controls or comparison windows fail qualification")))
    return results


def phase_run(phase, ack_path):
    verify_freeze()
    ack = check_ack(ack_path, phase)
    output = OUT / (phase + ".json")
    rows_path = OUT / (phase + "-runs.jsonl")
    assert not output.exists() and not rows_path.exists(), "phase already attempted; no retry"
    assert time.time() < GLOBAL_STOP, "absolute stop reached"
    controls = None
    if phase == "compare":
        aa = json.loads((OUT / "aa.json").read_text())
        assert aa["status"] == "complete", "complete retained controls required"
        controls = aa["results"]
        # Failed controls are retained. This diagnostic still runs as preregistered.
    lock = SCRATCH / "MEASUREMENT.lock"
    fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    os.write(fd, json.dumps(dict(phase=phase, started_utc=utc(), pid=os.getpid())).encode())
    os.close(fd)
    state = dict(phase=phase, status="running", started_utc=utc(), authorization=ack,
                 source_optimization="NONE", classification=PLAN["classification"],
                 runs=[], results=[], timing_seconds=0.0, unknown_timed_work_on_failure=False)
    started = time.monotonic()
    save(output, state)
    try:
        for block, seed in enumerate(PLAN["seeds"]):
            order = CELLS[block % len(CELLS):] + CELLS[:block % len(CELLS)]
            if block % 2:
                order = list(reversed(order))
            for cell in order:
                comparisons = ["old", "new"] if block % 2 == 0 else ["new", "old"]
                if phase == "compare":
                    comparisons = ["old-vs-new"]
                for comparison in comparisons:
                    for step, label in enumerate("ABBA"):
                        verify_freeze()
                        remaining_wall = PLAN["budgets"]["wall_seconds_per_phase"] - (time.monotonic() - started)
                        remaining_global = GLOBAL_STOP - time.time()
                        remaining_timed = PLAN["budgets"]["timed_seconds_per_phase"] - state["timing_seconds"]
                        assert state["timing_seconds"] < PLAN["budgets"]["timed_seconds_per_phase"]
                        # Child wall time upper-bounds its timed work, so clipping
                        # by remaining timed budget is deliberately conservative.
                        timeout = min(PLAN["budgets"]["child_seconds"], remaining_wall, remaining_global, remaining_timed)
                        assert timeout > 0, "phase/global time exhausted before child"
                        adapter = comparison if phase == "aa" else ("old" if label == "A" else "new")
                        name = f"{phase}-b{block}-{cell['id']}-{comparison}-p{step}-{label}"
                        state["unknown_timed_work_on_failure"] = True
                        try:
                            stdout, _, record = execute(arguments(SCRATCH / adapter / "iterator", cell, seed), name, "raw", timeout)
                        except BaseException:
                            state["unknown_timed_work_on_failure"] = True
                            raise
                        row = csv_row(stdout, cell, seed)
                        result = dict(name=name, phase=phase, comparison=comparison, adapter=adapter,
                                      cell=cell["id"], block=block, seed=seed, step=step, label=label,
                                      operations=int(row["operations"]), elapsed_ns=int(row["elapsed_ns"]),
                                      ns_op=int(row["elapsed_ns"]) / int(row["operations"]),
                                      checksum=row["checksum"], tree_bytes=int(row["tree_bytes"]),
                                      csv=row, logs=record["logs"], started_utc=record["started_utc"],
                                      finished_utc=record["finished_utc"])
                        state["runs"].append(result)
                        state["timing_seconds"] += result["elapsed_ns"] / 1e9
                        state["unknown_timed_work_on_failure"] = False
                        with rows_path.open("a") as stream:
                            stream.write(json.dumps(result) + "\n")
                        save(OUT / (phase + "-state.json"), dict(status="running", completed_rows=len(state["runs"]),
                                                               timing_seconds=state["timing_seconds"], last=name))
                        # Retain the completed row before applying post-child limits.
                        assert state["timing_seconds"] <= PLAN["budgets"]["timed_seconds_per_phase"], "post-child timed budget"
                        assert time.monotonic() - started <= PLAN["budgets"]["wall_seconds_per_phase"], "post-child phase wall budget"
                        assert time.time() <= GLOBAL_STOP, "post-child absolute stop"
                        verify_freeze()
            print(phase, "block", block + 1, "/6 rows", len(state["runs"]), "timed_s", round(state["timing_seconds"], 3), flush=True)
        expected = 384 if phase == "aa" else 192
        assert len(state["runs"]) == expected
        state["results"] = derive(state["runs"], phase, controls)
        verify_freeze()
        assert state["timing_seconds"] <= PLAN["budgets"]["timed_seconds_per_phase"], "post-derive timed budget"
        assert time.monotonic() - started <= PLAN["budgets"]["wall_seconds_per_phase"], "post-derive phase wall budget"
        assert time.time() <= GLOBAL_STOP, "post-derive absolute stop"
        state["status"] = "complete"
    except BaseException as error:
        state.update(status="incomplete", failure=generic(repr(error)))
        raise
    finally:
        completed_children = [json.loads(line) for line in (OUT / "commands.jsonl").read_text().splitlines()
                              if json.loads(line)["name"].startswith(phase + "-")]
        all_reaped = all(child["process_reaped"] for child in completed_children)
        state.update(finished_utc=utc(), wall_seconds=time.monotonic() - started,
                     all_children_reaped=all_reaped)
        save(output, state)
        save(OUT / (phase + "-state.json"), dict(status=state["status"], completed_rows=len(state["runs"]),
                                               timing_seconds=state["timing_seconds"], all_children_reaped=all_reaped))
        lock.unlink()
    print(phase, "COMPLETE; harness diagnostic only; no source optimization acceptance", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "aa", "compare"))
    parser.add_argument("--ack", help="Root+independent review and published-freeze authorization JSON")
    args = parser.parse_args()
    if args.action == "prepare":
        prepare()
    else:
        assert args.ack, "explicit frozen publication/review ACK required"
        phase_run(args.action, args.ack)
