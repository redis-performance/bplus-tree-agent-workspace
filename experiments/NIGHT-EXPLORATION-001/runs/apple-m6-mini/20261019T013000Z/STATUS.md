# M6 driver campaign — rank and update rejected; lookup next

Updated 2026-10-19T02:19:16.817210+00:00. Campaign deadline **08:00 UTC / 09:00 Lisbon**;
start no experiments after **07:15 UTC**. Round 2 ends 02:31:47 UTC.
Branch `exploration/apple-m6-mini-20261019T013000Z`. Source selection **NONE**.
Baseline src/header/referee/allocator/hash/upstream tests retain launcher hashes.

| Target | Status | M1 action / evidence |
|---|---|---|
| Five-size baseline | COMPLETE | Reused baseline-attempt002; 120 processes / 960 rows. Never rerun inventory. |
| RANK-001 | REJECT / NONE | All candidates regress 100K. [Results](002-rank/RESULTS.md); skip exact candidates. |
| UPDATE-001 | REJECT / NONE | No 100K winner. [Results](003-update/RESULTS.md); all patches retained. 1M is an exploratory lead only. |
| LOOKUP-001 | NOT STARTED | Next: review EXP-006; profile independent public hit/miss paths and count tag/full comparisons. |
| Optional / confirmation | RESERVED | No dual-primary eligible contender. |

Update hypothesis **M6-UPDATE-REPACK-001**: after neighbor order checks pass but exact
packing fails, re-encode score fields inside the existing allocation, retaining
records and index. Both population steps were three sequential passes by one worker,
not independent agents. [Exact source/patch/harness/binary identity](003-update/comparison-freeze.json)
and [patch manifest](003-update/implementation-manifest.json).

| Variant | 100K median / block range | 1M median / block range | Decision |
|---|---:|---:|---|
| A logical snapshots | +0.084% / −1.798..+1.817% | −7.705% / −8.951..−6.214% | REJECT dual primary |
| B physical memmove | +1.694% / +0.140..+2.639% | −8.765% / −12.499..−5.353% | REJECT dual primary |
| C base-preserving envelope | +1.992% / +0.191..+3.070% | −9.270% / −12.789..−6.940% | REJECT dual primary |

Update calibration 75 rows, controls 48 rows, discovery 144 rows; serial processes
with one batch each. A/A maxima 1.1722% / 1.5527%, both fail ±1%. No primary relabeling,
confirmation or universal gain. Primary memory decreases 0.31–0.50% in these fixtures.
All original 43 tests per source/build and targeted native/ASan-UBSan checks pass.
Private oracle: 74 repacks/candidate/build, six reversed, plus two faults detected.
Audit PASS: 267 reconstructed rows, 36 effects, three patches, 878 serial windows.
Full candidate guards, independent review and adoption profile validation NOT RUN.

Host provenance: launcher verified Apple M6 / arm64 / 12 cores / macOS 27 / Apple
Clang 21 in launch-manifest.json. Worker sysctl denied, not retried. Frequency, DVFS,
performance-core residency, migration and PMU unknown. CPU Performance MCP absent.
Public self-sampler controls pass; sampled PCs are diagnostic, not exact time shares.
External profiler attachment failed round 1; no permissions changed or repeated attempt.

Publication: update profile/referee 33bf7899, chair f8d2badf, candidate freeze a9e16781.
Earlier round-1/referee requests timed out; coordinator resumed and published their
retained evidence. Update comparison/decision and round handoff publication pending.
Only coordinator commits/pushes. Git worktree creation denied once; isolated copies
used. Oracle baseline pointer failure and metadata/classifier/audit errors retained.

Cached published M1 branch revision 4c48fa7e inspected for context; exact M6 update
patch/harness on M1 NOT RUN. Its update referee uses different warmup, so no timing
comparison/pooling. See HANDOFF.md for exact next action. Exact serving model/token
cost unknown; visible identity Codex/GPT-6 family. No agents/independent review.

Recorded branch totals: **9 populations** (7 sequential fallback + 2 multi-agent),
**0 accepted / 4 rejected / 5 parked**, **27 patches / 12 validated harnesses**.
Concurrent M1 night population counts remain separate pending reconciliation.

A separately supplied operator audit at02:18 UTC reconstructs all144 discovery rows/36 effects and agrees with NONE. See OPERATOR-UPDATE-DISCOVERY-AUDIT.json; raw-data scope only, not independent timing/semantic adversarial review or replication.
