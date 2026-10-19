# Adversarial review — exact Intel scan B

## Verdict: NOT YET DEFENSIBLE for adoption; declared discovery is supported

No blocking semantic defect or discovery parity failure was found. The frozen Intel screen supports a narrow scan improvement on its declared fixtures. It does not establish safe performance across the required guards, independent confirmation, or a validated explanation of the elapsed gain. Keep source **NONE**.

Reviewer: `/root/aws_amd`, one actual native agent using the benchmark-adversarial-review checklist, adapted to this standalone in-process benchmark. The reviewer authored independent variant A earlier and knows the shared hypothesis; this is not a blinded review. B was independently authored by Intel. No extra reviewer panel or stronger model execution is claimed; exact inherited model and token/USD costs are unknown. Network, server, TLS, client saturation and pricing checks are inapplicable to the user’s standalone scope.

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
