# H6-A: exact short-inline length in record descriptors

Status: **correctness ready; exact fleet code-generation, performance and affected-consumer guards pending**. Implementer: `cont_helper` (H6-A). Base `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. Completed 2026-11-14 02:35 UTC. Other H6 implementations were not inspected. No fleet access, local benchmark, instruction-count measurement, profiling, commit or push.

## Representation and lookup

Each existing 16-bit offset word becomes a descriptor: low 12 bits are the record offset; upper nibble 0 means generic, and codes 1–15 encode physically inline lengths 0–14. No structure, array position, allocation request or record header changes. The original score stream/base and metadata-array sizing remain unchanged. Leaf/helper boundary, `memchr`, `memcmp`, home-filter mathematics, raw dispatch, hashing and external ownership retain their original behavior; no H1–H5 patch is included.

Named accessors decode offset/code, encode a descriptor from an **already-written actual record**, and relocate an offset while preserving its code. A static assertion ties the leaf limit to 12-bit offsets; encoder/relocation assertions check representability. Debug descriptor reads validate any cached length against the physical header, and the test-only structural checker validates the full encoding policy for every descriptor. External markers never acquire a hint, even for short externally allocated values.

After a tag match, hinted candidates get length from the descriptor and payload at `record+1`; the existing length equality and bounded `memcmp` expression remain unchanged. Generic candidates retain the original external full-hash rejection, decoder, length and byte comparison. The successful mapping/output block is unchanged. The new mask costs other member-offset consumers, and mutation writers maintain redundant state; neither cost may be ignored by acceptance guards.

Source SHA-256: `ffd548a1fba1db452e98fbe1dd3902b2ba34f44af797edeaed9976783444e744`.
Baseline source SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
See [implementation.patch](implementation.patch) and [source-verification.json](source-verification.json).

## Offset and mutation audit

| Consumer or writer | Descriptor contract |
|---|---|
| `zbtScoreLeafOffset` / ordinary member access | Logical-to-physical selection returns a checked descriptor; pointer displacement uses only decoded low bits. |
| `zbtScoreLeafFindMember` | Direct physical descriptor load separately decodes offset and length code; generic external hash filtering remains intact. |
| `zbtScoreLeafBuild` | Descriptor store moved after `zbtBuildElementWrite`; the encoder never reads an unwritten marker. Covers original builder uses in initial/bulk construction, rebuild, split, merge and compaction. |
| Re-encoding `zbtScoreInsertInPlace` | The inserted record is written first and then encoded. Existing locations are complete descriptors, not decoded offsets. |
| Temporary `locations[]` in insertion | Existing entries come from `zbtScoreLeafDescriptor`; the placeholder for the new entry is ignored in favor of its freshly encoded record. |
| `zbtScoreInsertFast` | Existing array moves preserve full words. The new record is encoded after construction. |
| Live-byte accounting | Decodes each offset before adding it to the leaf base. |
| `zbtScoreDeleteInPlace` | Decodes deleted-record address and all address-order comparisons. After record movement, `zbtRecordRelocate` updates low bits with a checked sum while retaining the old high nibble. |
| Score-array shifts and leaf reversal | Full descriptor words are moved/swapped with their corresponding records and tags; no hint is recomputed or lost. |
| Duplicate and defragmentation | Existing whole-allocation copying preserves relative offsets and hints. External pointer repair still uses decoded record addresses; it does not change external representation. |

Audited all direct `offsets[]`, `old_offsets[]`, and `locations[]` reads/writes. `record_start` remains an unencoded free-space boundary. Existing byte-limit and capacity-capping checks remain intact. No unmasked descriptor is used as a record address, address-order comparison or free-space quantity. Reverse swaps deliberately carry full descriptors, although the original local swap variable remains named `offset`.

## Correctness evidence

Local GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1). The unchanged `qualify.sh` exited 0. Fixtures execute `verify`, not the timer-reading measurement branch.

| Check | Result | Evidence |
|---|---|---|
| Upstream native `-O2` | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Upstream ASan/UBSan `-O1` | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Six fixtures × seeds 17/29/43, native | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same fixtures, ASan/UBSan | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Supplied optional-output oracle, ASan/UBSan | 90,000 passed | [output_oracle.json](output_oracle.json) |
| Supplied external-record oracle, ASan/UBSan | 45,000 passed | [output_external_oracle.json](output_external_oracle.json) |
| Added descriptor oracle, ASan/UBSan | 796,816 invariants; 11,272 comparisons; 1,800 mutations; 132 relocations | [descriptor-oracle-sanitizer.json](descriptor-oracle-sanitizer.json) |
| Same oracle, optimized native `-O3` | Identical passing result | [descriptor-oracle-native.json](descriptor-oracle-native.json) |

The added [descriptor_oracle.c](descriptor_oracle.c) observes all 16 nibble states and a maximum actual offset of **4094**. Public mutations include descending insertion, score movement/re-encoding, deletion, alternating edge pops, batch append, duplication and active defragmentation. Every surviving descriptor is checked against the actual record header after operations, with unchanged structural/index checks. The relocation callback allocates extra capacity; invariants still cap meaningful record bounds at the original leaf byte limit.

Its member lengths include all codes 0–14 plus 15/16, 253/254 and 319/320/384; the frozen fixtures additionally exercise inline 256 and external 384. Binary members and the empty string are included. Guard-page tests place payload ends immediately before inaccessible memory, put queries at both readable-page edges, exercise both physical leaf orders and all output-pointer combinations, and test every single-byte mismatch for lengths 0–16. Same-tag unequal candidates precede the target. Exact allocation ends exercise all eight source/query alignments independently, with longer-query rejection added separately. Zero-length checks use non-NULL one-past pointers and make no expanded NULL-input API claim.

The external-short test creates **real owned external allocations** for lengths 0–14, supplies them to the unchanged builder, asserts marker 255/code 0, checks successful lookup and same-tag/full-hash mismatch rejection, then frees the owning tree. It does not fake an inline length from the query. Existing output oracles retain their reversed-leaf and optional-output coverage.

Coverage limits: no per-branch instrumentation proves every internal rebuild/compaction branch was taken. Coverage combines the complete static offset audit, the existing suite, and explicit mutation entrypoints/invariant checks. The synthetic collision fixtures do not establish naturally occurring full 32-bit collisions. Additional mixed/boundary/member-iterator performance coverage remains required; correctness counts do not qualify those workloads.

Sanitizer oracles use C11, `-g -Wall -Wextra -O1 -DREDIS_DEBUG -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`, with `-Werror` for the added test and unchanged compatibility sources. Native added-oracle validation uses `-O3 -Werror`. Final runs exit 0 with empty stderr.

The first **new oracle setup** failed under ASan before invoking the candidate lookup: its zero-length query lay at the guard boundary, and setup incorrectly copied one byte from it to construct a nonempty decoy. The failed [source](first-attempt/descriptor_oracle.c), [stderr](first-attempt/stderr.log), compiler log and private binary are preserved. The test now uses a separate valid byte for that decoy; the candidate source was unchanged. Exact-allocation padding was also removed to strengthen end checks, then explicit different-length comparisons were added and both sanitizer/native runs repeated. The earlier passing count before added length comparisons is retained. No candidate-source failure or measurement retry occurred. Baseline qualification evidence was restored after copying candidate logs here; `git diff --check` passes.

## Static mechanism evidence

A separate **unexecuted x86-64** GCC13 `-O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`, no-LTO lookup ELF has SHA-256 `02ad2b115219de7ad0e6f9c9e34f1427d9c4ce67d1489a577892afa630e82043`. This is static code inspection, not local performance evidence or a fleet-cohort gate.

In [leaf-codegen.txt](leaf-codegen.txt), the offset-word load at `0x3c9c` is followed by low-bit masking and nibble extraction. A nonzero code branches at `0x3cb1` to length comparison at `0x3c58`–`0x3c66`, bypassing the record-header load at `0x3cb3`. Both paths reach the original `memcmp` call at `0x3ce9`; `memchr` remains at `0x3c7e`. Thus this local compiler realizes the intended header-dependency bypass. Exact ARM native, GCC15/LTO and fleet Intel ELFs must be inspected separately before timing. Debug builds intentionally read headers to validate hints; timing binaries must retain identical assertion flags across controls and variants.

## Remaining gates and TMA

Apply the chair's independently qualified cohorts: ≥2% primary gain in every block, ≤1% guard/memory regression and ≥250 ms windows. Preserve source selection separation, fresh confirmation, portability and review. Member-address consumers now mask descriptors, so member iteration/rank/churn and mixed boundary-length guards need their own frozen qualification before adoption. A score-only guard is insufficient. No allocation change is expected, but fleet-owned bytes remain a measured gate.

| Pipeline-slot category | ARM baseline | H6-A |
|---|---|---|
| Frontend_Bound | Unavailable: scope/formula qualification absent | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Child categories unavailable. No pipeline cause follows from the observed load chain or another architecture's baseline. The controller owns actual topdown assessment.

## Consultation provenance

Own exposed-tool discovery found no `cpu-perf`/`library_status` tools. Consumed the controller's actual shared stdio descriptor `library_status`/`ask`, not calls made by this implementer. The question covered the 12-bit bound, three proposed encodings, physical-inline restriction, complete mutation/relocation audit and risk to member-address consumers.

Bundled revision `deb5a0bac467` (2026-10-05), 3/287 sources, 158 passages, zero vectors, keyword-only. No supporting primary passage matched. Unread entries and bundled examples establish no gain. The consultation did not alter the selected encoding; correctness invariants and exact fleet gates remain controlling evidence. Detailed participant accounting remains private.
