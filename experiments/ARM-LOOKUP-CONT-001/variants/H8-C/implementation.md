# H8-C — shared range-first record decoder

Independent implementation C. **Local correctness passes and local static code is credible; exact ARM native/target admission remains pending.** No timing, profiling, fleet access, commit, publication or adoption occurred. Other H8 implementation drafts were not read.

Original baseline e13d9fc8875a636ca07203b1f3fdd1aa28488bda, upstream ee8e7f70152404649ac947157fd662d11b4a00d5, source SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. Frozen candidate source SHA256 `37f5c33a57120e33a5a0203dc05bfb41f9e528cd5dabef934c66335526b2de0e`. The [source patch](source.patch) changes only current/src/zset_btree.c:18 inserted/8 deleted lines. No H1–H7 patch is present.

## Implementation and semantics

The original packed decoder body now resides in `zbtPackedDataChecked(record, len, expected_hash)`. It retains the complete ordinary-inline range first, followed by extended-inline marker254 and external marker255. Only the external arm adds optional full-hash validation. A mismatch returns NULL **before** loading or validating the external pointer and leaves the length output untouched. Accepted external records retain the original nonnull pointer assertion and size-range assertion.

The original `zbtPackedData(record, len)` API remains as a no-hash wrapper passing literal NULL. All its callers remain unchanged. Leaf lookup calls the shared decoder with its expected hash and continues at the next tag when the result is NULL. The original length/variable-memcmp condition, successful-match output block, memchr traversal and leaf boundary remain. No record layout, index probe, home filter, migration, score packing, allocation or ownership change is included. No inlining attribute, barrier, branch hint or compiler flag was added to influence the source result.

Ordinary inline and extended inline payload addresses are nonnull even for zero length. For an external record, NULL remains an assertion failure after an accepted hash; only an actual mismatching external hash can produce the new rejection result. Generic callers never request rejection and retain their previous decoder contract. Query length does not select a representation.

## Correctness

The unchanged qualification script ran with only its log destination redirected to this variant. [run-focused.sh](run-focused.sh) records the additional compile/run commands. Native uses GCC13.3.0 -O2; sanitizer uses -O1 with ASan+UBSan and nonrecovering errors. Static production builds use the frozen -O3 flags. All completed executions pass; ordinary logs have empty stderr. The two assertion cases described below intentionally abort child processes and are checked as expected outcomes.

| Check | Result |
|---|---|
| Original upstream tests | 57 native +57 sanitizer, zero failures |
| Frozen fixture cells | 18 native +18 sanitizer; exact original baseline JSON, including owned memory |
| Supplied optional-output oracle | 90,000 ASan/UBSan checks |
| Supplied external-record oracle | 45,000 ASan/UBSan checks |
| Record/equality/output oracle, each native/sanitizer | 1,264,736 checks |
| Independent decoder oracle, each build | 45,122 checks,2 expected NULL-pointer assertion children |
| Mutation oracle, each build | 7,693 full-tree validations,30 page relocations |

[record_oracle.c](record_oracle.c) adapts the earlier C worker's bounded equality correctness fixture without copying its source optimization. It now covers **every ordinary header0–253** plus inline254/255/256/319, both zero and binary/high-bit payload patterns, tag0/255, every mismatch position, unequal lengths/prefixes, query pages protected before/after their readable range, and records ending at a protected page. All four score/position output modes are checked. It retains all16×16 query/record alignments for lengths0–8 and same-tag candidate/reversal checks. External320/384 and artificially retained external short/empty records are exercised. A NULL external pointer with a different full hash is tested through the leaf lookup itself, requiring rejection and untouched output sentinels.

[decoder_oracle.c](decoder_oracle.c) builds its expected decoder result through independent explicit header cases and memcpy reads. All inline lengths0–319 and external lengths0–384 are tested at16 record alignments, through the no-hash wrapper and checked decoder with absent/matching/mismatching expected hash. Inline records ignore expected hashes; only external mismatches reject. Returned length remains a sentinel on rejection. An external header/hash is placed in the last five readable bytes before a protected page; mismatching-hash decode succeeds in rejecting without reading inaccessible length/pointer bytes. Separate child processes check that generic decode and matching-hash decode of a NULL external pointer still terminate with SIGABRT. Core dumps and expected assertion diagnostics are suppressed only inside those children, and their termination status is mandatory.

[mutation_oracle.c](mutation_oracle.c) adapts the earlier C worker's lifecycle oracle, removing descriptor-specific invariants rather than importing a descriptor patch. It validates original offset/storage bounds, complete tree/index structure and zero/full64-bit/reversed score states. Mixed empty, short, extended-inline and external binary members undergo insertion, repeated score movement, deletion, shrink, alternating edge pops, duplication, actual node relocation/repair and append-builder flush. Native observes53,527 leaf checks and sanitizer53,597; their allocator layouts differ, so these counts are reported separately rather than forced equal. Both perform30 page relocations and7,693 validations. The supplied output oracles additionally check signed-zero scores and exact successful/missing output behavior.

