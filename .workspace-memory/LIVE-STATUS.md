<!-- EXPERIMENT-FLOWS-20261020 -->
Architecture Sankey and source-linked ledger: experiments/EXPERIMENT-FLOWS-20261020/README.md.
22 unique populations = M1 9 + M6 12 − 7 shared inherited + AWS 8; 9 PARK / 13 REJECT / 0 approved.
11 follow-ups shown separately; historical host counts and decisions unchanged.
Main README pruned. User explicitly prefers concise messages and useful results over bloat.
<!-- EXPERIMENT-FLOWS-20261020-END -->

<!-- MAIN-CONSOLIDATION-20261019 -->
Published performance history consolidated into main: M1 overnight + lookup A/A,
M6 overnight, AWS ARM/Intel/AMD. All six pinned tips are ancestors; 154,955 evidence
files match exact branch blobs/modes. Existing source/referee files unchanged.
Current shared status retained; exact worker notes archived. Source NONE and all
counts/decisions unchanged. Publisher combines AWS support/runtime summary with M6
requests/isolation/acknowledgements. See experiments/MAIN-CONSOLIDATION-20261019/README.md
and validation/checks.json. CPU MCP upstream PR #13 remains separate and open.
No runner resumed and no new performance investigation conducted in this integration.
<!-- MAIN-CONSOLIDATION-20261019-END -->

<!-- MCP-PR-CURRENT -->
CPU-perf upstream PR #13 opened with explicit user authorisation:
https://github.com/usamahz/cpu-performance-engineering/pull/13
Head a5a05e6 fixes unknown clock/SMT state handling and equivalent metadata wording.
Actual evals36/36 vs10/36 baseline; falsequotable18→0; fullsuite211passed/2crawled-DB
skips; realstdio36/36; existinglistretrieval21/21. UpstreamCI action_required, not
passed. See experiments/MCP-TOOLING-REVIEW-001/pr-validation/VALIDATION.json.
No source-tree optimisation, AWS workload, new population or upstream merge.
<!-- MCP-PR-CURRENT-END -->

<!-- M6-BRACKET-CURRENT -->
M6-CLOCK-BRACKET-001 CLOSED: lookup clock-bracket harness implemented and validated;
fresh two-size baseline PARK, source NONE. Original43 tests pass native+ASan/UBSan,
36 paired frontend checks match exact output/memory, and72 empirical controls pass
sensitivity. Three empty conditional intervals remain INCONCLUSIVE; physical clock
accuracy/accounting error UNVALIDATED. Fresh48 A/A rows qualify100K6/6 and1M2/6,
with four retained1M failures. Independent B raw audit and C decision review PASS;
134 commands/268 streams and all frozen identities verified. Native lease RELEASED,
no queued workload. New harness/diagnostic/baseline add zero source populations;
historical M6 counts12:0accepted/7rejected/5parked unchanged. Old EXP-009 and offline
diagnosis remain frozen. Read experiments/M6-CLOCK-BRACKET-001/RESULTS.md.
<!-- M6-BRACKET-CURRENT-END -->

<!-- M6-METROLOGY-CURRENT -->
M6-METROLOGY-001 CLOSED offline diagnostic: root plus3actual independent reviewers reconstruct all48rawrows/12blocks/96streams. All3failed1Mwallcontrasts alsofailthreadCPUdiagnostic; residualcomponent≤0.029wallpp. Nestedclockbrackets/accountingerror remain unbounded, so no strictcausal attribution orclocksubstitution. Seedrepeat signflips confounded withtime/sizeorder; endpoints notresidency. NONE for a ready corrective method. Future nestedclock-attribution design is unimplemented/unexecuted; no nativeworkload/lease queued. Source NONE and EXP-009 PARK unchanged; M6historical12populations0accepted/7rejected/5parked unchanged. Read experiments/M6-METROLOGY-001/RESULTS.md and selection.md.
<!-- M6-METROLOGY-CURRENT-END -->

