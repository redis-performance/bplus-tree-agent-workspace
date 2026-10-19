#!/usr/bin/env python3
"""Render only M6-LOOKUP-CALLER-001, reconstructing effects from raw CSV rows."""
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator, PercentFormatter

OUT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((OUT / name).read_text())


def reconstruct(phase, cell):
    selected = [r for r in phase["runs"] if r["cell"] == cell]
    assert len(selected) == 24
    rows, effects, memory = [], [], []
    for block in range(6):
        group = sorted((r for r in selected if r["block"] == block), key=lambda r: r["step"])
        assert [r["label"] for r in group] == list("ABBA")
        assert len({r["operations"] for r in group}) == 1
        assert len({r["checksum"] for r in group}) == 1
        block_rows = []
        for row in group:
            path = OUT / row["file"]
            assert sha(path) == row["sha256"], path.name
            with path.open() as handle:
                raw = list(csv.DictReader(handle))
            assert len(raw) == 1
            raw = raw[0]
            elapsed, operations = int(raw["elapsed_ns"]), int(raw["operations"])
            assert elapsed == row["elapsed_ns"] and operations == row["operations"]
            assert raw["checksum"] == row["checksum"]
            assert int(raw["tree_bytes"]) == row["tree_bytes"]
            ns_op = elapsed / operations
            assert math.isclose(ns_op, row["ns_op"], rel_tol=0, abs_tol=1e-12)
            block_rows.append(dict(block=block, step=row["step"], label=row["label"],
                                   seed=row["seed"], variant=row["variant"],
                                   elapsed_ns=elapsed, operations=operations,
                                   ns_op=ns_op, tree_bytes=int(raw["tree_bytes"]),
                                   checksum=raw["checksum"], file=row["file"],
                                   sha256=row["sha256"]))
        a = [r for r in block_rows if r["label"] == "A"]
        b = [r for r in block_rows if r["label"] == "B"]
        effects.append(100 * (statistics.mean(r["ns_op"] for r in b) /
                              statistics.mean(r["ns_op"] for r in a) - 1))
        memory.append(100 * (statistics.mean(r["tree_bytes"] for r in b) /
                             statistics.mean(r["tree_bytes"] for r in a) - 1))
        rows.extend(block_rows)
    stored = next(r for r in phase["results"] if r["cell"] == cell)
    assert all(abs(a - b) < 1e-12 for a, b in zip(effects, stored["effects_pct"]))
    median = statistics.median(effects)
    assert abs(median - stored["median_pct"]) < 1e-12
    shortest = min(r["elapsed_ns"] for r in rows) / 1e6
    return dict(cell=cell, effects_pct=effects, median_pct=median,
                min_pct=min(effects), max_pct=max(effects),
                memory_effects_pct=memory, shortest_window_ms=shortest,
                all_blocks_pass_speed_gate=max(effects) <= -2 and shortest >= 10,
                raw_rows=rows)


