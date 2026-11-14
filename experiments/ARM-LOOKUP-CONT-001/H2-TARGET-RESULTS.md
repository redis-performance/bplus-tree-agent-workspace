# H2 original six-case discovery; later guard rejection retained

At the original six-case stage, both surviving variants pass all three primary blocks, all six-case guard blocks and tree-owned memory in the separately qualified ARM GCC15/LTO target cohort. This remains discovery, not source acceptance. Subsequent affected-path guards reject C for20–25% iterator regressions; see [guard decision](H2-GUARD-DECISION.md). B passes the ARM supplemental guards and continues confirmation. The original six-case evidence below remains unchanged.

| Variant | ARM LTO hit blocks | Median hit | Score median | Miss median | Inline256 | External384 | Update | Memory |
|---|---|---:|---:|---:|---:|---:|---:|---|
| B same-size cache | −5.148%, −5.313%, −5.396% | −5.313% | −5.600% | −0.605% | −3.085% | −1.673% | −3.682% | unchanged |
| C metadata-first | −8.419%, −8.381%, −8.470% | −8.419% | −4.032% | −0.328% | −3.163% | −2.551% | −1.486% | unchanged |

Raw144rows and complete command/stdout artifacts are in `H2-lto/`. B's miss blocks range −4.115% to −0.197%; preserve the unusually large first-block change and do not attribute that magnitude to the patch. All required blocks pass their declared bound; confirmation remains necessary. C leads on the primary but B benefits scored/update paths more; final selection depends on the additional guards and confirmation, not primary medians alone.

Intel native discovery also passes for both: B hit median −4.258% (blocks −3.543% to −4.311%), C −7.568% (−7.279% to −7.606%). All six guards pass and memory is unchanged. Exact144rows are in `intel/H2-native/`. Intel GCC15/LTO also passes every block: B hit median −5.679% (−5.326% to −5.824%), C −7.261% (−7.210% to −7.273%), all original guards within bounds and memory unchanged. Its144rows are in `intel/H2-lto/`. Intel portability requires no >1% regression, not a mandatory speedup; these candidates also happen to clear the discovery speed gate.

ARM LTO assembly confirms cached16-bit metadata-size loads for B and score-width-independent metadata addresses for C. Both target leaf frames are128bytes; C's112-byte frame is confined to the earlier native compiler. No frame-size benefit is transferred between cohorts.

Independent source review [H2-CODE.md](reviews/H2-CODE.md) found no concrete semantic blocker and reran the focused sanitizer binaries. It documents unvalidated32-bit/big-endian execution and bounded coverage. It does not approve adoption.

## TMA classification

ARM baseline/candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and child categories remain unavailable as qualified workload measurements. Intel baseline roots/children are qualified within the registered CPU-wide limits in `reviews/INTEL-TMA-BASELINE.md`; candidate captures remain pending. No slot-category change is claimed from these timings or static code.
