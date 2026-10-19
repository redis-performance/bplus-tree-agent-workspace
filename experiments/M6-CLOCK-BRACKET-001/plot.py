#!/usr/bin/env python3
"""uv run --offline --with matplotlib python experiments/M6-CLOCK-BRACKET-001/plot.py"""
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

E = Path(__file__).resolve().parent
aa = json.loads((E / 'results/aa/summary.json').read_text())
controls = json.loads((E / 'results/controls/summary.json').read_text())
assert aa['complete'] and len(aa['rows']) == 48 and len(controls['rows']) == 72
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'svg.hashsalt': 'M6-clock-bracket001'})
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 2, left=.08, right=.97, top=.82, bottom=.16, hspace=.66, wspace=.16)
axes = [fig.add_subplot(gs[0, i]) for i in range(2)]
bottom = fig.add_subplot(gs[1, :])
fig.text(.08, .945, 'M6 clock brackets: controls and fresh baseline', fontsize=23, weight='bold', color='#173047')
counts = [sum(b['qualified'] for b in aa['blocks'] if b['size'] == n) for n in [100000, 1000000]]
fig.text(.08, .893, f"{aa['decision']} · wall A/A: 100K {counts[0]}/6, 1M {counts[1]}/6 · source NONE", fontsize=16, color='#a33e30' if aa['decision'] == 'PARK' else '#176b5b')
fig.text(.08, .852, 'Six timestamp reads · unchanged lookup work · all 48 lookup windows and 72 control rows retained', fontsize=12, color='#445a70')
all_effects = [b[k] for b in aa['blocks'] for k in ['wall_effect_percent', 'thread_effect_percent_diagnostic']]
limits = min(-1.5, min(all_effects) - .6), max(1.5, max(all_effects) + .6)
for ax, n in zip(axes, [100000, 1000000]):
    group = [b for b in aa['blocks'] if b['size'] == n]
    ax.axhspan(-1, 1, color='#e7f3ed')
    for y in [-1, 1]:
        ax.axhline(y, color='#60997f', linestyle='--', linewidth=1)
    ax.axhline(0, color='#8b98a6', linewidth=.8)
    ax.scatter([b['block'] + .92 for b in group], [b['wall_effect_percent'] for b in group], color='#b14636', s=50, label='Wall acceptance clock', zorder=3)
    ax.scatter([b['block'] + 1.08 for b in group], [b['thread_effect_percent_diagnostic'] for b in group], color='#245e99', marker='D', s=35, label='Thread CPU diagnostic', zorder=3)
    for b in group:
        if not b['qualified']:
            ax.annotate(f"{b['wall_effect_percent']:+.3f}%", (b['block'] + .92, b['wall_effect_percent']), xytext=(0, 10 if b['wall_effect_percent'] >= 0 else -17), textcoords='offset points', ha='center', fontsize=10)
    ax.set_title(('100K' if n == 100000 else '1M') + ' members', loc='left', weight='bold')
    ax.set_xticks(range(1, 7), [f'{i+1}\ns{i%3+1}' for i in range(6)])
    ax.set_xlim(.45, 6.55)
    ax.set_ylim(*limits)
    ax.grid(axis='y', color='#dce3e9', linewidth=.6)
    ax.set_axisbelow(True)
    ax.spines[['top', 'right']].set_visible(False)
axes[0].set_ylabel('Inner-pair difference from outer pair (%)')
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper left', bbox_to_anchor=(.075, .52), frameon=False, ncol=2, fontsize=11)
for index, (kind, color, marker) in enumerate([('empty', '#7b7d86', 'o'), ('cpu', '#245e99', 'D'), ('block', '#197968', 's')]):
    group = [r for r in controls['rows'] if r['raw']['control'] == kind]
    bottom.scatter([int(r['raw']['repetition']) + 1 + (index - 1) * .16 for r in group],
                   [r['bracket']['recorded_residual_ns'] / 1e6 for r in group], color=color, marker=marker, s=30, label=kind)
bottom.axhline(18, color='#60997f', linestyle='--', linewidth=1, label='Blocking sensitivity floor: 18 ms')
bottom.set_title('Empirical controls: 24 empty / CPU / 20 ms blocking triplets', loc='left', weight='bold')
bottom.set_xlabel('Repetition')
bottom.set_ylabel('Wall − thread (ms)')
bottom.set_xticks(range(1, 25))
bottom.set_xlim(.45, 24.55)
bottom.grid(axis='y', color='#dce3e9', linewidth=.6)
bottom.set_axisbelow(True)
bottom.spines[['top', 'right']].set_visible(False)
bottom.legend(loc='center left', bbox_to_anchor=(0, -.33), ncol=4, frameon=False, fontsize=10.5)
fig.text(.08, .045, 'Clock accuracy/accounting error remains unbounded; residuals and intervals are conditional diagnostics.', fontsize=11, color='#445a70')
fig.text(.08, .02, 'Fresh baseline qualification only. No timing rerun, candidate gain, architecture-specific guard or source adoption.', fontsize=11, color='#445a70')
fig.savefig(E / 'clock-brackets.png', dpi=170, facecolor='white')
fig.savefig(E / 'clock-brackets.svg', facecolor='white', metadata={'Date': None})
svg = E / 'clock-brackets.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
plt.close(fig)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
(E / 'chart.json').write_text(json.dumps({'input_sha256': {str(p.relative_to(E)): sha(p) for p in [E / 'results/aa/summary.json', E / 'results/controls/summary.json']},
    'plot_script_sha256': sha(Path(__file__)), 'matplotlib_version': matplotlib.__version__,
    'artifacts': {n: sha(E / n) for n in ['clock-brackets.png', 'clock-brackets.svg']}}, indent=2) + '\n')
print('Rendered clock-brackets.png and clock-brackets.svg')
