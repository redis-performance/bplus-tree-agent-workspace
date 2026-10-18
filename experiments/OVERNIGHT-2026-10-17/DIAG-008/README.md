# DIAG-008 — warmup-operation phase hypothesis supported locally

All48 processes/768 windows completed; the primary miss16 cell meets the preregistered
phase-contrast, direction and residual-phase bounds. The secondary long-key cell does
not meet the contrast criterion and does not determine the primary decision. All
semantic, memory, duration and gap controls pass. No observations removed or gates changed.

This supports a local effect of the warmup-operation bundle on early/late miss behavior.
It does not identify cache/branch/frequency mechanisms, prove stable timing, or qualify
source comparisons. Both warmups execute the same count but take different time. Source
selection NONE and lookup qualification PARK remain unchanged. A separate isolated
referee revision with miss warmup is warranted, followed by fresh preregistered A/A.

[Plan](PLAN.md), [all rows](raw/), [summary](SUMMARY.md), [full process contrasts](summary.json),
[commands/hashes](manifest.json), [analysis](analyse.py) and saved patch/freeze preserve
exact provenance. Release/ASan+UBSan validate16 smoke cells/64 windows per build using
independent partial-pass checksum/fingerprint reconstruction and both warmup modes.
Only warmup/metadata and fresh fixture seeds differ from DIAG-007. Main source/referee
unchanged. CPU MCP evidence checker consulted; metadata/clock limits remain explicit.
No independent agent ran; sequential coordinator review, backend/model/cost unknown.
