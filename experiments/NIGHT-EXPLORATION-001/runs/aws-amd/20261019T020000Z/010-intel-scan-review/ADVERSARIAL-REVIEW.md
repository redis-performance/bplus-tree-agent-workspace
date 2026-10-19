# Adversarial review — exact Intel scan B

## Verdict: NOT YET DEFENSIBLE for adoption; declared discovery is supported

No blocking semantic defect or discovery parity failure was found. The frozen Intel screen supports a narrow scan improvement on its declared fixtures. It does not establish safe performance across the required guards, independent confirmation, or a validated explanation of the elapsed gain. Keep source **NONE**.

Reviewer: `/root/aws_amd`, one actual native agent who consulted the benchmark-adversarial-review parity/replicability checklist as a reference. This is one independently authored standalone review, not a completed multi-reviewer skill workflow or a memtier/server audit. The reviewer authored independent variant A earlier and knows the shared hypothesis; this is not a blinded review. B was independently authored by Intel. No extra reviewer panel or stronger model execution is claimed; exact inherited model and token/USD costs are unknown. Network, server, TLS, client saturation and pricing checks are inapplicable to the user’s standalone scope.

Immutable evidence reviewed: Intel discovery commit `c3e5882ca`, original-guard plans `555da4539`, B submission `89dc8721f` and exact source SHA256 `204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23`. No Intel runner was accessed. Review predates any fresh confirmation handoff.

## Semantics, ownership and portability

B changes only the all-match helper and its guarded include. `words = count / 8`; the SSE2 loop runs while `w + 1 < words` and advances by two. Therefore each 16-byte `memcpy` stays entirely inside complete tag spans. The original residual word loop resumes at the exact unconsumed word, and the byte tail still starts at `words * 8`. Count zero causes no load or output, including reversed count zero: the unsigned `last` wrap is unused.

Byte comparisons create exact masks. Query tag one combines physical bytes zero and one once by OR; other tags compare exactly. A nonzero mask is tested before `ctz`, its lowest bit is removed each iteration, and physical positions are emitted in ascending order. Reversed mapping applies `last - physical` to those same positions, preserving the original descending logical output order and every match. There is no first-match shortcut or duplicate output from folded masks.

`memcpy` supports unaligned input and avoids an alignment/aliasing promise. No stores target the tree: only the existing output positions array changes. Scores, binary member lengths, packed/external record ownership, IDs, rehash state, scan cursor progression and iterator invalidation are untouched. The portable branch retains the original word/tail behavior when SSE2 is unavailable or the designated local test macro is set. Forced fallback on x86 is not evidence of native ARM or big-endian execution.

The original 43 tests and V2 exact-output/guard-page oracle passed native and sanitizer builds on Intel; designated A/B fallback builds passed too. The immutable B also passed AMD’s extended scan interval, wide/live-widen and resize-generation suites. V2 checks 299,664 cases per invocation, including all tags, both orientations, zero spans, complete-vector misalignment, boundary-only matches and output canaries. AMD’s isolated deliberate fold/order/tail/aligned-load faults were all detected. Those fault controls used A and should not be represented as separately injected B faults. No further semantic blocker was found from source review.

## Measurement integrity

The independent audit script reconstructs all **48 A/A rows and 96 comparison rows**, producing 12 control and 24 candidate ABBA effects directly from raw CSVs. It verifies serial boundaries, CPU2 at both endpoints, the exact schedule, empty error streams, matching checksum/actual callbacks/tree-owned bytes, and source/referee/binary freezes. Effects use unrounded `elapsed_ns / operations`, preserving duplicate-emitting scan semantics; requested operations are not incorrectly used as the denominator.

Both control sizes qualify. A and B each pass the 2% gate in every primary block. B’s descriptive medians are −6.665% at 100K and −3.661% at 1M; the narrow ranges and complete rows support the stated discovery. Choosing B was a preregistered source-maintenance preference, not a claim that B is faster than A. The Intel qualification was separately frozen with five million requested operations and seeds 101–103; AMD’s failed controls are neither reused nor repaired by these rows.

The baseline binary is identical between Intel qualification and comparison. All variants use isolated snapshots, matching relative frontend/output paths and flags, unchanged allocator/assertions/hash, and the original timing referee. No profile executable is substituted. Raw evidence and the audit are in [independent-raw-audit.json](independent-raw-audit.json).

## Required evidence and guard gaps

- **Original guards:** the current 80-cell plan covers all eight operations, five sizes and 16/128-byte members. It correctly retains its 12 calibration windows below 10 ms as qualification gaps. A passing subset cannot become universal acceptance. Await the complete fixed A/A outcome; do not extend the phase, drop cells or switch to A after a B guard failure.
- **Length boundaries:** 128-byte members do not cover the separately required 8/319/320/321/1024-byte boundaries. Those fixtures, including external records, still need frozen controls and comparison. The discovered 16-byte scan behavior cannot substitute for them.
- **Focused scan behavior:** require real-hash dense ordinary-tag and folded-zero/one fixtures, partial/full vector tails, physically reversed leaves, tied/signed-zero layouts, and active resize/migration states. Record actual fixture/tag/reversed-state census, callback multiset/count and unchanged memory. Do not infer a reversed leaf from insertion order or manufacture hash output. New referee files need baseline correctness and A/A qualification before candidate measurements.
- **Independent confirmation:** seeds 201–203 remain untouched at this review checkpoint. A fresh fixed schedule and explicit idle-runner handoff must precede their execution. No author should consume or adapt those held-out results early.
- **Matched profile:** compare exact B and baseline under the same scoped Intel workload and report controller boundaries, sample denominator and uncertainty. Instruction shape alone does not establish the measured gain. Keep the AMD discrepancy visible rather than treating another architecture’s timing as its explanation.

