# EXP-006 coverage for morning review

Source adoption NONE; C/PARK is a performance decision. This inventory separates
recorded candidate correctness from baseline/EXP-004 coverage. A passing corpus does
not establish freedom from all defects. Exact snapshots and run matrices are in the
linked manifests; no old test is represented as rerun this round.

| Coverage | Candidate sources | Evidence |
|---|---|---|
| Original43 tests, raw-query guard pages, exact tag-position oracle, batch fixture grid | control/A/B/C, native andASan/UBSan | [EXP-006 validation](../EXP-006/validation.json), round18 |
| Protected tag spans on both page boundaries, lengths0..128 | control/A/B/C, native andASan/UBSan | [tag guard](../EXP-006/tag-guard/manifest.json), round18 |
| Heterogeneous lengths/binary prefixes, duplicate/aliased lanes, counts0..16, score changes/deletion/reinsert/clone | control/A/B/C, two discovery and two fresh debug-off seeds, native andASan/UBSan | [BOUNDARY-026](BOUNDARY-026/README.md), round19 |
| Last-lane promotion, original18 count/layout cases, external score transfer and liveSCAN | control/A/B/C, fresh92503/92521, native andASan/UBSan | [cross-boundary](../EXP-006/cross-boundary-round020/manifest.json), round20 |
| Natural widening then ID compaction/narrowing with4096 continuous anchors | control/A/B/C, same two seeds/builds | Same round20 matrix |
| Active mixed-width clone, full relocation, partial-decline relocation with external members | control/A/B/C, all three modes and same two seeds/builds | Same round20 matrix |
| Natural growth generation wrap with new batch leaves | control/A/B/C, fresh94503/94521 × batch2/13, native andASan/UBSan, debug enabled | [generation wrap](../EXP-006/generation-wrap-round020/README.md), round20 |
| Forced scalar fallback first-match/page bounds; unchanged surrounding preprocessed program | control/A/B/C, native andASan/UBSan, host stillM1 | [fallback](../EXP-006/scalar-fallback-round020/manifest.json), round20 |
| Dense short-leaf hits plus original promotion family | control/C only, fresh93503/93521, native andASan/UBSan | [dense results](../EXP-006/dense-promotion-round020/README.md), round20 |

Five transferred faults are detected on C: promotion stale table/UAF, last-hit omission,
outside-count write, stale compacted leaf ID and shallow external clone. A sixth
forced-scalar zero-span read is detected at a protected page. These are deliberately
modified test snapshots and repeated fault families, not six production bugs or new
optimization variants. The original C patch remains unchanged.

Remaining gaps include actual big-endian/other-architecture execution, independent
review, committed provenance, and running every older boundary family on EXP-006.
In particular, earlier same-size cleanup and several packed mutation suites used
baseline/EXP-004 sources; this table does not transfer their
candidate coverage to EXP-006 by inference. A/B are not included in the dense extension.
Whole-corpus random stateful fuzzing is not claimed. Other compiler/allocator evidence
must be measured and tested explicitly; no cross-machine timing transfer.

Performance remains separately blocked: the long-key uncertainty gate and concerning
single-lane screening behavior are not repaired by semantic checks. Round19's prefetch
intervention and A/A qualification failed their fixed criteria. Keep all raw rows,
original guards and fifteen patches. No unchanged timing retry or source adoption.

Counts stay7 harnesses,13 baselines,34 diagnostics,26 named boundary suites,
5sequential populations;0accepted/2rejected/3parked. These extensions reuse existing
oracle families or add EXP-006 regression validation; they are not extra named suites.
