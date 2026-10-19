# Idle AWS runner observations

One frozen 600-second observation completed on each reserved host. These are current
idle-window observations, not explanations for historical A/A failures. No benchmark
or candidate ran during this job. All original experiment decisions remain unchanged.

| Host | Valid intervals | CPU2 non-idle | CPU2 maximum 10s window | CPU2 steal | Observer CPU |
|---|---:|---:|---:|---:|---:|
| INTEL | 60/60 | 0.0000% | 0.0000% | 0.0000% | 0 |
| AMD | 60/60 | 0.0700% | 0.2002% | 0.0000% | 0 |
| ARM | 60/60 | 0.0000% | 0.0000% | 0.0000% | 0 |

Non-idle here excludes iowait and steal, both retained separately. Aggregate, sibling
and observer counters, all 61 snapshots per host, actual monotonic durations, scheduling
lateness, PSI and available frequency fields remain in [RESULT.json](RESULT.json) and
the host raw files. Missing frequency is retained as missing, not interpreted as a
fixed clock. Zero observed steal is not proof of undisturbed prior measurements.
The observer has small overhead on another core. No prior precision gate changes.

The code was independently reviewed before launch; the missing-counter/affinity
checks were corrected before the final freeze. The initial version never executed.
Root independently reconstructs every delta and preserves all intervals. Raw identities
and commands are in [the frozen plan](PLAN.md) and [freeze](freeze.json).

The helper job record retains its initial CPU2 affinity; the observer then sets its
own affinity to CPU0 as preregistered. Every recorded snapshot verifies CPU0.
