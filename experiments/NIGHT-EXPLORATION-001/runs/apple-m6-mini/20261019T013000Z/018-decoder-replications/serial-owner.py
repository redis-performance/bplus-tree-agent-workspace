#!/usr/bin/env python3
"""Own one unchanged canonical phase and its process group, with an absolute cutoff."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
PHASES = {
    '007-profile-base': ('007', ['experiments/EXP-007/profile.py', 'base', '--out-dir', 'build/m6-replications/EXP007/profiles'], 40),
    '007-profile-B': ('007', ['experiments/EXP-007/profile.py', 'B', '--out-dir', 'build/m6-replications/EXP007/profiles'], 40),
    '008-profile-base': ('008', ['experiments/EXP-008/profile.py', 'base', '--out-dir', 'build/m6-replications/EXP008/profiles'], 40),
    '004-discovery': ('004', ['scripts/run-decoder.py', '--out', 'build/m6-replications/EXP004/discovery', '--budget-seconds', '300'], 360),
    '007-discovery': ('007', ['experiments/EXP-007/run.py', '--out', 'build/m6-replications/EXP007/discovery', '--budget-seconds', '300'], 360),
    '008-discovery': ('008', ['experiments/EXP-008/run.py', '--out', 'build/m6-replications/EXP008/discovery', '--budget-seconds', '300'], 360),
}

def utc():
    return datetime.now(timezone.utc).isoformat()

def alive(pgid):
    try:
        os.killpg(pgid, 0)
        return True
    except ProcessLookupError:
        return False

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=PHASES)
    args = parser.parse_args()
    tag, command, bound = PHASES[args.phase]
    cwd = ROOT / 'worktrees' / ('m6-replica-exp' + tag)
    assert (cwd / command[0]).is_file(), cwd
    record_path = OUT / (args.phase + '-owner.json')
    if record_path.exists():
        raise SystemExit('Existing phase record; no automatic retry')
    cutoff = datetime(2026, 10, 19, 7, 15, tzinfo=timezone.utc).timestamp()
    if time.time() + bound + 10 >= cutoff:
        raise SystemExit('Insufficient time before experimental cutoff')
    scratch = ROOT / 'scratch' / 'm6-decoder-replication-phases'
    scratch.mkdir(exist_ok=True)
    for stream in ('stdout', 'stderr'):
        if (scratch / (args.phase + '.' + stream)).exists():
            raise SystemExit('Existing private phase log; no overwrite')
    if 'profile' in args.phase:
        variant = command[1]
        profile_dir = cwd / command[-1]
        for suffix in ('-profile.csv', '-profile.stderr', '-sample.txt', '-sampling.json'):
            if (profile_dir / (variant + suffix)).exists():
                raise SystemExit('Existing profile artifact; no overwrite')
    elif (cwd / command[2]).exists():
        raise SystemExit('Existing matrix directory; no overwrite')
    record = dict(phase=args.phase, command=['python3'] + command,
                  cwd=str(cwd.relative_to(ROOT)), bound_seconds=bound,
                  absolute_cutoff_utc='2026-10-19T07:15:00+00:00', started_utc=utc())
    record_path.write_text(json.dumps(record, indent=2) + '\n')
    def cancelled(signum, frame):
        raise KeyboardInterrupt('Owner received signal ' + str(signum))
    for signum in (signal.SIGTERM, signal.SIGHUP):
        signal.signal(signum, cancelled)
    child = None
    started = time.monotonic()
    try:
        with (scratch / (args.phase + '.stdout')).open('xb') as so, (scratch / (args.phase + '.stderr')).open('xb') as se:
            child = subprocess.Popen(['python3'] + command, cwd=cwd, stdout=so, stderr=se, start_new_session=True)
            record['owned_process_group'] = child.pid
            while child.poll() is None:
                if time.monotonic() - started >= bound or time.time() >= cutoff:
                    record['timed_out'] = True
                    break
                time.sleep(0.2)
    except BaseException as exc:
        record['exception_type'] = type(exc).__name__
        raise
    finally:
        if child is not None:
            # Also clean up target/sampler descendants after a failed driver's exit.
            if alive(child.pid):
                try:
                    os.killpg(child.pid, signal.SIGKILL)
                    record['owned_group_killed'] = True
                except ProcessLookupError:
                    record['owned_group_exited_before_kill'] = True
            try:
                child.wait(timeout=5)
                record['driver_reaped'] = True
            except subprocess.TimeoutExpired:
                record['driver_reaped'] = False
            deadline = time.monotonic() + 3
            while alive(child.pid) and time.monotonic() < deadline:
                time.sleep(0.1)
            record['owned_group_empty'] = not alive(child.pid)
            record['returncode'] = child.returncode
        record.update(ended_utc=utc(), wall_seconds=time.monotonic() - started)
        record['logs'] = {}
        for stream in ('stdout', 'stderr'):
            p = scratch / (args.phase + '.' + stream)
            if p.exists():
                record['logs'][stream] = dict(path=str(p.relative_to(ROOT)), sha256=hashlib.sha256(p.read_bytes()).hexdigest(), bytes=p.stat().st_size)
        record['exclusive_release_safe'] = bool(record.get('driver_reaped') and record.get('owned_group_empty'))
        record_path.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record))
    if record.get('returncode') != 0 or not record['exclusive_release_safe'] or record.get('timed_out'):
        raise SystemExit(1)

if __name__ == '__main__':
    main()
