# Independent H2 final review — PARK / NONE

**PARK. No source is selected or accepted.** H2-B passes the original discovery/transfer evidence and both hosts' seed29 confirmation. Intel seed43 also passes. ARM seed43 fails its fresh baseline A/A qualification, so the mandatory target confirmation is incomplete. This is a qualification failure, not a demonstrated H2-B regression; the source remains eligible for a separately justified future investigation. Neither the earlier gains nor the Intel result can waive the failed ARM control.

This review independently reconstructs the completed confirmation evidence and executable identities. The reviewer authored the hardened Intel profile parser and the earlier [readiness review](H2-INDEPENDENT-READINESS.md), but did not implement H2-B, the supplemental guard harness, or either confirmation driver. Parser authorship is an overlap, not an independent second implementation of profile qualification. The separate [source review](H2-CODE.md) and [ARM profile audit](H2-ARM-PROFILE-AUDIT.md) supply additional independently reviewed evidence. Only saved artifacts were inspected: no fleet access, new timing, profiling, source/referee edit, commit or publication occurred.

## Decisive failed control

The [ARM seed43 qualification](../H2-confirmation/arm/H2-lto-confirmation-43/qualification.json) contains all72 required rows and18 blocks. Seventeen blocks pass; `miss`, block index1, fails the frozen ±1% A/A bound. Both nominal A and B slots execute the identical baseline ELF, with seed43 and500,000 sweeps/250,000,000 negative lookups per process.

| ABBA slot | Elapsed ns | Tree-owned bytes |
|---|---:|---:|
| A0 | 2,933,432,897 | 14,272 |
| B1, baseline again | 2,931,161,925 | 14,272 |
| B2, baseline again | 2,945,491,659 | 14,272 |
| A3 | 3,162,753,291 | 14,272 |

`100 × ((B1+B2)/(A0+A3) − 1) = −3.601146638731889%`. The failed block's shortest row is2931.162ms; the full qualification's shortest row is2385.990ms. Duration and memory therefore pass. The final A slot is longer, but the record does not establish the cause of that difference. Do not drop that row, substitute a median, reinterpret the apparent A/A gain as candidate improvement, or retry the unchanged phase.

All85 commands succeeded and have matching successful postflight identity/lease/isolation records. The full row grid, individual stdout, command arguments, return codes, operation/hit/score models, memory, ordering, source/referee hashes and original-provenance hashes agree. The [wrapper result](../H2-confirmation/arm/H2-lto-confirmation-43/confirmation-result.json) correctly records `PARK`, stage `aa`, `comparison_executed=false`, `source_adoption=false`. No ARM seed43 comparison rows, comparison commands or comparison report exist. Its supplemental guard phase was not run.

The original private AA file SHA256 is `126f33a6261bf956e064cd0d15e8cee319e52c74b8bd3da46caf0ba1c7729b9b`; qualification JSON is `6bf8d60143fb673b05588b8a8407972b22b4c3590855d30bcc6be787c0edf154`; wrapper result is `0ab5ad6482fab14987c5a875d5030773d64d74c2a9db539e76b135f4027eefef`. Public sanitized captures retain their separate provenance manifests. One audit assertion initially expected uppercase stage `AA`; the recorded lowercase `aa` is valid. Correcting that audit expectation changed no evidence or gate.

## Complete confirmation record

The [admission protocol](../H2-CONFIRMATION.md) requires fresh qualification for each seed, three ABBA blocks per case, ARM hit improvement≥2% in every block, every other elapsed/memory guard≤1%, and every row≥250ms. Intel is the separately registered portability cohort: every case, including hit, must stay≤1%; Intel need not improve by2%. The earlier independently qualified native comparisons remain transfer evidence, not controls for these GCC15/LTO confirmations.

I reconstructed all864 completed rows:468 A/A and396 candidate-comparison rows. Each completed eleven-case host/seed contributes264 rows; ARM seed43 contributes only its72 control rows. The intended missing ARM candidate/guard stages are absent, not treated as passes.

**Cross-host stopping limitation:** both complete four-phase host sequences had been launched in advance. Each driver gated its own preceding phase; there was no cross-host failure barrier. Recorded host timestamps put Intel seed43 guard start13.426seconds after ARM's failed A/A report finished. The controller reports first observing the ARM PARK later, when Intel guard A/A already had43/60rows, and then allowed that in-flight phase to finish without admitting another H2 sequence. “Previously admitted” therefore describes the prior chain launch, not a guard phase already executing when ARM failed. This is a deviation from a global interpretation of the stop-after-failure rule and must remain visible. The retained post-failure Intel phase cannot rescue ARM or support H2 acceptance; this review's PARK does not depend on treating that phase as newly eligible acceptance evidence.

