# H3 short-inline equality: REJECT

No source is selected. C fails the native ARM primary and score guards. A and B pass the native ARM cohort, but both fail the independently qualified Intel native long-inline and external-member guards. B additionally fails the ARM GCC15/LTO external guard. All gates use per-block elapsed changes; primary wins do not offset guard regressions.

| Cohort | Variant | Hit median | Failing guard blocks |
|---|---|---:|---|
| ARM native | A | -6.007% | none |
| ARM native | B | -6.441% | none |
| ARM native | C | +1.685% | hit: +1.628%, +1.685%, +1.950%; score: +3.329%, +3.301%, +3.430% |
| ARM GCC15/LTO | A | -6.635% | none |
| ARM GCC15/LTO | B | -6.237% | external: +1.816%, +1.825%, +1.862% |
| Intel native | A | -6.382% | long: +1.379%, +1.564%, +1.472%; external: +1.081%, +1.115%, +1.252% |
| Intel native | B | -4.183% | long: +1.844%, +1.736%, +1.498%; external: +1.438%, +1.208%, +1.226% |

All measured footprint endpoints remain unchanged and all windows exceed 250 ms. Native ARM controls belong to the qualified renewed cohort; target LTO and Intel native each have separate passing controls. Exact patches, correctness artifacts and static mechanism gates remain in `variants/H3-*` and `H3-codegen.md`; raw rows are in `H3/native`, `H3/lto` and `intel/H3-native`.

The Intel rejection arrived while the already-running ARM target cohort was active. That cohort completed without restarting or removing rows. No Intel LTO candidate timing, new guard trial, held-out confirmation or selected-candidate profiling follows this rejection. Prebuilt unused binaries remain artifacts, not performance evidence. No unchanged retry or patch stacking is authorized by these results.

## TMA classification

Candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children are unavailable: no candidate pipeline capture was made before the rejection. ARM event/formula qualification remains unresolved. Separately qualified Intel baseline profiles are in `reviews/INTEL-TMA-BASELINE.md`; they do not establish H3's category changes or the cause of its fallback regressions. No pipeline or server-level recovery claim follows from these timings.

[Independent final review](reviews/H3-FINAL.md) verifies all504 comparison rows and216 original control rows, source/referee joins and measured ELF hashes. It confirms21 failing blocks and the rejection. Count one completed ARM population, not each compiler/variant:42 attempts,23 PARK,19 REJECT,0 approved; ARM30,Intel6,AMD6;25 populations,5 replications,12 qualifications.
