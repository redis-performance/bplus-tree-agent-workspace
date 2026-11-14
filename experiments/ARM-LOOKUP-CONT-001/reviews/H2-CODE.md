# Independent H2 source review

**No concrete source-semantic blocker found in the two final candidates.** This is a bounded code/correctness review, not source adoption or performance approval. Original timing, memory, portability, confirmation and profile gates remain independent requirements. I did not implement either H2 source candidate. I did author the supplemental guard harness, so this report must not be counted as its independent review.

Reviewed exact source identities:

- H2-B: `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29`.
- H2-C: `789ca7e217baa67cba165d2ebed7be0c9c1a2a7067f94ae870431395e66ffe49`.
- Unchanged baseline: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, extracted from upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`.

I independently reconstructed both retained patches in memory against the baseline and matched each result to its isolated final source. No target source or referee was edited.

## H2-B: cached score bytes and packed flags

The required invariant is `score_bytes == zbtScoreLeafScoreBytes(count, score_bits)` for every live leaf. I enumerated all four direct leaf-count writes and both score-width writes. Complete build and re-encoding insertion install count/width/cache before resolving offsets or writing arrays. Fast insertion reads old offsets through the old cache, uses explicit new-size destinations during movement, then publishes count/cache before path updates. Deletion likewise uses the old cache until relocation is complete and installs the new value before returning. No count/width mutation without cache maintenance was found.

Split, merge, compaction and append construction reach the complete builder. Position-preserving score updates and reversal change neither count nor width, so their unchanged cache is appropriate. Reversal can change the score base without invalidating the reserved byte count. The maximum reserve is776 bytes at96 members/64 bits, within `uint16_t`; zero-width scores correctly reserve zero. I checked the reserve bound over all96 counts and65 widths.

All old node-type/external/shift field accesses are migrated to the new masks/accessors. The score shift occupies bits0–5; the nonzero-difference encoding path produces0–63, while equal-score encoding explicitly uses shift0. The shift setter preserves leaf/external bits. External-record writes set their flag without changing the shift, and inner-page zero initialization leaves the leaf bit clear. Retaining a true external flag after deletion is conservative, as in the baseline: ownership paths still inspect each record tag. The full moved-out and resize-ID fields remain intact.

Duplication copies the entire header/allocation before repairing ownership; defragmentation copies that state and fixes pointers without introducing a cached absolute address. Free, dismiss, duplicate and node-relocation paths all use the new leaf/external tests. I found no stale-cache, ownership or flag-aliasing defect in these paths. The updated upstream test checker changes its representation accessor without removing its previous assertions.

## H2-C: metadata before packed scores

With `D=leaf->data`, `n=count`, and `S(n,b)` the existing score reserve, the new regions are offsets `[D,D+2n)`, tags `[D+2n,D+3n)`, scores `[D+3n,D+3n+S)`. The total size and record-capacity calculation remain unchanged. Fixed offsets remain aligned, checked by a compile-time alignment assertion. Odd score bases are allowed: loads/stores remain byte access or `memcpy`, not misaligned typed64-bit dereferences, and existing endian conversions remain present.

Fast insertion saves tags, moves the score reserve right to the new count's base, zeroes the nonnegative reserve extension and inserts the bit field with explicit old count. It then shifts fixed-base offsets and rebuilds saved tags before publishing count. These offset/tag writes end at the new score base and do not destroy the relocated score payload. The existing capacity test bounds the complete new arrays below the new record.

Deletion reads record metadata and saves tags first, deletes the packed field while count is old, compacts offsets, then moves the reduced score reserve left before rebuilding tags and publishing count. The compacted offsets end before the new score base; new tags end exactly at it. The overlapping score movement correctly uses `memmove`. Count1 is handled by the existing remove-leaf path, avoiding zero-count deletion arithmetic. Zero-width movement and unchanged-width reserve monotonicity are consistent with the same ordering.

Build/re-encoding, reversal and in-place score updates use the new score accessor. Split/merge/repack use the existing builders; copy/defrag retain relative record offsets and introduce no new lifetime-sensitive pointer. Only four direct `leaf->data` uses remain: fixed offsets, the general score base, and the explicit new-count insert/delete score bases. I independently confirmed the nine claimed unchanged bodies, including scanner/index lookup, allocation formula, and bit read/write helpers. No missing old-layout access or demonstrated overlap corruption was found.

## Correctness evidence independently checked

Saved final evidence for each candidate contains57 native and57 sanitizer upstream passes,18 fixture cells per mode,90,000 optional-output and45,000 explicit external-record checks. These counts are supporting evidence, not exhaustive proof. The focused source was also inspected rather than accepted solely from its reported counters.

I independently reran the existing focused ASan/UBSan executables after verifying their recorded hashes, without recompilation or performance collection:

| Candidate | Binary SHA256 | Rerun outcome |
|---|---|---|
| B | `539bf352080ed6a649cf07a7763ba56061832f15592646b5f7c09b1434fd35fe` | Pass:7,693 validations,100,285 leaf checks,54 page moves,256 flag/shift combinations; zero/full-width and reversed leaves observed |
| C | `d3c3861d06f9af1c507ef875218a21984e12bd0f23889b514f83c653fdb7592e` | Pass:10,752 matrix cases,366,336 leaf checks,156 full-tree/model checks,186,616 odd score bases,7,833 external-record checks,8 rehash states |

Both processes exited0 with empty stderr. B's focused test checks cache formula/flags after mutations and moves. C's direct-leaf model covers widths0–64, both orientations and count/boundary transitions, with independent expected member IDs and exact scores; its mixed-tree phase adds external ownership, updates, duplication and moving defragmentation. These reruns reproduce existing coverage; they do not constitute newly randomized or exhaustive fuzz coverage.

## Residual limits and maintainability

- **Portability remains scoped.** B's original unconditional64-bit footprint assertion was repaired before the final source; the retained32-bit toolchain probe fails for missing multilib headers. Neither candidate has demonstrated32-bit or big-endian execution in this review. Source alignment/endian reasoning is not cross-platform validation. C's focused oracle itself asserts24/56-byte layout unconditionally and uses `__uint128_t`; that oracle cannot establish general32-bit/compiler portability without adaptation. This is a test limitation, not a demonstrated production-source failure.
- **B adds a maintained invariant.** Current writes are covered, but a future count/width mutation can forget the cache. Keeping the focused cache/flag oracle in the permanent regression path would protect this invariant; the ordinary structural checker does not itself independently recompute every cached value.
- **C broadens movement risk.** Fixed metadata simplifies lookup addressing while relocating scores on count changes and adding count dependence to score reads. This review found the ordering valid, but does not establish acceptable iterator/rank/churn cost. Direction-separated guards and exact immediate memory endpoints remain necessary.
- **Memory evidence has boundaries.** Unchanged layout size/formulas do not prove all workloads have identical allocator behavior or transient peaks. Native/sanitizer owned-byte values are not interchangeable. Apply measured memory gates in the correct compiler/host cohort.
- **Coverage is bounded.** The focused cases sample widths, shifts, positions and lifecycle sequences; they do not exhaust every legal tree history, hash collision pattern, interleaved defrag mutation or compiler optimization. NaN remains outside the stated low-level contract.

## Provenance and TMA

This worker performed read-only source/evidence inspection and bounded correctness-only execution. Only this report was written for this task. No fleet query, timing, profiling, source/referee change, commit or push occurred. Detailed backend provenance is retained privately; exact model, tokens and monetary costs are unreported. Own fresh tool discovery found no cpu-perf/library_status tools. Shared controller consultation in `../CONSULTATION.md` is explicitly shared: server0.1.1, bundled `deb5a0bac467`,3/287 indexed sources,158 passages; no supporting retrieved passage establishes a workload mechanism. Those were not this reviewer's calls.

| TMA category | Qualified baseline | H2-B | H2-C |
|---|---|---|---|
| Frontend_Bound | Unavailable | Unavailable | Unavailable |
| Bad_Speculation | Unavailable | Unavailable | Unavailable |
| Backend_Bound | Unavailable | Unavailable | Unavailable |
| Retiring | Unavailable | Unavailable | Unavailable |

Qualified child categories are unavailable. This source review supplies no pipeline-slot or causal performance claim and does not replace the separate measurement/profile review.
