# Fixed idle-host environment observation

This is one descriptive, read-only observation per reserved AWS host after all
candidate/control jobs have ended. It is not a benchmark, A/A retry, causal noise
diagnostic for an earlier run, or source-selection round. No existing decision can
change from these observations. Start before07:15UTC under the existing owned lease;
release remains08:00UTC. No host service, package, permission, governor or frequency
setting changes.

Freeze61 snapshots at10-second scheduled offsets (60 intervals,600 seconds), with a
620-second owned helper cap. Preserve every raw snapshot, actual monotonic duration,
missed schedule, unavailable field and invalid counter interval. No retries or extension.
Derive the targetCPU2's actual sibling set and online CPUs from sysfs. The observer alone
sets its affinity to the lowest online CPU outside that sibling set, leaving benchmark
CPU2/its sibling free of the observer's reads. The job remains in the existing owned
slice/lock and deadline; no lease configuration changes. This observational affinity
is explicit and differs from the helper's initial CPU2 benchmark affinity.

Record aggregate/target/sibling/observer CPU counters, online set, loadavg, CPU PSI,
reported scaling frequency if available, and initial governor/clocksource. Do not
collect process command lines, hostnames, addresses or credentials. CPU totals use
only the first eight /proc/stat fields because user/nice already include guest time;
retain guest fields raw and report steal separately. Changed/reset/missing counters,
changed online set or nonpositive tick totals invalidate intervals without pruning.

Interpretation is limited to these idle observation windows. Reported frequency may
be absent or misleading, PSI is an aggregate, and zero observed steal does not prove
an undisturbed or fixed-frequency host. The observer creates small activity itself.
None of this establishes what caused earlier measurement variation or qualifies a
failed experiment. Existing controls remain failed. Root authored the observer;
Intel independently reviewed the observation scope and required these limitations.
Exact model/tokens/USD unavailable. No candidate code or population is created.
