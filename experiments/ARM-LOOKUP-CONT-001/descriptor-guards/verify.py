#!/usr/bin/env python3
"""Build all four sources; execute verify mode only, without clocks or PMU."""
import hashlib
import json
import os
from pathlib import Path
import subprocess

here = Path(__file__).resolve().parent
root = here.parents[2]
exp = root / 'experiments/ARM-LOOKUP-CONT-001'
logs = here / 'correctness'
local = here / 'local'
logs.mkdir(exist_ok=True)
local.mkdir(exist_ok=True)
sources = {'baseline': exp / 'current/src/zset_btree.c'}
for variant in 'ABC':
    sources[variant] = (root / 'build/arm-cont-private/worktrees' / ('H6-' + variant)
                       / 'experiments/ARM-LOOKUP-CONT-001/current/src/zset_btree.c')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = {
    'status': 'in_progress', 'local_measurement_calls': 0, 'fleet_calls': 0,
    'compiler': subprocess.check_output([os.environ.get('TASK_CC', 'cc'), '--version'],
                                       text=True).splitlines()[0],
    'source_sha256': {label: sha(p) for label, p in sources.items()},
    'referee_sha256': {}, 'builds': {},
}
for p in [here / 'guards.c', here / 'build.sh', here / 'verify.py',
          exp / 'current/src/zset_btree.h', exp / 'current/compat/server.h',
          exp / 'current/compat/standalone.c', exp / 'current/vendor/sds.h',
          exp / 'current/vendor/siphash.c']:
    manifest['referee_sha256'][str(p.relative_to(root))] = sha(p)

def save_manifest():
    (here / 'correctness-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

save_manifest()
cases = ['member-forward', 'member-reverse', 'lookup-inline', 'lookup-external']
for label, source in sources.items():
    for mode in ['native', 'sanitizer']:
        name = label + '-' + mode
        binary = local / name
        command = ['sh', str((here / 'build.sh').relative_to(root)),
                   str(source.relative_to(root)), str(binary.relative_to(root)), mode]
        process = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=120)
        (logs / (name + '-build.stdout')).write_text(process.stdout)
        (logs / (name + '-build.stderr')).write_text(process.stderr)
        entry = {'build_argv': command, 'build_returncode': process.returncode,
                 'cells': 0, 'all_verify_passed': False}
        manifest['builds'][name] = entry
        save_manifest()
        assert process.returncode == 0, (name, process.stderr)
        entry['binary_sha256'] = sha(binary)
        rows, calls = [], []
        for seed in [17, 29, 43]:
            for case in cases:
                for sweeps in [1, 2, 5, 8]:
                    args = ['verify', case, str(seed), str(sweeps)]
                    process = subprocess.run([str(binary), *args], capture_output=True,
                                             text=True, timeout=60)
                    calls.append({'argv': ['<BINARY>', *args],
                                  'returncode': process.returncode,
                                  'stdout': process.stdout, 'stderr': process.stderr})
                    (logs / (name + '-calls.json')).write_text(json.dumps(calls, indent=2) + '\n')
                    assert process.returncode == 0 and not process.stderr, (name, calls[-1])
                    row = json.loads(process.stdout)
                    assert row['verified'] and row['mode'] == 'verify'
                    assert 'elapsed_ns' not in row and row['members'] == 529
                    expected_ops = 529 if case.startswith('member-') else (
                        930 if case == 'lookup-inline' else 128)
                    assert row['ops'] == sweeps * expected_ops
                    rows.append(row)
        (logs / (name + '.jsonl')).write_text(''.join(json.dumps(r) + '\n' for r in rows))
        entry.update(cells=len(rows), all_verify_passed=True)
        save_manifest()
        print(name, len(rows), 'verify cells passed', flush=True)

# Logical outcomes must match exactly. Memory is reported separately so a
# layout difference cannot be confused with an oracle failure or hidden.
memory = {}
for mode in ['native', 'sanitizer']:
    reference = [json.loads(s) for s in (logs / ('baseline-' + mode + '.jsonl')).read_text().splitlines()]
    for label in sources:
        rows = [json.loads(s) for s in (logs / (label + '-' + mode + '.jsonl')).read_text().splitlines()]
        for a, b in zip(reference, rows):
            assert {k: v for k, v in a.items() if not k.startswith('owned_bytes_')} == {
                k: v for k, v in b.items() if not k.startswith('owned_bytes_')}
        memory[label + '-' + mode] = {
            field: sorted(set(row[field] for row in rows))
            for field in ['owned_bytes_before', 'owned_bytes_after', 'owned_bytes_after_validation']}
manifest.update(status='passed', total_verify_cells=sum(x['cells'] for x in manifest['builds'].values()),
                identical_logical_outputs=True, memory_endpoints=memory)
save_manifest()
print('All 384 correctness cells passed; no measurement mode executed.', flush=True)
