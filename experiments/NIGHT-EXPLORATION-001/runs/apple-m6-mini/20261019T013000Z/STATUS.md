# M6 driver — DECODE-001 referee/profile ready

Updated 2026-10-19T02:37:36.649047+00:00. Round 4 ends 02:55:27 UTC. Campaign ends **08:00 UTC / 09:00 Lisbon**;

Round5 resumed at 2026-10-19T02:41:29.094528+00:00; deadline03:08:25UTC; handoff by03:06:55UTC.
Acknowledged prior final handoff publication: Published a8633cde.


| Target | Status | M1 action / evidence |
|---|---|---|
| Five-size baseline | COMPLETE | Reuse baseline-attempt002: 120 processes / 960 rows. |
| RANK-001 | REJECT / NONE | All 100K blocks regress; skip exact candidates. [Results](002-rank/RESULTS.md). |
| UPDATE-001 | REJECT / NONE | No 100K winner; 1M repacking effects are exploratory. [Results](003-update/RESULTS.md). |
| LOOKUP-001 | REJECT / NONE | No dual-primary winner; B at 100K is an exploratory lead. [Results](004-lookup/RESULTS.md). |
| DECODE-001 | RUNNING / referee ready | Count-one primary profile sufficient; three other captures insufficient. ITERATE-001 skipped. |

Lookup hypothesis **M6-LOOKUP-PHYSICAL-001** decodes a known physical slot directly,
retaining memchr. [Exact source/patch/referee/binary identity](004-lookup/comparison-freeze.json)
and [patch manifest](004-lookup/implementation-manifest.json).

| Variant | 100K median / block range | 1M median / block range | Decision |
|---|---:|---:|---|
| A exact decoder + wrapper | −1.328% / −2.646..+0.333% | −0.407% / −3.083..+3.568% | REJECT dual primary |
| B generic bit reader | −4.800% / −6.243..−3.482% | +0.428% / −3.926..+5.681% | REJECT dual primary |
| C local decoder | −1.095% / −1.662..−0.320% | −1.389% / −3.241..+2.396% | REJECT dual primary |

B passes the 100K gate in every block; no candidate passes 1M. A/A qualifies at 100K
(maximum 0.745%) and fails at 1M (4.184%). No primary relabeling, adoption shortlist,
fresh confirmation, full candidate performance guards, candidate profile validation
or independent review. Both population steps were sequential; all patches retained.
Exact serving model/token cost unknown; visible identity Codex/GPT-6 family.

All four sources pass 43 original tests per native/sanitizer build, 20 public lookup
cells per build and a 4160-cell/515840-check exact-bit/output oracle per build. Two
deliberate physical-decode faults detected. Four of six baseline profiles meet the
minimum; two smaller miss captures remain insufficient and were not repeated.
Audit passes 222 rows, 48 effects, three patches and 524 serial command windows.
Last experimental child ended 02:33:28 UTC. No further lookup trial is eligible.

Publications acknowledged: profile/referee e18d69d0; chair e1f3b73c; candidate freeze
94e4e897; decision 0ec11fb6. Final audited handoff publication follows. Coordinator
alone writes Git. A previous worktree denial is retained; separate copied sources
were used without retry. Cached published M1 branch 4c48fa7e was inspected; the exact
M6 physical-score patch/harness is NOT RUN there. No host pooling or fresh remote
fetch; earlier DNS failure remains recorded. Next action is in [HANDOFF.md](HANDOFF.md).

Launcher metadata verifies Apple M6. Direct sysctl is unavailable and was not retried.
Frequency, DVFS, performance-core residency, migration and PMU observations are unknown.
Self-sampled PCs identify regions only; no profiler permission retry or permission changes.

Recorded branch totals: **10 populations** (8 sequential + 2 multi-agent),
**0 accepted / 5 rejected / 5 parked; 30 patches / 13 validated harnesses**.
Concurrent M1 night counts remain separate pending reconciliation. Baseline src/ unchanged.

Final checks: raw/source/referee/patch audit and whitespace checks pass. The lookup
evidence seal covers 1098 files with a compact aggregate hash; no private paths or
bytecode found. Last experimental child remains 02:33:28 UTC. No active experiment.

DECODE-001: [plan](005-decode/PLAN.md), [diagnosis](005-decode/PROFILE.md).
Native/sanitizer existing oracle and2080-cell extended control checks pass. Primary
profile has28 PCs; three guard captures insufficient and preserved. Both population
steps pending; no candidate timed. All176 materialized-output cells are frozen.

DECODE referee/profile published80177d1e. Sequential proposal/chair chooses
M6-DECODE-COUNT1-001; all three proposal passes preserved. Implementation population
next: natural scalar branch / outlined bulk bridge / forced-inline early-bulk policy.
No candidate built or timed yet; no independent agents/review.

DECODE chair published e62f839d. All three isolated implementations now pass
unchanged Python oracle and2080 extended geometries per native/sanitizer build.
Two deliberate policy faults detected. Actual release codegen preserved.
Candidate/referee/source/binary identities in005-decode/comparison-freeze.json.
Next calibration then fixed A/A and three176-cell serial comparisons, no overlap.
