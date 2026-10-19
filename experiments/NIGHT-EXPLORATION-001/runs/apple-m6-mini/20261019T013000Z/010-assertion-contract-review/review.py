#!/usr/bin/env python3
"""Private standalone-adapter compiler-contract review; no timed runs."""
from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path
import re
import resource
import shutil
import signal
import subprocess

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
SCR = ROOT / 'scratch/m6-assertion-contract'
assert not SCR.exists(), 'preserve prior attempts; do not overwrite'
SCR.mkdir(parents=True)
LOG = SCR / 'logs'
LOG.mkdir()
TRACK = ['src/zset_btree.c', 'src/zset_btree.h', 'compat/server.h',
         'compat/standalone.c', 'tests/upstream.c', 'vendor/redis/siphash.c']

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

STATE = dict(participant='/root/followup_proposal_c', backend='GPT-6/Codex family',
             exact_serving_model=None, token_usage=None, monetary_cost=None,
             started_utc=datetime.now(timezone.utc).isoformat(),
             root_before={name: sha(ROOT / name) for name in TRACK}, commands=[])
assert STATE['root_before']['src/zset_btree.c'] == 'd9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2'

def save():
    (OUT / 'review.json').write_text(json.dumps(STATE, indent=2) + '\n')

def no_core():
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))

def run(name, cmd, cwd=ROOT, abort=False):
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(list(map(str, cmd)), cwd=cwd, capture_output=True,
                            text=True, timeout=120, preexec_fn=no_core if abort else None)
    logs = {}
    for channel, value in [('stdout', result.stdout), ('stderr', result.stderr)]:
        path = LOG / (name + '.' + channel)
        path.write_text(value)
        logs[channel] = dict(path=str(path.relative_to(ROOT)), sha256=sha(path))
    record = dict(name=name, command=[str(x).replace(str(ROOT), '<workspace>') for x in cmd],
                  cwd=str(cwd.relative_to(ROOT)) if cwd != ROOT else '.',
                  started_utc=started, finished_utc=datetime.now(timezone.utc).isoformat(),
                  returncode=result.returncode, expected='SIGABRT' if abort else 0,
                  child_core_limit_zero=abort, logs=logs)
    STATE['commands'].append(record)
    save()
    print(name, result.returncode, flush=True)
    assert result.returncode == (-signal.SIGABRT if abort else 0), record
    if abort:
        assert 'AFTER_PANIC' not in result.stderr
        assert 'abort-probe.c:' in result.stderr
        assert ('contract probe panic' if cmd[-1] == 'panic' else '0') in result.stderr
    return result.stdout

