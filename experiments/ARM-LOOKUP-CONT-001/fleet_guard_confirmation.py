#!/usr/bin/env python3
"""Fleet-only fresh-seed guard confirmation using original immutable base/B ELFs."""
import argparse
import hashlib
import json
import math
import os
import pathlib
import subprocess
import sys
import time

EXP = pathlib.Path('experiments/ARM-LOOKUP-CONT-001')
CASES = {'iterator-forward': 1000000, 'iterator-reverse': 1000000,
         'rank-forward': 200000, 'rank-reverse': 200000, 'churn': 20000}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def checked_blocks(report, variant, qualification=False):
    blocks = [b for b in report['blocks'] if b['variant'] == variant]
    expected = {(case, block) for case in CASES for block in range(3)}
    require(len(blocks) == 15 and
            {(b['case'], b['block']) for b in blocks} == expected,
            'Missing or duplicated guard blocks for ' + variant)
    if qualification:
        require(report['pass'] is True and report['rows'] == 60 and
                len(report['blocks']) == 15, 'Original/new A/A did not qualify')
    for b in blocks:
        delta = b['delta_pct']
        memory = b['memory_delta_pct']
        require(b['passed'] is True and math.isfinite(delta) and
                (abs(delta) <= 1 if qualification else delta <= 1) and
                b['min_window_ns'] >= 250000000 and
                set(memory) == {'owned_bytes_before', 'owned_bytes_after'} and
                all(math.isfinite(v) and v <= 1 for v in memory.values()),
                'Failed guard block for ' + variant)


def leasecheck(root):
    d = read(root / 'reservation.json')
    require(d['owner'] == 'bplus ARM-LOOKUP-CONT-001' and
            d['state'] == 'RESERVED' and time.time() < d['deadline'] - 300,
            'Missing live owned lease or cleanup margin')
    require(subprocess.run(['systemctl', 'is-active', '--quiet',
                            root.name + '-release.timer']).returncode == 0,
            'Release timer inactive')
    stat = (pathlib.Path('/proc') / str(d['coordinator_pid']) / 'stat').read_text()
    fields = stat.split(') ')[1].split()
    require(fields[0] == 'T' and fields[19] == d['coordinator_ticks'],
            'Saved coordinator identity/state mismatch')
    require(os.sched_getaffinity(0) == {0}, 'Controller must be pinned to CPU0')
    require(not subprocess.check_output(['docker', 'ps', '-q'], text=True).strip(),
            'Concurrent Docker work')
    if 'sibling50_online' in d:
        require(pathlib.Path('/sys/devices/system/cpu/cpu50/online').read_text().strip()
                == '0', 'Intel SMT sibling is online')
        require(subprocess.run(['systemctl', 'is-active', '--quiet',
                                'snap.parca-agent.parca-agent-svc.service']).returncode
                != 0, 'Intel Parca service is active')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', required=True)
    p.add_argument('--origin-phase', required=True)
    p.add_argument('--cohort', choices=['native', 'gcc15-lto'], required=True)
    p.add_argument('--seed', type=int, choices=[29, 43], required=True)
    p.add_argument('--collector-sha256', required=True)
    a = p.parse_args()
    # One deterministic phase per original cohort/seed; failed phases cannot restart.
    require(pathlib.Path(a.origin_phase).name == a.origin_phase and
            a.origin_phase not in {'', '.', '..'}, 'Origin must be a phase basename')
    root = pathlib.Path(a.root).resolve()
    os.chdir(root)
    origin = root / a.origin_phase
    phase = a.origin_phase + '-confirmation-' + str(a.seed)
    out = root / phase
    require(not out.exists(), 'Confirmation phase already exists; no restart permitted')
    meta = read(origin / 'metadata.json')
    require(meta['cohort'] == a.cohort and meta['seed'] == 17 and
            meta['cases'] == CASES and not meta.get('confirmation'),
            'Origin must be the original seed17 cohort with frozen cases')
    checked_blocks(read(origin / 'qualification.json'), 'base', True)
    # C may have failed: only the complete B grid authorizes B confirmation.
    checked_blocks(read(origin / 'comparison-analysis.json'), 'B')
    freeze = read(root / EXP / 'guards/FREEZE.json')
    binaries = {v: meta['binaries'][v] for v in ['base', 'B']}
    collector = root / EXP / 'fleet_guards.py'

    def identities():
        require(sha(collector) == a.collector_sha256, 'Collector differs from reviewed pin')
        for file, key in [('guards/guards.c', 'harness_sha256'),
                          ('guards/build.sh', 'build_script_sha256')]:
            require(sha(root / EXP / file) == meta[key] == freeze['sha256'][file],
                    'Frozen referee identity mismatch: ' + file)
        for variant, binary in binaries.items():
            path = root / binary['path']
            require(path.resolve().is_relative_to(root), 'ELF outside reserved root')
            require(binary['source_sha256'] == freeze['source_hashes'][variant] and
                    sha(path) == binary['binary_sha256'], 'Frozen ELF/source mismatch')

    identities()
    leasecheck(root)
    exclusions = root / 'H2-exclusions.json'
    require(not exclusions.exists() or 'B' not in read(exclusions), 'B is excluded')
    out.mkdir()  # Atomic claim; even a partial/failed phase stays consumed.
    newmeta = {k: meta[k] for k in ['cohort', 'cases', 'harness_sha256',
                                   'build_script_sha256', 'compiler_image']}
    newmeta.update(seed=a.seed, binaries=binaries, started=time.time(), confirmation=True,
                   confirmation_origin=a.origin_phase, requested_variants=['B'],
                   confirmation_collector_sha256=a.collector_sha256,
                   confirmation_driver_sha256=sha(pathlib.Path(__file__).resolve()),
                   origin_sha256={name: sha(origin / name) for name in
                                  ['metadata.json', 'qualification.json',
                                   'comparison-analysis.json']})
    write(out / 'metadata.json', newmeta)

    def run(action):
        identities()
        leasecheck(root)
        cmd = [sys.executable, str(collector), '--root', str(root), '--phase', phase,
               '--cohort', a.cohort, '--seed', str(a.seed), '--variants', 'B',
               '--action', action]
        record = dict(action=action, argv=cmd, started=time.time())
        write(out / ('orchestration-' + action + '.json'), record)
        with (out / ('orchestration-' + action + '.stdout')).open('x') as stdout, \
                (out / ('orchestration-' + action + '.stderr')).open('x') as stderr:
            result = subprocess.run(cmd, stdout=stdout, stderr=stderr)
        record.update(returncode=result.returncode, finished=time.time())
        write(out / ('orchestration-' + action + '.json'), record)
        require(result.returncode == 0, 'Collector failed; retain phase without retry')

    run('qualify')
    qualification = read(out / 'qualification.json')
    if qualification['pass'] is not True:
        write(out / 'confirmation-result.json', dict(status='PARK', stage='qualification',
              comparison_executed=False, seed=a.seed, cohort=a.cohort))
        return
    checked_blocks(qualification, 'base', True)
    run('compare')
    comparison = read(out / 'comparison-analysis.json')
    require(comparison['rows'] == 60 and len(comparison['blocks']) == 15 and
            all(b['variant'] == 'B' for b in comparison['blocks']), 'Unexpected comparison')
    if comparison['pass'] is True:
        checked_blocks(comparison, 'B')
    write(out / 'confirmation-result.json', dict(status='PASS' if comparison['pass'] else
          'FAIL', stage='comparison', comparison_executed=True, seed=a.seed,
          cohort=a.cohort, origin=a.origin_phase, source_adoption=False))


if __name__ == '__main__':
    main()
