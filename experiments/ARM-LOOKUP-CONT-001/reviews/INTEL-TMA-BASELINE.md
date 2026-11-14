# Independent Intel v3 baseline TMA review

Reviewed 2026-11-14 02:04 UTC by the independent reviewer. Exact model, token usage and cost are unavailable. No new measurements, fleet access, timing analysis, collector/parser edits or commits were performed.

**Decision: both v3 baselines qualify under the registered CPU-wide scope and scheduling gates. No blocking defect was found in these captures.** This is a baseline classification decision, not candidate acceptance or proof of exact per-process TMA attribution. The author's `all_qualified=true` is narrower than its name suggests; the additional independent checks below are necessary to support this conclusion.

## Provenance and scope

Reviewed [collector](../fleet_intel_profile.py), [parser](../analyse_intel_profile.py), [cohort protocol](../INTEL-COHORT.md), [TMA reporting rules](../../../docs/TMA-REPORTING.md), the pinned Sapphire Rapids model, and private raw directories `build/arm-cont-private/intel-fleet/profile-native-v3` and `profile-gcc15-lto-v3`. Raw files remain private and unchanged.

Both profiles use Intel Xeon Platinum 8488C (Sapphire Rapids), CPU2 with sibling CPU50 offline, controller CPU0, and the Parca service inactive at every capture endpoint. The collector also checks no running Docker containers before launching. The actual zero-work `taskset -c 2` launcher probe succeeds; workload snapshots independently confirm affinity `{2}` and a live, single-thread process with unchanged process identity during each capture.

The workload is the frozen `hit`, seed17, 500-member fixture, launched with 10,000,000 sweeps and intentionally terminated after collection. Both verification commands succeed and report 14,272 owned bytes. Workload stderr is empty. TMA command is `toplev.py -l2 -I1000 -x, --no-desc -v -C 2 -- sleep 5`: CPU-wide, with no PID argument and therefore avoiding the documented wrapper CPU0 path. Each cohort has three five-second captures with five approximately one-second windows each. Scope snapshots bracket slightly more than the five seconds of counter collection.

