#!/usr/bin/env python3
"""Local correctness only: never invokes measure or a clock API."""
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
EXP = HERE.parent.relative_to(ROOT)
PRIVATE = Path('build/arm-cont-private/index-guards')
EXPECTED = {
    'base': '16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9',
    'A': '002c3568202dff5cb5f39f28753f4b48d1c9ec1c533775371f2fea41eccb6ce8',
    'B': 'ce8ed5476d5b04953e514a1a798947272a4ab2846034d417fe1e7e0b25e080eb',
    'C': 'fa45c5d7bdd04f37bd448a48b573ef92128b56ed35df9d176659d9ddd00ca5d9',
}
CASES = ['collision-hit', 'collision-miss', 'repair-churn', 'scan-members']
env = dict(os.environ, VERIFY_CLOCK_DENY='1', ASAN_OPTIONS='detect_leaks=1:abort_on_error=1')
os.chdir(ROOT)
(ROOT / PRIVATE).mkdir(parents=True, exist_ok=True)
(HERE / 'correctness').mkdir(exist_ok=True)
manifest = {'measurement_calls': 0, 'source_sha256': EXPECTED, 'binaries': {}}
for variant, expected in EXPECTED.items():
    source = EXP / 'current/src/zset_btree.c'
    if variant != 'base':
        source = Path('build/arm-cont-private/worktrees') / ('H7-' + variant) / source
    assert hashlib.sha256(source.read_bytes()).hexdigest() == expected
    for mode, scope in [('native', 'public'), ('sanitizer', 'public'), ('native', 'diagnostic')]:
        label = f'{variant}-{mode}-{scope}'
        binary = PRIVATE / label
        command = ['sh', str(EXP / 'index-guards/build.sh'), str(source), str(binary), mode, scope]
        with (HERE / 'correctness' / (label + '-build.stdout')).open('w') as out, \
             (HERE / 'correctness' / (label + '-build.stderr')).open('w') as err:
            subprocess.run(command, env=env, stdout=out, stderr=err, check=True)
        symbols = subprocess.check_output(['nm', '-u', str(binary)], text=True)
        assert 'clock_gettime' not in symbols, symbols
        assert '__wrap_clock_gettime' in subprocess.check_output(['nm', str(binary)], text=True)
        manifest['binaries'][label] = {'sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
                                     'clock_symbol_wrapped': True, 'cells': 24}
        rows = HERE / 'correctness' / (label + '.jsonl')
        with rows.open('w') as out, (HERE / 'correctness' / (label + '.stderr')).open('w') as err:
            for seed in (17, 29, 43):
                if variant == 'base' and mode == 'native' and scope == 'public':
                    fixture = subprocess.check_output([str(binary), 'fixture', str(seed)], env=env)
                    (HERE / 'correctness' / f'fixture-{seed}.json').write_bytes(fixture)
                for sweeps in (1, 2):
                    for case in CASES:
                        subprocess.run([str(binary), 'verify', case, str(seed), str(sweeps)],
                                       env=env, stdout=out, stderr=err, check=True)
        print(label, '24 correctness cells pass', flush=True)
(HERE / 'correctness' / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
