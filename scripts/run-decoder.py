#!/usr/bin/env python3
"""Bounded, serial A/A then baseline/A decoder experiment; retain every sample."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import shutil
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
WIDTHS = (0, 8, 31, 57, 59, 60, 61, 62, 63, 64)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, help='New evidence directory')
    parser.add_argument('--build', default='build/decoder')
    parser.add_argument('--blocks', type=int, default=6)
    parser.add_argument('--samples', type=int, default=129)
    parser.add_argument('--rounds', type=int, default=64)
    parser.add_argument('--budget-seconds', type=int, default=300)
    args = parser.parse_args()
    if not 3 <= args.blocks <= 12 or not 1 <= args.samples <= 4096 or not 1 <= args.rounds <= 65536:
        parser.error('blocks=3..12, samples=1..4096, rounds=1..65536')
    if not 10 <= args.budget_seconds <= 1800:
        parser.error('budget-seconds=10..1800')
    os.chdir(ROOT)
    out, build = Path(args.out), Path(args.build)
    if json.loads((build/'build.json').read_text())['sanitizers']:
        parser.error('timing requires a release build')
    out.mkdir(parents=True, exist_ok=False)
    (out/'raw').mkdir()
    shutil.copyfile(build/'build.json', out/'build.json')
    build_manifest = json.loads((build/'build.json').read_text())
    for path, expected in build_manifest['files'].items():
        if sha(path) != expected:
            raise SystemExit(f'Build is stale: {path}; run make decoder')
    binaries = {v: build/v/'decoder-bench' for v in ('base', 'A')}
    for v, path in binaries.items():
        if sha(path) != build_manifest['variants'][v]['binary_sha256']:
            raise SystemExit(f'Binary differs from build manifest: {v}')
    cells = [(w, rev) for w in WIDTHS for rev in (0, 1)]
    schedule = []
    for phase in ('aa', 'compare'):
        for block in range(args.blocks):
            seed = (81031, 81041)[block % 2]
            for width, reverse in cells[block % len(cells):] + cells[:block % len(cells)]:
                for step, label in enumerate('ABBA'):
                    variant = 'base' if phase == 'aa' or label == 'A' else 'A'
                    schedule.append(dict(phase=phase, block=block, step=step, label=label,
                                         variant=variant, width=width, reversed=reverse, seed=seed))
    manifest = dict(status='running', started_utc=now(), code_commit=subprocess.run(
        ['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip(),
        driver_sha256=sha(__file__), arguments=vars(args), schedule=schedule, runs=[],
        machine=dict(os=platform.system(), release=platform.release(), arch=platform.machine(),
                     frequency='unknown; uncontrolled DVFS', affinity='not pinned',
                     core_residency='boundary IDs only; within-window migration unknown'),
        purpose='Decoder throughput diagnostic; does not clear iterator guards or accept EXP-004')
    if platform.system() == 'Darwin':
        for key in ('machdep.cpu.brand_string', 'hw.physicalcpu', 'hw.logicalcpu'):
            result = subprocess.run(['sysctl', '-n', key], capture_output=True, text=True)
            manifest['machine'][key] = result.stdout.strip() if result.returncode == 0 else 'unknown'
    (out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    start = time.monotonic()
    summaries = []
    fixtures = {}
    try:
        for index, item in enumerate(schedule):
            if time.monotonic() - start > args.budget_seconds:
                raise TimeoutError('Campaign budget exhausted; partial evidence retained')
            name = f"{index:04d}-{item['phase']}-b{item['block']}-w{item['width']}-r{item['reversed']}-{item['label']}"
            command = [str(binaries[item['variant']]), '--width', str(item['width']),
                       '--reversed', str(item['reversed']), '--seed', str(item['seed']),
                       '--count', '96', '--leaves', '8', '--score-shift', '0',
                       '--rounds', str(args.rounds), '--samples', str(args.samples), '--warmup', '16']
            before = now()
            p = subprocess.run(command, capture_output=True, text=True, timeout=30)
            (out/'raw'/f'{name}.csv').write_text(p.stdout)
            (out/'raw'/f'{name}.stderr').write_text(p.stderr)
            record = dict(item, command=command, started_utc=before, ended_utc=now(), returncode=p.returncode,
                          csv=f'raw/{name}.csv', stderr=f'raw/{name}.stderr',
                          csv_sha256=sha(out/'raw'/f'{name}.csv'), stderr_sha256=sha(out/'raw'/f'{name}.stderr'))
            manifest['runs'].append(record)
            if p.returncode:
                raise RuntimeError(f'Child {name} failed: {p.stderr}')
            rows = list(csv.DictReader(io.StringIO(p.stdout)))
            assert len(rows) == args.samples and all(r['kind'] == 'time' and None not in r for r in rows)
            reference = rows[0]
            key = (item['width'], item['reversed'], item['seed'])
            invariant = tuple(reference[x] for x in ['operations', 'leaf_bytes', 'offset_mask',
                              'crossings_per_round', 'fixture_hash', 'checksum'])
            assert all(tuple(r[x] for x in ['operations', 'leaf_bytes', 'offset_mask',
                       'crossings_per_round', 'fixture_hash', 'checksum']) == invariant for r in rows)
            assert int(reference['operations']) == 96*8*args.rounds
            assert all(int(r['sample']) == i for i, r in enumerate(rows))
            assert fixtures.setdefault(key, invariant) == invariant
            values = [float(r['ns_per_decode']) for r in rows]
            assert min(values) > 0
            ordered = sorted(values)
            summaries.append(dict(item, min_ns=min(values), median_ns=statistics.median(values),
                                  p90_ns=ordered[int(.9*(len(ordered)-1))], max_ns=max(values),
                                  min_batch_ns=min(float(r['elapsed_ns']) for r in rows),
                                  endpoint_migrations=sum(r['cpu_start'] != r['cpu_end'] for r in rows)))
            if (index + 1) % 56 == 0:
                (out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
                print(f'{index+1}/{len(schedule)} processes checked', flush=True)
        manifest['status'] = 'complete'
    except BaseException as error:
        manifest['status'] = 'failed'; manifest['error'] = str(error)
        raise
    finally:
        manifest['finished_utc'] = now()
        manifest['elapsed_seconds'] = time.monotonic() - start
        manifest['binary_hashes_after'] = {v: sha(path) for v, path in binaries.items()}
        (out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
        (out/'process-summary.json').write_text(json.dumps(summaries, indent=2)+'\n')
    assert all(manifest['binary_hashes_after'][v] == build_manifest['variants'][v]['binary_sha256'] for v in binaries)
    print(f'Completed {len(schedule)} processes / {len(schedule)*args.samples} samples in {manifest["elapsed_seconds"]:.1f}s')


if __name__ == '__main__':
    main()
