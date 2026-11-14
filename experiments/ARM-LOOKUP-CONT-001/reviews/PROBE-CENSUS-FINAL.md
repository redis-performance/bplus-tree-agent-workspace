# Baseline probe census final independent review

**PASS: the four saved census grids are internally consistent, match the admitted artifacts, and agree exactly. Close the negative-cache lead as NONE for these fixed workloads. Keep the exact home-filter table proposal at NONE for implementation under the current primary objective.** The census establishes logical path counts only. It provides no elapsed-time result, speed estimate, candidate acceptance, or qualification retry.

Reviewer role: independent result reviewer, prior source/artifact reviewer, and proposer of the home-filter diagnostic lead; not the census implementation author. This review performed no fleet action, workload execution, timing, compilation, or source edit. Original referees and the public ledger count of 47 remain unchanged.

## Execution and artifact joins

I independently parsed all 24 raw case outputs and replayed the frozen revision-1 checker. All four complete six-case grids pass, and the independently recomputed checker output equals each saved validation result. Every corresponding raw stdout file is byte-identical across ARM native, ARM target LTO, Intel native, and Intel target LTO. Equality includes the complete ordered table-call records and per-query resize states, not just final totals.

The source/admission identities remain those in [the source review](PROBE-CENSUS-CODE.md) and [the exact fleet artifact review](PROBE-CENSUS-FLEET-CODEGEN.md). The execution metadata pins the latter review at `f32b5b00f39119fe35caeb377df44b7a9cc89665a543391de62b538b8c200ba1` and all 56 inputs: the 48 census-directory pins plus eight original dependency/referee pins. I rehashed them against the retained canonical bytes and rehashed each actual ELF against both build and execution metadata:

| Artifact | Actual ELF SHA-256 |
|---|---|
| ARM native | `5c2bcf4418b445ea99a97416f08fa58e84c65e3676d67674eb888cbbbb0069d9` |
| ARM target LTO | `2d2e90ecaa2bfc951b4f01561fabb6e186e348008b80a2188443d17e8cb17540` |
| Intel native | `bfdfc3e77c2d05940c7d785b0e72c391e30c85e8ea92481dc6625df92edf5f24` |
| Intel target LTO | `47116266f5f76474714376aacdbffcc571707314a8baf4bcb571df9743608bac` |

The fetched ARM and Intel driver bodies match the frozen controller template exactly at the parsed syntax-tree level. Their five prefixed constants match the architecture, root, input pins, binary pins, and admission-review hash in the receipts. Each architecture records precisely 12 launches and 12 matching completed commands: native then LTO, each in the frozen hit/score/miss/long/external/update order. Every child command selects the admitted census ELF and one case, is pinned to CPU 2, returns zero, and has empty stderr. All four checker stderr files are empty. Both completion records identify 12 structural cases, with qualification and source adoption false; neither has an error record. There is no adaptive repeat or candidate launch in these drivers or recorded commands.

The driver performs pre/post input and ELF hash assertions for every child. Its isolation checks assert a stable reservation and deadline margin, stopped coordinator identity, controller affinity to CPU 0, CPU 2 availability, architecture-specific sibling isolation, unchanged active release timers and release commands, profiler service inactive with PID zero, no profiler process, and no running container. I checked all 48 saved pre/post isolation receipts: each reports success; lease hash, coordinator identity, timer fields, profiler state, and controller affinity remain stable within its architecture. Recorded ordering is pre-check, launch, post-check, followed by the next case. This validates the saved driver/receipt consistency; the reviewer was not an independent live observer of either host.

Fetch provenance has a narrower scope. The controller reports checking the ARM work service inactive with MainPID zero before fetching; that assertion is retained in the controller transcript rather than a separate ARM fetch receipt inspected here. The Intel controller-side receipt records its asserted inactive/MainPID-zero checks and subsequent archive fetch; its SHA-256 is `9ddf97153ab0115131cafc2fe726ff8aa0621ae81dee70ec26134e4c38c41041`. That receipt is not independent live-observer evidence. These distinctions do not change the independently verified fetched bytes, models, and hashes.

## Fixed model and counts

Every process uses the original seed 17, 500 members, exact fixture/query setup, and 1000 uncounted warmup sweeps. Each read case counts one sweep, or 500 operations. Update counts two sweeps, or 1000 original FindForAdd/UpdateScore pairs, and restores integer scores. Each grid has 3500 counted operations; the four grids contain 14000. The four identical grids are cross-toolchain/architecture consistency evidence, not four independently sampled workload populations.

Hit, score, long, and external return 500 successes; miss returns zero; update returns 1000. Only the score case has a nonzero score sum, exactly 125250. Immediate before/after owned bytes match the frozen baseline map: hit/score/miss 14272, long 146656, external 217600, update 14432. The separately reported post-validation bytes also equal these values in every output. Counter enable/disable, mandatory original leaf calls, output validation, and clock-denial semantics retain the previously reviewed artifact identities.

The following table applies identically to each of the four grids:

