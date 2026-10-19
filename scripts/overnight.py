#!/usr/bin/env python3
"""Run serial, bounded Codex experiment rounds until an explicit UTC deadline.

Full transcripts stay in ignored scratch/. No credentials or permission overrides.
"""
import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import time

ROOT = Path(__file__).resolve().parent.parent


def utc():
    return datetime.now(timezone.utc).isoformat()


def atomic_json(path, data):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n")
    tmp.replace(path)


def process_table():
    result = subprocess.run(["ps", "-axo", "pid=,ppid=,lstart="],
                            capture_output=True, text=True, check=True)
    rows = {}
    for line in result.stdout.splitlines():
        fields = line.split(None, 2)
        if len(fields) == 3:
            rows[int(fields[0])] = (int(fields[1]), fields[2])
    return rows


def remember_children(pid, known):
    rows = process_table()
    parents = {pid} | {p for p, stamp in known.items()
                       if p in rows and rows[p][1] == stamp}
    while True:
        children = {p for p, (parent, _) in rows.items() if parent in parents}
        if children <= parents:
            break
        parents |= children
    for p in parents:
        if p in rows:
            known[p] = rows[p][1]


def stop_worker(worker, known):
    """Stop only our worker and observed descendants, including separate sessions."""
    remember_children(worker.pid, known)
    for sig in (signal.SIGTERM, signal.SIGKILL):
        rows = process_table()
        for pid, stamp in known.items():
            if pid in rows and rows[pid][1] == stamp:
                try:
                    os.kill(pid, sig)
                except ProcessLookupError:
                    pass
        if sig == signal.SIGTERM:
            time.sleep(2)
    worker.wait(timeout=10)


