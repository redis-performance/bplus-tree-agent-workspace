# AWS overnight campaign — 19 October 2026

User-authorized work ends at **08:00 UTC / 09:00 Europe/Lisbon**. Stop starting
experiments at 07:15 UTC. Source adoption remains NONE. Existing M1/M6 runs continue
on their own branches; the AWS controller does not alter them.

SSH access was verified on all three reserved hosts. Their OSS coordinators were
stopped and verified stopped at approximately 01:54 UTC. Independent system timers
stop all owned B+ tree cgroups and restore OSS at 08:00 UTC. Existing unrelated
processes remain intact. Private operational details are in ignored controller
scratch and the private fleet inventory, never public evidence.

| Host | Actual CPU | Compiler | Affinity | Baseline | Optimization |
|---|---|---|---|---|---|
| AWS Intel | Xeon Platinum 8488C, Sapphire Rapids | Clang 18.1.3 | CPU 2; SMT sibling 50 | Complete | See live dashboard |
| AWS AMD | EPYC 9R45, Zen 5 | Clang 18.1.3 | CPU 2, no SMT sibling | Complete | See live dashboard |
| AWS ARM | Neoverse V2, Graviton | Clang 18.1.3 | CPU 2, no SMT sibling | Complete | See live dashboard |

Baseline source/referee commit: `8fab511e` (only Linux affinity metadata differs
from `9c192c9c`; target source unchanged). Each host runs 100/1K/10K/100K/1M members,
eight operations, 16-byte members, seeds 1/2/3, six same-binary ABBA blocks. Native
and ASan/UBSan validation precede timing. The per-host timing budget is 1200 seconds;
results are never pooled. The initial jobs are managed by systemd, bounded to
1800 seconds, and all baseline children inherit CPU2 affinity.

All three baselines are complete and raw-audited:120processes/960rows/40cells per
host, seven validation stages each. Intel338.54s, AMD325.44s, ARM377.83s timing.
Cells with >1% A/A variation:Intel27/40, AMD30/40, ARM19/40;11short-window cells
on every AWS host. These are coverage baselines, not blanket precision qualification.
The [baseline chart](baseline-charts/m1-m6-baseline.png) now includes all five hosts.
Profile-led work applies the [population gates](../../docs/POPULATION.md); completed
results are in the [decision ledger](AWS-DECISIONS.md). The exact shorter-side rank
candidates rejected on both Apple hosts are skipped; lookup/update/decoder work
requires fresh AWS profile evidence. No speed claim or candidate acceptance yet.

[Activity log](AWS-ACTIVITY.md). [Worker contract](AWS-WORKER.md). Native workers use
the already authorized session tools, with no permission changes. Actual backend/model and measured usage are retained
when available; no invented agent identities or costs.


## Execution update

Detached Codex CLI launchers failed before any shell command with `bwrap: setting
up uid map: Permission denied`. Their reports and measured CLI usage remain on the
host branches. The failed supervisors were stopped. Three native session agents
then verified SSH independently and continue with the existing authorized tools;
no permission settings changed. Native agent token costs are unknown. The root
session coordinates review, Git updates and reporting through the deadline.

Each host branch has STATUS.md, HANDOFF.md, ACTIVITY.md and NATIVE-STATUS.json.
[Worker dashboard](AWS-WORKERS.md) tracks published host revisions. Sequential
three-pass populations are explicitly labelled when independent slots are unavailable.

## Release verification

A separate read-only controller auditor is scheduled for08:00:20UTC using
`scripts/audit-aws-release.py`. Its02:59UTC live preflight found all three OSS
coordinators still stopped, no active owned job units at that instant, and all
three release timers scheduled for08:00UTC. This is not release proof. The final
audit requires a release marker, saved status, live coordinator PID, inactive
owned slice, and no active owned jobs or remaining cgroup processes. Connection
details and pending output remain private; publish verified generic results after
the timers actually fire. The auditor changes no service state.


## 19 October03:42 UTC — Intel scan primary replication audited

Exact A/B scan replication passes both qualified primary cases on Intel. Root audit
reconstructs48 A/A +96 candidate rows,36 total blocks, frozen hashes, serial CPU2,
callbacks/checksums and exact owned memory. A medians−6.666%/−3.847%; B−6.665%/−3.661%
at100K/1M. B alone advances under the preregistered source preference, not a speed
superiority claim. Full guards, fresh confirmation and matched profiles remain.
Source NONE; AWS counts stay7 populations (0 accepted/4 rejected/3 parked), plus
one parked ARM replication and the in-progress Intel replication. ARM prepares
focused guard fixtures; AMD profiles a distinct deletion offset-adjust loop.
See AWS-DECISIONS.md and reviews/aws-intel-scan-raw-audit.json under NIGHT-EXPLORATION-001.
Lease release remains08:00UTC; live restoration verification is still required.