<!-- PERFORMANCE-MCP-RULE -->
User rule (19 October2026): every Codex and Claude investigation/optimization session
must use the cpu-perf MCP from usamahz/cpu-performance-engineering. Read
[docs/PERFORMANCE-MCP.md](../docs/PERFORMANCE-MCP.md): discover/library_status,
ask with actual investigation context, follow source evidence, log actual calls and
limits; explicitly record unavailable tools rather than inventing consultation.
Keep retrieval/indexing off the measurement runner and preserve frozen protocols.
<!-- PERFORMANCE-MCP-RULE-END -->

<!-- M6-CPU-PERF-CONSULTATION -->
M6 controller CPU-perf consultation is now operational through local stdio (server0.1.1,bundleddeb5a0bac467). Actual calls and coverage/parser limits are recorded in experiments/EXP-009/cpu-perf-consultation-20261019/. This consultation occurred after EXP-009 closure; it changes no frozen inputs or PARK decision and queues no benchmark. Direct host tools remain unexposed; use the documented compatible stdio route and record each session accurately.
<!-- M6-CPU-PERF-CONSULTATION-END -->


<!-- ARM-FRONTEND-DIAGNOSTIC-CURRENT -->
## ARM frontend diagnostic closed — 19 October11:24UTC release

Final native explanationINCONCLUSIVE; exact candidateREJECT/sourceNONE unchanged.
Native288rows/72blocks qualify all6cells: primary−7.775%/−7.194%; H4forward+2.903%/
+2.953%, reverse+8.431%/+3.141%, everyguardblockregresses. Fixed profile266360cfb
completes642commands/415.038s: all18instrumented instruction pairs decrease1.744–1.777%,
but only2/12source-cell transfercontrols qualify (zero complete control/A pairs),
and strict mapping credits1685/1837treeevents with152entrysamples uncredited.
No post-result mapping exception, retry, source adoption or causal claim. Root132cf5be7,
Intel16118f441 and AMDf1ffd7e17 independently audit raw evidence/limits.
Early release11:24:28UTC; fresh live11:24:35–37 proof confirms OSSRUNNING withmatching
saved/livePID, freshmarker, inactiveslice, zeroownedunits/PIDs/noerrors. Timer stopped
only aftersuccess; pendingauditor cancelled afterproof; privatefleetRELEASED.
Intel/AMD stayedreleased. No queuedwork/currentlease. HistoricalAWS8populations
remain0accepted/5rejected/3parked; thisdiagnosticaddsnone.
MandatoryMCP rule dfff5540f applies to everyCodex/Claude session. Actualrootconsultation
and resultreconsultation logged;0/287sourcesindexed/no supportingpassages, nomechanism.
[Final report](../experiments/ARM-FRONTEND-DIAGNOSTIC-001/RESULTS.md) ·
[Live proof](../experiments/ARM-FRONTEND-DIAGNOSTIC-001/RELEASE-FINAL.json).
<!-- ARM-FRONTEND-DIAGNOSTIC-CURRENT-END -->

<!-- ARM-MASK-FOLLOWUP-CURRENT -->
## ARM follow-up closed — 19 October 10:03 UTC handback

Final REJECT / source NONE. All six fixed timing phases completed: 4,272 processes /
5,952 rows. Primary451456c2f retains −7.780706% / −7.212021%, but iterator comparison
f30ac4330 has nine qualified all-six-block losses (median +2.860% to +8.519%),
30 qualified passes, four mixed cases and39 unqualified controls. Root and independent
Intel d3cc358f2 verify rows, exact AA/fixture/checksum/memory/source/binary joins.
All nine losses are score-only under the distinct frozen guard frontend; cause of
the disagreement with the primary frontend remains unmeasured. No retry/retuning.
Original controls/comparison retain11 required noisy cells,11 short diagnostics,
17 qualified passes and one mixed100-member SCAN. Earlier PARK checkpoints preserved.
Correctness composite preserves FAILED8cdebdcba + six-only19fd53594; passes2,048 mode
runs, four original43-test suites,12 oracles,14 faults. No source/referee weakening.
Matched profile0a1040780 and held-out confirmation are UNEXECUTED after rejection.
No queued workload, no current runner lease, no adoption or upstream action.
Early owned release script succeeded10:03:18UTC while timer armed; timer stopped
only after success. Independent live audit10:03:25–27 verifies OSS RUNNING with
matching live/saved PID, fresh marker, inactive slice, zero owned units/recursive PIDs,
no errors. Pending read-only auditor cancelled only after proof. Private fleet
reservation RELEASED. Intel/AMD stayed released. Historical eight AWS populations
remain0 accepted /5 rejected /3 parked; this exact-candidate continuation adds none.
[Final report](../experiments/ARM-MASK-FOLLOWUP-001/RESULTS.md) · [Live proof](../experiments/ARM-MASK-FOLLOWUP-001/RELEASE-FINAL.json).
<!-- ARM-MASK-FOLLOWUP-CURRENT-END -->

