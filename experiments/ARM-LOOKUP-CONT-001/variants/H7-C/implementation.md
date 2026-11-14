# H7-C — exact shared scalar tag masks

Independent implementation C. Local correctness and static-code review are complete; **ready for controller review and exact ARM native/target codegen admission, not performance-qualified or accepted**. No fleet access, local performance measurement, commit, push or source adoption. Other H7 implementations were not read.

Starts original e13d9fc8875a636ca07203b1f3fdd1aa28488bda, upstream ee8e7f70152404649ac947157fd662d11b4a00d5. Baseline C SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`; frozen candidate C SHA256 `fa45c5d7bdd04f37bd448a48b573ef92128b56ed35df9d176659d9ddd00ca5d9`. [source.patch](source.patch) contains only the authorized current/src/zset_btree.c change. No H1–H6 patch is included.

## Change and proof

Strengthened `zbtIndexTagMask` to exact byte equality using the selected unsigned64-bit identity:

```c
uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
const uint64_t low = UINT64_C(0x7f7f7f7f7f7f7f7f);
return ~(((x & low) + low) | x | low);
```

Each low-seven-bit value is0–127; adding127 yields127–254, so no byte generates a carry into its neighbor. OR with the original byte retains its original high bit; OR with127 sets all low bits. The final complement has exactly the high bit set when the original XOR byte was zero. This is unsigned bounded arithmetic, with no extra loads, target intrinsic, alignment assumption or endian-dependent memory reinterpretation.

Removed the now-redundant byte check from three consumers: `zbtIndexTableFind`, `zbtIndexTableFindReference`, and the full-word enumeration of `zbtLeafTagMatches`. Existing boolean zero-tag calls in reference termination and scan-overflow termination use the stronger helper without source changes. The leaf scan still uses `zbtLeafTagWord`'s endian conversion, ORs tag1 with tag0, enumerates positions in the same order, maps reversal identically, and preserves its scalar tail byte comparisons.

All other behavior remains in its original code: no changes to home filters, bucket format, IDs, tombstones, bounds/free-ID checks, migration checks, resize progression, insertion hints or output assignments. The leaf matcher and packed decoder were checked byte-identical against baseline. Record layout, score stream, allocation policy and member ownership are untouched. Tree-owned memory is expected to be exact; all36 frozen fixture outputs, including owned bytes, match the saved baseline byte-for-byte after JSON parsing.

## Correctness evidence

Commands are retained in [run-focused.sh](run-focused.sh), [run-scan.sh](run-scan.sh), and the original qualify.sh. Qualification runs the unchanged script commands with only its LOG destination redirected to this variant. All tests are correctness-only; none supplies timing or counter results.

| Check | Result |
|---|---|
| Original suite | 57/57 native and57/57 ASan+UBSan |
| Frozen fixtures | 18 native +18 sanitizer cells, seeds17/29/43, exact baseline result/memory match |
| Supplied output oracle | 90,000 checks, ASan+UBSan |
| Supplied external-record oracle | 45,000 checks, ASan+UBSan |
| Exact-mask oracle, each build | 2,721,440 masks; scalar byte reference and ordered bit enumeration |
| Guard-ended leaf scan oracle, each build | 198,656 cases, count0–96, all tags, both orders, four patterns, untouched output sentinel |
| Reference-finder differential oracle, each build | 1,572,864 scalar-reference pairs, narrow/wide70000+ IDs, wrap, zeros, tombstones, all tag values |
| Index/output differential oracle, each build | 138,496 comparisons over32 output combinations; active/new/old tables, three real migration steps, final public-lookup completion |
| Public scan differential trace, each of baseline/candidate native/sanitizer | 30 phases,2,204 calls,35,432 callbacks; identical trace `6d17a8ba5de08373` |
| Frozen -O3 build | GCC13.3.0, -Wall -Wextra -Werror, successful |

[mask_oracle.c](mask_oracle.c) derives truth by checking each byte; it does not repeat the candidate's arithmetic. It covers all256 tags/bytes in all8 lanes against equal and adjacent-nonmatching backgrounds, every equality pattern, high-bit patterns, every16-bit adjacent pair at all7 byte boundaries, and100k deterministic mixed words. Scan arrays end immediately before a PROT_NONE page; count0 has no readable element and count0–96 exercises every tail/alignment. Reference search uses a scalar loop and scalar empty-bucket detection, independent of the exact mask.

[index_oracle.c](index_oracle.c) adapts the earlier C worker's index correctness test, retaining a frozen approximate-mask implementation inside its baseline finder. It is not a comparison against the new shared mask under two names. Synthetic full/empty/collision tables exercise narrow and wide IDs, wrapped displacement, filter rejection, tombstones and insertion hints. The real resize case checks per-member old/new table exclusivity and final completion.

[scan_oracle.c](scan_oracle.c) is compiled separately against the materialized original baseline and candidate. Its300 binary members deliberately cover real hash tags0/1/127/128/254/255 for correctness, not candidate specialization. Every callback checks actual bytes, membership and exact score. Scans use COUNT1/7/16/1000, record cursor and callback order in a deterministic trace, and require complete membership while allowing the API's legal duplicates. Phases cover leaf reversal, incremental expansion/completion, cross-leaf score moves/reference repair, deletion/tombstones, duplication, reinsertion and resizing back. Both native and sanitizer baseline/candidate outputs match exactly. Existing upstream scan tests additionally cover mutation during a cursor pass.

## Retained failure

The first version of the new scan harness passed NULL to `zbtreeUpdateScore`, whose position argument is required. The **unchanged baseline** segfaulted before candidate scan execution. The exact failed test, stderr and GDB backtrace are retained under [failures/scan-harness-null-position](failures/scan-harness-null-position/README.md). The harness was corrected to obtain and validate a position using `zbtreeFindForAdd` before changing the score; candidate source was not changed. All four corrected baseline/candidate scan executions pass. This harness failure is not omitted or represented as a candidate result.

## Local static codegen

Inspected the actual standalone -O3 ELF from GCC13.3.0 x86-64 using the frozen build flags, plus a separately compiled original-source ELF with the same flags. Full disassemblies and size output are retained. These are local build/static observations, not local performance results and not ARM evidence.

- The baseline raw candidate-to-ID sequence atd741–d755 includes `tzcnt`, a byte-position mask, variable stored-tag shift, byte comparison and conditional branch before the ID load. Candidate d8f6–d8fe is `tzcnt`, position shift, ID load. The same removal appears in its stable narrow path atdb22–db2a and both wide paths atdcee/dece. Tombstone, bound, free-ID, assertion and migration checks remain.
- The baseline approximate-mask path has XOR plus subtract/not/and/high-bit filtering. The exact mask emits scalar XOR, low-bit AND, addition, OR with original, OR with low mask, complement; there is no helper call or new load. It does add per-bucket work, including no-match buckets. This is the central miss/scan guard risk; removing candidate checks does not prove a net speedup.
- The reference finder at513f–5159 extracts the first bit and immediately loads/checks the ID; no stored-tag recheck remains. Full-word scan enumeration uses the exact mask; scalar-tail tests remain required and present in source.
- Raw stack reservation remains0x88 after the same six saved-register pushes; prehashed raw remains0x78. There is no local raw-frame growth. The leaf helper remains a call to the existing constprop clone; its source is unchanged.
- Local executable text:101,042 baseline bytes,100,234 candidate bytes. This size observation includes compiler layout and differing baseline materialization `__FILE__` strings; it is not an instruction/op or performance comparison. Data784/BSS40 unchanged.

The local mechanism is plausible and remains small:9 inserted/16 deleted source lines. The mandatory ARM native/target emitted-code gate is **not yet evaluated by this worker**. No ARM compiler was run and no fleet operation was attempted. The controller must inspect actual candidate/no-score clones, frame sizes, mask construction and candidate-to-ID paths, rejecting NONE if rechecks persist, frame grows, or added dependency work cancels the specified removal. No rescue patch or compiler flag change is proposed.

## Remaining risk and scope

The wider C scope intentionally changes exact-mask arithmetic for boolean empty-bucket and scan callers too. Extra arithmetic on misses or repeated scan groups may regress despite fewer candidate branches. All original six cases and iterator/rank/churn guards remain mandatory; qualified collision/displacement/resize and member-returning scan guards must precede adoption. Same-tag actual equality still runs the original leaf helper. No memory tradeoff is requested.

32-bit and big-endian execution were not validated locally. Numeric bucket order and the existing `intrev64ifbe` leaf-load path remain unchanged, but source reasoning is not execution evidence. Exact target codegen, fleet timings, heldout confirmation and independent review are outstanding. This implementation is not selected or adopted.

## TMA and consultation

New candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children are unavailable: no candidate profile has been collected. Qualified ARM baseline categories remain unavailable under the registered scope/formula limits. Separate Intel baseline categories exist in the controller's audit, but are not substituted for this candidate or ARM. No sample share, text size, static instruction sequence or IPC is presented as a pipeline-slot result.

Own active-tool discovery found no callable cpu-perf/library_status names. The actual controller stdio consultation in `build/arm-cont-private/mask-classifier-consult/{discovery,library_status,ask}.json` is consumed as shared evidence, not a worker invocation. It covers this exact identity, all three consumer scopes and guard risks; library coverage is3/287 sources and158 passages. The retrieved perf_event_open register/stack passage is unrelated to the mask's speed and supplies no support. The arithmetic proof and inspected source justify correctness review only; performance remains unmeasured. Public attribution is implementation role only; detailed provenance and unknown cost/model accounting remain in the ignored private worker record.
