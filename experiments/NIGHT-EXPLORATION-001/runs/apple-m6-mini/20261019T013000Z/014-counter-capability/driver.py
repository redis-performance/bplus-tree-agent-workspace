#!/usr/bin/env python3
"""Prepare metadata/probe; a separate reviewed ACK gates one self-only trace."""
import argparse
import hashlib
import json
import os
import re
import signal
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
REL = OUT.relative_to(ROOT)
SCR = Path("scratch/m6-counter-capability")
PLAN = json.loads((OUT / "PLAN.json").read_text())
TOOLS = {"xctrace": "/usr/bin/xctrace", "powermetrics": "/usr/bin/powermetrics"}


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    Path(path).write_text(json.dumps(data, indent=2) + "\n")


def generic(value):
    value = value.replace(str(ROOT), "<workspace>")
    value = re.sub(r"/" + r"Users/[^\s\"']+", "<user-path>", value)
    return re.sub(r"/" + r"(?:private/)?var/folders/[^\s\"']+", "<compiler-temp>", value)


def trace_size(path):
    return sum(p.stat().st_size for p in path.rglob("*") if p.is_file()) if path.exists() else 0


def command(args, name, timeout=30, public_output=False, watch_trace=None):
    """No implicit escalation, prompts, attachments, or collection retries."""
    SCR.mkdir(parents=True, exist_ok=True)
    raw = SCR / "logs"
    raw.mkdir(exist_ok=True)
    assert not (raw / (name + ".stdout")).exists(), ("no overwrite/retry", name)
    args = list(map(str, args))
    started = time.monotonic()
    record = dict(name=name, command=[generic(a) for a in args], started_utc=utc(),
                  timeout_seconds=timeout, timed_out=False, trace_cap_triggered=False)
    process = None
    stdout, stderr = "", ""
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, start_new_session=True)
        while True:
            left = timeout - (time.monotonic() - started)
            if left <= 0:
                record["timed_out"] = True
                break
            if watch_trace is not None and trace_size(watch_trace) > PLAN["bootstrap"]["private_trace_watchdog_bytes"]:
                record["trace_cap_triggered"] = True
                break
            try:
                stdout, stderr = process.communicate(timeout=min(.1, left))
                break
            except subprocess.TimeoutExpired:
                continue
    except BaseException as error:
        record["interrupted"] = generic(repr(error))
    finally:
        if process is not None and process.poll() is None:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        if process is not None:
            # Collect even when exit races the poll above. A broker may own the
            # target; recorder-group reaping alone never establishes target exit.
            try:
                stdout, stderr = process.communicate(timeout=8)
            except subprocess.TimeoutExpired as error:
                record["output_drain_timeout"] = True
                stdout = error.output or ""
                stderr = error.stderr or ""
                stdout = stdout.decode(errors="replace") if isinstance(stdout, bytes) else stdout
                stderr = stderr.decode(errors="replace") if isinstance(stderr, bytes) else stderr
                for pipe in (process.stdout, process.stderr):
                    if pipe is not None:
                        pipe.close()
                try:
                    process.wait(timeout=1)
                except subprocess.TimeoutExpired:
                    record["recorder_reap_incomplete"] = True
        record.update(returncode=process.returncode if process is not None else None,
                      process_spawned=process is not None,
                      process_reaped=process is None or process.poll() is not None,
                      finished_utc=utc(), wall_seconds=time.monotonic() - started)
        record["raw"] = {}
        for channel, text in (("stdout", stdout), ("stderr", stderr)):
            path = raw / (name + "." + channel)
            path.write_text(text)
            record["raw"][channel] = dict(location="ignored " + str(path), sha256=sha(path))
            if public_output:
                (OUT / "metadata" / (name + "." + channel)).write_text(generic(text))
        with (OUT / "commands.jsonl").open("a") as stream:
            stream.write(json.dumps(record) + "\n")
    return stdout, stderr, record


