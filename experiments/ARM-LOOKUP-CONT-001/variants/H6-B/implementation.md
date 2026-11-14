# H6-B: exact inline lengths in record descriptors

The H6-B implementer encoded physically inline lengths 0–7 in existing 16-bit record-offset entries: bit 15 is valid, bits 12–14 contain the length, and the low 12 bits contain the offset. Writers derive hints from completed records. Unhinted records retain the original decoder and external full-hash check. The tag scanner, byte comparator, leaf helper boundary, hashing, packed score stream, fixed score-data address and external ownership code are unchanged.

Correctness passes and the intended mechanism is present in the inspected local GCC 13.3 non-LTO O3 ELF. This is ready for independent target code-generation review; it is not performance acceptance. No local or fleet timings, profiles or instruction measurements were collected. No other H6 implementation was read, and no H1–H5 changes were stacked.

Source SHA-256: `5f6bfd216350dceee6ed486d5fc6e1535162a64c037c3ceee746ceae9b0813ae`.

Patch SHA-256: `88f0e6e6306c5befdfc2414e14c2c8b529ecddaa8c6d3dd7f40e8da38332fc94`.

## Representation and mutation audit

| Consumer or writer | Contract |
|---|---|
| Descriptor accessors | Named valid-bit, length and low-offset accessors; compile-time leaf-cap bound; range assertions on encoding and relocation. The logical-position descriptor accessor retains all bits, while the existing offset accessor returns only low address bits. |
| Leaf record access and lookup | Record pointers mask descriptors. Debug assertions check hinted length against the actual inline header. Hinted tag matches use the cached length, then the original bounded `memcmp`; generic records retain their original decoder and external full-hash rejection. |
| Build | The descriptor store follows `zbtBuildElementWrite`, so hint construction cannot read an uninitialized record header. Allocation and usable-capacity clamping remain unchanged. |
| Fast insertion | Existing descriptors move intact with the original `memmove`s; the new descriptor is encoded after the new record is written. |
| In-place score repacking/insertion | Temporary `locations` now contains intact descriptors in logical order. Existing hints survive rewritten packed-score metadata; only the newly inserted record is encoded. |
| Live-byte accounting | Decodes offsets before calculating record addresses. |
| Delete and compact | Decodes the deleted record address and all address comparisons. Relocation updates low address bits through a checked helper while retaining the old hint. Arithmetic cannot carry into the length field. |
| Reverse and trimming | Reverse swaps entire descriptor entries. Range trimming rebuilds through the audited builder; the focused oracle also exercises range deletion and both edge-pop directions. |
| Split, merge and rebuild | Existing build entries preserve physical external ownership. All reconstructed records receive fresh descriptors through the builder. Original split and merge bodies are unchanged. |
| Duplication and defrag | Byte copies preserve relative descriptors; moved leaves remain addressed relative to their new base. External-pointer repair uses the masked record accessor and original ownership logic. |

`scope-audit.json` lists every direct descriptor/temporary-array site and verifies byte-identical bodies for 23 protected functions, including score encoding accessors, packed decoder/writer, full-hash helper, generic table/index finders, raw APIs, split selection, compact/merge, reverse, duplicate and defrag. The entire source prefix before the new descriptor helpers is unchanged, including structure layout and score metadata addressing. Production changes are confined to the one authorized C file. Referees remain unchanged.

## Correctness

| Check | Result |
|---|---|
| Original suite | 57 native +57 ASan/UBSan tests pass. |
| Frozen fixture verifier | 18 native +18 sanitizer cells pass. |
| Supplied output oracles | 90,000 ordinary/long +45,000 external checks pass under ASan/UBSan. |
| Focused descriptor oracle, each mode | 739,144 descriptor checks; 1,640 guarded lookup/output checks; 1,549 tree invariant sweeps; 113 allocation relocations; all eight hinted codes; one explicitly successful merge. |
| Capacity and boundary checks | Actual maximum record offset 4094; synthetic representable offset 4095; all relocation offsets 0–4095; 6,581 native observations of allocator capacity above the 4095 cap. ASan allocations are exact and have no such rounding. |

