# AMD baseline qualification: PARK

Both compiler cohorts fail the frozen ±1% A/A bound. All 144 rows are retained; no candidate timing is authorized by these controls.

| Compiler | Case | Block | A/A elapsed change |
|---|---|---:|---:|
| gcc15-lto | score | 0 | +1.170255% |
| gcc15-lto | update | 0 | +1.086695% |
| gcc15-lto | update | 1 | +1.422493% |
| gcc15-lto | update | 2 | -1.422308% |
| native | update | 1 | -1.124031% |

Minimum measurement windows exceed 1.62 seconds. A longer duration is not automatically a remedy: baseline-only profiles investigate the gap before any separately preregistered changed-condition qualification. Failed controls are neither discarded nor retried unchanged. [Raw controls and analysis](amd/baseline/).

## TMA classification

Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring, and child categories, remain unavailable pending actual AMD collection and formula/scheduling review. No category is inferred from the control variance.

This closes one qualification protocol, counting both compilers once: 41 completed attempts, 23 PARK, 18 REJECT, 0 approved; ARM 29, Intel 6, AMD 6; 24 populations, 5 replications, 12 qualifications. Active source populations remain excluded.
