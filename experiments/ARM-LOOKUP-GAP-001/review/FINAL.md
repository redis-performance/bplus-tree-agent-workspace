# Independent adversarial review — final decision

**Concur: REJECT this optimization experiment; source selection NONE.** No variant passes the preregistered requirement that every primary discovery block improve by at least2%. No correctness defect was found. This rejects advancement under the experiment's gate; it does not establish that the change has no smaller benefit.

Reviewer: a separate Codex session, independent of the three proposers/implementers. Exact model, token and currency costs are unknown. The reviewer inspected saved files, source, assembly and raw outputs only; no fleet access, builds or performance measurements. The earlier review remains preserved in PRELIMINARY.md. Independent computations are in [final-audit.json](final-audit.json) and [preliminary-audit.json](preliminary-audit.json).

## Reconstructed results

All144 discovery rows join exactly to their individual stdout and successful command records. There are36 complete ABBA blocks; slots0/3 are baseline and1/2 candidate. Every row uses seed17 and50million operations, the shortest timing window is568.015ms, and checksums plus tree-owned bytes agree within each comparison. All48 baseline A/A rows and12 precision blocks independently reconstruct and pass.

Elapsed-time changes below are `(mean(candidate)/mean(baseline)-1)*100`; negative is faster.

| Variant | Primary median | Primary block range | Primary blocks passing≥2% | Largest guard slowdown |
|---|---:|---:|---:|---:|
| A | −1.394140% | −1.709261% to−1.174807% | 0/3 | +0.348614% |
| B | −1.527604% | −1.570803% to−1.417748% | 0/3 | +0.146210% |
| C | −1.840990% | −2.182287% to−1.480585% | 1/3 | +0.960722% |

Only1/9 primary blocks clears2%; none of27 guard blocks exceeds1%. The single qualifying C block does not permit selecting C or replacing its other blocks. No variant is eligible for fresh confirmation. Stopping before held-out-seed confirmation, selected-variant profiles and Intel measurements follows the frozen gate. Those phases must remain marked unexecuted, not passed or unnecessary for a future acceptance.

## Source, code and correctness

The five extracted source/vendor files match actual Git blobs at upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`, including manifest SHA256s. The controller's final fetch record at2026-11-13T22:43:51.801366Z records the same upstream tip and unchanged five files. This reviewer independently checked the local pinned Git objects; the live upstream fetch itself was performed by the controller.

All three retained patches apply cleanly to the exact baseline. Their source SHA256s match the comparison manifest; all three retained `.text` artifacts independently match their recorded hashes. The retained baseline ELF matches `d54311ffae324cf623a000f1c026f377c3657f5810c76cd1b2284645b9411431`. Candidate full-ELF hashes are supplied by the collector manifest; this review independently hashed their retained `.text` artifacts rather than claiming access to unretained local full ELFs.

The semantic assessment remains pass: A guards existing output work; B returns only after verified equality when neither output is requested; C computes mapping inside each requested output branch. None changes probing, hash/tag handling, decoding, member equality, allocation, layout, resize/scan behavior or assertions. The mapping is pure count/reverse arithmetic. Requested score and logical position remain unchanged. No new portability or undefined-behavior issue was found.

Retained qualification records show57 native and57 sanitizer upstream tests per build, plus12 native and12 sanitizer fixture cells per build. The original90,000-case optional-output oracle is preserved. Its shorter and256-byte cases exercise inline records, both orientations, all output masks, signed-zero score bits and misses. Oracle seeds17/30/43 differ intentionally from the timing confirmation seeds17/29/43; no claim should conflate them.

The preliminary coverage finding is resolved: the frozen256-byte timing guard is correctly described as inline with a16-bit length, since external storage starts at320. A separate384-byte correctness oracle explicitly asserts the external record tag and records45,000 successful sanitizer checks on baseline and each candidate. It preserves the original oracle/cohort and supplies no external-member performance result.

The recorded helper assembly supports the limited codegen statement: all three variants branch on the null score pointer before loading the reverse flag and computing the logical position, unlike baseline. Their sampled helper assembly is the same, while full text hashes differ. Static codegen cannot assign the observed elapsed changes exclusively to the removed work; no matched candidate counter/profile validation or confirmation ran after rejection.

## Measurement and scope limits

The fixture correctly isolates the current two-input membership API on500 distinct short members and two separately allocated trees. It does not reproduce the original Redis server, allocator/hash seed,64-set footprint, iteration, command dispatch or networking. No command-level parity or ARM-gap closure follows. No Intel performance or architecture-general improvement was established.

Baseline samples cover whole process lifetime and use all captured user-cycle sample weight, with zero reported lost samples. Unknown libc PCs remain unassigned. Baseline counters include setup, warmup and teardown; they are not exact loop-only counts. Actual perf version is6.17.13 despite the directory name. No selected-variant profile is available to validate a quantitative mechanism.

## TMA classification and consultation

| Category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Topdown-profiler0.2.3 captured L1 output labeled as slot-denominated through `-a -C2`, but labels alone do not validate its formulas, and this CPU-wide scope lacks continuous exclusion evidence. The report appropriately retains it as exploratory rather than a qualified process funnel. No children or candidate captures are qualified, and no stall-cycle/sample percentages were substituted for TMA.

Own tool discovery found no exposed cpu-perf/library_status tool. Following the documented worker provision, the reviewer consumed root's explicitly shared stdio library_status, ask, source-reading and reconsultation evidence in CONSULTATION.md. Those calls are not claimed as reviewer calls. None of the retrieved material establishes an execution-resource cause for these results. Rejection here is the arithmetic application of the frozen gate.

## Closure

No unresolved source, correctness, accounting or decision blocker remains for reporting this bounded experiment as REJECT/sourceNONE. Preserve the unexecuted confirmation/profile/Intel gates and all losing patches. Operational runner release is a separate controller responsibility; this reviewer has not queried the fleet. The reviewed controller proof [RELEASE.json](../RELEASE.json), timestamp2026-11-13T22:43:55.222696Z, records restored original coordinator identity, zero owned workload processes/benchmark containers, inactive owned work unit/release timer, unchanged PMU/SMT settings, and a subsequent fresh waiting heartbeat with pending=lag=0. Root also reports an independent parent live verification. This reviewer inspected that sanitized controller/parent evidence and did not perform a live fleet query. RESULTS.md and implementation-selection.md accurately report the rejected gate and unexecuted phases.
