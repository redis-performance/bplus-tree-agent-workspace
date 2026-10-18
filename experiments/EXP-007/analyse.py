#!/usr/bin/env python3
"""Report process distributions and paired effects, without treating inner samples as independent trials."""
import argparse
from collections import defaultdict
import csv
import json
from pathlib import Path
import statistics

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('directory')
a = p.parse_args()
root = Path(a.directory)
manifest = json.loads((root/'manifest.json').read_text())
if manifest['status'] != 'complete':
    raise SystemExit('Incomplete campaign: inspect manifest; do not summarise as a completed result')
rows = json.loads((root/'process-summary.json').read_text())
groups = defaultdict(list)
for row in rows:
    groups[(row['phase'], row['width'], row['reversed'], row['count'])].append(row)
results = []
for (phase, width, reverse, count), group in sorted(groups.items()):
    result = dict(phase=phase, width=width, reversed=reverse, count=count)
    for statistic in ('min_ns', 'median_ns'):
        effects = []
        for block in sorted({r['block'] for r in group}):
            pair = [r for r in group if r['block'] == block]
            av = statistics.mean(r[statistic] for r in pair if r['label'] == 'A')
            bv = statistics.mean(r[statistic] for r in pair if r['label'] == 'B')
            effects.append(dict(block=block, seed=pair[0]['seed'], percent=100*(bv/av-1)))
        result[statistic] = dict(A=statistics.median(r[statistic] for r in group if r['label'] == 'A'),
                                B=statistics.median(r[statistic] for r in group if r['label'] == 'B'),
                                block_effects=effects, median_effect_pct=statistics.median(e['percent'] for e in effects),
                                effect_min_pct=min(e['percent'] for e in effects), effect_max_pct=max(e['percent'] for e in effects))
    result['min_batch_ns'] = min(r['min_batch_ns'] for r in group)
    result['endpoint_migrations'] = sum(r['endpoint_migrations'] for r in group)
    results.append(result)
(root/'summary.json').write_text(json.dumps(results, indent=2)+'\n')
lines = ['# EXP-007 bulk decoder diagnostic', '',
         'Percentages are candidate/control elapsed-time changes (negative means lower time).',
         'Each effect pairs process statistics within an ABBA block. All inner samples and',
         'all blocks are retained. Ranges below are observed block ranges, not confidence intervals.',
         'A/A uses the exact same binary. No source acceptance or iterator-guard conclusion follows.',
         'Column A is the baseline role; column B is also baseline in aa and the indicated candidate in compare-X.', '',
         '| Phase | Width | Reverse | Count | A median ns/decode | B median ns/decode | Median effect % [block range] | Minimum effect % [block range] |',
         '|---|---:|---:|---:|---:|---:|---|---|']
for r in results:
    m, n = r['median_ns'], r['min_ns']
    lines.append(f"| {r['phase']} | {r['width']} | {r['reversed']} | {r['count']} | {m['A']:.3f} | {m['B']:.3f} | {m['median_effect_pct']:+.2f} [{m['effect_min_pct']:+.2f}, {m['effect_max_pct']:+.2f}] | {n['median_effect_pct']:+.2f} [{n['effect_min_pct']:+.2f}, {n['effect_max_pct']:+.2f}] |")
(root/'SUMMARY.md').write_text('\n'.join(lines)+'\n')

# Portable histogram data: 0.05 ns bins, retain phase/variant/fixture identity.
histogram = defaultdict(int)
for run in manifest['runs']:
    with (root/run['csv']).open() as handle:
        for row in csv.DictReader(handle):
            bucket = int(float(row['ns_per_decode'])/.05)
            histogram[(run['phase'], run['variant'], run['width'], run['reversed'], run['count'], bucket)] += 1
with (root/'histogram.csv').open('w') as handle:
    writer = csv.writer(handle, lineterminator='\n')
    writer.writerow(['phase', 'variant', 'width', 'reversed', 'count', 'bin_lower_ns', 'bin_upper_ns', 'samples'])
    for (phase, variant, width, reverse, leafcount, bucket), count in sorted(histogram.items()):
        writer.writerow([phase, variant, width, reverse, leafcount, f'{bucket*.05:.2f}', f'{(bucket+1)*.05:.2f}', count])
print(f'Wrote {len(results)} cell summaries and histogram.csv; no acceptance decision')

controls={(r['width'],r['reversed'],r['count']):r for r in results if r['phase']=='aa'}
candidates=[]
for phase in sorted({r['phase'] for r in results if r['phase']!='aa'}):
    cells=[r for r in results if r['phase']==phase]
    primary=next(r for r in cells if (r['width'],r['reversed'],r['count'])==(60,0,96))
    bad=[dict(width=r['width'],reversed=r['reversed'],count=r['count'],effect=r['median_ns']['median_effect_pct']) for r in cells if r['median_ns']['median_effect_pct']>1]
    unqualified=[dict(width=r['width'],reversed=r['reversed'],count=r['count']) for r in cells if not(-1<=controls[(r['width'],r['reversed'],r['count'])]['median_ns']['effect_min_pct'] and controls[(r['width'],r['reversed'],r['count'])]['median_ns']['effect_max_pct']<=1)]
    candidates.append(dict(variant=phase[-1],primary_effect_pct=primary['median_ns']['median_effect_pct'],guard_median_regressions=bad,unqualified_cells=unqualified))
(root/'selection-input.json').write_text(json.dumps(candidates,indent=2)+'\n')
print(json.dumps([dict(variant=r['variant'],primary=r['primary_effect_pct'],guard_regressions=len(r['guard_median_regressions']),unqualified=len(r['unqualified_cells'])) for r in candidates]))
