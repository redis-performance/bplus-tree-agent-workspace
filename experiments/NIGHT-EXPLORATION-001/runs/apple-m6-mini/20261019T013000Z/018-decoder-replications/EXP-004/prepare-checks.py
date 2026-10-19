#!/usr/bin/env python3
"""Preparation checks only; never runs a decoder matrix or profile."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, re, signal, subprocess, time

ROOT = Path.cwd()
WT = ROOT / 'worktrees/m6-replica-exp004'
OUT = ROOT / 'experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications/EXP-004'
SCR = ROOT / 'scratch/m6-replica-exp004-preparation'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def generic(text):
    text = text.replace(str(ROOT), '<workspace>')
    text = re.sub(r'/' + r'Users/[^\s"\']+', '<user-path>', text)
    text = re.sub(r'/' + r'private/var/folders/[^\s"\']+', '<compiler-temp>', text)
    return re.sub(r'^InstalledDir:.*$', 'InstalledDir: <compiler-installation>', text, flags=re.M)

SCR.mkdir(parents=True, exist_ok=False)
(OUT / 'logs').mkdir()
records = []
for name, args in [('decoder-check', ['make', 'decoder-check']),
                   ('decoder-sanitize', ['make', 'decoder-sanitize']),
                   ('upstream-native', ['make', 'check']),
                   ('upstream-sanitize', ['make', 'sanitize'])]:
    record = dict(name=name, command=args, cwd='worktrees/m6-replica-exp004',
                  timeout_seconds=180, started_utc=datetime.now(timezone.utc).isoformat(), timed_out=False)
    started = time.monotonic()
    process = None
    try:
        with (SCR / (name + '.stdout')).open('w') as stdout, (SCR / (name + '.stderr')).open('w') as stderr:
            process = subprocess.Popen(args, cwd=WT, stdout=stdout, stderr=stderr, start_new_session=True)
            try:
                process.wait(timeout=180)
            except subprocess.TimeoutExpired:
                record['timed_out'] = True
                os.killpg(process.pid, signal.SIGKILL)
                process.wait(timeout=10)
    except BaseException as error:
        record['failure'] = generic(repr(error))
        if process is not None and process.poll() is None:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait(timeout=10)
    finally:
        record.update(returncode=process.returncode if process is not None else None,
                      process_reaped=process is None or process.poll() is not None,
                      finished_utc=datetime.now(timezone.utc).isoformat(),
                      wall_seconds=time.monotonic() - started, logs={})
        for stream in ('stdout', 'stderr'):
            raw = SCR / (name + '.' + stream)
            public = OUT / 'logs' / (name + '.' + stream)
            public.write_text(generic(raw.read_text() if raw.exists() else ''))
            record['logs'][stream] = dict(public_file=str(public.relative_to(OUT)), public_sha256=sha(public),
                original_raw=str(raw.relative_to(ROOT)), original_raw_sha256=sha(raw) if raw.exists() else None)
        records.append(record)
        (OUT / 'commands.json').write_text(json.dumps(records, indent=2) + '\n')
    print(name, record['returncode'], 'reaped', record['process_reaped'], flush=True)
    if record['returncode'] != 0 or record['timed_out'] or 'failure' in record:
        raise SystemExit('Preparation stopped; preserve failure, no retry')
print('PREPARATION COMMANDS COMPLETE; NO MATRIX OR PROFILE', flush=True)
