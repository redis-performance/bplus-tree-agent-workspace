#!/usr/bin/env python3
"""Render immutable, primary-only ARM mask replay evidence. Runs no benchmark."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import statistics
import subprocess
import tarfile

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = 'experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/'

def archive(revision, directory):
    payload = subprocess.check_output(['git', 'archive', revision, directory])
    with tarfile.open(fileobj=io.BytesIO(payload)) as stream:
        return {item.name[len(directory):]: stream.extractfile(item).read()
                for item in stream if item.isfile()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path('experiments/NIGHT-EXPLORATION-001/latest-charts'))
    args = parser.parse_args()
    directory = BASE + '026-exp005A-replication/'
    files = archive('6bcd8e575', directory)
    result = json.loads(files['screen/result.json'])
    groups = {}
    for run in result['runs']:
        row, = csv.DictReader(io.StringIO(files['screen/' + run['name'] + '.csv'].decode()))
        assert row == run['row'] and run['returncode'] == 0
        groups.setdefault((run['size'], run['block']), []).append((run, row))
    effects = []
    for (size, block), entries in sorted(groups.items()):
        assert [run['label'] for run, row in entries] == list('ABBA')
        assert len({row['tree_bytes'] for run, row in entries}) == 1
        elapsed = [int(row['elapsed_ns']) for run, row in entries]
        effects.append(dict(size=size, block=block, effect_pct=100*((elapsed[1]+elapsed[2])/(elapsed[0]+elapsed[3])-1)))
    assert len(effects) == 12
    expected = json.loads(files['screen/audit.json'])['effects']
    assert all(a['effect_pct'] == b['effect_pct'] for a, b in zip(effects, expected))
    aa = json.loads(subprocess.check_output(['git', 'show', '27a4afee1:experiments/NIGHT-EXPLORATION-001/reviews/aws-arm-iterator-baseline-independent-audit.json']))['effects']
    assert len(aa) == 12 and all(row['qualified'] for row in aa)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.hashsalt': 'arm-mask-primary-20261019'})
    fig, axes = plt.subplots(1, 2, figsize=(13, 6), gridspec_kw={'width_ratios': [1, 1.3]})
    colors = {100000: '#2668b5', 1000000: '#c4551c'}
    for axis, data in zip(axes, (aa, effects)):
        for size, offset in ((100000, -.07), (1000000, .07)):
            rows = [row for row in data if row['size'] == size]
            axis.plot([row['block']+1+offset for row in rows], [row['effect_pct'] for row in rows],
                      'o-', color=colors[size], markersize=6, linewidth=1.15,
                      label='100K members' if size == 100000 else '1M members')
        axis.set_xticks(range(1, 7))
        axis.set_xlabel('ABBA block (all six retained)')
        axis.set_ylabel('Elapsed-time change (%)')
        axis.grid(alpha=.2)
        axis.spines[['top', 'right']].set_visible(False)
    axes[0].axhspan(-1, 1, color='#26833c', alpha=.08)
    axes[0].axhline(1, color='#6a6a6a', linestyle='--', linewidth=1)
    axes[0].axhline(-1, color='#6a6a6a', linestyle='--', linewidth=1)
    axes[0].set_ylim(-1.2, 1.2)
    axes[0].set_title('Baseline A/A: 12/12 blocks qualify\nSeeds 701–703 twice · unchanged actual binary', fontsize=11)
    axes[0].legend(loc='lower left', frameon=False)
    axes[1].axhline(-2, color='#555555', linestyle='--', linewidth=1)
    axes[1].text(1.05, -1.7, 'Required primary reduction: at least 2%', fontsize=9, color='#444444')
    axes[1].set_ylim(-9, .1)
    axes[1].set_title('Exact historical A: 12/12 primary blocks pass\nSeeds 401–403 twice · 48 processes · lower is faster', fontsize=11)
    medians = {size: statistics.median(row['effect_pct'] for row in effects if row['size'] == size) for size in colors}
    axes[1].text(1.05, -4.3, f"Primary median: {medians[100000]:.2f}% at 100K\nPrimary median: {medians[1000000]:.2f}% at 1M", fontsize=11)
    fig.suptitle('ARM mask replay — primary screen only · PARK', fontsize=17, fontweight='bold', y=.98)
    fig.text(.5, .09, '50M forward score-only visits · 16-byte members · Clang 18.1.3 · corrected adapter · exact EXP-005 A', ha='center', fontsize=10)
    fig.text(.5, .045, 'Missing: qualified performance guards, fresh confirmation and matched candidate profile. No source adoption.', ha='center', fontsize=10, color='#8a3b19')
    fig.text(.5, .012, 'Dots are paired ABBA effects, not confidence intervals. Static instruction reduction does not establish causal savings.', ha='center', fontsize=9, color='#555555')
    fig.subplots_adjust(top=.80, bottom=.22, left=.07, right=.98, wspace=.30)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.output_dir/'aws-arm-mask-primary'
    fig.savefig(stem.with_suffix('.png'), dpi=170)
    fig.savefig(stem.with_suffix('.svg'), metadata={'Date': None})
    svg_path = stem.with_suffix('.svg')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines()) + '\n')
    plt.close(fig)
    metadata = {'screen_revision': '6bcd8e575', 'baseline_revision': '73c9e313f',
                'baseline_root_audit_revision': '27a4afee1', 'decision': 'PARK',
                'renderer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'source_adoption': 'NONE', 'new_population': False, 'effects': effects,
                'baseline_aa_effects': aa, 'median_effect_pct': medians,
                'artifacts': {suffix: hashlib.sha256(stem.with_suffix(suffix).read_bytes()).hexdigest() for suffix in ('.png', '.svg')}}
    stem.with_suffix('.json').write_text(json.dumps(metadata, indent=2)+'\n')
    print(json.dumps({'decision': 'PARK', 'median_effect_pct': medians, 'artifacts': metadata['artifacts']}))


if __name__ == '__main__':
    main()
