#!/usr/bin/env python3
"""Read-only audit of the separately authorized ARM mask follow-up lease.

Reuses the reviewed recursive cgroup inspection from audit-aws-release.py, with
this lease's distinct unit names. Connection details remain in a private config.
A release marker alone is not proof: saved RUNNING status must match the live PID.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import runpy
import shlex
import subprocess
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--at', help='Optional timezone-aware ISO timestamp')
    args = parser.parse_args()
    if args.at:
        target = datetime.fromisoformat(args.at)
        if target.tzinfo is None:
            parser.error('--at requires timezone')
        while time.time() < target.timestamp():
            time.sleep(min(30, target.timestamp()-time.time()))
    cfg = json.loads(args.config.read_text())
    if cfg['owned_slice'] != 'bplus-mask-20261019.slice' or cfg['unit_prefix'] != 'bplus-maskjob-20261019-':
        parser.error('unexpected lease namespace')
    remote = runpy.run_path(str(Path(__file__).with_name('audit-aws-release.py')))['REMOTE']
    remote = remote.replace('/bplus.slice/bplus-night.slice/bplus-night-20261019.slice',
                            '/bplus.slice/bplus-mask.slice/bplus-mask-20261019.slice')
    remote = remote.replace('bplus-night-20261019.slice', cfg['owned_slice'])
    remote = remote.replace("'bplus-job-20261019-*', 'bplus-baseline-*'", "'bplus-maskjob-20261019-*'")
    remote = remote.replace('bplus-release-20261019.timer', 'bplus-mask-release-20261019.timer')
    assert 'bplus-night' not in remote and 'bplus-baseline' not in remote
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'host': 'AWS ARM Neoverse V2'}
    try:
        result = subprocess.run(['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=10',
            '-i', str(Path(cfg['ssh_key']).expanduser()), cfg['ssh_host'],
            'python3 - '+shlex.quote(cfg['lease_root'])], input=remote,
            text=True, capture_output=True, timeout=90)
        if result.returncode:
            record = {'verified_released': False, 'error': 'remote query failed', 'exit_code': result.returncode}
        else:
            record = json.loads(result.stdout)
            saved = re.search(r'\bRUNNING\s+pid (\d+)', record['saved_release_status'] or '')
            marker = datetime.fromisoformat(record['release_marker'].replace('Z', '+00:00')) if record['release_marker'] else None
            acquired = datetime.fromisoformat(cfg['acquired_at'])
            record['fresh_marker'] = bool(marker and acquired <= marker <= datetime.now(timezone.utc))
            record['saved_pid_matches_live'] = bool(saved and int(saved.group(1)) == record['coordinator_pid'])
            record['verified_released'] = bool(record['coordinator_running'] and record['fresh_marker'] and
                record['saved_pid_matches_live'] and record['slice_state'] == 'inactive' and
                record['units_query_ok'] and not record['active_owned_units'] and
                record['owned_cgroup_process_count'] == 0 and not record['inspection_errors'])
    except (OSError, ValueError, TypeError, KeyError, subprocess.TimeoutExpired):
        record = {'verified_released': False, 'error': 'query timeout or invalid response'}
    report['state'] = record
    report['finished_at'] = datetime.now(timezone.utc).isoformat()
    report['marker_semantics'] = 'Release-attempt start, not exact restoration completion'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix('.tmp')
    temporary.write_text(json.dumps(report, indent=2)+'\n')
    temporary.replace(args.output)
    print(json.dumps({'checked_at': report['checked_at'], 'verified_released': record['verified_released']}))


if __name__ == '__main__':
    main()
