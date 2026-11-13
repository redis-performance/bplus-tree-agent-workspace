# Continuation bounds and measurement protocol

The prior experiment is sealed. Current baseline is exact upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`, with same-pin dependencies and unchanged original lookup semantics. No rejected position-arithmetic patch is included. New referee changes are a separate preparation commit, followed by correctness and fresh A/A. One hypothesis per numbered round; keep all patches and failed attempts.

## Distinct scope and budget

Investigate helper boundaries, tag/record handling and index-to-record metadata. Three independent proposals use separate lenses. Chair selects the first supported hypothesis and orders the remaining distinct tracks. Each selected hypothesis receives three isolated implementations, then serial measurement. Failure advances to the next supported distinct track, not another spelling of position arithmetic. A track with no safe supported implementation records a concrete blocker. Bound this campaign to these three tracks, at most three implementations per track, and one independent confirmation for a passing selection. No unchanged timing retries, no threshold relaxation, no source adoption without all gates.

A fresh ARM lease is bounded to90 minutes; only one measurement workload runs at a time. If the admitted work cannot finish with cleanup margin, release and record the precise remaining stage before acquiring another lease. Workstation builds, correctness and offline analysis of existing profiles are allowed; no new local performance measurement.

## Toolchains and transfer

Two independent compiler cohorts use identical source, flags except LTO, allocator, hash seed and host runtime libc. `native` uses host GCC13.3 with no LTO. `gcc15-lto` compiles with the pinned GCC15.2 Bookworm image and `-flto=auto`, then executes directly on the same host libc2.39. Record image digest, compiler/linker versions, ELF and section hashes. No Docker work runs during timings.

The primary target cohort is gcc15-lto, which tests the earlier integration inlining lead under the relevant compiler/LTO choice. The native cohort is a transfer guard: no demonstrated>1% regression. This does not recreate the Redis server, jemalloc, command workload or full production link; no standalone result is called command-level recovery. Never compare timings across cohorts as candidate effects.

## Frozen cases

All trees contain500 ascending members and distinct query/source storage. Short members remain `m:1` through `m:500`. Construction/query iteration is excluded from timing. Long256 stays inline; external384 must use external records. Added `update` repeatedly performs FindForAdd and position-preserving score changes between integer and integer+0.125, then verifies all final scores. Mutation memory is recorded after warmup so one-time capacity growth is outside the steady-state window. Original native/sanitizer suites and explicit optional-output/external-record oracles remain mandatory.

| Case | Sweeps | Operations per process | Role |
|---|---:|---:|---|
| hit | 50,000 | 25,000,000 | Primary membership/no score |
| score | 50,000 | 25,000,000 | Score output guard |
| miss | 100,000 | 50,000,000 | Negative lookup guard |
| long | 20,000 | 10,000,000 | Inline256-byte guard |
| external | 20,000 | 10,000,000 | External384-byte guard |
| update | 10,000 | 5,000,000 | Mutation/output-position guard |

Fixed warmup1000 sweeps. Each fresh cohort first runs three A/A ABBA blocks per case:72 rows/cohort. Every A/A block must be within±1%, every row≥250ms, checksums/final state/memory consistent. Failure parks that cohort without unchanged retries. No adaptive pilot.

Passing candidates run three baseline/candidate ABBA blocks per case in gcc15-lto:72 rows/variant. Require primary improvement≥2% in every block and no demonstrated>1% guard or tree-owned memory regression. A single borderline/noisy guard is unresolved, never silently waived. Select the best eligible implementation, with simpler code preferred within noise. Validate the selected implementation in the independently qualified native cohort using the same72-row comparison before confirmation. If native regresses, reject portability; do not mix its controls with gcc15-lto.

Fresh confirmation seeds29 and43 each receive their own A/A qualification and then three ABBA blocks per case, with the same limits. Matched process-scoped profiles/counters and independent adversarial review follow. Intel guards require a fresh reserved host and own A/A before acceptance. No explicit SIMD, batching, prefetch, hardcoded fixture strings or query-order shortcuts.

## Profiles and TMA

Fresh gcc15-lto baseline process-scoped cycles/instructions/branches/misses and sampled profiles cover process lifetime, including setup/warmup. Keep instrumented timings separate. Resolve libc by exact build ID; retain unknowns if not attributable. Record actual topdown command/scope and CPU affinity. CPU-wide slot labels without exclusion evidence remain exploratory. Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring are unavailable as validated baseline/candidate categories until qualified; unsupported children stay unavailable.
