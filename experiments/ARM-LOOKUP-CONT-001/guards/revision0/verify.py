#!/usr/bin/env python3
"""Local correctness only: compile guards and execute only their verify mode."""
import hashlib
import json
import pathlib
import subprocess

here = pathlib.Path(__file__).resolve().parent
root = here.parents[2]
exp = root / 'experiments/ARM-LOOKUP-CONT-001'
local = here / 'local'
logs = here / 'correctness'
local.mkdir(exist_ok=True)
logs.mkdir(exist_ok=True)
sources = {'baseline': exp / 'current/src/zset_btree.c'}
for variant in ['B', 'C']:
    sources[variant] = (root / 'build/arm-cont-private/worktrees' /
                        ('H2-' + variant) / 'experiments/ARM-LOOKUP-CONT-001' /
                        'current/src/zset_btree.c')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = {
    'scope': 'local correctness only; verify calls only; no timers or PMU',
    'compiler': subprocess.check_output(['cc', '--version'], text=True).splitlines()[0],
    'source_sha256': {label: sha(path) for label, path in sources.items()},
    'referee_sha256': {},
    'builds': {},
}
referees = [here / 'guards.c', exp / 'current/src/zset_btree.h',
            exp / 'current/compat/server.h', exp / 'current/compat/standalone.c',
            exp / 'current/vendor/siphash.c', exp / 'current/vendor/sds.h']
manifest['referee_sha256'] = {str(p.relative_to(root)): sha(p) for p in referees}
for label, source in sources.items():
    for mode in ['native', 'sanitizer']:
        name = label + '-' + mode
        binary = local / name
        flags = ['-O3'] if mode == 'native' else [
            '-O1', '-fsanitize=address,undefined', '-fno-sanitize-recover=all']
        command = ['cc', '-std=c11', '-g', '-Wall', '-Wextra', '-Werror',
                   '-fno-omit-frame-pointer', *flags,
                   '-I' + str(exp / 'current/src'),
                   '-I' + str(exp / 'current/compat'),
                   '-I' + str(exp / 'current/vendor'),
                   str(here / 'guards.c'), str(source),
                   str(exp / 'current/compat/standalone.c'),
                   str(exp / 'current/vendor/siphash.c'), '-lm', '-o', str(binary)]
        built = subprocess.run(command, capture_output=True, text=True, timeout=120)
        (logs / (name + '-build.stdout')).write_text(built.stdout)
        (logs / (name + '-build.stderr')).write_text(built.stderr)
        assert built.returncode == 0, (name, built.stderr)
        rows, calls = [], []
        # Odd and even sweep endpoints, each direction, all confirmation seeds.
        for seed in [17, 29, 43]:
            for case in ['iterator', 'rank', 'churn']:
                for sweeps in [1, 2, 5, 8]:
                    argv = [str(binary), 'verify', case, str(seed), str(sweeps)]
                    process = subprocess.run(argv, capture_output=True, text=True, timeout=60)
                    calls.append({'argv': ['<BINARY>', *argv[1:]],
                                  'returncode': process.returncode,
                                  'stdout': process.stdout, 'stderr': process.stderr})
                    # Retain a failure instead of silently retrying.
                    (logs / (name + '-calls.json')).write_text(json.dumps(calls, indent=2) + '\n')
                    assert process.returncode == 0 and not process.stderr, (name, calls[-1])
                    row = json.loads(process.stdout)
                    assert row['verified'] and row['mode'] == 'verify' and 'elapsed_ns' not in row
                    assert row['ops'] == sweeps * 500
                    rows.append(row)
        (logs / (name + '.jsonl')).write_text(''.join(json.dumps(r) + '\n' for r in rows))
        manifest['builds'][name] = {'binary_sha256': sha(binary), 'cells': len(rows),
            'compiler_flags': flags + ['-std=c11', '-g', '-Wall', '-Wextra', '-Werror',
                                       '-fno-omit-frame-pointer'],
            'all_verify_passed': True}
        print(name, len(rows), 'verify cells passed', flush=True)
for mode in ['native', 'sanitizer']:
    reference = (logs / ('baseline-' + mode + '.jsonl')).read_bytes()
    for variant in ['B', 'C']:
        assert (logs / (variant + '-' + mode + '.jsonl')).read_bytes() == reference
manifest['same_mode_outputs_and_memory_equal'] = True
(here / 'correctness-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print('All 216 correctness cells passed; no measurement mode executed.', flush=True)
