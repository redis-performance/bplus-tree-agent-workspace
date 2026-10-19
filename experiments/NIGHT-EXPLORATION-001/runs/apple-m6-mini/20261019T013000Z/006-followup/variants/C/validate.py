#!/usr/bin/env python3
"""C-only bounded correctness/codegen validation; never a timing campaign."""
import hashlib
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
WORK = ROOT / 'worktrees/m6-caller-C'
REF = Path('experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup')
LOGS = WORK / 'scratch/caller-C-validation'
LOGS.mkdir(parents=True, exist_ok=True)
(WORK / 'build').mkdir(exist_ok=True)
SUMMARY = dict(participant='/root/followup_proposal_c', backend='GPT-6/Codex family',
               exact_serving_variant=None, token_usage=None, monetary_cost=None,
               scope='correctness and static codegen only; no performance results',
               source_commit='e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf', commands=[], hashes={})

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save():
    (OUT / 'validation.json').write_text(json.dumps(SUMMARY, indent=2) + '\n')

def run(name, command, timeout=120):
    assert not (LOGS / (name + '.stdout')).exists(), name
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(list(map(str, command)), cwd=WORK, capture_output=True,
                            text=True, timeout=timeout)
    logs = {}
    for stream, value in [('stdout', result.stdout), ('stderr', result.stderr)]:
        path = LOGS / (name + '.' + stream)
        path.write_text(value)
        logs[stream] = dict(path=str(path.relative_to(WORK)), sha256=sha(path))
    SUMMARY['commands'].append(dict(name=name, cwd='worktrees/m6-caller-C',
                                   command=list(map(str, command)), started_utc=started,
                                   finished_utc=datetime.now(timezone.utc).isoformat(),
                                   returncode=result.returncode, logs=logs))
    save()
    print(name, result.returncode, flush=True)
    assert result.returncode == 0, (name, result.stderr[-1000:])
    return result.stdout

def build(name, frontend, san=False, upstream=False, included=False):
    flags = ['-std=c11', '-g', '-Wall', '-Wextra', '-fno-omit-frame-pointer',
             '-O1' if san else '-O3']
    if san:
        flags += ['-fsanitize=address,undefined', '-fno-sanitize-recover=all']
    if upstream:
        flags += ['-DREDIS_TEST', '-DREDIS_DEBUG']
    command = ['clang', *flags, '-Isrc', '-Icompat', '-Ivendor/redis', '-I.',
               frontend, *([] if included else ['src/zset_btree.c']),
               'compat/standalone.c', 'vendor/redis/siphash.c', '-lm', '-o', 'build/' + name]
    run('build-' + name, command)

SUMMARY['started_utc'] = datetime.now(timezone.utc).isoformat()
for name in ['src/zset_btree.c', 'src/zset_btree.h', 'tests/upstream.c',
             'compat/standalone.c', 'vendor/redis/siphash.c', str(REF / 'lookup-bench.c'),
             str(REF / 'physical-oracle.c'), 'readonly-oracle.c']:
    SUMMARY['hashes'][name] = sha(WORK / name)
SUMMARY['hashes']['candidate.patch'] = sha(OUT / 'candidate.patch')
save()
for san in (False, True):
    suffix = '-san' if san else ''
    build('upstream' + suffix, 'tests/upstream.c', san, upstream=True)
    output = run('upstream' + suffix, ['build/upstream' + suffix])
    SUMMARY.setdefault('upstream_output', {})[suffix or 'release'] = output
    build('lookup' + suffix, REF / 'lookup-bench.c', san)
    build('physical' + suffix, REF / 'physical-oracle.c', san, included=True)
    SUMMARY.setdefault('physical_output', {})[suffix or 'release'] = run(
        'physical' + suffix, ['build/physical' + suffix])
    build('readonly' + suffix, 'readonly-oracle.c', san, included=True)
    SUMMARY.setdefault('readonly_output', {})[suffix or 'release'] = run(
        'readonly' + suffix, ['build/readonly' + suffix])
    for size in (100, 1000, 10000, 100000, 1000000):
        for case in ('lookup-hit', 'lookup-miss'):
            run(f'lookup{suffix}-n{size}-{case}', ['build/lookup' + suffix,
                '--case', case, '--size', size, '--ops', 2003, '--seed', 1,
                '--member-bytes', 16])
    for member in (8, 319, 320, 321, 1024):
        for case in ('lookup-hit', 'lookup-miss'):
            run(f'lookup{suffix}-m{member}-{case}', ['build/lookup' + suffix,
                '--case', case, '--size', 1000, '--ops', 2003, '--seed', 1,
                '--member-bytes', member])
assembly = run('release-assembly', ['otool', '-tvV', 'build/lookup'])
symbols = {}
for symbol in ('_zbtreeScoreRaw', '_zbtScoreLeafFindMember', '_zbtScoreLeafFindMemberReadOnly'):
    marker = symbol + ':\n'
    if marker not in assembly:
        symbols[symbol] = dict(present=False)
        continue
    body = assembly.split(marker, 1)[1].split('\n_', 1)[0]
    (OUT / (symbol[1:] + '.asm')).write_text(marker + body + '\n')
    symbols[symbol] = dict(present=True, instructions=len(body.splitlines()),
                           frame_instructions=[line for line in body.splitlines()
                                               if '\tsub\tsp, sp,' in line],
                           memchr_calls=body.count('symbol stub for: _memchr'),
                           memcmp_calls=body.count('symbol stub for: _memcmp'),
                           generic_leaf_calls=body.count('bl\t_zbtScoreLeafFindMember'))
SUMMARY['static_codegen'] = symbols
SUMMARY['binary_hashes'] = {path.name: sha(path) for path in (WORK / 'build').iterdir()
                            if path.is_file()}
SUMMARY['status'] = 'PASS'
SUMMARY['finished_utc'] = datetime.now(timezone.utc).isoformat()
save()
print(json.dumps(symbols, indent=2), flush=True)
