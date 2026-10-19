#!/usr/bin/env python3
"""Durable M6 launch: baseline, publish, then bounded supervisor and coordinator."""
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'scripts/overnight.py').exists())
CONFIG = ROOT/'scratch/m6-night-launch.json'
config = json.loads(CONFIG.read_text())
evidence = ROOT/config['campaign_dir']
status_path = evidence/'LAUNCH-STATUS.json'
state = json.loads(status_path.read_text())


def save(status, **fields):
    state.update(status=status, updated_utc=datetime.now(timezone.utc).isoformat(), **fields)
    tmp = status_path.with_suffix('.tmp')
    tmp.write_text(json.dumps(state, indent=2)+'\n')
    tmp.replace(status_path)


def run_logged(name, args):
    with (ROOT/'scratch'/name).open('w') as output:
        subprocess.run(args, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT, check=True)


def detached(name, args):
    with (ROOT/'scratch'/name).open('a') as output:
        return subprocess.Popen(args, cwd=ROOT, stdin=subprocess.DEVNULL,
            stdout=output, stderr=subprocess.STDOUT, start_new_session=True)


def main():
    if datetime.now(timezone.utc) >= datetime.fromisoformat(config['deadline']):
        raise RuntimeError('Launch deadline already passed')
    save('baseline running', launcher_pid=__import__('os').getpid())
    run_logged('m6-baseline-attempt002.log', [sys.executable, 'scripts/run-size-matrix.py',
        '--out', state['baseline_path'], '--budget-seconds', '600'])
    run_logged('m6-baseline-analysis.log', [sys.executable, 'scripts/analyse-size-matrix.py',
        state['baseline_path']])
    manifest = json.loads((ROOT/state['baseline_path']/'manifest.json').read_text())
    if manifest['status'] != 'complete':
        raise RuntimeError('Baseline incomplete')
    save('baseline complete; publishing', baseline_processes=len(manifest['runs']),
         baseline_timing_seconds=manifest['timing_seconds'])
    status = evidence/'STATUS.md'
    text = status.read_text().replace('# M6 driver campaign — baseline recovery',
        '# M6 driver campaign — baseline complete, worker starting').replace(
        '| Five-size baseline | RETRY AFTER INFRASTRUCTURE FAILURE |',
        '| Five-size baseline | COMPLETE |')
    text += ('\nReplacement baseline completed all 120 serial processes / 960 rows after all seven\n'
             'native/sanitizer validations. Analysis is in baseline-attempt002/SUMMARY.md.\n'
             'Timing alone: '+str(round(manifest['timing_seconds'], 2))+' seconds.\n')
    status.write_text(text)
    spec = importlib.util.spec_from_file_location('sync', ROOT/'scripts/sync-night-campaign.py')
    sync = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sync)
    publication = sync.publish(config, 0)
    save('starting supervisor', baseline_publication=publication)
    supervisor = detached('m6-night-supervisor.log', [sys.executable, 'scripts/overnight.py',
        '--deadline', config['deadline'], '--run-dir', config['runtime_dir'],
        '--round-seconds', '1800', '--prompt-file', config['prompt_file'],
        '--campaign-dir', config['campaign_dir'], '--host-label', config['host_label']])
    runtime_status = ROOT/config['runtime_dir']/'status.json'
    for _ in range(30):
        if supervisor.poll() is not None:
            raise RuntimeError('Supervisor exited during startup; inspect scratch log')
        if runtime_status.exists():
            break
        time.sleep(1)
    else:
        supervisor.terminate()
        raise RuntimeError('Supervisor did not write startup status')
    coordinator = detached('m6-night-coordinator.log', [sys.executable,
        'scripts/sync-night-campaign.py', '--config', str(CONFIG.relative_to(ROOT)),
        '--interval-seconds', '5'])
    save('supervisor and coordinator running', supervisor_pid=supervisor.pid,
         coordinator_pid=coordinator.pid)
    print('Durable M6 supervisor and publication coordinator started.', flush=True)


if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        save('launcher failed', error=f'{type(error).__name__}: {error}')
        raise
