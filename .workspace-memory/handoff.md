# Handoff

The user requested a workspace like hdr-agent-workspace, created in redis-performance,
with an experiment log and both population-based decision steps. They clarified that
only the data structure matters and experiments must use microbenchmarks, not Redis.

Source: PR #15635, immutable head in source-manifest.json. The tree .c/.h files initially
match that commit exactly. compat/ supplies a standalone host; vendor/redis/ is minimal
support. Do not expand scope back to server integration tests or client benchmarks.

Read README.md, docs/POPULATION.md and docs/MICROBENCHMARKS.md. The initial harness covers
eight direct API cases; fixture coverage and qualified performance evidence remain future
work. Local smoke output is not a baseline. No agent populations have been executed.
Unknown token usage is not estimated or fabricated.

Next action is EXP-001. Workspace acceptance and upstream publication are separate.
