#!/usr/bin/env python3
"""Plot pinned M1/M6 baseline summaries with matching axes and observed ranges."""
import argparse
import hashlib
import json
from pathlib import Path

CASES = ('insert', 'lookup-hit', 'lookup-miss', 'rank', 'iterate', 'scan', 'update', 'delete')
TITLES = ('Insert', 'Hit lookup', 'Miss lookup', 'Rank', 'Forward iteration', 'Scan', 'Score update', 'Delete')
SIZES = (100, 1000, 10000, 100000, 1000000)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path, help='Contains sources.json and pinned summaries')
    args = parser.parse_args()
    sources = json.loads((args.directory/'sources.json').read_text())['hosts']
    hosts = []
    for source in sources:
        payload = (args.directory/source['file']).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == source['sha256']
        rows = json.loads(payload)
        assert len(rows) == len(CASES)*len(SIZES)
        cells = {(r['case'], r['size']): r for r in rows}
        assert set(cells) == {(case, size) for case in CASES for size in SIZES}
        for r in rows:
            assert r['observations'] == 24
            assert 0 < r['min_ns_op'] <= r['median_ns_op'] <= r['max_ns_op']
        hosts.append((source, cells))
    assert {s['host'] for s, _ in hosts} == {'apple-m1', 'apple-m6'}

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'svg.fonttype': 'none', 'svg.hashsalt': 'bplus-m1-m6-baselines'})
    limits = {case: max(cells[(case, size)]['max_ns_op']
                       for _, cells in hosts for size in SIZES)*1.12 for case in CASES}
    for source, cells in hosts:
        color = '#1d4ed8' if source['host'] == 'apple-m1' else '#b45309'
        fig, axes = plt.subplots(2, 4, figsize=(14, 7.2))
        fig.patch.set_facecolor('white')
        for ax, case, title in zip(axes.flat, CASES, TITLES):
            rows = [cells[(case, size)] for size in SIZES]
            med = [r['median_ns_op'] for r in rows]
            ax.errorbar(range(5), med,
                yerr=[[v-r['min_ns_op'] for v, r in zip(med, rows)],
                      [r['max_ns_op']-v for v, r in zip(med, rows)]],
                marker='o', markersize=4.5, linewidth=2, elinewidth=1.2, capsize=3,
                color=color, label='Median; whiskers: observed min–max', zorder=3)
            ax.set_xticks(range(5), ['100', '1K', '10K', '100K', '1M'])
            ax.set_ylim(0, limits[case])
            ax.yaxis.set_major_locator(MaxNLocator(5))
            ax.set_title(title, loc='left', fontweight='bold', pad=12)
            ax.set_ylabel('ns/op')
            ax.set_xlabel('Members')
            ax.grid(axis='y', alpha=.2, zorder=0)
            ax.spines[['top', 'right']].set_visible(False)
        fig.suptitle(f'{source["label"]} · whole-tree baseline',
                     fontsize=22, fontweight='bold', x=.07, ha='left', y=.98)
        fig.text(.07, .91, f'{source["compiler"]} · -O3 · 16-byte members · 24 observations per cell',
                 fontsize=11, color='#475569')
        fig.subplots_adjust(left=.07, right=.98, bottom=.19, top=.82, wspace=.42, hspace=.65)
        fig.text(.07, .035,
                 'Dots: median batch-average ns/op. Whiskers: observed min–max. Lower is less time.\n'
                 'Each operation uses the same y-axis on both host charts. Host/compiler differences are not candidate gains.',
                 fontsize=10, color='#475569', linespacing=1.5)
        stem = args.directory/(source['host']+'-baseline')
        fig.savefig(stem.with_suffix('.png'), dpi=150, facecolor='white', metadata={'Software': 'Matplotlib'})
        fig.savefig(stem.with_suffix('.svg'), facecolor='white', metadata={'Date': None})
        plt.close(fig)
        svg = stem.with_suffix('.svg')
        svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    print('Validated 80 host cells; wrote two PNG charts and two SVG exports.')


if __name__ == '__main__':
    main()