The focused oracle covers lengths 0–9, 14, 15, 16, 24, 32, 64, 128, 253, 254, 255, 319, 320, 321 and 384; binary data and empty strings; same-tag byte and length mismatches; same-tag/different-full-hash rejection for external records; score/position optional-output combinations and unchanged miss sentinels; exact signed zero; both physical leaf orders; unaligned records and query pointers; and record/query ends followed by protected pages. A deliberately synthetic empty record at offset 4095 tests descriptor representability; production writers are separately checked against the actual allocation cap and attain offset 4094.

Actual externally owned lengths 0–8 are constructed through the existing writer, compacted, duplicated and freed. Every resulting descriptor remains generic, the physical marker remains external, and different full hashes are rejected despite equal tags and bytes. The mutation fixture checks every live descriptor against its actual record after inserts, score changes, explicit compaction, duplication, active-resize defrag, deletes, range removal and both edge pops. Direct fixtures force successful fast insertion, score-width-changing in-place insertion, edge-leaf creation and merge. The original suite additionally exercises late-widening splits, batch append, iteration and index collisions. Normal allocator rounding above 4095 is observed while all actual record extents remain within the capped capacity.

Two focused-fixture failures are preserved. `failed-attempt-1` requested an impossible inline 320-byte record and hit the unchanged writer's length assertion. The fixture now uses the required external representation for lengths at or above 320. `failed-attempt-2` assumed an eligible adjacent merge pair would remain after natural deletion; all attempted pairs returned NULL, so the fixture assertion failed. A separate fixture now deliberately creates two small adjacent leaves and asserts successful merge. Neither failure required a production-source change. Final native/sanitizer compiler and runtime stderr logs are empty. `initial-focused-pass` retains the earlier passing subset; final logs supersede its counts.

`run-correctness.sh` reproduces the final validation. These tests do not enumerate every operation interleaving or establish performance of affected member-address consumers. Exact target compiler testing and the separately frozen boundary/mixed-length/iterator/update guards remain required before adoption.

## Static code generation

The local executable was built with `cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3`, current source/compat/vendor include paths, `lookup.c`, current target C, `standalone.c`, `siphash.c`, and `-lm`; it was not executed. Compiler: Ubuntu GCC 13.3.0. Disassembly and symbol sizes are preserved in `local-O3-*-assembly.txt` and `local-O3-symbols.txt`.

In `zbtScoreLeafFindMember.constprop.0`, the descriptor load at 0x3ac6 is followed by the offset mask at 0x3ace and valid-bit branch at 0x3ada. Hinted records extract length at 0x3adc/0x3ae4 and compare it at 0x3ae7, reaching the original `memcmp` at 0x3afd without loading the record header. The header load at 0x3a68 is confined to the unhinted branch. The generic helper has the same separation at 0x3e76/0x3e8a/0x3e8c through `memcmp` at 0x3ead; its unhinted header load is at 0x3e18. The helper boundary and `memchr` call remain. Constprop and generic symbol sizes are 433 and 449 bytes respectively; these are static sizes, not measured execution costs. Exact ARM/LTO code generation remains uninspected by this implementer.

## Consultation and TMA classification

Own tool-name discovery found no CPU-perf or library-status tools. The controller actually performed the shared descriptor-specific stdio consultation, preserved in ignored `descriptor-consult/{ask,library_status}.json`; these are shared calls, not invocations by this implementer. Its bundled library revision is deb5a0bac467, with 3/287 sources indexed and 158 passages. No supporting primary passage was retrieved. The source and static assembly support mechanism plausibility only. Backend identity and unknown token/currency accounting remain in the ignored private participant record.

| TMA category | Qualified ARM baseline | H6-B candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Qualified ARM pipeline-slot collection is unavailable; no candidate profile or validated child categories were collected. Existing Intel baseline categories are separate and cannot explain an ARM effect. Static instruction structure and sampled hotspot shares are not pipeline-slot measurements.

No commit, push, fleet operation or source adoption was performed. Correctness and controller static feasibility are complete; performance selection remains pending the parent campaign's target-specific gates.
