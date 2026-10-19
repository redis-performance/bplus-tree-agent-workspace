#!/usr/bin/env python3
"""Read-only release verification; connection details stay in private config.

The independent host timers perform restoration. This script merely checks live
state after a requested time and writes generic evidence, never changing services.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shlex
import subprocess
import time


REMOTE = r'''
import json, pathlib, re, subprocess, sys
root = pathlib.Path(sys.argv[1])
def command(args):
    r = subprocess.run(args, text=True, capture_output=True, timeout=20)
    return r.returncode, r.stdout.strip()
code, status = command(['sudo', '-n', 'supervisorctl', 'status', 'redis-benchmarks-spec-sc-coordinator'])
match = re.search(r'\bRUNNING\s+pid (\d+)', status)
pid = int(match.group(1)) if match else 0
_, slice_state = command(['systemctl', 'show', 'bplus-night-20261019.slice', '--property=ActiveState', '--value'])
units_code, units = command(['systemctl', 'list-units', 'bplus-job-20261019-*', 'bplus-baseline-*', '--state=active,activating,deactivating', '--no-legend', '--plain'])
_, timer = command(['systemctl', 'show', 'bplus-release-20261019.timer', '--property=NextElapseUSecRealtime', '--value'])
marker = root/'LEASE-RELEASED'
saved = root/'released-status.txt'
cgroup = pathlib.Path('/sys/fs/cgroup/bplus-night-20261019.slice')
errors = []
processes = []
try:
    for f in cgroup.rglob('cgroup.procs'):
        processes.extend(f.read_text().split())
except OSError:
    errors.append('could not inspect owned cgroup')
print(json.dumps(dict(coordinator_running=code == 0 and pid > 0 and pathlib.Path('/proc', str(pid)).exists(),
    coordinator_pid=pid,
    coordinator_status=status, slice_state=slice_state,
    active_owned_units=units.splitlines(), units_query_ok=units_code == 0,
    owned_cgroup_process_count=len(set(processes)), inspection_errors=errors,
    release_marker=marker.read_text().strip() if marker.exists() else None,
    saved_release_status=saved.read_text().strip() if saved.exists() else None,
    release_timer_next=timer)))
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--identity', type=Path, required=True)
    parser.add_argument('--at', help='Timezone-aware ISO timestamp; omit for immediate check')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.at:
        target = datetime.fromisoformat(args.at)
        if target.tzinfo is None:
            parser.error('--at must include timezone')
        while time.time() < target.timestamp():
            time.sleep(min(30, target.timestamp() - time.time()))
    config = json.loads(args.config.read_text())
    if set(config['hosts']) != {'intel', 'amd', 'arm'}:
        parser.error('config must identify exactly intel, amd and arm')
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'hosts': {}}
    for label, host in config['hosts'].items():
        try:
            result = subprocess.run(['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=10',
                '-i', str(args.identity.expanduser()), 'ubuntu@' + host,
                'python3 - ' + shlex.quote(config['remote_root'])], input=REMOTE,
                text=True, capture_output=True, timeout=90)
            if result.returncode:
                record = {'verified_released': False, 'error': 'remote query failed',
                          'exit_code': result.returncode}
            else:
                record = json.loads(result.stdout)
                record['verified_released'] = bool(record['coordinator_running'] and
                    record['release_marker'] and record['saved_release_status'] and
                    record['slice_state'] == 'inactive' and record['units_query_ok'] and
                    not record['active_owned_units'] and
                    record['owned_cgroup_process_count'] == 0 and not record['inspection_errors'])
        except (subprocess.TimeoutExpired, ValueError, OSError):
            record = {'verified_released': False, 'error': 'query timeout or invalid response'}
        report['hosts'][label] = record
    report['all_released'] = all(v['verified_released'] for v in report['hosts'].values())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix('.tmp')
    temporary.write_text(json.dumps(report, indent=2) + '\n')
    temporary.replace(args.output)
    print(json.dumps({'checked_at': report['checked_at'], 'all_released': report['all_released']}))


if __name__ == '__main__':
    main()
