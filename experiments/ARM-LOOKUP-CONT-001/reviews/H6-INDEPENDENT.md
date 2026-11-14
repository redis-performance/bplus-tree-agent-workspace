# Independent H6 source and ARM code-generation review

2026-11-14. **PASS for the source/identity/static-mechanism screen for A, B and C. No concrete blocker found before the registered discovery measurement. Source adoption remains NONE.** This is not a speed claim, duration qualification or waiver of affected-consumer guards. Native-first discovery and any later compiler/architecture cohort must keep their own qualified controls and original gates.

I did not author any H6 implementation, its focused tests or the descriptor-guard harness. Earlier work in this campaign included the Intel parser and H2 readiness review; neither supplies independent H6 performance evidence. This review inspected source, existing correctness artifacts and exact saved ARM code only. No executable under review was run, no new benchmark/profile or fleet operation occurred, and no source/collector was changed. Only this report was written. Exact model, token usage and cost are unknown.

## Exact identities

All variants derive from baseline C SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, isolated base `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`. I independently reconstructed each retained patch in memory against the baseline and matched it byte-for-byte to the isolated final source and both fleet build metadata records. No H1–H5 patch is stacked.

| Variant | Source SHA256 |
|---|---|
| A | `ffd548a1fba1db452e98fbe1dd3902b2ba34f44af797edeaed9976783444e744` |
| B | `5f6bfd216350dceee6ed486d5fc6e1535162a64c037c3ceee746ceae9b0813ae` |
| C | `bf2cbbe66b36d178692ba214fd192af1b5dc6b1c67f1619e2d782c839b2da825` |

Independently hashed all six supplied ELF files under private `build/arm-cont-private/fleet/bin/`; every hash matches its cohort metadata. All are AArch64 little-endian ELF64. I also parsed their ELF section tables and matched every encoded instruction word in all nine saved leaf-symbol extracts to the corresponding `.text` bytes. This checks that the inspected snippets belong to these exact binaries; it is static byte verification, not a dynamic instruction measurement.

| Variant | Native ELF SHA256 | GCC15/LTO ELF SHA256 |
|---|---|---|
| A | `35e580eeb9c13804abc54db235e11d256a09c48dcc39fd51557169694a764449` | `554c7a80dc42b6063721d60637ea885d8f983c0e2f35a2fd5724476a45106ac8` |
| B | `770aae745abc3ff95820cbac01d54837d8591977f97637a6b68740d4f40c5bfb` | `53ab6151c968b6e8b3822e92bfa30cef2bbf5548b6baab35a439f0e6467082b4` |
| C | `3af61e2ac8203e22a7247ed34b4cb3eaeea057efdd73bfa97d5a109867198b7d` | `3fbc45890344a7bd9983a990180a020e45d3c9bdd2fcacfe33cc1608f7250acf` |

Build commands are retained in private `fleet/H6-{native,lto}/commands.jsonl`: C11, `-O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`, frozen lookup/compat/SipHash sources; LTO adds `-flto=auto` in pinned GCC15.2 image `sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460`. Native uses the campaign's GCC13.3 compiler. Production builds omit debug-only descriptor assertions; their absence on the hinted CFG paths was checked directly.

## Descriptor correctness and consumer audit

All three keep the existing16-bit word, record bytes, score stream, array placement and allocation formulas. Low12 bits encode the record offset. A's nonzero nibble is length+1 for0–14; B's bit15 validates the three-bit length0–7; C's nonzero codes map injectively to0–8,12,16,24,32,64,128. C's table index is bounded by the extracted four-bit code; its code0 table entry is unused by the hinted path. B's writer emits no stray high bits for a generic record.

I enumerated every `zbtScoreLeafOffsets` call, direct offset-array load/store, `uint16_t` array alias and temporary `locations[]` use. The following distinctions are correct:

