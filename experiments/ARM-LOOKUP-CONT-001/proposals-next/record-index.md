# Independent population 2: carry short-record length in spare offset bits

Proposer: the independently assigned record/index worker, 2026-11-14. This is a fresh review of CONT source and evidence, not the earlier logical-position proposal. I did not read `raw-state.md` or `index-probe.md`. Detailed backend provenance is retained privately; model identifier, token usage and monetary cost are not reported. No source edits, measurements, fleet access, commits or publication were performed.

## Selected hypothesis

**Use the unused upper four bits of each existing 16-bit record-offset entry to carry an exact short-inline length hint. For a hinted tag match, validate length from the offset entry and call the unchanged byte comparator directly, avoiding the dependent record-header load and generic record classification.** The hypothesis predicts at least 2% lower elapsed time in every qualified primary block, with no greater-than-1% guard or tree-owned-memory regression. Static plausibility does not establish that gain.

This changes metadata encoded in the existing offset entries, not their size, the tag scanner, member index, record payload, allocator, score stream, or equality algorithm. All unhinted records retain the complete baseline decoder, external-hash check and comparison path. Start from the exact current baseline, not H1/H2/H3: unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`, source C SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, referee commit `e13d9fc88` used by the continuation. Recheck current upstream before freezing a new implementation cohort as the user requires.

## Evidence

`current/src/zset_btree.c` declares `ZBT_SCORE_LEAF_BYTES` as **4095**, while offsets occupy `uint16_t`. `zbtScoreLeafBuild()` asserts its requested bytes are within that limit and caps the allocator's larger usable capacity to the same limit before placing records. In-place insertions place records below `record_start`. Thus a valid record address within a score leaf needs only the lower 12 bits; four upper bits are available without enlarging a leaf or index bucket. This is a source invariant to preserve and test, not permission to assume allocator usable sizes are always below 4096.

The exact native assembly at `native-profile/assembly.stdout`, `zbtScoreLeafFindMember.constprop.0`, shows the dependency: `ldrh` of the offset at 0x37e0, then `ldrb` of the record marker through the loaded offset at 0x37e8, two format comparisons at 0x37ec/0x37f4, then a length comparison at 0x3804 before the unchanged `memcmp` call at 0x3814. For the primary's 3–5-byte inline records, that marker is exactly the member length. A hint can provide that length at the same time as the offset, leaving the record address necessary only for actual byte equality.

The fresh native profile assigns 41.38% of captured user-cycle weight to the leaf helper and 21.77% to raw lookup. This identifies a relevant chain; it does not establish the latency of the marker load, a cache miss, or a removable percentage. H2's native discovery supports investigating dependency removal generally, but neither its gains nor H1's rejected results count as evidence that this new representation wins. Process profiles include setup and warmup; the optional CPU-wide TMA remains exploratory.

## Three maintainable implementation options

All three encode/decode offsets through small named accessors, preserve ordinary record headers, use exactly two bytes per offset entry, and change no other hypothesis. Retain each patch, emitted-code evidence and failures.

| Option | Encoding and lookup shape | Tradeoff |
|---|---|---|
| R1: exact low-length nibble | Lower12 bits hold offset. Upper nibble0 means generic; codes1–15 represent physically inline lengths0–14. After a tag match, extract the code; nonzero supplies `code-1` as exact length. Equal query length permits baseline `memcmp(record+1, query, length)`, otherwise reject that candidate. | Broad compact range with simple arithmetic. Adds subtract/decode work and requires masking on every raw offset use. Preferred first spelling for a clear invariant. |
| R2: valid bit plus three-bit length | Bit15 marks a physically inline length0–7; bits12–14 hold that exact length. Unhinted records have high bits clear. Test the validity bit and compare the three-bit length with the query before the unchanged comparator. | Smaller useful range but cheap validity/length extraction; covers the full primary without relying on its names or seed. All lengths8 and above remain generic. Must guard the 7/8 boundary explicitly. |
| R3: explicit common-length codebook | Nibble0 means generic; codes1–15 refer to a fixed documented injective table such as lengths0,1,2,3,4,5,6,7,8,12,16,24,32,64,128. Record writers select a code only for physically inline records. Lookup decodes the small constant table to get an exact length before baseline equality. | Extends the same cached-length mechanism to larger common inline lengths. Adds a small table access or compiler-generated decoding sequence that may erase the saving. Reject this spelling statically if it introduces disproportionate dispatch/spills; do not add another optimization to rescue it. |

The codebook is a general documented representation policy, not an encoding of fixture keys or scores. Zero-length and all unlisted lengths remain fully supported. R1/R2 are simpler review candidates; R3 tests whether a broader exact-length cache can remain useful despite its decode cost. These are three implementation alternatives of one metadata hypothesis, not three independent proposal votes.

## Ownership and mutation contract

The hint describes the **physical record representation**, not merely the member's length. Never mark an external record as inline, even if a correctness oracle constructs an externally represented short member. Hinted records must have an inline byte-length header matching the cached value. Unhinted external records must still validate their full cached hash, length, nonnull pointer, and complete member bytes. Preserve allocation ownership and all original assertions.

Centralize a decoded offset accessor and an encoder that accepts the true offset plus the already-written record. Add a compile-time assertion that the leaf limit fits12 bits and debug checks for representable offsets and cache/header agreement. Do not use an unmasked descriptor as a pointer displacement, byte ordering comparison or free-space quantity.

The audit must include at least:

- `zbtScoreLeafOffset()` and the direct offset load in `zbtScoreLeafFindMember()`.
- Every descriptor store in `zbtScoreLeafBuild()`, `zbtScoreInsertInPlace()` and `zbtScoreInsertFast()`. The build currently stores its plain offset **before** `zbtBuildElementWrite()`; generating a hint from the actual record requires moving that store after record construction or supplying an equally justified representation-aware encoder. Do not read an uninitialized header.
- Direct offset reads in live-byte accounting and deletion/compaction. Around lines2515,2613,2639 and2666, pointer arithmetic, comparisons and offset adjustment must use decoded lower bits and preserve the corresponding hint. An arithmetic carry must never corrupt hint bits.
- Offset-array `memmove`, reverse-leaf swaps, temporary locations arrays, rebuild/merge/split, trimming and score-width repacking. Some temporary locations come from a decoded accessor, so simply copying them back would lose hints; choose a consistent raw-descriptor versus decoded-offset contract.
- Duplicate/defragmentation/external-pointer repair. Relative offsets and byte length hints should survive leaf relocation, while external ownership stays with the original rules. Explicitly prove these paths rather than adding cached pointers.

The main risk is stale metadata after mutation, followed by skipped length validation or an incorrect record address. A second risk is the extra mask/decoding cost in iterator/rank/update paths that do not benefit from lookup hints. No memory growth is expected, but actual accounting and alignment effects still require measurement.

## Guard and falsification plan

Before timing, retain the full upstream native/sanitizer suite, output/external ownership oracles, and focused descriptor-invariant tests. Exercise every supported code, all transitions7/8,14/15,253/254,319/320, unlisted lengths, binary contents, empty members, same-tag and full-hash collisions, mismatching lengths, all output combinations, both physical leaf orders, allocator capacity rounded above4095, and record offsets near the12-bit limit. Force insertion/repack/delete/compaction/split/merge/dup/defrag/resize paths, validating every surviving hint against the actual record header after each operation. External short-record fixtures remain generic and must retain hash rejection. Guard-page and exact allocation checks must prove unchanged comparison bounds; no padding assumption.

Use separately qualified native ARM, target GCC/LTO and Intel cohorts; preserve the campaign's fixed all-block ≥2% primary and ≤1% guard/memory gates. Keep hit/score/miss/inline256/external384/update cases and the already prepared iterator/rank/churn guards. Add boundary-length and mixed-length/collision guard coverage **before** candidate timing, within a declared run budget. Native and LTO code generation can differ; never pool their effects. Fresh seeds, matched profiles and independent review remain mandatory after discovery.

Static falsifier: if hinted short hits still load the record marker before comparison, or masking/decoding length adds a comparable serial chain, the intended mechanism is absent or weakened. Inspect exact binaries rather than assuming source hoisting. Dynamic falsifiers: any semantic/cache invariant failure, any >1% guard or memory loss, any required primary block below2%, or unexplained timing-only improvement. A smaller leaf-helper sample share cannot override elapsed-time failure. An iterator regression rejects the candidate rather than removing masking from required accesses.

## Alternatives not selected

Replacing compact leaf IDs with full pointers would increase bucket storage and create relocation/ownership work; no measured evidence here justifies that memory tradeoff. A last-leaf lookup cache would add invalidation obligations and likely tax misses, while depending heavily on sequential query locality. Duplicate-leaf suppression could help collision misses, but the current profile lacks probe/duplicate counts proving sufficient exposure in the primary. Select NONE for those alternatives until a separately frozen diagnostic supports them.

This proposal is distinct from H1 helper boundaries, H2 count×score-width-to-metadata address computation, and H3 short byte equality. It removes the offset→record-header **length/representation dependency** by encoding redundant record metadata in otherwise unused bits. It keeps memchr and memcmp, shared score decoding, and all H1/H2/H3 changes out of the first comparison.

## Consultation and TMA

My own fresh tool-discovery filter found no exposed cpu-perf/library_status tools. Under the worker-sharing allowance, I consumed the controller's actual continuation consultations in `CONSULTATION.md` (server0.1.1, bundled deb5a0bac467,3/287 sources,158 passages), including its metadata-dependency question. Those are shared controller calls, not mine. Retrieved passages did not establish a workload mechanism. The new descriptor-cache proposal needs a controller reconsultation with its exact range/mutation contract before implementation; current support is inspected source/assembly only.

| TMA category | Qualified baseline | New candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No new profile or candidate exists. Existing CPU-wide labels lack the required exclusion/formula qualification and supply no validated child categories. Do not translate the observed load chain or sample shares into a backend/memory slot percentage.