| Host / seed | Six-case A/A delta range % | Five-guard A/A delta range % | Hit candidate delta range % | Largest other candidate delta % | Shortest row ms | Disposition |
|---|---:|---:|---:|---:|---:|---|
| ARM29 | −0.432948…+0.285405 | −0.132312…+0.175963 | −5.312964…−5.136019 | +0.097839 | 1129.991 | All11 cases pass |
| ARM43 | One failure:−3.601147 | Not run | Not run | Not run | 2385.990 | PARK at A/A |
| Intel29 | −0.136180…+0.155760 | −0.220033…+0.272110 | −4.813100…−4.732384 | +0.277743 | 1308.328 | All11 cases pass |
| Intel43 | −0.112802…+0.170612 | −0.134701…+0.195593 | −5.659787…−5.458430 | +0.298244 | 1308.570 | All11 cases pass |

Negative elapsed deltas favor the candidate. Every completed candidate block passes its appropriate directional bound; these ranges do not pool hosts, seeds or compiler cohorts. Each host/seed's largest other delta is forward iteration. All measured candidate/base tree-owned memory endpoints are exactly equal. Supplemental guards compare both pre-loop and immediate post-loop memory; the later post-validation endpoint does not replace the immediate endpoint or establish transient peak memory.

Raw records: [ARM29 lookup](../H2-confirmation/arm/H2-lto-confirmation-29/comparison.jsonl), [ARM29 guards](../H2-confirmation/arm/guards-gcc15-lto-confirmation-29/comparison.jsonl), [ARM43 controls](../H2-confirmation/arm/H2-lto-confirmation-43/aa.jsonl), [Intel29 lookup](../H2-confirmation/intel/H2-lto-confirmation-29/comparison.jsonl), [Intel29 guards](../H2-confirmation/intel/guards-gcc15-lto-confirmation-29/comparison.jsonl), [Intel43 lookup](../H2-confirmation/intel/H2-lto-confirmation-43/comparison.jsonl), [Intel43 guards](../H2-confirmation/intel/guards-gcc15-lto-confirmation-43/comparison.jsonl). Each has adjacent controls, commands, per-process stdout/stderr, metadata and decisions.

The audit checks unique measurement commands, exact ordered case/block/slot grids, serial nonoverlapping measurement intervals within each phase, A/A completion before comparison, CPU2 launcher, binary path/hash, seed, sweeps and successful returns. Lookup outputs match the independent500-member operation/hit/score model. Guard outputs additionally match the integer-derived iteration/rank/churn item counts, rank sums, score sums, weighted sums and mutation-call counts. No comparison was synthesized from an analysis summary. The retained1158 seed29 files were rehashed after the failed seed43 control and remain byte-identical.

The original four host/compiler cohorts remain covered by [the readiness audit](H2-INDEPENDENT-READINESS.md): complete qualified controls, original six-case B comparisons and five affected-operation guards. A's memory failure and C's ARM LTO iterator regressions remain disqualifying; none is rehabilitated by B's evidence. Confirmation phases and seeds are stages of this one H2 population, not additional accepted populations or separate qualification ledger entries.

## Immutable identity and collector review

The upstream baseline remains `ee8e7f70152404649ac947157fd662d11b4a00d5`, with C SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. Every H2-B join resolves to revision1 C SHA256 `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29`. The header is unchanged at `e1575e812cdff6fae794c4dd619a4d6d7c586c5df01ac0c881376acd294161ac`.

Independently hashed saved GCC15/LTO executable bytes:

| Architecture / executable | SHA256 |
|---|---|
| ARM lookup baseline | `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb` |
| ARM lookup B | `283263f631cbc1440c1c688537edc8eb894de90cba86107d63faa3e68ca7a1f4` |
| ARM guard baseline | `b5bfd9166d5bd7d7b2a720f8177a9a8f8e755a5f314c8a547248ca304bc9a146` |
| ARM guard B | `1200a7358ed1d69b4b7c7dfe8dd71a4d4d90f7dca6b9ddfc4d1302649a4e1f0b` |
| Intel lookup baseline | `1d64647324ba83427c4eab71196e7d136ee566bd03b3c1b3b7acc9ae5ffe3868` |
| Intel lookup B | `0b6365ed258752de05af80434f8e85feb30ac833e3bba76ce93ff9e28375b293` |
| Intel guard baseline | `a7c25483af84443319cd894a424a0a9c36dd951d9bbbc1bdda0cd47432190e31` |
| Intel guard B | `54d7d9866ea1eff606dab9d3e904faee69aea25574b51feef00757f5235fa48b` |