def main():
    plan, freeze = read("PLAN.json"), read("freeze.json")
    assert plan["identity"] == "M6-LOOKUP-CALLER-001"
    cells = plan["primaries"]
    assert cells == ["lookup-n100000-lookup-hit-m16-b1", "lookup-n1000000-lookup-hit-m16-b1"]
    aa = read("aa.json")
    assert aa["status"] == "complete"
    controls = {}
    for cell in cells:
        data = reconstruct(aa, cell)
        data["max_absolute_effect_pct"] = max(map(abs, data["effects_pct"]))
        data["qualified"] = data["max_absolute_effect_pct"] <= 1 and data["shortest_window_ms"] >= 10
        assert data["qualified"] == next(r for r in aa["results"] if r["cell"] == cell)["qualified"]
        controls[cell] = data
    assert controls[cells[0]]["qualified"] and not controls[cells[1]]["qualified"]
    variants = {}
    for variant in "ABC":
        phase = read(f"screen-{variant}.json")
        assert phase["status"] == "complete" and phase["variant"] == variant
        variants[variant] = {cell: reconstruct(phase, cell) for cell in cells}
        assert not all(variants[variant][cell]["all_blocks_pass_speed_gate"] for cell in cells)
    inputs = ["PLAN.json", "freeze.json", "aa.json", "screen-A.json", "screen-B.json", "screen-C.json"]
    provenance = dict(source_commit=freeze["source_commit"],
                      source_sha256=freeze["files"]["worktrees/m6-caller-control/src/zset_btree.c"],
                      candidate_source_sha256={v: freeze["files"][f"worktrees/m6-caller-{v}/src/zset_btree.c"] for v in "ABC"},
                      candidate_patch_sha256={v: sha(OUT / "variants" / v / "candidate.patch") for v in "ABC"},
                      lookup_referee_sha256=freeze["files"][str(OUT.relative_to(Path.cwd()) / "referees/lookup.c")],
                      lookup_binary_sha256={v: freeze["binaries"][f"scratch/m6-caller/build/{v}-lookup"] for v in "0ABC"},
                      input_json_sha256={name: sha(OUT / name) for name in inputs},
                      host=freeze["host"], compiler=freeze["compiler"],
                      plot_script_sha256=sha(Path(__file__)))
    data = dict(experiment=plan["identity"], decision="REJECT dual primary / NONE",
                baseline_unchanged=True, scope="Apple M6 only; public single-query hit lookup; 16-byte binary members",
                formula="100 * (mean candidate ns/op / mean control ns/op - 1), per ABBA block",
                block_count=6, discovery_seeds=plan["discovery_seeds"],
                matplotlib_version=matplotlib.__version__,
                interpretation="Negative = less elapsed time; segments are observed block min/max, not confidence intervals",
                primary_gate="Every block must be <= -2% at BOTH primary sizes; same-session controls must qualify",
                confirmation="NOT RUN; no dual-primary contender", provenance=provenance,
                controls=controls, variants=variants,
                participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact serving model/token usage/cost unknown")
    (OUT / "chart-data.json").write_text(json.dumps(data, indent=2) + "\n")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "svg.fonttype": "none", "axes.spines.top": False,
                         "axes.spines.right": False, "axes.spines.left": False,
                         "axes.edgecolor": "#ccd2d9", "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(13.8, 6.2), sharex=True, sharey=True)
    fig.subplots_adjust(left=.075, right=.975, top=.72, bottom=.255, wspace=.24)
    colors = {"A": "#2563a8", "B": "#c56c13", "C": "#7347a5"}
    offsets = [-.12, -.072, -.024, .024, .072, .12]
    y_positions = [2, 1, 0]
    for ax, cell, label in zip(axes, cells, ["100K members", "1M members"]):
        control = controls[cell]
        state = "QUALIFIED" if control["qualified"] else "FAILED"
        state_color = "#23684b" if control["qualified"] else "#a63232"
        ax.set_title(label, loc="left", fontsize=15, fontweight="bold", pad=39)
        ax.text(0, 1.04, f"A/A control {state}  ·  max |effect| {control['max_absolute_effect_pct']:.3f}%",
                transform=ax.transAxes, color=state_color, fontsize=10.5)
        ax.axvspan(-5.3, -2, color="#edf6f0", zorder=0)
        ax.axvline(0, color="#6f7782", lw=1.3, zorder=1)
        ax.axvline(-2, color="#478461", lw=1.4, ls=(0, (4, 3)), zorder=1)
        for variant, y in zip("ABC", y_positions):
            item = variants[variant][cell]
            color = colors[variant]
            ax.hlines(y, item["min_pct"], item["max_pct"], color=color, lw=3, alpha=.48, zorder=2)
            ax.scatter(item["effects_pct"], [y + off for off in offsets], s=36,
                       color=color, edgecolor="white", linewidth=.65, zorder=3)
            ax.scatter([item["median_pct"]], [y], marker="D", s=82, color=color,
                       edgecolor="#17212c", linewidth=1, zorder=4)
            ax.text(-5.15, y + .29, f"median {item['median_pct']:+.3f}%", color=color, fontsize=10)
        ax.set_yticks(y_positions, ["A", "B", "C"], fontweight="bold", fontsize=12)
        ax.tick_params(axis="y", length=0, pad=12, labelleft=True)
        ax.set_ylim(-.5, 2.62)
        ax.set_xlim(-5.3, 2.5)
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
        ax.grid(axis="x", color="#e5e8ed", linewidth=.7)
        ax.set_axisbelow(True)
        ax.set_xlabel("Change in elapsed time versus unchanged control", labelpad=10, fontsize=10.5)
    fig.text(.075, .945, "Apple M6 · Caller specialization", fontsize=21, fontweight="bold", color="#17212c")
    fig.text(.075, .89, "All A/B/C REJECT dual primary · baseline unchanged", fontsize=13, color="#a63232", fontweight="bold")
    fig.text(.075, .842, "M6-LOOKUP-CALLER-001  |  16-byte members · public single-query hits · six serial ABBA blocks per size", fontsize=10.5, color="#55616e")
    handles = [Line2D([0], [0], marker="o", color="none", markerfacecolor="#566273", markersize=6, label="One block"),
               Line2D([0], [0], marker="D", color="none", markerfacecolor="#566273", markersize=7, label="Median"),
               Line2D([0], [0], color="#8994a2", lw=3, label="Observed min–max"),
               Line2D([0], [0], color="#478461", lw=1.4, ls=(0, (4, 3)), label="−2% speed gate")]
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(.068, .115), ncol=4,
               frameon=False, fontsize=10, handlelength=2, columnspacing=2.4)
    fig.text(.075, .082, "Negative = less elapsed time. Gate requires ≤−2% in EVERY block at BOTH sizes; no candidate qualifies.", fontsize=10, color="#394756")
    fig.text(.075, .041, "Segments are observed block ranges, not confidence intervals. 1M precision failed; confirmation and candidate guards not run.", fontsize=9.5, color="#5a6571")
    fig.savefig(OUT / "candidate-screens.png", dpi=190, facecolor="white")
    fig.savefig(OUT / "candidate-screens.svg", facecolor="white", metadata={"Date": None})
    plt.close(fig)
    print("Rendered candidate-screens.png/.svg; verified192 raw CSV rows and48 block effects (36 candidate +12 control).")


if __name__ == "__main__":
    main()
