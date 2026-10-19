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


## 19 October 04:21 UTC — Guard and profile follow-ups

Intel B original-operation guards run serially under the frozen 1440-second cap;
AMD independently audits the raw comparison after publication. The matched profile
revision was frozen before any candidate capture: 120 fixed captures / 600 seconds,
with all captures retained and callback-normalized counts. The unexecuted original
12-capture plan remains preserved. This increases sample coverage without changing
source, scope or requested operations; it is not a retry after profile outcomes.

ARM prepares a separate baseline-only supplemental referee covering fully reversed
leaves, active resize, 8/319/320/321/1024-byte members and ordinary/tied/signed-zero
scores. This is correctness and coverage engineering, with no candidate timing yet.
Existing focused guards remain immutable. AWS source/referee stays pinned to
8fab511e, including its original adapter; the separate main/M6 adapter correction
is a different baseline identity. No population counts or decisions change.


## 19 October 04:21 UTC — Release auditor correction

Read-only live inspection found systemd nests the campaign slice beneath its parent
slices. The auditor previously inspected an incorrect top-level cgroup path, which
could silently miss remaining processes. It now verifies the live ControlGroup,
walks its descendants, and fails verification on inspection errors. Six targeted
tests and an independent static review pass. The corrected live preflight detects
three Intel job processes and zero AMD/ARM job processes; every coordinator remains
stopped and no host is yet released. Host restoration timers are unchanged.
[Sanitized preflight](reviews/aws-release-auditor-preflight.json).


## 19 October 04:29 UTC — Corrected-adapter baselines queued

Main13e459ff8 contains the independently reviewed C11 `_Noreturn` correction to the
standalone panic declaration and definition, plus an isolated build-path option.
Each AWS host will requalify this distinct harness identity in a fresh detached
checkout after its current serial queue: the original five-size/eight-operation
matrix,16-byte members,1M requested operations,seeds1/2/3,six same-binary ABBA blocks,
seven native/sanitizer validation stages,1200-second timing cap and1800-second owned
job cap. Source/referee/binary hashes are retained before and after.

This is baseline requalification, not a new optimization population, an old/new
adapter speed comparison, or a retry of the original candidate controls. All prior
8fab511e evidence, decisions and timing binaries remain unchanged. No new baseline
results are claimed yet. The actual detached Git HEAD must match the recorded
source identity; a plain archive must not silently inherit a parent checkout's HEAD.


## 19 October 04:33 UTC — Full original Intel B guards remain PARK

Independent AMD review72553e841 reconstructs both120-process phases:1,920 raw rows,
480 block effects, exact serial CPU2 schedule and fixture/memory identity. All22
post-phase source/referee/binary hashes match. Of57 qualified cells,56 pass every
guard block. The100-member/16-byte iteration guard has+0.304%,−0.825%,+1.329%;
its mixed exceedance remains unresolved. No qualified cell has all three blocks
above+1%. Another23 cells retain failed/short controls, leaving24/80 unresolved.
Unqualified100/128 insert has three positive effects, retained as exploratory
rather than silently passed or promoted to a demonstrated regression.

PARK/source NONE. Independent primary confirmation remains valid only in its
narrow scope. Matched profiles and focused/supplemental guards continue serially.
Root verified the independent reports against their immutable publication.
[Audit summary](reviews/aws-intel-original-guards-independent-summary.json).
Measured AWS populations remain7:0 accepted/4 rejected/3 parked; no new population.


## 19 October 04:42 UTC — Profile, portability and corrected-baseline checkpoints

Independent review5bffe4d28 reconstructs all120 matched Intel captures. Helper
samples base→B are337→316 at100K and419→316 at1M, with matched callback denominators.
The21-sample100K gap is coarse;1M is directionally stronger. SSE2 codegen is present,
but these are captured-text samples from diagnostic layouts, not exact cycles or
a quantitative explanation of elapsed gains. All24 diagnostic and22 original
post-phase hashes match. The24 unresolved original guards still prevent adoption.
[Independent profile summary](reviews/aws-intel-matched-profile-independent-summary.json).

Exact B also passes native ARM original43 tests and V2 oracle299664 checks in both
release and ASan/UBSan through the natural portable fallback. Root verified the
24-file seal, exact source identity and14.2-second bounded CPU2 job. This is
correctness only, not performance qualification or big-endian coverage.
[Portability review](reviews/aws-selected-b-native-arm-review.json).

Separate corrected-adapter baselines on13e459ff8 now complete on AMD and ARM. Root
independently reconstructs120 processes/960 rows/240 blocks per host, exact schedules,
raw hashes, source/runner identities, validation commands, paired memory and summaries.
AMD qualifies11/40:11short plus18other noisy cells. ARM qualifies21/40:11short plus
8other noisy cells. All seven native/sanitizer stages pass on each host. M6's separate
corrected baseline also audits successfully with5/40 qualified; Intel remains queued.
[AMD raw audit](reviews/corrected-aws-amd-baseline-audit.json),
[ARM raw audit](reviews/corrected-aws-arm-baseline-audit.json).

AMD and ARM will reassess scan only under the corrected identity, starting with
separately frozen baseline profiles and48-row A/A controls at5M requested operations,
100K/1M members and seeds401–403 twice. No candidate timing is yet authorized.
Failed controls stop that new comparison without retry. These new harness results
do not repair or replace any original8fab511e decision. Source NONE; measured
AWS population counts remain7:0 accepted/4 rejected/3 parked.


## 19 October 04:45 UTC — Apple branch status checked read-only

