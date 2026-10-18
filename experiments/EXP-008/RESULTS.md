# EXP-008 result: broad scalar fallback rejected; single-score path worth a new test

**Decision: PARK this experiment; production source remains unchanged.** None of the
three frozen cutoffs passes the preregistered gates. The A/A control also fails the
primary all-block ±1% precision requirement, so no fresh confirmation was run. The
results expose one narrower hypothesis for a separate experiment: scalar decode only
when `count == 1`, and retain the frozen B bulk helper for every larger range.

## Latest measured comparison

Candidate effect is `100 × (candidate / all-bulk control − 1)`; negative is faster.
The figure shows width 60, forward orientation. Results are paired medians over six
ABBA blocks; ranges are observed block ranges, not confidence intervals.

![EXP-008 short-range candidate effects](discovery/threshold-effects.svg)

| Scores | Scalar cutoff 4 | Scalar cutoff 8 | Scalar cutoff 16 |
|---:|---:|---:|---:|
| 1 | -8.79% | -8.48% | -0.14% |
| 4 | +22.81% | +24.32% | +45.50% |
| 7 | +0.15% | +25.93% | +40.16% |
| 8 | -0.15% | +28.87% | +37.45% |
| 16 (primary) | -0.58% | -0.87% | +38.06% |
| 96 (secondary) | +0.32% | +0.32% | +0.38% |

A and B use the scalar path for count 1, while C's larger policy body erases nearly
all of that gain. The count-1 result appears repeatable within this dataset: A spans
-9.19% to -8.61% and B spans -8.77% to -7.57%. That is a follow-up lead, not an
accepted policy: the candidate implementations differ in generated code size and the
result needs a one-score-only implementation with fresh A/A and broader guards.

At the declared primary count16, A and B miss the required 2% improvement; C is 38.06%
slower. At count96 all variants use bulk and sit around 0.3% slower. The count16 A/A
block effects run from -0.69% to +2.79%, failing the fixed ±1% precision gate. Only
26/160 A/A cells qualify on every-block precision; 134 remain unresolved. Candidate
A/B also have many apparent guard losses and most short-cell A/A controls are too noisy
to adjudicate. No threshold can be selected from these data under the frozen rule.

## Scope and evidence

The run used a standalone C microbenchmark for the packed B+ tree score decoder; it did
not build Redis or exercise a tree-level iterator. One process handled each member of
a serial ABBA schedule. Six blocks per cell compared baseline/baseline and baseline/
cutoff, with 129 timed batches per process and the same output materialization and
checksum. The 160 cells cover widths 0, 8, and 57–64; both orientations; and counts
1, 2, 4, 7, 8, 16, 32, and 96. Fixture identities, binary hashes, raw rows, paired
blocks, and schedule order are retained.

Host: Apple M1, 8 physical/logical cores, macOS 26.3 / Darwin 25.3.0, ARM64; Apple
clang 17.0.6.3.2; C11 `-O3 -fno-lto`, no sanitizers for timing. One unpinned process;
frequency/DVFS and within-window migration are unknown. No hardware cycle counters were
available. The CPU Performance Engineering seven-field screen classifies these quantitative
claims as drop-number quality because per-run core residency, frequency, and turbo/SMT
state are not established. Keep the plotted values as internal M1 observations only; this
is not a portable performance claim or server prediction.

Discovery completed all 15,360 child processes / 1,981,440 measured batches in 265.83s,
under its frozen 300s cap. Raw audit independently reconstructed all 30,720 raw hashes,
640 candidate/A-A cell summaries, 7,680 paired block effects and 320 fixture identities.
The baseline whole-process sample and focused count1/count4 samples are retained in
`profile-results/` and `profiling/`; setup and warmup are included, so samples identify
active code but do not attribute timed-only cost or cycles.

Correctness: all four binaries passed the existing decoder suite in release and
ASan/UBSan builds. The 1,820-case self-test and Python oracle groups passed. The frozen
B helper is byte-identical to EXP-007 B; the root source remains the original baseline.
No public iterator, tree representation, or production source was changed.

Reproduce with `python3 experiments/EXP-008/build.py`, `python3 experiments/EXP-008/build.py --sanitize`,
`python3 experiments/EXP-008/run.py --out experiments/EXP-008/discovery --budget-seconds 300`,
then `analyse.py experiments/EXP-008/discovery` and `audit.py discovery`. Do not rerun
the same schedule as confirmation: it failed its fixed gates. Any count-one-only test
must be a separately frozen experiment with a fresh A/A, count2+ guards, and its own
implementation and review record.
