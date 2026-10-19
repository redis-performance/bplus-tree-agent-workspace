# Round 2 handoff — UPDATE-001 complete; resume LOOKUP-001

Saved 2026-10-19T02:19:16.817210+00:00, more than 90 seconds before round end 02:31:47 UTC.
All experimental children finished. Campaign ends 08:00 UTC / 09:00 Lisbon; no new
experiments after 07:15 UTC. No baseline source adoption.

Do not restart baseline, RANK-001, or UPDATE-001 calibration/A/A/discovery. Launcher
selected baseline-attempt002 is complete; earlier baseline/ remains preserved.
Rank REJECT/NONE; update REJECT/NONE. [Update result](003-update/RESULTS.md),
[selection](003-update/implementation-selection.md), [audit](003-update/final-audit.json).
Three sequential proposal passes/chair and three isolated implementations complete.
All update patches in 003-update/variants/; snapshots/builds under ignored
scratch/m6-update/variants/0,A,B,C. Git worktree add was denied once; do not retry it.

Update candidate screen: 100K medians +0.084/+1.694/+1.992%, none pass the primary.
1M medians −7.705/−8.765/−9.270%, every block negative beyond observed A/A, but only an
exploratory transient-packing lead for a separately declared future experiment. Do not
relabel 1M as this experiment's sole primary or pick a noisy 100K winner. No contender
qualifies for adoption confirmation; full guards/independent review/profile validation
remain absent. Both controls fail strict precision. All semantic/sanitizer checks pass,
including reversed metadata/headroom/ownership oracles and two deliberate faults.
Initial baseline-only private oracle held a pointer across public mutation; ASan
caught it. Corrected to test the in-place helper; original public tests unchanged.
Raw failure/old source in ignored scratch/m6-update/oracle-attempt001; see erratum.

Next create 004-lookup. Read shared PLAN.md LOOKUP-001 and EXP-006 results before a
hypothesis. Use one frozen independent-query public hit/miss referee at 10K/100K/1M,
construction and query streams separate; count leaf tag candidates and full comparisons
untimed, inspect actual release assembly and profile. Rank/update samples often show
memchr/FindForAdd, but sampled nearest-symbol PCs are not exact cost shares. Review
whether a new portable hypothesis explains EXP-006's single-query regression. Reusing
its scanner unchanged is a control, not a new idea. If no new supported mechanism,
record three sequential proposal passes/chair NONE and move to the optional target.
Do not manufacture a second implementation population after a NONE chair decision.

Cached published M1 branch4c48fa7e already completed its own lookup diagnostic/chair
NONE and has reusable lookup-bench.c / instrumentation.patch in004-lookup. Inspect
that source with read-only git show if useful, record its exact hash/origin and keep
all M6 observations separate. No exact M6 update patch/harness replication exists on
M1. Remote DNS refresh failed round1; current cached context is not a fresh remote
cross-host decision. M6 leads; do not wait for this host remotely.

Coordinator alone commits/pushes. Latest successful ack a9e16781 for update candidates;
profile33bf7899, chairf8d2badf. Current update decision/final round request follows this
handoff. Read matching publish-ack.json first on resume, and record its published commit.
For each new milestone atomically replace only publish-request.json, then poll 5s,
at most120s, no builds/tests/profiles/timings during barrier. Preserve timeouts/failed
acks once and continue bounded local work if necessary. No Git writes, permission,
supervisor, deadline, STOP, credentials or upstream changes.

Host launcher metadata proves Apple M6. Worker sysctl denied, not retried. Direct
frequency/DVFS/core residency/migration/counters remain unknown. Self-sampler works,
external attach failed earlier; no permission changes. Model/cost unknown beyond
visible Codex/GPT-6 family. All proposal/implementation/review passes sequential,
not independent. Recorded branch totals9 populations (7 sequential +2 multi-agent),
0 accepted /4 rejected /5 parked,27 patches,12 harnesses; M1 night counts unreconciled.

A separately supplied operator audit at02:18 UTC reconstructs all144 discovery rows/36 effects and agrees with NONE. See OPERATOR-UPDATE-DISCOVERY-AUDIT.json; raw-data scope only, not independent timing/semantic adversarial review or replication.
