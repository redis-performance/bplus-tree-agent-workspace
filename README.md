# bplus-tree-agent-workspace

**EXP-007 completed:** per-leaf specialization reduces fresh full-leaf decode time
by 33% on the primary case and about 43% on aligned 8/64-bit scores. Three short-range
regressions block adoption. [Results and next experiment](experiments/EXP-007/RESULTS.md).
Both three-agent population steps, native/sanitizer validation, fresh confirmation,
assembly inspection and raw-data audit are complete. Production source stays baseline.

**Focused decoder benchmark (19 October):** ready and locally measured; see the
[run guide](docs/DECODER-MICROBENCHMARK.md) and [results](experiments/EXP-004/decoder-microbench-2026-10-19/README.md).
The 12.58-second A/A and baseline/A matrix found EXP-004 A slower in aligned 8-bit
and 64-bit decoder loops. Release/sanitizer checks passed; source selection remains
NONE and EXP-004 stays PARK. The overnight supervisor is stopped.

Standalone B+ tree optimisation workspace, modelled on
[hdr-agent-workspace](https://github.com/redis-performance/hdr-agent-workspace).
The target is the packed score-ordered tree **and its compact member index** from
[Redis PR #15635](https://github.com/redis/redis/pull/15635), measured through direct C API
microbenchmarks. No Redis server, networking, command processing, or persistence is built.

**State:** preparation complete; 0 accepted, 2 rejected, 4 parked optimisation experiments.
[Round 20](experiments/OVERNIGHT-2026-10-17/ROUND-020.md): 112 correctness cells pass, including candidate boundary histories, forced scalar fallback, dense-leaf promotion and natural generation wrap; six repeated faults detected. Counts and performance decisions unchanged; main source preserved.
[Round 19](experiments/OVERNIGHT-2026-10-17/ROUND-019.md): fixed prefetch diagnostic does not resolve the batch-size guard; 32 heterogeneous batch cells pass. Scoped counters confirm equal logical lookup paths, not equal timings. Main source preserved.
[Round 18](experiments/OVERNIGHT-2026-10-17/ROUND-018.md): new batch qualification and fifth sequential population complete; main source preserved.
[EXP-006](experiments/EXP-006/README.md): bounded inline tag search C/PARK; fresh primary passes, long-key guard uncertainty and single-lane regression concern block adoption.
[Partial batch promotion](experiments/OVERNIGHT-2026-10-17/BOUNDARY-025/README.md): discovery and fresh confirmation pass sixteen source/build cells; three faults detected, source NONE.
[Round 17](experiments/OVERNIGHT-2026-10-17/ROUND-017.md): 144 final-scope semantic cells pass; 16 initial batch cells retain a coverage gap. Score moves, exact finite ties, external ownership and batch promotion are checked; source NONE.
[Round 16](experiments/OVERNIGHT-2026-10-17/ROUND-016.md): 192 source/build/seed/mode cells pass, including live widening/narrowing, clone/relocation, external ownership and fresh seeds; source NONE.
[Round 15](experiments/OVERNIGHT-2026-10-17/ROUND-015.md): 80 passing source/build cells, three branch captures, all candidate patches preserved; source adoption NONE.
[Growth-wrap](experiments/OVERNIGHT-2026-10-17/BOUNDARY-021/batch-extension/README.md) and [colliding SCAN](experiments/OVERNIGHT-2026-10-17/BOUNDARY-022/README.md) coverage pass all eight source/build cells; same-size cleanup and fault sensitivity are checked.
The overnight campaign completed seven harness revisions, thirteen baseline explorations,
thirty-four measurement diagnostics and twenty-six boundary oracle suites.
[Round 12](experiments/OVERNIGHT-2026-10-17/ROUND-012.md) adds mixed finite-score and
packed-movement oracles; all source/build cells pass and four new faults are detected.
Predecessor-workload contrasts reproduce, but a placebo blocks robustness; a fixed
idle-gap remedy also fails. No timing policy or source change is adopted.
EXP-004 stays A/PARK; the original guard remains unresolved.
[EXP-005](experiments/EXP-005/README.md) stays parked after fresh primary confirmation
failed in round9. Main source stays baseline.
[EXP-002](experiments/EXP-002/README.md) completed both population stages as sequential
passes; expanded guards and fresh confirmation reject all three iterator implementations.
[Expanded evidence](experiments/EXP-002/guard-extension/README.md): selection NONE; main source unchanged.
[EXP-003](experiments/EXP-003/README.md) completes a second sequential population;
member-decoder outlining also fails fresh full-output guards. All patches preserved.
[EXP-004](experiments/EXP-004/README.md) completes the third sequential population: a
smaller score-decoder predicate is provisionally preferred, but remains PARKED because
a mixed-output guard is unresolved. [Round 8](experiments/OVERNIGHT-2026-10-17/ROUND-008.md)
records the fresh qualification, negative diagnostics and preserved baseline.
[New ordered/signed-zero guards](experiments/EXP-004/ordered-guards/README.md) pass for
all three retained variants; the original mixed-output guard remains unresolved.
[Targeted requalification](experiments/OVERNIGHT-2026-10-17/AA-001/README.md) passed
2/8 cells (iteration and scan). [Larger-fixture requalification](experiments/OVERNIGHT-2026-10-17/AA-002/README.md)
passed rank only (1/4). [Independent-query requalification](experiments/OVERNIGHT-2026-10-17/AA-003/README.md)
passed 0/4. [Miss-warmup requalification](experiments/OVERNIGHT-2026-10-17/AA-004/README.md)
also passed 0/4; lookup and suite qualification remain parked. [Local M1 measurements](experiments/EXP-001/local-m1-2026-10-17/README.md)
completed 144 processes / 984 rows and four sampled profiles. Baseline qualification
is parked: 40/41 cells fail the precision/duration gates. No optimisation is accepted.
See [the experiment log](experiments/EXPERIMENTS.md) and [next steps](experiments/NEXT-STEPS.md).
The user authorised an [overnight local campaign](experiments/OVERNIGHT-2026-10-17/PLAN.md)
through 18 October, 08:00 Lisbon: measurement repair, requalification and bounded
population experiments. Worker drafts stay local pending review; runtime status is
`scratch/overnight-20261017/status.json`.
The [Linux/macOS CI configuration](docs/ci-check.yml) is a draft; publishing an active
workflow requires GitHub `workflow` scope, absent from the available write credential.

## Source and standalone boundary

`src/zset_btree.c` and `.h` are byte-for-byte copies at commit
`a7ecd959374d66847c095250bf2d373edf7316c5` of `antirez/redis`.
[source-manifest.json](source-manifest.json) pins the PR, commit, original paths and SHA-256 hashes.
`vendor/redis/` contains only the needed upstream SDS header, SipHash implementation,
test macros and licensing text. `compat/` supplies the standalone host adapter.
The retained `server.h` include resolves to that adapter, not a Redis header.

The adapter uses libc's actual allocation usable sizes, the upstream SipHash algorithm,
deterministically seeded hashing, and SDS64 fixture strings. Tree-owned member layout is
unchanged. The SDS subset is not a general-purpose SDS library. Fork-child page dismissal
is a no-op and is outside benchmark scope. See [the extraction notes](docs/STANDALONE.md).

## Build and check

Requires a C11 GCC/Clang compiler, Make, and Python 3; supported host adapters: Linux and macOS.

```sh
make -j2
make check
make sanitize
make smoke
python3 scripts/check-workspace.py --pristine-source
```

`make check` runs the tree's original embedded tests with debug assertions. Sanitizers
use a separate build. `make smoke` checks the microbenchmark paths at small sizes; its
timings are not a performance result. Do not compare sanitizer and release binaries.

```sh
build/btree-bench --size 100000 --ops 1000000 --member-bytes 16 --seed 1
build/btree-bench --case lookup-hit --size 100000 --ops 1000000 --member-bytes 320 --seed 2
```

CSV includes the case, fixture parameters, effective operation count, elapsed ns,
ns/op, ops/sec, tree-owned usable bytes, a checked result checksum, thread CPU time,
boundary CPU IDs and reported QoS (effective QoS remains unknown). Cases: insert,
lookup hit/miss, rank, forward iteration, unordered scan, score update, delete.
Inputs and access order are generated outside timing. Point operations reuse a shuffled
permutation; reads use a documented warm-up. Insert/delete visit each member once;
iteration/scan report ns per visited member. See [measurement rules](docs/MICROBENCHMARKS.md).

## Two population-based decision steps

1. **Selection population:** three independent proposers inspect the same baseline,
   profiles and experiment history. Each supplies one falsifiable hypothesis. A chair
   ranks the evidence and chooses one hypothesis or `NONE`, recording why the others lost.
2. **Implementation population:** three independent implementers start at the same commit
   and implement that chosen hypothesis in isolated worktrees. Correctness is a hard gate.
   A measured comparison selects the best passing variant or `NONE`; a fresh confirmation
   run must reproduce its gain before acceptance.

Both steps are required. They are separate from **validation step 1: benchmark** and
**validation step 2: profile**. A proposal vote cannot accept a patch; timing alone cannot
replace correctness or profiling. Preserve losing proposals, variants and evidence.
Full protocol: [POPULATION.md](docs/POPULATION.md). Reusable prompts: [.claude/skills/](.claude/skills/).

```text
qualify baseline + profile
  -> 3 proposals -> chair decision
  -> 3 isolated implementations -> correctness -> serial measurements
  -> best passing variant -> fresh benchmark + profile -> adversarial review
  -> accept / reject / park -> append log + update shared memory
```

## Layout

| Path | Purpose |
|---|---|
| `src/` | Mutable B+ tree target, initially identical to the pinned PR |
| `compat/`, `vendor/redis/` | Frozen host adapter and upstream support |
| `bench/`, `tests/` | Frozen microbenchmark referee and test entry point |
| `experiments/` | Append-only log, summary, templates, evidence and cost ledger |
| `docs/` | Population protocol, workload plan, standalone contract |
| `.claude/program.md` | Evidence-led optimisation playbook |
| `.workspace-memory/` | Shared session state and handoff for any agent |
| `scripts/` | Workspace validation, experiment creation, ABBA runner and profiling |

Source notices are retained. [Licensing and attribution](NOTICE.md) describe the upstream files.

Additional standalone regression oracles: [finite-score/collision model](tests/boundary_oracle.c)
and [score-bound/ownership model](tests/score_boundary_oracle.c). Exact release and
sanitizer commands/results are in [BOUNDARY-001](experiments/OVERNIGHT-2026-10-17/BOUNDARY-001/README.md)
and [BOUNDARY-002](experiments/OVERNIGHT-2026-10-17/BOUNDARY-002/README.md).

Additional natural-ID and relocation oracles: [wide scan](tests/wide_scan_oracle.c)
and [allocation relocation](tests/defrag_oracle.c), with commands and evidence in
[BOUNDARY-003](experiments/OVERNIGHT-2026-10-17/BOUNDARY-003/README.md) and
[BOUNDARY-004](experiments/OVERNIGHT-2026-10-17/BOUNDARY-004/README.md).

Additional controlled collision and bulk-delete oracles: [probe boundaries](tests/index_probe_oracle.c)
and [bulk rebuild thresholds](tests/bulk_delete_oracle.c), with final passes and preserved
faults in [BOUNDARY-005](experiments/OVERNIGHT-2026-10-17/BOUNDARY-005/README.md) and
[BOUNDARY-006](experiments/OVERNIGHT-2026-10-17/BOUNDARY-006/README.md).
The [round3 handoff](experiments/OVERNIGHT-2026-10-17/ROUND-003.md) records independent-query
fixture evidence and the next qualification step; no source optimisation is accepted.

The [round4 handoff](experiments/OVERNIGHT-2026-10-17/ROUND-004.md) records the validated
independent-query snapshot, parked A/A, scoped self-process profiles and sampler controls.
Additional [lexical](tests/lex_boundary_oracle.c) and [append-batch](tests/append_batch_oracle.c)
oracles pass release/debug and sanitizers. Root source remains unchanged for morning review.

The [round5 handoff](experiments/OVERNIGHT-2026-10-17/ROUND-005.md) records miss-warmup
phase evidence, the isolated HARNESS-003 revision, parked A/A and timer calibration.
New [batched-score](tests/batch_score_oracle.c) and [guarded raw-buffer](tests/raw_guard_oracle.c)
oracles pass both builds and detect all four planned faults. No source candidate selected.
