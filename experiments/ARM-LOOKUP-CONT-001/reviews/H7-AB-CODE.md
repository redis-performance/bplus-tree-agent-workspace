# H7-A/B independent source and correctness review

Review date:2026-11-14. Reviewer role: H7-C implementer, independently reviewing A and B. **C is excluded from this independent review.** No source, collector or fixture was changed; no fleet access, timing, profiling, commit or adoption occurred. Five existing correctness-only sanitizer executables were independently rerun.

**Decision: no source-correctness blocker found in A or B. Both may proceed to exact ARM native/target static review. This does not pass the ARM codegen gate or authorize timing before that gate.** The exact-mask computation adds dependent arithmetic before every bucket result. Whether removing candidate validation compensates for that cost, without growing the raw frame, remains an explicit admission question. This concern was reported to the controller before ARM builds.

## Frozen source and scope

Baseline commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, source SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`.

| Variant | Independently hashed source | Independently hashed patch |
|---|---|---|
| A | `002c3568202dff5cb5f39f28753f4b48d1c9ec1c533775371f2fea41eccb6ce8` | `a3945089f4abe5a483c2f01722d01d38b6fa0f246b4221a030c419c21fd2ab29` |
| B | `ce8ed5476d5b04953e514a1a798947272a4ab2846034d417fe1e7e0b25e080eb` | `6d28bf50be1c9364f110968a1c00416996c81c4ba574c5aa39f48b25002689e5` |

Reviewed [A patch](../variants/H7-A/implementation.patch), [A focused mask test](../variants/H7-A/mask_oracle.c), [A index test](../variants/H7-A/index_oracle.c), [B patch](../variants/H7-B/candidate.patch), [B mask test](../variants/H7-B/mask_oracle.c), [B index test](../variants/H7-B/index_oracle.c), [B reference-repair test](../variants/H7-B/reference_oracle.c), implementation reports, saved qualification/oracle results and local disassembly.

Both saved patches exactly match their source diffs. The only tracked source modification is current/src/zset_btree.c. I independently removed each new helper and restored only the declared call sites/checks; the resulting full source reproduces the frozen baseline byte-for-byte. This establishes the narrow scope independently of each implementer's scope-audit JSON.

A adds one exact helper and uses it only in `zbtIndexTableFind`, removing that loop's redundant stored-byte validation. B makes the same change in `zbtIndexTableFindReference` as well. Both leave the approximate helper unchanged, including its boolean vacancy consumers and leaf scan users; those callers retain their original checks. No H1–H6 patch, record/layout/ID change, leaf inlining, negative-filter change or resize dispatch change is present.

## Exact-mask identity and consumer semantics

For each byte of `x = tags ^ (0x0101010101010101 * tag)`, let its low-seven-bit value be a and its original high bit be h. The selected low mask L gives a in0–127. Adding127 yields127–254, so the addition cannot carry between bytes, including from the most significant byte. The sum's high bit is clear exactly when a=0. OR with x retains h; OR with L sets all seven low bits. Complementing therefore leaves precisely a high bit for a=0 and h=0, equivalent to an equal input tag byte.

The tag parameter is uint8_t; broadcast multiplication fits uint64_t even for255. All arithmetic is unsigned64-bit. The expression neither introduces a signed shift nor depends on memory byte order. Bucket tags already use numeric-byte positions through the existing accessors, which are unchanged. The existing guarded `while (matches)` prevents zero-input first-bit extraction; clearing the least significant set bit preserves ascending true-candidate order.

In A's member finder, every removed iteration was a false approximate candidate whose original validation immediately continued without loading an ID. Removing those false iterations while directly consuming only exact candidates preserves all remaining side effects and outputs. Folded tag0→1 remains in `zbtIndexTag`; actual member equality still occurs in the unchanged leaf helper. Equal tags never become proof of member equality. Tombstone/deleted/free-ID checks, ID bounds, leaf-ID assertion, migration ownership checks and all optional outputs remain in their original order. The post-candidate home filter, earliest tombstone insertion hint, empty-slot termination and wrapped probe order are untouched.

B's additional reference change preserves the first true tag/ID match, not merely some later equivalent match. The exact mask enumerates the same true lanes in the same order as the old mask plus byte validation. That matters because reference repair and scan disambiguation use the selected bucket/position. The original boolean empty-byte test remains approximate, which is valid for its existence-only use and introduces no new behavior. The shared reference caller may affect mutation/scan performance even though scan source is unchanged; those guards remain required.

No concrete out-of-bounds access, invalid shift, ownership error, relaxed assertion or optional-output change was found. These source checks do not constitute32-bit or big-endian execution validation.

## Artifact and test audit

Verified all33 listed A artifact checksums and all68 listed B artifact checksums. Both variants' saved original logs report57 native and57 sanitizer tests passing with zero failures. For each variant, all18 native and18 sanitizer fixture JSON objects exactly match the original baseline objects, including owned bytes. The saved supplied output/external oracle results are90,000 and45,000 checks respectively. Those original suites/oracles were inspected from saved evidence, not independently rerun in full during this review.

Independently reran the following existing ASan/UBSan correctness binaries. Every execution returned0, produced the expected passing JSON and had empty stderr:

| Independent rerun | Result |
|---|---|
| A mask oracle | 2,559,808 masks;4,711,764 ordered positions |
| A index oracle | 54 reference checks;21,654 table checks;3,072 optional-output cases;16 migration steps;2 completed resizes |
| B mask oracle | 3,507,872 masks;4,681,407 ordered lanes;987,938 masks expose approximate false candidates |
| B index oracle | 131,584 filter checks;222 hits;24 misses;222 references;126 wrapped hits;111 wide-ID hits;12 tombstone/hint cases;16 migration lookups;4 final resize steps |
| B reference oracle | 4 synthetic repairs;4,668 mutations;28 active-resize updates;3,952 cross-leaf updates |

Both mask tests construct expected results with scalar per-byte equality and independently check complete enumeration order. They cover all query tags, byte values and numeric lanes. Adjacent-byte-pair testing exhausts the XOR-byte domain across all seven boundaries with varied translations/backgrounds; it is not a full all-tag×all-pair Cartesian product. The per-byte proof and explicit XOR translation support that reduction. Long borrow patterns and set high bits are covered. The tests never invoke first-bit extraction on a zero mask.

A's focused index fixture validates all64 combinations of its optional output groups, multiple unsuccessful candidates before hits, folded0/1 tags, wrap/displacement, tombstones and insertion hints. Synthetic chosen hashes are explicitly internal correctness constructions, supplemented by full trees with actual hashes. Its migration tests check old/new ownership exclusivity and narrow/wide-destination completion. B's focused index test additionally includes actual wide IDs above65535 and distinct members sharing a full hash. Its reference test deliberately constructs XOR bytes0,1,0, gives the middle false approximate lane the requested ID, and proves repair changes only the later true tag/ID entry. The negative repair preserves the unrelated entry and output sentinels. This is a meaningful discriminator for B's extra consumer change.

The reference mutation test obtains fresh insertion-position state before score updates, validates the full tree/index after mutations, and exercises cross-leaf moves during resizing, deletion and growth/shrink transitions. There is no new scan-loop implementation in A/B to validate; nevertheless B changes a function used by scan disambiguation, so existing scan tests are relevant and qualified scan traffic must remain in its affected-path performance guards.

Retained noncandidate failures are accurately disclosed: A's initial log redirection lacked its parent directory before qualification began; B's first static output filename named an existing directory and the linker rejected it. Neither is a passing execution or a source-correctness failure. No candidate source was repaired following those setup errors.

## Static findings and gate concerns

The saved local x86-64 GCC13.3 disassembly supports feasibility. A's candidate path atd716 uses first-bit extraction, divides by8, then loads the narrow ID atd71e without extracting/comparing the stored tag byte. B's analogous stable narrow path isdb82→db8a; its reference function also loses the stored-tag check. The leaf calls remain. Both raw prologues retain six saved registers and0x88 stack reservation in the inspected local output; B's paired baseline confirms the same reservation. No out-of-line exact-mask helper appears in the inspected paths.

This is deliberately narrower than passing the ARM gate:

1. The baseline approximate mask has subtract and NOT branches that can proceed in parallel before their AND join. The exact mask imposes AND→ADD→OR→OR→complement after XOR in the observed local lowering. A lower source-operation count or removed branch alone cannot establish a shorter complete home-hit dependency path.
2. Extra exact-mask work is paid on **every visited bucket**, including no-candidate misses. A and B retain approximate boolean vacancy checks; B still adds exact work to reference-finder buckets, affecting repairs and scan collision disambiguation. Miss/resize/scan guards cannot be inferred from hit codegen.
3. Exact ARM native and GCC15/LTO builds must inspect all narrow/wide, stable/resize and actual scored/no-score clones, complete mask construction and raw frame. A dead recheck in one displayed clone does not establish removal everywhere. Apply the registered NONE rules if the recheck persists, the frame grows, or at least four new dependent steps replace the removed chain.
4. Local text size and symbol boundaries are not measurements of instructions/operation or pipeline slots. They do not satisfy≥2% primary or≤1% guard gates. Compiler-generated code layout may still regress guards even with semantically narrow patches.

No additional semantic patch or pre-build source correction is requested. The static concern is a required next gate, not grounds to bypass that gate or predeclare the candidates successful. A remains the chair's stated maintainability preference only if equivalent candidates clear all gates; this review does not select a timing winner.

## Review limits and TMA

This review covers the exact A/B hashes above, not future revisions or own C. It does not establish target compilation,32-bit/big-endian execution, fleet performance, fresh confirmation or source acceptance. All original and affected-path guards remain binding.

| Qualified pipeline slots | ARM baseline | H7-A | H7-B |
|---|---|---|---|
| Frontend_Bound | unavailable: scope/formula qualification unresolved | unavailable: uncollected | unavailable: uncollected |
| Bad_Speculation | unavailable | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable | unavailable |
| Retiring | unavailable | unavailable | unavailable |

Children are unavailable. Separate Intel baseline evidence does not classify either candidate or ARM. No static sequence, hotspot share or counter ratio is substituted for TMA.

Own tool discovery found no callable cpu-perf/library_status endpoint. The controller's actual shared consultation recorded in [H7-selection.md](../H7-selection.md) covers the exact identity, removed checks, consumer scopes and miss risks. Its3/287-source,158-passage library returned an unrelated register/stack-sampling passage, which supports no arithmetic speed claim. This is shared consultation evidence, not a reviewer invocation. The proof, source inspection and correctness tests support the source decision; the performance decision remains pending.
