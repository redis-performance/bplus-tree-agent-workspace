# Corrected Intel exact-B replication: guard-first plan

**Prepared for coordinator review; nothing is authorized to launch by this document.** No candidate source or runner workload has been created. This is an architecture/source-identity replication of the exact retained SSE2 B patch, not another implementation population or a repair of the rejected source. The original-adapter replication remains REJECT/NONE, with no A fallback.

## Question and fixed inputs

Does exact B retain a primary SCAN benefit against the corrected baseline while passing the known qualified small-leaf regression guard? The corrected baseline profile shows material all-match work (368/1315 and478/1740 captured text samples), and its fresh 48-row A/A qualifies both primary sizes. Those observations justify a bounded question, not a positive prediction. The seven-member signed-zero guard is a strong known negative result. The adapter correction is not evidence that its regression disappears.

Baseline source is exactly `13e459ff8800be3f02b6b45c87dd7b0c39453fa9`. Baseline target C SHA256 is `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`; header `496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83`. Candidate is the unchanged B patch `bd93f3922c72c4f1e8776a897e80321e3380345ee4dbd37d6d62e99683f4a644`, producing target C `204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23`. Only that target C file differs. No source alternative, edited threshold, compiler switch or repair after failure.

Actual primary baseline binary remains the untouched 013 artifact, SHA256 `eee1da2c6c3202a2799eb7d71b1e281ec2faf81998800c02c7ce0a1655e84523`. All original 8fab timing binaries and the 013 source/build remain untouched. New isolated source snapshots are planned under `scratch/intel-corrected-scan-replication/{base,B}`, each with the same relative native/sanitizer and referee paths. Record actual 13e source identity and exact patch, rather than attributing a modified tree to a pristine commit.

Use Clang18.1.3, one thread pinned CPU2, unchanged malloc/compatibility adapter, assertions and hashing. Native flags are `-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3` with the same `-Isrc -Icompat -Ivendor/redis` and `-lm`; sanitizer is O1 plus address/undefined and no recovery. No LTO, architecture flags, permission changes or concurrent runner work. Candidate primary frontend/source/output paths match a reproduced baseline build. Before using candidate timing, require the reproduced baseline executable text to equal the actual 013 timing binary; differences in debug paths are reported separately. A text mismatch stops the plan, rather than changing flags or silently replacing the qualified control.

## Stage 1: bounded correctness and identity, 600 seconds

No performance decision or calibration begins until correctness passes. Build both sources using the frozen original bench/referee and reviewed supplemental referee `ec21ce601`. Retain 43 original tests per native/sanitizer build, the unchanged exhaustive `all_match_guard_oracle_v2.c`, and B's designated `ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE` native/sanitizer validation. Also run the supplemental validator unchanged for its original 90 fixture models per source, including native/sanitizer public-versus-private census parity and all retained negative controls. Private census binaries are never timed.

Add a separately recorded validation of the new guard seeds701/702/703 through the unchanged public and census executables, native and sanitizer, passes0. Independently record expected key/score model hashes using the reviewed Python formula. Assert seven members, one fully reversed leaf, zero full16 and full8 tag chunks, 319-byte long packed records, exact alternating positive/negative-zero score bits, unchanged bytes/scores/membership and matching public/census results. Baseline and B must agree within each allocator/build mode; do not compare owned-byte counts across native and sanitizer allocators.

Retain every command/result, compiler/frontend identity, source/referee/binary hash and pre/post identity. Any failure, timeout or incomplete validation stops candidate work. No test weakening, retry, recompilation with alternative flags, or replacement patch. Exact execution driver and commands will be sealed before the coordinator authorizes launch.

## Stage 2: new known-guard calibration, 60 seconds

Guard fixture is ONLY `trim`, width319, encoding2 (alternating signed zero), seeds701/702/703. This deliberately preserves the previously failing structural case while using fresh deterministic member bytes. It does not assume a different adapter cures the prior result. Fresh seed models must satisfy Stage1 before calibration.

