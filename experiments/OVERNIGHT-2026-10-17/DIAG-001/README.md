# DIAG-001 — process/fixture reuse hypothesis not supported

Completed 42 serial processes and all 72 windows with stable counts, checksums and
memory; no failures, timeouts or excluded windows. The preregistered requirement of
halving within-block CV in at least four of six blocks was met in only one block.
Decision: do not adopt process reuse as a demonstrated precision remedy. AA-001's
lookup PARK remains unchanged. No algorithmic source change, population or optimisation
count. No speedup claim. The isolated instrument/patch remains available for review.

[Plan](PLAN.md), [source hashes](freeze.json), [patch](diagnostic-harness.patch),
[runner](run.py), [manifest](manifest.json), [raw rows](raw/), [analysis](analyse.py),
[summary](SUMMARY.md). Exact flags are in build.stdout; smoke checks and invalid-case
refusal passed before timing. Root harness remained frozen.

CPU MCP evidence checker consulted; no performance number was promoted. The heuristic
reported no_number and flagged missing frequency/residency. Query formatting confused
some compiler/workload fields, which are specified in PLAN.md and manifest arguments.
All observed CV/mean ratios are descriptive, affected by process/fixture reuse and
workload history together. No attribution to one latent cause. Backend/model unknown.

Next: stronger exact finite-score/binary-member boundary oracle validation can improve
readiness while profiling and lookup precision remain unavailable. Do not rerun this
diagnostic unchanged expecting it to pass.
