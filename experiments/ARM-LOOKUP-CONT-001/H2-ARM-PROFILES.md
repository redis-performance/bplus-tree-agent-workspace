# H2-B matched ARM profile assessment

Matched fixed-work profiles support the expected reduction in lookup work; they do not replace fresh confirmation. Baseline and B use identical 500-member hit fixtures, seed17 and 400,000 sweeps (200,000,000 reported lookup operations), with three process-user counter repetitions per compiler and immutable ELF joins. Every counter reports100% scheduling. All workload checksums and owned bytes match; sample reports record zero lost samples.

| Cohort | Median cycles change | Instructions change | Branches change | Branch misses change |
|---|---:|---:|---:|---:|
| native | -4.914% | -2.300% | -1.774% | +2.152% |
| gcc15-lto | -5.150% | -2.101% | -0.000% | +0.407% |

Counters cover the complete process, including setup and the identical warmup. They are fixed-work totals; dividing by the reported operation count would still include that overhead and must not be labeled pure steady-state cost. These are profile observations, not another accepted timing cohort or confidence interval. Native and LTO remain separate.

The exact H2-B assembly replaces recomputed count/score-width metadata addressing with the cached16-bit size. Its memory layout retains the original leaf size and score base. Lower instruction counts are consistent with removing that arithmetic. The larger cycle reduction is consistent with a shorter dependent address path, but this experiment does not isolate that cause from scheduling, branch layout or other generated-code effects. Do not infer a pipeline category from the counts.

All four actual profile captures include samples, full disassembly, size, tool version, command records, stdout checksums and source/binary joins. The public text captures retain original and sanitized hashes; binary sample data remains private with its original checksum. Source baseline is ee8e7f701 /16def20f…, B revision1 is63b18cd5…. Independent review separately verifies code and the saved ELF bytes.

## TMA classification

Qualified ARM baseline/B Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and child categories remain **unavailable**. The actual topdown-profiler ARM collector emitted CPU-wide generic percentages; scope/formula and scheduling evidence is insufficient to qualify those rendered values. They remain raw diagnostics. Process-user counters and hotspot shares are not substitute pipeline categories.

Qualified matched Intel roots and children are reported separately in [H2 profile/guard audit](reviews/H2-PROFILE-GUARD-AUDIT.md), with its bounded CPU-wide scope and parser limitations. Their category changes concern Intel, not ARM.

Actual stdio cpu-perf discovery, library_status and ask were repeated with these counter changes, workload identities and mechanism caveats. Coverage remains3/287 sources and158 passages. Two generic pmu-tools feature/release passages were retrieved; neither establishes this workload’s cause. The interpretation above is a bounded inference from this campaign's own assembly/counters, not a claim established by retrieved literature. Fresh seeds29/43 across all11target cases and final independent raw review remain acceptance gates.

The [independent ARM profile audit](reviews/H2-ARM-PROFILE-AUDIT.md) recomputes all counters and raw sample summaries. Native sample files carry matching GNU build IDs; the LTO binaries have no GNU build IDs, so their joins rely on saved SHA-256, capture metadata, mapped paths and matching disassembly rather than an embedded sample-file fingerprint. Each capture also contains two kernel-mode-labelled startup samples with negligible period weight despite user-filtered event attributes. Their cause is unresolved; the audit preserves them and does not infer qualified ARM pipeline categories.
