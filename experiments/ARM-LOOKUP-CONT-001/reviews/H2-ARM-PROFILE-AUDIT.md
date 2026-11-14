# H2-B ARM matched-profile audit

**PASS as supporting profile evidence, with the identity and sampling qualifications below.** The process-counter values and all reported percentage changes in [H2-ARM-PROFILES.md](../H2-ARM-PROFILES.md) reproduce from the raw captures. The saved candidate code removes the intended metadata-address arithmetic. These observations support consistency with the hypothesis; they do not establish its isolated cause, fresh confirmation, portability or final acceptance.

Reviewer role: independent profile auditor; previously implemented a different H2 option, not H2-B. This review read already captured artifacts and saved executables only. Offline sample decoding and ELF inspection collected no new events and executed no workload. No source change, timing run, fleet access or publication action occurred. The audit program, detailed provenance and offline decoding records are retained separately in private evidence.

## Workload and artifact joins

Reconstructed all four profiles—native baseline/B and GCC15/LTO baseline/B—from their raw command logs, completion records, counter stdout/stderr, reports, sample files, full disassembly and saved ELF bytes. Each capture has ten unique successful commands. The three counter runs, sample run and exploratory topdown run all invoke the same profile ELF with `measure hit 17 400000`, pinned to CPU 2. The independent launcher-affinity check reports that CPU. The command suffix, rather than a comparison cohort's scale setting, establishes the profile's fixed work.

The [frozen lookup referee](../lookup.c) defines 500 members and 1,000 warmup sweeps before the 400,000 measured sweeps. Every one of the 20 workload outputs agrees with the independently derived model: case `hit`, seed 17, 200,000,000 reported operations, 200,000,000 hits, score sum zero and 14,272 tree-owned bytes. The zero score sum is appropriate for this no-score path. Initial fixture construction, checks, 500,000 warmup queries and cleanup belong to the process-counter scope but not the reported operation denominator. Existing source assertions validate setup queries and hit totals; this audit does not replace the separate source-correctness oracles.

Each actual saved ELF's SHA-256 equals its profile completion identity, the [analysis JSON](../H2-profiles/arm-analysis.json), and its corresponding comparison metadata identity. Source bytes independently hash to baseline `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9` and B revision 1 `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29`, as recorded by those joins. The metadata's upstream freeze remains `ee8e7f70152404649ac947157fd662d11b4a00d5`.

| Capture | Rehashed saved ELF SHA-256 | Executable build-ID join in sample file |
| --- | --- | --- |
| Native baseline | `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf` | `b6956469db975a8773ac6262bd9965a7e54eb68c` matches |
| Native B | `e16a70a4de79ede0bf177b2dd8bd2ddb3af4349c9e22509c8e5199d390a52cdd` | `2ffafe6b733026091d419641ecc27e2db92a64ca` matches |
| GCC15/LTO baseline | `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb` | Unavailable: ELF has no GNU build ID |
| GCC15/LTO B | `283263f631cbc1440c1c688537edc8eb894de90cba86107d63faa3e68ca7a1f4` | Unavailable: ELF has no GNU build ID |

The native sample files independently contain the matching executable build IDs. Neither LTO ELF has a GNU build ID, and neither LTO sample file contains an executable build-ID entry. The LTO join is therefore **saved ELF hash plus capture/comparison metadata, matching workload/mmap path and matching disassembly**, not an embedded sample-file fingerprint of the executable. This is a provenance limitation to retain whenever describing the four joins. None of these checks is a reproducible-build proof or an independent pre/post-run hash record for every counter invocation.

All 64,265 four-byte machine words printed in the four full disassemblies were compared directly with the saved AArch64 little-endian ELF load segments: 20,264 native baseline, 20,220 native B, 12,025 LTO baseline and 11,756 LTO B. Every word matches. These are static artifact-integrity counts, not dynamic instruction measurements. DWARF producers identify GCC 13.3.0/O3 for both native binaries and GCC 15.2.0/O3 with LTO for both target binaries. The two toolchains are distinct cohorts; their defaults are not interchangeable controls.

