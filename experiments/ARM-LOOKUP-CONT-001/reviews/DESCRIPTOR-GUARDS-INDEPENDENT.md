# Independent descriptor-guard harness review

Reviewed 2026-11-14. **Revision 0 is ready for controller freeze and subsequent fleet qualification; no blocking harness defect was found.** This is not duration qualification, performance acceptance, or independent confirmation of an H6 candidate. Exact target ELF inspection and the registered fleet A/A gates remain required before candidate timing.

The reviewer authored H6-B but did not author this guard harness. This is independent harness review, not independent-author review of H6-B. No harness, candidate, collector or protocol file was edited. No `measure` invocation, local timing, profiling, instruction measurement or fleet access occurred.

## Reviewed freeze

The review applies only to the following exact files in [descriptor-guards](../descriptor-guards/). Every entry in its existing `SHA256SUMS`, all proposal referee hashes, and all eight saved correctness-binary hashes were independently checked and matched.

| File | SHA-256 |
|---|---|
| `guards.c` | `1f5ea1beb4391e5ae1818a5df60167c85e0931f2172efa300fd5cc2aea90fed9` |
| `build.sh` | `1c8c4f8f4cd1233a2d71f4e660cb144bccd675fe37337dad02bb1bc5ce761d78` |
| `verify.py` | `6db5b9f7e9dcf49dacb290cc90bfa06d5f749b119bc724bfbe957a4e3facb58c` |
| `check_oracle.py` | `7ed75a3357b3a77936a424f2eac6398f2d7aaae740bc36b5ff49f5d5bba1542b` |
| `PROTOCOL.md` | `39f44530191b246f6efb3345243d524af190f66b4d5688df73ee5ae0c444a04c` |
| `PROPOSAL.json` | `7958465a983eef061b0b28abc156edcabb71c23e62d5d86aa41fc24f3dae2577` |
| `SHA256SUMS` | `f2fc6ac06d34491592b1cd3c31902aafe0cd48063f4a15f0cb0d268719e8412b` |