These are unresolved adoption gates, not grounds to falsify or discard the valid narrow discovery. No new feature variant is warranted to close them.

## Hotspot and mechanism limits

Intel baseline sampling places the all-match helper in **36 of 131 samples at 100K and 42 of 174 at 1M** (27.48% and 24.14%) within the executable-range sampler. Scan-slot inclusive shares are 86.26% and 90.23%. Nested inline shares overlap; the denominator excludes libraries/out-of-range/lost events, and missing-event counts are unavailable. This establishes a relevant CPU-time location, not a precise fraction of all process cycles or proof of a particular cache/branch bottleneck.

Discovery thread time is close to wall time (minimum ratio 0.998962, median 0.999629 across 96 processes), which limits off-CPU waiting as the explanation for those rows. It does not distinguish instruction throughput from memory stalls. Assembly supports the intended exact-mask mechanism, but Intel’s matched B profile remains outstanding.

AMD’s single matched diagnostic reduced instructions/branches by about 12% while branch misses rose about 5%, with less than 1% cycle improvement. It did **not** reproduce its exploratory 4–5% elapsed magnitude. Its diagnostic layout also differed from the original timing binary. Do not claim that discrepancy is explained by layout, sampling or another machine without evidence.

## What the numbers support

Exact B reduced elapsed time for Intel’s original, uninstrumented 16-byte scan fixtures at 100K and 1M under its qualified, frozen discovery schedule. It remains a conditional architecture-specific lead. Missing/noisy guards, fresh confirmation and profile validation keep adoption **PARK / NONE**. No portable, production Redis or universal data-structure speedup is established.

## Focused referee extension: immutable 2ab283daa

The separate focused referee is suitable to measure its declared cells after its own frozen calibration and A/A; no blocking defect was found. This is a read-only review, not a timing result. The independent audit verifies all six referee hashes, the fixture-manifest hash, 368 serial validation commands, 108 exact cells and eight expected fault exits. It reconstructs native/census semantic and memory parity and records sanitizer validation separately. Fixture binary hashes were not recomputed because only the manifests are published; no generation or workload was rerun. See [focused-referee-audit.json](focused-referee-audit.json).

The generator filters the original seeded SipHash bytes rather than modifying tree tags. Keys contain distinct binary ordinal/nonce content and 321-byte fixtures exercise external records. Callback validation compares exact member bytes, length and finite score bits, checks full membership while allowing legitimate scan duplicates, and separately verifies ordered iteration. Four deliberate callback faults cover wrong score, wrong length, real callback omission and wrong nonce content; native and sanitizer runs detect all eight instances. The omission fault actually suppresses the callback, rather than changing expected coverage.

The timing executable links the public API and original tree as separate translation units without LTO. The private census is a separate executable and rejects nonzero pass counts. Zero-pass validation avoids both clocks. Two warmups, membership/iteration checks and key construction are outside the clock; timed work includes complete public scan traversals and a count/checksum callback. That callback is heavier than the original count-only discovery callback, so focused elapsed percentages cannot be pooled with original discovery. Both logical members and actual duplicate-inclusive callbacks are recorded. Fixed pass counts must be selected from baseline calibration before A/A, without control-dependent retries.

Coverage is concrete and limited. All 36 descending cells contain exactly one reversed leaf with 64 members: only 1.5625% of 4,096-member fixtures and 0.064% of 100,000-member fixtures. This is sparse reverse coverage. Folded fixtures contain both real zero and one tags; zero-tag fractions range 48.853–50.684%. The dense tag-17 fixtures contain only tag 17. No cell has active rehash or wide IDs. All-equal scores are positive 0.25, so signed-zero behavior is not exercised. Only lengths 16 and 321 are included. These results do not close broad reverse, active resize/migration, wide-ID, signed-zero or remaining length-boundary performance gaps. Existing correctness oracles remain useful but cannot qualify performance in those missing states.

The 300/900/900-second phase caps, 200 ms calibration target and 100 ms qualification floor are frozen before timing. Any exhausted budget, unqualified cell or missing guard leaves adoption PARK. Root review 239ac9730 independently approved this referee; this extension adds one independently authored review and does not claim a completed multi-reviewer skill workflow.

## Independent confirmation follow-up

The fixed independent held-out protocol5c29cb07f subsequently qualified both Intel A/A primaries and confirmed B in all12 blocks, with medians−6.783%/−3.656%. All96 raw processes and independent reconstruction are preserved in [012 result](../012-intel-confirmation/RESULT.md). This closes the narrow independent primary confirmation gate; guard/profile gaps above remain. No adoption.
