#!/usr/bin/env python3
"""Independently reconstruct a corrected-adapter baseline without rewriting evidence."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import re
import statistics
import subprocess

SIZES = [100, 1000, 10000, 100000, 1000000]
CASES = ['insert', 'lookup-hit', 'lookup-miss', 'rank', 'iterate', 'scan', 'update', 'delete']
CORE = ['Makefile', 'bench/microbench.c', 'src/zset_btree.c', 'src/zset_btree.h',
        'compat/standalone.c', 'compat/server.h', 'vendor/redis/siphash.c',
        'vendor/redis/sds.h', 'vendor/redis/testhelp.h']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--host', required=True)
    parser.add_argument('--evidence-revision', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    directory = args.directory
    manifest = json.loads((directory / 'manifest.json').read_text())
    assert manifest['status'] == 'complete' and manifest['sizes'] == SIZES
    assert manifest['arguments']['ops'] == 1000000 and manifest['arguments']['member_bytes'] == 16
    assert manifest['binary_sha256'] == manifest['binary_sha256_after']
    assert len(manifest['validation']) == 7
    build = manifest['arguments']['build']
    common = ['make', '-B', 'CC=clang', 'CPPFLAGS=-Isrc -Icompat -Ivendor/redis', 'LDLIBS=-lm']
    flags = '-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer'
    validation = [
        ('release-build-check', common + [f'BUILD={build}', f'CFLAGS={flags} -O3', 'LDFLAGS=', 'all', 'check']),
        ('sanitize-build-check', common + [f'BUILD={build}/sanitize',
            f'CFLAGS={flags} -O1 -fsanitize=address,undefined -fno-sanitize-recover=all',
            'LDFLAGS=-fsanitize=address,undefined', 'all', 'check']),
    ]
    validation += [(f'sanitize-size-{n}', [build + '/sanitize/btree-bench', '--size', str(n),
                    '--ops', str(2*n+1), '--member-bytes', '16', '--seed', '101']) for n in SIZES]
    for entry, (name, command) in zip(manifest['validation'], validation):
        assert entry['returncode'] == 0 and entry['name'] == name and entry['command'] == command
    for mode in ['release', 'sanitize']:
        output = (directory / (mode + '-build-check.stdout')).read_text()
        clean = re.sub(r'\x1b\[[0-9;]*m', '', output)
        assert '43 passed, 0 failed, 43 total' in clean
    core = {}
    for name in CORE:
        blob = subprocess.check_output(['git', 'show', '13e459ff8:' + name])
        core[name] = hashlib.sha256(blob).hexdigest()
        assert manifest['source_hashes'][name] == core[name], name
    linux = manifest['machine']['os'] == 'Linux'
    if linux:
        assert manifest['commit'] == subprocess.check_output(['git', 'rev-parse', '13e459ff8'], text=True).strip()
        assert manifest['machine']['affinity'] == [2]
    assert set(manifest['source_hashes']) == set(CORE + ['scripts/run-size-matrix.py', 'scripts/analyse-size-matrix.py'])
    for name, digest in manifest['source_hashes'].items():
        blob = subprocess.check_output(['git', 'show', manifest['commit'] + ':' + name])
        assert hashlib.sha256(blob).hexdigest() == digest, name
    expected = []
    for block in range(6):
        for n in SIZES[block % 5:] + SIZES[:block % 5]:
            for step, label in enumerate('ABBA'):
                expected.append((block, 1 + block % 3, n, step, label))
    assert len(manifest['runs']) == len(expected) == 120
    groups = {}
    raw_hashes = {}
    for run, identity in zip(manifest['runs'], expected):
        assert tuple(run[k] for k in ['block', 'seed', 'size', 'step', 'label']) == identity
        block, seed, n, step, label = identity
        assert run['returncode'] == 0
        assert run['command'] == [manifest['arguments']['build'] + '/btree-bench', '--size', str(n),
                                  '--ops', '1000000', '--member-bytes', '16', '--seed', str(seed)]
        for field in ['csv', 'stderr']:
            data = (directory / run[field]).read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            assert digest == run[field + '_sha256']
            raw_hashes[run[field]] = digest
            if field == 'stderr':
                assert not data
        rows = list(csv.DictReader(io.StringIO((directory / run['csv']).read_text())))
        assert [r['case'] for r in rows] == CASES
        for row in rows:
            assert (int(row['size']), int(row['seed']), int(row['member_bytes']), int(row['requested_ops'])) == (n, seed, 16, 1000000)
            count = int(row['operations'])
            if row['case'] in ['insert', 'delete']:
                assert count == n
            elif row['case'] == 'scan':
                assert count >= 1000000
            else:
                assert count == 1000000
            assert int(row['elapsed_ns']) > 0
            if linux:
                assert row['cpu_start'] == row['cpu_end'] == '2'
            groups.setdefault((n, row['case']), []).append((block, step, row))
    assert len(groups) == 40
    summary_rows = json.loads((directory / 'summary.json').read_text())
    summaries = {(r['size'], r['case']): r for r in summary_rows}
    assert len(summary_rows) == len(summaries) == 40
    assert set(summaries) == set(groups)
    reconstructed = []
    for (n, case), rows in groups.items():
        assert len(rows) == 24
        values = [int(r['elapsed_ns']) / int(r['operations']) for _, _, r in rows]
        effects = []
        for block in range(6):
            selected = [r for b, _, r in rows if b == block]
            assert len(selected) == 4
            for field in ['operations', 'checksum', 'tree_bytes', 'traversals', 'warmup_passes']:
                assert len({r[field] for r in selected}) == 1
            v = [int(r['elapsed_ns']) / int(r['operations']) for r in selected]
            effects.append(100 * ((v[1] + v[2]) / (v[0] + v[3]) - 1))
        shortest = min(int(r['elapsed_ns']) for _, _, r in rows) / 1e6
        result = dict(size=n, case=case, observations=24, median_ns_op=statistics.median(values),
                      min_ns_op=min(values), max_ns_op=max(values), aa_block_effects_pct=effects,
                      aa_max_abs_pct=max(map(abs, effects)), shortest_timed_ms=shortest,
                      tree_bytes_median=statistics.median(int(r['tree_bytes']) for _, _, r in rows))
        supplied = summaries[n, case]
        for key, value in result.items():
            if isinstance(value, list):
                assert all(math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-10) for a, b in zip(value, supplied[key])) and len(value) == len(supplied[key])
            elif isinstance(value, (int, float)):
                assert math.isclose(value, supplied[key], rel_tol=1e-12, abs_tol=1e-10)
            else:
                assert value == supplied[key]
        result['qualified'] = shortest >= 10 and result['aa_max_abs_pct'] <= 1
        reconstructed.append(result)
    report = dict(checked_utc=datetime.now(timezone.utc).isoformat(), host=args.host,
                  evidence_revision=args.evidence_revision, source_commit=manifest['commit'],
                  manifest_sha256=hashlib.sha256((directory / 'manifest.json').read_bytes()).hexdigest(),
                  binary_sha256=manifest['binary_sha256'], corrected_adapter_core_hashes=core,
                  binary_before_after_verification='Manifest hash equality; this audit does not read a live runner binary.',
                  source_verification='Manifest hashes match recorded Git source; post-run source immutability is asserted by the runner.',
                  processes=120, rows=960, cells=40, paired_blocks=240, validation_stages=7,
                  qualified_cells=sum(r['qualified'] for r in reconstructed),
                  short_cells=sum(r['shortest_timed_ms'] < 10 for r in reconstructed),
                  precision_failure_cells=sum(r['aa_max_abs_pct'] > 1 for r in reconstructed),
                  exact_schedule_and_raw_hashes_verified=True, raw_hashes=raw_hashes,
                  timing_seconds=manifest['timing_seconds'], results=reconstructed,
                  limitations=['Coverage baseline, not a candidate or old/new adapter speed comparison.',
                               'Ordered serial runner schedule verified; runner does not record per-child UTC intervals.',
                               'Machine/compiler/OS differences are not candidate gains.'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['host', 'processes', 'rows', 'cells', 'qualified_cells', 'short_cells', 'precision_failure_cells']}))


if __name__ == '__main__':
    main()
