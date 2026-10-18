# EXP-008 — short-range scalar fallback for bulk score decoding

Date: 2026-10-19
Status: complete on Apple M1; cross-host M6 replication prepared
Decision: PARK; no candidate adopted

## Frozen scope

This is a standalone microbenchmark of packed B+ tree score decoding. It uses no Redis
server and makes no claim about the public scalar iterator. The source baseline is
`4fd3a3fdbce5acca18ee292642a3d80a79f50362`; the B bulk helper is frozen from EXP-007.
The per-range policy is private referee code. Main source remains unchanged.

The full frozen plan, chair selection and implementation record are in
[PLAN.md](PLAN.md), [selection.md](selection.md), and
[implementation-selection.md](implementation-selection.md). Three independent
proposers predicted scalar fallbacks with cutoffs 4, 8, or 16; three isolated
implementers produced those variants. Correctness and sanitizer tests passed for all
four binaries. Compiler assembly confirms the cutoff comparison occurs once per range,
outside the inner score loop; the policy call is outlined in every variant.

## Machine result

The complete 15,360-process discovery matrix passed on an **Apple M1** with Apple clang
17, C11 `-O3 -fno-lto`, one unpinned process, and uncontrolled frequency/DVFS. A/A
precision at the declared count16 primary failed, and no candidate reached both primary
gates. No confirmation was run; all candidates remain PARKED. Results and limits are in
[RESULTS.md](RESULTS.md), with the latest measured chart embedded there.

| Variant | Scalar path | Width60 forward count16 | Width60 forward count96 | Result |
|---|---|---:|---:|---|
| A | count ≤4 | -0.58% | +0.32% | Fails ≥2% primary gains |
| B | count ≤8 | -0.87% | +0.32% | Fails ≥2% primary gains |
| C | count ≤16 | +38.06% | +0.38% | Count16 scalar path substantially slower |

Negative elapsed-time change means faster than all-bulk control. The only narrow lead is
count1 under A/B; counts4–8 show large losses when routed through scalar. The next
falsifiable test is a new count1-only policy with fresh A/A and count2+ guards. It is
not an EXP-008 threshold adjustment.

## Apple M6 mini replication

M1 data remain labeled by host and are never pooled with M6 observations. Use the
[latest-host replication guide](../REPLICATE-LATEST.md) to rebuild the frozen EXP-007
and EXP-008 candidates, capture profiles, run each full matrix into a host-specific
folder, and analyze/audit the raw files. Keep M6 as an independent machine result.
