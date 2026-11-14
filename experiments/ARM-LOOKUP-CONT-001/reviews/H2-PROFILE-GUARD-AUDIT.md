# H2-B profile, guard and confirmation readiness audit

Read-only artifact audit, 2026-11-14. **This is a self-audit: the reviewer implemented H2-B, including its portability revision, and did not implement H2-C. It cannot satisfy the independent acceptance-review gate.** No source adoption, collector modification, fleet access or new measurement occurred. The only authored artifact is this report.

**Result:** the saved B discovery comparisons and supplemental guards pass their registered numerical gates. All four matched Intel baseline/B profiles pass the hardened offline parser. B may advance to confirmation after the six-case confirmation driver is repaired and independently reviewed; the driver version reviewed below is blocked. The controller acknowledged the blocker and held execution. These findings do not constitute final acceptance or heldout confirmation.

## Raw joins and guard gates

Audited private directories under `build/arm-cont-private/`: `fleet/{H2-native,H2-lto,guards-native,guards-gcc15-lto}` and the corresponding four `intel-fleet/` directories. These are separate architecture/compiler cohorts, with separate controls. Negative elapsed-time deltas favor B. No cross-architecture raw-time comparison is made.

For each supplemental guard cohort, independently reconstructed all 60 A/A and 60 B rows from JSONL and individual stdout. Checked the exact five-case × three-block × four-slot grid; ABBA order; unique command stem; successful return; CPU2 launcher; binary path; seed17 and frozen sweeps; stdout/JSONL agreement; metadata binary hash; and empty measurement stderr. Recomputed each block's elapsed-time ratio and compared it with the saved report. Operations, mutation-call counts, items, ranks, score sums and weighted sums agree within each block. Before/after/after-validation owned-byte endpoints are identical within each block, including baseline/B; the advertised endpoint memory change is exactly zero.

All 240 A/A rows and 240 B comparison rows pass. Every A/A block is within ±1%; every B block is ≤1%; every row exceeds 250 ms. Frozen guard harness/build-script bytes independently hash to `guards/FREEZE.json` and each cohort metadata. All B source identities are the final revision1 hash below, rather than the prior unconditional-assertion revision.

| Guard case | ARM native B delta range % | ARM GCC15/LTO | Intel native | Intel GCC15/LTO |
|---|---:|---:|---:|---:|
| Iterator forward | −0.5154…−0.5011 | +0.0943…+0.1097 | +0.2162…+0.7411 | +0.2320…+0.2790 |
| Iterator reverse | −1.2697…−0.7571 | −0.0175…+0.0279 | +0.0241…+0.4001 | −0.9577…−0.6700 |
| Rank forward | −4.9626…−4.2572 | −5.2224…−5.1851 | −4.7775…−4.2473 | −5.0834…−4.8640 |
| Rank reverse | −4.7763…−4.4586 | −5.2014…−4.8675 | −4.7464…−4.5585 | −5.2023…−5.0176 |
| Churn | −2.9135…−2.8384 | −1.8397…−1.8036 | −4.1243…−3.9984 | −0.3344…+0.0023 |
| Shortest A/A row, ms | 1378.037 | 1130.100 | 1863.080 | 1308.529 |
| Shortest B comparison row, ms | 1361.986 | 1130.118 | 1862.558 | 1308.600 |

The four six-case B comparisons were additionally reconstructed: 288 rows, exact six-case/block/slot grids, individual stdout and successful command joins, metadata hashes, seed and scale, equal hits/score sums/ops/owned bytes, and successful saved per-case verification. Unlike the supplemental guard harness, the six-case measurement JSON does not contain `verified` or `sweeps`; verification is a separate saved command and sweeps come from its measurement argv. This distinction was retained in the audit.

| Six-case B delta range % | ARM native | ARM GCC15/LTO | Intel native | Intel GCC15/LTO |
|---|---:|---:|---:|---:|
| Hit | −4.818…−4.785 | −5.396…−5.148 | −4.311…−3.543 | −5.824…−5.326 |
| Score | −5.467…−4.916 | −5.797…−5.578 | −5.484…−5.143 | −5.500…−5.363 |
| Miss | −0.790…−0.771 | −4.115…−0.197 | −0.059…+0.113 | −0.504…−0.399 |
| Long | −2.038…−1.977 | −3.144…−3.059 | −2.141…−1.767 | −2.188…−1.710 |
| External | −1.708…−1.614 | −1.683…−1.655 | −2.127…−1.827 | −1.340…−1.275 |
| Update | −4.833…−3.671 | −3.691…−3.453 | −3.305…−3.188 | −3.370…−3.147 |
| Shortest row, ms | 471.75 | 2295.07 | 2057.55 | 1971.70 |