<!-- AWS-CURRENT-START -->

EXP-009 guarded M6 lookup follow-up: PARK before proposal/implementation/candidate timing. Fresh native/sanitizer/oracle validation and profiles pass;48A/A runs qualify100K6/6 but1M3/6, with−1.414%,+1.036%,+2.567% failed controls despite586–630ms windows. Source NONE; local M6 native ownership released, no workloads queued. All new evidence publishes on main; read experiments/EXP-009/RESULTS.md and STATUS.md. Historical overnight counts unchanged; remote ARM follow-up remains separate.

## AWS overnight campaign complete — 19 October 08:01 UTC

All three requested AWS hosts were reached by SSH, their OSS coordinators stopped
for the campaign, and original/corrected baselines completed. Live fleet release
verified during 08:00:20–08:00:25 UTC: coordinators RUNNING with live/matching saved PIDs,
fresh files, inactive owned slices, zero owned units/recursive PIDs, no query errors.
Private fleet reservation RELEASED and pushed. No further runner work is authorized
by the expired overnight lease. Main tree source remains unchanged; adoption NONE.

Eight measured AWS populations: 0 accepted / 5 rejected / 3 parked, 24 retained
patches (21 public-tree patches, 3 private decoder-control variants). Replications
are separate: original Intel scan REJECT after qualified +4.93% trim guard; corrected
Intel PARK before candidate timing; corrected AMD exact-B REJECT. ARM has two parked
architecture replications. Latest historical EXP005A screen passes all12 primary
blocks, medians−7.77%/−7.10%, but remains PARK pending guards, fresh confirmation and
matched candidate profile.570 validation commands include536 correctness/fault checks.

Original five-host chart retained. Corrected-adapter chart covers M6/Intel/AMD/ARM,
3840 rows/160 cases, qualified5/10/11/21 of40 respectively; no corrected M1 baseline.
Compiler/OS/affinity differences prevent causal architecture rankings. Apple ledgers
remain separate. M1d41738b05/2baeafcef resolves earlier DNS/publication failures;
M6 final85afa6c7b reports campaign closed/no queued workload. No Apple-host control.

[Morning report](../experiments/NIGHT-EXPLORATION-001/AWS-MORNING-REPORT.md) and
[live handback proof](../experiments/NIGHT-EXPLORATION-001/reviews/aws-release-final.json)
are the current entry points. Historical entries below retain prior task states.
Native model/token/currency costs unknown. No upstream actions.
<!-- AWS-CURRENT-END -->

# Live status — round20 final handoff, 2026-10-18 UTC

## Latest completed task: EXP-007 bulk specialization

[Results](../experiments/EXP-007/RESULTS.md): B has fresh full-leaf gains (-33.14%
primary; about -43% aligned) and repeated short-range losses (+20.79%, +10.60%,
+6.49%). Reject B as a universal replacement; retain bulk direction PARK, source
NONE. These losses had qualified discovery controls, not merely unresolved noise.
4320 serial processes / 557280 measured batches completed in 67.65 seconds total.
All semantic/sanitizer checks and raw-data audits pass. Two genuine three-agent
population steps and cross-author reviews completed. Main source and original
scalar iterator unchanged; no integration started because guards fail. Next is a
new preregistered short-range scalar fallback experiment. Overnight stays stopped.

## Latest task completed: 19 October decoder diagnostic

