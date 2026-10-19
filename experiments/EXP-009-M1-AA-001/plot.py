#!/usr/bin/env python3
"""Render the completed same-binary A/A block effects as an SVG."""

import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
result = json.loads((HERE / "results/summary.json").read_text())
assert len(result["blocks"]) == 12

width, height = 880, 400
left, right, top, bottom = 80, 835, 65, 345
ymin, ymax = -5.5, 5.5
px = lambda block: left + (block + 0.5) * (right - left) / 6
py = lambda value: bottom - (value - ymin) * (bottom - top) / (ymax - ymin)
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
         '<rect width="100%" height="100%" fill="white"/>',
         '<text x="80" y="27" font-family="sans-serif" font-size="18" font-weight="bold">Apple M1 lookup-hit same-binary A/A controls</text>',
         '<text x="80" y="47" font-family="sans-serif" font-size="12" fill="#555">Six ABBA blocks per size · effects are noise controls, not candidate speedups</text>',
         f'<rect x="{left}" y="{py(1):.2f}" width="{right-left}" height="{py(-1)-py(1):.2f}" fill="#e9f6ed"/>']
for tick in range(-5, 6):
    y = py(tick)
    color = '#4b9460' if abs(tick) == 1 else '#d9dfe5'
    parts.append(f'<line x1="{left}" y1="{y:.2f}" x2="{right}" y2="{y:.2f}" stroke="{color}" stroke-width="{1.5 if abs(tick)==1 else 1}"/>')
    parts.append(f'<text x="{left-12}" y="{y+4:.2f}" text-anchor="end" font-family="sans-serif" font-size="11" fill="#555">{tick:+d}%</text>')
for block in range(6):
    x = px(block)
    parts.append(f'<text x="{x:.2f}" y="{bottom+23}" text-anchor="middle" font-family="sans-serif" font-size="12">{block+1}</text>')
for size, color, offset in [(100000, '#1269a3', -9), (1000000, '#d56622', 9)]:
    points = [b for b in result['blocks'] if b['size'] == size]
    assert len(points) == 6
    for b in points:
        x, y = px(b['block']) + offset, py(b['effect_percent_display_only'])
        fill = color if b['qualified'] else 'white'
        parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="6" fill="{fill}" stroke="{color}" stroke-width="2"><title>{html.escape(str(size))}, block {b["block"]+1}: {b["effect_percent_display_only"]:+.4f}% — {"pass" if b["qualified"] else "fail"}</title></circle>')
parts.extend([f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#444"/>',
              f'<text x="{(left+right)/2}" y="{height-18}" text-anchor="middle" font-family="sans-serif" font-size="12">ABBA block</text>',
              '<circle cx="640" cy="42" r="5" fill="#1269a3"/><text x="652" y="46" font-family="sans-serif" font-size="12">100K (1/6 pass)</text>',
              '<circle cx="765" cy="42" r="5" fill="#d56622"/><text x="777" y="46" font-family="sans-serif" font-size="12">1M (2/6 pass)</text>',
              '</svg>'])
(HERE / 'aa-controls.svg').write_text('\n'.join(parts) + '\n')
