# M6 DECODE-001 — reject universal policies; retain count-one lead

Decision **REJECT / source NONE**, 2026-10-19T03:04:04.162366+00:00. All three frozen policies fail required
guards. B/C retain a roughly30% count-one exploratory lead; neither is an adoption
shortlist or eligible winner. No production source or public iterator changed.

Hypothesis **M6-DECODE-COUNT1-001** used the original scalar decoder only at count1
and byte-identical EXP-007 B for every other range. Both population steps were three
sequential passes by one Codex worker, not independent agents. Exact backend/model
and token/currency cost unknown; visible identity GPT-6 family.

## Fixed comparison

Effects are100×(candidate/control−1), negative means less batch-average ns/score.
Primary width60/forward/count1; all176 width/orientation/count cells retained.
Six process-level ABBA blocks, seeds1/2/3/1/2/3, fixed baseline-calibrated counts.

| Candidate | Primary median | Six-block range | Uncapped qualified guard losses (any block) | Guard losses in all six blocks |
|---|---:|---:|---:|---:|
| A | -16.914% | -20.263..-0.192% | 21 | 8 |
| B | -29.952% | -34.328..-27.469% | 24 | 9 |
| C | -30.160% | -36.649..-21.475% | 22 | 10 |


The last two columns count guards with numerically qualified same-cell A/A and
exclude the41 calibration-cap cells. Repeated loss examples:

- A: width58, reversed1, count4: +4.059..+4.993% in all six blocks, median+4.519%.
- B: width57, reversed1, count4: +5.422..+6.418% in all six blocks, median+5.920%.
- C: width8, reversed1, count4: +5.103..+10.337% in all six blocks, median+7.877%.

Thus the guard rejection is supported by repeated observations in qualified,
uncapped controls, beyond unresolved noise elsewhere. A also misses the primary
all-block2% gate: its first block is−0.192%, retained without exclusion. B/C pass
the primary elapsed-time magnitude gate, but the primary A/A fails:−6.331..+1.195%.
Only53/176 controls numerically qualify; shortest control window11.162ms.
41 cells cannot reach the50ms target below100million scores; no fine precision
claim from those cells. All per-run rows, minima/medians/ranges and paired effects
remain in calibration.json and comparison-aa/A/B/C.json with raw CSV hashes.
Count-one inputs have zero deltas and are seed-invariant; this is one input geometry
per cell, not new input diversity. There are no individual-latency percentiles.

## Mechanism and validation

Primary baseline profile28 PCs is sufficient for region identification, with18
in the policy and10 in decoder_batch. Three guard captures have17/6/9 PCs and
remain insufficient without rerun. Self-process sampling uses public macOS APIs
and is separate from timing; no PMU/cycle/cache/core-frequency inference. Candidate
profile validation was not run because every policy fails guards.

Actual release codegen: A retains the per-leaf policy call; B/C inline the scalar
branch and call bulk for other counts. B/C caller disassemblies match after callee
symbol rename, but their bulk loops differ (flag-setting/conditional branches and
register choices). Do not claim full binary equality or rank B versus C by their
small observed median difference. Caller+policy/helper text sizes: control1448,
A1620, B/C1632 bytes. These are static inspected ARM64 function sizes, not executed
instruction/cycle counts. Successive A/B/C phases can include phase drift; variant
order was not rotated across phases. This is a protocol limitation, not qualified
implementation ranking. Cell order was rotated/reversed within every phase.

All four sources pass unchanged tests/test_decoder.py in release and ASan/UBSan,
plus2080 extended geometries per build covering widths0..64, both orientations,
all required counts, min/max shifts, partial/empty ranges, exact finite/signed-zero
bits and output canaries. Original tree tests reuse the launcher's unchanged source
validation; no public API integration was introduced. Two deliberate policy faults
are detected; see VALIDATION.md. Matched leaf bytes agree across every phase;
this private fixture is not a new whole-tree memory benchmark.

## Audit and provenance

Raw/source/referee/patch checks pass with one recorded precomparison document
change: SELECTION.md and selection.md collide on this filesystem. The direction
note at80177d1e was superseded by the chair note at e62f839d before candidates or
comparisons. Original broad referee manifest and initial audit failure are retained;
audit.json verifies both historical blobs and all executable hashes. No check of
source/referee correctness was weakened. Audit reconstructs17424 calibration/control/
candidate rows,4224 effects,3 patches and17467 serial command windows. No overlap.
Last experimental child ended2026-10-19T03:00:37.811992+00:00.

[Source/referee/patch/binary identities](comparison-freeze.json), [audit](audit.json),
[profile](PROFILE.md), [plan](PLAN.md), [review](REVIEW.md). Exact source baseline
hashes in../launch-manifest.json remain unchanged. Launcher-verified Apple M6;
Apple clang21.0.0, C11−O3−fno-lto, identical allocator/assertions/frame-pointer policy.
Direct sysctl was unavailable and not retried. Frequency/DVFS/core residency,
migration and PMU observations remain unknown. All numbers are internal host-scoped
measurements. Cached M1 branch4c48fa7e has no exact candidate replication; no pooling.

Published: referee80177d1e; chair e62f839d; candidate freeze6e9e4ec8; calibration
7c671a8b; controls b0aee748; A87c3305f8; B9df7bb2e9; C4a884419d. Per-phase manifests
retain acknowledged publication pins. Coordinator alone writes Git.

## Reproduce and next action

Historical commands from repository root use E equal to this directory:
`python3 "$E/run.py" prepare`, `candidates`, `calibrate`, then `compare base`,
`compare A`, `compare B`, `compare C`. They ran serially with publication barriers
and no build/test/profile overlap. The archived runner intentionally stops new
children at03:06:30UTC this round; a future campaign must preregister new deadlines
and output directories, not overwrite these rows. `PYTHONDONTWRITEBYTECODE=1 python3
"$E/audit.py"` rechecks retained evidence on this host with preserved ignored builds.
For independent reproduction, start at6e9e4ec8, rebuild all four isolated copies with
run.py, retain source/referee hashes and pin new binaries and host metadata.

M1 action: **REJECT these exact universal policies**, skip their eligible-winner
replication. Count-one scalar caller dispatch remains an exploratory mechanism
lead for a distinct future caller design that preserves larger-range guards.
No fresh confirmation, independent timing confirmation or independent adversarial
review was run. Adoption would require new qualified controls, cap resolution,
sufficient baseline/candidate guard profiles, all guards, held-out confirmation
and independent review. No unchanged schedule retries or second optional target.