The user approved a focused Lemire-style benchmark. It is implemented and measured:
[report](../experiments/EXP-004/decoder-microbench-2026-10-19/README.md).
960 serial processes / 123,840 batches finished in 12.58 seconds; release/sanitizer
checks and raw reconstruction pass. A regresses aligned 8-bit/64-bit decoder loops.
EXP-004 A/PARK and production baseline unchanged. No new population. The overnight
supervisor remains stopped; do not infer permission to restart it from this run.
This adds one standalone harness/diagnostic after historical overnight totals.

## Round 20 final extension and sealed handoff

The final bounded generation-wrap matrix passes8 additional control/A/B/C cells and
8 builds on fresh94503/94521 seeds. Each cell retains four fixtures,262160 natural
resizes, four65535→1 growth wraps,262188 complete models and24254190 exact results.
Only seed literals changed; no new fault or timing run. Round20 final total:112 passing
semantic cells and six detected repeated faults. Earlier104-cell checkpoint and all
469 sealed files are preserved and reverified; final report/seal supersede it.

Final audit PASS:3960 hashes,220 serial experimental windows,23 reconstructed patches,
including all15 optimization patches. Last experimental child ended06:25:59UTC.
No more experiments start. Counts remain7 harnesses/13 baselines/34 diagnostics/
26 named suites/5 sequential populations;0 accepted/2 rejected/3 parked. SourceNONE,
EXP-006C/PARK and all other decisions unchanged. Main baseline preserved.

Canonical [round20](../experiments/OVERNIGHT-2026-10-17/ROUND-020.md),
[coverage](../experiments/OVERNIGHT-2026-10-17/ROUND-020-CANDIDATE-COVERAGE.md) and
[next action](../experiments/OVERNIGHT-2026-10-17/ROUND-020-NEXT.md). Final worker must
write MORNING-REPORT.md before07:00UTC/08:00Lisbon, using the supplied morning draft
and final seal. Same-size cleanup and actual architecture portability remain gaps;
forced scalar fallback is not big-endian testing. Independent review/confirmation,
qualified performance guards and committed provenance remain pending. Reviewer startup
failed; exact backend/model/token cost unknown, supervisor CLI accounting separate.
No publishing, git retry, credentials, permission or supervisor/runtime/STOP edits.


## Latest: EXP-008 / Apple M1 decoder work

EXP-008 is complete on Apple M1. Scalar cutoffs 4/8/16 failed the frozen count16/count96
primary gates; count16 A/A precision failed. No confirmation, no selected candidate, and
root source remains unchanged. The count1 scalar path is only a lead for a separate
experiment. All recent focused decoder results (EXP-004/007/008) are Apple M1 observations.
The user plans to rerun the latest decoder campaigns on Apple M6 mini; use
`experiments/REPLICATE-LATEST.md`, host-specific output folders, and separate A/A/results.
Do not pool M1 and M6 rows. EXP-008 completed 15360 serial processes / 1981440 batches in
265.83s; all release/sanitizer tests and raw audit pass. Frequency, DVFS, actual core use
and within-window migration remain unknown. Source/hash baseline is EXP-008 commit plus
M1 host metadata in its run manifest.


## Latest: four-size baseline ready for M6 replication

Completed SIZE-MATRIX-001 on Apple M1: 100/1K/10K/100K members × all eight standard
operations, 16-byte members, three seeds, six same-binary ABBA blocks. All 32 cells,
96 processes and 768 rows are retained; timing took 79.03 seconds. Native/sanitizer
tests and raw-data reconstruction passed. All cells show >1% variation in at least
one A/A block; 10 have <10 ms windows. No optimization acceptance or source change.
See [report](../experiments/SIZE-MATRIX-001/README.md), README chart, and
[M6 runbook](../experiments/REPLICATE-LATEST.md). The user requested publishing the
plan/documentation so they can follow up on M6. Run the same matrix into a new
host-specific directory and compare separately; do not overwrite M1 evidence.


## Latest: five-size M1 results and shared night plan published