def usage_from(path):
    usage = {}
    completed = False
    try:
        for line in path.read_text().splitlines():
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if item.get("type") == "turn.completed":
                completed = True
                for key, value in item.get("usage", {}).items():
                    if isinstance(value, (int, float)):
                        usage[key] = usage.get(key, 0) + value
    except OSError:
        pass
    return completed, usage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deadline", required=True, help="ISO timestamp with timezone")
    parser.add_argument("--run-dir", required=True, help="New directory beneath scratch/")
    parser.add_argument("--round-seconds", type=int, default=1800)
    parser.add_argument("--prompt-file", default="docs/OVERNIGHT-PROMPT.md")
    parser.add_argument("--campaign-dir", default="experiments/OVERNIGHT-2026-10-17",
                        help="Host-specific evidence directory beneath experiments/")
    parser.add_argument("--host-label", default="unspecified",
                        help="Directory-safe label; actual CPU must be recorded separately")
    args = parser.parse_args()
    deadline = datetime.fromisoformat(args.deadline)
    if deadline.tzinfo is None or deadline.timestamp() <= time.time():
        parser.error("deadline must be in the future with an explicit timezone")
    if not 60 <= args.round_seconds <= 3600:
        parser.error("round-seconds must be 60..3600")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.host_label):
        parser.error("host-label must contain lowercase letters, digits and hyphens")
    campaign_dir = (ROOT / args.campaign_dir).resolve()
    if not campaign_dir.is_relative_to(ROOT / "experiments") or campaign_dir == ROOT / "experiments":
        parser.error("campaign-dir must be a directory beneath experiments/")
    template_path = (ROOT / args.prompt_file).resolve()
    if not template_path.is_relative_to(ROOT) or not template_path.is_file():
        parser.error("prompt-file must be an existing file inside the repository")
    template = template_path.read_text()
    run_dir = (ROOT / args.run_dir).resolve()
    if not run_dir.is_relative_to(ROOT / "scratch"):
        parser.error("run-dir must be beneath this repository's scratch/")
    (ROOT / "scratch").mkdir(exist_ok=True)
    lock = (ROOT / "scratch/overnight.lock").open("a+")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock.close()
        parser.error("an overnight supervisor already holds the lock")
    run_dir.mkdir(exist_ok=False)
    codex = shutil.which("codex")
    if not codex:
        parser.error("codex is not installed")
    (run_dir / "prompt-template.md").write_text(template)
    stop_requested = False

    def request_stop(_sig, _frame):
        nonlocal stop_requested
        stop_requested = True

    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)
    state = {"started_utc": utc(), "deadline_utc": deadline.isoformat(),
             "supervisor_pid": os.getpid(), "status": "starting", "rounds": [],
             "prompt_sha256": hashlib.sha256(template.encode()).hexdigest(),
             "prompt_file": str(template_path.relative_to(ROOT)),
             "campaign_dir": str(campaign_dir.relative_to(ROOT)),
             "host_label": args.host_label,
             "round_limit_seconds": args.round_seconds,
             "sandbox": "workspace-write", "publication": "local drafts; no automatic push"}
    (run_dir / "supervisor.pid").write_text(str(os.getpid()) + "\n")
    awake = None
    worker = None
    known = {}
    if shutil.which("caffeinate"):
        awake = subprocess.Popen(["caffeinate", "-i", "-t",
                                  str(math.ceil(deadline.timestamp() - time.time())),
                                  "-w", str(os.getpid())],
                                 stdin=subprocess.DEVNULL,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    failures = 0
    try:
        while time.time() < deadline.timestamp():
            if stop_requested or (run_dir / "STOP").exists():
                state["status"] = "stopped_by_request"
                break
            index = len(state["rounds"]) + 1
            current = run_dir / f"round-{index:03d}"
            current.mkdir()
            remaining = deadline.timestamp() - time.time()
            limit = min(args.round_seconds, remaining)
            final_round = remaining <= args.round_seconds
            end = datetime.fromtimestamp(time.time() + limit, timezone.utc).isoformat()
            prompt = (template + f"\nRound: {index}. Current UTC: {utc()}. "
                      f"This round ends: {end}. Campaign ends: {deadline.isoformat()}.\n"
                      f"Final round: {final_round}. Runtime directory: {run_dir.relative_to(ROOT)}.\n"
                      f"Host label: {args.host_label}. Evidence directory: {campaign_dir.relative_to(ROOT)}.\n"
                      "Read previous round reports here before choosing work. "
                      "Finish active work and save a handoff at least 90 seconds before round end.\n")
            (current / "prompt.md").write_text(prompt)
            record = {"round": index, "started_utc": utc(), "deadline_utc": end,
                      "status": "running"}
            state["rounds"].append(record)
            state["status"] = "running"
            command = [codex, "exec", "--ephemeral", "--json", "--sandbox", "workspace-write",
                       "-C", str(ROOT), "-o", str(current / "report.md"), "-"]
            with (current / "events.jsonl").open("w") as out, (current / "stderr.log").open("w") as err:
                worker = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=out,
                                          stderr=err, cwd=ROOT, start_new_session=True)
                worker.stdin.write(prompt.encode())
                worker.stdin.close()
                known = {}
                record["worker_pid"] = worker.pid
                round_end = time.monotonic() + limit
                while worker.poll() is None:
                    remember_children(worker.pid, known)
                    state["heartbeat_utc"] = utc()
                    atomic_json(run_dir / "status.json", state)
                    if stop_requested or (run_dir / "STOP").exists():
                        record["status"] = "stopped_by_request"
                        break
                    if time.monotonic() >= round_end or time.time() >= deadline.timestamp():
                        record["status"] = "timed_out"
                        break
                    time.sleep(5)
                stop_worker(worker, known)
                record["exit_code"] = worker.returncode
                record["finished_utc"] = utc()
                completed, usage = usage_from(current / "events.jsonl")
                record["usage"] = usage
                if record["status"] == "running":
                    record["status"] = "completed" if worker.returncode == 0 and completed else "failed"
                worker = None
            # Consecutive infrastructure failures stop the loop instead of burning quota.
            failures = 0 if record["status"] == "completed" else failures + 1
            state["heartbeat_utc"] = utc()
            atomic_json(run_dir / "status.json", state)
            if (campaign_dir / "BLOCKED.md").exists():
                state["status"] = "blocked_reported_by_worker"
                break
            if failures >= 3:
                state["status"] = "blocked_after_three_failed_rounds"
                break
            if record["status"] == "stopped_by_request":
                state["status"] = "stopped_by_request"
                break
            # Avoid spinning on immediate authentication/connection failures.
            if record["status"] != "completed":
                for _ in range(12):
                    if stop_requested or (run_dir / "STOP").exists() or time.time() >= deadline.timestamp():
                        break
                    time.sleep(5)
        else:
            state["status"] = "deadline_reached"
    except BaseException as exc:
        state["status"] = "supervisor_error"
        state["error"] = type(exc).__name__ + ": " + str(exc)
        raise
    finally:
        if worker is not None:
            stop_worker(worker, known)
        if awake is not None:
            awake.terminate()
            awake.wait(timeout=10)
        state["finished_utc"] = utc()
        state["heartbeat_utc"] = utc()
        atomic_json(run_dir / "status.json", state)
        lock.close()


if __name__ == "__main__":
    main()
