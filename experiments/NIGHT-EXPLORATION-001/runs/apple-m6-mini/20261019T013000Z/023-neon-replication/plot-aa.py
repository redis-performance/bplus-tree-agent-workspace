#!/usr/bin/env python3
"""Plot all fixed M6 baseline controls. There are no candidate timing rows."""
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

P = Path(__file__).resolve().parent
s = json.loads((P / "aa/summary.json").read_text())
audit = json.loads((P / "aa/independent-audit.json").read_text())
assert audit["status"] == "PASS" and len(s["rows"]) == 48 and len(s["blocks"]) == 12
fig, axes = plt.subplots(1, 2, figsize=(12, 5.7), sharey=True)
panels = []
for ax, size, name in zip(axes, [100000, 1000000], ["100K", "1M"]):
    rows = [r for r in s["rows"] if r["size"] == size]
    blocks = [b for b in s["blocks"] if b["size"] == size]
    assert len(rows) == 24 and len(blocks) == 6
    assert all(r["window_qualified"] for r in rows)
    for i, b in enumerate(blocks):
        q = rows[i * 4:i * 4 + 4]
        aa, bb = q[0]["elapsed_ns"] + q[3]["elapsed_ns"], q[1]["elapsed_ns"] + q[2]["elapsed_ns"]
        assert b["aa_qualified"] == (abs(bb - aa) * 100 <= aa)
        assert abs(b["effect_percent"] - 100 * (bb - aa) / aa) < 1e-12
    good = sum(b["aa_qualified"] for b in blocks)
    minimum_ms = min(r["elapsed_ns"] for r in rows) / 1e6
    maximum_ms = max(r["elapsed_ns"] for r in rows) / 1e6
    ax.axhspan(-1, 1, color="#e5f1e9", zorder=0)
    ax.axhline(0, color="#7c8790", linewidth=.8)
    for line in [-1, 1]: ax.axhline(line, color="#648574", linewidth=1, linestyle="--")
    for i, b in enumerate(blocks):
        y = b["effect_percent"]
        ax.scatter(i + 1, y, color="#2563a6" if b["aa_qualified"] else "#be3d3d", s=64, zorder=3)
        ax.annotate(f"{y:+.3f}%", (i + 1, y), xytext=(0, 10 if y >= 0 else -17),
                    textcoords="offset points", ha="center", fontsize=9)
    ax.set_title(f"{name} · {good}/6 controls qualify", loc="left", weight="bold", fontsize=13)
    ax.set_xticks(range(1, 7))
    ax.set_xlabel("Fixed ABBA block (seeds 401 / 402 / 403 twice)")
    ax.set_xlim(.5, 6.5)
    ax.set_ylim(-2.15, 2.15)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=.15)
    ax.text(.02, .94, f"All windows {minimum_ms:.1f}–{maximum_ms:.1f} ms", transform=ax.transAxes, fontsize=10, va="top")
    panels.append(dict(size=size, qualified_blocks=good, total_blocks=6, minimum_ms=minimum_ms,
                       maximum_ms=maximum_ms, effects_percent=[b["effect_percent"] for b in blocks]))
axes[0].set_ylabel("Same-binary A/A elapsed difference (%)")
fig.suptitle("Apple M6 · fresh SCAN controls", x=.045, y=.98, ha="left", fontsize=20, weight="bold")
fig.text(.045, .885, "Comparison blocked · PARK / source NONE", fontsize=14, color="#a13232", weight="bold")
fig.text(.045, .835, "48 baseline processes · 5M requested operations · 16-byte members · no candidate comparison", fontsize=11)
fig.text(.045, .035, "Every block must stay within ±1%; every window must reach 10 ms. 1M fails two controls.\n"
         "All rows retained and independently audited. No retry, count change or NEON speed claim.", fontsize=10)
fig.tight_layout(rect=(.015, .13, .995, .79))
for ext in ["png", "svg"]: fig.savefig(P / f"aa-controls.{ext}", dpi=160, facecolor="white")
(P / "aa-controls.json").write_text(json.dumps({"decision": "PARK / NONE; no candidate timing",
    "summary_sha256": hashlib.sha256((P / "aa/summary.json").read_bytes()).hexdigest(),
    "audit_sha256": hashlib.sha256((P / "aa/independent-audit.json").read_bytes()).hexdigest(),
    "panels": panels}, indent=2) + "\n")
print("Plotted every control: 100K 6/6, 1M 4/6; no candidate data")