SIZE-MATRIX-001/apple-m1-five-sizes completes 100/1K/10K/100K/1M × all eight operations:
120 processes, 960 rows, 40 cells, 351.43s timing; native/sanitizer checks and raw audit
passed. Variation remains (39 cells >1% in an A/A block, 11 short cells). No tree change.
See experiments/NIGHT-EXPLORATION-001 for the shared M1/M6 eight-hour plan, launch/stop
commands, population/measurement rules, and pinned Lemire template/blog/cbitset review.
All documents/results are prepared for publishing; no overnight run started. User
wants M6 follow-up using the same five-size definitions and separate host evidence.


## 19 October 2026 — AWS overnight launch

Three user-authorized hosts (Intel Sapphire Rapids, AMD Zen 5, ARM Neoverse V2)
passed SSH preflight; OSS coordinators stopped, five-size baselines running from
8fab511e with Clang18/CPU2. Independent release timers restore OSS at08:00UTC /
09:00Lisbon. [Live status](../experiments/NIGHT-EXPLORATION-001/AWS-STATUS.md). Public Git/README/chart updates requested after
completed evidence. No new optimization decision; population counts unchanged.


## 19 October — AWS baselines complete and native workers active

All three AWS baselines pass seven native/sanitizer validation stages and raw audit:
120processes/960rows/40cells each, frozen8fab511e. Intel338.54s/27noisy cells,
AMD325.44s/30noisy cells, ARM377.83s/19noisy cells;11short cells each. Results
committed4e8edf65; five-host README chart now measured. Source adoption NONE and
optimization counts unchanged. Detached CLI workers failed bwrap uid-map setup;
original reports preserved, supervisors stopped. Native agents independently
verified SSH and continue on host branches, no permission changes. Deadline08:00UTC.


## 19 October 02:20 UTC — two independently audited AWS rejections

AMD lazy lower-bound metadata decoding and Intel bounded SSE2 lookup scanners both
failed the preregistered speed gate. Root independently audited all 144 AMD and 432
Intel raw processes. AWS count: 2 measured populations, 0 accepted / 2 rejected /
0 parked; ARM's corrected-profile withdrawal was unmeasured and is excluded. No
source adoption. Host workers continue distinct profile-led directions until the
08:00 UTC deadline. See the central AWS-DECISIONS.md ledger and retained host patches.


## 19 October — AMD builder-write rejection independently audited

BUILDER-WRITE-001 qualified A/A but all three candidates slowed every primary block.
Root reconstructed144rawprocesses/36effects; sourceNONE. AWS totals3measured
populations,0accepted/3rejected/0parked. ARM's count-one exploratory population
continues after failed longer-duration qualification. Intel's update diagnostic
selectedNONE without implementations; bounded iterator profiling is underway.
See experiments/NIGHT-EXPLORATION-001/AWS-DECISIONS.md for exact evidence links.


## 19 October — ARM decoder parked; AMD full chunks rejected

Root independently audited ARM's4175 longer-control/comparison CSVs and AMD's144
full-chunk screen CSVs. ARM has a conditional private-helper count-one lead but failed
precision and guard concerns; identical candidate text cannot select a winner.
AMD full-chunk candidates all miss2% in every primary block. SourceNONE. AWS totals
5completed measured populations:0accepted/4rejected/1parked. Intel iterator screen
continues; ARM public-update profiling and AMD SDS-length assembly inspection are
new diagnostics, not selected winners. See central AWS-DECISIONS.md for exact links.


## 19 October03:03 UTC — Intel iterator parked; ARM replication underway

Intel ITERATOR-CACHE-001 fixed300s screen stops566/576 processes,141 complete blocks
+2 trailing rows. A/B conditional primary leads, C slower;100K A/A fails and full
guards/confirmation remain pending. Root independent raw audit verifies192 A/A and
566 comparison rows, exact schedule prefix, hashes, serial CPU2 windows and fixture/
owned-byte parity. Source NONE. AWS totals6 measured populations:0accepted/4rejected/
2parked. ARM separately profiles exact A/B for possible native replication; AMD
investigates index scan after inner-child chairNONE. Live workers/decisions are in
experiments/NIGHT-EXPLORATION-001. Release timers remain08:00UTC; read-only auditor
scheduled08:00:20UTC, actual restoration still unverified before deadline.


## 19 October03:19 UTC — ARM iterator replication independently audited

