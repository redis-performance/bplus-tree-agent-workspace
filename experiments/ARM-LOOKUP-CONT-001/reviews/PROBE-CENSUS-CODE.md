# Probe census independent code review

**CODE ADMISSION: PASS for admission revision 1, limited to the frozen baseline structural census.** The reviewed preparation can proceed to separate fleet builds and exact target artifact review. Execution remains subject to that review and the controller's reservation, isolation, and freeze checks. This admits no timing experiment, optimization candidate, or performance conclusion. No diagnostic executable or clock probe was run in this review.

Reviewer role: independent code reviewer and proposer of one diagnostic lead; not the census implementation author. This review covers the generator, generated source and harness, instrumentation, parser, protocol, saved compile artifacts, and synthetic tests. No candidate or original referee was edited.

## Reviewed freeze

All 47 entries in the revised directory manifest were independently rehashed. Generated products reconstruct exactly from the pinned inputs, and the patch reconstructs the generated tree source.

| Artifact | SHA-256 |
|---|---|
| `probe-census/SHA256SUMS` | `82e7ca06eaf451d26b4bc3b40e6386bf689d34fab418af3862e82d586ac3ef48` |
| `probe-census/PROTOCOL.md` | `6762c2d5b8901f0a8eb739c30ad708ef3a508a47c81a6193b6a46e0311778568` |
| `probe-census/GENERATION.json` | `f14cc62377359f1d53f6f7cd85c05ee7ec8891b01ea0c36e20af08d7773ed0e7` |
| Original tree source | `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9` |
| Original `lookup.c` | `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827` |
| Generated tree source | `c975a36f61d9780c8450f78336e8b509cbae75b23c87abb0de6f6acc4855dff5` |
| Generated census harness | `9b54905269b64205b98267c1522883fad8e833fc202622b9d0fb5dcdc8be99af` |
| Instrumentation patch | `702a4d24054b8c18dc3dc06a78b42728ff9c188354736150fdd8013ebb965f92` |
| Revised parser | `4d39817d1ae884162343418314ef1b095f24cf70c762110e7edb9a73ce0eb317` |
| Revised Python tests | `c91be87cfe602d217e216c521913df53348dab38ec886d3c8c3104cd6e4a2a93` |
| Memory provenance | `4bcf2aa5027958a0ea1339adcadd9ad789d0c84a3522bc70a6e9c3c39eaaf817` |

