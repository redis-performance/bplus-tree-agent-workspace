# DIAG-002 — adjacent add brackets do not explain lookup variation

Completed six serial measured processes /24 windows plus one preregistered warmup
process. All checksums, counts and tree memory stable; all timing regions exceed10ms.
Fixed correlation/CV criterion not met. No exclusions or timing failures. Do not use
bracket normalization as a demonstrated precision remedy. A/A lookup remains PARK,
source selection NONE. No clock GHz, cycle rate, causal DVFS or portable speed claim.

[Plan](PLAN.md), [isolated source hashes](freeze.json), [patch](diagnostic-harness.patch),
[commands](validation.json), [assembly review](ASSEMBLY-REVIEW.md), [runner](run.py),
[manifest](manifest.json), [raw rows](raw/), [analysis](analyse.py), [results](SUMMARY.md).
Release/ASan+UBSan smoke passed. The initial register-specific assembly inspector
failed because Clang used x8, not x0; corrected before timing without source changes.
Eight dependent adds verified. No public API/QoS changes or M4 ID/frequency assumptions.

CPU MCP evidence checker consulted: no_number for the scoped qualitative claim;
frequency unknown, heuristic failed to parse compact compiler spelling (full build
commands are retained). Four windows/process are clustered, nearby brackets cannot
exclude migration or establish clock during lookup, and correlation is not causation.
Negative result does not prove frequency is stable or identify the remaining cause.
Backend/model/token costs unknown; supervisor records CLI usage. All drafts uncommitted.