- `zbtScoreLeafOffset` always returns decoded address bits. Record access, element/hash extraction, ownership free/dismiss, copy/defrag pointer repair, iterator/member consumers, split/merge construction and byte-cost callers inherit that address contract. Direct membership lookup and live-record-byte accounting also mask their own loads.
- Build and fast insertion construct the physical record **before** deriving its hint. All entrypoints that reconstruct leaves reach the builder. The existing usable-capacity clamp remains4095 even when allocator rounding supplies more memory.
- A/B carry complete descriptors in insertion `locations[]`; the new placeholder is replaced by a newly encoded record. C intentionally carries decoded locations and regenerates every descriptor from its already-written record. The insertion capacity check keeps rewritten score/offset/tag arrays below all record bytes, so C's header rereads do not inspect overwritten metadata. Logical-to-physical conversion uses the appropriate old/new count at each stage.
- Deletion decodes the removed address and both address-order comparisons before any arithmetic. Compaction moves only lower-address records upward by the removed record's storage size. Relocation preserves the old high bits and writes the checked new low offset, so addition cannot carry into a hint. Insertion/deletion array moves and reverse-for-pop swaps preserve the entire descriptor word with its tag.
- `record_start` remains a plain offset and is never populated from an encoded descriptor. Whole-leaf duplication and relocation retain relative descriptors, not cached pointers. No overlooked raw descriptor-to-record address or numeric descriptor-order comparison was found.

Every record occupies at least its physical header byte. Therefore a real record within the capped4095-byte allocation starts at most4094, although4095 is representable arithmetically. Range assertions permit the representable maximum; production callers' storage/capacity checks supply the stricter dereference bound. B's synthetic empty record at4095 uses a4096-byte test mapping and is correctly distinguished from its production-cap tests; C tests4095 only as relocation arithmetic.

External representation is selected from the **physical marker**, not logical length. Marker255 and marker254 remain generic in every encoder. In particular an externally allocated short or empty member cannot take `record+1` as payload or bypass the original external full-hash rejection. Existing external ownership transfer still writes the external marker/hash/length/pointer, clears the prior owner's pointer and leaves the marker unchanged. Descriptor creation follows that writer; duplicate/defrag repair only the external pointer through decoded record addresses. The supplied external-short fixtures and source paths support this distinction; natural occurrence of every synthetic collision is not claimed.

No new32-bit pointer-size or64-bit leaf-footprint assumption was found in production changes. The descriptor is explicitly `uint16_t`; code shifts fit16 bits and intermediate32-bit arithmetic; masked offsets and relocation sums stay within4095 under the existing movement bounds. C's `unsigned int` offset and A/B's `size_t` parameters are sufficient on supported32-bit targets. Signed integer promotion of B/C's `~0x0fff` mask preserves the intended upper four bits after combination. Native-endian16-bit offsets and original packed/external byte handling are unchanged. **Actual32-bit and big-endian execution remain unvalidated**; these source observations are not portability certification.

## Actual ARM call paths

Native `zbtreeScoreRaw`, `zbtreeScoreRawWithHash` and `zbtreeScores` call `.constprop.0`; `zbtreeFindForAdd`, `zbtreeRank` and `zbtreeDelete` call the generic helper. Both native clones were inspected, not just an unused standalone symbol. LTO retains one leaf helper called by the raw lookup variants and find-for-add. All nine leaf symbols allocate128-byte frames. The inspected native raw function and both LTO raw variants allocate176-byte frames.

The table identifies descriptor load, hint branch, generic record-header load bypassed by that branch, and the existing bounded `memcmp` call. Each path masks the address with `0xfff` before forming a record pointer.

