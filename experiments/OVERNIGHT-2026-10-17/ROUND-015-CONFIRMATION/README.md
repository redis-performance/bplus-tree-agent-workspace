# Fresh seeds and debug build coverage — PASS

All48cells pass: three oracles × four frozen sources × native/sanitizer × debug
assertions enabled/disabled. Every oracle CHECK and unconditional serverAssert stays
active. Within each oracle, complete outputs and logical digests match across all16cells.
This is sequential fresh-seed confirmation, not independent-agent or hardware evidence.

| Oracle | Fixtures per cell | Model states | Exact results | Additional coverage |
|---|---:|---:|---:|---|
| Multi-member growth wrap | 4 | 262,188 | 24,385,302 | 262,160 resizes; 4 natural wraps |
| Colliding SCAN intervals | 2 | 20 | 326,930 | 684 calls; 128 active growth +128 active shrink |
| Same-size cleanup intervals | 2 | 10 | 119,784 | 432 SCAN calls; active64→64copy and cached-position fallback |

Exact-result totals include legal duplicate SCAN callbacks, so they may differ from
earlier seeds. Do not pool them as performance measurements. All sanitizer stderr is
empty. No new suite, diagnostic, baseline or population count. Source NONE/prior PARK
unchanged; independent review and committed provenance still pending.

PLAN.md freezes fresh seeds,48cells, fixed order and bounds. `python3
experiments/OVERNIGHT-2026-10-17/ROUND-015-CONFIRMATION/run.py` records exact commands,
flags, timestamps, stdout/stderr, source and binary hashes in manifest.json. Seed-only
patches reconstruct every new oracle from its earlier frozen input. summary.json is
recomputed from raw output; all failures from earlier fixtures remain unchanged.
