# H7-B/C ARM emitted-code admission review

**Decision: B = NONE; C = NONE.** Both fail the literal target static gate in [H7-selection.md](../H7-selection.md): the GCC15/LTO general `zbtreeScoreRaw` frame grows from176 to192 bytes. The no-score clones remain176 bytes, but the gate covers the actual raw readers, not only the primary clone. Native frame/mask checks pass in isolation; that does not admit either variant to timing. No source rescue or flag change is proposed.

Role: independent reviewer of B/C. The reviewer implemented H7-A and does not review A here. This is an offline source/disassembly/ELF audit, not a performance measurement or repeat of source correctness. No workload was run, no fleet was accessed, and no source or timing script was changed. A change in runner isolation or new baseline qualification cannot waive this static rejection.

## Identity and byte validation

The unchanged baseline is upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, extraction `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, source `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. Rehashed isolated B/C sources match both native/LTO build metadata: B `ce8ed5476d5b04953e514a1a798947272a4ab2846034d417fe1e7e0b25e080eb`; C `fa45c5d7bdd04f37bd448a48b573ef92128b56ed35df9d176659d9ddd00ca5d9`. Their [B patch](../variants/H7-B/candidate.patch) and [C patch](../variants/H7-C/source.patch) have the selected independent scopes.

All six saved actual ELF hashes match the build metadata. Independently parsed ELF64 program headers and mapped every four-byte instruction word in each saved disassembly back to its PT_LOAD file offset. All96739 words match byte-for-byte; zero mismatches. This validates the disassembly against the actual saved binaries, rather than trusting a compiler listing. The source/build association is the retained source hashes and build metadata, not a claim that source identity can be inferred solely from machine instructions.

| Cohort / artifact | Actual ELF SHA-256 | Matched words |
|---|---|---:|
| native base | `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf` | 20264 |
| native B | `e4a0200d3b20d6232c1c88deee9906a1ebed5e265f952086e78f9191459825bc` | 20260 |
| native C | `cf2f40a8775fe1c8826cd226d466f746dee177dd94a86106ca8c0b081a3add16` | 20276 |
| lto base | `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb` | 12025 |
| lto B | `00aebca89d60776b228f4068f797975a5c087c58a9cdcbb20c855b8588c2bb09` | 11961 |
| lto C | `be6a094effd3cac02398d507e78c1f3821d4c29f37e4902b5a675dd4ea4f3953` | 11953 |

Candidate assembly names below identify the archived capture by cohort/variant; PCs and one-based line numbers refer to its complete `assembly-B.stdout` or `assembly-C.stdout`, including the leading header. Original assembly SHA-256 anchors:

| Capture | Assembly SHA-256 |
|---|---|
| native base | `6e71c5dbba16d8192449f76513b16ccaafd92bfd57f62a9dc499a1904fa242a0` |
| native B | `14ea796d8eff075d49d7b1114f7ac693391253bef758807091f54cac460e688c` |
| native C | `d0710ec33d648bb2abb85fd6f2372fb8edc00d7398a57de561a4a3f4cbe4cb9a` |
| lto base | `d7a70495c2fa10cc5c5238a605bffc5c464c7a708001244225a7d85fdf840d40` |
| lto B | `59680d9e45a487492f56474d3886eb7deff2c886be268be10a53c5a32d89c87f` |
| lto C | `d551ae657c1d6b77f87421d082ede667561167d3508cf25c6dca1ef68e1a5438` |

Baseline line references use the published [native](../H2-profiles/arm-native-base/assembly.stdout) and [GCC15/LTO](../H2-profiles/arm-gcc15-lto-base/assembly.stdout) matched captures. Private provenance retains the verification records and exact archived locations; no machine identity is needed for the static decision.

## Decisive frame gate

| Reader | Baseline entry / frame | B entry / frame / line | C entry / frame / line |
|---|---|---|---|
| Native raw | `c1c0` /176 | `c350` /176 /11986 | `c390` /176 /12002 |
| Native prehashed raw | `c9b4` /176 | `cb54` /176 /12503 | `cb94` /176 /12519 |
| LTO general raw | `405f20` /176, baseline line5642 | `405f00` /192 /5634 | `405f00` /192 /5634 |
| LTO no-score clone | `406820` /176 | `4067a0` /176 /6188 | `4067a0` /176 /6188 |

