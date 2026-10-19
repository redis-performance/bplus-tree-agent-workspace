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
import re
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


def validate_config(config):
    worktree = (ROOT / config['worktree']).resolve()
    if not (worktree == ROOT or worktree.is_relative_to(ROOT / 'worktrees')) or not worktree.is_dir():
        raise ValueError('worktree must be this checkout or beneath worktrees/')
    host = config.get('host_label', 'apple-m1')
    if host not in ('apple-m1', 'apple-m6-mini'):
        raise ValueError('unexpected host label')
    expected = f'experiments/NIGHT-EXPLORATION-001/runs/{host}/'
    evidence = (worktree / config['campaign_dir']).resolve()
    if not config['campaign_dir'].startswith(expected) or not evidence.is_relative_to(worktree / expected):
        raise ValueError('unexpected campaign path')
    if not re.fullmatch(r'exploration/' + re.escape(host) + r'-[A-Za-z0-9-]+', config['branch']):
        raise ValueError('unexpected host branch')
    runtime = (worktree / config['runtime_dir']).resolve()
    if not runtime.is_relative_to(worktree / 'scratch'):
        raise ValueError('runtime must be beneath scratch/')
    return worktree


def publication_paths(config, requested):
    worktree = validate_config(config)
    paths = [config['campaign_dir'], 'experiments/EXPERIMENTS.md',
             'experiments/SUMMARY.md', 'experiments/NEXT-STEPS.md', 'README.md',
             '.workspace-memory/MEMORY.md', '.workspace-memory/LIVE-STATUS.md',
             '.workspace-memory/handoff.md']
    for value in requested:
        path = Path(value)
        if path.is_absolute() or '..' in path.parts or not path.parts:
            raise ValueError('invalid requested publication path')
        if path.parts[0] not in ('bench', 'scripts', 'tests', 'docs', 'experiments', 'compat') and value != 'Makefile':
            raise ValueError('requested path outside harness/documentation scope')
        if path.parts[0] == 'compat' and value not in ('compat/server.h', 'compat/standalone.c'):
            raise ValueError('only the two standalone adapter files may be published')
        if (value == 'tests/upstream.c' or (worktree / path).is_dir()
                or not (worktree / path).resolve().is_relative_to(worktree)):
            raise ValueError('referee entry point or external path cannot be published')
        if path.parts[0] == 'experiments' and not (worktree / path).resolve().is_relative_to(worktree / config['campaign_dir']):
            raise ValueError('cannot publish another campaign through a request')
        paths.append(value)
    return list(dict.fromkeys(paths))


def publish(config, round_number, requested=()):
    validate_config(config)
    worktree = (ROOT / config['worktree']).resolve()
    evidence = worktree / config['campaign_dir']
    paths = publication_paths(config, requested)
    if not evidence.exists():
        return 'No evidence directory yet'
    # All content is public; refuse obvious credential/private-path mistakes.
    # Split source literals so publishing this scanner does not match its own rules.
    # Runtime patterns remain exact, including the synthetic privacy test fixture.
    needles = (b'/' + b'Users/', b'gh' + b'o_', b'github' + b'_pat_',
               b'Authorization' + b': Bearer')
    for file in evidence.rglob('*'):
        if file.is_file() and file.suffix not in ('.svg', '.png'):
            payload = file.read_bytes()
            if any(needle in payload for needle in needles):
                raise RuntimeError(f'Public-evidence review required: {file.relative_to(evidence)}')
    for value in paths[1:]:
        file = worktree / value
        if file.is_file() and any(needle in file.read_bytes() for needle in needles):
            raise RuntimeError(f'Public-evidence review required: {value}')
    branch = run(['git', 'branch', '--show-current'], worktree)
    if branch != config['branch']:
        raise RuntimeError('Host branch changed unexpectedly')
    if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=worktree).returncode != 0:
        raise RuntimeError('Unexpected pre-staged changes; coordinator requires an exclusive Git writer')
    run(['git', 'add', '-A', '--', *paths], worktree)
    has_staged = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=worktree).returncode == 1
    if has_staged:
        host = config.get('host_label', 'apple-m1')
        run(['git', 'commit', '-m', f'Publish {host} campaign through round {round_number}'], worktree)
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
    try:
        worktree = validate_config(config)
    except ValueError as exc:
        parser.error(str(exc))
    runtime = worktree / config['runtime_dir'] / 'status.json'
    request_path = runtime.with_name('publish-request.json')
    ack_path = runtime.with_name('publish-ack.json')
    out = config_path.with_name(config_path.stem + '-sync-status.json')
    lock_path = config_path.with_name(config_path.stem + '-sync.lock')
    with lock_path.open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        completed = 0
        acknowledged = None
        while True:
            if not runtime.exists():
                time.sleep(args.interval_seconds)
                continue
            status = json.loads(runtime.read_text())
            finished = [r['round'] for r in status['rounds'] if r['status'] != 'running']
            latest = max(finished, default=0)
            final = status['status'] not in ('running', 'starting')
            request = json.loads(request_path.read_text()) if request_path.exists() else {}
            pending = bool(request.get('id')) and request['id'] != acknowledged
            if latest > completed or final or pending:
                result = {'checked_utc': now(), 'supervisor_status': status['status'],
                          'through_round': latest, 'branch': config['branch'],
                          'request_id': request.get('id') if pending else None}
                try:
                    result['publication'] = publish(config, latest, request.get('paths', []) if pending else [])
                    result['status'] = 'ok'
                    completed = latest
                    if pending:
                        acknowledged = request['id']
                except Exception as exc:
                    result['status'] = 'failed'
                    result['error'] = str(exc)
                    out.write_text(json.dumps(result, indent=2)+'\n')
                    if pending:
                        ack_path.write_text(json.dumps(result, indent=2)+'\n')
                    raise
                out.write_text(json.dumps(result, indent=2)+'\n')
                if pending:
                    tmp = ack_path.with_suffix('.tmp')
                    tmp.write_text(json.dumps(result, indent=2)+'\n')
                    tmp.replace(ack_path)
                print(f"{result['checked_utc']} {result['publication']}", flush=True)
            if final:
                break
            time.sleep(args.interval_seconds)


if __name__ == '__main__':
    main()
