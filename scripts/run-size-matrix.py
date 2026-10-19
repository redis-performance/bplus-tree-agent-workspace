#!/usr/bin/env python3
"""Build, validate and measure all eight tree operations at four fixed sizes."""
import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import subprocess
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SIZES = (100, 1000, 10000, 100000)
CASES = ('insert', 'lookup-hit', 'lookup-miss', 'rank', 'iterate', 'scan', 'update', 'delete')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', required=True, help='New directory; never overwritten')
    p.add_argument('--ops', type=int, default=1000000)
    p.add_argument('--member-bytes', type=int, default=16)
    p.add_argument('--budget-seconds', type=int, default=300)
    a = p.parse_args()
    if not 1 <= a.ops <= 100000000 or not 8 <= a.member_bytes <= 65536 or a.budget_seconds < 1:
        p.error('Invalid operation count, member length or budget')
    os.chdir(ROOT)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=False)
    (out/'raw').mkdir()
    build = Path('build/size-matrix')
    files = ['Makefile', 'bench/microbench.c', 'src/zset_btree.c', 'src/zset_btree.h',
             'compat/standalone.c', 'compat/server.h', 'vendor/redis/siphash.c',
             'vendor/redis/sds.h', 'vendor/redis/testhelp.h', 'scripts/run-size-matrix.py',
             'scripts/analyse-size-matrix.py']
    manifest = dict(status='preparing', started_utc=datetime.now(timezone.utc).isoformat(),
        commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        arguments=vars(a), source_hashes={f: sha(f) for f in files},
        machine=dict(os=platform.system(), release=platform.release(), arch=platform.machine(),
                     threads=1, affinity='unpinned', frequency='unknown', core_residency='unknown'),
        compiler=subprocess.check_output(['clang', '--version'], text=True),
        validation=[], runs=[])
    if platform.system() == 'Darwin':
        for key in ('machdep.cpu.brand_string', 'hw.physicalcpu', 'hw.logicalcpu'):
            manifest['machine'][key] = subprocess.check_output(['sysctl', '-n', key], text=True).strip()
        manifest['machine']['macos'] = subprocess.check_output(['sw_vers', '-productVersion'], text=True).strip()
    else:
        manifest['machine']['cpu_info'] = Path('/proc/cpuinfo').read_text().split('\n\n')[0]
    def save():
        (out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    def validate(name, command):
        r = subprocess.run(command, capture_output=True, text=True, timeout=180)
        (out/(name+'.stdout')).write_text(r.stdout.replace(str(ROOT), '<workspace>'))
        (out/(name+'.stderr')).write_text(r.stderr.replace(str(ROOT), '<workspace>'))
        manifest['validation'].append(dict(name=name, command=command, returncode=r.returncode))
        save()
        if r.returncode:
            raise RuntimeError(f'{name} failed; see retained output')
    save()
    try:
        common = ['make', '-B', 'CC=clang', 'CPPFLAGS=-Isrc -Icompat -Ivendor/redis', 'LDLIBS=-lm']
        flags = '-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer'
        validate('release-build-check', common + [f'BUILD={build}', f'CFLAGS={flags} -O3', 'LDFLAGS=', 'all', 'check'])
        validate('sanitize-build-check', common + [f'BUILD={build}/sanitize',
            f'CFLAGS={flags} -O1 -fsanitize=address,undefined -fno-sanitize-recover=all',
            'LDFLAGS=-fsanitize=address,undefined', 'all', 'check'])
        for size in SIZES:
            validate(f'sanitize-size-{size}', [str(build/'sanitize/btree-bench'), '--size', str(size),
                '--ops', str(2*size+1), '--member-bytes', str(a.member_bytes), '--seed', '101'])
        binary = str(build/'btree-bench')
        manifest['binary_sha256'] = sha(binary)
        manifest['status'] = 'running'
        save()
        start = time.monotonic()
        # Same binary on both A/B sides; seeds 1,2,3 occur twice each.
        for block in range(6):
            seed = 1 + block % 3
            for size in SIZES[block % 4:] + SIZES[:block % 4]:
                invariants = None
                for step, label in enumerate('ABBA'):
                    remaining = a.budget_seconds - (time.monotonic()-start)
                    if remaining <= 0:
                        raise TimeoutError('Timing budget exceeded')
                    name = f'b{block}-n{size}-s{step}-{label}'
                    cmd = [binary, '--size', str(size), '--ops', str(a.ops),
                           '--member-bytes', str(a.member_bytes), '--seed', str(seed)]
                    r = subprocess.run(cmd, capture_output=True, text=True, timeout=min(30, remaining))
                    (out/'raw'/f'{name}.csv').write_text(r.stdout)
                    (out/'raw'/f'{name}.stderr').write_text(r.stderr)
                    record = dict(block=block, seed=seed, size=size, step=step, label=label,
                        command=cmd, returncode=r.returncode, csv=f'raw/{name}.csv',
                        stderr=f'raw/{name}.stderr', csv_sha256=sha(out/'raw'/f'{name}.csv'),
                        stderr_sha256=sha(out/'raw'/f'{name}.stderr'))
                    manifest['runs'].append(record)
                    save()
                    if r.returncode:
                        raise RuntimeError(f'{name} failed')
                    rows = list(csv.DictReader(io.StringIO(r.stdout)))
                    assert tuple(row['case'] for row in rows) == CASES
                    current = [tuple(row[k] for k in ('case', 'size', 'seed', 'member_bytes', 'operations', 'checksum')) for row in rows]
                    if invariants is None:
                        invariants = current
                    assert invariants == current
                    assert all(int(row['elapsed_ns']) > 0 for row in rows)
                print(f'Completed block {block+1}/6, size {size}', flush=True)
        manifest['timing_seconds'] = time.monotonic()-start
        manifest['binary_sha256_after'] = sha(binary)
        assert manifest['binary_sha256_after'] == manifest['binary_sha256']
        assert all(sha(f) == h for f, h in manifest['source_hashes'].items())
        manifest['status'] = 'complete'
    except BaseException as error:
        manifest['status'] = 'failed'
        manifest['error'] = str(error)
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        save()
    print(f'Completed {len(manifest["runs"])} processes in {manifest["timing_seconds"]:.1f}s')


if __name__ == '__main__':
    main()