These bytes agree with the fresh metadata and row labels, original cohorts and prior live hash attestations. Lookup and guard executables are distinct builds. Both source and all eleven prospective source/referee/build pins were rechecked against local bytes. Each confirmation metadata's original-provenance hashes also match the saved original files.

The executed collector hashes equal the reviewed versions: six-case driver `1491e9dd9fede0f5c62ce5e04169a62b48626f04f56b799e6e47e3c1f7e2237b`; guard confirmation driver `72a0d1771c830becf95a8f7439378b9f88b2c689c214dcd8d2b7b2a386841a67`; guard collector `a1ddc7e99f7a03076757dd64f263a3c3dd6d4fc0501dc516a83a6a1306c09704`. See [hardening review](CONFIRMATION-HARDENING.md) and [independent readiness](H2-INDEPENDENT-READINESS.md) for exact admission, identity and negative-case review. The supplemental wrapper is less self-contained and trusts original derived reports; independent reconstruction of its actual origins and returned rows closes that gap for these specific phases. Its per-row lease checks and stage-entry Docker checks do not establish continuous isolation of every possible service. Successful checks never override a failed A/A block.

## Source semantics, maintenance and portability

Rereading the final patch found no new concrete semantic blocker beyond the bounded risks already documented in [H2-CODE.md](H2-CODE.md). B caches the packed-score reserve while packing leaf/external/shift flags into explicit masks. All four leaf-count writes and both score-width writes maintain the cache; copying/relocation preserves relative state, and external ownership still follows record tags. The maximum cached reserve776 fits `uint16_t`; shift0…63 fits its six bits. The original lookup matching/scanner/hash semantics and full moved-out/resize fields remain intact.

The maintained invariant is `score_bytes == zbtScoreLeafScoreBytes(count, score_bits)`. Future mutations can violate it if they bypass maintenance, so the focused cache/flag oracle should remain part of any eventual integration's regression coverage. Existing correctness evidence includes native/sanitizer suites, optional-output and external-record oracles, and the source reviewer's independently rerun focused sanitizer oracle. This review inspected that evidence without unnecessarily rerunning the same tests. It is bounded coverage, not exhaustive proof.

The64-bit footprint assertions are correctly scoped.32-bit execution and big-endian execution remain unvalidated; source reasoning and Intel portability do not erase those gaps. Performance guards cover the registered500-member fixtures and affected-operation loops, not every tree size, ownership history, rehash state or allocation peak. No Redis command/server, allocator integration or production performance recovery is claimed.

## Matched profile evidence and TMA classification

The [independent ARM audit](H2-ARM-PROFILE-AUDIT.md) reconstructs all48 process-user event rows and sample/ELF joins. Fixed-work native cycles/instructions change−4.914064%/−2.299854%; target LTO changes−5.149789%/−2.101198%. Every event reports100% scheduling. Counts include setup, warmup and cleanup; they are not pure steady-state operation costs. Branch misses increase, so these data do not show a branch-prediction improvement. The exact assembly replaces the count/width address arithmetic with the cached halfword load, supporting the intended mechanism without isolating its causal cycle contribution.

Native ARM sample files contain matching executable build IDs. ARM LTO executables have no GNU build IDs; their join rests on saved SHA256, capture/comparison metadata, mapped paths and matching machine words, not embedded executable sample fingerprints. Each ARM capture contains two negligible kernel-mode-labelled records despite user-filtered event attributes; no lost records were found. Their origin remains unresolved. Sampling percentages cannot be multiplied by unrelated stat totals to infer exact function costs.

| Qualified ARM pipeline-slot category | Baseline | B |
|---|---|---|
| Frontend_Bound | Unavailable | Unavailable |
| Bad_Speculation | Unavailable | Unavailable |
| Backend_Bound | Unavailable | Unavailable |
| Retiring | Unavailable | Unavailable |

All ARM child categories remain unavailable. The saved CPU-wide topdown output lacks sufficient attribution/formula/scheduling qualification; neither process counters nor Intel fractions supply those missing ARM values.