| Variant/cohort symbol | Descriptor | Hint branch | Generic header load | `memcmp` |
|---|---:|---:|---:|---:|
| A native constprop | `32fc` | `330c`→`32c0` | `3310` | `3344` |
| A native generic | `3490` | `34a0`→`3454` | `34a4` | `34d8` |
| A LTO | `403374` | `403384`→`403338` | `403388` | `4033bc` |
| B native constprop | `310c` | `3118` generic-only branch | `30b4` | `3134` |
| B native generic | `34bc` | `34c8` generic-only branch | `3464` | `34e4` |
| B LTO | `404d50` | `404d5c` generic-only branch | `404cf8` | `404d78` |
| C native constprop | `38a0` | `38b0`→`3864` | `38b4` | `38ec` |
| C native generic | `3a30` | `3a40`→`39f4` | `3a44` | `3a7c` |
| C LTO | `403380` | `403390`→`403344` | `403394` | `4033cc` |

A decodes by code−1; B tests bit15 and uses `ubfx` for bits12–14; C loads a byte from its16-byte constant codebook. All hinted paths compare the query length before the unchanged `memcmp` and do not execute the generic record-header load. Generic paths retain marker handling and external full-hash filtering. `memchr`, the out-of-line leaf boundary and successful score/position mapping remain. C still has a dependent table load and spills the hash for its generic path; it is not a load-free implementation. These facts establish the preregistered static mechanism, not which variant is fastest.

## Correctness evidence and pending gates

I checked the saved final logs: each variant has57 native and57 sanitizer upstream passes,18+18 verified fixture cells and90,000+45,000 passing optional-output/external checks. Top-level final focused runtime stderr is empty. The focused tests inspect actual header/descriptor agreement, same-tag byte/length mismatches, external short records, empty/binary input, optional outputs, reversal, protected-page boundaries, near-capacity records and mutation/relocation paths. Final records report A796,816 invariant checks and11,272 comparisons in both modes; B739,144 descriptor checks,1,640 lookup checks and113 relocations per mode; C1,414,196 boundary checks per mode plus its separate mutation oracle. Earlier failed/subset fixtures remain preserved and were not counted as final passes.

I inspected the focused test sources where their assumptions matter and did not rerun or mirror these large suites. This review is independent source/evidence inspection, not a new independently randomized runtime campaign. Test counters do not prove exhaustive branch or mutation-history coverage. Debug checks intentionally read record headers; production mechanism validation comes from the separate exact O3 ARM binaries above.

The separately reviewed [descriptor guard harness](DESCRIPTOR-GUARDS-INDEPENDENT.md) covers member iteration and mixed/boundary inline/external lookup. Its reviewer authored H6-B but did not author that harness; it is independent harness review, not an independent source review of B. Its GO permits freeze and its own fleet qualification, not automatic acceptance of H6.

Before adoption, require the original primary/guards/memory gates, separately qualified affected-member/descriptor guards, fresh held-out confirmation, Intel portability and matched profiles. Score-only iterator guards cannot measure the new address-mask cost. Lookup hints may tax generic/long/external misses and writes; C also regenerates all descriptors on re-encoding insertion. None of these costs may be averaged away or excused by a short-hit gain. A missing or restored header dependency in another exact cohort invalidates that cohort's mechanism screen.

## TMA and consultation

| Qualified total-slot category | ARM baseline | H6-A | H6-B | H6-C |
|---|---|---|---|---|
| Frontend_Bound | unavailable | unavailable | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable | unavailable | unavailable |
| Retiring | unavailable | unavailable | unavailable | unavailable |

No qualified H6 matched pipeline capture exists in this review; children are unavailable. Static dependency/stack inspection is not TMA, and Intel baseline fractions cannot supply ARM candidate categories.

Own current tool discovery exposed no cpu-perf `library_status`/`ask`. I read the controller's actual shared descriptor-specific request and library response in private `descriptor-consult/{ask,library_status}.json`: bundled revision `deb5a0bac467`,3/287 sources indexed,158 passages; no supporting passage establishes a gain. Those calls belong to the controller. This review relies on the inspected source, saved correctness evidence and exact ARM code, with no unsupported source-authority or causal performance claim.
