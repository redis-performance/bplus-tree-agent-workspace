# DECODE-001 — count-one private range policy

Frozen 2026-10-19 01:34 UTC, before building or timing candidates. This is a
standalone score-array decoder experiment; it does not change the public iterator.
Source baseline: launch tree `77d32df82cd5da02b95c6afb6193fcf83f67223f`.
Frozen referee: `bench/decoder_bench.c`, `bench/decoder_kernel.h`,
`experiments/EXP-008/referee/kernel.c`, and EXP-007 B bulk helper as copied to
`experiments/EXP-008/referee/bulk.inc`. All variants use the same source and flags.

Prior EXP-008 focused count-one whole-process samples place PCs in the decoder
policy and caller. Generated code has an outlined policy call; the scalar path
inlines `zbtScoreLeafScore`. Those profiles include setup and warmup, so they
support a narrow test but do not assign timed-only cycle shares. The CPU
Performance Engineering MCP was consulted for microbenchmark method; the
actual release assembly and output stores must be inspected before timing.

Hypothesis: for a one-score range at width 60, the generic score accessor is
faster than the frozen B bulk helper under identical output-array/checksum
contract, while all requests of two or more scores retain the bulk path.
Primary: width 60, forward, count 1. Required second primary: width 60,
reversed, count 1. Guards: widths 0, 8, 57, 59, 60, 63, 64; both orientations;
counts 2, 4, 16, 96. A count-one seed is invariant by construction, so different
seed literals are fresh measurement sessions, not fresh input values.

The three sequential implementation passes start from identical concatenated
source snapshots. A: scalar at count one for every width. B: scalar at count one
for noncrossing widths and byte-aligned widths, bulk otherwise. C: scalar at
count one only for width 60; bulk otherwise. These are implementation/policy
alternatives for the one hypothesis, not independent agent implementations.
All must pass the 1,820-fixture release self-test, focused native and sanitizer
checks across widths/directions/counts, and codegen inspection. Retain patches.

Discovery schedule: same binary B/B A/A first, then B versus A/B/C, six serial
ABBA blocks for each cell. Seeds 81031/81041 alternate; 129 within-process
samples, 16 warmups, 8 leaves and `ceil(49152/(8*count))` rounds. Timing is
process-serial with no builds/tests/profiles overlapping. A/A qualifies only if
all six block effects lie within ±1% and windows are at least 10 ms. A candidate
must improve each primary by at least 2% in every fresh block, have no guard
block above +1% or tree-owned memory increase, then pass independent review.
Discovery can reject but cannot accept. If precision or guards fail, PARK or
REJECT as appropriate; do not repeat this schedule unchanged. One candidate
can receive fresh six-block ABBA confirmation on seeds 82037/82051 only if
discovery justifies it. Each phase is capped at 300 seconds; each child at 30
seconds; round cutoff takes precedence. Preserve all raw rows and checksums.

M6 publication and main must be checked before implementation and before timing.
An explicit matching M6 discard vetoes this trial; DNS failure is UNKNOWN.
