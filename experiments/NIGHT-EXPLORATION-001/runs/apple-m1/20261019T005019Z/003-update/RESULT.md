# UPDATE-001 path decomposition — Apple M1

Decision: **COMPLETE diagnostic; candidate NONE; source unchanged.** The new
referee and untimed instrumentation distinguish the requested paths. The
position-preserving primary's same-binary A/A controls fail strict precision
at both 100K and 1M. No implementation population or candidate comparison
is justified in this round.

## Referee and validation

update-path-bench.c is a separate 16-byte-member referee. Construction and
query orders use independent deterministic permutations. Same-value,
position-preserving, nearby reorder, distant move, and original +N are named
cases. Every process checks exact score bits for every member after the run,
full iteration order/uniqueness, membership count and sampled or full public
ranks. Native 15-cell smoke and five 10K ASan/UBSan cells pass. The unchanged
source also passed upstream and signed-zero rank oracles before this work.
Referee SHA256: d2f6a7b6f3e2e64683343b5cae9a9e4d757f9eec9fa15de7d36eff428605bc56.
Native binary SHA256: 8fa7f0b5b72431ef725741d5abcb9d7b70e7b9281478f26a201889da00f9625f.
Baseline tree SHA256: d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2.
Release compiler: Apple Clang 17, C11 -O3, no LTO; sanitizer uses -O1.
No root tree or frozen rank referee was edited. Harness commit provenance is
pending after the earlier index-lock denial; the exact source and hashes are
retained.

## Untimed path counts

Separate source copies counted the result of zbtScoreUpdateInPlace for
20,000 updates, seed 1. counts.json, reasons.json and their source patches
retain the diagnostic. Each pair sums to 20,000.

| Size | Same in-place | Preserve in-place / reinsert | Nearby / distant / +N reinsert |
|---|---:|---:|---:|
| 100K | 20,000 | 18,483 / 1,517 | 20,000 each |
| 1M | 20,000 | 8,942 / 11,058 | 20,000 each |

The position-preserving fallbacks are all zbtScoreLeafPackScore failures
in the separate reason pass; no neighbor-order rejection occurred. This
explains why preserving sorted position does not always take the in-place
path. The source comment states that exact representation in the current
leaf base/shift/width is a second precondition.

## Baseline inventory and profile

inventory.json records 75 serial, independently seeded processes: all five
sizes × five cases × seeds 1/2/3, 100,000 operations each. Every raw CSV and
stderr is retained. These are descriptive batch averages with varying cache
and update histories, not paired effects or individual latency percentiles.
At 100K, observed ns/op ranges were same 107.50–253.90, preserve
121.32–275.37, nearby 457.61–738.18, distant 535.62–711.47, +N
511.33–862.34. At 1M the ranges were 372.42–380.87, 526.97–549.23,
857.50–1078.08, 808.76–1093.38 and 986.07–1033.26 in that order.
Cross-case differences include different work and are not an optimization
effect.

An in-process 1,000 microsecond **requested** SIGPROF sampler captured
44/232/258 PCs at 100K and 116/236/394 at 1M for preserve/distant/+N
respectively. profile-summary.json records symbols, commands and raw
profile hashes; raw PC logs remain in ignored scratch. At 100K distant,
_platform_memmove (46 PCs), zbtScoreInsertAt (32) and
zbtScoreLeafLowerBound (30) appeared; at 1M distant, allocator (79),
reclaim trap (54) and main (45) dominated resolved samples. Sampling
cadence, inlining and signal overhead limit attribution. Release
zbtreeUpdateScore assembly is retained. These observations support a
different update path mix, not a precise component-time estimate.

## Same-binary qualification

Three baseline calibration observations per primary cell froze operation
counts at 415,111 (100K) and 100,000 (1M). The six ABBA blocks used seeds
1/2/3 twice and 48 serial processes; all matching checksums and tree-owned
bytes agree. Raw rows, calibration, per-run hashes and analysis are in
qualification/.

| Size | A/A block effects, B relative to A | Shortest window | Strict result |
|---|---|---:|---|
| 100K | −7.11%, +0.47%, −0.73%, −1.50%, −0.26%, −2.46% | 45.009 ms | FAIL |
| 1M | −0.51%, −0.39%, −10.49%, +1.87%, +5.45%, −2.25% | 52.895 ms | FAIL |

No outlier was removed or block rerun. A/A failure prevents the required
fine-grained adoption gate. No update implementation was written; repacking
a leaf after exact-width failure would require a separately profiled and
preregistered hypothesis, ownership/memory guards, and fresh qualification.
The current target ends here and the queue advances to single lookup.

M6 check before this timing phase at 2026-10-19 01:23:28 UTC failed DNS
resolution for github.com; branch, commit, decision and patch outcome
remain UNKNOWN. No M6 data was used.
