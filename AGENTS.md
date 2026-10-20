# Agent Notes — bplus-tree-agent-workspace

Read this file, `.workspace-memory/MEMORY.md`, `.workspace-memory/LIVE-STATUS.md`,
and `.workspace-memory/handoff.md` at the start of each session. Apply the mandatory
per-session workflow in `docs/PERFORMANCE-MCP.md` for both Codex and Claude.

## Scope

Optimise the standalone packed B+ tree and compact member index from Redis PR #15635.
The user explicitly scoped this to the data structure and microbenchmarks. Do not add
Redis server, command, persistence, client, or integration work to this campaign.

`src/zset_btree.c` and `.h` are the mutable target. `compat/`, `vendor/redis/`, `bench/`
and the test entry point are the frozen referee during a candidate comparison.
Harness fixes are separate commits followed by baseline requalification. Regression
tests may be added, but never weaken existing checks to let a candidate pass.

## Mandatory performance MCP use — every session

Every investigation or optimization work session, whether run by Codex or Claude,
must use the `cpu-perf` performance MCP from
[usamahz/cpu-performance-engineering](https://github.com/usamahz/cpu-performance-engineering).
This is a required part of the investigation, not an optional reference.

At session start, discover the server/tools and check `library_status`; before
proposing changes or interpreting performance, call `ask` with the actual question
and relevant measured counters, assembly or compiler output. Use its source lookup
and evidence-checking tools as needed. Record the calls, source/version information,
findings, limitations and resulting decisions in the experiment/activity log.
Follow [docs/PERFORMANCE-MCP.md](docs/PERFORMANCE-MCP.md) for the shared workflow.
If unavailable, record the attempted connection and concrete blocker, use the linked
primary sources as a disclosed fallback, and restore MCP use when possible. Never
claim a consultation happened when it did not. Keep indexing and retrieval off the
dedicated measurement runner; existing frozen protocols and acceptance gates remain.

## Required TMA classification — every experiment

Codex and Claude must use [topdown-profiler](https://github.com/redis-performance/topdown-profiler)
to assess further experiments. Every experiment's Markdown report must contain a
**TMA classification**: Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring,
with their measured shares of total pipeline slots, plus measured child categories.
The four L1 categories sum to 100% within reported rounding/measurement error.
Show baseline and candidate separately; link raw captures, tool revision, binary,
CPU/collector scope, workload, run IDs and collection quality. Follow
[docs/TMA-REPORTING.md](docs/TMA-REPORTING.md). Never substitute hotspot sample
shares, IPC, instruction counts, another machine, or illustrative numbers for TMA.
If unsupported or uncollected, show all four as unavailable and state the blocker.
Historical sealed reports may use a linked adjacent TMA.md supplement.

## Required decision process

Follow `docs/POPULATION.md`: (1) three independent proposals plus a chair decision,
(2) three isolated implementations of the chosen hypothesis plus measured selection.
These are planning instructions for future optimisation rounds, not a request to run
agent populations during workspace preparation. Use available agents only when the
session permits delegation; otherwise record three separate passes and explicitly
label that they were sequential and not independent agents. Never invent participants.
Record actual backend/model and measured token costs; unknown costs remain unknown.

Every acceptance requires correctness, benchmark validation, profile validation,
independent confirmation and adversarial review. Profile before proposing. Select
`NONE` when evidence is absent. Never manufacture results or carry timings across machines.

## Measurement and source rules

- One falsifiable hypothesis per experiment; all variants share an exact source commit,
  fixture seeds, compiler/flags, allocator and machine. Use separate worktrees/builds.
- Benchmark serially on a dedicated runner. Builds and bounded correctness/smoke checks
  may run locally; ask for the runner only when a real campaign needs one. Do not search
  private SSH configurations or infer access from unrelated workspaces.
- Qualify timer precision with A/A. Measure same-session ABBA, at least three blocks,
  then confirm the selected winner independently. Preserve per-run rows, not just means.
- Draft speed gate: >=2% improvement in the preregistered primary case, no demonstrated
  >1% regression on guard cases or tree-owned memory. Unresolved noise means PARK.
  Declare alternative memory/speed trade-offs before running, not after seeing results.
- Preserve score/member order, binary member lengths, exact finite scores and signed-zero
  behaviour, rank counts, leaf ownership, index/leaf ID maintenance, resize/scan semantics,
  and iterator invalidation. Do not assume NaN is a supported low-level input.
- Keep assertions, hashing, allocator and build options identical across timing binaries.
  Treat architecture-specific results as scoped, pending broader confirmation.
- Preserve losing variants as patches. Never reset or discard another session's edits.

## Logging and publishing

This is a public repo in `redis-performance`. Commit code, experiment evidence, decisions
and shared memory together. No secrets, private hosts, credentials or customer data.
Use generic machine descriptions. Keep raw profiles locally if too large; commit summaries,
commands and checksums. Update EXPERIMENTS.md, SUMMARY.md and README counts on each decision.

The current request authorises repository creation and preparation here. It does not
request upstream PRs, issues, comments, merges, releases, or changes to PR #15635.
Prepare upstream text here when useful; obtain user direction before those later actions.
Never force-push. Never change agent permission settings to bypass a restriction.