Run baseline only. For each seed in ascending order, probe passes1,10,100,... up to10000000 until the first window reaches20ms, then retain three additional windows at that exact probe count. Preserve every probe and trial. Derive one count for all three seeds as `ceil(200000000 / min(trial_elapsed_ns / passes))`. Require count1..10000000. Freeze that count, all raw calibration rows and both complete schedules before A/A. Target200ms; qualification floor100ms. No later count, fixture, seed or duration change. Incomplete calibration or inability to meet the cap stops the plan.

## Stage 3: known-guard same-binary A/A, 120 seconds

Exactly24 serial processes: six ABBA blocks, seeds701/702/703 twice, fixed derived traversal count, baseline binary in all four positions. The new callback/referee is independently qualified; old guard A/A and primary original-bench A/A do not qualify it.

Every block must be within±1%, and every window at least100ms. Check exact callback counts, output checksum, owned bytes, structural fixture identity, source/binary hashes and CPU2/serial boundaries. **One noisy block, short window, mismatch, timeout or incomplete schedule blocks advancement.** Label unresolved noise PARK; do not retry or run B diagnostically after a failed qualification in this plan.

## Stage 4: known-guard B comparison, 120 seconds

Only after all Stage3 gates pass, run the exact24-process ABBA schedule with unchanged B in the middle two positions, same six blocks/seeds/count. Compute each effect as `(B1+B2)/(A1+A2)-1` using time per actual callback.

Require every block at most+1%, every window at least100ms, exact callback/checksum/owned-byte parity and all identities unchanged. If all six blocks exceed+1%, REJECT. If any block exceeds+1% without all-six regression, PARK. Any short/noisy/mismatched/incomplete result also stops advancement. **No failed guard can be diluted into a mean or waived because primary cases are faster. No A fallback or B revision.**

Publish the full guard result and leave the runner idle for coordinator review before any primary candidate timing, even if the guard passes. This stage cannot establish acceptance.

## Conditional later primary comparison, 300 seconds, not launch-authorized

Only after explicit coordinator review of a passing known guard, exact B may be compared to the untouched actual 013 binary. The prior 016 baseline A/A uses this exact binary, fixed5M operations, 16-byte members, sizes100K/1M and seeds401/402/403 twice, and qualifies all12 blocks. Preserve it unchanged; do not restart controls to obtain favorable data.

The proposed discovery schedule has48 processes: two sizes, six ABBA blocks per size, alternating size order by block, seeds401–403 twice. Require B at least2% faster in every primary block, useful windows, exact outputs/callbacks/owned bytes and unchanged identities. No source selection exists; only exact B is eligible. Failed primary speed, noisy data or incomplete schedule rejects or parks this replication, without another source or retry.

## Acceptance remains unavailable from these stages

Passing the known guard and primary discovery would be only a lead. All original operation/size/member-length guards, focused dense/folded/reversed and resize/boundary guards, exact memory checks, matched profile, independent fresh confirmation and adversarial review remain mandatory on this corrected source. The 24 unresolved original-source guard cells, 14 focused noisy cells and 20 supplemental noisy cells cannot be imported as corrected passes; neither can the corrected full-baseline 30 unqualified cells be ignored. The other old-source mixed 319-byte resize/signed-zero case also remains a mandatory later corrected guard.

Reserve independent primary confirmation seeds801/802/803; do not consume them in any stage here. Confirmation and remaining guard plans need separate coordinator review and frozen budgets. They must use baseline-first qualification and retain failed controls. No acceptance or upstream action is authorized by this plan.

Budget ceiling for the currently proposed correctness/known-guard stages is900 seconds (600+60+120+120), serial owned helpers only, with fail-closed progression. No new experiment after07:15UTC and no owned work after08:00UTC. Actual author `/root/aws_intel`; exact backend/model and measured token/USD costs unknown. Old-source rejection and all losing patches remain intact.