The baseline extraction is `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, with upstream pin `ee8e7f70152404649ac947157fd662d11b4a00d5`. No H1–H8 patch is present. Admission/parser revision 1 deliberately retains C output schema revision 0: source, instrumentation, generation manifest, and compiled bytes did not change during parser hardening.

## Instrumentation and work model

The only tree-source changes lie in `zbtIndexTableFind` and its instrumentation include. All other source text, including leaf search, decoder, hash, allocator, reference finder, migration, and filter formula, remains byte-identical. Instrumentation preserves candidate order, stored-tag validation, tombstone handling, ID bounds/free-reference checks, migration ownership, output writes, and original return values.

Shadow history resets for every table-finder call. It records an identity only after the original eligibility checks and a completed failed leaf search. A repeated identity still executes the original leaf helper with the original arguments. The wrapper then checks that the search remains negative and that requested score and position object bytes remain unchanged. No failed-result cache, skipped search, extra validation search, or cross-table/query reuse is implemented. Leaf data cannot mutate during the synchronous table search. Consecutive repeats refer to successive actual leaf calls; intervening ineligible candidates do not constitute leaf calls. Cross-bucket repeats compare with the first failed occurrence and can overlap the consecutive subset.

Home hits finish before the original home filter. After failed home candidates, the filter is evaluated once; rejection terminates search. A positive home post-filter fallback can terminate at an unused slot in the home bucket, so it does not imply a displaced bucket visit. Approximate mask candidates and true stored-tag candidates remain separate. `leaf_entries_present` measures summed leaf counts at calls, not elements actually scanned or bytes compared. These distinctions are necessary when interpreting the emitted totals.

The original fixture function and query setup are exact extracted substrings. The executable fixes seed 17, 500 members, original insertion/reserve behavior, byte patterns, and independent source/target query buffers. Hash-key bytes retain `(seed + i * 29) & 255`. The six cases are hit, score, miss, long, external, and update; no favorable extra fixture or configurable work count is introduced.

The original 1000-sweep warmup executes with counters disabled. Counter reset and immediate memory/resize capture precede enabling. Read cases count one sweep of 500 operations; update counts two sweeps of 500 original FindForAdd/UpdateScore pairs, restoring integer scores. Its scratch score initialization only defines snapshot bytes before the successful lookup overwrites the value. Counters disable immediately after work. Owned bytes and resize state are captured before validation, printing, or cleanup. Final validation checks member bytes, lengths, order, exact scores, successful score lookup, and unchanged negative-lookup score output. Post-validation memory is reported separately because validation can advance rehash.

The parser's resize constraint is **specific to this frozen harness call sequence**. In generated `census.c:24`, each update calls FindForAdd before UpdateScore; read cases call the original raw reader. Their counted table calls arise through `zbtIndexFind` (`current/src/zset_btree.c:2311`), which advances an existing resize and does not create one before its table calls. FindForAdd (`:3322`) delegates to that finder. UpdateScore (`:3738`) can reserve a leaf ID and potentially initiate widening (`:2206`), but this happens after the counted lookup; its move/reference paths do not call the instrumented table finder. Therefore an active counted table must have an active query-entry resize in these operations. A `[1,0]` query whose resize completes before its first table call remains valid. This is not a general claim that arbitrary Redis mutations cannot start and finish resizing inside one operation.

## Fixed memory and parser corrections

The immediate memory requirement is both equality and an exact baseline value:

| Cases | Before and immediately after, bytes |
|---|---:|
| hit, score, miss | 14272 |
| long | 146656 |
| external | 217600 |
| update | 14432 |

I independently joined all 324 saved baseline-label-A seed-17 rows across ARM/Intel native/LTO cohorts to their metadata and independently rehashed all four actual baseline ELFs. Each row matches this map. Label A denotes the baseline within a comparison pair, not candidate H2-A. The comparison, metadata, and ELF hashes match `MEMORY-PROVENANCE.json`. These checks establish memory provenance only; H2 remains PARK.

Initial revision 0 was **not admitted**. Four synthetic records with recomputed, internally consistent totals exposed missing semantic checks:

| Impossible record | Revised rejection |
|---|---|
| Repeated failed leaf with no first distinct failure | Requires a distinct failure before any repeat |
| Successful search despite a false home filter | Requires result zero and only the home bucket |
| Active destination-table call inside an inactive query | Requires query-entry active resize for this harness |
| Home hit with zero bucket visits | Requires a visit for every nonempty table |

An additional wrong-but-equal memory probe exposed the need for the fixed baseline map above. I independently reproduced all five as accepted by the archived parser and rejected by the revised parser. All eight archived revision-0 preservation hashes also match. The original rejected parser, tests, protocol, manifest, and logs remain under `failed-attempts/revision0-parser-admission/`.

Revision 1 additionally checks eight-slot candidate capacity, positive filter before displacement, displacement before cross-bucket repeats, valid resize context for migration/free-reference skips, zero work in empty tables, counter partitions, ordered calls, state continuity, complete case coverage, exact work/checksums, and aggregate totals. Independent execution of the 12 Python-only tests passes, including valid resize completion and synthetic repeat accounting. These tests execute no C diagnostic.

The parser checks consistency of aggregates; it does not independently reconstruct leaf identities, which are not emitted. Identity correctness relies on the reviewed instrumentation and its assertions. Synthetic records establish validator behavior, not observed census traffic.

## Saved code and clock denial

The two local GCC 13.3 compile-only artifacts were independently rehashed:

| Mode | ELF SHA-256 | Assembly SHA-256 |
|---|---|---|
| Native | `02a5fa2291f1d3e6b84a56815f7c5eea9cb12e2a3ab1879f22f2d8fdef96a6bb` | `876b042a5838827f540d06ea09b44cc89008478b730a719b465290cb7d6f23a2` |
| LTO | `fd7d23cd1168385f9282845c7a69796d66bba29e67deec09c8705e637ef37053` | `5404381d2f3637dc2feb588d7131aa3d8bd933ee5322b08ce510048df84a039b` |

Saved disassembly bytes match ELF load segments: 103859 native bytes and 61856 LTO bytes, 165715 total. These are static byte checks, not instruction measurements. Native leaf calls at `0x4cdc` and `0x4e03` target the original helper at `0x4a80` (assembly lines 3918 and 3999). LTO calls at `0x5efd` and `0x6037`, plus inactive forwarding at `0x6021`, target the helper at `0x58b0` (lines 5168, 5257, and 5252). The repeat path retains the mandatory call before its assertion.

Both ELFs retain all 13 clock-denial wrappers. Inspection found each wrapper writes its denial message and exits before reading time, with no unresolved denied clock API. Explicit linker retention covers LTO. The generated harness contains no timing reader, timing mode, elapsed output, or direct cycle-counter instruction. A separately compiled, never-executed link probe confirms an explicit clock_gettime call targets its wrapper; its ELF hash is `d3b237b37c9749f004d7054085a463dace9f9dffcf2f4b18e5ea5a34ac0bf69f`.

This denial contract covers owned linked entry points and inspected source paths. It does not promise interception of arbitrary injected libraries or private timer implementations inside dependencies. Runtime denial was not tested. `build.sh` only builds and inspects; it does not execute the result. Initial compilation and LTO wrapper-retention failures remain preserved.

## Limits and next gate

Local static checks do not qualify target GCC 15 output. Before structural execution, independently join exact fleet source/compiler flags, ELF hashes, complete emitted assembly, retained clock wrappers, and mandatory original leaf calls for each admitted artifact. Keep build and execution as separate actions. Execution must remain the protocol's fixed six fresh processes with no clocked pilot, adaptive count, repeated qualification, or local workload run.

No observed path counts exist at this review point. The census is bounded to the original seed, six warm states, and 500-member fixture; it does not manufacture collisions or resize coverage. Zero repeats could rule out the negative-cache lead for this primary fixture. Nonzero repeats would establish potential redundant calls only. Instrumentation can alter compiler hoisting and register use; source filter counts cannot establish dynamic arithmetic cost in the unmodified target ELF. Neither counts nor sampled function shares justify a speed estimate or selection without separate evidence.

No new MCP consultation, fleet action, profile, timing, or TMA measurement was performed for this review. The protocol labels the controller's prior actual consultation as shared and reports no matched supporting passage; this review does not convert that consultation into mechanism evidence. Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring, and their children remain unavailable here. H2/Q4 PARK decisions and all original acceptance thresholds remain unchanged.
