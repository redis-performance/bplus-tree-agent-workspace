# UPDATE-001 — REJECT dual-primary repacking trial; source NONE

19 October2026, Apple M6. No implementation clears the frozen100K and1M preserve
primaries. Keep all three patches. The1M direction is an exploratory lead for a
separate preregistered experiment, never a substitute primary or adoption shortlist.

| Variant |100K median|100K block range|1M median|1M block range|Outcome|
|---|---:|---:|---:|---:|---|
|A logical snapshots|+0.084%|−1.798..+1.817%|−7.705%|−8.951..−6.214%|REJECT dual primary|
|B physical memmove|+1.694%|+0.140..+2.639%|−8.765%|−12.499..−5.353%|REJECT dual primary|
|C base-preserving envelope|+1.992%|+0.191..+3.070%|−9.270%|−12.789..−6.940%|REJECT dual primary|

Negative means less elapsed time; block effects are100*(mean B/mean A−1), two
processes per side. Six fixed ABBA blocks, discovery seeds1/2/3 used twice, variants
rotated and size order alternated. No row removal or optional stopping.144 serial
processes/batches,6.913444s timed; shortest43.577ms. Counts829394/217444 operations.
Controls48processes/2.327719s:100K max1.1722%,1M1.5527%; both fail strict±1%.
100K A is unresolved near zero, not a win. B/C100K regress consistently. The1M effects
exceed these observed controls but remain exploratory, unconfirmed and guard-incomplete.
Tree-owned memory is0.31–0.50% lower in measured candidate final states. No memory gain
claim beyond these fixtures and no demonstrated >1% primary memory increase.

## Why this experiment

The public API already tries in-place updates. [Census](census.json) distinguishes
all five patterns at five sizes: all20K same-value calls stay in place; preserve
has1517/11058 exact packing failures at100K/1M, with no order failures. Initial
nearby/distant/plus-n calls fail neighbor order. [Profile](PROFILE.md) and actual
release assembly explain a bounded mechanism: avoid remove/reinsert after order
succeeds, re-encode existing packed scores and move only offset/tag arrays when the
current allocation has room. Long profiles show lookup dominates after amortization;
the early failure path cannot establish a universal steady-state improvement.

Both population steps used three sequential passes by one worker, not independent
agents. [Chair](selection.md) selected M6-UPDATE-REPACK-001 over off-primary no-op
and previously explored lookup ideas. A minimizes encoding and snapshots logical
metadata; B minimizes encoding and memmoves physical metadata; C retains the base
and conservatively expands the representable envelope. All retain standard fallback.
[Implementation selection](implementation-selection.md): NONE. No best noisy winner.

## Provenance and reproduction

Launcher metadata ../launch-manifest.json: verified Apple M6,arm64,12cores,macOS27,
Apple Clang21. Worker direct sysctl unavailable, not retried. Frequency, DVFS, actual
performance-core use, migration and PMU unavailable. Allocator/hashing/assertions
identical. C11−O3,noLTO; timing binaries never sanitized. [Freeze](comparison-freeze.json)
pins source/referee/binaries; [manifest](implementation-manifest.json) pins all patches.
Source baseline33bf7899, chairf8d2badf, candidate publicationa9e16781. Referee SHA256
and exact patch/source SHA256 are in those manifests, rather than duplicated here.

```
python3 <host-evidence>/003-update/run.py prepare
python3 <host-evidence>/003-update/run.py census
python3 <host-evidence>/003-update/run.py profile
# Publish freeze; then baseline-only calibration and fixed controls.
python3 <host-evidence>/003-update/run.py calibrate
python3 <host-evidence>/003-update/run.py qualify
# Read chair decision; prepare isolated sources; publish candidates before timing.
python3 <host-evidence>/003-update/implement.py
python3 <host-evidence>/003-update/compare.py validate
python3 <host-evidence>/003-update/compare.py discover
python3 <host-evidence>/003-update/audit.py
```

Use a new host output directory/build when replicating; never overwrite these rows.
The commands document the completed phases, not an instruction to restart them.
Longer profile extension commands are recorded in commands.jsonl/PROFILE-EXTENSION.md.
Warmup runs the operation on an exact duplicate, frees it, then reads the timed tree;
timed initial scores/layout remain unchanged. Public lookup, target calculation and
checksum work are included. Full logs/CSV rows are preserved alongside batch values.

Native/ASan-UBSan validation passes original43tests/source/build,100 pattern/size/
length checks/source, finite/signed-zero/tie/binary-length/clone oracles and private
repack metadata/headroom/exact-score/ownership oracles. Each candidate direct helper
oracle exercises74successful repacks including6reversed leaves/build. Two deliberate
faults detected. All existing checks unchanged. The private baseline-only oracle's
invalid retained pointer was detected by ASan and corrected; raw failure, source and
hashes retained in ignored scratch; see ORACLE-ERRATUM.json. Metadata dSYM finalization,
fault-result classifier and audit self-match failures are disclosed. No failed timing
schedule repeated. Git worktree creation denied once; isolated copies/builds used.

[Audit](final-audit.json) PASS:267 raw rows,36 candidate block effects,3 reconstructed
patches, source/referee/binary hashes and878 non-overlapping serial command windows.
No baseline source/header/historical referee/test/allocator/hash edits or adoption.

## M1 action and limits

Do not treat A/B/C as contenders for the shared dual-primary update target. Exact
patch/harness replication on M1 is NOT RUN. Cached published M1 branch4c48fa7e supplies
score-pattern context and matches branch counts, but uses a different warmup referee;
no timing rows are pooled or attributed across machines. The1M transient-pack lead
needs a new primary/phase declaration, exact patch/harness pin, qualified same-session
controls, held-out confirmation, all update-pattern/size/long-key and lookup/rank/
iterator/owned-memory guards, matched profile validation and independent review.
None of those missing gates is waived by these1M results. Full guard/confirmation
campaign was not run because no dual-primary contender qualified. Adversarial review
here is a sequential self-review only; exact serving model and token cost unknown.

A separate operator supplied [raw-data reconstruction](../OPERATOR-UPDATE-DISCOVERY-AUDIT.json) at 02:18 UTC: all 144 process rows and 36 block effects agree, including checksums. This is independent raw-data auditing only; it supplies no new timing, semantic review, hardware replication or adoption confirmation.
