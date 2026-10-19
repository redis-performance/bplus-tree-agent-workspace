#!/usr/bin/env python3
"""Plot pinned host baseline summaries with matching axes and observed ranges."""
import argparse
import hashlib
import json
from pathlib import Path

CASES = ('insert', 'lookup-hit', 'lookup-miss', 'rank', 'iterate', 'scan', 'update', 'delete')
TITLES = ('Insert', 'Hit lookup', 'Miss lookup', 'Rank', 'Forward iteration', 'Scan', 'Score update', 'Delete')
SIZES = (100, 1000, 10000, 100000, 1000000)
STYLES = {'apple-m1': ('#1d4ed8', 'o', '-'),
          'apple-m6': ('#b45309', 's', '--'),
          'aws-intel': ('#7c3aed', '^', '-.'),
          'aws-amd': ('#15803d', 'D', ':'),
          'aws-arm': ('#be123c', 'v', '-')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path, help='Contains sources.json and pinned summaries')
    args = parser.parse_args()
    manifest = json.loads((args.directory/'sources.json').read_text())
    sources = manifest['hosts']
    pending = manifest.get('pending_hosts', [])
    assert all(p['status'] == 'NOT RUN' and 'file' not in p for p in pending)
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
    assert len({s['host'] for s, _ in hosts}) == len(hosts)
    assert {s['host'] for s, _ in hosts} <= set(STYLES)

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.ticker import MaxNLocator
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'svg.fonttype': 'none', 'svg.hashsalt': 'bplus-m1-m6-baselines'})
    limits = {case: max(cells[(case, size)]['max_ns_op']
                       for _, cells in hosts for size in SIZES)*1.12 for case in CASES}
    for group in [[host] for host in hosts] + [hosts]:
        combined = len(group) > 1
        fig, axes = plt.subplots(2, 4, figsize=(14, 7.2))
        fig.patch.set_facecolor('white')
        for ax, case, title in zip(axes.flat, CASES, TITLES):
            for source, cells in group:
                color, marker, linestyle = STYLES[source['host']]
                rows = [cells[(case, size)] for size in SIZES]
                med = [r['median_ns_op'] for r in rows]
                ax.errorbar(range(5), med,
                    yerr=[[v-r['min_ns_op'] for v, r in zip(med, rows)],
                          [r['max_ns_op']-v for v, r in zip(med, rows)]],
                    marker=marker, linestyle=linestyle,
                    markersize=4.5, linewidth=2, elinewidth=1.2, capsize=3,
                    color=color, label=source['label'], zorder=3)
            ax.set_xticks(range(5), ['100', '1K', '10K', '100K', '1M'])
            ax.set_ylim(0, limits[case])
            ax.yaxis.set_major_locator(MaxNLocator(5))
            ax.set_title(title, loc='left', fontweight='bold', pad=12)
            ax.set_ylabel('ns/op')
            ax.set_xlabel('Members')
            ax.grid(axis='y', alpha=.2, zorder=0)
            ax.spines[['top', 'right']].set_visible(False)
        label = ('Apple M1 / M6 + AWS Intel / AMD / Graviton' if len(group) == 5 else
                 'Apple M1 + M6') if combined else group[0][0]['label']
        compiler = ('Apple Clang 17 / 21 · AWS Clang 18.1.3' if len(group) == 5 else
                    'M1: Apple Clang 17 · M6: Apple Clang 21') if combined else group[0][0]['compiler']
        fig.suptitle(f'{label} · whole-tree baseline',
                     fontsize=20, fontweight='bold', x=.07, ha='left', y=.98)
        fig.text(.07, .925, f'{compiler} · -O3 · 16-byte members · 24 observations per cell',
                 fontsize=11, color='#475569')
        if combined:
            handles, labels = axes.flat[0].get_legend_handles_labels()
            for platform in pending:
                handles.append(Line2D([], [], marker='s', markerfacecolor='none',
                                      linestyle='none', color='#64748b'))
                labels.append(platform['label']+' · NOT RUN')
            fig.legend(handles, labels, loc='lower left', bbox_to_anchor=(.065, .855),
                       ncol=len(labels), frameon=False, fontsize=10)
        fig.subplots_adjust(left=.07, right=.98, bottom=.19, top=.79, wspace=.42, hspace=.65)
        note = ('Intel, AMD and Graviton: placeholders only; no measurements plotted.'
                if combined and pending else
                'Host series remain separate. Each panel has its own y-axis. Host/compiler differences are not candidate gains.')
        fig.text(.07, .035,
                 'Dots: median batch-average ns/op. Whiskers: observed min–max. Lower is less time.\n'+note,
                 fontsize=10, color='#475569', linespacing=1.5)
        stem = args.directory/('m1-m6-baseline' if combined else group[0][0]['host']+'-baseline')
        fig.savefig(stem.with_suffix('.png'), dpi=150, facecolor='white', metadata={'Software': 'Matplotlib'})
        fig.savefig(stem.with_suffix('.svg'), facecolor='white', metadata={'Date': None})
        plt.close(fig)
        svg = stem.with_suffix('.svg')
        svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    print(f'Validated {len(hosts)*40} host cells; wrote combined and individual PNG/SVG charts.')


if __name__ == '__main__':
    main()