For each capture, all 23 original-artifact checksum entries—including sample data—match the retained raw bytes, and all 22 published checksum entries match the sanitized public files. See the per-capture [native baseline](../H2-profiles/arm-native-base/ORIGINAL-SHA256.json), [native B](../H2-profiles/arm-native-B/ORIGINAL-SHA256.json), [LTO baseline](../H2-profiles/arm-gcc15-lto-base/ORIGINAL-SHA256.json) and [LTO B](../H2-profiles/arm-gcc15-lto-B/ORIGINAL-SHA256.json) manifests and adjacent `PUBLISHED-SHA256SUMS` files.

## Independently recomputed counters

Parsed all 48 event rows: four events × three complete repetitions × four captures. The events are process `cycles:u`, `instructions:u`, `branches:u` and `branch-misses:u`; every raw scheduling field is 100.00%. Each raw row, reported operation count and median equals the saved analysis JSON. Changes below use `100 × (candidate median / baseline median − 1)` separately by event and cohort.

| Cohort / event | Baseline median | B median | Recomputed change |
| --- | ---: | ---: | ---: |
| Native cycles | 16,746,594,521 | 15,923,656,136 | −4.914064% |
| Native instructions | 70,027,849,445 | 68,417,311,497 | −2.299854% |
| Native branches | 11,348,147,444 | 11,146,841,282 | −1.773912% |
| Native branch misses | 10,705,978 | 10,936,374 | +2.152031% |
| GCC15/LTO cycles | 16,847,040,601 | 15,979,453,483 | −5.149789% |
| GCC15/LTO instructions | 67,029,402,188 | 65,620,981,836 | −2.101198% |
| GCC15/LTO branches | 11,339,711,626 | 11,339,705,129 | −0.000057% |
| GCC15/LTO branch misses | 14,156,115 | 14,213,736 | +0.407040% |

The assessment's three-decimal rounding is correct. Its LTO branch entry `−0.000%` means a negligible nonzero difference, not exact equality. Branch misses increased in both cohorts; these data do not support a branch-prediction improvement claim. Ratios of median misses to median branches are about 0.09434%→0.09811% native and 0.12484%→0.12534% LTO, without establishing a causal contribution.

These are whole-process user-event totals under fixed work, not paired ABBA elapsed comparisons, a confidence interval or pure steady-state per-operation costs. Three repetitions provide useful consistency checks but do not isolate drift, sample uncertainty or generated-code causes. No counter reduction overrides a failed timing guard or pending confirmation. `100.00%` is the reported event scheduling evidence; it does not prove continuous CPU isolation or a qualified pipeline-slot denominator.

## Sample quality

Offline decoding of each complete sample file confirms the capture command's user-filtered cycle event at requested frequency 999, with `exclude_kernel=1` and `exclude_hv=1`. Actual sample records agree with the original record logs, and period sums equal the event-count totals in the original reports. No lost-event record was found; the reports also state zero lost samples.

| Capture | Decoded samples | Lost records | Kernel-mode-labelled samples | Their summed period |
| --- | ---: | ---: | ---: | ---: |
| Native baseline | 5,999 | 0 | 2 | 25 |
| Native B | 5,704 | 0 | 2 | 2 |
| GCC15/LTO baseline | 6,089 | 0 | 2 | 25 |
| GCC15/LTO B | 5,726 | 0 | 2 | 26 |

The remaining records are user-mode-labelled. Each kernel-labelled contribution is below 0.000001% of that file's summed sample periods and appears as rounded 0.00% unknown-kernel entries in the saved reports. Record this small scope nuance rather than asserting literally every sampled IP is userspace. The audit does not diagnose its origin or reinterpret it as evidence of kernel counter collection; the event attributes explicitly request user-only counting.