Exact Intel A/B patches completed all 576 ARM raw processes / 144 blocks. Both
primary A/A controls fail; favorable primary observations remain PARK, no winner.
Root verifies every row, frozen schedule/hash, serial CPU2 windows, fixture/owned
bytes, result seal and fresh live binary hashes. A state24 bytes, B16. No adoption
or timing pooling. AWS counts remain6 populations (0 accepted/4 rejected/2 parked),
plus1 parked architecture replication. AMD's distinct all-match SSE2 round now
has3 actual independent proposals and implementations, root chair/static review
0695cf415/e47157087; serial correctness/fault controls precede its fixed exploratory
screen.1M scan A/A fails, so acceptance is unavailable. Lease/release08:00UTC intact.


## 19 October03:36 UTC — AMD scan parked; qualified Intel controls

AMD SCAN-TAGS-001 completes 144 rows/36 effects after123 validation commands and
eight detected faults. A/B conditional gains about4–5%, C fails1M every-block gate.
Failed AMD1M A/A and missing guards/profile magnitude keep PARK/NONE. Root raw audit
verifies48 controls+144 comparison rows and exact schedules/callbacks/memory. AWS
count7 populations (0 accepted/4 rejected/3 parked), plus1 parked ARM replication.
Actual independent AMD/Intel/ARM proposals and implementations, separate root chair.
Intel's fresh5M-op scan controls qualify both sizes; exact A/B replication begins
after validation. B is predeclared source preference if both pass, not a speed
superiority claim. ARM prepares missing focused guards; AMD profiles deletion only.
No source adoption. Deadline/release08:00UTC unchanged. Dashboard push race repaired
without dropping its pending commit; bounded rebase/push retries now installed.


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
[Chair and participant evidence](../experiments/NIGHT-EXPLORATION-001/reviews/aws-amd-delete-population/selection.md).


## 19 October 04:01 UTC — Native ARM scan chair selects NONE

All three actual independent proposals identify bounded native-vector all-match
comparison as plausible, conditional on qualification. Fresh5M-op controls fail
first1M block at+1.889270895%;100K qualifies. Root independently verified48 raw rows,
12 blocks and107 sealed files, exactsource/referee/driver hashes, serialCPU2, callbacks,
checksums and owned memory. NONE before implementation: no retry or failed-row removal.
All proposals/profile/controls remain. No candidate or new measured population.
[Chair](../experiments/NIGHT-EXPLORATION-001/reviews/aws-arm-native-scan-population/selection.md),
[raw audit](../experiments/NIGHT-EXPLORATION-001/reviews/aws-arm-native-scan-aa-audit.json).
Intel B remains in follow-up; independent untouched-seed confirmation will run only
after its current baseline guard job explicitly hands over the idle runner.


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
[Root audit](../experiments/NIGHT-EXPLORATION-001/reviews/aws-intel-scan-confirmation-raw-audit.json).

This closes only the fresh independent primary-confirmation gate. Full original
controls qualify57/80; diagnostic full B guards, focused guards and matched profiles
remain. **PARK/source NONE**, not acceptance or a portable/full-suite speedup.
Measured population counts remain7 (0 accepted/4 rejected/3 parked).
<!-- M1-OVERNIGHT-CURRENT -->
M1 overnight campaign PUBLISHED: five-size public-operation baseline and
rank/update/lookup/decoder evidence at
experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/MORNING-REPORT.md.
M1 decisions 0 accepted / 3 rejected / 6 parked across nine populations;
source NONE. Strict baseline A/A fails 39/40 cells; M6 published gate checked
06:50 UTC and no further matching M1 source trial queued. Host totals separate.
<!-- M1-OVERNIGHT-CURRENT-END -->

<!-- M1-LOOKUP-AA-CURRENT -->
M1 EXP-009 lookup precision preflight PARK: 48 same-binary A/A processes;
100K passes 1/6 and 1M passes 2/6 blocks. All windows exceed 564 ms;
independent raw audit PASS. No proposal, candidate timing or source edit;
historical M1 population counts unchanged. See
experiments/EXP-009-M1-AA-001/RESULTS.md.
<!-- M1-LOOKUP-AA-CURRENT-END -->