Every hit block exceeds the 2% discovery improvement requirement and every remaining case stays within 1%. Six-case owned bytes are identical within every block. This audit rechecks the supplemental guards' own A/A rows; it does not independently reconstruct the earlier six-case A/A qualification history. Each six-case commands log contains two `affinity-zero-work` entries from its build/measure stages; the timing-command stems are unique. An initial overly broad audit assertion rejected that harmless command-log duplication; the corrected check requires uniqueness for each joined measurement, without discarding timing rows.

C's rejection remains in force. Its retained excluded-variant metadata cites the ARM LTO iterator regressions; B's result does not rehabilitate C or authorize missing excluded comparisons.

## Intel matched-profile identity and quality

Analyzed `intel-fleet/H2-profile-{native,gcc15-lto}-{base,B}` through the current `analyse_intel_profile.analyse()` entrypoint without writing analysis files. Hardened parser SHA256: `9d4b8b838cf2bb472b42bb1210f9de6c61999b9a635bbdcc083407d5d34396a3`. All four return `all_qualified=true`, including TMA, grouped counters, samples, report and provenance checks. This is the hardened parser, not the earlier parser whose broad qualification flag was criticized in `INTEL-TMA-BASELINE.md`.

Exact source identities:

- Baseline C: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`.
- B revision1 C: `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29`.

| Profile/cohort | ELF SHA256 |
|---|---|
| Native baseline | `2a38b93b94cfc59b347defaa3ccb5560f6bb7a70fbad92f350fbc5d74e00aebd` |
| Native B | `ff76b2b9e560cfaae0e48ca61f25d6f79c847cfad88df3bd5fcd6048e55eebd6` |
| GCC15/LTO baseline | `1d64647324ba83427c4eab71196e7d136ee566bd03b3c1b3b7acc9ae5ffe3868` |
| GCC15/LTO B | `0b6365ed258752de05af80434f8e85feb30ac833e3bba76ce93ff9e28375b293` |

The saved baseline ELF bytes were independently rehashed and match. Candidate ELF bytes are absent from the inspected `intel-fleet/bin` snapshot: their identity here is the matching profile/comparison metadata and workload-command path, not an independent rehash of candidate ELF bytes. Guard binaries are separately built executables; their source/harness joins must not be mistaken for equality with the lookup-profile ELF.

Machine/cohort: Intel Xeon Platinum8488C, Sapphire Rapids; kernel7.0.0-1017-aws; Ubuntu glibc2.39; native GCC13.3.0 and separate GCC15.2.0/LTO image `sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460`. Shared flags `-std=c11 -O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`; LTO adds `-flto=auto`. Collector topdown-profiler0.2.2, perf7.0.14, pmu-tools revision `2568760ffc9394ddaa7a71f0c39930e780cf2dca`. Formula/model evidence is the pinned Sapphire Rapids model and prior formula review; no formula inference is drawn from ARM.

All four profiles run the same validated 500-member hit fixture, seed17, 10,000,000 sweeps via `taskset -c 2 <matched ELF> measure hit 17 10000000`. Controller affinity is CPU0. The long workload is intentionally terminated after collection; it is not a completed timed-row denominator. Each profile has three five-second TMA captures, five intervals each; the actual command is `toplev.py -l2 -I1000 -x, --no-desc -v -C 2 -- sleep 5`. The launcher probe succeeds; the workload remains live, single threaded and identity-matched across captures. CPU50 is offline and Parca inactive at every recorded endpoint.

All 60 one-second TMA intervals have four unique roots, eight children and MUX. All values are finite, within range, correctly labeled `% Slots` or `% Slots <`, and fully scheduled. Root closure and child partition checks pass without rescaling. Every grouped process-user counter reports100% scheduling; all sample reports show zero loss and3003 samples. Capture commands return0. Scope snapshots span5.214–5.238 seconds for TMA; the counter window is approximately3.0006 seconds. The known NMI-watchdog advisory remains visible; no measured scheduling loss is hidden.

| Profile | TMA0 / TMA1 / TMA2 / counters / samples tick-accounting error % |
|---|---|
| Native baseline | 0 / 0 / 0 / 0 / 0 |
| Native B | 0 / 0 / 0.191571 / 0.330033 / 0.313480 |
| GCC15/LTO baseline | 0 / 0.191205 / 0.191205 / 0 / 0 |
| GCC15/LTO B | 0.191571 / 0.190840 / 0 / 0 / 0 |

These are aggregate `/proc` tick bounds across each capture, with quantization and non-atomic snapshots; they are not per-interval isolation proofs. TMA remains **CPU2-wide with workload accounting inside the registered1% bound**, not PID-exclusive attribution. Process-user counters/samples have their own scope and are not the TMA denominator. No underlying raw event-counter reconstruction or runtime model-selector proof is available from the rendered TMA CSV.

## Pipeline Slots (100%) — matched Intel baseline and B

Each column below is a separate pipeline tree. Values are unweighted means of fifteen displayed interval percentages; they are not pooled slot-count-weighted fractions. Children are shares of total pipeline slots. Mean roots retain rounding residuals: native baseline100.000%, native B100.000%, LTO baseline100.006%, LTO B100.000% at the displayed precision. No L1/L2/L3/DRAM memory children were collected, so those are unavailable.

| Pipeline category, % total slots | Native baseline | Native B | GCC15/LTO baseline | GCC15/LTO B |
|---|---:|---:|---:|---:|
| Frontend_Bound | 3.100 | 3.127 | 5.387 | 4.693 |
| ↳ Fetch_Latency | 0.727 | 0.700 | 0.700 | 0.940 |
| ↳ Fetch_Bandwidth | 2.373 | 2.420 | 4.673 | 3.660 |
| Bad_Speculation | 6.033 | 6.300 | 6.833 | 7.100 |
| ↳ Branch_Mispredicts | 5.927 | 6.293 | 6.680 | 6.720 |
| ↳ Machine_Clears | 0.107 | 0.000 | 0.133 | 0.373 |
| Backend_Bound | 20.427 | 18.853 | 21.533 | 20.020 |
| ↳ Memory_Bound | 0.800 | 0.800 | 0.800 | 0.400 |
| ↳ Core_Bound | 19.627 | 18.060 | 20.733 | 19.620 |
| Retiring | 70.440 | 71.720 | 66.253 | 68.187 |
| ↳ Light_Operations | 67.680 | 68.527 | 63.107 | 65.080 |
| ↳ Heavy_Operations | 2.727 | 3.100 | 3.073 | 3.100 |

Observed root ranges, baseline then B, native: Frontend3.1–3.1 then3.1–3.5; Bad_Speculation5.9–6.3 then6.3–6.3; Backend20.3–20.8 then18.7–19.2; Retiring70.2–70.6 then71.4–71.8. GCC15/LTO: Frontend5.1–5.5 then4.6–4.7; Bad_Speculation6.7–7.1 then7.1–7.1; Backend21.2–21.6 then20.0–20.3; Retiring66.0–66.5 then68.0–68.2. These are observed ranges in three serial captures, not confidence intervals or an interleaved causal experiment.

Backend/core fractions decrease within both compiler cohorts, consistent with the declared address-dependency hypothesis. That is supporting evidence, not proof that every changed slot comes from that dependency. Native frontend share is essentially unchanged; LTO frontend share decreases but its fetch-latency child rises. Bad-speculation share increases in both. A higher retiring fraction alone does not establish a speedup. The next falsifiable test is fixed-source heldout timing: losing the registered hit/guard thresholds would reject acceptance regardless of these attractive fractions. A later qualified matched capture without the backend/core direction would weaken the mechanism interpretation.

## Process counters and samples

| Counter window | Cycles:u | Instructions:u | Instructions/cycle within window | Running duration ns |
|---|---:|---:|---:|---:|
| Native baseline | 11,392,626,492 | 50,702,998,787 | 4.450510 | 3,000,577,076 |
| Native B | 11,393,113,725 | 51,479,287,522 | 4.518456 | 3,000,596,732 |
| GCC15/LTO baseline | 11,393,513,211 | 48,099,333,219 | 4.221642 | 3,000,721,114 |
| GCC15/LTO B | 11,393,133,933 | 49,383,017,658 | 4.334454 | 3,000,644,963 |

These are **within-window IPC**, never instructions/operation. The counters cover an attached interval while the workload continues; there is no exact completed-lookup count for those intervals. Dividing by a separate timed row's operations or the launch's total planned sweeps would be invalid. A larger instruction count in a fixed interval can reflect more work completed.

Whole-process user-cycle sample shares: native leaf helper29.33%→26.99%, raw lookup21.38%→22.36%; LTO leaf helper31.69%→31.82%, raw lookup19.42%→17.48%. They are sample fractions with changing denominators, not isolated function timings. The library report contains unresolved libc addresses; `memcmp@plt` must not be presented as all comparison work. No ARM sample percentage is substituted into this Intel result.

## Raw checksum anchors

The source directories above preserve full command/scope/stdout/stderr sets and `hit.data`. TMA stderr SHA256 values below identify the exact CSV inputs in capture order0/1/2:

| Profile | SHA256 values |
|---|---|
| Native baseline | `b8ed6e7a201f6380c6b11a1edbcdda701fdff404525d313f060f05b992824f0f` / `b20bba0705dafe4a22f7edbbfd291aa6f272d2d12377194ddec809443b740f75` / `51e321678fb3b25b966c9bd9fb598daacb450d29c8f9fa965e1c2beaebc8b561` |
| Native B | `841f2ea0218a882d0a85c77ed0915881213570778fb05a3b3012e96a07a309cc` / `cf84c2add81e9102ec4f34d9bfeb37b5fdded5068a80c56928fdbe76a16c2f0b` / `1dd347b9a5870e95387c8b8d63c75be67df3246f26b4675e873c9a9a379e8e5e` |
| GCC15/LTO baseline | `ad95e33e83ddfb84e5bbf9c8b67ce7cb472fff59db5e9a4d296a47609f0ef25c` / `94d3fae076984a38d55b33b4521ab7bdceac2a05b73932df53a3df4dec1eb162` / `9ae15eb2ab3d9be52ee8acad934a9a512bc4842b3520d13e55456262d7ea5e5a` |
| GCC15/LTO B | `5d1994786ca767e4ca4cc6fb3a312b2cee55cea158a60f323c090d803de6c731` / `2efb2aeee7c732957ef720e685d3354caa9b035ec473fc6dff6e4d659c48c8c3` / `e810d891364c0a1d269b7ea2395b1444f34819e2d0023afbfd30df5d41afd4c8` |

## Confirmation driver review before execution

Reviewed six-case `fleet_confirmation.py` SHA256 `20406fad12215890d512f24cca157f1a0d0ceae6bdcc7a260ffd3d499765bfd8`: **BLOCK**. It verifies its supplied ELF hashes and runs fresh A/A, but it does not bind confirmation to an eligible selected B source/cohort/original comparison. `--source-sha256` is merely copied into metadata; arbitrary variant/binary/phase arguments are accepted; original selection, qualification and exclusions are not checked. A failed heldout can be retried using a different phase name. The invoked `fleet_compare.py` is not checked against a reviewed hash; its measurement stage lacks the stronger per-run coordinator identity, SMT/Parca and lease checks used by the guard collector. Confirmation work scale is selected by CLI rather than required to match a frozen origin. A successful collector exit also does not itself produce a checked heldout acceptance decision. These are orchestration weaknesses, not evidence that the saved discovery rows are wrong.

Required before execution: bind an immutable selected origin/source/ELF/cohort/work scale; check original complete qualifying grids and exclusions; consume each frozen origin/seed once, preserving partial/failed attempts; pin the actual collector; maintain required live-lease/isolation checks; and evaluate the complete returned heldout grid with fixed thresholds. A separate worker is handling the repair, followed by independent review. Any new driver hash needs its own review; this block applies to the bytes identified above.

Reviewed `fleet_guard_confirmation.py` SHA256 `72a0d1771c830becf95a8f7439378b9f88b2c689c214dcd8d2b7b2a386841a67`: no new execution blocker found in this self-review. It binds the seed17 origin, frozen case work, complete original B guard grid, source/referee/ELF hashes, exclusion state and supplied reviewed collector hash; consumes deterministic origin+seed output before launching; parks failed fresh A/A; and validates the expected15-block/60-row B comparison. It checks owned lease, cleanup timer, coordinator PID/start identity/stopped state, controller affinity, Docker absence, and Intel sibling/service state before actions. The collector repeats lease/isolation checks per row.

Guard collector reviewed SHA256 `a1ddc7e99f7a03076757dd64f263a3c3dd6d4fc0501dc516a83a6a1306c09704`. This differs from the earlier `FREEZE.json` collector pin, reflecting the retained exclusion-aware collector revision; the confirmation driver's explicit reviewed collector pin must be this approved revision, not an assumed match to the older freeze. Harness and build-script freeze hashes match. As with any path-based driver, a trusted operator could manufacture another origin directory; the deterministic-phase protection applies to the genuine frozen origin and is not a tamper-proof global attempt ledger. Raw confirmation joins and independent final review remain required after execution.

## Limits and consultation provenance

This report does not re-review all source mutation invariants, reproduce candidate ELF bytes unavailable in this snapshot, validate32-bit compilation, audit all historical six-case qualification failures, or supply independent acceptance review. H2-B's source portability repair scopes64-bit footprint assertions; the original32-bit toolchain gap remains a gap. No performance claim about unsupported architectures follows from these Intel captures.

Own active-tool discovery exposed topdown tools but no directly callable cpu-perf `library_status`/`ask`. The controller's actual metadata consultation under `build/arm-cont-private/metadata-consult/` is shared provenance, not this worker's invocation: limited library coverage and no retrieved passage supporting the proposed mechanism. The evidence for the observed fractions is the raw matched Intel collection and inspected parser/model methodology. Detailed backend provenance remains private; model/cost usage is unavailable. No source or collector was adopted or modified by this audit.
