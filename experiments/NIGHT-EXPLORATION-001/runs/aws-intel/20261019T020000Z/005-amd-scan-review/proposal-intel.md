# Independent Intel proposal: exact 16-byte all-match masks

Participant: `/root/aws_intel`, native session. Exact serving backend/model and measured token/USD cost are unknown. This is one independently authored proposal, not a chair decision or candidate implementation. I read only the common packet and its linked baseline profile/census evidence, baseline source and previously known experiment decisions; I did not read AMD/ARM proposals or a chair decision.

Evidence pin: common packet commit `b1b670c0a`, AMD `008-scan-tags/COMMON-PACKET.md`; target source `8fab511e0e6ec7d4808546cd50064c6bf299e695`, `src/zset_btree.c` SHA256 `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`. Referee remains the original frozen `bench/microbench.c`. Measurements below belong to AMD Zen5, not Intel.

## One hypothesis and exact scope

On the measured x86-64 AMD host, replacing only the complete-word scanning portion of `zbtLeafTagMatches` with exact 16-byte SIMD equality masks will reduce complete tag-span scanning cost enough to improve both declared scan primaries by at least2%, without changing results, caller behavior or memory. Keep the existing bounded SWAR/scalar implementation as the portable fallback and for residual bytes. No first-match shortcut, member decoder change, caching, index layout change, hashing change or scan callback change is included.

The baseline processes complete eight-byte words, creates SWAR masks that may contain false-positive lanes, enumerates set bits and verifies each candidate byte. An SSE2 comparison plus movemask can produce exact matches for sixteen physical bytes at once. Enumerate nonzero mask bits in ascending lane order. For index tag1, OR exact comparisons against bytes0 and1. All other tags compare once. Only load complete16-byte spans; preserve bounded residual processing. This is a proposal for an architecture-scoped implementation behind a compile-time capability guard, not an instruction to add global target flags or runtime dispatch infrastructure.

## Evidence supporting a bounded experiment

The authoritative same-IP helper attribution is21.312%,38.985%,36.534% of sampled period at100K, and27.928%,23.343%,26.252% at1M. These are six coarse captures of67/67/67 and90/90/91 sampled events respectively, not precise cycle accounting. Nested TagMask attribution must not be added again. The enclosing ScanSlot dominates, but its whole share is not available to this change.

The census records1,066,100 calls at100K and1,003,270 at1M, mean spans69.903 and68.982 bytes. Nearly all spans are48..96 bytes; the1M census additionally has12 calls with span12. Every call must discover the full set of matching tags before the caller can decide whether hashing/reachability disambiguation is necessary. Approximately76.6–76.7% of calls have one match, but this does **not** permit stopping at the first match. Mean match counts are1.2701 and1.2664, so mask enumeration is usually short even though scanning is complete. Tag1 is about0.784%, so the double comparison is uncommon in these fixtures. These facts support testing wider complete-span equality with low result-extraction cost.

The census includes no reversed leaves, no zero-match calls, and only normal fixture distributions. It cannot establish performance or correctness for reversed, folded-tag-heavy, dense-collision, tiny-span or mutation/rehash workloads. Census counters are not timing evidence. Baseline A/A was pending in the common packet and remains a prerequisite for acceptance.

## Novelty and negative evidence

Intel's previous bounded SSE2 **first-match** scanners lost to libc memchr on both lookup primaries. That is a strong warning against assuming SIMD wins. The present baseline is an explicit eight-byte SWAR **all-match** loop that scans the whole span and verifies approximate-mask candidates. It does not already delegate the operation to libc's first-match implementation, and it cannot stop at one match. This different stopping condition and baseline mechanism make a narrowly bounded experiment defensible. It does not rehabilitate the rejected first-match variants or imply portability of an AMD result. M1's parked first-match SWAR and the M6 decoder families are also separate and supply no timing evidence here.

## Predictions and falsification

Expected direction: improvement on the original100K and1M scan primaries with ordinary48..96-byte leaves and sparse matches. Smaller spans below16 should closely follow unchanged residual code; dense matches may gain less because position emission dominates. Folded-tag-heavy and reversed cases may expose overhead hidden by the primary census. Tree-owned memory and iterator state must be exactly unchanged.

Preregister and retain the packet's same-session six-block ABBA schedule, frozen sources/flags/seeds/allocator, at least10ms windows, and300-second screen ceiling. Require every primary block at both sizes to meet the>=2% elapsed improvement gate and no demonstrated>1% guard or memory regression. Unqualified controls imply PARK, never acceptance. Any semantic/sanitizer failure disqualifies a candidate. Reject this direction if all implementations miss either primary gate, materially regress a qualified guard, or move the expected helper work without producing repeatable whole-operation benefit. No per-candidate tuning, post-hoc threshold changes, dropped rows or extending a failed bounded screen.

Matched scoped profiles should show reduced work associated with the complete tag loop, subject to sample uncertainty and inline attribution. Merely seeing fewer source branches, SSE instructions or a different hot PC is insufficient. Fresh independent confirmation and adversarial review remain required before a performance recommendation; source adoption remains NONE overnight.

## Correctness and portability gates

1. A new independent scalar oracle must compare the complete returned position sequence and count for every span0..96, all256 tags, both reversed states, all alignments and bounded guard-page placements. Include all-no-match, all-match, first/last lane, boundary15/16 and31/32, folded0/1, neighboring-byte borrow patterns, high-bit bytes and canaries beyond the permitted positions output. Do not reuse a first-match oracle as proof of this contract.
2. Keep physical enumeration order increasing; reverse maps each physical position to `count-1-position`, so the output logical positions decrease. Never sort logical positions or return only the first match. Mask extraction must be nonzero before ctz, use defined-width arithmetic, and never include tail lanes outside count.
3. Index tag1 stands for physical0 **and**1. OR masks without duplicates; generic tag0 behavior must still match the existing helper for direct tests even though live index slots reject0. Every reported position must fit the caller's96-entry array.
4. Preserve scan caller behavior for collisions, home intervals, tombstones, narrow/wide leaf IDs, old/new tables, migration ownership, table wraparound and external members. Run unchanged original tests and existing scan_interval, wide_scan, live_widen_scan and resize_generation oracles in release/sanitizer builds. Add deliberate lane-order and folded-zero omission faults to prove the new exact-position oracle detects those failures.
5. Verify the compile-time portable fallback with the same all-match oracle and inspect the actual binary. Forced fallback on x86 is not actual big-endian or ARM execution. No unbounded16-byte load, page overread, permission change or architecture-wide compiler flag is allowed.

Before candidate timing, freeze concrete performance guards for small sizes/short leaves, reverse-heavy leaves, folded0/1-heavy and dense-collision scans, long/external members, mixed mutation/resize scans, and the original non-scan operations. Correctness coverage does not substitute for those guards. If meaningful guard fixtures cannot be frozen and qualified within the budget, the experiment may remain exploratory/PARK or the chair may choose NONE.

## Recommendation

Choose this single exact all-match mask hypothesis for a bounded x86-64 AMD investigation **only if** the chair considers the complete-span baseline distinction sufficient to overcome the negative first-match prior. Otherwise choose NONE. I do not recommend an unbounded family of SIMD/tail/cutoff searches, and I do not claim that this proposal is already faster.
