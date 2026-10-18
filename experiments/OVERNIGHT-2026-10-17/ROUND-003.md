# Overnight round 3 — evidence and handoff

Bounded round:2026-10-17 22:39:28–23:09:28 UTC. Handoff prepared before the final90s;
this is not the final campaign round. No active benchmark/profile child remains.
Main src/zset_btree.c/.h and HARNESS-001 referee remain byte-identical to their pins.
No source optimisation, population, publishing, upstream action or permission change.
Exact backend/model/token cost unknown; supervisor records CLI usage separately.

## Completed work and decisions

| Evidence | Completed result | Decision |
|---|---|---|
| [DIAG-003](DIAG-003/README.md) |24 windows, matched access-array footprints, repeated versus per-pass reshuffled lookup | Preregistered repeated-order advantage not supported |
| [BOUNDARY-005](BOUNDARY-005/README.md) |622 full model checks/build, controlled lookup wraparound, tombstones, tag-mask candidates and insertion revisions | Final release/debug and ASan/UBSan pass; two faults detected; initial fixture failures retained |
| [BOUNDARY-006](BOUNDARY-006/README.md) |48 bulk-delete cases/build,240 verifications,24 cuts beginning during resize | Both builds pass; two faults detected |
| [DIAG-004](DIAG-004/README.md) |48 processes, ascending/shuffled construction with fixed lookup order | Ascending advantage not supported; contrary pattern motivated a new diagnostic |
| [DIAG-005](DIAG-005/README.md) |48 fresh-seed four-cell processes, independent/coupled query orders | Fixed construction/query interaction criterion supported locally |
| [COUNTERS-002](COUNTERS-002/README.md) |Four scoped Clang captures, all tree function/region/branch counts compared | Within each construction arm, query-order aggregate counts identical; not a time profile |

Round totals:120 measured windows in102 processes, four separate instrumented captures,
two added correctness suites and four detected intentional faults. No measured rows
removed; all timing schedules completed without failure or timeout. Instrumented CSV
times are excluded from comparison by design, not selected after seeing results.

Campaign totals: one harness revision, three baseline explorations, seven additional
measurement/path-count diagnostics and six boundary suites. Twelve intentional faults
have been detected across all rounds. Optimisations **0 accepted /0 rejected /0 parked**;
population rounds **0**. Source selection **NONE**, lookup qualification **PARK**.

## Most useful finding

The original harness uses the same shuffled permutation to build the tree and query it.
DIAG-004 changed construction order while leaving queries fixed; its predicted advantage
failed. DIAG-005 then preregistered a four-cell follow-up using fresh seeds211/307/401.
Decoupling query order largely removed the construction contrast, meeting the fixed
interaction criterion. Tree structure was identical between query modes within each
construction arm; lookup permutations/counts/checksums were controlled and verified.

This supports adding independent query permutations to future fixture coverage. It is
not a source speedup, a noise cure or proof of a cache/allocator/prefetch mechanism.
COUNTERS-002 confirms identical aggregate instrumented tree paths for the two query
orders within each construction arm. Those counts do not rank time costs or replace
required time-profile validation. Existing sampled EXP-001 profiles remain historical.

## Commands, failures and validation

- DIAG-003/004/005: each prepare.py saves an isolated snapshot/patch/freeze; validate.py
  builds release and ASan/UBSan and runs all preregistered small smoke cells. All final
  builds and smoke checks pass. Each run.py executes its fixed serial schedule; each
  analyse.py retains every row. Plans, commands, raw CSV/stderr, binary/source hashes,
  UTC stamps and load observations are in the experiment directories.
- BOUNDARY-005 initial run.py failed the required lookup-distance precondition. A
  diagnostic-only attempt2 printed distance20, despite a24-bucket occupied run: matching
  entries can name the same leaf, allowing earlier successful lookups. Attempt3 assigns
  distinct tags to the final bucket, forcing distance23 without lowering any assertion.
  All prior source snapshots, patches and failed logs remain. Final two-seed suite passes
  both builds. Clearing tombstone tags and suppressing home filters both fail as planned.
- BOUNDARY-006 run.py passes both builds for all48 cases. Cases straddle >1024 and
  >=length/10 rebuild thresholds, with prefix/middle/suffix cuts, exact score bits,
  binary members, clone/free ownership, reinsertion and ULONG_MAX clipping. Batched
  lookup counts0..16, repeated members and output canaries are checked. Omitted rebuild
  fails stale-index lookup; an endpoint off-by-one fails exact deletion count.
- COUNTERS-002 prepare.py/run.py build and capture four cells. Installed Clang17 public
  reset/dump header inspected; counters reset immediately before the operation clock,
  dump occurs before semantic checks/cleanup. All captures have1000000 lookup/SipHash
  entries and zero insertion/deletion entries. Raw profiles/full exports stay in ignored
  scratch with checksums; public tree count exports and commands are retained.
- `python3 experiments/OVERNIGHT-2026-10-17/verify-round003.py` passes snapshot/root
  referee hashes, raw hashes, fixed schedules, recomputed diagnostic criteria, all retained
  test attempts, fault controls and complete tree-count equality. This is a separate
  sequential coordinator audit, not independent performance confirmation.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check` pass.
  New public evidence was scanned for private paths/host patterns; none found. Round
  SHA256 inventory pins public evidence, new oracle sources and final shared ledgers.

## Limits and provenance

Base workspace commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c; target pin remains
Redis PR#15635 a7ecd959374d66847c095250bf2d373edf7316c5. All new instruments/oracles are
explicit uncommitted snapshots; commit-based acceptance awaits morning review. Previous
protected-git and sample inspection denials were respected, with no retries/escalation.

One reviewer agent startup failed before any agent ran (thread-store context load
failure). No independent participant, proposal, review, model identity or cost invented.
All work/reviews were sequential coordinator passes. Both population stages still must
run when prerequisites permit; neither was bypassed for an accepted optimisation.

CPU MCP ask and benchmark05/14 methods/code consulted. Retrieved HdrHistogram/general
repeatability passages do not support the local hypotheses; no unrelated retrieval cited
as evidence. Evidence checker consulted before diagnostic conclusions. No M4 numbers,
frequencies or CPU numbering transferred. Wall time stays primary; thread time and
opaque boundary IDs do not establish clock or residency. Frequency/turbo state/effective
QoS remain unknown. No local result is promoted as a portable rate or accepted speedup.

Final environment audit confirms arm64,macOS26.3 and Apple Clang17.0.0. A read-only
sysctl query for CPU/core/RAM metadata was denied; exact command/stderr are preserved
in ROUND-003-ENVIRONMENT.json and it was not retried. M1/core/RAM descriptions inherit
the established campaign context, rather than a successful new sysctl observation.

## Next concrete action

Prepare a separate referee fixture revision, in an isolated snapshot, with independently
seeded query order and explicit construction/query labels. DIAG-005 is a working prototype;
keep its factorial raw rows and interpretation limits. Preserve the current root referee
and source for morning review. Validate the new fixture, freeze its patch/hashes and
preregister a bounded targeted A/A on independent-query lookup, including long-key
coverage and unchanged precision/memory gates. The new fixture is a coverage fix, not
an assumed precision cure. Do not rerun prior failed schedules unchanged.

Only after qualified comparisons and relevant time profiles exist should the three
proposals/chair and three isolated implementations/measured selection begin. Fresh
confirmation and adversarial review remain mandatory. A capable independent runner may
still be required; no private SSH/cloud access was sought. Campaign endpoint remains
2026-10-18 07:00 UTC /08:00 Lisbon. Final campaign worker must write MORNING-REPORT.md.
