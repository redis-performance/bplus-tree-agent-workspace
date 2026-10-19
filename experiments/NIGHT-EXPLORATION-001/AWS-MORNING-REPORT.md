# AWS standalone B+ tree overnight report — 19 October 2026

**Campaign complete; all three OSS coordinators restored.** Live verification
passed on 19 October during 08:00:20–08:00:25 UTC (one hour later in Lisbon).
The private fleet reservation is released. Source adoption remains NONE.

SSH access was verified on the requested Intel, AMD and ARM AWS runners. Their OSS
benchmark coordinators were stopped at approximately 01:54 UTC. Work covered the
standalone packed B+ tree, compact member index, correctness oracles, profiles and
microbenchmarks. No optimization was adopted into `src/zset_btree.c` or its header.

## Baselines

All three original and corrected-adapter baseline matrices completed. Each matrix
contains 120 processes, 960 operation rows and 40 cases, preceded by seven validation
stages. The original five-host chart retains M1, M6 and all three AWS architectures.
The separate corrected-adapter chart covers M6 and AWS: 480 processes, 3,840 rows and
160 cases. A corrected M1 baseline is absent. Adapter identities remain separate.

| Corrected baseline | Qualified | Short windows | Other noisy cases |
|---|---:|---:|---:|
| M6 | 5/40 | 14/40 | 21/40 |
| Intel Sapphire Rapids | 10/40 | 11/40 | 19/40 |
| AMD Zen 5 | 11/40 | 11/40 | 18/40 |
| ARM Neoverse V2 | 21/40 | 11/40 | 8/40 |

These categories are disjoint. Unqualified observations remain in the matrices;
the matrices are not blanket precision qualification. Compiler, OS and affinity differ
between Apple and AWS, so the chart is not a causal ranking of processor architectures.

[Original five-host chart](baseline-charts/m1-m6-baseline.png) ·
[Corrected-adapter chart and provenance](corrected-adapter-charts/README.md).

## Optimization decisions

Eight measured AWS populations produced **0 accepted, 5 rejected and 3 parked**
decisions. All 24 population patches remain at immutable revisions: 21 apply to the
unchanged public tree; three ARM count-one patches target a separately documented
private decoder control. Architecture and source replications are recorded separately
and do not inflate the population count.

| Host | Measured populations | Outcomes |
|---|---:|---|
| Intel | 2 | First-match SSE2 rejected; full-member iterator cache parked |
| AMD | 4 | Lower-bound, builder-write and full-chunk variants rejected; all-match SSE2 scan parked |
| ARM | 2 | Private count-one decoder parked; corrected NEON scan rejected |

The original-adapter Intel scan replication passed primary discovery and fresh
independent confirmation, but later failed a qualified 319-byte, signed-zero trim
guard in all six blocks: **4.93% higher median elapsed time**. It is REJECT/NONE;
earlier primary gains do not override that loss. Its separate corrected-adapter
replication is PARK before candidate timing: two fresh A/A blocks in one known-guard
fixture failed precision. Corrected AMD exact-B replication failed the fixed
requirement that every primary block improve at least 2%. ARM's corrected NEON
implementations passed correctness but slowed every primary block. Losing variants
and failed controls remain available.

AMD's corrected score-only iterator profile passed review, but 100K controls failed,
so no candidate ran. ARM's separately measured native score-only baseline qualified
both sizes. Three independent proposals yielded one conditional exact historical
EXP-005 A replay recommendation and two NONE recommendations. The chair selected a
bounded replay of the exact old patch, preserving both dissents and its historical
PARK/NONE decision.

That ARM replay passed 570 validation commands: 536 correctness/fault executions and
34 preparation, build and inspection commands. All 12 primary comparison blocks
passed. Median elapsed time fell **7.77% at 100K members and 7.10% at 1M members**.
Root and independent Intel raw-data audits agree. This is a forward, score-only,
16-byte-member result on native ARM, with 50 million visits per process.
**PARK:** qualified performance guards, fresh independent confirmation and a matched
candidate profile remain missing. The static four-to-three instruction reduction
does not establish the cause of the larger elapsed-time change. No new population
or source adoption follows. ARM has two separately parked architecture replications.

[ARM primary-only chart](latest-charts/aws-arm-mask-primary.png) ·
[Raw-data audit](reviews/aws-arm-mask-screen-independent-audit.json) ·
[Decision ledger](AWS-DECISIONS.md) · [Patch index](AWS-PATCH-INDEX.md).

## Evidence and limitations

A ten-minute idle observation on each AWS runner retained 183 snapshots and 180 valid
intervals. Root and independent reviews reconstructed the counters. Those observations
describe that interval only; they do not explain earlier noise or rescue failed A/A.

Raw rows, command streams, failures, execution freezes, reviews and superseded decisions
are retained. Large raw perf files remain local with public hashes and normalized
summaries. Native serving models, measured token usage and monetary costs are unknown.

Git, the README, host branches, shared memory, activity and decision ledgers were kept
current. A reporting audit checked population and patch counts, chart summaries and
source provenance. Its material finding was corrected: the Intel README section now
leads with REJECT and labels its earlier PARK/discovery checkpoint as historical.
Original charts and raw observations remain unchanged.

[Activity log](AWS-ACTIVITY.md) · [Worker publications](AWS-WORKERS.md) ·
[Idle observation](ambient-observation/README.md).

## Apple repository status

M6 publication `fc7350a91` records the 07:15 UTC experimental cutoff and no queued
native workload. Its corrected NEON replication is PARK before candidate timing after
two 1M fresh-control failures. M1 publications `d41738b05` and `2baeafcef` resolve the
earlier publication/DNS failures and record receipt of M6's decision at 06:50 UTC,
with no further source experiment queued. Apple decisions and population counts remain
separate from AWS. These are repository observations; this campaign did not control
the Apple runners.

## Next measurement

The ARM historical mask replay is a scoped lead for a future authorized runner window.
Before acceptance it needs the preregistered mixed-output, no-output, reverse,
encoding/length and shared-decoder operation guards, fresh independent confirmation,
a matched candidate profile and final adversarial review. Preserve the exact source,
referee, compiler, allocator and machine identity; qualify controls for the new session.
A failed guard or unresolved precision remains decisive. The other rejected variants
retain their decisions. No additional benchmark phase was started after 07:15 UTC.

## Verified fleet handback

Independent host timers stopped the owned slices and restarted OSS. Live read-only
checks during **08:00:20–08:00:25 UTC** verified every coordinator RUNNING with a live PID,
fresh release files and saved RUNNING status matching that PID. All owned slices were
inactive, with zero active owned units, zero recursive cgroup processes and no
inspection errors. Release markers identify attempt start, not exact completion.

| Host | Live coordinator PID | Owned processes | Release verified |
|---|---:|---:|---|
| Intel | 2618300 | 0 | Yes |
| AMD | 625187 | 0 | Yes |
| ARM | 2916205 | 0 | Yes |

The private fleet reservation was marked RELEASED and pushed. The campaign's local
status publisher was stopped after its final reporting work; host release timers and
their recorded outcomes are retained. Unrelated workloads were left untouched.

[Live release proof](reviews/aws-release-final.json) ·
[Pre-handback inspection](reviews/aws-prehandback-0733.json) ·
[Final reporting reviews](reviews/aws-final-reporting-review-resolution.json).
