# Additional H2 public-API guards — proposal for controller freeze

This separate referee extends guard coverage for H2-B's cached score displacement/packed node flags and H2-C's metadata-first layout. It changes neither `lookup.c` nor its original observations. The controller must review and freeze this directory and exact compiler/source/ELF identities before any performance collection. No guard timing has been collected by this worker. Native discovery eligibility alone is not acceptance, and the original failed GCC15/LTO qualification remains PARK.

## Frozen fixture and cases

All cases construct the same500 short members `m:1` through `m:500`, distinct caller-owned SDS storage, scores1 through500 and reserve/construction sequence as the original short lookup fixture. Queries use public APIs; the harness does not include the implementation C file or inspect private layout. Each process starts fresh. Initial seed17 controls SipHash; independently confirmed seeds29 and43 use their own controls if this guard set reaches confirmation.

| Case | Work in one sweep | Proposed sweeps/process | Operations/process |
|---|---|---:|---:|
| iterator | One score-only iterator walk over500 members; alternate forward/reverse each sweep | 1,000,000 | 500,000,000 returned elements |
| rank | Rank plus score for all500 caller-owned member strings; alternate rank direction each sweep | 200,000 | 100,000,000 rank queries |
| churn | Delete each member and immediately reinsert it; alternate scores integer+0.125/integer between sweeps | 20,000 | 10,000,000 delete/reinsert pairs;20,000,000 mutation API calls |

One churn pair temporarily reduces length500→499→500. Fractional values preserve total member order while exercising score encoding and count-dependent packed-array movement. The delete succeeds before the public insert-new precondition is used. Timed churn is not a bulk delete/rebuild benchmark. All measurement counts are even so direction/score phases balance and final scores return to integers. Setup and final validation are outside the timer. The timer covers only the selected guard loop, including its checksum accumulation and fixed safety/count assertions.

All measure processes execute exactly1,000 untimed warmup sweeps, validate the full tree, capture owned bytes, execute the fixed timed loop, then validate checksums, both iterator directions, every member's bytes/score/rank, absence handling and final length. Report owned bytes both immediately before and after timing. Churn's timed score/weighted sums describe the inserted input sequence; successful delete counts and the independent final-tree model validate outcomes. Verify mode additionally checks every churn absence/reinsertion transition and validates the entire tree after each sweep. It never calls the clock and accepts only1–8 sweeps.

The counts aim for multi-second windows without a pilot. Existing native short lookup/score measurements are roughly30–33ns/query and update roughly50ns/member;100M rank queries deliberately exceed the earlier25M-query windows. Iterator lacks a directly comparable measured per-element cost, so its count is500M; churn has additional deletion/insertion work beyond the existing update loop. These are planning estimates, not measured duration guarantees or lower bounds. Keep the counts fixed: any window below250ms fails qualification rather than triggering a silent count change/retry. A duration repair would require a separately registered attempt retaining the failure.

## Qualification and comparison

Run on a currently reserved fleet host, serially, with exact per-cohort compiler flags, source/dependencies, allocator, CPU affinity and immutable binaries. Record compiler/linker versions, source/referee hashes, binary hashes, case/seed/sweeps, commands, return codes, stdout/stderr and run order. Use the same generated binary for both A/A labels. Build and correctness work must finish before measurement; no concurrent build, profile or MCP work on the measurement CPU. No local timing is authorized.

1. Each architecture/compiler cohort gets its own three A/A ABBA blocks for each of the three cases:36 raw rows. Every block's absolute elapsed change must be≤1%; every row must be≥250ms. Every process must pass its model, checksums and final-tree checks. Require exact within-cohort checksum/operation consistency, identical pre-timing memory across repeated identical processes, and identical post-timing memory across repeated identical processes. Any failure parks that cohort; retain all observations and do not retry unchanged.
2. Only a qualified cohort may compare each still-eligible H2-B/C candidate against that cohort's baseline. Three ABBA blocks per case give36 rows/variant,72 rows for both. Compute each block as100×(mean(candidate elapsed)/mean(baseline elapsed)−1). Require≤1% regression in every block; no averaging away an individually failing guard. Apply the same≤1% bound independently to pre-timing and post-timing tree-owned bytes. Within each binary/case, both endpoints must reproduce across its repeated processes. Report within-process memory changes explicitly; do not assume the two endpoints equal.
3. Preserve original primary≥2%, all original guards and all other acceptance gates. These are supplemental guards with no new speed objective or tradeoff. A failed guard blocks candidate adoption. Independent confirmation must include these cases with fresh seeds and separately qualified controls; neither this preparatory correctness run nor discovery counts as confirmation.

The full per-cohort plan for both candidates is108 processes:36 A/A plus72 baseline/candidate observations. The fleet controller must check its lease and cleanup budget against that cost before launching. Profile/counter captures, if needed, are separate and never enter the timing rows.

## Scope limits

Timed cases cover500 short members with distinct ascending scores and position-preserving fractional churn. They do not provide timed coverage of external ownership, zero-width/equal scores, signed zero, defragmentation, rehash stress, large trees or all deletion patterns. Existing upstream/oracle coverage remains required, including H2-B's flag/cache invariant tests and the explicit external-record oracle. Reverse iteration exercises logical reverse traversal; it is not proof that an internal reversed-leaf representation was encountered. Correctness builds are local; fleet architecture/compiler correctness and identity checks still apply.

Churn is steady logical traffic, not a claim of invariant physical packing. Before protocol freeze, the correctness-only1/2/5/8-sweep cells showed that owned bytes evolve as leaves repack; baseline/B/C outputs match exactly within each build mode. Therefore pre/post equality is deliberately not required, while both separately reproducible endpoints retain the1% candidate/control memory guard. This is a pre-measurement design choice, not a post-result waiver. Endpoint accounting does not bound transient peak allocation; no peak-memory claim is authorized.

## TMA classification

| Category | Baseline | H2-B | H2-C |
|---|---|---|---|
| Frontend_Bound | Unavailable | Unavailable | Unavailable |
| Bad_Speculation | Unavailable | Unavailable | Unavailable |
| Backend_Bound | Unavailable | Unavailable | Unavailable |
| Retiring | Unavailable | Unavailable | Unavailable |

No guard profile or topdown collection has run. Qualified child categories are unavailable. Existing CPU-wide labels do not qualify these new workloads; checksum counts and correctness runs supply no pipeline-slot evidence.

## Provenance and consultation

Guard author: worker previously assigned independent H1 review, now explicitly assigned referee construction. This author is not an independent reviewer of this new harness. Exact model, tokens and cost are unreported. Own fresh enabled-tool discovery found no cpu-perf/library_status tools. Shared controller consultation is recorded in `../CONSULTATION.md`: actual stdio library_status/ask, server0.1.1, bundled revision `deb5a0bac467`,3/287 indexed sources and158 passages. The metadata consultation challenged count×scorewidth dependencies and cache/layout alternatives; it returned no supporting passage establishing a workload mechanism. These were the controller's calls, not this worker's. Guard choice follows the public API paths changed by the patches; it asserts no causal bottleneck. No fleet access, commit or push was performed.