## 19 October 03:47 UTC — AMD deletion proposal chair selects NONE

Three actual independent proposals agree on a plausible portable rewrite of the final
offset-adjust loop, conditional on precision qualification. The fixed1M A/A fails;
root independently audited48 rows /12 blocks, including exact schedule, serialCPU2,
checksums, actual deletes and owned memory.100K qualifies;1M ranges+0.499..+4.682%.
The chair selects NONE before implementation; no retry, candidate or new measured
population. All proposals and baseline profile/census/control evidence are retained.
AWS counts remain7 populations (0 accepted/4 rejected/3 parked), plus a parked ARM
replication and Intel scan B follow-up. Source NONE.
[Chair and participant evidence](reviews/aws-amd-delete-population/selection.md).


## 19 October 03:51 UTC — Focused scan referee independently reviewed

Root verified the immutable ARM publication2ab283daa:108 baseline cells,368 commands,
eight realistic wrong-output controls, source/referee hashes, genuine tag distributions
and native diagnostic parity. Approved for Intel baseline qualification and B comparison
within the frozen300s/900s/900s phase budgets. Sparse reversal (one64-member leaf),
absent active resize/wide IDs and incomplete length boundaries remain explicit gaps.
No timing or source acceptance follows from this referee validation.
[Review](reviews/aws-focused-scan-referee-review.json).

A targeted publication check scanned25,819 text files across main and three worker
worktrees for the known private endpoints/key path; no matches. This is a targeted
check, not a comprehensive secret audit.


## 19 October 04:01 UTC — Native ARM scan chair selects NONE

All three actual independent proposals identify bounded native-vector all-match
comparison as plausible, conditional on qualification. Fresh5M-op controls fail
first1M block at+1.889270895%;100K qualifies. Root independently verified48 raw rows,
12 blocks and107 sealed files, exactsource/referee/driver hashes, serialCPU2, callbacks,
checksums and owned memory. NONE before implementation: no retry or failed-row removal.
All proposals/profile/controls remain. No candidate or new measured population.
[Chair](reviews/aws-arm-native-scan-population/selection.md),
[raw audit](reviews/aws-arm-native-scan-aa-audit.json).
Intel B remains in follow-up; independent untouched-seed confirmation will run only
after its current baseline guard job explicitly hands over the idle runner.


## 19 October 04:03 UTC — Independent review and confirmation handoff preparation

AMD independently reviewed exact Intel B discovery and frozen focused referee, published
9b6e529b5. No semantic or discovery-parity blocker found; incomplete/noisy guards and
missing confirmation/profile still preclude adoption. One actual reviewer; no fabricated
panel, serving model or cost. Confirmation protocol5c29cb07f reserves fresh201–203,
48 baseline A/A processes then conditionally48 B processes,300s per phase. No Intel
access or held-out execution before explicit idle handoff. ARM and AMD own runners
are idle; they have not been released to OSS yet.


## 19 October 04:07 UTC — Intel full original control audit

Root independently reconstructed120 serial processes/960 rows/240 paired blocks across
all eight operations,five sizes and16/128-byte members. Frozen hashes, exact schedule,
CPU2, callbacks/checksums and owned memory pass.57/80 cells qualify;12 insert/delete
cells are shorter than10ms and11 other cells fail precision. Complete original guard
qualification is unavailable; no primary result can override these gaps. All cells
remain in the separately frozen diagnostic B comparison.
[Root audit](reviews/aws-intel-original-guards-aa-audit.json), worker d9713d463.

Root independently verified the Intel runner idle at04:05:08UTC and granted AMD
the frozen independent confirmation protocol5c29cb07f. Intel waits until explicit
return. Source NONE; measured population counts unchanged.


## 19 October 04:11 UTC — Independent Intel B primary confirmation passes

Independent AMD operator on the Intel runner completed48 held-out A/A and48 B
comparison processes, seeds201–203 twice. All12 controls qualify and all12 candidate
blocks improve at least2%. B median elapsed changes are−6.783% at100K and−3.656%
at1M; ranges−6.858..−6.344% and−3.735..−3.580%. This is an Intel result, not an AMD
machine result. Immutable operator evidence27fed33a7; no retries/exclusions.

Root independently reconstructed all96 rows/24 blocks, frozen protocol, exact schedule,
serialCPU2, callbacks/checksums/owned memory across both phases, and source/referee/
binary hash records. Root also read the live binary hashes and independently verified
the runner idle04:09:44UTC before returning ownership to Intel.
[Root audit](reviews/aws-intel-scan-confirmation-raw-audit.json).

This closes only the fresh independent primary-confirmation gate. Full original
controls qualify57/80; diagnostic full B guards, focused guards and matched profiles
remain. **PARK/source NONE**, not acceptance or a portable/full-suite speedup.
Measured population counts remain7 (0 accepted/4 rejected/3 parked).
