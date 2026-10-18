# AA-011 — compact fixture qualification

All 384 measured rows and one prospective warmup complete. Five of sixteen cell/seed
combinations qualify; only alternating-zero trimmed forward mask4 qualifies on BOTH
seeds. Seven other cells PARK. All semantic/checksum/rounded-count/memory/fingerprint
invariants pass. No row omitted or rerun and no threshold changed.

The original analysis accidentally retained the old n100000 fixture's literal200
traversals, falsely marking every row invalid. [Erratum](ANALYSIS-ERRATUM.md) retains
that analyser and its outputs. The separate corrected analysis applies the original
plan's ceil(20m/95) rule:210527 traversals and20000065 effective items. This is an
analysis repair, not a referee change or relaxed check.

[Corrected results](SUMMARY-CORRECTED.md),[corrected eligibility](eligible-corrected.json),
[plan](PLAN.md),[commands/raw hashes](manifest.json). Wall time remains primary;
frequency/effective QoS and within-window migration remain unknown. CPU MCP evidence
checker returned drop_number; no portable timing or speedup headline is claimed.
No optimization count changes. Qualified compact guard is additive, not a substitute
for EXP-004's unresolved original integer mixed-output guard.
