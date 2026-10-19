#!/usr/bin/env python3
"""uv run --offline --with matplotlib python experiments/M6-METROLOGY-001/plot.py"""
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
source = HERE / 'analysis.json'
data = json.loads(source.read_text())
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans', 'svg.hashsalt': 'm6-metrology001'})
fig, axes = plt.subplots(1, 2, figsize=(14, 7.3), sharey=True)
fig.subplots_adjust(left=.08, right=.97, top=.77, bottom=.25, wspace=.12)
fig.text(.08, .94, 'M6 lookup controls: wall time and thread CPU time', fontsize=22, weight='bold', color='#173047')
fig.text(.08, .875, 'All three failed 1M blocks remain outside ±1% on both recorded clocks', fontsize=15, color='#a63f30')
fig.text(.08, .825, 'Offline diagnosis · same baseline binary · all 48 original processes retained', fontsize=12, color='#445a70')
for ax, size in zip(axes, [100000, 1000000]):
    group = [b for b in data['blocks'] if b['size'] == size]
    ax.axhspan(-1, 1, color='#e7f3ed')
    for bound in [-1, 1]:
        ax.axhline(bound, color='#60997f', linestyle='--', linewidth=1)
    ax.axhline(0, color='#8292a0', linewidth=.8)
    ax.plot([b['block'] + 1 - .085 for b in group], [b['wall_effect_percent'] for b in group],
            'o', color='#b14636', markersize=8, label='Wall time (acceptance clock)')
    ax.plot([b['block'] + 1 + .085 for b in group], [b['thread_effect_percent'] for b in group],
            'D', color='#245e99', markersize=6, label='Thread CPU time (diagnostic)')
    for b in group:
        if not b['original_wall_qualified']:
            y = b['wall_effect_percent']
            ax.annotate(f"{y:+.3f}% / {b['thread_effect_percent']:+.3f}%", (b['block'] + 1, y),
                        xytext=(0, 16 if y > 0 else -22), textcoords='offset points', ha='center', fontsize=10.5)
    ax.set_title(('100K' if size == 100000 else '1M') + ' members', loc='left', weight='bold', pad=14)
    ax.set_xticks(range(1, 7), [f'{i+1}\nseed {i%3+1}' for i in range(6)])
    ax.set_xlim(.45, 6.55)
    ax.set_ylim(-1.95, 3.3)
    ax.grid(axis='y', color='#dce3e9', linewidth=.6)
    ax.set_axisbelow(True)
    ax.spines[['top', 'right']].set_visible(False)
axes[0].set_ylabel('ABBA inner-pair difference from outer pair (%)')
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower left', bbox_to_anchor=(.075, .12), frameon=False, ncol=2, fontsize=11)
fig.text(.08, .085, 'Thread and wall intervals have different boundaries; their difference is not exact off-CPU time.', fontsize=11, color='#445a70')
fig.text(.08, .045, 'No clock substitution, causal mechanism or optimization gain established. EXP-009 remains PARK; source NONE.', fontsize=11, color='#445a70')
fig.savefig(HERE / 'wall-thread.png', dpi=170, facecolor='white')
fig.savefig(HERE / 'wall-thread.svg', facecolor='white', metadata={'Date': None})
svg = HERE / 'wall-thread.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
plt.close(fig)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
(HERE / 'chart.json').write_text(json.dumps({'analysis_sha256': sha(source), 'script_sha256': sha(Path(__file__)),
    'matplotlib_version': matplotlib.__version__, 'artifacts': {name: sha(HERE / name) for name in ['wall-thread.png', 'wall-thread.svg']}}, indent=2) + '\n')
print('Rendered wall-thread.png and wall-thread.svg from analysis.json')
