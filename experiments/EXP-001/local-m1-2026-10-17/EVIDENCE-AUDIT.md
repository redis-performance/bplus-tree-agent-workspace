# MCP evidence audit

Called `cpu_perf.check_evidence` with the actual local CPU/core description, unknown
frequency and residency, compiler/flags, workload, baseline hash, six-block method,
lookup observation and uncertainty, and separate sample counts.

The heuristic returned **drop_number**: frequency/turbo/SMT information was only partly
complete because operating frequency was not measured. The original claim explicitly
said frequency and placement were unknown; no frequency is guessed to satisfy the rule.

Its core-count regex matched the physical efficiency-core inventory, although the actual
benchmark used one thread. This demonstrates why the heuristic is an audit aid, not
independent hardware verification. Actual P/E-core residency is still unknown.

Disposition: preserve raw observations and their descriptive summaries for reproducibility,
mark timing tables as exploratory, and do not promote them to validated speedup claims
or cross-machine comparisons. Baseline qualification is PARKED independently because
40 of 41 case cells fail the preregistered control gates. No source optimisation is accepted.
