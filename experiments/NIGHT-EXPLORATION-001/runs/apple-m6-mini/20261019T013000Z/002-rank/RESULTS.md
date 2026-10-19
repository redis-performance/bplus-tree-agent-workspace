# M6 rank result — reject unconditional shorter-side accumulation

All three implementations slow the preregistered 100K primary in all six blocks.
Select **NONE**; retain the three patches. The 1M effects fall inside observed
same-binary variation and do not rescue the failed two-primary objective.

Comparison freeze `3102530f`; decision published `23df69a3`. Source and referee
identity: comparison-freeze.json, implementation-manifest.json and freeze.json.
Host is launcher-verified Apple M6 / macOS 27 / Apple Clang 21. Direct worker CPU
metadata unavailable; frequency, DVFS, core residency and counters unknown.

## Observed effects

Effect is100*(candidate mean ns/op / baseline mean ns/op -1) per ABBA block.
Negative means less elapsed time. Ranges are observed blocks, not confidence intervals.
All cells have six blocks, three seeds and three batches/process; no outlier deletion.

| Variant | Size | Median block effect | Observed block range | A/A maximum absolute effect |
|---|---:|---:|---:|---:|
| A | 10000 | +9.063% | +4.779 to +13.827% | 8.840% |
| A | 100000 | +3.808% | +2.733 to +4.393% | 1.886% |
| A | 1000000 | -4.002% | -6.606 to -2.091% | 7.406% |
| B | 10000 | +5.267% | -4.370 to +7.030% | 8.840% |
| B | 100000 | +3.425% | +2.856 to +10.610% | 1.886% |
| B | 1000000 | -2.551% | -4.064 to -0.920% | 7.406% |
| C | 10000 | +3.764% | -0.163 to +7.578% | 8.840% |
| C | 100000 | +3.871% | +2.829 to +4.367% | 1.886% |
| C | 1000000 | -2.148% | -3.850 to -0.648% | 7.406% |

## Batch-average costs

36 batch observations per side/cell; independent process pairing is retained in raw
rows. These are repeated-query batch averages, not individual-query latency percentiles.
Minima/medians/ranges combine the declared three seeds within this host and phase.
Throughput is derived from candidate median batch-average ns/op.

| Variant | Size | Baseline median ns/op | Candidate min / median / max ns/op | Candidate Mqueries/s |
|---|---:|---:|---:|---:|
| A | 10000 | 28.455 | 29.369 / 31.753 / 36.874 | 31.493 |
| A | 100000 | 62.674 | 63.600 / 65.249 / 66.802 | 15.326 |
| A | 1000000 | 193.240 | 178.670 / 186.130 / 196.901 | 5.373 |
| B | 10000 | 28.532 | 27.342 / 29.797 / 35.072 | 33.560 |
| B | 100000 | 63.043 | 62.804 / 65.260 / 72.693 | 15.323 |
| B | 1000000 | 192.965 | 179.987 / 187.582 / 212.412 | 5.331 |
| C | 10000 | 28.152 | 27.816 / 29.381 / 34.393 | 34.036 |
| C | 100000 | 62.664 | 63.927 / 64.954 / 67.315 | 15.396 |
| C | 1000000 | 191.934 | 181.973 / 187.340 / 200.042 | 5.338 |

| Size | Median tree-owned bytes | Observed byte range | Median bytes/member |
|---|---:|---:|---:|
| 10000 | 312304 | 310640 to 313456 | 31.2304 |
| 100000 | 2979824 | 2979056 to 2984176 | 29.7982 |
| 1000000 | 32915824 | 32892656 to 32936048 | 32.9158 |

Tree-owned bytes match baseline exactly in every compared block for every variant.
External fixture arrays and profiling allocations are excluded from that tree-owned
metric. No memory/speed trade-off was declared.

## Mechanism and evidence limits

The M6 public self-profile locates rank accumulation; the release compiler already
uses NEON. The untimed policy census reduces mean logical summands from27.823 to
12.890 at100K and37.418 to17.576 at1M. Parent/current subtree invariants pass during
that census. These counts are logical terms, not observed memory loads or cycles.
Rank code sizes are1772bytes baseline and1960/1984/1852bytes forA/B/C. More decisions,
metadata reads and code may outweigh fewer terms; that is a hypothesis, not a measured
branch/cache explanation. No selected-candidate time profile or hardware counters.

The screen completes216serialprocesses/648batches in32.629seconds of timed windows;
A/A is72processes/216batches in10.535seconds. All3A/A cells fail±1%. Native and
ASan/UBSan upstream43tests/build pass all3variants, plus38targetedchecks each.
Baseline referee138checks and a detected rank fault pass. See final-audit.json for
raw reconstruction, patch/source/referee identity and recorded serial chronology.
CALIBRATION-LIMITATION.md discloses brief summary work during duration calibration;
there was no recorded build/test/profile overlap with A/A or candidate phases.
Unobserved outside activity is unknown. The helper include build failure and single
external profiler attachment failure are retained; no permission changes or retries.

This reduced screen rejects the declared objective; remaining rank guards, mutation
performance, all-eight-operation candidate matrix, fresh confirmation, independent
review and acceptance profile validation are NOT RUN. No adoption claim. All
proposal/implementation passes were sequential by one worker, not independent agents.
Exact serving model/token costs unknown; visible identity Codex/GPT-6family.

## M1 action and reproduction

REJECT `M6-RANK-SHORTER-001`, the unconditional min-span policy, as an M6 contender
for the shared two-primary objective. Do not replicate exactA/B/C as contenders.
Any size-limited trade-off needs a new preregistered objective/policy and qualified
controls. M1 exact patch/harness replication NOT RUN/UNKNOWN. Latest remote refresh
failed DNS and public raw fetch failed; cached published M1 revision is context only.
No cross-host sample pooling or direct M1-baseline/M6-candidate gain comparison.

From repo root use the commands in run.py, implement.py, compare.py, diagnose.py and
audit.py, with NEW frozen output/snapshot directories for a new run. Preserve this
run unchanged; its driver deliberately refuses to overwrite completed phases. Use
`python3 <this-directory>/audit.py` to reconstruct existing evidence without timing.
Profile counts reconstruct with analyse-profile.py. Full disassembly/external raw
logs remain ignored under scratch/m6-rank with checksums and generic paths.
