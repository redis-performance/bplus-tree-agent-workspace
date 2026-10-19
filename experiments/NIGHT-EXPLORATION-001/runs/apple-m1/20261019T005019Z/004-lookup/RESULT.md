# LOOKUP-001 independent-query profile — Apple M1

Decision: **COMPLETE diagnostic; proposal selection NONE; source unchanged.**
The public hit path spends sampled PCs in leaf-tag search, but the existing
EXP-006 inline scanner already explored that family and raised single-lane
regression concerns. The current evidence does not identify a new bounded
single-query hypothesis with a reason to overcome those results. No
implementation population or candidate timing was run.

## Referee and validation

The separate lookup-bench.c changes only the lookup query permutation and
hit checksum relative to the frozen microbenchmark. Construction and query
orders come from independent deterministic seed streams. Release and
ASan/UBSan hit/miss checks pass at 10K, 100K and 1M, seed 1. Referee SHA256:
7c37bb1b1fffa3dd0331179d0ae61f1cce554bc8a1f93eca389eec264a898aa2.
Baseline tree SHA256:
d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2.
Release binary SHA256:
7d6d3a64e29e9fd06689cd97a7e37e3eb10e96fb0096837e11ecf8b1089a1866.
The root referee and tree remain unchanged; the new harness commit is
pending after the earlier git index-lock denial. Its source patch, build
logs and 12 validation cells are retained.

## Public profile and code

External process sampling was denied earlier in this host run, so a copied
referee used the already validated in-process SIGPROF sampler at a 1,000
microsecond **requested** interval. The first six captures had only 10–58
PCs. One predeclared 10×-operation-count capture per cell yielded:

| Size | Hit PCs | Hit PCs in platform memchr | Miss PCs | Leading miss symbol |
|---|---:|---:|---:|---|
| 10K | 439 | 251 | 167 | siphash 88 |
| 100K | 344 | 189 | 191 | siphash 116 |
| 1M | 233 | 160 | 230 | main 109; symbol attribution limited by inlining |

The release zbtScoreLeafFindMember disassembly has calls to both memchr and
memcmp. The profile identifies code regions; signal cadence, PC sampling,
inlining and library symbol resolution do not justify exact time fractions.
profile-summary.json and profile-long-summary.json retain commands, code
symbols and raw-log hashes. Raw PC logs remain in ignored scratch.

## Untimed structural counts

A separate instrumented source copy counted index tag candidates, leaf tag
candidates and complete member comparisons during 100,000 public queries
per cell. Results below span two seeds; counts.json preserves every row.
Instrumented durations are excluded from performance evidence.

| Size | Hit full compares/query | Miss full compares/query | Hit index tag candidates/query |
|---|---:|---:|---:|
| 10K | 1.1506–1.1554 | 0.0278–0.0280 | 1.0085–1.0109 |
| 100K | 1.15217–1.15272 | 0.03344–0.03460 | 1.01414–1.01415 |
| 1M | 1.14079–1.14118 | 0.01951–0.02041 | 1.00727–1.00728 |

Misses rarely reach a full member comparison in these 16-byte fixtures.
The hit profile and code identify the existing leaf-tag scan, but counts do
not establish the cost of replacing memchr with any proposed loop. Length
guards, collision tests, batch1/16 and other sizes remain unmeasured on a
new candidate because no candidate was selected.

## Three sequential proposal passes and chair

The same worker made three **sequential** passes over the same evidence;
these were not independent agents. Model family is GPT-6 per session
instructions. Exact backend variant and measured token cost are unavailable.

| Pass | Proposal | Chair reason |
|---|---|---|
| A | Inline single-query tag scan | Profile supports looking at memchr, but EXP-006 already retained scalar/SWAR/unrolled variants with concerning single-lane regressions. Reusing them unchanged would be a control, not a new hypothesis. |
| B | Prefetch the index bucket | No memory-stall counter or profile evidence establishes a prefetch opportunity; the current query is dependent on hashing. |
| C | Strengthen miss filtering before leaf access | Only about 0.02–0.035 full comparisons per miss in these fixtures; no evidence this is the limiting path. |

Chair selection: **NONE**. No second population step, candidate comparison,
fresh confirmation, independent review or source adoption. Revisit only with
a distinct profile-supported mechanism that explains the EXP-006
single-query losses and a frozen independent-query referee with A/A.

M6 remote checks through 2026-10-19 01:26:29 UTC failed DNS resolution
for github.com. Branch, commit, decision and patch outcome are UNKNOWN;
no M6 data was used.
