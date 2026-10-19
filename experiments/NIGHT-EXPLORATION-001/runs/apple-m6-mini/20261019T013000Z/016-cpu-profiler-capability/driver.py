#!/usr/bin/env python3
"""One gated CPU Profiler own-target capability attempt. No prepare/build/metadata action."""
import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
REL = OUT.relative_to(ROOT)
SCR = Path("scratch/m6-cpu-profiler-capability")
PLAN = json.loads((OUT / "PLAN.json").read_text())
TOOLS = {"xctrace": "/usr/bin/xctrace"}
PROBE = Path("scratch/m6-counter-capability/counter-probe")


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
    freeze = json.loads((OUT / "freeze.json").read_text())
    ack = json.loads(Path(ack_path).read_text())
    assert ack["status"] == "authorized" and ack["exclusive_runner"] is True
    for key, name in (("freeze_sha256", "freeze.json"), ("driver_sha256", "driver.py"), ("plan_sha256", "PLAN.json")):
        assert ack[key] == sha(OUT / name)
    assert ack["only_self_launch"] is True and ack["template_target_scope_reviewed"] is True
    assert ack["soft_trace_cap_understood"] is True and ack["stop_after_private_toc"] is True
    assert ack["prior_counter_review_did_not_resolve_capability"] is True
    assert re.fullmatch(r"[0-9a-f]{40}", ack["published_commit"])
    assert any(r["reviewer"] == "/root" and r["status"] == "PASS" for r in ack["reviews"])
    assert any(r["reviewer"] not in ("/root", "/root/followup_proposal_a") and r["status"] == "PASS" for r in ack["reviews"])
    deadline = datetime.fromisoformat(ack["absolute_stop_utc"]).timestamp()
    assert 20 < deadline - time.time() <= 600
    assert deadline <= datetime.fromisoformat(PLAN["absolute_campaign_stop_utc"]).timestamp()
    for path, digest in freeze["files_sha256"].items():
        assert sha(path) == digest
    assert sha(PROBE) == freeze["binary_sha256"]
    assert sha(TOOLS["xctrace"]) == freeze["xctrace_launcher_sha256"]
    state_path = OUT / "availability.json"
    trace, target_output, toc = SCR / "availability.trace", SCR / "own-probe.jsonl", SCR / "availability-toc.xml"
    assert not any(p.exists() for p in (state_path, trace, target_output, toc)), "no collection retry/overwrite"
    args = [TOOLS["xctrace"], "record", "--template", "CPU Profiler", "--recording-options", str((OUT / "recording-options.json").resolve()),
            "--no-prompt", "--time-limit", "4s", "--output", str(trace.resolve()),
            "--target-stdout", str(target_output.resolve()), "--launch", "--", str(PROBE.resolve()),
            "--case", "alu", "--items", "268435456"]
    planned = json.loads((OUT / "planned-command.json").read_text())
    assert [generic(x) for x in args] == planned["command"]
    assert planned["count"] == 1 and planned["collection_wait_limit_seconds"] == 51
    assert deadline - time.time() > 17, "reserve bounded cleanup and owned-target observation"
    save(state_path, dict(status="RUNNING ONE ROOT-AUTHORIZED CPU PROFILER BOOTSTRAP", started_utc=utc(), no_table_row_exports=True))
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
    if not outcome.get("probe_completed", False) or not outcome.get("signposts_enabled", False):
        outcome["status"] = "INCOMPLETE: invalid known-work checksum/completion or signposted interval"
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
            outcome.update(status="STOP FOR ROOT REVIEW: CPU Profiler bootstrap recorded; weights/units/scope unqualified",
                           private_toc_sha256=sha(toc), public_schema_names=names,
                           cpu_profile_named_schema_present="cpu-profile" in names)
        except (ET.ParseError, OSError):
            outcome["status"] = "INCOMPLETE: invalid private TOC"
    if time.time() >= deadline:
        outcome["status"] = "INCOMPLETE: ACK deadline reached after TOC derivation"
    save(state_path, outcome)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("availability",))
    parser.add_argument("--ack", required=True)
    arguments = parser.parse_args()
    availability(arguments.ack)