Source is `ee8e7f70152404649ac947157fd662d11b4a00d5`; C SHA256 is `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. Native is GCC13.3.0; LTO is GCC15.2.0, image `sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460`. Shared flags are `-std=c11 -O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`; LTO adds `-flto=auto`. Runtime is Ubuntu glibc2.39. Independent hashing of the saved ELFs matches both profile and baseline metadata:

| Cohort | Binary SHA256 |
|---|---|
| Native | `2a38b93b94cfc59b347defaa3ccb5560f6bb7a70fbad92f350fbc5d74e00aebd` |
| GCC15/LTO | `1d64647324ba83427c4eab71196e7d136ee566bd03b3c1b3b7acc9ae5ffe3868` |

Collector topdown-profiler0.2.2, perf7.0.14, kernel7.0.0-1017-aws, pmu-tools revision `2568760ffc9394ddaa7a71f0c39930e780cf2dca`, Sapphire Rapids TMA5.1-full. The local pinned model checkout is clean at that revision; every downloaded event-file hash matches [the manifest](../intel-tool-input-hashes.json).

## Formula and unit audit

The pinned `spr_server_ratios.py` defines all twelve collected categories in the `Slots` domain. Its event-counter path divides frontend bubbles minus dropped uops, backend-bound slots, and retired-uop slots by `TOPDOWN.SLOTS`; Bad_Speculation is the nonnegative residual. The fixed-metric path uses the corresponding `PERF_METRICS` slot fractions normalized by their root sum, with the frontend dropping correction. Both are slot models. Fetch latency is a slot fraction (six-wide pipeline in the event-counter path); bandwidth is frontend minus latency. Branch mispredicts and memory bound are slot fractions; machine clears and core bound are parent residuals. Heavy operations are a slot fraction; light operations are retiring minus heavy.

`% Slots <` is the verbose toplev below-threshold marker, not an unsupported unit or a conditional percentage. Children are shares of total slots, not shares of their parents. `MUX` has unit `%` and is correctly excluded from the funnel. The parser does not substitute branch-miss rates, IPC or sample percentages.

The saved output contains rendered metrics, not the underlying per-event counts or a dump of the runtime fixed-metric selector. Thus this audit verifies the pinned formulas, their units and output consistency, but cannot independently recompute each fraction from original counters or certify which of the model's two paths ran. Root closure is partly constructed by the residual formula and is not an independent accuracy proof.

## Independent quality checks

All 30 windows contain exactly four unique roots, eight unique children and one MUX row. Every slot value is finite and within 0–100. Every root sum is exactly100.0 at displayed precision. For each root, the two children sum to the root within0.1 percentage point, consistent with one-decimal rounding. No children, duplicated windows or unsupported rows were silently discarded. All six timestamps sequences are increasing and end at approximately5.001 seconds. Every row reports100% scheduling. The retained NMI-watchdog warning is advisory: watchdog remains enabled, but these rows show no multiplexing loss. No kernel setting change is needed to qualify these existing captures.

I recomputed busy ticks from the eight `/proc/stat` fields as total minus idle and iowait, and process ticks from `/proc/PID/stat` utime+stime. The recorded fields, identity, scope result and arithmetic agree for every capture:

| Capture | Native busy/process ticks; error | GCC15/LTO busy/process ticks; error |
|---|---:|---:|
| TMA0 | 525/524; 0.190476% | 522/522; 0% |
| TMA1 | 523/522; 0.191205% | 524/523; 0.190840% |
| TMA2 | 523/523; 0% | 523/523; 0% |
| Counters | 304/305; 0.328947% | 304/304; 0% |
| Samples | 321/320; 0.311526% | 320/320; 0% |

These pass the registered1% aggregate bound. Tick quantization and non-atomic snapshots explain why a process delta can exceed CPU busy by one tick; the bound is approximate, not an exact contamination percentage. It applies to each full bracket, not separately to each one-second window. Endpoint state checks cannot prove uninterrupted isolation. Consequently the correct attribution is **CPU2 activity with workload scope accounting within the registered bound**, not exact PID-exclusive slot attribution.

All TMA, counter, sample and report commands returned0. Grouped process-scoped user counters each report100% scheduling and equal running duration within a cohort. Both sample reports state zero lost samples and both collectors record3,003 samples. Their process/user scope differs from the CPU-wide TMA scope, so they remain supporting evidence rather than interchangeable denominators.

## TMA classification

Values below are unweighted means of fifteen displayed interval percentages, with observed ranges. They are not pooled slot-count-weighted fractions. No rounding residual has been rescaled.

| Total-slot category | Native mean [range] % | GCC15/LTO mean [range] % |
|---|---:|---:|
| Frontend_Bound | 3.100 [3.1–3.1] | 5.400 [5.4–5.4] |
| Fetch_Latency | 0.700 [0.7–0.7] | 0.700 [0.7–0.7] |
| Fetch_Bandwidth | 2.347 [2.3–2.4] | 4.700 [4.7–4.7] |
| Bad_Speculation | 6.167 [5.9–6.3] | 6.700 [6.7–6.7] |
| Branch_Mispredicts | 5.993 [5.9–6.3] | 6.700 [6.7–6.7] |
| Machine_Clears | 0.160 [0–0.4] | 0.000 [0–0] |
| Backend_Bound | 20.347 [20.3–20.4] | 21.600 [21.6–21.6] |
| Memory_Bound | 0.800 [0.8–0.8] | 0.800 [0.8–0.8] |
| Core_Bound | 19.547 [19.5–19.6] | 20.800 [20.8–20.8] |
| Retiring | 70.387 [70.2–70.6] | 66.300 [66.3–66.3] |
| Light_Operations | 67.653 [67.5–67.8] | 63.180 [63.1–63.5] |
| Heavy_Operations | 2.700 [2.7–2.7] | 3.020 [2.7–3.1] |

Rounded native root means total100.001%; underlying interval means total100%. No L3 memory children were collected. Candidate Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring are unavailable in this baseline audit; matched candidate captures are required before attributing any candidate change. These independent compiler cohorts must remain separate; a higher Retiring fraction does not establish a speedup.

## Resume provenance and parser limits

Native v3 TMA0's command JSON, scope JSON, stdout and stderr are byte-identical to v2. The retained stderr SHA256 is `35c734d2e28f1c3f88f20c70b5f7028606dd985a1e5d53ed02e85a5ccb0c3355`, matching `resume.json`. Old/new metadata agree on binary, tool revision/version, kernel, affinities and sysctls. TMA0 belongs to the earlier live workload; TMA1/2 and auxiliary captures belong to the new identical-binary workload. The previous process was intentionally terminated after the parser failure. This is the declared two-launch resume, not three uninterrupted windows from one PID. GCC15/LTO has no resumed capture. The initial invalid native launch and v2 parser failure remain preserved separately.

Additional stderr SHA256 values, in capture order:

| Cohort/capture | SHA256 |
|---|---|
| Native TMA1 | `c9787bb53e37eb6eb3dea6ac4c1d602410beff4665b6f1578b773dc6f89ea94c` |
| Native TMA2 | `90ecaff1683f3b1be705b0c950a0658b5ab1f3b5924cc3654437f024e776d3cd` |
| GCC15/LTO TMA0 | `a1d997b7c7d5bef33e58c3ccf710e5dbcef808f539f17fbfa6756870873fa3c2` |
| GCC15/LTO TMA1 | `e840c03b2f81abae3282c63501ea5d6791c04ce4b4c3d72eade0f9878248f9d5` |
| GCC15/LTO TMA2 | `dba43f499f2c6f8a19bddf0315a9a4e5c79d4e103637b8bd2bc8f2c11de9d630` |

The parser trusts `scope.pass`, does not validate child completeness/partition, and does not include counter/sample return status, scheduling or loss in `all_qualified`. Its advisory filter also skips every nonnumeric timestamp row. Those are automation limitations; the independent raw checks above found no corresponding actual capture failure. Future uses of the flag need those checks, rather than inheriting blanket qualification from this review.

The next falsifiable question is whether a candidate changes the proposed resource demand within its own matched compiler cohort. Failure to reproduce that directional change in qualified matched captures would challenge the mechanism; timing and guard gates remain separate.

## Consultation availability

This worker discovered the active tool catalog during the audit: topdown tools are exposed, but no cpu-perf `library_status`/`ask` tools are exposed directly. The controller's actual stdio cpu-perf consultation is consumed as **shared evidence**, documented in [CONSULTATION.md](../CONSULTATION.md): server0.1.1, bundled revision `deb5a0bac467`, limited coverage and no retrieved primary passage establishing a workload mechanism. No controller call is claimed as this worker's call. Formula evidence here is the inspected pinned pmu-tools primary source, not an unsupported library explanation.
