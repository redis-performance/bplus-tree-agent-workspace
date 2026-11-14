# Population 3 — record classification on the lookup dependency path

Independent dependency/record-path proposal, 2026-11-14 03:02 UTC. Proposal only: no implementation, build, measurement or fleet access. No other population3 draft was read. The participant previously implemented H2-B, H3-C, H4-C, H5-C and H6-C; this is an independent proposal relative to the other population3 proposers, not an independent acceptance review of those implementations. Detailed backend accounting remains private; token/cost usage is unknown.

**Nomination: classify the packed record's representation once, using the existing contiguous ordinary-inline range, before the reserved-record handling.** Keep the original variable-length `memcmp`, tag `memchr`, leaf helper boundary, record bytes and metadata layout. This is a small, falsifiable opportunity with modest confidence; the removed branch may not earn the2% gate. Prefer completing H2-B's acceptance work and evaluating the already-prepared H6 population over assuming this new spelling is valuable. `NONE` is appropriate if the exact compilers recreate the old classification chain or the fallback costs make the change unattractive.

## Baseline and exclusions from previous results

Each prospective implementation starts the original e13d9fc88 extraction, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, freshly confirmed unchanged by the controller. Inspected C SHA256 is `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. Do not layer H1–H6 patches, even if an earlier candidate is eligible.

Read the current STATUS, H1 results, H2 original/target and supplemental decisions, H3 final results, H4/H5 native decisions, and H6 selection. Their implications are concrete:

- H1 inlining increased raw frame/state and failed score/miss/update guards; this proposal does not inline the leaf search or duplicate a membership scanner.
- H2-B remains eligible and unadopted; H2-A loses memory and H2-C loses score-only iteration by20–25%. This proposal adds no cache, padding field, offset flag, array reordering or changed score address.
- H3 A/B have real short-hit gains but fail Intel long/external guards; B also loses the target external guard. This proposal does not add a length0–8 comparator or remove `memcmp`. Those fallback failures make even one added marker branch a material risk here.
- H4-B's query-mask boundary survives native screening while A/C fail miss; H5-A's raw-resize boundary survives while B/C do not. Query-mask work, probing and resize state remain untouched.
- H6 stores exact inline lengths in offset descriptors and has correctness/codegen evidence; timing is pending. This proposal still loads the actual record header and changes only its classification, so it neither retries nor stacks H6.

## Exact dependency evidence

Current source `current/src/zset_btree.c:1302` finds a leaf tag with `memchr`, loads its16-bit record offset, and obtains the record header. At1302–1340 it first tests whether that header is255 to reject an external full-hash mismatch, then calls `zbtPackedData`. The decoder at586 tests the same header's ordinary-inline range, marker254, or external form. The compiler eliminates duplicate header loads, but retains two representation decisions on an ordinary-inline hit.

The ordinary-inline domain is **all existing record headers0–253**, not a measured fixture length. Header254 selects the existing16-bit inline length, and255 selects external hash/length/pointer. The contiguous0–253 domain therefore has a single unsigned range test. No inference about query length or leaf contents is necessary.

Exact ARM native ELF SHA256 `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf`; saved assembly `build/arm-cont-private/fleet/native-profile/assembly.stdout`, SHA256 `6cfa41d17795ee7026a8f3cbcdd923576ddfba49673601139692e9d6c8960238`:

```text
zbtScoreLeafFindMember.constprop.0
37e0  ldrh w0,[x0,x23]          record offset
37e4  add  x2,x19,x0            record address
37e8  ldrb w0,[x19,x0]          actual record header
37ec  cmp  w0,#0xff
37f0  b.eq 3794                external hash/pointer/length path
37f4  cmp  w0,#0xfe
37f8  b.eq 3854                extended inline length path
37fc  mov  w1,w0               ordinary-inline length
3800  add  x0,x2,#1            ordinary-inline payload
3804  cmp  x22,x1              query length check
3808  b.ne 37b4
3814  bl   memcmp@plt
```

The ordinary-inline path's representation decisions at37ec–37f8 are the target. Its record address/header load dependency remains. The existing external path begins3794 with its stored32-bit hash comparison, and asserts a nonnull external pointer before the length comparison. The proposed change must preserve that sequence's semantics. The128-byte leaf frame and176-byte raw frame are baseline static facts, not an attributed bottleneck.

Exact Intel native ELF SHA256 `2a38b93b94cfc59b347defaa3ccb5560f6bb7a70fbad92f350fbc5d74e00aebd`, `intel-fleet/H2-profile-native-base/assembly.stdout` SHA256 `4154b62129d4c449eb4fcd1c6a52b72a5829ba4405785078cb5d8ee9f8e2c710`, has the same surviving chain:

```text
3f83 movzbl (%rax),%edx
3f86 cmp $0xff,%dl
3f89 je 3f28                   external handling
3f8b lea 0x1(%rax),%rdi
3f8f cmp $0xfe,%dl
3f92 jne 3f41                  ordinary length comparison
3f94 movzwl 0x1(%rax),%edx     extended length
3fb8 call memcmp@plt
```

Thus this is not a source-only duplicate-load claim: both inspected native backends retain two marker comparisons. No claim is yet made that the target GCC15/LTO compiler will retain or remove either proposed spelling; exact target codegen is a required admission gate.

The matched ARM baseline sample report assigns41.38% of whole-process user-cycle sample period to the leaf helper and21.77% to raw lookup, with2.82% in the named libc `memcmp` symbol. These shares locate the relevant routine, not the cost of its two comparisons. The Intel native baseline sample assigns29.33% to the leaf helper and21.38% to raw lookup. Neither profile measures how frequently ordinary/extended/external paths occur among all candidate tags, nor isolates marker-branch cost. There is no branch-miss attribution to these PCs.

## One hypothesis and three implementation choices

**Hypothesis:** moving the ordinary-inline range decision ahead of external rejection permits one common-case representation decision, shortening the dependent header-to-length decision path without importing byte comparison or score machinery. Enough surrounding branch/register work must disappear in the exact compiler output to plausibly earn2% overall; assembly presence alone is not evidence of that magnitude.

All choices preserve one tag traversal, the successful-match/output block, hash/zero-tag behavior, allocation sizes, and existing record format. No query-length dispatch is placed before a candidate record exists. Options are independent source spellings of this one classification hypothesis:

| Choice | Source shape | Reviewable distinction and principal risk |
|---|---|---|
| D1 — local range-first decode, preferred | Within `zbtScoreLeafFindMember`, read the header. For `< ZBT_PACKED_SHORT`, derive existing length/header+1 payload directly. Otherwise retain external full-hash rejection and call the unchanged generic `zbtPackedData`. Then run the original length/`memcmp` condition and original outputs. | Smallest affected surface; extended/external parsing remains in the existing decoder. It repeats the ordinary-inline decoder's two assignments in the lookup helper, but does not copy a scanner. Compiler range propagation must remove redundant rare-path classification. |
| D2 — lookup-only checked decoder | Factor only the candidate-record interpretation into a small pure internal helper returning success plus payload/length. Switch on the actual byte:254 uses the original extended decoder;255 checks the full hash before the original external decoder; default handles the complete0–253 range. The leaf loop retains equality and outputs. | Tests a different compiler CFG and keeps the record rules together. The helper must disappear into the existing leaf routine naturally; a new runtime boundary, indirect jump table, or two common-path equality tests makes it ineligible. Do not force the whole leaf/index path inline to rescue it. |
| D3 — shared decoder with optional hash validation | Factor `zbtPackedData` through one internal range-first decoder accepting an optional expected-hash pointer. Its ordinary branch is unchanged; only its external arm performs the optional full-hash rejection before pointer/length decode. Existing generic callers pass literal NULL; lookup passes its hash and consumes an explicit reject result. The original wrapper remains for callers without hash validation. | Avoids maintaining two copies of even the ordinary decode, but touches a shared abstraction and can expand nonlookup code. It must preserve the generic external-pointer assertion and permit rejection only for an actual external hash mismatch. Require constant optional-argument elimination in ordinary callers; otherwise reject this option rather than accepting broader iterator cost. |

D1 is the preferred maintainability candidate. D2 is not assumed to compile differently; retaining the same two comparisons is an explicit losing artifact. D3 has a higher review burden and may correctly be `NONE` at static review. Do not add a new comparator, offset hints, cold outlining, an ID cache, branch hints, assumptions or compiler barriers to rescue any option.

## Static admission and falsification

Freeze each source and inspect native ARM, target GCC15/LTO and Intel emitted lookup code before timing. Preserve rejected artifacts and compiler versions.

1. An actual ordinary-inline tag match must reach length comparison through **one representation classifier**, with one original header load and the unchanged bounded `memcmp`. The proof must hold for the whole0–253 header range. A source range test that compiles back to `==255`, then `==254` fails the mechanism gate.
2. Keep the original leaf call boundary and one memchr loop. No copied probe loop, membership-specific equality body, runtime optional-decoder call, indirect dispatch table, score-path import or record-layout change.
3. Count and document the **extended/external control path separately**. A three-way classification cannot generally make all three representations first: range-first can add a representation decision to external hits relative to the baseline's first255 test. That tax is real, not compiler noise to waive. Reject an implementation with redundant further marker checks, extra hash work, new spills/frame growth, or a decoded-pointer load before external-hash rejection. A single extra fallback decision may still enter measurement if explicitly recorded; the1% guard is binding.
4. D3's no-hash callers must retain their original decode semantics without a dynamic optional-hash test or additional boundary. Check scored/member iteration, rank-with-member output, build/rebuild and scan callers, not only raw lookup.
5. Tree-owned memory must remain exactly unchanged. Text size is separate: record it and reject disproportionate growth for this tiny mechanism. No speculative overread of record headers, payloads or external pointers.

The expected gain is modest and uncertain. These tests cannot establish2%; all three implementations may be correctly rejected before or after timing. If a candidate passes primary but repeats H3's long/external regressions, reject it without shrinking its length range or stacking another patch after observing the failure.

## Correctness and guard predictions

Retain57 native and57 sanitizer tests,36 frozen fixture cells and135k supplied output/external oracle checks. Additional correctness must exercise every ordinary header0–253, marker254 inline lengths254/255/256/319, and marker255 external records at320/384 plus externally represented short/empty members. Query length never proves record representation. Test same-tag and full-hash collisions, different-length equal prefixes, binary zero/high bytes, mismatches at each position, zero-length payload with no byte access, and unaligned/guard-ended header/payload storage. Preserve external hash rejection **before** pointer validation or dereference: a moved-out/null-pointer external record rejected by hash must not newly assert. On accepted external records, the existing nonnull assertion remains.

Exercise all score/position output combinations, reversed physical order, empty/full/singleton leaves, insertion/deletion/repacking/split/merge, duplication and defrag. No persistent metadata invariant is added, but all these operations create representations consumed by the changed branch.

| Workload/guard | Prediction and rejection risk |
|---|---|
| Short hit and scored hit | Same representation saving before unchanged equality; membership receives no special advantage. A measurable gain is plausible, but one classifier may be too little for2%. |
| Miss | No-tag misses should execute no new work; same-tag misses can save ordinary-inline classification. Code layout can still regress raw/index work. Keep the existing miss bound and add a collision-rich miss cell. |
| Inline256 / external384 | Most exposed adverse cases. Both bypass the ordinary range; external may pay an additional classifier. These guards cannot be replaced by shorter records or averaged with hit gains. |
| Update and churn | Lookup portion may benefit; decoded-record consumers and shared helper codegen may regress, particularly D3. No mutation work is removed. |
| Score-only forward/reverse iteration and rank | D1/D2 do not change their source path, so near-neutral is the expectation; D3's shared decoder requires explicit assembly checks. Existing five supplemental guards remain mandatory. |
| Member-returning iteration/scan, mixed representation, same-tag collisions | Affected-path guards needed for D3 and useful for all variants. These expose decoder overhead and representation transitions hidden by ordinary score-only guards. Freeze their fixtures/work before timing and qualify their controls independently. |
| Active/final resize, narrow/wide IDs, displaced buckets | No index algorithm change expected; retain correctness and affected-path guard coverage because all eventually enter the leaf helper. |

Existing acceptance remains≥2% primary improvement in every registered discovery block and≤1% regression in every guard/memory block, with qualified A/A and≥250ms windows. Intel portability requires its own≤1% guards. Heldout seeds, matched profiles and independent review precede any adoption. No local measurements or server-command claim is proposed.

## Other dependency mechanisms screened, not nominated here

Two concrete alternatives were considered to avoid simply repeating H1–H6. They are separate hypotheses and must not be folded into this experiment.

**Exact bucket equality mask:** `zbtIndexTagMask` at1858 uses borrow-propagating zero detection and therefore the candidate loop at1983 must recheck its tag byte. Native ARM atc4a0–c4ac performs a variable shift, compare and branch before loading the leaf ID. A scalar exact per-byte-zero mask can use `~(((x & 0x7f7f7f7f7f7f7f7f) + 0x7f7f7f7f7f7f7f7f) | x | 0x7f7f7f7f7f7f7f7f)` for `x=tags^repeated_tag`, avoiding the false-positive recheck. This adds mask-construction work to **every bucket**, including no-match misses, while saving work only on candidates. It also has shared scan/reference callers and folded-zero/endianness obligations. No dynamic candidate/probe census presently supports the tradeoff; recommend a separate proposal/consultation only if the chair judges that evidence sufficient, otherwise `NONE`. Do not silently change the leaf memchr scanner or revive the historical vector/SWAR leaf scan.

**Direct member-position hint in index entries:** a valid hint would remove the leaf tag scan and dependent offset selection, but the current32/48-byte buckets have no general spare position field. Narrow IDs must retain their full valid range, including delayed widening; adding fields grows memory, reducing ID bits triggers earlier widening, and hint repair or validation taxes mutations/collisions. No whole-dataset≤1% memory and mutation-cost case is established. Do not implement it merely because the500-member fixture has small leaf IDs. `NONE` without a separately preregistered representation, memory calculation and mutation policy.

These rejected leads explain why a small record-classification experiment is the current dependency nomination despite its limited expected gain. Bounds-check removal, low-bit pointer tagging, memoized query results and fixture-specific encodings are not substitutes for a proven invariant and are not proposed.

## TMA classification and consultation

ARM baseline and new-candidate Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring are **unavailable** as qualified slot categories; children are unavailable. Existing ARM CPU-wide exploratory output and symbol percentages are not converted into those categories.

The separately qualified matched Intel baseline reused for inspection has these roots, from the hardened raw analysis documented in [H2 profile/guard audit](../reviews/H2-PROFILE-GUARD-AUDIT.md):

| Pipeline Slots (100%) | Intel native baseline | Intel GCC15/LTO baseline | New candidate |
|---|---:|---:|---|
| Frontend_Bound | 3.100% | 5.387% | unavailable |
| Bad_Speculation | 6.033% | 6.833% | unavailable |
| Backend_Bound | 20.427% | 21.533% | unavailable |
| Retiring | 70.440% | 66.253% | unavailable |

Baseline measured children, all shares of total slots, native/LTO: Fetch_Latency0.727/0.700%; Fetch_Bandwidth2.373/4.673%; Branch_Mispredicts5.927/6.680%; Machine_Clears0.107/0.133%; Memory_Bound0.800/0.800%; Core_Bound19.627/20.733%; Light_Operations67.680/63.107%; Heavy_Operations2.727/3.073%. Other memory levels are uncollected. Roots preserve displayed rounding residuals. These are unweighted means of15 intervals per binary, CPU2-wide with≤1% aggregate workload tick-accounting error,100% scheduling, CPU50 offline at endpoints and controller CPU0. Scope, exact binaries, collector/model versions, raw checksum anchors and limitations are in the linked audit. No H2-B candidate fraction is transferred to this proposed change, and Intel is not evidence of an ARM pipeline cause.

Own session tool-catalog discovery at proposal start found no directly callable `cpu-perf` or `library_status` tools. Consumed [SCREEN-CONSULT.md](../SCREEN-CONSULT.md) as the controller's **shared actual consultation**, not this worker's call: discovery/library_status/ask covered the preceding results and guard failures, with3/287 sources,158 passages, keyword retrieval and no matching supporting passage. That screen consultation did not establish this new range-first mechanism. The controller will make an actual mechanism-specific consultation before selection; the question should include the exact paired marker tests above, the unavoidable external-classifier tradeoff, H3's fallback failures and the unchanged memcmp requirement. External source claims remain unsupported; the evidence here is inspected source/assembly plus the limited scope of existing profiles.
