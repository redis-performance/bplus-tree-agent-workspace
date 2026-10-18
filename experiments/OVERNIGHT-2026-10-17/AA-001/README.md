# AA-001 — targeted baseline qualification: partial, suite PARK

Completed all 192 planned serial processes/rows in 209.2 seconds,
plus the one preregistered binary warm-up. No failures, timeouts or exclusions.
All per-cell operation counts, checksums and tree-owned memory were stable. Binary
and frozen source/referee hashes verified before and after.

Only iterate16 and scan16 meet the preregistered +/-1% descriptive precision gate.
Hit16, hit320, miss16, rank16, update16 and hit321 fail. Decision: PARK the suite and
all lookup/rank/update optimisation comparisons; qualified traversal cells are scoped
to this session/fixture. No source candidate (NONE), no population or optimisation
decision. All eight cells clear the duration gate. Longer windows do not cure the
remaining noise. Boundary IDs often differ, while thread/wall time is close to one;
this does not identify the cause or establish constant frequency/core residency.

[Plan](PLAN.md), [runner](run.py), [manifest](manifest.json), [raw rows](raw/),
[analysis](analyse.py), [table](SUMMARY.md), [full summary](summary.json). Each row is
a batch average, not a percentile of individual-operation latency. Observed boundary
IDs are opaque; no P/E mapping is inferred. Reported QoS was user-interactive; the
public API does not expose effective overrides. Clock/frequency and effective QoS
remain unknown. Rates in the raw evidence are local observations, not portable claims.

CPU Performance Engineering evidence checker was consulted after analysis: verdict
`drop_number` for incomplete microarchitecture residency and frequency/turbo fields.
Its heuristic also mistook installed core count for used cores; this campaign used
one benchmark thread. We retain the control records and do not promote timing rates
or any speedup claim. Backend/model unknown; supervisor tracks CLI tokens separately.

Next: scan qualifies locally but requires a baseline scan profile before population
selection. The attempted scan profile is in SCAN-PROFILE-001; follow its blocker record.
