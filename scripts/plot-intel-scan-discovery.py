#!/usr/bin/env python3
"""Render the independently audited Intel discovery; never imply acceptance."""
import json
from pathlib import Path
import statistics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
NIGHT = ROOT / "experiments/NIGHT-EXPLORATION-001"
OUT = NIGHT / "latest-charts"
audit = json.loads((NIGHT / "reviews/aws-intel-scan-raw-audit.json").read_text())
chart = {
    "source_audit": "../reviews/aws-intel-scan-raw-audit.json",
    "worker_revision": audit["worker_revision"],
    "status": "Discovery checkpoint only; follow-up evidence is in the decision ledger; source NONE",
    "metric": "paired elapsed_ns / actual callback count change, percent; negative is faster",
    "ranges": "observed six-block minimum and maximum, not confidence intervals",
    "selection": "B by preregistered source-maintenance preference, not A/B speed superiority",
    "cases": {},
}
fig, axes = plt.subplots(1, 2, figsize=(13, 4.8), sharex=True, sharey=True)
colors = ["#64748b", "#157eab", "#7a48a3"]
for ax, size in zip(axes, [100000, 1000000]):
    groups = [
        ("Same binary A/A", audit["phases"]["aa"]["summary"][f"base/{size}"]),
        ("Variant A", audit["phases"]["screen"]["summary"][f"A/{size}"]),
        ("Variant B", audit["phases"]["screen"]["summary"][f"B/{size}"]),
    ]
    chart["cases"][str(size)] = {}
    ax.axvspan(-1, 1, color="#e2e8f0", alpha=0.55)
    ax.axvline(0, color="#475569", linewidth=1)
    ax.axvline(-2, color="#15803d", linestyle="--", linewidth=1)
    for y, ((label, result), color) in enumerate(zip(groups, colors)):
        values = [r["effect_pct"] for r in result["effects"]]
        median = statistics.median(values)
        chart["cases"][str(size)][label] = values
        ax.hlines(y, min(values), max(values), color=color, linewidth=2)
        ax.scatter(values, [y + (i - 2.5) * 0.035 for i in range(6)],
                   color=color, s=28, alpha=0.7, zorder=3)
        ax.scatter([median], [y], marker="D", color=color, edgecolor="white",
                   linewidth=0.7, s=65, zorder=4)
        ax.text(median, y + 0.28, f"median {median:+.3f}%", ha="center",
                va="center", fontsize=10, color=color)
    ax.set_title(f"{size:,} members · 16-byte keys", fontsize=12, pad=12)
    ax.set_yticks(range(3), [x[0] for x in groups])
    ax.tick_params(axis="y", labelleft=True)
    ax.set_ylim(2.6, -0.5)
    ax.set_xlim(-8.5, 1.3)
    ax.set_xticks([-8, -6, -4, -2, 0, 1])
    ax.set_xlabel("Paired elapsed change (%) · lower is faster")
    ax.grid(axis="x", alpha=0.17)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
fig.suptitle("Intel SCAN discovery — primary gates pass; source unchanged", fontsize=16, y=0.98)
fig.text(0.5, 0.887, "Six ABBA blocks per group · both A/A controls qualify · green dashed line: −2% primary gate",
         ha="center", fontsize=10, color="#334155")
fig.text(0.5, 0.075, "B advances by predeclared source preference. Follow-up evidence and limitations are reported separately.",
         ha="center", fontsize=10, color="#334155")
fig.text(0.5, 0.025, "Dots: individual blocks · diamonds: medians · lines: observed ranges, not confidence intervals · source unchanged",
         ha="center", fontsize=9, color="#475569")
fig.subplots_adjust(left=0.10, right=0.98, top=0.78, bottom=0.23, wspace=0.29)
OUT.mkdir(exist_ok=True)
for ext in ["png", "svg"]:
    fig.savefig(OUT / f"intel-scan-discovery.{ext}", dpi=170, facecolor="white")
(OUT / "intel-scan-discovery.json").write_text(json.dumps(chart, indent=2) + "\n")