Git fetch confirms M6 publication8efe8804c with corrected-adapter profile analysis
and preparation for a bounded counter capability probe; source NONE. M1's latest
published revision remains4c48fa7ed (01:33 UTC, round2), and its status reports an
unresolved DNS check. The AWS controller does not claim M1 is currently running
and does not access or alter either Apple runner. Original M1 baseline evidence
remains valid for its recorded identity; no corrected-adapter M1 baseline exists
in this campaign's published evidence.


## 19 October 05:00 UTC — corrected ARM population selected; AMD exact replication

Fresh corrected-adapter scan controls qualify on both ARM and AMD. Root independently
reconstructed each48-row/12-block schedule, CPU2 serial windows, checksums/callbacks,
exact owned memory and source/referee/binary identities. Maximum absolute A/A changes:
ARM0.398%/0.762%, AMD0.504%/0.890% at100K/1M. Scoped profiles link to the actual timing
binaries; this is a distinct13e459ff8 source identity, not a rescue of old8fab controls.

Three actual independently authored ARM proposals agree on bounded16-byte native NEON
exact tag matching. Root selects that one hypothesis for three isolated implementations,
with fixed correctness,144-row discovery and held-out confirmation contracts. Existing
21 patches and seven completed populations remain unchanged until this new round is
measured. [Chair and proposals](reviews/aws-arm-corrected-scan-population/selection.md).
AMD separately validates exact selected x86B under the corrected adapter before its
fixed48-row comparison; no new x86 population or candidate switching. Intel continues
its frozen old-adapter focused guards, then its corrected baseline and supplemental
guards. All source adoption remains NONE; no claim of a completed optimization.


## 19 October 05:06 UTC — corrected AMD replication rejected; ARM implementations sealed

Root independently reconstructs corrected AMD exactB evidence db7fdb5b4:60 validation
commands, four original43-test runs,30 oracle executions,48 serialCPU2 raw comparison
rows,12 ABBA effects, original A/A fixture joins and exact source/memory/binary identities.
Median elapsed changes are−1.848% at100K and−1.785% at1M; only2/6 blocks per size meet
2%. **REJECT this replication / NONE**, no guards/profile/confirmation advancement or
retry. This is not a new population, and original8fab scan PARK remains unchanged.
[Independent audit](reviews/aws-amd-corrected-B-independent-audit.json).

All three corrected ARM NEON implementations are sealed independently: A=a223b96b1,
B=9b2456c01,C=3b137666b. Root static review finds no blocker and exhaustively verifies
65,536 lane-match patterns for each of the two reduction methods. Native correctness,
codegen and timing remain pending. Frozen maintenance scores A28/B26/C26 give B,C,A
preference only among implementations passing every primary block, not a speed ranking.
[Review and retained patches](reviews/aws-arm-corrected-scan-population/implementation-static-review.md).

Intel focused A/A completes864 rows/216 blocks,22/36 qualified cells,14 precision
failures and no short windows. Root independently checks immutable c5a734191 raw data,
all36 retained fixture hashes, frozen schedules, serialCPU2, semantic/memory parity and
24 post-phase source/referee/binary identities. Full fixed candidate comparison continues,
retaining all failed-control cells. No new accepted source; completed AWS populations
remain7 (0 accepted/4 rejected/3 parked), plus separate replications.
[Focused control audit](reviews/aws-intel-focused-aa-independent-audit.json).


## 19 October 05:18 UTC — ARM discovery approved after native review

All three corrected ARM implementations pass the fixed native validation: 145 serial
commands, eight original 43-test runs, 56 semantic suite runs, six forced-portable
oracle runs and eight detected faults. Root independently checks every required
outcome, source/referee/patch hash, native vector codegen and comparison binding.
AMD independently reviews coverage/provenance, explicitly disclosing authorship of C.
The rebuilt baseline text equality is supported by the completed frozen driver; neither
reviewer claims to have independently rehashed unpublished section bytes. The overread
fault fails a count/canary assertion before a page signal, so no signal proof is claimed.

Root approves the exact 144-row, 300-second discovery schedule, source13e459ff8,
actual baseline8694 and frozen candidate binaries from24a1694d6. No retry or source
repair. Maintenance preference B,C,A applies only to complete primary survivors.
[Native review and grant](reviews/aws-arm-corrected-scan-population/native-validation-review.json).
Completed population counts remain seven until this round is measured.

The independent full Intel focused audit223d6d7de reconstructs 2,052 processes and
432 paired effects: all 22 qualified guard cases pass; 14 noisy controls remain
unresolved. Across all candidate blocks, changes range from−24.951% to+0.260%, but
unqualified rows remain exploratory. Original 24 guard gaps still block adoption.
[Independent summary](reviews/aws-intel-focused-independent-summary.json).

AMD's separate corrected rank/update profile survey4ed690fd1 completes 74 commands
and 12 scoped captures with matched controls and actual timing-binary mapping.
Sampled instruction locations identify index probing/ID stores as diagnostic topics;
load/store adjacency and sampling skid prevent calling their arithmetic removable.
No new hypothesis is selected. Intel's corrected baseline runs before its frozen
supplemental guards; a distinct corrected SCAN profile/control plan is queued later.

The05:08 live release preflight verifies all three coordinators remain stopped,
all host timers still target08:00UTC/09:00Lisbon, and cgroup inspection reports no
errors. This is not release proof; the final live auditor remains scheduled08:00:20.
[Sanitized preflight](reviews/aws-release-preflight-0508.json).
