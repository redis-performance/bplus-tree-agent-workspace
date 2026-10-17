# bplus-tree-agent-workspace

Standalone B+ tree optimisation workspace, modelled on
[hdr-agent-workspace](https://github.com/redis-performance/hdr-agent-workspace).
The target is the packed score-ordered tree **and its compact member index** from
[Redis PR #15635](https://github.com/redis/redis/pull/15635), measured through direct C API
microbenchmarks. No Redis server, networking, command processing, or persistence is built.

**State:** preparation complete; 0 accepted, 0 rejected, 0 parked optimisation experiments.
The initial harness is runnable. [Local M1 measurements](experiments/EXP-001/local-m1-2026-10-17/README.md)
completed 144 processes / 984 rows and four sampled profiles. Baseline qualification
is parked: 40/41 cells fail the precision/duration gates. No optimisation is accepted.
See [the experiment log](experiments/EXPERIMENTS.md) and [next steps](experiments/NEXT-STEPS.md).
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
ns/op, ops/sec, tree-owned usable bytes and a checked result checksum. Cases: insert,
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
