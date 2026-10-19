# Independent ambient-observation audit

**PASS:** reconstructed immutable `8a0f9e564` from git objects: all183 raw snapshots,180 endpoint deltas,12 host artifact hashes and published table. No producer audit code was imported or executed; audit.py is the independent reconstruction. No runner access, benchmark or candidate work occurred.

| Host | Valid intervals | CPU2 non-idle | CPU2 maximum 10s window | CPU2 steal | Observer CPU |
|---|---:|---:|---:|---:|---:|
| INTEL | 60/60 | 0.0000% | 0.0000% | 0.0000% | 0 |
| AMD | 60/60 | 0.0700% | 0.2002% | 0.0000% | 0 |
| ARM | 60/60 | 0.0000% | 0.0000% | 0.0000% | 0 |

Every interval has the expected aggregate/observer/target/sibling labels, unchanged online set, CPU0 observer affinity, positive monotonic duration and nondecreasing counters. CPU2 siblings are2/50 on Intel and2 alone on AMD/ARM. CPU0 is the lowest online CPU outside each target sibling set. Initial helper CPU2 affinity is correctly distinguished from the observer's own explicitly changed affinity.

All raw field deltas match intervals.json exactly. Totals include only the first eight /proc/stat CPU fields; guest/guest_nice remain raw and are not added again. Non-idle excludes iowait and steal; both are retained separately. Summary percentages use pooled ticks, maximum activity uses individual intervals, and every available-frequency count matches. Clocksource/governor/frequency values are retained metadata, not evidence of effective MHz or throttling.

Frozen script and plan SHA256 match final freeze9bf13ddea; initial d3da570d1 is superseded and unexecuted. The independent reviewer previously identified and verified the expected-label/affinity/duration correction. All three job records return0 within620seconds; metadata, UTC endpoints, 61 absolute ten-second schedule positions, elapsed monotonic spans, collection overhead and maximum lateness reconcile. Exact per-host durations/tick arrays and all input hashes are in audit.json.

These are descriptive current idle windows around06:15–06:25UTC, not historical measurement conditions. Zero observed steal does not prove an undisturbed host, and low aggregate activity does not independently prove absence of a workload; lease and idle process checks are separate coordinator evidence. Frequency files are missing on ARM and their absence is preserved. No failed A/A is rescued, no source selected and no prior decision changes. ARM's later profile is outside this observation window and cannot be characterized by it.

Actual independent participant `/root/aws_intel`; exact backend/model, tokens and monetary cost unknown. Source adoption NONE.
