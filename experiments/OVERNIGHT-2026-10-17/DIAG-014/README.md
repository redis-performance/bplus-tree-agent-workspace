# Predecessor workload diagnostic — robustness PARK

All 96 target and 96 predecessor rows plus one prospective binary warmup complete
serially. Every functional/fingerprint/count/memory control passes; every target
window exceeds the predeclared duration floor. The alternating-zero mixed-output
target meets the preregistered directional predecessor-effect criterion on both
seeds. The integer/no-output target does not: only one seed clears the interval bound.

This is a workload-plus-duration intervention: each target starts after either its
own workload or the other workload, in a fresh process using the same frozen binary.
Predecessor durations differ. The result does not isolate instruction mix, establish
frequency or cache state, qualify any source comparison, or repair earlier guards.
Coordinator launch gaps are retained per pair; they are not actual kernel execution
gaps. No timing rows were discarded. A fixed fresh confirmation with reversed treatment
labels and a same-predecessor placebo was specified separately before that execution.

Fresh confirmation completes another 96 target and 96 predecessor rows plus one
prospective warmup, with every invariant passing. The selected OTHER/SAME contrast
meets both fresh-seed directional bounds despite reversed labels. One of the two
same-predecessor placebo intervals fails the fixed precision bound; the other passes.
The preregistered joint confirmation criterion therefore FAILS: **robustness PARK**.
Discovery and repeated contrast evidence remain descriptive; no timing policy is
adopted and no source guard is repaired. Do not rerun this failed protocol unchanged.

[Confirmation plan](CONFIRM-PLAN.md), [confirmation raw manifest](confirm/manifest.json),
[confirmation summary](confirm/summary.json). All 384 diagnostic rows and two warmups
are retained. This extension adds no diagnostic, baseline or population count.

Local machine: Apple M1/arm64/macOS26.3, one thread per child, libc usable-size allocator.
HARNESS-006 uses Apple clang17 O3/debug symbols and frame pointers, C11, unchanged
assertions/hashing. Exact compiler command and source/binary hashes remain in the
[freeze](../HARNESS-006/freeze.json) and [manifest](manifest.json). Clock/turbo behavior,
effective QoS and within-window residency are unknown; endpoint IDs do not establish
core type or pinning. No M4 Pro numbering, frequencies or measurements are transferred.

[Plan](PLAN.md), [runner](run.py), [raw-derived summary](summary.json), [analysis](analyse.py).
Wall ns/item is primary; thread intervals and IDs are explanatory only. Six-block
Student-t intervals assume independent approximately normal block effects. There is no
portable speed headline. Source adoption NONE, EXP-004 A/PARK and EXP-005 PARK/NONE.
One additional diagnostic (22 total), no baseline or population count. Independent
reviewer startup failed; this is sequential work with unknown backend/model/token cost.