| Case | Operations | Home hits | Filter evaluations | Filter false | Positive filter fallback | Displaced bucket visits | Leaf calls | Failed leaf calls | Repeated failures |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| hit | 500 | 489 | 11 | 0 | 11 | 16 | 502 | 2 | 0 |
| score | 500 | 489 | 11 | 0 | 11 | 16 | 502 | 2 | 0 |
| miss | 500 | 0 | 500 | 489 | 11 | 0 | 9 | 9 | 0 |
| long | 500 | 494 | 6 | 0 | 6 | 6 | 503 | 3 | 0 |
| external | 500 | 493 | 7 | 0 | 7 | 7 | 501 | 1 | 0 |
| update | 1000 | 978 | 22 | 0 | 22 | 32 | 1004 | 4 | 0 |

Every query has exactly one table call. All calls use the current narrow-ID table with 128 buckets. Every per-query resize pair and global before/after resize endpoint is zero. Tombstone, free-reference, and migration skips are zero. Approximate candidates equal true stored-tag candidates in every case. Consecutive repeats, cross-bucket repeats, and repeated-leaf entry exposure are all zero.

The miss case demonstrates why a positive filter fallback is not synonymous with displacement: 11 queries pass the filter but all stop without visiting a displaced bucket. Failed leaf calls are first failures within their own table calls; their sum is not a count of globally unique leaves. Likewise, `leaf_entries_present` is summed leaf population exposed to calls, not the number of entries examined by the scanner.

## Raw output freeze

Each hash below identifies all four copies of that case's raw output:

| Case | Raw stdout SHA-256 |
|---|---|
| hit | `03587fbf8a899fc1308fedc2a25298aeadb1a358776bd3745e12c2641d3aff8f` |
| score | `eb8917c53e09f35b352c994666361596fccdefdc5a9ba8f73a00357d2dad06e1` |
| miss | `e31aecdae166df00808c70d91ce8c9d5376a6a6c477bef57ee5806c0131abbb0` |
| long | `03868b6872227562ed883efcb496b93d56b540b861ed2e8d4170649e51a45a61` |
| external | `e30a3bca5351c5c98b8dbef41693731fd4f32b375c17c8d9bf278175e877b78b` |
| update | `81a403232eaac849b473d2bb996eb77c6ac4cf6ab2ed4bd56dcf6155f231e55e` |

The fetched ARM driver hashes to `dc0b32273947c68598ad22677e9e7bb19310b3383c046412f91d82d2c734a1ea`; Intel hashes to `537cf174c66d96966a5c024729cbd6be578073b9a528e9f2184a616e6e4d940e`. Execution metadata hashes are `581282ad635032c59e3b81f5ca575fb43b21d1e2fc63c67479ada86b545f3952` and `c989ed34f300017ca6c48a5211a79935c687f4dda733a5dd163642da05de6ca3`, respectively. Full raw, driver, command, launch, completion, validation, and isolation hashes and independent replay details are retained in the private audit.

## Mechanism decisions and limits

**Negative cache: NONE on all six frozen workloads.** A per-table-call cache of previously failed eligible leaf IDs would skip no original leaf call in the observed work. This conclusion includes arbitrary prior failures, consecutive failures, and failures revisited across buckets. It does not rule out repeats in other seeds, tree sizes, mutation histories, ownership states, or production workloads. It also says nothing about a cross-query persistent cache, which was never the screened mechanism and would have different invalidation requirements. No candidate implementation is justified by these counts.

**Exact home-filter table: retain NONE for the current primary objective.** The primary has 489 successful home hits and 11 logical filter evaluations among 500 queries. The original ARM target LTO assembly already bypasses filter arithmetic on successful home hits, as recorded in [the proposal](../proposals-fourth/lookup-state.md): no-score leaf success at `0x406aac` reaches `0x406ff0`, while filter materialization lies on the fallback path at `0x406c00`–`0x406c40`. Thus the census confirms limited primary fallback exposure rather than a new common-path saving. It does not establish the cycle cost of those 11 evaluations or the benefit of replacing arithmetic with a table load.

The miss case exposes the predicate on all 500 queries, and native compilers may hoist its arithmetic before home search. Those facts identify different path exposure; they do not qualify a target-primary optimization or outweigh table-load, code-layout, frame, and guard risks. The diagnostic instrumentation itself can change hoisting and register allocation. Do not equate its source counter with executed arithmetic in an uninstrumented ELF, multiply counts by sampled function shares, or infer a speed limit or predicted percentage. The exact table mechanism is not disproved globally; the current evidence does not justify reopening implementation under this primary and guard contract.

Coverage is intentionally bounded. This census covers seed 17 and the six registered warm fixtures only. It does not cover seeds 29/43, member-returning rank/iteration guards, wide IDs, active resizing, tombstones, or manufactured collision histories. The aggregate parser cannot independently reconstruct leaf identities, which are not emitted; those semantics rely on the reviewed instrumentation and assertions. Four identical outputs do not remove these limitations.

No elapsed measurement, process-counter profile, retired-instruction count, or qualified TMA funnel was produced by this census. Controller timestamps support reservation and ordering checks only; this review does not derive workload durations from them. No new MCP consultation or supporting passage is claimed. H2/Q4 remain PARK, no source is adopted, and the existing public population ledger remains 47.
