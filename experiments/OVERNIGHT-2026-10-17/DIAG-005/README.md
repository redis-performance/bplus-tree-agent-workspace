# DIAG-005 — construction/query interaction supported locally

All48 preregistered serial processes complete with no failures/timeouts/exclusions.
The fixed interaction criterion is met across fresh fixture seeds: separating query
permutation from construction permutation largely removes the ascending/shuffled
construction contrast in this local long-key fixture. All structural, fingerprint,
operation-count and checksum controls pass. No source candidate or source speedup.

[Plan](PLAN.md), [patch](diagnostic-harness.patch), [freeze](freeze.json),
[build/smoke validation](validation.json), [commands and raw hashes](manifest.json),
[raw rows](raw/), [analysis](analyse.py), [descriptive results](SUMMARY.md).
Release and ASan/UBSan smoke pass all four cells. Both arrays have matched allocation
sizes; query order changes warmup and measured lookup history. The source and tree
structure are identical between query modes within a construction arm.

This motivates independent query-order fixture coverage in the next referee revision.
It does not identify cache/prefetch/allocation mechanisms, establish clock stability,
resolve existing precision qualification or validate an optimisation. Individual
noisy windows were retained; all claims stay scoped to the fixed local diagnostic.
This is a fresh-seed coordinator follow-up, not an independent-agent confirmation.

CPU MCP evidence checker consulted: no_number for qualitative claim; frequency absent,
heuristic also missed stated workload/baseline. No M4 timing/CPU mapping transferred.
Clock/turbo/effective QoS/residency unknown. Lookup PARK, source selection NONE; both
population stages and remaining acceptance gates still required. Backend/model/cost
unknown; supervisor records actual usage. Uncommitted snapshot awaits morning review.
Next: scoped count equality control, then independent-query A/A preregistration in a
future round. Do not repeat failed earlier schedules or promote DIAG-004's inverse
exploratory effect into its original hypothesis.