Fewer samples for B are unsurprising under frequency sampling over a shorter completed process and are not independently a speed metric. Hotspot percentages use each profile's own total: native leaf share changes 42.20%→39.15% while raw lookup changes 22.41%→25.33%; LTO leaf share changes 46.63%→42.89% while the no-score raw clone changes 22.18%→23.15%. Rising relative raw-lookup share is not proof that that function became slower. Symbol percentages and the separate stat runs must not be combined as exact function-cycle accounting. Sample density, imprecise sampled IPs, setup/warmup, libc work and unresolved addresses remain limitations.

## Mechanism evidence and causal limits

The exact native baseline [assembly](../H2-profiles/arm-native-base/assembly.stdout):2927–2940 loads score width/count and computes the packed-score byte displacement through branch/multiply/add/shift/mask operations at `0x3758`–`0x376c`. The native B [assembly](../H2-profiles/arm-native-B/assembly.stdout):2386–2394 instead loads the cached halfword at offset 22 (`0x2eec`) and forms the offset/tag addresses directly. Both use data-base displacement `0x38` and a 128-byte leaf-helper frame.

The target baseline [assembly](../H2-profiles/arm-gcc15-lto-base/assembly.stdout):4390–4402 contains the corresponding multiply/shift/add/mask/select chain (`0x404bf0`–`0x404c04`). Target B [assembly](../H2-profiles/arm-gcc15-lto-B/assembly.stdout):3296–3305 substitutes the halfword load at `0x403afc` and direct address formation, again retaining data displacement `0x38` and a 128-byte helper frame. The saved patch's footprint assertions retain the 24-byte node and 56-byte leaf prefix on these 64-bit builds; all profile rows retain the same tree-owned-byte observation.

This verifies the intended generated-code change and makes the instruction reduction plausible. It does **not** isolate the larger cycle reduction as address dependency latency. B also packs node flags and changes generated code outside that sequence; scheduling, register allocation, layout and branch behavior may contribute. Executable text changes 95,143→99,183 bytes native and 56,539→55,379 bytes LTO, so the result is not uniformly a smaller-code effect either. Executable text is distinct from the tree-owned-memory gate. No cache, frontend, backend or speculation bottleneck is proved here.

## TMA, consultation and disposition

| Qualified pipeline-slot category | ARM baseline | ARM H2-B |
| --- | --- | --- |
| Frontend_Bound | Unavailable | Unavailable |
| Bad_Speculation | Unavailable | Unavailable |
| Backend_Bound | Unavailable | Unavailable |
| Retiring | Unavailable | Unavailable |

All child shares remain unavailable. The saved topdown command is CPU-wide `perf stat --topdown -I1000 -x, -a -C 2` around the workload. Its rendered root percentages do not supply the necessary process attribution, continuous-isolation, underlying formula/exclusion and scheduling qualification. Their sum does not repair these omissions. The process-user counters and zero-loss samples are different captures and cannot qualify that CPU-wide CSV. The assessment correctly keeps ARM TMA unavailable and does not borrow Intel's classifications.

Own tool-catalog discovery found no callable cpu-perf/library_status endpoint. The controller's actual shared profile consultation supplied these workload identities, counters and caveats. Its source library remains revision `deb5a0bac467`, 3/287 sources and 158 passages. The two retrieved pmu-tools feature/release passages describe tooling; neither establishes the cause of this workload's change. The unrelated suggested benchmark is not validation for this machine. The assessment's limited inference is justified by its own assembly/counters, not retrieved authority. No new consultation is claimed by this reviewer; detailed participant accounting remains private and unknown costs remain unknown.

No numerical or checksum discrepancy requiring rejection was found. Retain the LTO build-ID limitation, two negligible kernel-labelled records per sample file, whole-process counter scope and unavailable ARM TMA alongside any summary. Fresh held-out confirmation, complete timing/guard review, source-correctness acceptance and final independent review remain separate gates. This audit supports the matched ARM profile assessment only; it does not declare H2-B accepted or any server-level performance gap recovered.
