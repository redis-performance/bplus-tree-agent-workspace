# Round 15 — natural growth wrap and adversarial SCAN intervals

**Source adoption NONE. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.**
The main source and root referee retain their hashes. This round adds one boundary
suite, extends two scopes, and completes one branch-count diagnostic. No timing
benchmark, harness revision, baseline qualification or optimization population ran.

Round start 03:52:00 UTC; deadline 04:22:00 UTC; handoff cutoff 04:20:30 UTC. All experimental
children have finished. This is not the final campaign round; the final worker still
owes MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed work

| Evidence | Passing source/build cells | Coverage per cell |
|---|---:|---|
| [Growth-wrap singleton extension](BOUNDARY-021/growth-extension/README.md) | 8 | 2 seeds, 131,080 natural resizes, 2 growth wraps, 131,094 full model states |
| [Multi-member wrap extension](BOUNDARY-021/batch-extension/README.md) | 8 | 4 fixtures, 262,160 resizes, 4 growth wraps, 262,188 model states |
| [BOUNDARY-022 SCAN intervals](BOUNDARY-022/README.md) | 8 | 2 seeds, 20 models, 684 SCAN calls; 128 active growth and 128 active shrink calls |
| [Same-size cleanup extension](BOUNDARY-022/cleanup-extension/README.md) | 8 | 2 seeds, 10 models, 432 SCAN calls; actual 64→64 cleanup and active clone |
| [Fresh-seed build confirmation](ROUND-015-CONFIRMATION/README.md) | 48 | All three final oracles, control/A/B/C, native/sanitizer, debug assertions on/off |

Every low/high state in the wrap loops receives a complete sorted-vector model.
New batch leaves are observed in generation 1 after a natural 65535→1 growth transition.
Two-member batches preserve an active resize; 13-member batches create two leaves
and complete it. Exact scores, binary bytes, ranks, subtree counts and owned allocations
pass. SCAN permits duplicates while checking current exact values, per-call intervals,
continuous anchors, and unchanged scan metadata. Cleanup observes only 56 of 256 members
copied and five uncopied leaves before cloning and verification consume the window.

All 48 fresh-seed cells pass, including omission of REDIS_DEBUG as in benchmark builds.
Every oracle CHECK and unconditional serverAssert remains. This adds build coverage;
it does not change historical timing assertion settings or establish independent review.
Logical digests match within every source/build matrix. No production defect observed.

[COUNTERS-008](COUNTERS-008/README.md) completes three serial whole-oracle captures.
Actual skip-zero branches occur 2/4 times in singleton/multi-member fixtures; active
batch flushes 2/6 times. The colliding SCAN fixture reaches displaced-slot, multiple-tag
and probe-reachability rejection paths. These are execution counts, not CPU-time
profiles, hotness, timed-loop costs or evidence of a speedup.

## Failures and test sensitivity

Seven deliberate fault runs produce six detections and one retained survival. Four
new distinct fault types are detected: premature batch migration, omitted displaced
SCAN tail, collapsed same-tag members, and skipped equal-mask cleanup destination.
Allow-zero-generation is detected twice again and is not counted as a new type.

The batch-migration fault SURVIVES singleton coverage because the ordinary insertion
path can still index its sole member. Fresh multi-member coverage catches it. An
initial 12-member recipe failed its two-leaf requirement; a separately frozen 13-member
recipe retains that requirement. A cleanup fixture initially expected ordinary inserts
to change member_revision; source inspection showed the resize changes it. The revised
new fixture explicitly checks equal-before/different-after. Both initial failures,
all raw rows, old plans, snapshots, patches and the surviving fault remain. No existing
production assertion or referee check was weakened.

## Verification and commands

Run/fault entrypoints and exact compiler commands are in each linked manifest. The
fresh matrix uses `ROUND-015-CONFIRMATION/run.py`; census uses `COUNTERS-008/run.py`
and `analyse.py`. All experiment children are bounded 120 seconds and run serially.
Native -O3/debug and -O1 ASan/UBSan use unchanged source/support/allocator; the additional
fresh matrix varies only its declared seeds and debug flag. Local compiler is Apple
Clang 17.0.0 (clang-1700.6.3.2), arm64. This does not establish current CPU frequency.

`python3 experiments/OVERNIGHT-2026-10-17/verify-round015.py` passes 1,512 hash checks,
190 recorded serial command windows,16 new patch reconstructions, all model summaries
and raw coverage branch mappings. Three captures are disjoint from recorded builds/tests.
Workspace/pristine-source and `git diff --check` pass. Original 43 tests were not rerun;
the unchanged source/build evidence from round 14 remains preserved.

[A separate retained-candidate audit](ROUND-015-CANDIDATE-AUDIT.json) verifies 256 frozen
file hashes and reconstructs all 12 optimization patches exactly across EXP-002–005.
Current decisions are reconciled without remeasurement: EXP-002/003 REJECT/NONE,
EXP-004 A/PARK, EXP-005 PARK/NONE. Historical provisional choices are not current wins.
See [sequential review](ROUND-015-REVIEW.md) and [full audit](ROUND-015-VERIFY.json).

## Decision and handoff

Totals: **6 harnesses, 12 baseline explorations, 28 diagnostics, 22 boundary suites,
45 distinct boundary fault types; 4 sequential populations; 0 accepted, 2 rejected, 2 parked
optimizations.** This round adds one suite, one diagnostic and four fault types.
Baseline commit remains `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c` plus explicitly
uncommitted isolated snapshots. Source stays baseline until separate morning review.

CPU MCP ask and methods/code 05/14 were consulted; irrelevant SPEC/Linux timer passages
are not support. Its evidence checker returned `no_number` for the qualitative no-win
statement. No M4 measurements/core numbering/frequencies transfer. Backend/model/token
cost unknown; supervisor records CLI usage separately. Reviewer startup failed, so all
confirmation/review is sequential. Frequency, effective QoS, within-window migration,
independent review and committed provenance remain unresolved.

Next: [carry a real SCAN cursor across natural narrow→wide ID migration](ROUND-015-NEXT-FIXTURE.md).
The recipe is preparation only, not a result. Existing tests scan inside migration
or mutate afterward; the transition with a live cursor is distinct. Preregister and
bound it before execution. Performance needs a qualified runner or a new justified
method; do not repeat failed protocols unchanged. No publishing, protected-git retry,
credential inspection, supervisor/runtime/STOP edits or permission changes occurred.