I reran the hardened Intel parser without writes on all four matched profiles; they pass its documented capture-quality checks. Parser SHA256 is `9d4b8b838cf2bb472b42bb1210f9de6c61999b9a635bbdcc083407d5d34396a3`. Its authorship overlap is disclosed above. All four actual Intel ELF byte hashes match profile metadata and original comparisons; the former self-audit's missing candidate-byte limitation is now closed. Intel LTO baseline/B also lack GNU build IDs. No independent embedded sample-file executable fingerprint is claimed here.

Intel Sapphire Rapids/8488C captures use topdown-profiler0.2.2, pmu-tools `2568760ffc9394ddaa7a71f0c39930e780cf2dca`, TMA5.1-full and perf7.0.14. Each column comprises three five-second captures/fifteen intervals, CPU2-wide with sibling50 offline, controllerCPU0 and bounded workload tick accounting. Native GCC13.3 and GCC15.2/LTO are separate cohorts. The [profile audit](H2-PROFILE-GUARD-AUDIT.md) retains raw captures, run identities, source/tool versions and scope details.

| Intel % total pipeline slots | Native base | Native B | LTO base | LTO B |
|---|---:|---:|---:|---:|
| Frontend_Bound | 3.100 | 3.127 | 5.387 | 4.693 |
| Fetch_Latency | 0.727 | 0.700 | 0.700 | 0.940 |
| Fetch_Bandwidth | 2.373 | 2.420 | 4.673 | 3.660 |
| Bad_Speculation | 6.033 | 6.300 | 6.833 | 7.100 |
| Branch_Mispredicts | 5.927 | 6.293 | 6.680 | 6.720 |
| Machine_Clears | 0.107 | 0.000 | 0.133 | 0.373 |
| Backend_Bound | 20.427 | 18.853 | 21.533 | 20.020 |
| Memory_Bound | 0.800 | 0.800 | 0.800 | 0.400 |
| Core_Bound | 19.627 | 18.060 | 20.733 | 19.620 |
| Retiring | 70.440 | 71.720 | 66.253 | 68.187 |
| Light_Operations | 67.680 | 68.527 | 63.107 | 65.080 |
| Heavy_Operations | 2.727 | 3.100 | 3.073 | 3.100 |

These are unweighted means of rendered interval fractions, not pooled raw-slot ratios. Root sums are100% within rounding; LTO baseline is100.006% at shown precision. Children use total slots; deeper memory children are unavailable. Aggregate `/proc` accounting is within the registered1% bound, with quantization/non-atomic snapshot limitations; it is not PID-exclusive or per-interval attribution. Raw underlying event counters and runtime model-selector proof are unavailable, so formula validation is limited to rendered units/partitions. Auxiliary process counters are fully scheduled and samples record zero loss, but fixed-window instruction totals cannot be divided by another run's operation count. Lower backend share is supporting context, not proof of the source change's isolated cause or a substitute for failed confirmation.

Own tool discovery found no callable cpu-perf `library_status`/`ask`. The controller's actual [shared consultation](../CONSULTATION.md) and ARM profile consultation are shared evidence, not this reviewer's calls. The library remained revision `deb5a0bac467`,3/287 sources and158 passages; generic retrieved tooling passages do not establish this workload's mechanism. Numerical conclusions derive from saved evidence. Detailed participant accounting remains private; exact model, token and monetary costs are unknown.

## Preservation and precise revisit condition

The prospective source/header snapshot and upstream-path patch were independently hashed, and the patch was reconstructed in memory against the frozen baseline to obtain the exact candidate bytes. Patch SHA256 is `0f4d190bcb6de74bad14e6bd216b6dddde80437d0708e4da6e49bed25754ae4b`. It remains a private preparation artifact, not an accepted `selected/` package. Historical root source and every frozen extraction remain preserved under [the snapshot policy](../OVERNIGHT.md); this review authorizes no source adoption.

Revisit only after diagnosing the failed baseline qualification and preregistering a concrete justified change to measurement conditions as a distinct protocol. Preserve this failed phase and all prior evidence. New conditions must first qualify their own baseline controls; any later candidate admission needs explicit scope and all required fresh target confirmations, affected-operation guards, portability/profile evidence and independent review under unchanged acceptance limits. An unchanged retry, replacing seed43, dropping its last row, relaxing±1%, or borrowing Intel controls is insufficient. A separately proposed service-exclusion baseline investigation is not an H2 confirmation pass and does not reopen this closed disposition by itself.

Final disposition: **H2 PARK; selected source NONE; accepted count unchanged.**
