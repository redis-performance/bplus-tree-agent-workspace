# B+ tree optimisation playbook

Profile first. No optimisation has been accepted or ruled out in this workspace yet.
Historical PR report numbers are not standalone baseline measurements.

| Evidence | Candidate family | Guard conditions |
|---|---|---|
| Tree search / packed-score decode hot | Search strategy, decode reuse, local code generation | ties, boundary ranks, signed zero, both directions |
| Member-index probes hot | Tag matching, probe bounds, prefetch placement | collisions, tombstones, resize, wide IDs |
| Leaf moves / copying hot | Avoid repeated packing, narrow local moves | split/merge, long members, exact score bits |
| Allocator pressure / bytes high | Capacity policy, reuse, reservation | sparse pages, update/delete churn, bytes/member |
| Iteration / scan hot | Batch work, loop structure, locality | iterator invalidation, full scan coverage and cursor progress |
| Branch/cache misses dominate | Layout and guarded specialisation | native ARM/x86, scalar fallback, code size |

Use one family per falsifiable hypothesis. Freeze the referee before candidates.
The current harness has integer scores and repeated shuffled accesses; extend fixtures
before making claims about equal scores, arbitrary doubles, cold caches or mixed workloads.

## Known non-starters

None measured. Do not confuse untested ideas with rejected experiments.

## Prerequisite queue

1. Qualify A/A and capture baseline profiles (EXP-001).
2. Complete workload coverage for the selected hot path.
3. Run both population steps (EXP-002 and later).