probe = '''#include "server.h"
#include <string.h>
int main(int argc, char **argv) {
    if (argc != 2) return 2;
    if (!strcmp(argv[1], "assert")) {
        serverAssert(0);
    } else if (!strcmp(argv[1], "panic")) {
        serverPanic("contract probe panic");
    } else return 2;
    fputs("AFTER_PANIC\\n", stderr);
    return 99;
}
'''
(OUT / 'abort-probe.c').write_text(probe)
ref = ROOT / 'experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/009-iterator-profile'
for variant in ('base', 'noreturn'):
    tree = SCR / variant
    tree.mkdir()
    for name in ('src', 'compat', 'vendor', 'tests'):
        shutil.copytree(ROOT / name, tree / name)
    (tree / 'referee').mkdir()
    (tree / 'build').mkdir()
    for name in ('iterator.c', 'microbench.c'):
        shutil.copy2(ref / name, tree / 'referee' / name)
    (tree / 'abort-probe.c').write_text(probe)
    if variant == 'noreturn':
        for name in ('compat/server.h', 'compat/standalone.c'):
            path = tree / name
            old = path.read_text()
            assert old.count('void standalone_panic(') == 1
            new = old.replace('void standalone_panic(', '_Noreturn void standalone_panic(', 1)
            path.write_text(new)
            with (OUT / 'adapter.patch').open('a') as dest:
                dest.write(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                                      fromfile='a/' + name, tofile='b/' + name)))
    assert sha(tree / 'src/zset_btree.c') == STATE['root_before']['src/zset_btree.c']
    flags = ['-std=c11', '-g', '-Wall', '-Wextra', '-fno-omit-frame-pointer', '-O3']
    include = ['-Isrc', '-Icompat', '-Ivendor/redis']
    support = ['compat/standalone.c', 'vendor/redis/siphash.c', '-lm']
    run(variant + '-build-iterator', ['clang', *flags, *include, 'referee/iterator.c',
                                    'src/zset_btree.c', *support, '-o', 'build/iterator'], tree)
    assembly = run(variant + '-otool', ['otool', '-tvV', 'build/iterator'], tree)
    marker = '_zbtreeIteratorNext:\n'
    assert marker in assembly
    body = marker + assembly.split(marker, 1)[1].split('\n_', 1)[0] + '\n'
    (OUT / (variant + '-zbtreeIteratorNext.asm')).write_text(body)
    lines = [line for line in body.splitlines() if re.match(r'^[0-9a-f]+\t', line)]
    STATE.setdefault('iterator_codegen', {})[variant] = dict(
        instructions=len(lines), assembly_sha256=sha(OUT / (variant + '-zbtreeIteratorNext.asm')),
        frames=[line.split('\t', 1)[1] for line in lines if '\tsub\tsp, sp,' in line],
        register_pair_stack_stores=[line.split('\t', 1)[1] for line in lines if '\tstp\t' in line and '[sp' in line],
        calls=[line.split('\t', 1)[1] for line in lines if '\tbl\t' in line],
        unconditional_branches=[line.split('\t', 1)[1] for line in lines if '\tb\t_' in line],
        binary_sha256=sha(tree / 'build/iterator'))
    for san in (False, True):
        suffix = '-san' if san else ''
        build_flags = flags if not san else ['-std=c11', '-g', '-Wall', '-Wextra',
            '-fno-omit-frame-pointer', '-O1', '-fsanitize=address,undefined', '-fno-sanitize-recover=all']
        run(variant + '-build-abort' + suffix, ['clang', *build_flags, *include,
            'abort-probe.c', *support, '-o', 'build/abort' + suffix], tree)
        for fault in ('assert', 'panic'):
            run(variant + '-abort' + suffix + '-' + fault, ['build/abort' + suffix, fault], tree, abort=True)
        if variant == 'noreturn':
            run('noreturn-build-upstream' + suffix, ['clang', *build_flags,
                '-DREDIS_TEST', '-DREDIS_DEBUG', *include, 'tests/upstream.c',
                'src/zset_btree.c', *support, '-o', 'build/upstream' + suffix], tree)
            output = run('noreturn-upstream' + suffix, ['build/upstream' + suffix], tree)
            assert '43 passed' in re.sub(r'\x1b\[[0-9;]*m', '', output)
            (OUT / ('upstream' + suffix + '.stdout')).write_text(output)
    if variant == 'noreturn':
        run('c11-pedantic-declaration', ['clang', '-std=c11', '-pedantic-errors',
            '-Wall', '-Wextra', '-Werror', *include, '-fsyntax-only', 'abort-probe.c'], tree)

for label, cmd in [('clang', ['clang', '--version']), ('gcc-command', ['gcc', '--version'])]:
    version = run(label + '-version', cmd)
    STATE.setdefault('compiler_versions', {})[label] = '\n'.join(
        line for line in version.splitlines() if not line.startswith('InstalledDir:'))
STATE['root_after'] = {name: sha(ROOT / name) for name in TRACK}
assert STATE['root_after'] == STATE['root_before'], 'original files changed'
STATE['private_sources'] = {v: {name: sha(SCR / v / name) for name in TRACK}
                            for v in ('base', 'noreturn')}
STATE['status'] = 'PASS; PRIVATE ADAPTER CONTRACT REVIEW ONLY'
STATE['failed_command_count'] = sum(c['returncode'] != (-signal.SIGABRT if c['expected'] == 'SIGABRT' else 0)
                                    for c in STATE['commands'])
STATE['adapter_patch_sha256'] = sha(OUT / 'adapter.patch')
STATE['review_script_sha256'] = sha(Path(__file__))
STATE['finished_utc'] = datetime.now(timezone.utc).isoformat()
save()
print(json.dumps(STATE['iterator_codegen'], indent=2), flush=True)