def metadata():
    destination = OUT / "metadata"
    destination.mkdir(exist_ok=False)
    calls = [("xctrace-help", [TOOLS["xctrace"], "help"]),
             ("record-help", [TOOLS["xctrace"], "help", "record"]),
             ("export-help", [TOOLS["xctrace"], "help", "export"]),
             ("list-help", [TOOLS["xctrace"], "help", "list"]),
             ("version", [TOOLS["xctrace"], "version"]),
             ("standard-templates", [TOOLS["xctrace"], "list", "templates"]),
             ("powermetrics-help", [TOOLS["powermetrics"], "--help"])]
    calls += [(name.lower().replace(" ", "-") + "-options",
               [TOOLS["xctrace"], "record", "--template", name, "--show-recording-options"])
              for name in ("CPU Counters", "CPU Profiler", "Processor Trace")]
    records = []
    for name, args in calls:
        stdout, _, result = command(args, name, public_output=True)
        assert result["returncode"] == 0 and not result["timed_out"]
        if name == "standard-templates":
            # Never publish an unrelated user template name, if installed.
            (destination / (name + ".stdout")).write_text("Advertised standard templates relevant to this task:\n" +
                "\n".join(n for n in ("CPU Counters", "CPU Profiler", "Processor Trace") if n in stdout.splitlines()) + "\n")
        if name.endswith("-options"):
            save(destination / (name + ".json"), json.loads(stdout))
        records.append(result)
    options = json.loads((destination / "cpu-counters-options.json").read_text())
    assert options["CPU Counters"]["countingLevel"] == "EL0"
    assert options["CPU Counters"]["selectedCountingModeDisplayName"] == "CPU Bottlenecks"
    options["Points of Interest"]["excludeOSLogs"] = True
    save(OUT / "recording-options.json", options)
    save(OUT / "capability.json", dict(status="METADATA ONLY", tool_version=(destination / "version.stdout").read_text().strip(),
         advertised_templates=["CPU Counters", "CPU Profiler", "Processor Trace"],
         counter_collection_started=False, probe_executed=False, permission="UNKNOWN",
         actual_counter_availability="UNKNOWN", exported_counter_schemas="UNKNOWN", own_process_scope="PENDING ROOT REVIEW",
         read_only_schema_method="--show-recording-options; local help explicitly says no recording starts and no target is required",
         powermetrics="Excluded: no target-process filter in inspected help", commands=len(records)))
    print("METADATA ONLY: no recording, attachment, counter collection or probe execution")


