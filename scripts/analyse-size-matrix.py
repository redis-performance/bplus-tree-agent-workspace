#!/usr/bin/env python3
"""Reconstruct all size-matrix summaries from hashed raw rows; optionally plot."""
import argparse
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path
import statistics as stats

CASES = ('insert', 'lookup-hit', 'lookup-miss', 'rank', 'iterate', 'scan', 'update', 'delete')
SIZES = (100, 1000, 10000, 100000)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory', type=Path)
    p.add_argument('--plot', action='store_true', help='Requires matplotlib')
    a = p.parse_args()
    m = json.loads((a.directory/'manifest.json').read_text())
    assert m['status'] == 'complete' and len(m['runs']) == 96
    groups = defaultdict(list)
    for run in m['runs']:
        assert run['returncode'] == 0
        for field in ('csv', 'stderr'):
            assert hashlib.sha256((a.directory/run[field]).read_bytes()).hexdigest() == run[field+'_sha256']
        with (a.directory/run['csv']).open() as f:
            rows = list(csv.DictReader(f))
        assert tuple(r['case'] for r in rows) == CASES
        for r in rows:
            assert int(r['size']) == run['size'] and int(r['seed']) == run['seed']
            assert int(r['member_bytes']) == m['arguments']['member_bytes']
            ops = int(r['operations'])
            n, requested = int(r['size']), m['arguments']['ops']
            if r['case'] in ('insert', 'delete'):
                assert ops == n
            elif r['case'] == 'iterate':
                assert ops == ((requested+n-1)//n)*n
            elif r['case'] == 'scan':
                assert ops >= ((requested+n-1)//n)*n
            else:
                assert ops == requested
            assert int(r['elapsed_ns']) > 0 and ops > 0
            groups[(run['size'], r['case'])].append(dict(r, block=run['block'], label=run['label']))
    assert len(groups) == 32
    results = []
    for size in SIZES:
        for case in CASES:
            rows = groups[(size, case)]
            assert len(rows) == 24
            value = lambda r: int(r['elapsed_ns'])/int(r['operations'])
            values = [value(r) for r in rows]
            effects = []
            for block in range(6):
                sides = {label: [r for r in rows if r['block'] == block and r['label'] == label] for label in 'AB'}
                assert all(len(v) == 2 for v in sides.values())
                assert len({(r['checksum'], r['operations']) for v in sides.values() for r in v}) == 1
                effects.append(100*(stats.mean(map(value, sides['B']))/stats.mean(map(value, sides['A']))-1))
            results.append(dict(size=size, case=case, observations=len(rows), median_ns_op=stats.median(values),
                min_ns_op=min(values), max_ns_op=max(values), aa_block_effects_pct=effects,
                aa_max_abs_pct=max(map(abs, effects)), shortest_timed_ms=min(int(r['elapsed_ns']) for r in rows)/1e6,
                tree_bytes_median=stats.median(int(r['tree_bytes']) for r in rows)))
    (a.directory/'summary.json').write_text(json.dumps(results, indent=2)+'\n')
    with (a.directory/'summary.csv').open('w') as f:
        w = csv.DictWriter(f, [k for k in results[0] if k != 'aa_block_effects_pct'], extrasaction='ignore')
        w.writeheader(); w.writerows(results)
    host = m['machine'].get('machdep.cpu.brand_string', m['machine']['arch'])
    lines = [f'# Size matrix — {host}', '',
        'Median batch-average ns/op over 24 observations per cell; lower is better.',
        'Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.', '',
        '| Operation | 100 | 1K | 10K | 100K |', '|---|---:|---:|---:|---:|']
    for case in CASES:
        lines.append('| '+case+' | '+' | '.join(f'{next(r for r in results if r["size"] == n and r["case"] == case)["median_ns_op"]:.2f}' for n in SIZES)+' |')
    lines += ['', '## Variation and timing duration', '',
        'Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.',
        'A/A is the difference between identical-binary sides. Large values show noise, not a code change.',
        'Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.', '',
        '| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |',
        '|---:|---|---:|---:|---:|---|']
    for r in results:
        lines.append(f'| {r["size"]} | {r["case"]} | {r["min_ns_op"]:.2f}–{r["max_ns_op"]:.2f} | {r["aa_max_abs_pct"]:.2f}% | {r["shortest_timed_ms"]:.4f} | {"yes" if r["shortest_timed_ms"] < 10 else "no"} |')
    (a.directory/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
    if a.plot:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 4, figsize=(13, 6.5), layout='constrained')
        for ax, case in zip(axes.flat, CASES):
            rr = [r for r in results if r['case'] == case]
            med = [r['median_ns_op'] for r in rr]
            ax.errorbar(range(4), med, yerr=[[r['median_ns_op']-r['min_ns_op'] for r in rr],
                        [r['max_ns_op']-r['median_ns_op'] for r in rr]], marker='o', capsize=3, color='#2563eb')
            ax.set_xticks(range(4), ['100', '1K', '10K', '100K'])
            ax.set_ylim(bottom=0); ax.set_title(case); ax.set_ylabel('ns/op'); ax.set_xlabel('Members')
            ax.grid(axis='y', alpha=.2)
        fig.suptitle(f'{host} · sorted-set baseline · {m["arguments"]["member_bytes"]}-byte members\nMedian and observed min–max; each panel has its own y-axis')
        fig.savefig(a.directory/'size-matrix.svg', metadata={'Date': None})
        plt.close(fig)
    print(f'Validated 96 raw runs / 768 rows / {len(results)} cells; summaries written.')


if __name__ == '__main__':
    main()
