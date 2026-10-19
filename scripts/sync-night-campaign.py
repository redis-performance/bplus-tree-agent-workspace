#!/usr/bin/env python3
"""Publish a host campaign's completed-round evidence from outside the worker sandbox.

The Codex worker uses workspace-write and may be unable to create .git/index.lock
from an isolated worktree. This coordinator stages only its campaign evidence and
pushes only its host branch after each completed supervisor round. No force push.
"""
import argparse
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def now():
    return datetime.now(timezone.utc).isoformat()


def run(args, worktree):
    result = subprocess.run(args, cwd=worktree, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"{args[0]} {args[1:3]} failed: {result.stderr[-400:]}")
    return result.stdout.strip()


def publish(config, round_number):
    worktree = (ROOT / config['worktree']).resolve()
    evidence = worktree / config['campaign_dir']
    relative = config['campaign_dir']
    if not evidence.exists():
        return 'No evidence directory yet'
    # All content is public; refuse obvious credential/private-path mistakes.
    needles = (b'/Users/', b'gho_', b'github_pat_', b'Authorization: Bearer')
    for file in evidence.rglob('*'):
        if file.is_file() and file.suffix not in ('.svg', '.png'):
            payload = file.read_bytes()
            if any(needle in payload for needle in needles):
                raise RuntimeError(f'Public-evidence review required: {file.relative_to(evidence)}')
    branch = run(['git', 'branch', '--show-current'], worktree)
    if branch != config['branch']:
        raise RuntimeError('Host branch changed unexpectedly')
    run(['git', 'add', '-A', '--', relative], worktree)
    has_staged = subprocess.run(['git', 'diff', '--cached', '--quiet', '--', relative], cwd=worktree).returncode == 1
    if has_staged:
        run(['git', 'commit', '-m', f'Publish Apple M1 campaign through round {round_number}'], worktree)
    # Publish previous worker commits too; never rewrite the remote branch.
    run(['git', '-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential',
         'push', 'origin', branch], worktree)
    return f'Published {run(["git", "rev-parse", "--short", "HEAD"], worktree)}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    parser.add_argument('--interval-seconds', type=int, default=30)
    args = parser.parse_args()
    if not 5 <= args.interval_seconds <= 300:
        parser.error('interval-seconds must be 5..300')
    config_path = (ROOT / args.config).resolve()
    if not config_path.is_relative_to(ROOT / 'scratch'):
        parser.error('config must be beneath scratch/')
    config = json.loads(config_path.read_text())
    worktree = (ROOT / config['worktree']).resolve()
    if not worktree.is_relative_to(ROOT / 'worktrees') or not worktree.exists():
        parser.error('worktree must exist beneath worktrees/')
    if not config['campaign_dir'].startswith('experiments/NIGHT-EXPLORATION-001/runs/apple-m1/'):
        parser.error('unexpected campaign path')
    runtime = worktree / config['runtime_dir'] / 'status.json'
    out = config_path.with_name(config_path.stem + '-sync-status.json')
    lock_path = config_path.with_name(config_path.stem + '-sync.lock')
    with lock_path.open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        completed = 0
        while True:
            if not runtime.exists():
                time.sleep(args.interval_seconds)
                continue
            status = json.loads(runtime.read_text())
            finished = [r['round'] for r in status['rounds'] if r['status'] != 'running']
            latest = max(finished, default=0)
            final = status['status'] not in ('running', 'starting')
            if latest > completed or final:
                result = {'checked_utc': now(), 'supervisor_status': status['status'],
                          'through_round': latest, 'branch': config['branch']}
                try:
                    result['publication'] = publish(config, latest)
                    result['status'] = 'ok'
                    completed = latest
                except Exception as exc:
                    result['status'] = 'failed'
                    result['error'] = str(exc)
                    out.write_text(json.dumps(result, indent=2)+'\n')
                    raise
                out.write_text(json.dumps(result, indent=2)+'\n')
                print(f"{result['checked_utc']} {result['publication']}", flush=True)
            if final:
                break
            time.sleep(args.interval_seconds)


if __name__ == '__main__':
    main()
