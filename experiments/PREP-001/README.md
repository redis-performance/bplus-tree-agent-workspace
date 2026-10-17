# PREP-001 — standalone workspace preparation

Date: 2026-10-17. Status: COMPLETE. Decision: preparation only, no optimisation.

## Scope and provenance

Prepared a public `redis-performance/bplus-tree-agent-workspace`, following the HDR
workspace conventions. The user clarified that this campaign concerns only the data
structure and microbenchmarks; Redis server integration is out of scope.

Copied the tree .c/.h unchanged from PR #15635 at
`a7ecd959374d66847c095250bf2d373edf7316c5`. Kept only the required upstream support and
notices. Added a standalone libc/SipHash/SDS adapter and direct embedded-test entry point.
No Redis source checkout or submodule is required to build the workspace.

## Prepared artifacts

- Eight direct API microbenchmark cases, seeded fixture generation and checked outputs.
- Separate release and sanitizer builds, serial ABBA evidence runner, Linux perf wrapper.
- Both population decision steps and separate benchmark/profile validation gates.
- Experiment template, append-only log, summary, baseline plan, playbook, reusable prompts,
  shared agent instructions/memory, cost-ledger header and a draft CI workflow.

## Local validation

Host: macOS ARM64, Apple Clang. These are functional checks, not baseline measurements.

| Check | Result |
|---|---|
| Release build, `make -j2 all` | PASS |
| Original embedded B+ tree tests with debug assertions | 43/43 PASS |
| Same tests under ASan + UBSan | 43/43 PASS |
| All 8 microbenchmark cases, 1K members / 1K operations, 16-byte keys | PASS |
| All 8 cases, 1K members / 2001 operations, lengths 319/320/321/1024, seed 2 | PASS |
| Sanitized harness, 1K members / 2001 operations, 320-byte keys, seed 3 | PASS |
| ABBA orchestration with identical binaries at smoke sizes | 3 blocks / 12 processes PASS |
| Provenance hashes, local Markdown links and shell syntax | PASS |

Raw tree-test output: [release](upstream-tests.log), [sanitizers](sanitizer-tests.log).
The benchmark smoke checks validate operation paths only; their tiny timings are not
published as a performance result. The smoke ABBA run validates orchestration, not noise.

During preparation, scan smoke checks revealed an incorrect harness assumption that
every member is emitted exactly once. The harness now uses actual callback count and
an untimed completeness/score check. No change to the upstream tree was needed.
The ABBA runner was also adjusted for macOS's Bash 3 empty-array behaviour.

## Remaining work and limits

EXP-001 baseline qualification, real profiles, dedicated-runner measurements and population
rounds are NOT RUN. The perf wrapper has syntax validation only on this macOS host.
Linux/GCC validation is not yet run. The CI matrix is prepared in docs/ci-check.yml;
the available account with repository write access lacks OAuth workflow scope, so
GitHub rejected publication of an active workflow. The configuration is saved as a
draft and does not execute. It can be installed at .github/workflows/check.yml with
a credential authorised to publish workflows.
Current benchmarks use integer scores, fixed-size members and shuffled repeated accesses;
the wider fixture plan is documented but not implemented. Standalone lexical sentinel
and defragmentation coverage remains a targeted follow-up. Dismiss-memory is a no-op.

No speedup, memory saving, selected hypothesis, candidate acceptance, upstream issue/PR,
merge or release is claimed. Agent token cost was unavailable and is not fabricated.
