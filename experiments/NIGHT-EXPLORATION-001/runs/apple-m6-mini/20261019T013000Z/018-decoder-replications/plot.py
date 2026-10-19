#!/usr/bin/env python3
"""Plot audited M6 decoder diagnostics; no benchmarks, profiles or builds."""
import hashlib
import json
from pathlib import Path
import statistics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

BASE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PROVENANCE = {}


def load(path):
    path = Path(path)
    PROVENANCE[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return json.loads(path.read_text())


audits = {exp: load(BASE / f"EXP-{exp}/INDEPENDENT-AUDIT.json") for exp in ("004", "007", "008")}
summaries = {exp: load(BASE / f"EXP-{exp}/discovery/summary.json") for exp in audits}
confirmation_audit = load(BASE / "EXP-007/CONFIRMATION-AUDIT.json")
confirmation_summary = load(BASE / "EXP-007/confirmation/summary.json")
load(BASE / "EXP-007/CONFIRMATION-SEAL.json")
assert confirmation_audit["confirmation_complete"] and confirmation_audit["source_selection"] == "NONE"


def select(summary, phase, width, count=None, reverse=0):
    choices = [r for r in summary if r["phase"] == phase and r["width"] == width
               and r["reversed"] == reverse and (count is None or r["count"] == count)]
    assert len(choices) == 1
    return choices[0]


def row(label, variant, effects, control, contract, audited_median=None):
    aa = [r["percent"] for r in control["median_ns"]["block_effects"]]
    assert len(effects) == len(aa) == 6
    median = statistics.median(effects)
    if audited_median is not None:
        assert abs(median - audited_median) < 1e-9
    return dict(label=label, variant=variant, contract=contract, block_effects_pct=effects,
                median_pct=median, observed_min_pct=min(effects), observed_max_pct=max(effects),
                aa_block_effects_pct=aa, aa_median_pct=statistics.median(aa),
                aa_observed_min_pct=min(aa), aa_observed_max_pct=max(aa),
                aa_relative_pass=all(abs(x) <= 1 for x in aa), minimum10ms_pass=False,
                fully_qualified=False, interpretation="conditional private-kernel elapsed-time difference")


panels = []
rows = []
for width in (8, 60, 64):
    comparison = next(r for r in audits["004"]["comparisons"] if r["width"] == width and r["reversed"] == 0)
    control = select(summaries["004"], "aa", width)
    item = row(f"width{width} · A", "A", comparison["block_effects_pct"], control,
               dict(width=width, reversed=0, count="focused scalar loop"), comparison["median_pct"])
    assert item["aa_relative_pass"] == comparison["aa_relative_qualified"]
    rows.append(item)
panels.append(dict(title="EXP-004 · focused scalar decoder", subtitle="Forward widths 8/60/64 · A versus original control", rows=rows,
                   note="Relative A/A: 3/20 overall; no advancement", xlim=(-6, 19)))
rows = []
for variant in "ABC":
    comparison = next(r for r in audits["007"]["results"] if r["variant"] == variant)["primary"][0]
    item = row(variant, variant, comparison["block_effects_pct"], select(summaries["007"], "aa", 60, 96),
               dict(width=60, reversed=0, count=96), comparison["median_effect_pct"])
    assert item["aa_relative_pass"] == comparison["control_qualified"]
    rows.append(item)
panels.append(dict(title="EXP-007 · private bulk decoder", subtitle="Width 60 · forward · count 96 · all frozen variants", rows=rows,
                   note="Relative A/A: 14/30 overall; primary A/A FAIL", xlim=(-40, 9)))
rows = []
for count in (16, 96):
    for variant in "ABC":
        comparison = next(p for r in audits["008"]["results"] if r["variant"] == variant for p in r["primary"] if p["count"] == count)
        item = row(f"count{count} · {variant}", variant, comparison["block_effects_pct"], select(summaries["008"], "aa", 60, count),
                   dict(width=60, reversed=0, count=count), comparison["median_effect_pct"])
        assert item["aa_relative_pass"] == comparison["control_qualified"]
        rows.append(item)
panels.append(dict(title="EXP-008 · scalar/bulk cutoff", subtitle="Width 60 · forward · primary count 16 + count 96", rows=rows,
                   note="Relative A/A: 38/160 overall; all fail count 16 gain gate", xlim=(-18, 88)))
rows = []
for label, width, reverse, count in (("Primary · w60 F n96", 60, 0, 96),
                                     ("Guard · w62 R n96", 62, 1, 96),
                                     ("Guard · w63 F n7", 63, 0, 7)):
    comparison = select(confirmation_summary, "compare-A", width, count, reverse)
    effects = [r["percent"] for r in comparison["median_ns"]["block_effects"]]
    independently_derived = next(r for r in confirmation_audit["candidate"]["primary"] + confirmation_audit["candidate"]["qualified_control_guard_losses"]
                                 if (r["width"], r["reversed"], r["count"]) == (width, reverse, count))
    assert all(abs(a - b) < 1e-9 for a, b in zip(effects, independently_derived["block_effects_pct"]))
    rows.append(row(label, "A", effects, select(confirmation_summary, "aa", width, count, reverse),
                    dict(width=width, reversed=reverse, count=count), comparison["median_ns"]["median_effect_pct"]))
assert not rows[0]["aa_relative_pass"] and all(r["aa_relative_pass"] for r in rows[1:])
panels.append(dict(title="EXP-007 A · fresh same-M6 confirmation", subtitle="Fresh seeds · NOT an independent-machine confirmation", rows=rows,
                   note="Relative A/A: 14/30; primary FAIL; full 0/30\nSix guard median losses; two with passing relative controls shown", xlim=(-40, 9)))

assert audits["004"]["windows"]["short_below10ms_rows"] == audits["004"]["rows"] == 123840
assert audits["007"]["batch_window_screen"]["batches_below10ms"] == 371520
assert audits["008"]["batch_window_screen"]["batches_below10ms"] == 1981440
assert sum((audits["004"]["aa_full_window_qualified"], audits["007"]["workspace_fully_qualified_cells_including10ms"], audits["008"]["workspace_fully_qualified_cells_including10ms"])) == 0
assert confirmation_audit["batch_window_screen"]["batches_below10ms"] == confirmation_audit["batch_window_screen"]["total_batches"] == 185760
assert confirmation_audit["batch_window_screen"]["workspace_fully_qualified_cells"] == 0
data = dict(title="M6 exact decoder replications", status="ALL CONDITIONAL; PRIVATE KERNELS; NO TREE ADOPTION",
    discovery=dict(processes=19200, windows=2476800, windows_below10ms=2476800,
                   fully_qualified_cells=0, total_cells=210, relative_AA_pass_cells=55),
    confirmation=dict(experiment="EXP-007", selected_variant="A", same_machine=True,
                      independently_audited=True, independent_machine=False,
                      windows=185760, windows_below10ms=185760, fully_qualified_cells=0, total_cells=30,
                      audit=confirmation_audit),
    panels=panels, statistic="Median of 6 paired ABBA effects from 129-sample process medians",
    ranges="Observed 6 block minimum/maximum, not confidence intervals", units="Percent elapsed-time change within each frozen contract; negative=less elapsed time",
    source_provenance_sha256=PROVENANCE, script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    constraints="Legacy adapter; separated experiments/contracts; no cross-host or native-ns pooling; no new measurements; every discovery window<10 ms",
    participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact model/token/cost unknown")
(BASE / "decoder-replications.json").write_text(json.dumps(data, indent=2) + "\n")

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "svg.hashsalt": "M6-decoder-replications-018", "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(2, 2, figsize=(18, 14), gridspec_kw={"height_ratios": [1, 1.6]})
fig.subplots_adjust(top=.775, bottom=.18, left=.105, right=.91, hspace=.80, wspace=.55)
fig.suptitle("M6 exact decoder replications", fontsize=24, fontweight="bold", y=.97)
fig.text(.5, .927, "ALL RESULTS CONDITIONAL · PRIVATE DECODER KERNELS · NO TREE ADOPTION", ha="center", fontsize=15, color="#9a3412", fontweight="bold")
fig.text(.5, .875, "Discovery: all 2,476,800 windows <10 ms · full qualification 0/210 cells\nFresh A: all 185,760 windows <10 ms · full qualification 0/30 cells", ha="center", fontsize=15, fontweight="bold", linespacing=1.5, bbox=dict(boxstyle="round,pad=.5", facecolor="#fff2df", edgecolor="#f2b66f"))
fig.text(.5, .827, "Negative = less elapsed time within the same workload. Each experiment keeps its own frozen contract.", ha="center", fontsize=11)
palette = {"A": "#007d79", "B": "#2768b0", "C": "#8951a0"}
jitter = np.array([-.075, -.045, -.015, .015, .045, .075])
for panel_index, (ax, panel) in enumerate(zip(axes.flat, panels)):
    ax.set_title(panel["title"], loc="left", fontsize=14, fontweight="bold", pad=33)
    ax.text(0, 1.055, panel["subtitle"], transform=ax.transAxes, fontsize=10, color="#354254")
    ax.axvspan(-1, 1, color="#dfe5eb", alpha=.60)
    ax.axvline(0, color="#38465a", linewidth=.9)
    ax.axvline(-2, color="#d18b19", linestyle="--", linewidth=1)
    ax.axvline(1, color="#ce655e", linestyle=":", linewidth=.9)
    for index, item in enumerate(panel["rows"]):
        color = palette[item["variant"]]
        candidate_y, control_y = index - .14, index + .18
        ax.plot([item["observed_min_pct"], item["observed_max_pct"]], [candidate_y] * 2, color=color, linewidth=2, zorder=2)
        ax.scatter(item["block_effects_pct"], candidate_y + jitter, s=26, facecolors="white", edgecolors=color, linewidths=1.2, zorder=4)
        ax.scatter([item["median_pct"]], [candidate_y], marker="s", color=color, s=46, zorder=5)
        ax.plot([item["aa_observed_min_pct"], item["aa_observed_max_pct"]], [control_y] * 2, color="#7b8795", linewidth=1.25, zorder=2)
        ax.scatter(item["aa_block_effects_pct"], control_y + jitter * .8, s=18, marker="x", color="#77818c", linewidths=.9, zorder=3)
        ax.scatter([item["aa_median_pct"]], [control_y], marker="D", s=21, color="#7b8795", zorder=5)
        status = "PASS" if item["aa_relative_pass"] else "FAIL"
        ax.text(1.015, candidate_y, f'{item["median_pct"]:+.2f}%', transform=ax.get_yaxis_transform(), va="center", color=color, fontweight="bold", fontsize=10)
        ax.text(1.015, control_y, "AA " + status, transform=ax.get_yaxis_transform(), va="center", color="#47654b" if status == "PASS" else "#9a3e35", fontsize=9)
    ax.set_yticks(range(len(panel["rows"])), [r["label"].replace("count", "n").replace("width", "w") for r in panel["rows"]])
    ax.set_ylim(len(panel["rows"]) - .45, -.55)
    ax.set_xlim(*panel["xlim"])
    ax.set_xlabel("Elapsed-time change (%)", fontsize=10)
    ax.grid(axis="x", color="#d7dde5", linewidth=.5)
    ax.tick_params(axis="y", length=0)
    ax.text(0, -.27 if panel_index < 2 else -.14, panel["note"], transform=ax.transAxes, fontsize=9, color="#4d5968", va="top")
handles = [Line2D([0], [0], marker="o", markerfacecolor="white", color="#007d79", label="Variant: 6 block points, square median, observed range"),
           Line2D([0], [0], marker="x", color="#7b8795", label="A/A: 6 block points, diamond median, observed range"),
           Line2D([0], [0], linestyle="--", color="#d18b19", label="−2% gain reference"),
           Line2D([0], [0], linestyle=":", color="#ce655e", label="+1% loss reference")]
fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(.5, .056), ncol=2, frameon=False, fontsize=10)
fig.text(.5, .032, "Gray band: ±1% relative A/A screen. Passing it does not clear the 10 ms precision requirement. Bars are observed ranges, not confidence intervals.", ha="center", fontsize=10)
fig.text(.5, .013, "M6 only · legacy adapter · short-window diagnostics · profiled timing rows excluded · no source acceptance", ha="center", fontsize=10, color="#7c3a27")
fig.savefig(BASE / "decoder-replications.png", dpi=175, facecolor="white")
fig.savefig(BASE / "decoder-replications.svg", facecolor="white", metadata={"Date": None})
plt.close(fig)
print("Wrote audited chart PNG/SVG/data; all effects conditional")
