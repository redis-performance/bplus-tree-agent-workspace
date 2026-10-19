#!/usr/bin/env python3
"""Plot retained sampled locations; never interpret counts as cycle weights."""
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

BASE = Path(__file__).resolve().parent
rows = json.loads((BASE / "summary.json").read_text())
assert len(rows) == 16 and sum(r["sample_count"] for r in rows) == 2469
classes = ["text-symbol", "external-symbol", "import-stub-unknown-target"]
actual_classes = {b["classification"] for r in rows for b in r["pc_bins"]}
assert len(actual_classes) == 3, actual_classes
# Preserve the exact actual classifier spelling in the output data.
unknown = actual_classes - set(classes[:2])
assert len(unknown) == 1
classes[2] = unknown.pop()
assert [sum(b["samples"] for r in rows for b in r["pc_bins"] if b["classification"] == k) for k in classes] == [1422, 1037, 10]
colors = ["#2563a6", "#d38c28", "#7c598f"]
fig, axes = plt.subplots(2, 2, figsize=(13, 8), sharex=True)
data = []
for ax, case in zip(axes.flat, ["lookup-hit", "lookup-miss", "rank", "scan"]):
    subset = [r for r in rows if r["case"] == case]
    assert len(subset) == 4
    labels = [f'{"1M" if r["size"] == 1000000 else "100K"} · seed {r["seed"]}' for r in subset]
    left = [0] * 4
    for kind, color in zip(classes, colors):
        values = [sum(b["samples"] for b in r["pc_bins"]
                      if b["classification"] == kind) for r in subset]
        ax.barh(range(4), values, left=left, color=color, height=.6)
        left = [x + y for x, y in zip(left, values)]
    for i, (r, total) in enumerate(zip(subset, left)):
        assert total == r["sample_count"] and r["sufficient"] and not r["capped"]
        ax.text(total + 5, i, str(total), va="center", fontsize=10)
        data.append({"case": case, "size": r["size"], "seed": r["seed"],
                     "total": total, "counts": {kind: sum(b["samples"] for b in r["pc_bins"]
                         if b["classification"] == kind) for kind in classes}})
    ax.set_yticks(range(4), labels)
    ax.invert_yaxis()
    ax.set_title(case, loc="left", weight="bold", pad=9)
    ax.set_xlim(0, 475)
    ax.set_xlabel("Retained PC observations · counts, not cycles")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", alpha=.18)
    ax.set_axisbelow(True)
fig.suptitle("Apple M6 · corrected-adapter member-index profile", fontsize=19,
             x=.035, ha="left", y=.985, weight="bold")
fig.text(.035, .925, "16 fixed captures · 2,469 observations · independent raw audit PASS · source selection NONE",
         fontsize=12)
fig.legend([Patch(color=c) for c in colors],
           ["Program text (1,422)", "External libraries (1,037)", "Import stubs: target unknown (10)"],
           loc="lower left", bbox_to_anchor=(.025, .055), ncol=3, frameon=False)
fig.text(.035, .025,
         "Descriptive locations only: no cycle cost, cache latency, unbiased time share or speedup is inferred.\n"
         "All original captures retained once; metadata repair pause recorded separately. Sampling frontend differs from timing frontend.",
         fontsize=10, color="#444444")
fig.tight_layout(rect=(.02, .14, .99, .89), h_pad=2.4, w_pad=2.5)
for ext in ("png", "svg"):
    fig.savefig(BASE / f"member-index-profile.{ext}", dpi=160, facecolor="white")
payload = {"interpretation": "sampled PC locations only; not cycles or time shares",
           "source_candidate": "NONE", "input_sha256": hashlib.sha256((BASE / "summary.json").read_bytes()).hexdigest(),
           "captures": data}
(BASE / "member-index-profile.json").write_text(json.dumps(payload, indent=2) + "\n")
print("16 captures / 2469 observations conserved; PNG, SVG and chart data written")