The frozen source identities are baseline `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, A `ffd548a1fba1db452e98fbe1dd3902b2ba34f44af797edeaed9976783444e744`, B `5f6bfd216350dceee6ed486d5fc6e1535162a64c037c3ceee746ceae9b0813ae`, and C `bf2cbbe66b36d178692ba214fd192af1b5dc6b1c67f1619e2d782c839b2da825`. The controller must retain these identities with the frozen referee and each exact fleet ELF. `verify.py` reports the sources it builds; it is not itself a replacement for checking them against the intended freeze.

## Timing, counts and memory

`verify` is limited to 1–8 sweeps, skips warmup, and takes neither timer branch. `measure` is bounded at 2,000,000 sweeps, warms up 1,000 sweeps, validates warmup sums and full tree contents, constructs expected sums, and samples owned memory before starting the timer. The measured interval contains `run`, its loop assertions and accumulators, and ordinary call/return/result-transfer overhead. Setup, expected-value construction, full comparisons, printing and cleanup remain outside.

The stop timestamp precedes `owned_bytes_after`, which is sampled before checksum and full-tree validation. Validation can advance index maintenance, so the separately named `owned_bytes_after_validation` must not replace the immediate endpoint. Both original endpoints are preserved for the memory gate. Endpoint snapshots do not measure transient peak allocation; the protocol discloses this.

| Case | Exact operations per sweep | Registered provisional sweeps | Operations per measured process |
|---|---:|---:|---:|
| member-forward | 529 returned members | 1,000,000 | 529,000,000 |
| member-reverse | 529 returned members | 1,000,000 | 529,000,000 |
| lookup-inline | 465 hit/miss pairs = 930 queries | 100,000 | 93,000,000 |
| lookup-external | 64 hit/miss pairs = 128 queries | 500,000 | 64,000,000 |

Iterator start and the terminating unsuccessful `Next` are executed but intentionally not counted as returned-member operations. No mutation-operation count is implied. At the maximum accepted sweep count, independent arithmetic checks show all counters fit their types: the largest sampled-byte checksum is 2,010,996,922,864,000,000, below `UINT64_MAX`; the largest signed score sum is 280,370,000,000, below `INT64_MAX`.

There is no local duration evidence. Counts are provisional until each exact fleet cohort passes all 48 A/A rows: three ABBA blocks for each of four cases, every row at least 250 ms, every block within 1%, reproducible memory endpoints. The registered 48 comparison rows per eligible candidate and 1% every-block/every-case guard rules are coherent. Short or failed controls park the attempt and require a newly registered repair; they do not authorize an unchanged retry. A bound of 2,000,000 sweeps limits work but does not promise a wall-clock upper bound. The controller must budget the full campaign and cleanup before starting it.

## Fixture and oracle audit

All implementations compile the same public-API fixture and compatibility sources. The 529 generated members are unique by length and replica first byte; there is one empty member. Scores are distinct exact integers 1–529. Before and after the run, both iterator directions check every full byte, length and score against separately owned caller buffers, require exactly 529 entries, and check end-of-iteration. Full hit/miss lookup validation checks success, exact score and untouched miss sentinel.

Absent partners are provable: nonempty first bytes become 128–143 while stored first bytes are 0–15; the empty member's absent partner is byte 254. Selection is based on the original member length, so the empty member's one-byte miss stays in its intended inline pair. Every lookup sweep is exactly half hits. The inline/external division is 465/64 and matches the physical external threshold used by the frozen sources.

The fixture covers each descriptor codebook and uncoded transitions, including 7/8, 14/15, 16/17, 127/128/129, 253/254 and 319/320. Eligibility differs by candidate as intended; queries and bytes do not. Forward/reverse cases test opposite **logical traversal** and have distinct order-weighted expectations. They do not establish reversed physical leaf storage. The protocol correctly excludes that claim, as well as externally stored short records, forced same-tag collisions, displaced probes, active resize and mutation from these timed workloads. Those remain separate correctness and affected-path guard obligations.

Timed iterator sums consume returned pointer bytes at bounded first/middle/last positions, exact length, score and ordinal-weighted values; empty members perform no sampled byte access. Lookup sums consume results and returned scores. All sums reach assertions and printed output. These aggregate checks are not injective: compensating transient mistakes could cancel, and three byte samples do not prove every timed returned byte. The exact pre/post full-member oracle provides stronger state validation, while the dedicated semantic oracles remain necessary. This limitation is already disclosed and is acceptable for a supplemental performance guard; no claim of exhaustive transient correctness follows.

The C expectation helper shares byte sampling with the timed loop, but the supplied Python oracle independently generates the fixture and calculates its expectations. I reran that oracle successfully for all 384 saved rows. I additionally verified every saved matrix has exactly the 48 unique `(seed, case, sweeps)` cells, rather than relying on row count or `zip` alone. Closed-form independent checks confirmed score sums and forward/reverse ordinal weighting. All four sources have identical logical rows; native memory endpoints are each 86,008 bytes and sanitizer endpoints each 85,267 bytes. Those allocator-specific values are not interchangeable across modes or fleet cohorts.

## Additional verification and optimizer audit

Executed 16 fresh **native verify-only** cells: baseline/A/B/C × four cases, seed 101, three sweeps. Each process used an interposed `clock_gettime` that immediately exits 99 if called; all 16 completed successfully with no elapsed field and identical output across sources. This confirms the experiment's verify path does not read that clock. The saved evidence is [verify-no-clock.json](../../../build/arm-cont-private/descriptor-guard-review/verify-no-clock.json), SHA-256 `3b28635f1d23c9e3e0cba5d643b4e8aac2408e3fb61fedfea3434c5bc14cff1e`. Existing ASan/UBSan rows were reviewed, not rerun.

Inspected the existing native baseline and built an additional local baseline LTO ELF strictly for disassembly; that LTO ELF was not executed. Both retain a non-inlined `run` and repeated work. Native `run` calls raw lookup at `29be` and iterator-next at `2b64`, with the sweep backedge `28b8 → 2840`; local LTO calls raw lookup at `942e` and iterator-next at `95d4`, with sweep backedge `9328 → 92b0`. Iterator byte-sample accumulation remains inside the repeated traversal. Thus the inspected builds do not replace repeated sweeps with a multiplied first-sweep result or remove pointer consumption.

The native measured call is bracketed by `now_ns` at `1b68`, `run` at `1b87`, and `now_ns` at `1bd2`. Local LTO has `now_ns` at `4273`, `run` at `4292`, and `now_ns` at `42d6`. Immediate memory sampling follows those intervals before full validation. These are static observations, not measurements. Saved native/LTO disassemblies are under ignored `build/arm-cont-private/descriptor-guard-review/`; the unexecuted LTO ELF hash is `4f5b20b83761d1d4bb8f7ff843cecac8185aa91b0f482b5acdc8c0171443eca0`.

Exact fleet native/LTO and candidate ELFs must still preserve the timer boundaries, repeated loops and result consumption. Local compiler behavior cannot qualify a different compiler's emitted code. No compiler barriers, volatile accesses or candidate changes were introduced by this review.

## Disposition and provenance

**Freeze-ready for fleet qualification, with the hashes above; no required harness revision.** The protocol remains provisional until the controller records its freeze. Passing qualification would permit only the preregistered supplemental comparison; it would not waive the original primary gate, existing guards, newly affected-path guards, held-out confirmation, matched profiles or independent candidate review. Any later semantic harness change requires a new identity/review rather than applying this verdict to different bytes.

Fresh own tool discovery found no exposed CPU-perf/library-status names. The controller's actual shared descriptor consultation remains disclosed shared evidence, with no supporting retrieved passage; no new consultation or performance cause is claimed here.

| TMA category | Baseline for these guards | Candidates for these guards |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No workload profile or qualified child-category collection was performed. This review provides no pipeline-slot inference from code structure or another machine. No benchmark, local timer, fleet action, commit or push was performed.
