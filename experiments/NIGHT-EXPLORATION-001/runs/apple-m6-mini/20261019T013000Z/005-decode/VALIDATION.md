# Referee validation and fault recipes

Unchanged tests/test_decoder.py:4 test groups/build, including1820 self-test
fixtures, geometry/accounting, bad arguments and explicit PMU availability reporting.
New --extended-test:2080 fixtures/build (65 widths×2 orientations×8 counts×2 shifts).
Each uses the independent bit-at-a-time packer and exact expected IEEE bits, plus
scalar and policy checks, partial starts, zero/full ranges and canaries. All eight
release/sanitizer base/A/B/C builds pass. Original launcher tree checks are reused
only for the unchanged root tree source. No original test or benchmark was weakened.

Faults are isolated copied A sources, never root edits. Compile with the same
release includes and driver/kernel, then invoke --extended-test. Each exits2
with Decoder self-test failed. First replace the sole policy assignment
`out[0] = zbtScoreLeafScore(leaf, start);` with `out[0] = 0.0;`. Second replace
the sole policy bulk call with an early `if (count > 1) return;` followed by the
original call. Exact commands/return codes in commands.jsonl, source hashes in
fault-controls.json, logs in validation/fault-*. Source snapshots stay ignored scratch.
