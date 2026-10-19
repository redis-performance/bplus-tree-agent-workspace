# Apple M1 lookup precision preflight

Status: preregistered; no candidate timing. This is a separate Apple M1
follow-up to [M6 EXP-009](../EXP-009/RESULTS.md), whose corrected-adapter
lookup-hit A/A passed 6/6 blocks at 100K and 3/6 at 1M. M6 selected no
candidate. This run asks only whether the same public lookup workload has
qualified **M1** controls. It cannot turn the M6 PARK decision into a pass.

Freeze: branch base `4bc71bd73ae7be8e68761269b9bdfd5a8df11495`, matching
M6 tree, adapter and EXP-009 lookup harness hashes. The program checks all
four identities before building and again before A/A. Apple M1 MacBook Air,
macOS 26.3, Apple Clang 17, C11 `-O3 -g -Wall -Wextra -Werror
-fno-omit-frame-pointer -fno-lto`, one unpinned thread, 16-byte members,
public successful score lookup. Use the exact EXP-009 `harness/lookup.c` and
unchanged tree/adapter. Native and ASan/UBSan lookup smoke must pass.

For each size, 100K and 1M, take three 200,000-query calibration runs on
seed 1. Fix operations at `ceil(600,000,000 * 200,000 / fastest_elapsed_ns)`,
cap at 100 million, and record whether capped. Calibration fixes counts
**before** A/A; no count adjustment follows observed controls. Six seed/block
pairs are 1, 2, 3, 1, 2, 3. Alternate size order by block parity; within
each size use ABBA, producing 48 serial fresh processes and 12 blocks.
Use one warmup pass per process. Preserve CSV stdout, stderr, exact command,
timestamps, hashes, checksum, operation count, tree-owned bytes, elapsed and
thread-clock metadata. No other local benchmark may overlap.

For each four-run block, A = first + fourth `elapsed_ns`, B = second + third.
Qualify only if `abs(B-A)*100 <= A` **and every operation window is at least
10 ms**. Both sizes require all six blocks. If any block fails, mark M1
precision PARK and stop before proposals, source edits, or candidate timing.
If both qualify, record only that M1 can measure this baseline under this
schedule; await a separately selected M6 candidate or a new user-authorized
M1 hypothesis. Never pool host rows or reclassify M6's failed controls.

The [`cpu-perf` MCP](../../docs/PERFORMANCE-MCP.md) was consulted at
2026-10-19 11:20 UTC: `library_status` reports bundled list revision
`deb5a0bac467` (2026-10-05), 245/287 indexed sources. `ask` received the
actual M1/M6 workload and control context. Its returned passages were about
other workloads and do not establish an M1 noise cause. Its
[measurement-pitfalls benchmark](https://github.com/usamahz/cpu-performance-engineering/tree/main/misc/benchmarks/05-measurement-pitfalls)
illustrates why a consumed result and multiple runs matter; those Apple M4 Pro
numbers are not M1 evidence. This plan retains the independently checked
lookup checksum and all repeated raw rows. No CPU-frequency or core-residency
claim follows from it.

Run in this clean worktree: `python3 experiments/EXP-009-M1-AA-001/run.py build`;
commit/push the resulting fixed counts and build identities; then run
`python3 experiments/EXP-009-M1-AA-001/run.py aa` once. The script refuses
overwriting any raw output. No tree optimization population is added.
