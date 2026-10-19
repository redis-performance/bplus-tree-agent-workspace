#!/usr/bin/env python3
"""Run one owned fleet job in a deadline-bounded systemd cgroup, without host addresses.

Invoke on the reserved runner. The lease JSON is private operational state outside
the checkout. A system timer independently stops the entire campaign slice.
"""
import argparse
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import re
import subprocess
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lease', required=True, type=Path)
    parser.add_argument('--name', required=True)
    parser.add_argument('--seconds', required=True, type=int)
    parser.add_argument('--script', required=True, type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,70}', args.name):
        parser.error('invalid unit suffix')
    lease = json.loads(args.lease.read_text())
    root = Path(lease['root']).resolve()
    script = args.script.resolve()
    if not script.is_relative_to(root) or not script.is_file():
        parser.error('script must exist beneath the leased checkout')
    remaining = int(datetime.fromisoformat(lease['deadline']).timestamp() - time.time()) - 10
    if (args.lease.parent / 'LEASE-RELEASED').exists() or remaining < 30:
        parser.error('lease is released or expired')
    if not 1 <= args.seconds <= min(1800, remaining):
        parser.error('job must fit within lease, maximum 1800 seconds')
    with (args.lease.parent / 'job.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if subprocess.run(['systemctl', 'is-active', '--quiet', 'bplus-baseline-20261019.service']).returncode == 0:
            parser.error('baseline is still running')
        active = subprocess.check_output(
            ['systemctl', 'list-units', '--no-legend', '--plain',
             '--state=activating,active,deactivating', lease['unit_prefix'] + '*.service'], text=True)
        if active.strip():
            parser.error('an earlier owned job is still active')
        unit = lease['unit_prefix'] + args.name
        command = ['sudo', '-n', 'systemd-run', '--quiet', '--wait', '--collect',
                   '--unit=' + unit, '--slice=' + lease['slice'], '--uid=ubuntu',
                   '--property=WorkingDirectory=' + str(root),
                   '--property=RuntimeMaxSec=' + str(args.seconds),
                   '--property=TimeoutStopSec=5', '--property=KillMode=control-group',
                   '--property=StandardOutput=append:' + str(script) + '.stdout',
                   '--property=StandardError=append:' + str(script) + '.stderr',
                   '/usr/bin/taskset', '-c', str(lease['cpu']), '/bin/bash', str(script)]
        start = datetime.now(timezone.utc).isoformat()
        try:
            result = subprocess.run(command, timeout=args.seconds + 20)
            code = result.returncode
        except subprocess.TimeoutExpired:
            subprocess.run(['sudo', '-n', 'systemctl', 'stop', unit], timeout=15)
            code = 124
        record = dict(started_utc=start, finished_utc=datetime.now(timezone.utc).isoformat(),
                      unit=unit, cpu=lease['cpu'], limit_seconds=args.seconds, returncode=code)
        script.with_suffix(script.suffix + '.job.json').write_text(json.dumps(record, indent=2)+'\n')
        print(json.dumps(record), flush=True)
        raise SystemExit(code)


if __name__ == '__main__':
    main()