def build():
    assert not (OUT / "freeze.json").exists()
    assert (OUT / "capability.json").exists()
    obj, binary = SCR / "counter-probe.o", SCR / "counter-probe"
    flags = ["-std=c11", "-g", "-O3", "-Wall", "-Wextra", "-Werror", "-fno-omit-frame-pointer", "-fdebug-compilation-dir=."]
    for name, args in [("reviewed-compiler-version", ["clang", "--version"]),
                       ("reviewed-compile-probe", ["clang", *flags, "-c", REL / "counter-probe.c", "-o", obj]),
                       ("reviewed-link-probe", ["clang", "-g", obj, "-o", binary]),
                       ("reviewed-probe-dsym", ["dsymutil", binary, "-o", SCR / "counter-probe.dSYM"]),
                       ("reviewed-probe-disassembly", ["otool", "-tvV", binary])]:
        stdout, _, record = command(args, name, public_output=True)
        assert record["returncode"] == 0
        if name == "reviewed-probe-disassembly":
            assert "_qualification_alu:" in stdout and "eor" in stdout, "known work disappeared"
    files = [OUT / n for n in ("PLAN.json", "README.md", "driver.py", "counter-probe.c", "recording-options.json", "capability.json")]
    files += [p for p in (OUT / "metadata").iterdir() if p.is_file()]
    save(OUT / "freeze.json", dict(status="PREPARED ONLY; root/independent review and exclusive publication ACK pending",
         frozen_utc=utc(), files_sha256={str(p.relative_to(ROOT)): sha(p) for p in files},
         binary_sha256=sha(binary), object_sha256=sha(obj), xctrace_launcher_sha256=sha(TOOLS["xctrace"]),
         tool_launcher_sha256={name: sha(shutil.which(name)) for name in ("clang", "dsymutil", "otool")},
         dsym_files_sha256={str(p): sha(p) for p in (SCR / "counter-probe.dSYM").rglob("*") if p.is_file()},
         preparation_commands_sha256=sha(OUT / "commands.jsonl"), compiler_flags=flags,
         probe_executed=False, recording_started=False, tree_source_changed=False,
         participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact serving model/token/cost unknown"))
    print("BUILT/FROZEN, NOT EXECUTED: standalone known work; no tree/referee changes")


def observe_own_target(target_output, deadline):
    """Private owned start marker only; no process list, broad query or PID kill."""
    result = dict(target_exit_observed=False, target_reaped_by_driver=False,
                  exclusive_runner_release_safe=False)
    until = min(deadline, time.time() + 8)
    while time.time() < until:
        try:
            records = [json.loads(line) for line in target_output.read_text().splitlines()]
            starts = [r for r in records if r.get("event") == "started"]
            if len(starts) != 1:
                break
            pid = starts[0]["own_pid"]
            if not isinstance(pid, int) or pid <= 1:
                break
            result["owned_start_marker_observed"] = True
            try:
                os.kill(pid, 0)  # Existence observation only, never signals/kills.
            except ProcessLookupError:
                result.update(target_exit_observed=True, exclusive_runner_release_safe=True)
                break
            except PermissionError:
                break
        except (OSError, ValueError, KeyError, TypeError):
            break
        time.sleep(min(.05, max(0, until - time.time())))
    if target_output.exists():
        result["private_probe_output_sha256"] = sha(target_output)
        try:
            records = [json.loads(line) for line in target_output.read_text().splitlines()]
            starts = [r for r in records if r.get("event") == "started"]
            ends = [r for r in records if r.get("event") == "completed"]
            probe = ends[0] if len(ends) == 1 and len(starts) == 1 else {}
            result["probe_completed"] = (probe.get("own_pid") == starts[0]["own_pid"]
                and probe.get("case") == "alu" and probe.get("items") == PLAN["bootstrap"]["items"]
                and probe.get("seed") == 1 and probe.get("checksum") == PLAN["bootstrap"]["expected_checksum"])
            result["signposts_enabled"] = bool(probe.get("signposts_enabled", False))
        except (OSError, ValueError, KeyError, IndexError, TypeError):
            result["probe_completed"] = False
    return result


def availability(ack_path):
    """One bootstrap only. No table-row export or broader matrix exists here."""
    freeze = json.loads((OUT / "freeze.json").read_text())
    ack = json.loads(Path(ack_path).read_text())
    assert ack["status"] == "authorized" and ack["exclusive_runner"] is True
    for key, name in (("freeze_sha256", "freeze.json"), ("driver_sha256", "driver.py"), ("plan_sha256", "PLAN.json")):
        assert ack[key] == sha(OUT / name)
    assert ack["only_self_launch"] is True and ack["template_target_scope_reviewed"] is True
    assert ack["soft_trace_cap_understood"] is True and ack["stop_after_private_toc"] is True
    assert re.fullmatch(r"[0-9a-f]{40}", ack["published_commit"])
    assert any(r["reviewer"] == "/root" and r["status"] == "PASS" for r in ack["reviews"])
    assert any(r["reviewer"] != "/root" and r["status"] == "PASS" for r in ack["reviews"])
    deadline = datetime.fromisoformat(ack["absolute_stop_utc"]).timestamp()
    assert 20 < deadline - time.time() <= 600, "reserve drain/reap9seconds and owned-target observation8seconds"
    for path, digest in freeze["files_sha256"].items():
        assert sha(path) == digest
    binary = SCR / "counter-probe"
    assert sha(binary) == freeze["binary_sha256"] and sha(TOOLS["xctrace"]) == freeze["xctrace_launcher_sha256"]
    state_path = OUT / "availability.json"
    trace, target_output, toc = SCR / "availability.trace", SCR / "own-probe.jsonl", SCR / "availability-toc.xml"
    assert not any(p.exists() for p in (state_path, trace, target_output, toc)), "no collection retry/overwrite"
    save(state_path, dict(status="RUNNING ONE ROOT-AUTHORIZED BOOTSTRAP", started_utc=utc(), no_table_row_exports=True))
    args = [TOOLS["xctrace"], "record", "--template", "CPU Counters", "--recording-options", str((OUT / "recording-options.json").resolve()),
            "--no-prompt", "--time-limit", "4s", "--output", str(trace.resolve()),
            "--target-stdout", str(target_output.resolve()), "--launch", "--", str(binary.resolve()),
            "--case", "alu", "--items", "268435456"]
    # At most51seconds collection wait + bounded8second pipe drain +1second
    # reap, then up to8seconds owned-target observation, all before ACK deadline.
    stdout, stderr, record = command(args, "availability-record", min(51, deadline - time.time() - 17), watch_trace=trace)
    outcome = dict(record_returncode=record["returncode"], timed_out=record["timed_out"],
                   trace_cap_triggered=record["trace_cap_triggered"], trace_bytes=trace_size(trace),
                   no_table_row_exports=True, counters_qualified=False, scope_and_units="PENDING ROOT SCHEMA REVIEW")
    outcome.update(observe_own_target(target_output, deadline))
    outcome["recorder_reaped"] = record["process_reaped"]
    outcome["exclusive_runner_release_safe"] &= record["process_reaped"] and not record.get("output_drain_timeout", False)
    if (record["returncode"] != 0 or record["timed_out"] or record["trace_cap_triggered"]
            or "interrupted" in record or record.get("output_drain_timeout") or not record["process_reaped"]):
        outcome["status"] = "UNAVAILABLE/INCOMPLETE; preserve evidence, stop without retry or permission changes"
        save(state_path, outcome)
        return
    if not outcome["target_exit_observed"]:
        outcome["status"] = "INCOMPLETE: owned target exit unobserved; do not release exclusive runner"
        save(state_path, outcome)
        return
    left = deadline - time.time()
    if left <= 9:
        outcome["status"] = "INCOMPLETE: deadline before private TOC"
        save(state_path, outcome)
        return
    _, _, exported = command([TOOLS["xctrace"], "export", "--input", trace, "--toc", "--output", toc],
                              "availability-toc", min(21, left - 9))
    outcome["exclusive_runner_release_safe"] &= exported["process_reaped"] and not exported.get("output_drain_timeout", False)
    if (exported["returncode"] != 0 or not toc.exists() or exported["timed_out"]
            or "interrupted" in exported or exported.get("output_drain_timeout")
            or not exported["process_reaped"] or time.time() >= deadline):
        outcome["status"] = "INCOMPLETE: TOC unavailable"
    else:
        try:
            names = sorted({x.attrib["schema"] for x in ET.parse(toc).iter()
                            if "schema" in x.attrib and re.fullmatch(r"[A-Za-z0-9._-]{1,120}", x.attrib["schema"])})
            outcome.update(status="STOP FOR ROOT REVIEW: bootstrap recorded; no counter metric/unit/scope qualification yet",
                           private_toc_sha256=sha(toc), public_schema_names=names)
        except (ET.ParseError, OSError):
            outcome["status"] = "INCOMPLETE: invalid private TOC"
    if time.time() >= deadline:
        outcome["status"] = "INCOMPLETE: ACK deadline reached after TOC derivation"
    save(state_path, outcome)
    # No --xpath path, broad export, attach, all-process collection or escalation.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("metadata", "build", "availability"))
    parser.add_argument("--ack")
    args = parser.parse_args()
    if args.action == "availability":
        assert args.ack, "root/independent/published/exclusive ACK required; no collection authorized now"
        availability(args.ack)
    else:
        globals()[args.action]()
