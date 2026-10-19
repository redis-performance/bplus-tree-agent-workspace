# EXP-009 harness precheck C

Status: **PASS — final static harness/driver/mapper/seal review for baseline prerequisites only**. Source selection NONE. No build, native execution, timing, profiling or new disassembly. Root publication, exact frozen manifests/ACKs and exclusive idle-runner release remain required before launch. Earlier pending paragraphs below are preserved review chronology; the final verdict at the end governs.

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

## Mapper final offline review

Final `profile-map.py` SHA256 `258d34b4c16b76153808b6ec3289e2f1ccc23b45472eab88d8a458b466a3576e`: PASS for bounded static mapping/probe/conservation review. A fixed initial findings before freeze: duplicate wanted labels now reject, instruction addresses must be aligned/contiguous, probe extent stays in actual text and starts at unique nm probe address without crossing another text symbol, CLI output opens exclusively. All observations (including unknown/import/alias cases and failed sufficient/scope controls) remain retained. No nearest-name probe proof.

Pure Python synthetic Mach-O/nm/otool/PC controls (no binary execution), 18 PASS: actual nm beats dladdr, aliases retained, stub unknown, outside unknown retained, unaligned unknown, external separated, good strict25 probe control, bad checksum FAIL, outside probe FAIL, short24 FAIL retains24, capped reject, non1000 interval reject, PC-count mismatch reject, duplicate probe label reject, assembly gap reject, nm anchor mismatch reject, interior symbol reject, probe beyond text reject. Temporary synthetic files removed. An initial control harness expected map_profile to raise on bad checksum; revised mapper instead intentionally returns FAIL with all observations. That offline review assertion failed, was retained in chat, and the control expectation was corrected to accept only FAIL/rejection, not PASS; no experimental data was rerun.

Reproducibility control setup failure preserved: first saved-control invocation (script SHA `625755c4508080be9b9ff8617f8418e397b2c94c22563c5d6b901cff15a17b26`) stopped with FileNotFoundError creating `scratch/exp009-C-map-*` because this new worktree had no scratch directory. Added only an explicit mkdir for synthetic control scratch; no native command was attempted.

## Final driver and seal verdict — PASS

Final reviewed driver SHA256 `2b2ae7c1c7647ba7dff21279383e8284f0fe55c94e47fdcdd2d5cafd006598b5`; mapper `258d34b4c16b76153808b6ec3289e2f1ccc23b45472eab88d8a458b466a3576e`; seal `3beae8c9f52b11c996b2f363c747f39dd5fe072be718fbf0bcd0784112b0ab79`. All source-copy/profile-calibration details are now explicit in README/PLAN/driver. Root owns execution/ACKs and B is correctly labelled driver author.

The driver scopes native C11/O3/debug/strict warnings/frame-pointer/noLTO consistently; sanitizer changes only O1/ASan+UBSan/no-recover. The physical oracle omits the separate tree translation unit. Original43 parser was checked offline against retained023 native stdout including ANSI sequences: all indices1..43 and the success summary match. Native/sanitizer semantic matrix remains36 hit/miss/mixed length cases plus8 expected-bad-CLI contracts and two original43/two physical oracles. These are planned commands, not newly executed evidence.

Calibration uses exactly three equal200K samples per size, seed1, fastest positive elapsed and integer ceiling to600ms with100M cap, without remeasurement. AA reconstructs the exact48-entry six-block ABBA schedule, seeds1/2/3 twice and alternating size order; it precomputes independent query models and parses the strict22-field CSV. Fingerprints include operations/checksum/owned bytes and all fixture parameters. Gates use integer elapsed sums and10ms minimum windows; display floats are not decisions. It completes all48 on control noise, preserving every failed block, while execution/semantic/timeout/identity failure stops intact. No candidate phase exists in this driver.