No candidate source or sanitizer failure occurred. After the initial focused pass, one test was extended to cover NULL-pointer hash rejection through leaf lookup; only that test was rebuilt/rerun. Candidate source remained frozen. All required suites were not redundantly repeated after a test-only coverage addition.

## Local codegen and generic-caller audit

Inspected original/candidate local x86-64 GCC13.3.0 standalone ELFs with the frozen C11 -O3 debug/frame-pointer/warning flags. Full disassemblies, size output and a GCC optimized-tree diagnostic are retained. These are static observations, not performance or ARM results.

The candidate leaf clone's relevant sequence is:

```text
36b4  movzbl (%rax),%edx       original actual-header load
36bb  cmp $0xfd,%dl
36be  jbe 36de                ordinary0–253 directly to length comparison
36c0  cmp $0xfe,%dl
36c3  je 3740                 extended-inline length
36c8  cmp %esi,0x1(%rax)      external full-hash comparison
36cb  jne 3678                rejection before pointer access
36cd  mov 0xd(%rax),%rdi      external pointer, accepted hash only
36d1  test %rdi,%rdi
36d4  je 3761                 original nonnull assertion path
36da  mov 0x5(%rax),%rdx      external length
36de  cmp %rdx,-0x38(%rbp)    query-length equality
36f4  call memcmp@plt         unchanged bounded comparator
```

Ordinary-inline classification falls from two marker comparisons to one range decision. Extended inline still takes two representation decisions. External handling takes two instead of the baseline's initial255 decision: **one added necessary classifier**, explicitly admitted only subject to the original1% external guard. There is no redundant third marker check, runtime decoder call, indirect jump table or external pointer access before hash rejection.

Both original and candidate leaf helpers reserve0x48 after the same saved registers. Raw lookup reserves0x88 and prehashed raw0x78 in both. No local leaf/raw frame grows. Local text is101,042 baseline versus101,354 candidate bytes (+312); data784/BSS40 unchanged. Text includes code layout and different baseline materialization `__FILE__` strings, so the difference is not an instruction/op measurement or a clean attribution to this helper alone.

The optimized-tree diagnostic contains no live `expected_hash` variable/check outside debug annotations. The only remaining function named `zbtPackedDataChecked.part.0` is a compiler-created **assertion-only** routine whose entire runtime body calls `standalone_panic` for `ptr != NULL`. It is not a normal decoder boundary and is reached only on the existing assertion failure path. No general checked decoder or no-hash wrapper call remains out of line.

[generic-static.json](generic-static.json) lists literal-NULL inline sites; [generic-optimized.txt](generic-optimized.txt) retains representative optimized bodies. These include build-from-leaf/rebuild preparation, tree lower-bound traversal, scan slot decoding and iterator-next member decoding. For example iterator-next at15de2 tests the ordinary range, at15de8 the extended marker, and at15df2 directly loads the external pointer; there is no optional-hash test or hash comparison between them. Generic build/compact/delete/merge/scan callers likewise use constant NULL. Public rank's indexed member lookup still performs the same required external full-hash validation through leaf lookup; its generic tree-ordering decode is represented by the lower-bound/find-leaf paths. This distinction avoids falsely requiring all hash checks to disappear from rank.

The shared abstraction remains a broader optimization surface than A. Although optional validation disappears locally, other backends can make different inlining/layout choices. Exact ARM native and target LTO codegen, including actual scored/no-score clones and generic iterator/rank/build/scan paths, has **not** been evaluated here. The controller must apply the registered NONE rules before timing: reject a runtime decoder, surviving optional generic checks, redundant marker tests, frame growth or disproportionate code growth. No fallback/metadata/equality optimization will be stacked to rescue a failure.

## Outstanding gates, TMA and consultation

No speed is claimed. The external extra decision and global code layout are leading risks given H3's fallback regressions. All six original cases, five supplemental guards, affected member/collision/decode traffic, qualified controls, heldout seeds and independent review remain required.32-bit and big-endian execution are unvalidated; original memcpy and size-range assertions remain. Tree-owned memory has no new field/allocation and matches the frozen fixture cells exactly.

Baseline ARM and candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children are unavailable as qualified slot categories. Candidate profiling is uncollected; the ARM baseline's scope/formula qualification remains unresolved. Separate Intel baseline evidence is not substituted for this candidate or ARM. Assembly and text size are not TMA.

Own enabled-tool discovery found no callable cpu-perf/library_status endpoint. The controller's actual shared mask-classifier consultation, recorded in H8-selection.md, covers this separate range-first mechanism and fallback risk. Its3/287-source,158-passage coverage returned only an unrelated sampling-register passage; it supports no causal speed claim. These are shared calls, not this implementer's invocation. Public role is implementation C; detailed provenance remains private and exact cost/model accounting is unavailable.
