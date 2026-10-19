# Dual-frontend scoped diagnostic result

Phase status: **complete**; issued 642/642 commands, 642 returned. Prior historical candidate remains **REJECT; source NONE**. This diagnosis cannot rescue it.

UTC 2026-10-19T11:15:40.021569+00:00 to 2026-10-19T11:22:35.054735+00:00; fixed1200s owned job/120s child, serial CPU2. Fresh diagnostic lease remains ACTIVE until11:45UTC; restoration pending. Separate postcheck records protected identities and zero owned jobs/PIDs.

Raw integrity: integrity_pass. Physical scope valid: True. Sampled tree code attribution valid: False. Universal lower-retired-instructions hypothesis: **SUPPORTED**. These are distinct conclusions; all18 directions are retained.

3395 scientific sample records retained; all36 captures and36counter runs retained. Known/scientific losses zero: True. Deliberate missing-disable scope fault detected: True.

| Fixture | Seed | Instructions change (%) | Cycles change (%) |
|---|---:|---:|---:|
| primary-forward-100000 | 1701 | -1.745424 | -4.017874 |
| primary-forward-100000 | 1702 | -1.744826 | -4.464473 |
| primary-forward-100000 | 1703 | -1.744823 | -4.603979 |
| primary-forward-1000000 | 1701 | -1.744633 | -2.144730 |
| primary-forward-1000000 | 1702 | -1.744488 | -1.585930 |
| primary-forward-1000000 | 1703 | -1.744558 | -2.107274 |
| h4-forward-100000 | 1701 | -1.745780 | -1.300331 |
| h4-forward-100000 | 1702 | -1.744717 | -1.312874 |
| h4-forward-100000 | 1703 | -1.744705 | -1.408918 |
| h4-forward-1000000 | 1701 | -1.744740 | -1.252321 |
| h4-forward-1000000 | 1702 | -1.744523 | -1.939646 |
| h4-forward-1000000 | 1703 | -1.744571 | +0.048146 |
| h4-reverse-100000 | 1701 | -1.777182 | -1.859400 |
| h4-reverse-100000 | 1702 | -1.776219 | -1.420519 |
| h4-reverse-100000 | 1703 | -1.776112 | -1.736474 |
| h4-reverse-1000000 | 1701 | -1.776139 | -2.379263 |
| h4-reverse-1000000 | 1702 | -1.775970 | -2.512579 |
| h4-reverse-1000000 | 1703 | -1.775970 | -1.494502 |

Counters are unscaled and normalized to actual visited members. Reported100.00% runtime is rounded perf output, not an exact enabled/running nanosecond equality. Retired instruction changes alone do not causally explain cycle or native elapsed effects.

| Source/cell | Own same-fixture A/A | Disabled perturbation | Elapsed transfer |
|---|---|---|---|
| A/h4-forward-100000 | True | False | PARK |
| A/h4-forward-1000000 | True | False | PARK |
| A/h4-reverse-100000 | True | False | PARK |
| A/h4-reverse-1000000 | True | False | PARK |
| A/primary-forward-100000 | True | False | PARK |
| A/primary-forward-1000000 | True | True | qualified |
| control/h4-forward-100000 | True | False | PARK |
| control/h4-forward-1000000 | True | False | PARK |
| control/h4-reverse-100000 | True | True | qualified |
| control/h4-reverse-1000000 | True | False | PARK |
| control/primary-forward-100000 | True | False | PARK |
| control/primary-forward-1000000 | True | False | PARK |

Exclusive sampled-period shares below use each source/frontend/size’s own denominator across its three seeds. They are not per-instruction latency or cross-frontend causal effects. All raw PCs, frames, source-linked code and unmatched entries are retained.

| Source/cell | Events | Decoder (%) | Iterator other/transition (%) | Consumer (%) |
|---|---:|---:|---:|---:|
| A/h4-forward-100000 | 165 | 28.473 | 20.870 | 50.657 |
| A/h4-forward-1000000 | 197 | 39.212 | 16.296 | 44.492 |
| A/h4-reverse-100000 | 171 | 26.312 | 25.403 | 48.285 |
| A/h4-reverse-1000000 | 203 | 21.441 | 28.383 | 50.176 |
| A/primary-forward-100000 | 435 | 30.053 | 24.082 | 45.865 |
| A/primary-forward-1000000 | 508 | 40.931 | 19.464 | 39.605 |
| control/h4-forward-100000 | 168 | 30.836 | 22.476 | 46.688 |
| control/h4-forward-1000000 | 199 | 37.058 | 19.259 | 43.683 |
| control/h4-reverse-100000 | 172 | 31.667 | 20.013 | 48.320 |
| control/h4-reverse-1000000 | 210 | 33.983 | 29.073 | 36.943 |
| control/primary-forward-100000 | 451 | 29.863 | 21.385 | 48.752 |
| control/primary-forward-1000000 | 516 | 40.031 | 19.153 | 40.815 |

Census controls preserve exact within-allocator-mode control/A logical packing, independent score digests and owned bytes. Histograms describe structural entry predicates; their loops’ elapsed fields are excluded from performance claims. Native/sanitizer memory sizes are not equated. Instrumented census does not establish historical heap addresses.

All unmatched/different caller bytes retained; no causal elapsed attribution or equivalence across frontends.

Scope transport, unknown/external samples, mismatched bytes, all loss warnings and perturbation failures remain visible. Independent raw review is pending; producer audit is not that review.

The mandatory cpu-perf consultation was shared from root dfff5540f; this worker’s direct tools were unavailable. It supplied no source-backed mechanism explanation. Frequency/DVFS/SMT remain unknown; no unread-source claim is made.

Raw perf.data stays local with published SHA256; public scripts/reports/disassembly/rows preserve raw/public hash mappings. Native contrast remains separately qualified and independently reviewed.

Raw perf/disassembly text retains original trailing whitespace and terminal blank lines. The ordinary diff whitespace check flagged only these raw artifacts; all non-artifact staged files pass. No measurements or parsing rules changed for publication.