Fixed minimal environment and explicit PROFILE_USEC1000 prevent inherited sampling configuration. Strict initial controls require the exact affine checksum plus every retained PC inside the actual contiguous nm/otool-anchored probe extent, minimum25 uncapped. Lookup capture mapping checks mapped PASS, sample conservation and raw/binary/nm identities. Import stubs and unmapped own PCs stay explicit unknowns. Private absolute-PC originals remain in scratch; only relative mapping summaries publish. Timing fields from instrumented runs cannot support a speed or cost claim.

Each phase refuses existing output/raw directories and raw streams use exclusive creation. Input/derived/binary identities are checked before and after phases. A root-authorized phase/hash/plan ACK requires root and C PASS plus idle/exclusive declarations and clips the absolute stop. Parent phase watchdogs cover build600s/calibration180s/profile180s/AA600s and reserve10s; child timeout is clipped to remaining budget, cleanup uses owned session/group TERM1s/KILL/wait4s/empty-observation3s and journals stdout/stderr/hash/result even on interruption. Managed signals are blocked across Popen handle assignment and child restores the prior mask before exec; this preexec operation relies on the explicit single-thread launcher. Signals remain blocked through cleanup/journal persistence. Post-row, derivation/finalization and post-serialization checks prevent an over-budget success. This was static lifecycle inspection, not a newly executed process-kill test.

Review found and authors fixed before freeze: exact header enforcement; parent spawn-assignment interruption gap and inherited blocked-child-mask consequence; mapped result identity/conservation checks; complete raw/build evidence hashing; and final phase-status prerequisite gates. COMPLETE counts/build-manifest alone are insufficient if finalization later fails: final code checks actual COMPLETE/release-safe build status before calibration/profile and rechecks its hash afterward; seal and AA pin/check actual final build/calibration/profile statuses. Seal writes manifests exclusively and retains the full build table plus calibration/profile artifacts and raw identities. The separate publication helper statically preserves nonprofile streams byte-for-byte after phase completion and rejects obvious private paths/PC lines; root remains responsible for publication review.

Persisted reproducibility files `review/C-offline-controls.py` and `.json` report **41 passing pure-Python controls** against these exact final driver/mapper/seal hashes:18 mapper controls plus direct checksum/model/CSV malformed-input checks and actual-AA-function in-memory schedules at exact±1% boundaries, one-nanosecond-outside cases and short windows. Every simulated noise schedule executes all48 stubbed rows. No main/Owner/subprocess/native command is invoked by these controls. The two reviewer-only setup/expectation failures above remain documented; they were not experimental reruns. The saved controls now create their temporary scratch directory explicitly and remove synthetic fixture files.

No remaining blocker found for these frozen **baseline prerequisites**. Future source selection still requires actual successful profiles and all twelve qualified fresh controls, then independent proposal/chair/isolated implementations with the retained full guards, exact-bit/fault checks, held-out confirmation and adversarial review. This verdict approves no candidate or uninspected later script revision. All review activity is now stopped.

Final artifact hashes:
- `README.md`: `382337a161fdb5ee236cb1090639ef0711656972c8e0ab493673f875444faa37`
- `PLAN.json`: `8002a1513ced827ac4c68794035af1287ce365b10a8f32e4dc6ff583c840d0ed`
- `driver.py`: `2b2ae7c1c7647ba7dff21279383e8284f0fe55c94e47fdcdd2d5cafd006598b5`
- `profile-map.py`: `258d34b4c16b76153808b6ec3289e2f1ccc23b45472eab88d8a458b466a3576e`
- `seal.py`: `3beae8c9f52b11c996b2f363c747f39dd5fe072be718fbf0bcd0784112b0ab79`
- `publish-raw.py`: `f1bb850a5440f29ea8659d4dcf0bef7e1ffea2ad56f65f3f7a4355c04eee0c73`
- `review/C-offline-controls.py`: `295731b9d165c6910a3d2159c1d71555af04c5ab8afdc0731db7f8e6494f0e00`
- `review/C-offline-controls.json`: `e5d97e7de37983ed3095bae4d7380b7fd92d41cd32289faa4f3c888c5e806069`
