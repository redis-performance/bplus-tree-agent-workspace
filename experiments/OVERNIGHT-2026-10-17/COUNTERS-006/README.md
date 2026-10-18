# COUNTERS-006 — capacity-policy sensitivity supported

All twelve allocator unit cells and all twelve semantic cells pass. Each semantic cell
checks 1,940 fixtures, 289,060 full model states and 86,570,560 exact-score results.
The preregistered structural prediction is supported: fixing reported capacity gives
identical physical outputs across O1/O3 and native/ASan+UBSan for each controlled policy.
The unchanged adapter reproduces the native/sanitizer difference at both optimization
levels. Changing exact capacity to 16-byte rounding also changes physical orientation
counters. No optimization, speed claim, or baseline qualification follows from this.

Native and sanitizer ambient results differ in orientation/opportunity counters for
384 fixtures. Exact versus rounded capacity differs in those counters for 40 fixtures.
Layout hashes differ more broadly because record positions themselves depend on capacity;
do not interpret every differing hash as a compaction or orientation change. The first
ambient orientation difference is n6/bytes320; the first controlled orientation difference
is n7/bytes16. Both use seed31121 and ascending insertion. A separately preregistered
trace followup can inspect these observed cases; it is exploratory, not fresh confirmation.

Controlled adapters have metadata overhead and allocate at different addresses. Their
reported payload capacities exclude this overhead and hidden libc slack. They are
diagnostic interventions, never replacements for the frozen allocator or optimization
memory guards. Equal fixture hashes are evidence scoped to this matrix, not proof of
all build/allocator invariance. All old failed predictions and raw outputs remain intact.

[Plan](PLAN.md), [commands/hashes](manifest.json), [analysis](summary.json),
[adapter](allocator.inc), [unit checks](unit.c), and preserved adapter patches.
Review is sequential after independent reviewer startup failed. Backend/model/cost
unknown. Main source and referee unchanged. EXP-004 A/PARK and EXP-005 PARK/NONE remain.

The [exploratory trace](trace/audit.json) supports the predicted compaction threshold
mechanism in both selected cases. At n6/bytes320, the last remaining native leaf reports
224 usable bytes versus338 in the sanitizer run before the check; the threshold is308.
Only the latter compacts and resets reversal. At n7/bytes16, exact capacity334 crosses
threshold300 while rounded-policy history has208 and does not. These are payload sizes
at the check, not the same allocation request with different rounding. Earlier history
already differs. All six trace cells reproduce the original per-fixture layout hashes
and pass exact semantics. This is selected-case explanation, not fresh confirmation.

The separately planned [fresh-seed confirmation](fresh/summary.json) passes all16cells:
baseline and EXP-004 A/B/C, exact/rounded capacity, native/debug and ASan/UBSan/debug.
Each covers1,980fixtures including every size0..96 and97/513,325,860modelchecks and
163,246,200exact-score results. Within each policy all eight complete outputs match.
This strengthens the tested capacity/source invariance result; confirmation is sequential,
and neither controlled allocator becomes the optimization referee. No new suite count.