The target instruction is `a9b47bfd stp x29,x30,[sp,#-192]!`; baseline is `a9b57bfd ... #-176`. This is actual allocated stack growth, not inferred register pressure. Candidate general readers also use `[sp,#184]` at `405fc0` (line5682), within the expanded frame. The complete raw functions have no other stack subtraction that could reverse this conclusion. The saved LTO lookup ELF does not retain a separate prehashed-raw symbol; the general and no-score raw functions are both inspected. Keeping the clone small does not excuse the general reader.

## Exact mask and candidate chain

Both variants naturally inline the exact mask. No new mask-helper call is emitted. Every raw function has four materializations covering narrow/wide and current/rehash table paths. Native has two raw functions, and LTO has general plus no-score; all32 candidate materializations across B/C and both cohorts were inspected. They use the same six-operation sequence:

```
eor x, tags, broadcast
and t, x, #0x7f7f7f7f7f7f7f7f
add t, t, low
orr t, t, x
orr t, t, low
mvn matches, t
```

The zero-mask branch precedes first-bit extraction. `rbit; clz; lsr #3` then goes directly to the slot offset and existing16-/32-bit ID load. The baseline dependent `lsl` of the candidate position, variable `lsr` of stored tags, byte `cmp`, and rejection branch are absent from all these paths. For example native baseline `c4a0–c4ac` (lines12070–12073) disappears between B `c628` and `c630` (lines12168–12170). LTO no-score baseline `406ac8–406ad4` disappears before B/C `406a34` (line6353). Remaining immediate shifts, ID/tombstone comparisons, leaf-ID assertion, free-pointer tests, migration tests, leaf equality and optional outputs are required semantics, not leftover tag rechecks.

| Capture / reader | All mask-start PCs (EOR), with line numbers |
|---|---|
| Native B raw | `c458`12052; `c604`12159; `c7f8`12284; `c9c4`12399 |
| Native B prehashed | `cc48`12564; `cdf4`12671; `cfe8`12796; `d1b4`12911 |
| Native C raw | `c498`12068; `c644`12175; `c838`12300; `ca04`12415 |
| Native C prehashed | `cc88`12580; `ce34`12687; `d028`12812; `d1f4`12927 |
| LTO B and C general | `405fd8`5688; `406140`5778; `406448`5972; `40657c`6049 |
| LTO B and C no-score | `406870`6240; `406a08`6342; `406c78`6498; `406e44`6613 |

The source retains the original bucket tag load and ID widths. The raw exact helper contains no memory access. Thus it adds no new overread. Native B current narrow example: bucket64-bit load `c5f8`, exact arithmetic `c604–c618`, ID halfword load `c630`, bounds/free-ID/leaf-ID checks `c63c–c664`, resize checks `c668–c688`, original leaf call `c6a0`. All four table paths retain those protections.

### Added work, not total work

The mask's six arithmetic instructions are **not six new instructions**. Baseline narrow paths use five: EOR/EON/ADD/AND/ANDS; EOR and EON can begin independently. Baseline wide paths use four: EOR/ADD/BIC/ANDS. The exact sequence therefore adds **one arithmetic operation narrow and two wide** per visited bucket. Its longest register-dependency chain is six stages versus four in both baseline forms: **two added dependent stages**, not four or six. Removing the four candidate recheck steps therefore clears that particular static rejection condition. This is a dependency-graph count, not a claim about measured instruction latency or branch speculation.

Constant construction also matters: the original subtraction constant generally needs MOV+MOVK, whereas the exact low-seven mask is one logical-immediate MOV. In the raw blocks this offsets one of the added arithmetic instructions. Broadcast multiplication and bucket/address work remain; stack loads, spills, argument moves and layout changes must not be hidden inside a simplistic “four instructions saved” claim. Native current narrow B reloads the bucket base at `c5f0` where the baseline retained it in a register. The LTO general frame expansion is direct evidence that register allocation changed materially.

No-match and false-candidate paths pay the complete exact mask per bucket, with no successful-candidate recheck to remove. Exact masks also suppress baseline borrow-induced false candidates, whose frequency is not established by this static audit. Probe advancement, home negative-filter computation/placement, empty-slot and tombstone semantics remain; the predicate is not the changed tag mask. Mask-zero branch direction and layout differ. All of these would require miss/collision/resize guards if static admission had passed. Nothing here predicts a timing win.

