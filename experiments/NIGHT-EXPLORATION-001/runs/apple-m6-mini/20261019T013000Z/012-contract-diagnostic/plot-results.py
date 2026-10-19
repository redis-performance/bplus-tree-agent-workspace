#!/usr/bin/env python3
"""Chart the matched adapter diagnostic using exact raw-CSV block ratios."""
import csv
import hashlib
import json
import math
import re
import statistics
from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator, PercentFormatter

OUT = Path(__file__).resolve().parent
OWNED = ["plot-results.py", "chart-data.json", "adapter-diagnostic.png", "adapter-diagnostic.svg", "CHART.md"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((OUT / name).read_text())


def reconstruct(phase, cell, comparison):
    selected = [r for r in phase["runs"] if r["cell"] == cell and r["comparison"] == comparison]
    assert len(selected) == 24
    rows, effects, exact, memory = [], [], [], []
    for block in range(6):
        group = sorted((r for r in selected if r["block"] == block), key=lambda r: r["step"])
        assert [r["label"] for r in group] == list("ABBA")
        assert len({r["operations"] for r in group}) == 1
        block_rows = []
        for row in group:
            log = row["logs"]["stdout"]
            path = OUT / log["file"]
            assert sha(path) == log["sha256"]
            with path.open() as handle:
                raw = list(csv.DictReader(handle))
            assert len(raw) == 1
            raw = raw[0]
            elapsed, ops = int(raw["elapsed_ns"]), int(raw["operations"])
            assert raw == row["csv"]
            assert elapsed == row["elapsed_ns"] and ops == row["operations"] == 100000000
            assert raw["checksum"] == raw["expected_checksum"] == row["checksum"]
            assert int(raw["tree_bytes"]) == row["tree_bytes"]
            assert math.isclose(elapsed / ops, row["ns_op"], rel_tol=0, abs_tol=1e-12)
            block_rows.append(dict(block=block, step=row["step"], label=row["label"], adapter=row["adapter"],
                                   seed=row["seed"], elapsed_ns=elapsed, operations=ops,
                                   checksum=raw["checksum"], tree_bytes=int(raw["tree_bytes"]),
                                   construction_fingerprint=raw["construction_fingerprint"],
                                   file=log["file"], sha256=log["sha256"]))
        for field in ("checksum", "tree_bytes", "construction_fingerprint"):
            assert len({r[field] for r in block_rows}) == 1
        a = [r for r in block_rows if r["label"] == "A"]
        b = [r for r in block_rows if r["label"] == "B"]
        effect = 100 * (Fraction(sum(r["elapsed_ns"] for r in b), sum(r["elapsed_ns"] for r in a)) - 1)
        mem = 100 * (Fraction(sum(r["tree_bytes"] for r in b), sum(r["tree_bytes"] for r in a)) - 1)
        exact.append(str(effect))
        effects.append(float(effect))
        memory.append(float(mem))
        rows.extend(block_rows)
    stored = next(r for r in phase["results"] if r["cell"] == cell and r["comparison"] == comparison)
    assert all(abs(a - b) < 1e-9 for a, b in zip(effects, stored["effects_pct"]))
    median = statistics.median(effects)
    assert abs(median - stored["median_pct"]) < 1e-9
    shortest = min(r["elapsed_ns"] for r in rows) / 1e6
    return dict(comparison=comparison, cell=cell, effects_pct=effects, exact_effect_fractions=exact,
                median_pct=median, observed_min_pct=min(effects), observed_max_pct=max(effects),
                memory_effects_pct=memory, shortest_window_ms=shortest,
                max_absolute_effect_pct=max(map(abs, effects)), raw_rows=rows)


def hygiene():
    patterns = [r"/" + r"Users/[^\s\"']+", r"/" + r"home/[^\s\"']+",
                r"/var/" + r"folders/[A-Za-z0-9_]+/", r"AKIA[0-9A-Z]{16}",
                r"gh[pousr]_[A-Za-z0-9]{20,}", r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----"]
    for name in OWNED:
        path = OUT / name
        content = path.read_bytes().decode("latin1") if path.suffix == ".png" else path.read_text()
        for pattern in patterns:
            assert not re.search(pattern, content), (name, "private path/credential pattern")


def main():
    plan, freeze = read("PLAN.json"), read("freeze.json")
    immutable_names = ["PLAN.json", "driver.py", "README.md", "freeze.json"]
    before = {name: sha(OUT / name) for name in immutable_names}
    aa, comparison = read("aa.json"), read("compare.json")
    assert aa["status"] == comparison["status"] == "complete"
    assert len(aa["runs"]) == 384 and len(comparison["runs"]) == 192
    cells = plan["cells"]
    controls, matched = {}, {}
    for cell in cells:
        key = cell["id"]
        controls[key] = {}
        for adapter in ("old", "new"):
            data = reconstruct(aa, key, adapter)
            data["qualified"] = data["max_absolute_effect_pct"] <= 1 and data["shortest_window_ms"] >= 10
            stored = next(x for x in aa["results"] if x["cell"] == key and x["comparison"] == adapter)
            assert data["qualified"] == stored["qualified"]
            controls[key][adapter] = data
        data = reconstruct(comparison, key, "old-vs-new")
        data["both_adapter_controls_qualified"] = all(x["qualified"] for x in controls[key].values())
        data["conditional"] = not data["both_adapter_controls_qualified"] or data["shortest_window_ms"] < 10
        assert data["both_adapter_controls_qualified"] == next(x for x in comparison["results"] if x["cell"] == key)["both_adapter_controls_qualified"]
        matched[key] = data
    qualified = sum(c["qualified"] for cell in controls.values() for c in cell.values())
    jointly_qualified = sum(c["both_adapter_controls_qualified"] for c in matched.values())
    assert qualified == 3 and jointly_qualified == 0
    assert all(x["conditional"] and x["memory_effects_pct"] == [0.0] * 6 for x in matched.values())
    frozen = freeze["files_sha256"]
    ref_key = next(key for key in frozen if key.endswith("/012-contract-diagnostic/iterator.c"))
    data = dict(identity=plan["identity"], classification="Harness/adapter contract diagnostic; no tree candidate or optimization acceptance",
                qualification="ALL CONDITIONAL: 0/8 cells qualify both adapter controls; 3/16 A/A controls qualify",
                qualified_aa_controls=qualified, jointly_qualified_cells=jointly_qualified,
                memory_change_pct=0, negative_means="less elapsed time",
                formula="100 * (mean new-adapter ns/item / mean old-adapter ns/item - 1), per ABBA block",
                summary="Six-block medians and observed min/max; circles are all six block points; ranges are not confidence intervals",
                measured_adapter_difference="Truthful C11 _Noreturn contract only; same native compiler/flags, tree source/header, referee, hashing and allocator",
                discovery_seeds=plan["seeds"], items_per_process=100000000,
                provenance=dict(input_json_sha256={n: sha(OUT / n) for n in [*immutable_names, "aa.json", "compare.json", "AUTHORIZATION.json"]},
                                source_c_sha256=frozen["src/zset_btree.c"], source_h_sha256=frozen["src/zset_btree.h"],
                                adapter_sha256={a: {n: frozen[str(Path(p) / n)] for n in ("server.h", "standalone.c")} for a, p in plan["adapters"].items()},
                                iterator_sha256=frozen[ref_key], microbench_sha256=frozen[ref_key.replace("iterator.c", "microbench.c")],
                                binaries_sha256=freeze["binaries_sha256"], compiler=freeze["compiler"],
                                plot_script_sha256=sha(Path(__file__)), matplotlib_version=matplotlib.__version__),
                controls=controls, matched_effects=matched,
                public_hygiene="Own five chart artifacts scanned for concrete private paths and credential patterns; PNG contains standard Matplotlib metadata only",
                participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact serving model/token usage/cost unknown")
    (OUT / "chart-data.json").write_text(json.dumps(data, indent=2) + "\n")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "svg.fonttype": "none",
                         "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
                         "axes.edgecolor": "#c9d0d8", "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(15.2, 7.5), sharex=True, sharey=True)
    fig.subplots_adjust(left=.19, right=.975, top=.705, bottom=.225, wspace=.20)
    labels = ["Integer · full\nforward", "Integer · full\nreverse", "Integer · score only\nforward", "Fraction · full\nforward"]
    colors = ["#2465a3", "#794c9b", "#ba6e22", "#287c82"]
    point_offsets = [-.20, -.155, -.11, .11, .155, .20]
    for ax, size, title in zip(axes, (100000, 1000000), ("100K members", "1M members")):
        ax.set_title(title, loc="left", fontweight="bold", fontsize=15, pad=16)
        ax.axvline(0, color="#727c89", lw=1.4, zorder=1)
        for index, color in enumerate(colors):
            cell = cells[index if size == 100000 else index + 4]
            item, control = matched[cell["id"]], controls[cell["id"]]
            y = 3 - index
            ax.hlines(y, item["observed_min_pct"], item["observed_max_pct"], color=color, alpha=.5, lw=3, zorder=2)
            ax.scatter(item["effects_pct"], [y + offset for offset in point_offsets], color=color,
                       edgecolor="white", linewidth=.6, s=36, zorder=3)
            ax.scatter([item["median_pct"]], [y], marker="D", color=color, s=82,
                       edgecolor="#17212b", linewidth=1, zorder=4)
            old = "PASS" if control["old"]["qualified"] else "FAIL"
            new = "PASS" if control["new"]["qualified"] else "FAIL"
            ax.text(-20.2, y + .35, f"median {item['median_pct']:+.3f}%   ·   A/A old {old} / new {new}", color=color, fontsize=9.5)
        ax.set_ylim(-.55, 3.7)
        ax.set_xlim(-20.7, 10.3)
        ax.set_yticks([3, 2, 1, 0], labels, fontsize=11)
        ax.tick_params(axis="y", length=0, pad=15)
        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
        ax.grid(axis="x", color="#e5e8ed", lw=.7)
        ax.set_axisbelow(True)
        ax.set_xlabel("Elapsed-time change: corrected versus original adapter", fontsize=10, labelpad=10)
    fig.text(.075, .95, "Apple M6 · Panic compiler contract", fontsize=22, fontweight="bold", color="#17212c")
    fig.text(.075, .893, "ALL CONDITIONAL · 0/8 cells have qualified controls for both adapters", fontsize=14, fontweight="bold", color="#a43232")
    fig.text(.075, .842, "3/16 A/A qualified  ·  exact tree-owned memory change 0%  ·  harness diagnostic; no tree optimization acceptance", fontsize=11, color="#485565")
    fig.text(.075, .795, "Same native compiler / flags, tree source and frozen referee  ·  100M items per process  ·  six serial ABBA blocks", fontsize=10.5, color="#65717e")
    legend = [Line2D([0], [0], marker="o", color="none", markerfacecolor="#5d6b7c", markersize=6, label="One block"),
              Line2D([0], [0], marker="D", color="none", markerfacecolor="#5d6b7c", markersize=7, label="Median"),
              Line2D([0], [0], color="#8a96a4", lw=3, label="Observed min–max"),
              Line2D([0], [0], color="#727c89", lw=1.4, label="Original adapter reference (0%)")]
    fig.legend(handles=legend, loc="lower left", bbox_to_anchor=(.068, .105), ncol=4,
               frameon=False, fontsize=10, handlelength=2, columnspacing=2.1)
    fig.text(.075, .073, "Negative = less elapsed time. Every effect remains conditional because same-cell precision failed for at least one adapter.", fontsize=10, color="#3c4958")
    fig.text(.075, .034, "Segments show six observed block effects, not confidence intervals. Old/new A/A controls stay separate; no historical timing subtraction.", fontsize=9.5, color="#606c79")
    fig.savefig(OUT / "adapter-diagnostic.png", dpi=190, facecolor="white")
    fig.savefig(OUT / "adapter-diagnostic.svg", facecolor="white", metadata={"Date": None})
    plt.close(fig)

    lines = ["# Matched adapter diagnostic chart — all effects conditional", "",
             "![Eight-cell matched adapter diagnostic](adapter-diagnostic.png)", "",
             "**ALL CONDITIONAL: 0/8 cells qualify both adapter controls; 3/16 individual A/A controls qualify.**",
             "This measures the standalone panic compiler contract under matched source/referee/compiler conditions. It is a harness diagnostic, with no tree candidate or optimization acceptance. Tree-owned memory differs by exactly0% in every compared block.", "",
             "Circles show all six ABBA block effects, diamonds their median, and segments the observed min/max. Negative means less elapsed time for the corrected adapter. Ranges are observed extrema, not confidence intervals. No old/new A/A control pooling or historical timing subtraction is used.", "",
             "|Members|Contract|Median elapsed change|Observed block range|Old A/A|New A/A|", "|---|---|---:|---:|---|---|"]
    for cell in cells:
        item, control = matched[cell["id"]], controls[cell["id"]]
        states = ["PASS" if control[a]["qualified"] else "FAIL" for a in ("old", "new")]
        lines.append(f"|{cell['size']}|{cell['contract']}|{item['median_pct']:+.3f}%|{item['observed_min_pct']:+.3f}..{item['observed_max_pct']:+.3f}%|{states[0]}|{states[1]}|")
    lines += ["", "Every comparison window exceeds10ms; failed A/A precision causes the conditional labels. Only the old-adapter100K full-forward, full-reverse and fractional full-forward controls qualify. All eight corrected-adapter controls fail the ±1% every-block rule. Exact A/A effects and window minima are retained in chart-data.json.", "",
              "The plot script independently reconstructs all576 raw CSV rows and144 block effects (96A/A +48matched), using exact rational ratios of integer elapsed totals. It verifies raw hashes, metadata, checksums, construction fingerprints, exact owned bytes and stored effects. chart-data.json retains exact effect fractions and per-run evidence plus source/header/adapter/referee/binary/input hashes. Exact fixture semantics and native compiler flags are unchanged; only the declared panic contract differs.", "",
              "Reproduce from the repository root:", "", "```",
              "uv run --offline --with matplotlib python " + str(Path(__file__).resolve().relative_to(Path.cwd())), "```", "",
              "PNG supports embedding and SVG preserves vector shapes/selectable text. The PNG was visually inspected for eight cells, all points, labels, conditional status and legends. The five owned chart artifacts were scanned for concrete private paths and credential patterns. Frozen PLAN.json, driver.py, README.md and freeze.json are verified byte-unchanged before and after plotting. No build, test, benchmark, profile, Git or shared-memory action was performed.", "",
              "Participant /root/followup_proposal_b; inherited Codex/GPT-6 family; exact serving model, token usage and cost unknown."]
    (OUT / "CHART.md").write_text("\n".join(lines) + "\n")
    hygiene()
    assert before == {name: sha(OUT / name) for name in immutable_names}
    print("Chart complete:576 raw rows,144 effects; all8conditional;3/16AA qualified; frozen files unchanged; own public hygiene PASS")


if __name__ == "__main__":
    main()
