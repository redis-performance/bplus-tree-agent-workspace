# HARNESS-007 — validated public batch lookup referee

[Attempt002](attempt-002/PLAN.md) passes540fixture cells in each native/ASan-UBSan
build (1,080total),14invalid-input checks, and three deliberate reporting faults.
Independent Python reconstructs the PRNG query/construct orders, fingerprints,
partial-batch counts, exact hits and checksum. All source/support/inherited referee
files retain parent hashes. New code is an additional isolated benchmark, not a
change to root bench/microbench.c or data structure source.

[First failure](VALIDATION-FAILURE.md) is retained: a one-operation case reported
zero wall ticks but a fabricated rate from a1nsfallback. Attempt002 adds elapsed_zero
and reports rate0 as unavailable for such rows. Semantic assertions and positive
arithmetic checks remain; later A/A requires every measured window>=10ms.
The initial manifest's running status means the validator stopped, not an active child.

The fixture builds shuffled binary members and independently permuted queries, checks
all values, warms matching batch/layout operations, then times exactly requested lanes.
It reports API calls separately and handles a final partial batch without rounding.
Timed work includes assembling batch input, exact mask checking and score checksum
consumption. Steady-state memory equality excludes migration; natural active transitions
are covered separately by BOUNDARY-025 and are not what this benchmark times.

[Freeze](attempt-002/freeze.json), [validation](attempt-002/validation.json),
[patch](attempt-002/harness.patch), [faults](attempt-002/faults/summary.json).
Decision: seventh validated harness revision, A/A qualification pendingAA-012.
Source NONE; existing performance PARK and all acceptance gates unchanged.
