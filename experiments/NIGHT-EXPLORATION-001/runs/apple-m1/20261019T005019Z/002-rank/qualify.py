#!/usr/bin/env python3
"""Frozen rank A/A: three baseline calibrations, then six serial ABBA blocks."""
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import statistics
import subprocess
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
BIN = ROOT / 'build/size-matrix/btree-bench'
SIZES = (10000, 100000, 1000000)
SEEDS = (1, 2, 3, 1, 2, 3)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(size, ops, seed, name):
    cmd = [str(BIN), '--size', str(size), '--ops', str(ops),
           '--member-bytes', '16', '--seed', str(seed), '--case', 'rank']
    result = subprocess.run(cmd, text=True, capture_output=True, timeout=120)
    path = OUT / 'raw' / (name + '.csv')
    path.write_text(result.stdout)
    (OUT / 'raw' / (name + '.stderr')).write_text(result.stderr)
    if result.returncode:
        raise RuntimeError(f'{name} failed with {result.returncode}')
    rows = list(csv.DictReader(io.StringIO(result.stdout)))
    assert len(rows) == 1 and rows[0]['case'] == 'rank'
    row = rows[0]
    assert int(row['size']) == size and int(row['operations']) == ops
    assert int(row['seed']) == seed and int(row['member_bytes']) == 16
    assert int(row['elapsed_ns']) > 0
    return {'name': name, 'size': size, 'ops': ops, 'seed': seed,
            'elapsed_ns': int(row['elapsed_ns']), 'checksum': row['checksum'],
            'tree_bytes': int(row['tree_bytes']), 'csv': str(path.relative_to(OUT)),
            'sha256': sha(path)}


def save(m):
    (OUT / 'qualification.json').write_text(json.dumps(m, indent=2) + '\n')


def main():
    (OUT / 'raw').mkdir(exist_ok=False)
    m = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
         'binary_sha256': sha(BIN), 'source_sha256': sha(ROOT/'src/zset_btree.c'),
         'referee_sha256': sha(ROOT/'bench/microbench.c'),
         'method': 'rank only; baseline calibration 3 per size at 1M ops; fixed >=50ms target; six serial ABBA blocks; no candidate',
         'calibration': [], 'fixed_ops': {}, 'runs': [], 'results': []}
    save(m)
    try:
        for size in SIZES:
            for i in range(3):
                m['calibration'].append(run(size, 1000000, 1, f'cal-n{size}-{i}'))
                save(m)
            fastest = min(r['elapsed_ns']/r['ops'] for r in m['calibration'] if r['size'] == size)
            m['fixed_ops'][size] = min(100000000, math.ceil(50000000/fastest))
            save(m)
        for block, seed in enumerate(SEEDS):
            ordered = SIZES[block % len(SIZES):] + SIZES[:block % len(SIZES)]
            for size in ordered:
                for step, label in enumerate('ABBA'):
                    row = run(size, m['fixed_ops'][size], seed, f'b{block}-n{size}-s{step}-{label}')
                    row.update(block=block, step=step, label=label)
                    m['runs'].append(row)
                    save(m)
                print(f'block {block+1}/6 size {size}', flush=True)
        assert len(m['runs']) == 72
        for size in SIZES:
            effects = []
            windows = []
            for block in range(6):
                rows = [r for r in m['runs'] if r['size'] == size and r['block'] == block]
                assert len(rows) == 4 and len({r['checksum'] for r in rows}) == 1
                assert len({r['tree_bytes'] for r in rows}) == 1
                a = statistics.mean(r['elapsed_ns']/r['ops'] for r in rows if r['label'] == 'A')
                b = statistics.mean(r['elapsed_ns']/r['ops'] for r in rows if r['label'] == 'B')
                effects.append(100*(b/a-1))
                windows.extend(r['elapsed_ns']/1e6 for r in rows)
            m['results'].append({'size': size, 'effects_pct': effects,
                'shortest_window_ms': min(windows),
                'qualified': all(abs(e) <= 1 for e in effects) and min(windows) >= 10})
        assert sha(BIN) == m['binary_sha256']
        assert sha(ROOT/'src/zset_btree.c') == m['source_sha256']
        assert sha(ROOT/'bench/microbench.c') == m['referee_sha256']
        m['status'] = 'complete'
    except BaseException as e:
        m['status'] = 'failed'
        m['error'] = repr(e)
        raise
    finally:
        m['finished_utc'] = datetime.now(timezone.utc).isoformat()
        save(m)
    print(json.dumps(m['results'], indent=2))


if __name__ == '__main__':
    main()
