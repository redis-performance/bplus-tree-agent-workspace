# Microbenchmark plan and measurement contract

## Implemented seed harness

`bench/microbench.c` calls the tree API in-process. It generates unique binary members,
integer scores, and a seeded shuffled insertion/access permutation before starting timers.
Each case creates its own tree. Point cases repeat the same shuffled permutation, which
is not independent random sampling. A full successful-lookup pass warms each existing tree
and may finish pending incremental rehashing; these rows are steady-state cases.

| CSV case | Timed work | Effective operations |
|---|---|---|
| insert | find-for-add + insert-new, growing an unreserved tree | cardinality |
| lookup-hit / lookup-miss | member lookup, including hash and checksum accumulation | `--ops` |
| rank | member lookup plus forward rank, checksum accumulation | `--ops` |
| iterate | one complete forward traversal, score checksum | members visited |
| scan | complete cursor scan, COUNT hint 64, counting callback | members emitted |
| update | find-for-add + score update to a larger score | `--ops` |
| delete | delete each member in shuffled order | initial cardinality |

Assertions on required insert/update preconditions remain inside those timed loops and
are identical for all candidates. Result checks and update-state verification run after
timing. Timings include loop/index/checksum overhead; there is no overhead subtraction.
Iteration/scan are single traversals and need sufficient cardinality to exceed timer noise.
Scan may emit duplicates; its operation count is actual callbacks, and a separate untimed
pass checks every member was seen with the expected score. It is not a unique-members rate.
`tree_bytes` is post-case owned memory except delete, which records pre-deletion memory.
The update fixture moves scores toward the high end; it does not represent all churn patterns.
This is an initial referee, not a claim of broad workload coverage.

## Frozen matrix for baseline qualification

Run cardinalities 1K, 100K, 1M; member lengths 8, 16, 64, 319, 320, 321, 1024 bytes;
seeds 1, 2, 3 for discovery and 101, 102, 103 for confirmation. Select a bounded initial
subset and record it before running. Include both sides of the 320-byte storage boundary.
Use at least 10x cardinality for lookup/rank/update operations where runtime permits;
calibrate durations against timer noise and record the chosen counts. No timing has yet
qualified any of these cases. Workload fit is evidence to establish, not an assumption.

Follow-up fixtures, to implement and freeze **before** relevant optimisation rounds:

- Equal, clustered and arbitrary finite double scores; signed-zero/infinity correctness.
- Ordered/reverse insertion, mixed member lengths, random versus skewed access, and
  working sets larger than LLC with cache counters (large alone does not prove cold).
- Batched score lookup, range seeks/count/delete, reverse iteration, ordered append,
  reservation, duplication and steady-size insert/delete churn.
- Active resize/tombstones, narrow/wide leaf IDs and allocation/memory after churn.
- Independent sorted-vector oracle and mixed-operation differential checks.

## Fair comparisons

Keep benchmark, support code, machine, CPU affinity, allocator, compiler and flags fixed.
Use separate worktrees for baseline and candidate. Start with GCC and Clang `-O3` and
frame pointers on native x86-64 and ARM64; `-O2`/`-Os` can be later diagnostic controls.
Do not conflate a compiler/allocator change with a tree optimisation.

```sh
# First A/A: use the exact same executable twice.
scripts/run-bench.sh /absolute/base/btree-bench /absolute/base/btree-bench experiments/EXP-001/aa
# Then candidate discovery, on the same dedicated runner/session.
scripts/run-bench.sh /absolute/base/btree-bench /absolute/variant/btree-bench experiments/EXP-002/discovery
```

`BENCH_SIZE`, `BENCH_OPS`, `MEMBER_BYTES`, `SEED`, `CASE`, `BLOCKS` select a cell; defaults
are 100K, 1M, 16, 1, all, 3. `CPU` optionally pins Linux runs with taskset.
The runner uses A B B A in each block and refuses to overwrite an evidence directory.
Record compiler/flags, CPU model, frequency policy, cache sizes, OS, allocator and fixture
hashes in the experiment README. The script records binary hashes and fixture settings.
It does not qualify noise, choose a winner, or provide confidence intervals automatically.

For each case/block, compare mean A with mean B; lower ns/op is better. Report paired
effects and uncertainty, raw runs and guard cases. Do not average distinct workloads
into an unexplained headline. Use fresh held-out confirmation after population selection.

## Profiling

On Linux: `scripts/run-profile.sh /absolute/btree-bench OUTDIR --case lookup-hit --size 100000 --ops 10000000`.
This captures whole-process perf counters and sampled call stacks, including setup and
cleanup. Compare the same case/arguments and inspect symbol attribution; increase the
operation count only by preregistered calibration to amortise setup. Timed-region counter
instrumentation is future work. Missing PMU permissions/counters are missing evidence,
not zero events. Do not change machine-wide permissions automatically.

Local smoke checks are functional checks only. Substantive benchmarks run serially on a
dedicated runner selected for the campaign; never share that runner with builds or tests.
