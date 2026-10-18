# DIAG-009 — delivery-rate equivalence hypothesis not supported

All18 fixed known-function runs pass checksum, sample-count, overflow and symbol
calibration controls. The1000us/3001us requested intervals do not meet the predeclared
similar-delivery-rate bound. The17011us request meets its lower-rate bound, but both
conditions were required, so the overall hypothesis is unsupported. No rows filtered,
threshold changed or further observations added after seeing the outcome.

This is useful calibration evidence: requested timer values must not be substituted
for observed delivery rates, and the two earlier request values cannot be assumed to
produce equal rates. Aggregate sample counts per bracketed thread time are not exact
interarrival intervals, a kernel tick measurement, CPU GHz, independent sample draws
or evidence of unbiased profile shares. Counts include delivery/coalescing/boundary
limitations; frequency/effective QoS/residency remain unknown. Prior source decisions
stay NONE, lookup qualification PARK; no timing or profile fraction is promoted.

The isolated snapshot also resolves DIAG-006's archival calibrate.c interface mismatch:
stop and dump are separate, and dump follows wall/thread endpoints. The original frozen
snapshots were not edited. Small calibration smoke passes release and ASan/UBSan with
sampler on/off; measured calibration uses release only. Atomic import check and binary/
dSYM UUID output retained. Handler unchanged, with no clock or library call added.
Installed SDK sigaction does not list clock_gettime as async-safe; no handler timestamp
method was adopted. This limitation is evidence, not an attempted denied operation.

[Plan](PLAN.md), [summary](SUMMARY.md), [all measured data](summary.json), [commands/raw
hashes](manifest.json), [symbolication](symbolication.json), validation/freeze and patch
preserve evidence. Raw PC dumps and full symbols remain ignored scratch. CPU MCP evidence
checker consulted. No independent agent ran; exact backend/model/cost unknown.12 additional
diagnostics total. Next work should use the corrected helper interface while preserving
these sampling limitations; do not rerun the unsupported rate-equivalence schedule.