## Reference finder and C's broader consumers

B/C also remove the reference finder's stored-byte recheck while preserving ID equality and optional found-slot writes. Native exact ranges are B `4ac4–4ad8` and `4b84–4b98`, C `4ac4–4ad8` and `4b88–4b9c`. LTO ranges are B `402a20–402a34` / `402b00–402b14`, C `402a18–402a2c` / `402af8–402b0c`. Candidate positions lead straight to original-width ID loads; narrow sentinel translation remains (for example C LTO `402a58–402a64`). No helper call is introduced.

B retains approximate zero-byte boolean tests. C changes them globally, including reference fallback and scan termination. At native reference `4b30–4b44`, C executes AND/ADD/ORR/ORR/CMN plus one constant MOV. B's `4b30–4b40` executes ADD/BIC/TST plus MOV/MOVK. C thus adds two dependent arithmetic operations and one total instruction at this boolean fallback even though the existence-of-zero question never needed exact candidate bits. This is real extra miss/scan work, not a removed recheck saving. Raw table-finder empty-slot loops are separate source code and remain unchanged.

C's native `zbtIndexScanSlot` and `.constprop.0` inline the full-word leaf scan. The `count >>3` guard precedes eight-byte loads: general `55c8`, zero-word branch `55d4`, load `55f8`, loop bound `5680–5684`; reversed load `5718`; clone `6028/6034`, loads `6058/6160`. No wider tag load is introduced. Full-word candidate loops directly store positions, without a tag byte reload. General `5610–562c` preserves tag1 union with tag0 via the complemented-mask equivalent; reversed path `571c–5754` selects the same union. Forward position store is `5660`; reversed conversion/store `5784–5788`. Tail start/count checks `5688–5690` and `57b0–57b8` lead to byte loads `56bc` and `57e4` with the original tag0-fold comparisons. Clone equivalents preserve these bounds and reversal (`60c0`, `61cc–61d0`, tail bounds `60e8–60f0`, `61f8–6200`).

The native compiler additionally emits register-only population-count instructions (`fmov; cnt; addv; fmov`) to update `found` after the exact full-word loops, e.g. `5668–5674` and `5790–579c`. These are compiler-generated vector instructions, not source intrinsics or wider memory accesses. They change scan work and must be reported; source-level scalar arithmetic alone does not describe the emitted scan. No scan function survives in these LTO lookup ELFs, so target scan code generation is **unavailable in this artifact**, not certified by the native scan. Separate scan ELFs/guards would be required if C otherwise survived. It does not.

## Static footprint and decision limits

| ELF | text bytes | Change from cohort baseline | data / bss |
|---|---:|---:|---:|
| Native baseline |95143|—|856 /40|
| Native B |95071|−72|856 /40|
| Native C |95135|−8|856 /40|
| LTO baseline |56539|—|744 /40|
| LTO B |56255|−284|744 /40|
| LTO C |56211|−328|744 /40|

Smaller whole-ELF text does not override larger raw frames. Source record/index layouts remain unchanged; this review does not rerun memory or correctness oracles. It establishes emitted-code rejection, not a measured regression and not another measured population. Both variants remain preserved unchanged.

## TMA classification and consultation

| Category | Qualified ARM baseline | B | C |
|---|---|---|---|
| Frontend_Bound and children |Unavailable|Unavailable|Unavailable|
| Bad_Speculation and children |Unavailable|Unavailable|Unavailable|
| Backend_Bound and children |Unavailable|Unavailable|Unavailable|
| Retiring and children |Unavailable|Unavailable|Unavailable|

The saved ARM collector's scope/formulas remain unqualified. No candidate profile was collected for this static gate; a100% slot tree cannot be reconstructed from arithmetic counts, frames or hotspot shares. No Intel category is transferred to ARM.

Own current-session discovery found no callable cpu-perf/library_status endpoint. The actual controller consultation recorded in [H7-selection.md](../H7-selection.md) is shared provenance:3/287 sources,158 passages, and an unrelated register/stack-sampling passage that does not establish mask speed. This reviewer did not make that call and does not cite it as support for the rejection; the rejection follows the frozen frame gate and verified machine code. Exact model/token cost remains unknown; detailed execution provenance is private.
