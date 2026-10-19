# EXP-009 harness precheck C

Status: **source-copy precheck PASS; launch review PENDING driver and exact profile/calibration contract**. Preparation only; source selection NONE. No build, native execution, timing, profiling or new disassembly. This review does not authorize launch.

Reviewer `/root/followup_proposal_c`, Codex/GPT-6 family; exact serving variant/token/currency cost unknown. Prior006 C author disclosed. Root is sole launcher/publisher. Reviewed main7b4d2153b plan and the current preparation worktree files. Remote ARM work is a separate host and is not evidence for M6.

## Copies and semantics

Independently read old pinned85afa6c7b798130452ca9dbd63082337e8bd78b7 Git blobs and checked every origin/current hash. `harness/lookup.c` differs from006-followup/referees/lookup.c only by its sampler include path. `sampler-calibration.c` similarly changes only the include path; `sampler.h` and004 physical-oracle.c are byte-identical. No production C/H/referee weakening is present in these four copies.

The lookup frontend creates unique fixed-endian binary keys with embedded NULs, seeds SipHash and insertion/query permutations deterministically, uses public `zbtreeScore` with a non-NULL score output, and preserves requested operation count/units for hit/miss/mixed. Setup, hash seeding, fixed warmup, expected-checksum construction and exhaustive public hit/miss verification are outside elapsed timing. All-hit checksums sum returned integer-ID scores; all-miss checksum is zero; mixed hit/miss verifies every timed return and score. The final full hit/miss sweep verifies all members and retained tree length, not only the aggregate. Tree-owned bytes are reported after lookup and must match per seed, not across unrelated seeds. This frontend does not exercise NULL-score output, reversed/wide-score throughput or arbitrary finite-bit scores; those remain future guard obligations before candidate code/acceptance.

Physical oracle coverage remains unchanged: widths0..64, 16 counts1..8/19..96, shifts0/3where permitted, both orientations, signed-zero width0, colliding tags, exact score bits and logical positions, all four optional-output combinations. It is source-included: link no second tree C. It is not a full public mutation/ownership model or performance guard. Missing-output sentinel/all-shift/all-count and reversed/wide finite throughput gaps from preparation-C remain.

The sampler is explicitly macOS AArch64 self-process, lock-free atomic buffer, single thread, ITIMER_PROF/SIGPROF. It rejects an already armed timer, blocks delivery around start/stop/reset, stores interrupted PCs only while active, disables timer before symbolization, caps65536 entries and fails on overflow. Its min sample sufficiency and scope attribution must be checked externally. SIGPROF sampling provides PC locations, not cycles, unbiased time shares, frequency or core-residency proof. `dladdr` names alone are not exact extents; offline mapping must conserve all observations, actual Mach-O __text/stubs, aliases and unknowns as in020. Raw absolute PCs stay private; public summaries use image-relative offsets.

Initial sampler control `sampler_probe(200000000)` computes a volatile uint64 affine recurrence. Independent pure-Python affine composition modulo2^64 establishes exact expected result **1128443088728658433**. Driver must validate this stdout and an adequate number of mapped PCs in the actual `sampler_probe` extent; a nonzero header total can otherwise pass a broken scope. This calculation did not execute the C probe.

## Exact frozen contract to resolve before final launch PASS

README freezes two successful-score-lookup primaries (100K AND1M,16-byte keys), six ABBA blocks, discovery1/2/3 repeated, confirmation501/502/503 repeated, every-block ≥2% gains, every-block A/A±1%, minimum10ms windows, fixed baseline-calibrated counts targeting600ms with100M cap, no retries/count retune/exclusions, corrected adapter and full101-cell guard floor. Missing/noisy guards remain unresolved. Historical004/006 timings and controls never transfer across the corrected adapter.

README does not yet state the exact calibration observation count, initial count, estimator/rounding and whether counts are per-size or per-seed; profile fixture cases/seeds/counts, PROFILE_USEC and minimum/on-target PCs; sampler initial-control minimum attribution; and whether the600s qualification cap spans calibration+profile+AA or just AA. These must be explicitly frozen before launch (driver plus published detailed plan or clarified README), with an overall90min deadline and phase-specific bounds. A cap-limited count that cannot qualify10ms must remain short/PARK. Profile sufficiency cannot be fixed by a rerun after seeing results.

Driver review will check: exact expected CSV schema/single row, case/size/seed/memberbytes/warmup/requested/actualops/checksum/memory, positive integer elapsed, displayed rate consistency without using rounded ns/op for gates; fixed six-block serial ABBA/seed and size rotation; count source and target arithmetic; exclusive/write-once logs and output directories; pre/post immutable source/referee/binary hashes; published ACK and deadline pinning; deterministic ENV; timeout stdout/stderr retention; owned session/group TERM/KILL/reap+empty-group observation; interrupt cleanup with deadline watchdog; post-derive/serialization budget checks and incomplete release-safe status. Initial sampler controls and profiler mapping must fail closed. Every execution/failure command belongs in the retained ledger; no hidden native retry.

## Input hashes

- `README.md`: `7434dbd7dc5c3eb7e11e9f832a801dd68db3236807f10b5054a602d5ad839aca`
- `baseline-identity.json`: `2ab98cd022c33ca7934e1885aea1aa1c51362a34cc4414cc55d6547f817e894b`
- `harness-origin.json`: `a94fe75852ef86ff78bf118acf8c478f12d5aafacf59f3abff6c9102de6fff75`
- `harness/lookup.c`: `7569d802357a8ca937ba8eaa668f9fe2c17652b6cd8b957d952129b6cab87cf5`
- `harness/sampler.h`: `18033d406b2bc4ff97d9c956ecf0d7081f6d1cbfb34db89ed5b94f6f09c267f1`
- `harness/sampler-calibration.c`: `b9e6fea2e0ac79f406a6341a43e83458fc2d70c94abeff9d222285e33a3fe016`
- `harness/physical-oracle.c`: `ac37c96fd1b583a6c74f8be083e3f68bff9a74989929cdc4fddcce8d8177f59a`

## Concrete-plan follow-up

Root supplied PLAN.json and host.json during review. PLAN now pins source d13b3598f6e859969c764daf9982998f87233f73 and absolute stop09:44:00.664180UTC, AA-only600s,600ms target/10msminimum/100Mcap, three200K calibration rows/size, two10M-hit profiles(seed1,100K/1M), minimum25 and two sampler controls. Root clarified fastest equal-ops observation with integer ceiling, no remeasure; PROFILE_USEC1000 and uncapped profile PC counts; both initial controls require exact1128443088728658433 and at least25 PCs, every PC inside the real sampler_probe extent. All other own-image unknowns remain explicit bins. These resolutions are sound predeclared prerequisites. Fixed sampler/profile ENV, overflow rules, checksum and phase bounds still need to be literal in the frozen driver/ACK detailed contract before final launch review.

Sampler scope boundary note: all-PC-in-probe is a deliberately strict initial-control gate. A boundary PC elsewhere is a retained failed control, not authority to exclude that PC or rerun. Other profiled lookup captures may legitimately include imports/unknowns; conservation applies without an on-probe requirement there. Profile failure must block source proposals alongside A/A failure; it cannot become a posthoc sample-cost explanation.
- `PLAN.json`: `4bb978e9c6f5ecec94b2796752a89e786066c44301bb8cc5d909ad117d7ac764`
- `host.json`: `46af81ff108e1b1f881daf65cb25110ab4e9a10af30a1764a23a7221a38d1560`
