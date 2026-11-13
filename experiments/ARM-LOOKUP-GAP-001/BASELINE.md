# Qualified current-unstable baseline

Source/referee commit `4876d21ce62fdf9306572b690c891d2d5ed0e04d`, upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`. All 48 A/A rows and 12/12 ABBA blocks pass the registered ±1% gate, across primary and all three guards. No retries. Complete per-process rows, commands, binaries, hashes and scope: [baseline](baseline/). [Analysis](baseline/aa-analysis.json).

| Case | Median ns/lookup | A/A block differences | Tree-owned bytes |
|---|---:|---|---:|
| Successful, no score | 29.867 | −0.151%, −0.135%, −0.594% | 14,272 |
| Successful, score | 32.686 | +0.239%, +0.264%, −0.107% | 14,272 |
| Missing | 11.400 | −0.202%, −0.175%, +0.206% | 14,272 |
| Successful, 256-byte | 102.810 | +0.036%, −0.045%, +0.032% | 146,656 |

ARM Neoverse V2, 96 cores, one measured thread pinned to CPU2, sibling list `2` (no SMT), nominal 2.8GHz; effective frequency/governor unavailable. GCC13.3.0, libc Ubuntu2.39, C11 O3 flags in build.sh, no LTO. Existing system services and continuous profiling were unchanged; no concurrent benchmark. Monotonic raw timing excludes construction, query iteration, warmup and teardown. Every timed row is ≥568ms.

Process-scoped user-cycle sampling (zero lost samples): primary leaf helper41.91%, raw lookup21.91%, SipHash6.75%, libc memcmp3.45%. Several libc addresses remain unresolved and are not assigned to a function. Long-member control: SipHash45.22%, raw lookup26.09%, leaf helper11.47%, memcmp9.76%. These shares are of all captured user-cycle sample weight, not the selected-symbol subtotal. Profiles cover whole process lifetime, including construction and warmup; do not call them exact loop-only costs. Three primary perf-stat captures report 100% scheduling for cycles/instructions/branches/misses; see raw captures. Baseline profile confirms concentration in the lookup chain under this standalone fixture, not release parity or a proven execution-resource bottleneck.

## TMA classification

| Category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Installed topdown-profiler0.2.3, collector source SHA256 `747173cbf804e6d04e43a244adbf319890598c79c2b4e56f73f2815b1ecedefe`. Actual command uses perf6.17.13 (installed under the6.14 kernel-tools path) `stat --topdown -I1000 -x, -a -C2`. It returns L1 output labeled “percent of slots” but measures CPU-wide activity with no continuous proof that other work stayed off CPU2. Therefore it is exploratory, not a qualified process classification. Six windows show Frontend5.4%, BadSpeculation1.8–1.9%, Backend41.5–41.6%, Retiring51.2%, approximately100% within rounding. No children collected. The next profile experiment needs explicit CPU exclusion/continuous occupancy evidence before promoting this funnel. The tool’s header alone does not validate its underlying formulas or process isolation. No manual conversion from stall cycles or sample percentages was performed.

Next gate: three independent hypotheses and chair decision using the frozen evidence. No candidate selected yet; batching/SIMD/prefetch remain excluded. Historical inline scanners are parked/rejected and must not be relabeled as new accepted work.
