# Independent H4 final rejection audit

**REJECT all three implementations; source selection NONE.** A/C fail native ARM miss guards. B passes native ARM discovery but fails the independently qualified Intel miss guard in all three blocks. Neither the ARM gain nor static success permits waiving the1% portability guard. No target-LTO comparison, fresh confirmation or additional H4 guard timing is warranted.

This reviewer proposed an earlier index-filter hypothesis but did not implement H4-A/B/C or author their collectors. That proposal overlap is disclosed; this is an independent reconstruction of the measured rejection, not a claim of blind hypothesis review. The [prior ARM codegen review](H4-ARM-CODEGEN.md) was authored by H4-A's implementer and is not counted as author-independent review of A. Exact model, tokens and cost are unavailable. No fleet access, measurements, source/collector edits, commit or push occurred; only final review documents were written.

## Evidence and joins

Reviewed private `build/arm-cont-private/fleet/H4-native` and `intel-fleet/H4-native`:216 rows each,432 total,108 complete ABBA blocks. Reconstructed the exact three-variant × six-case × three-block × four-slot grids. Each row joins one successful measurement command and its identical JSON stdout, with empty stderr, CPU2 affinity launcher, correct baseline/candidate path, seed17, native cohort, fixed sweeps and recorded ELF identity. Command windows are serial within each cohort. Separate six-case verification commands succeed for every candidate.

Operations/hits/score sums match the fixture formula and agree within blocks; tree-owned bytes match exactly between baseline and candidate and remain reproducible per case/binary. Every row exceeds250ms: shortest ARM row488.620ms, Intel2101.613ms. Recomputed block effects and eligibility agree with the saved analysis. No row, first block or outlier was removed.

Original controls were independently reconstructed from `fleet/native-requalification` and Intel `baseline`:72 native rows/18 blocks per architecture. ARM A/A effects are−0.397978…+0.264268%, minimum495.198ms; Intel−0.631511…+0.441593%, minimum2127.005ms. All meet±1% and duration gates, with correct raw command/result/model joins. The control ELF hashes equal the H4 baseline hashes. ARM uses scale1, Intel scale5; the cohorts and elapsed times are not pooled. Earlier failed control attempts remain preserved and do not qualify these comparisons.

Baseline upstream is `ee8e7f70152404649ac947157fd662d11b4a00d5`, source SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. I independently hashed each isolated candidate source and all six newly supplied native ELFs; every hash matches both metadata and measurement rows. Nine frozen referee files per worktree, including lookup/build/qualification, header, compatibility and vendor sources, match the root referee byte-for-byte.

| Variant | Source SHA256 |
|---|---|
| A | `0ef8edf451945b24712a28add6c7b92ab250af24c3238ebb2fad8e352c763025` |
| B | `a1aef5b623a24fda5ed4a9a47c68fe7b29f75150f4cd996db640059221252fac` |
| C | `52cd1ce514806d3b7097dd0ca46ac8ff9a932e6a8c06c14ab04862d400193621` |

| Variant | ARM native ELF | Intel native ELF |
|---|---|---|
| A | `821ac6b6df2d0f6b7cbf73939a9d740eba90176cd970aed3338efb4504c5d076` | `93b756431072496482e2335633f9c540e413bbe3419d706fdf34de45460f8bf3` |
| B | `d4bfd7bbde2096af3219f7f95e3a9bea7c64cbb786819d7088f34a4ea8a99a22` | `e712d14c41ed397587e6e2da83a02c33fe4edb5cd64b277bde205e93bb6ff363` |
| C | `aa6795d727a79d7c1297589ae96a46f21db0b70d3bc1e68103c6542ab20809ca` | `202083a9eb1f020d0fec4ad04d9d2210076b48a0c1ce208ed9834f3b8344c380` |

## Decisive gates

Effects are100×(mean candidate elapsed / mean baseline elapsed−1); negative favors the candidate. Native ARM primary requires≤−2% in every block; every other guard and Intel portability case requires≤+1%, with the same memory bound.

| Variant | ARM hit range % | ARM miss range % | Intel miss blocks0/1/2 % | Final reason |
|---|---:|---:|---|---|
| A | −2.776…−2.310 | +7.151…+7.529 | +5.667302 / +5.765140 / +5.874171 | ARM miss failure |
| B | −2.518…−2.237 | −1.551…−1.281 | **+1.321529 / +1.370942 / +1.382719** | Intel portability failure |
| C | −2.327…−2.094 | +26.152…+26.419 | +19.491946 / +19.370284 / +19.526243 | ARM miss failure |

B's other ARM and Intel cases pass. Intel A additionally exceeds1% external lookup in two blocks; Intel C exceeds1% long and external lookup in all three. Those retained results reinforce rejection but are not needed to reject the ARM-ineligible A/C. Intel C's smaller hit gain is not itself a portability failure: the Intel rule is no>1% regression, not an extra2% speed objective.

Both saved H4 LTO build directories contain no comparison rows. Build/codegen artifacts and every losing patch remain preserved. A successful static boundary screen means only that the intended filter deferral was emitted; it does not establish acceptable miss-path cost. No pipeline cause is inferred from the elapsed regressions.

Raw comparison JSONL SHA256: ARM `56cf07fefa55053bd56e17015f2cc118a2aba70d4eac29833f32f5892f4a789a`; Intel `71162b13fb80c5af10e5f24325cd37277e9277805a44a4cc5a1e2ec2ca55c97f`. These anchors identify the complete retained populations, including losing blocks.

## TMA classification and scope

H4 ARM baseline/candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children are unavailable as qualified matched captures. H4 Intel candidate categories/children are also unavailable; no matched H4 candidate profile was collected.

For explicitly **unmatched earlier Intel baseline context only**, [the qualified native baseline audit](INTEL-TMA-BASELINE.md) reports the same native baseline ELF on Sapphire Rapids/CPU2: Frontend_Bound3.100%, Bad_Speculation6.167%, Backend_Bound20.347%, Retiring70.387%, totaling100.001% after rounding. Children in total-slot units: Fetch_Latency0.700%, Fetch_Bandwidth2.347%, Branch_Mispredicts5.993%, Machine_Clears0.160%, Memory_Bound0.800%, Core_Bound19.547%, Light_Operations67.653%, Heavy_Operations2.700%. These are unweighted displayed-interval means from three5-second captures, topdown-profiler0.2.2 / pinned pmu-tools `2568760ffc9394ddaa7a71f0c39930e780cf2dca`, with CPU-wide scope accounting and full scheduling. They cannot explain H4 deltas or substitute for missing candidates. The linked audit retains exact binary/raw checksums and scope limitations.

## Closure and consultation

Count H4 once as **one rejected ARM-led population**, including its Intel portability screen. It adds one attempt, one REJECT, one ARM and one population; no separate Intel replication, qualification or acceptance. Together with the separately audited H6 closure, the prior42/23PARK/19REJECT ledger becomes **44 attempts /23PARK /21REJECT /0 approved; ARM32 /Intel6 /AMD6;27 populations /5 replications /12 qualifications**. H2/H5 remain active and excluded.

Own fresh tool discovery found no exposed cpu-perf tools. The controller's H4-specific stdio consultation documented in [H4-selection.md](../H4-selection.md) is shared evidence; no other agent's calls are claimed as mine. Limited retrieval supplies no supported causal explanation for these regressions. The rejection follows the frozen gates and retained raw evidence.
