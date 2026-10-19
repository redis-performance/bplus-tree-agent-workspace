# SCAN-TAGS-001 implementation decision

Decision: **PARK / NONE**. A and B are conditional leads only; both reach the preregistered2% improvement in every block at100K and1M. The fresh1M A/A failed before implementation, so there is no qualified implementation winner or adoption. Required performance guards remain unqualified/unimplemented. C fails the every-block1M gate. Fixed A/B/C priority chooses A for one bounded matched mechanism diagnostic; this does not establish A superiority over B.

| Variant | 100K median elapsed change | 1M median elapsed change | Every-block dual-primary gate |
|---|---:|---:|---|
| A | -5.255% | -4.360% | conditional pass |
| B | -4.279% | -4.297% | conditional pass |
| C | -3.790% | -2.143% | fail |

Negative means lower elapsed time. This is an unqualified exploratory AMD Zen5 result, not a general performance claim. Fixed144serial processes completed03:27:59–03:29:53UTC with36ABBA effects, six blocks per variant/size, seeds1/2/3 twice, original1Mrequested SCAN operations and16byte keys. Callback counts/duplicates are preserved and reported by the original referee. All returncodes, CPU2 placement, per-block checksums/operations/tree-owned bytes, raw reconstruction and before/after binary hashes pass. Full raw CSVs, process metadata and effects retained under screen/.

A effect ranges:100K−5.795% to−5.064%,1M−4.856% to−3.190%. B:100K−5.354% to−3.484%,1M−5.067% to−3.665%. C:100K−4.050% to−3.508%,1M−4.728% to+0.103%. The failed1M control blocks were+1.397%/−1.687%; all controls retained, no reruns or metric changes. Numerical A/B median differences do not establish superiority.

All123 validation commands passed unchanged original43 tests and exact all-match/scan interval/wide/live-widen/resize-generation oracles in native/sanitizer modes for all four sources, with source-local fallback checks. All8 deliberately injected fold/order/tail/aligned-load faults were detected. Root independent static review e47157087 found no blocker. Baseline rebuilt .text exactly matches the frozen timing binary. A/B/C generated code differs; A/B share code size but register/control layout differs, not independent mechanism confirmation.

Actual independent AMD/Intel/ARM proposal and implementation authors, root chair; immutable original commits/provenance retained. Exact inherited models and measured token/USD costs remain unknown. All losing/parked patches retained. Root independent raw audit and one matched profile remain pending at this checkpoint. No additional candidate timing/tuning; future cross-architecture evidence is separately preregistered, never carried across machines.

AMD totals:4 completed populations,0accepted,3rejected,1parked. Baseline source unchanged; sourceNONE overnight. See GUARDS.md for every missing fixture and acceptance condition.

Decision UTC: 2026-10-19T03:31:21.336887+00:00.

Matched mechanism diagnostic now complete: [report](mechanism/RESULT.md). Instructions/branches fall about12%, branch misses rise about5%, scoped cycles improve under1%; this does not validate the exploratory4–5% elapsed magnitude. PARK unchanged; no further candidate timing or sampling.
