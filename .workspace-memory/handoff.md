<!-- ARM-MASK-FOLLOWUP-CURRENT -->
## Active ARM follow-up — 19 October 09:48 UTC

Fresh primary controls53e193c5b and candidate451456c2f pass all12blocks; medians
−7.780706% at100K / −7.212021% at1M, identical outputs/memory. Root/AMD verify.
Original controls1329e440a qualify18/29 required;11 noisy required +11 short diagnostic
cells remain unresolved. Comparison4c7668661:17 qualified passes,100-member SCAN mixed
(one +1.477795% block,five small improvements). Root/Intel73f66fe89 raw audits agree.
PARK/source NONE; acceptance/heldout confirmation blocked. Qualified losses can REJECT.
Iterator controls8ed45423c complete1968rows/492blocks in764.223s:43/82qualify,
39noisy required,no shortwindows(min44.7965ms). Root/Intel d68b27aa2 audits agree.
Root ddb4cf444 grants only fixed iteratorcomparison:1968processes/82cases,1500s,
60schild CPU2 freeze380ef3109; allcasesretained,43calibrated. No retry/retuning/
automatic nextphase. Fullcap+20 mustfit10:15UTC. Matched profile0a1040780 reviewed
but ungranted; heldoutconfirmation blocked. Additional qualified loss can REJECT.
Correctness composite preserves originalFAILED8cdebdcba + six-only19fd53594;2048 modes,
4original43/12oracles/14faults. No new population/source. Historical AWS8:0accepted,
5rejected,3parked unchanged. ARM-only lease ACTIVE; independent restore timer and
local auditor armed. Root must verify live handback early when finished or10:15UTC /
11:15Lisbon. Intel/AMD remain released. No upstream actions.
[Results](../experiments/ARM-MASK-FOLLOWUP-001/RESULTS.md) · [Live status](../experiments/ARM-MASK-FOLLOWUP-001/STATUS.md).
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

# Handoff

## Latest handoff: EXP-007 completed

[Result](../experiments/EXP-007/RESULTS.md): source NONE / experiment PARK. B was
shortlisted by the preregistered fewest-guard-loss rule. Its fresh 96-score primary
is 33.14% lower elapsed time; aligned 8/64-bit full leaves are about 43% lower.
Three short-range losses repeat, with qualified controls in discovery; B is not
eligible as a universal replacement. All candidates frozen before timing and
retained. Two three-agent populations were real; exact model/token/currency cost
unknown. Cross-author reviews are not independent-machine timing confirmation.
Referee commit fd1f96c5; candidate freeze 9a219300. Discovery/fresh audits validate
8640 raw files and 557280 batches; no samples excluded or candidate retuning.
No scalar iterator integration was attempted because guard eligibility failed.
Next: preregister a scalar-short / specialized-long bulk crossover with held-out
counts/seeds. No production adoption or overnight restart. Pre-existing round21
drafts remain local and separate from this task's published work.

## Latest handoff: focused decoder benchmark, 19 October

The user-approved focused benchmark is complete; see
[report and reproducible commands](../experiments/EXP-004/decoder-microbench-2026-10-19/README.md).
Harness commit c5b817d0 preceded the fixed local timing matrix. Release/sanitizer
checks pass, all 123,840 measured batches retained and raw-derived effects audited.
A is ~16%/~10% slower on forward aligned 8/64-bit layouts; smaller effects may be
inconclusive. No CPU-cycle evidence on Mac; Linux PMU success remains unvalidated.
Source baseline and A/PARK remain; overnight supervisor stays stopped. A useful
next diagnostic is assembly comparison against the actual mixed-output iterator.
Do not reinterpret this kernel as clearing that guard. Pre-existing round21 drafts
remain local and separate from this task's commits.

The user requested a workspace like hdr-agent-workspace, created in redis-performance,
with an experiment log and both population-based decision steps. They clarified that
only the data structure matters and experiments must use microbenchmarks, not Redis.

Source: PR #15635, immutable head in source-manifest.json. The tree .c/.h files initially
match that commit exactly. compat/ supplies a standalone host; vendor/redis/ is minimal
support. Do not expand scope back to server integration tests or client benchmarks.

Read README.md, docs/POPULATION.md and docs/MICROBENCHMARKS.md. The initial harness covers
eight direct API cases; fixture coverage and qualified performance evidence remain future
work. Local smoke output is not a baseline. No agent populations have been executed.
Unknown token usage is not estimated or fabricated.

EXP-001 subsequently ran locally under explicit user authorisation, using the CPU
Performance Engineering MCP methodology. Read its local-m1-2026-10-17/README.md: 144
processes/984 rows, four profiles, unchanged source. Only 1/41 cells qualified; suite
qualification is parked. Next: a separate referee observability/duration improvement
and requalification, then the two population steps. Workspace acceptance and upstream
publication are separate. Do not repeat these completed runs without a new reason.

The user subsequently requested an all-night experiment loop. See
experiments/OVERNIGHT-2026-10-17/PLAN.md and scratch/overnight-20261017/status.json.
The supervisor has an explicit 07:00 UTC deadline, per-round timeouts, a STOP file,
saved reports/transcripts and idle-sleep prevention. Workers use workspace-write;
never change permissions when git metadata or a network operation is denied.
Evidence and candidate patches may be local drafts until the morning commit/review.

Round 1 in progress: HARNESS-001 records a separate validated referee revision; see
its README and validation logs. No population or source optimisation yet.

Round 1 update: AA-001 complete (192 rows, all checks pass); only iterate16/scan16
qualified. Suite/lookup/rank/update PARK. New scan profile blocked: sample exit255
cannot examine child, no retry/escalation. No profile-backed qualified population
target yet, selection NONE. Git add denied once at index.lock; frozen snapshot and
SHA256/patch recorded in HARNESS-001, no commit/worktree retries.

DIAG-001 complete: 42 processes / 72 windows; process/fixture reuse did not meet
preregistered dispersion criterion (1/6 blocks, required4/6). All invariants stable.
No remedy established; do not repeat identical trial. Next: stronger boundary oracle
validation while source optimisation remains blocked by profile/qualification gates.

## Round1 completed handoff

Canonical report: experiments/OVERNIGHT-2026-10-17/ROUND-001.md. HARNESS-001 frozen and
validated; AA-001192 rows only2/8 qualify, suite PARK; DIAG-00172 windows does not
establish a reuse remedy. Two new boundary suites pass release/debug and ASan/UBSan;
four faults detected. Three scoped Clang execution-count captures succeeded after
sample inspection was denied. Counts are not CPU-time profiles. No candidates or
populations. New large-fixture A/A or stronger active-resize boundaries are concrete
next actions. Do not repeat denied git/sample actions or failed identical schedules.
All source/support pristine; uncommitted referee/evidence drafts await morning review.

Round2 AA-002 complete: 96 rows, rank16 only qualifies; lookup PARK. No rank time
profile or qualified lookup guards; selection NONE. Next natural wide-ID boundary
coverage. See experiments/OVERNIGHT-2026-10-17/AA-002/README.md. No source change.

BOUNDARY-003 complete: natural widening to leaf ID70834 with mixed binary members,
two seeds release/debug+ASan/UBSan pass, two mutation controls detected. No original
source changes. Independent reviewer startup failed; no independent review claimed.

DIAG-002 complete:24 fixed lookup windows, adjacent add-loop bracket diagnostic fails
its preregistered association criterion. No GHz conversion or normalization remedy.
Do not repeat unchanged. Root source and frozen referee still pristine.

BOUNDARY-004 complete: standalone relocating callbacks, exact usable-size deltas and
ownership pass2673 full model checks per release/sanitizer build; four fixtures, two
fault controls detected. Review sequential, source untouched. No performance acceptance.

## Round2 completed handoff

Canonical report: experiments/OVERNIGHT-2026-10-17/ROUND-002.md. AA-00296 rows only
rank16 qualifies, lookup PARK; no rank time profile, so populations not started.
DIAG-00224 windows does not establish adjacent add-loop rates as an explanation or
normalization remedy. BOUNDARY-003/004 pass release/debug and ASan/UBSan; four more
intentional faults detected. Source/referee unchanged. New lookup access-history
coverage or controlled probe/stale-position boundaries are concrete next actions;
do not repeat failed schedules. Frequency/effective QoS/residency unknown. Reviewer
startup failed, sequential reviews only; git/sample denials not retried. All drafts
await morning review. Final campaign round still must write MORNING-REPORT.md.

Round3 DIAG-003 complete:24 fixed access-order windows, repeated-order advantage
criterion not met. See DIAG-003/README.md. No retry, precision remedy or optimisation
claim. Reviewer startup failed before running; sequential review only. Next controlled
probe/tombstone and insertion-position boundary coverage. Root source/referee frozen.

BOUNDARY-005 complete: controlled home-bucket wraparound, tombstones, tag masks and
insertion revisions pass622 checks/build; two faults detected. Initial lookup-distance
precondition failures retained; strengthened final fixture passes without lowering
thresholds. No source bug or optimisation claim. Next precise bulk-delete thresholds.

BOUNDARY-006 complete:48 bulk-delete cases/build and240 model checks pass release
and ASan/UBSan; both planned faults detected. Threshold/active-resize/endpoint/batch
canary coverage added. Six boundary suites now complete, twelve faults detected.
Next DIAG-004 insertion-history diagnostic is preregistered and being prepared.

DIAG-004 complete:48 rows; ascending advantage hypothesis fails, slower in all
primary blocks. Long-key contrast motivates fresh independent-query factorial
diagnostic, because original harness couples insertion and lookup permutation.
No causal mechanism or performance acceptance. Five additional diagnostics complete.

DIAG-005 complete:48 fresh-seed factorial rows support local construction/query-order
interaction; all fixed controls pass. Main harness reuses insertion permutation for
lookup; independent-query coverage is now evidence-backed preparation. Not a noise
remedy, causal cache attribution or source win. Six additional diagnostics complete.

## Round3 completed handoff

Canonical report: experiments/OVERNIGHT-2026-10-17/ROUND-003.md. DIAG-00324 windows
and DIAG-00448 rows fail their original advantage hypotheses. DIAG-00548 fresh-seed
factorial rows support a local construction/query-order interaction: decoupling queries
largely removes construction contrast. This warrants fixture coverage, not a source win
or precision remedy. COUNTERS-002 four captures show identical aggregate tree paths
between query modes within construction arm; no time-profile replacement claimed.
BOUNDARY-005/006 final suites pass both builds, four more faults detected. Initial
BOUNDARY-005 fixture/precondition failures are retained; final >=23 distance check
was strengthened through distinct final-bucket tags, never lowered. Round audit passes.

Totals: one harness revision, three baseline explorations, seven additional diagnostics,
six boundary suites, twelve detected fault controls. Source NONE; lookup PARK; no
optimisation/population. Reviewer startup failed, exact model/backend/cost unknown.
No git/sample denial retry, settings changes, publishing or root source/referee edit.

Next: separate isolated referee fixture revision with independent query seed/order
labels (DIAG-005 prototype), validate/freeze, then preregister targeted A/A. Keep root
baseline for morning review. Do not assume fixture coverage resolves noise. Relevant
time profiles, both population stages, qualified guards, fresh independent confirmation
and adversarial review remain mandatory. Final campaign round writes MORNING-REPORT.md.

Round3 final metadata audit: arm64/macOS26.3/Clang17 confirmed; CPU/core/RAM sysctl
query denied once, preserved in ROUND-003-ENVIRONMENT.json, no retry/escalation.

Round4 HARNESS-002 validated in isolated snapshot, original tests and80 all-case query
fixture cells/build pass release and sanitizers. Root source/referee preserved. AA-003
independent-query qualification preregistered; source NONE. Reviewer startup failed.

Round4 AA-003 complete:96 rows,0/4 qualify; independent queries do not resolve precision.
Lookup PARK/source NONE, no population. Next bounded public in-process profile method
inspection; previous external sample/git denials will not be retried.

Round4 PROFILE-002 succeeds:two known-function calibrations,12 scoped self-process
profiles, all symbols resolved. Public own-process signal APIs; no external sample retry.
Sample counts are descriptive; timer cadence/aliasing/overhead unknown, instrumented
thread time includes post-loop output and is unusable for thread/wall interpretation.
Short lookup memchr, long lookup SipHash, rank matching/traversal observed. Lookup PARK
unchanged; source NONE. Next stronger lexicographic iterator boundary coverage.

Round4 BOUNDARY-007 passes36 lexical fixtures/180 checks/4075200 seeks per build in
release/debug and ASan/UBSan; two faults detected. Seven suites/14 fault controls total.
Root source/referee unchanged. Next append-batch ownership/flush boundaries.

Round4 BOUNDARY-008 passes18 append-batch fixtures/162 checks per build; two faults
detected. Eight suites/16 fault controls total. Root source/referee intact. Next bounded
self-sampler perturbation diagnostic; acceptance/source precision gates stay unchanged.

Round4 DIAG-006 complete:48 sampler off/on rows meet preregistered coarse perturbation
bound. No source precision or unbiased-time-fraction claim; lookup PARK/source NONE.
Nine diagnostics complete. No further measurements this round; audit and handoff next.

## Round4 completed handoff

Canonical report:experiments/OVERNIGHT-2026-10-17/ROUND-004.md. HARNESS-002 separately
validates independent query RNG/order/fingerprints; AA-00396 rows,0/4 qualify. Root
HARNESS-001 and target source unchanged. Lookup PARK/source NONE; no population.
PROFILE-002 succeeds with public own-process timer/context APIs:two known-function
calibrations,12 scoped captures,all symbols resolved. No external inspection retry.
Short-key memchr,long-key SipHash and rank matching/traversal observed. Sample counts
are not exact time fractions. PROFILE-002 thread time includes post-loop dump and must
not be used for CPU/wall share. DIAG-006 moves dump after endpoint and48 off/on rows meet
only a coarse preregistered perturbation bound; its inherited calibration source needs
helper-interface consolidation before reuse. Clock/effective QoS/residency unknown.

BOUNDARY-007/008 add lexical/sentinel/optional-output and append-batch buffer/flush/
resize coverage:both builds pass,four faults detected. Totals:two harness revisions,
four baseline explorations,nine diagnostics,eight boundary suites,16 faults. Optimisation
and population counts remain zero. Agent startup failed; sequential reviews only,
exact backend/model/cost unknown. Full read-only audit and source/whitespace checks pass.
Curation path error retained and corrected; MCP source excerpts remain ignored scratch
with public curated metadata/hashes. No git/sample/sysctl denial retry or publishing.

Next: distinct preregistered finer-window placement/phase diagnostic or new fixture
coverage. Do not rerun failed precision schedules. Keep root baseline until morning
review and use isolated HARNESS-002. Both population stages and all acceptance gates
remain mandatory. Campaign final worker still must write MORNING-REPORT.md.

Round5 DIAG-007 complete:24 processes/384 fine contiguous windows, semantic/memory/
duration/gap controls pass. Only1/4 cells meets early/late phase criterion, required2;
hypothesis unsupported. Source NONE/lookup PARK unchanged;10 additional diagnostics.
Reviewer startup failed before running; sequential reviews only. Root preserved.
Next missing zbtreeScores batch-mask/exact-score boundary coverage.

Round5 BOUNDARY-009 complete:526590 batches/7883000 slots per build, two seeds,
12 complete model checks and28 active-resize batches pass release/debug+ASan/UBSan.
Both intentional mask/score-slot faults detected. Nine suites/18 fault controls.
Next new warmup-operation intervention: DIAG-007 only miss16 exhibited consistent
early/late shift, and its warmup performs hits. Fresh seeds and preregistered contrast
required; this observation does not establish mechanism or qualify comparisons.

Round5 DIAG-008 complete:48 fresh-seed ABBA processes/768 windows; primary short-miss
phase contrast supported, all controls pass. Not source qualification/mechanism proof.
11 diagnostics. Next separate HARNESS-003 miss-only warmup revision and fresh AA-004;
root unchanged. Raw-buffer guard-page boundary work also planned but not yet started.

Round5 HARNESS-003 validates miss-operation warmup/CSV metadata. Both builds pass43
original tests, three referee groups and80 query cells. Third harness revision isolated;
AA-004 fresh96-row qualification preregistered. Root source/referee unchanged.

Round5 AA-004 complete:96 rows,0/4 qualify unchanged precision gate; all controls pass.
Miss-warmup phase remedy is not a precision remedy. Five baseline explorations; source
NONE/lookup PARK; no populations. Next raw-buffer guard-page coverage. Root unchanged.

Round5 BOUNDARY-010 final suite passes both builds:four fixtures,33 lengths,260 guard
mappings,652 raw queries and12 complete model checks/build; overread/truncated-hash
faults detected. Initial missing-string.h compile failure retained; final snapshot only
adds header.10 boundary suites/20 controls. Root unchanged.

Round5 DIAG-009 complete:18 known-function runs pass all calibration controls,
1000/3001us delivery-rate equivalence unsupported. Do not equate requested intervals
with observed rates or infer exact cadence/GHz. Corrected DIAG-006 calibrate stop/dump
interface in new DIAG-009 snapshot; prior snapshots intact.12 diagnostics total.
Source NONE/lookup PARK. No further measurements planned this round; audit/handoff next.

## Round5 completed handoff

Canonical report:experiments/OVERNIGHT-2026-10-17/ROUND-005.md. DIAG-007384 windows
fails overall phase criterion; DIAG-008768 fresh-seed windows supports operation-matched
miss warmup. HARNESS-003 validates this isolated change and warmup_case. AA-00496 fresh
rows still0/4 qualify; lookup PARK/source NONE. No populations/source candidates.

BOUNDARY-009/010 pass release/debug+ASan/UBSan; four additional faults detected. Raw
guard test initial compile failure preserved, final adds string.h only. DIAG-00918
known-function calibrations pass but requested1000/3001us rate-equivalence fails. Corrected
calibration stop/dump interface saved in new snapshot; exact cadence/frequency/profile
fractions remain unknown. All source/referee and prior frozen evidence preserved.

Totals:3 harness revisions,5 baseline explorations,12 additional diagnostics,10 boundary
suites,20 detected fault controls; optimisation/population counts remain zero. Sequential
read-only audit recomputes all decisions and measured fixture fingerprints. Reviewer
startup failed before running; no independent confirmation, exact model/backend/cost
unknown. Protected git/sample/sysctl actions not retried; no runtime/STOP/settings or
network changes. All new drafts await morning commit/source review.

Next distinct preregistered QoS/placement intervention after public API inspection, or
uncovered fixture coverage. No unchanged retry of AA-004/DIAG-007/009. Use HARNESS-003
independent queries/miss warmup; use DIAG-009 corrected calibration driver if profiling.
Both population stages,qualified target/guards,matched profiles,fresh confirmation and
adversarial review remain mandatory. Final worker writes MORNING-REPORT.md by07:00UTC.

Round5 final capability preparation: public requested-QoS setter succeeds in a short-
lived child, inherited user-interactive->user-initiated. AA-004 also reports user-
interactive, so no simple priority-increase remedy is implied. Probe source/commands/
SDK constants/hashes saved in ROUND-005-QOS-PROBE.json. No benchmark or count change.

Round6 DIAG-010 complete:96 requested-QoS rows, all controls pass; primary halving
criterion unsupported. No A/A retry warranted.13 diagnostics; source NONE/lookup PARK.
Reviewer startup failed; sequential review only. Next active-resize clone boundaries.

Round6 BOUNDARY-011 complete:12 clone fixtures/build pass both builds;22 clone audits
and74 model checks,6 active-resize clones. Both faults caught, second driver matcher
failed on earlier accounting assertion; retained/audited without test changes.11 suites/22
faults. Next newly available self-process traversal profiling, previously externally blocked.

Round6 PROFILE-00312 traversal profiles/two calibrations pass; AA-00596 rows qualify
iterate16/320, scans PARK.14 diagnostics/6 baselines. EXP-002 sequential populations
started, isolated source variants only; source baseline preserved. No independent agents.

## Round6 completed handoff

Canonical ROUND-006.md and EXP-002/README.md. DIAG-01096 QoS rows unsupported; BOUNDARY-011
12 clone fixtures/build pass and two faults caught, expected-message driver mismatch
preserved/read-only audited. PROFILE-00312 captures/two calibrations pass; AA-00596 rows
qualifies iterate16/320,scan/lookup/suite PARK. Both population stages now executed as
three separate sequential passes plus chair and three isolated implementations. No
independent agents (startup failure), unknown backend/model/cost.

EXP-002 forward score-only dispatch:control/A/B/C all validation passes;72 fixed screening
rows select C,24 fresh-seed confirmation rows pass,four matched descriptive profiles and
codegen support dispatch/register isolation. Final PARK for unmeasured reverse/output
performance guards,independent confirmation/review and morning committed provenance.
Main src/referee untouched; losing A/B patches retained.6 baselines,14 diagnostics,
11 suites/22 faults,1 sequential population round,0 accepted/0 rejected/1 parked.

Next: new isolated iterator mode fixture covering direction/output masks/score encodings,
validate/freeze/qualify,then retained C/control guard comparisons. No repeat failed QoS/
lookup qualification unchanged. Final worker still writes MORNING-REPORT.md by07:00UTC.

Round7 HARNESS-004 validated:640 iterator mode fixtures/build plus original tests,
three sensitivity faults detected. Separate frozen snapshot;root untouched. AA-006
14-cell fixed A/A preregistered. Reviewer startup failed;EXP-002 PARK unchanged.

Round7 AA-006336 rows complete,10/14 modes qualify. Masks2,3,5,6 PARK. All invariants
pass. EXP-002 guard-extension plan freezes504 comparisons across all3 retained
variants;four unqualified modes diagnostic only. Root source unchanged.

Round7 EXP-002 expanded guard decision:504 discovery+216 fresh rows confirm no-output
regressions for ALL3 candidates on BOTH fresh seeds;B/C full-output also confirms.
REJECT represented implementations,selection NONE,superseding round6 C/PARK. All640
mode fixtures/build and original tests pass control/A/B/C;5144 validation commands.
Eight matched profiles/two calibrations pass;codegen supports added fallback dispatch.
Main baseline/all patches preserved;0accepted/1rejected/0parked;one sequential population.
Four AA-006 modes,lookup/suite remain PARK. Boundary012 mixed mutation/mask checks next.

Round7 BOUNDARY-012 passes control/EXP-002A/B/C release+sanitizers;1032 model checks
and2176436iterator results/build. Two faults detected (first driver matcher failure
retained/audited).12suites/24faults. New EXP-003 separate member-decoder outlining
hypothesis selected by sequential proposals/chair;isolated validation in progress.

Round7 EXP-003 completes second sequential population:member-decoder outlining A/B/C
all pass1064validation commands,504screen+216fresh rows. All3 full-output regressions
confirm on BOTH fresh seeds10103/10111. REJECT/NONE.12matchedprofiles/2calibrations
pass;register saves reduced but helper-call work added. Main source untouched,all
patches kept.0accepted/2rejected/0parked;two sequential populations. Four AA/lookup/suite
modes still PARK. No independent agent,unknown backend/model/cost. Final audit next.

## Round7 completed handoff

Canonical ROUND-007.md. Main source/referee pristine.1776 measured rows plus one
prospectivewarmup and24profile/calibration windows verified serial;all raw/hash/interval/
patch checks PASS. Workspace/pristine-source and git diff --check PASS. EXP-002 and
EXP-003 REJECT/NONE from fresh qualified guard failures. No source accepted;all patches
retained.4harnesses/7baselines/14diagnostics/12boundarysuites/24faults,2sequential
populations,0accepted/2rejected/0parked. Independent reviewer startup failed,unknown
backend/model/cost. Four iterator modes plus lookup/scan/suite remain PARK.

Next concrete work:new preregistered packed-score-width/physical-order/member-record
path coverage diagnostic,using existing baseline profiles to justify any new hypothesis.
Do not repeat failed dispatch/outlining/QoS/lookup schedules unchanged. Final worker
still writes MORNING-REPORT.md by07:00UTC. No git/permission/runtime/STOP/publishing edits.

Round8 COUNTERS-003 complete:320 child executions pass structural oracles. Original
post-run equality assertion retained;only native/ASan owned bytes differ. Narrow-width
coverage supported;64-bit/cross-word coverage remains essential.15diagnostics/source
NONE. Reviewer startup failed;next exhaustive decoder boundary oracle.

Round8 BOUNDARY-013 complete:2572800exact-bit checks/build and two faults detected.
13suites/26faults. EXP-004 three sequential proposals/chair and isolated predicate
implementations;all1080validation commands pass. AA-007 current-round baseline next.

Round8 AA-007240rows complete,6/10qualify including primary;four newly PARK.
Eighth baseline. EXP-004504row screening next;all broader unqualified guards block ACCEPT.

Round8 EXP-004 provisional A/PARK:both sequential populations,1080validation commands,
504screen+216fresh rows,12profiles/2calibrations. Main baseline unchanged.3populations,
0accepted/2rejected/1parked. AA-008 new5x-duration score+length guard diagnostic next.

Round8 AA-00896rows complete,2/4qualify;onlyone mask6seed passes,long guard comparison
skipped per plan. Ninth baseline. EXP-004 stays A/PARK;longer duration not a cure.

Round8 DIAG-011144rows complete,criterion unsupported in one seed.8profiles/2calibrations
pass;Clang already unswitches dynamic mask6 tests,so per-item-test premise incorrect.
384fixture checks+4builds pass;pre-timing arithmetic erratum retained.16diagnostics;
EXP-004 A/PARK unchanged. Final audit/report next;no new timing trial.

## Round 8 completed handoff

Canonical report: experiments/OVERNIGHT-2026-10-17/ROUND-008.md. EXP-004 is A/PARK:
three sequential proposals/chair and isolated predicate variants; 1,080 validation
commands pass. AA-007 qualifies6/10;504screen+216fresh rows preserve A preference.
AA-008 qualifies only one longer mask6 fixture,so comparison skipped per plan.
DIAG-011 fails the two-seed interaction criterion;codegen already unswitches dynamic
mask6 tests. Do not replace the referee or repeat that premise. All losing patches kept.

COUNTERS-003320child runs pass;post-run native/ASan allocation equality failure retained
and audited. BOUNDARY-013 passes2,572,800exact-bit results/build,two faults detected.
DIAG-011384fixture processes+4builds pass;pre-timing count erratum retained.
Round audit:1,200measured rows+2warmups+20profiles+4calibrations,1,226serial windows;
86effect intervals recomputed from raw rows. Workspace/pristine-source/diff checks pass.
Totals4harnesses/9baselines/16diagnostics/13boundarysuites/26faults;3sequential
populations,0accepted/2rejected/1parked. Root unchanged. No independent reviewer:
startup failed,backend/model/cost unknown,supervisor usage separate.

Next inspect real caller/iterator codegen,then a distinct preregistered code-placement
diagnostic or physical-order/signed-zero fixture coverage. No unchanged20m/100m mask6
retry,failed lookup/QoS retry,or adoption without broader guards/independent review/
committed provenance. Final worker still writes MORNING-REPORT.md before07:00UTC.
No git retry,publishing,permission/runtime/STOP changes or active benchmark child.

Round9 BOUNDARY-014 passes control/EXP-004A/B/C bothbuilds:22,080modelchecks and
46,005,384exact results each;twofaultsdetected.14suites/28faults. First memory
precondition failure retained;rehash explicitly settled before unchanged equality guard.
DIAG-012 placement preparation next;root/retained sources unchanged.

Round9 DIAG-012complete:480rows+4warmups;bothplaceboA/Acontrols pass,16-byteplacement
criterion unsupported.1028validationruns/fullcodegen pass.17diagnostics;EXP-004PARK.
Next distinct mask-arithmetic hypothesis;root source unchanged.

Round9 AA-00972rowsqualify3/3masks0/4/7.10baselines. EXP-005three sequential proposals/
chair and threeisolatedmaskimplementations pass1096validationcommands.180screen rows next;
rootbaseline unchanged,allotherguardqualificationstillpending.

Round9 EXP-005PARK/NONE:fourthsequentialpopulation,1096validationcommands pass,180screen
+216freshrows. Cscreenpreference failsfreshprimarybound;12profiles/2calibrations pass.
A/C hotinstructionsmatch modulo panicliteralrelocations;no intrinsicC superiority.
0accepted/2rejected/2parked;rootbaselineunchanged. Finalaudit/handoffnext.

## Round 9 completed handoff

Canonical [ROUND-009](../experiments/OVERNIGHT-2026-10-17/ROUND-009.md). BOUNDARY-014
passes control/EXP-004 A/B/C in both builds: 22,080 models and 46,005,384 exact-score
results each; two faults detected. First rehash memory-precondition failure retained.
DIAG-012 controlled placement: 480 rows + four warmups; primary criterion unsupported,
both placebo controls qualify. Full code isolation and 1,028 validation runs pass.
EXP-005 completes fourth sequential population; 1,096 validation commands pass; AA-009
72 rows qualifies 0/4/7. Screening 180 rows prefers C, but 216 fresh rows fail primary
bound: PARK/NONE. Twelve profiles/two calibrations pass. A/C iterator instructions match
modulo panic relocations; do not infer C superiority or pool observations.

Totals: 4 harnesses / 10 baselines / 17 diagnostics / 14 boundary suites / 28 faults;
4 sequential populations; 0 accepted / 2 rejected / 2 parked. Main baseline preserved.
Audit verifies 967 serial windows and 76 raw-derived intervals. Independent reviewer
startup failed; backend/model/cost unknown. No publishing, git retry or runtime edits.
Next: new monotonic-construction/alternating-zero iterator fixture with separate
validation/freezing/qualification; cannot replace original guard. Avoid unchanged failed
mask6/duration/QoS/caller/placement retries. Final worker owes MORNING-REPORT.md by07:00UTC.

Round10 HARNESS-005 validated1,408fixturecells/build,3faults; COUNTERS-00496children
pass. Large descending trees have only64reversedmembers; cannot claim broad physical
reverse throughput.5harnesses/18diagnostics. AA-010 preregistered next; root preserved.

Round10 AA-010384rows complete;14/16cellseeds qualify,sixjointcells.11baselines.
EXP-004 ordered-guards fixedscreen/fresh/profile plan saved;validationinprogress.
Originalguard remainsPARK and mainbaselineuntouched.

Round10 EXP-004 ordered-guards complete:1,194validationcommands;864rows+4warmups;
12profiles/2calibrations. All3passall6freshguards bothseeds;A/PARK unchanged,original
integer mixed-output guard unresolved. No newpopulation/sourceadoption. Next compact
deletion-induced reversed-leaf coverage specimen;largefixtures hadonly64reverseditems.

Round10 COUNTERS-005672children pass:public-API adjacent-sentinel minimumdeletion
yieldsfullyreversed singleleaf n1..95,clone/refill included;2diagnosticfaults detected.
19diagnostics;no timingclaim. Next separateharnessrevision/profile/qualification for
this smallfixture;do not time source-included census as equivalent harness. Auditnext.

Round10 BOUNDARY-014 compact extension: all8semanticruns pass 1,940fixtures and
86,570,560 exactresults/build. Bothfaultsdetected. Crossbuildaggregatephysicalcounters
differ; originalpostrunassertion retained,read-only audit/no rerun. Counts unchanged.

## Round 10 completed handoff

Canonical [ROUND-010](../experiments/OVERNIGHT-2026-10-17/ROUND-010.md). HARNESS-005
validates1,408fixtures/build plus originaltests and3faults. AA-010384rows qualifies6/8
cells onbothseeds;2integerforwardcells PARK. EXP-004 ordered extension passes1,194
validationcommands,864comparisonrows,12profiles/2calibrations;all3passall6freshguards.
A/PARK unchanged;originalguard unresolved. No newpopulation or sourceadoption.

COUNTERS-00496runs show only64reversedmembers inlargefixtures. COUNTERS-005672runs
establish a fullyreversed singleleaf recipe via adjacent finite sentinel andminimum
deletion,includingclones/refill. Two diagnosticfaults detected;earlierassertion corrected
byread-only audit/no rerun. Physical widths can differ by history.

BOUNDARY-014 compact extension:all8semanticruns pass1,940fixtures,289,060modelchecks,
86,570,560exactresults each;bothretainedfaults detected. Crossbuildwholeoutputequality
FAILS only onaggregatephysicalcounters;per-fixturelines/semanticcounts match. No rerun,
no oracle weakened. Causeunknown;allocator/compiler/ASan confounded. Unusedrenamedmain
warning retained. Originalfailedmanifest status running means stoppeddriver,not activechild.

Totals5harnesses/11baselines/19diagnostics/14suites/28distinctboundaryfaults;4sequential
populations;0accepted/2rejected/2parked. Audit1267serialwindows and176raw-derivedintervals
passes;mainbaseline preserved. Exactbackend/model/costunknown;reviewerstartupfailed.
No publication,gitretry orruntimeedits. Nextnewreferee/profile/qualification forcompact
history,orpreregisterallocator/buildfactorial forfailedphysicalprediction. Finalworker
stillowes MORNING-REPORT.md by07:00UTC. Do notpoolold/newchecksum timings orretryfailed
mask6/duration/QoS/caller/placement schedules unchanged.

Round11 COUNTERS-006 complete:12 unit+12 semantic cells pass,1940fixtures/cell.
Fixed capacity removes build-dependent physical differences; capacity policy changes
orientation counts.20diagnostics;source NONE. HARNESS-006 compact-history preparation
and validation in progress;root source/referee untouched. Reviewer startup failed.

Round11 HARNESS-006 validated2,560fixturecells/build plusoriginaltests,invalidchecks
and3faults.6harnesses/20diagnostics;compactprofiles andAA-011 next. Mainbaseline preserved.

Round11 AA-011384rowscomplete,oneofeightcellsjointqualifies. Analysisstale200traversal
literal correctedto preregisteredceil(20m/95);originaloutputsretained,no rerun.12baselines.
EXP-004compactguard extension preregistered;allotherguardsPARK. Rootbaselinepreserved.

Round11 EXP-004compactguardcomplete:1770validationcommands,144rows+4warmups,12profiles/
2calibrations. A/B passnewguardbothfreshseeds;C inconclusiveonone. A/PARK unchanged.
Next DIAG-013 preregisteredcompact-warmupintervention;rootpreserved.

Round11 DIAG-013192rows+1warmupcomplete;allinvariants pass butlongwarmupremedy
criterionunsupported(only1/4qualifies).21diagnostics. No rerun/policyadoption.
FreshseedCOUNTERS-006source/allocator confirmationpreregisterednext.

## Round 11 completed handoff

Canonical [ROUND-011](../experiments/OVERNIGHT-2026-10-17/ROUND-011.md). Main baseline
preserved; source NONE, EXP-004 A/PARK, EXP-005 PARK/NONE. No new population.
COUNTERS-006 fixed-capacity factorial supports allocator-sensitive physical history;
12unit+12semantic cells,6selected traces and16fresh-source cells pass. Fresh cells each
check1,980fixtures/325,860models/163,246,200exactresults; all outputs match per policy.
Controlled adapters remain diagnostic and cannot replace allocator/memory guards.
HARNESS-006 passes2,560fixtures/build,originaltests/invalidinputs/3faults. AA-011384rows
qualifies onlyzero-trim-f4 jointly. Stale200traversal analyser retained; corrected analysis
uses preregisteredceil(20m/95),no child rerun. Use *-corrected.json eligibility/summary.
EXP-004 compact extension passes1,770validationcommands,144comparisonrows+4warmups;
A/B passnewguardbothfreshseeds,C inconclusiveonone.20profiles/4calibrations pass, including
exactmask. Baseline adds6profiles/2calibrations. DIAG-013192rows+warmup:longerwarmup
remedyunsupported;only1/4longintervalqualifies. No policy or sourceadoption.
Audit758serialwindows/72raw-derivedintervals passes;7,017timestamped build/test commands
disjoint. Workspace/pristine-source/diff checks pass. All old evidence/losing patches kept.
Totals6harnesses/12baselines/21diagnostics/14suites/28boundaryfaulttypes;4sequential
populations,0accepted/2rejected/2parked. Backend/model/costunknown; reviewerstartupfailed.
Next controlled-capacity mixed-finite-score mutation boundary oracle, or distinctcompact
process/block-position diagnostic. Avoid unchangedfailedwarmup/QoS/duration/caller trials;
no poolingharnessversions or replacingoriginalmask6guard. No gitretry/publishing/runtime/
STOP/permission edits. Finalworker still writes MORNING-REPORT.md before07:00UTC.

## Round 12 completed handoff

Canonical [ROUND-012](../experiments/OVERNIGHT-2026-10-17/ROUND-012.md). Main source,
header, root referee and adapter retain their hashes. Source NONE; EXP-004 A/PARK,
EXP-005 PARK/NONE. No new population, baseline, harness or candidate adoption.

BOUNDARY-015 passes 24 capacity/source/build cells, each with 96 fixtures, 2,751 model
states and 2,721,586 exact-score comparisons, plus all 43 original tests. Controlled
policies yield identical complete output; logical digests agree everywhere. Initial
invalid SCAN uniqueness assertion and failed snapshot retained. Corrected new oracle
permits documented duplicate callbacks while checking exact values and completeness.
Both new finite-bit/numeric-update faults are detected; existing checks unchanged.

BOUNDARY-016 passes all eight baseline/A/B/C native/sanitizer cells with 146,250 packed
insert/delete operations each. Whole-buffer digests match; overlap-direction and tail
faults detected. Private integer streams do not introduce NaN score API inputs.

DIAG-014 discovery and fresh mirrored confirmation each complete 192 rows plus warmup.
Selected zero-trim-f6 contrast reproduces on both fresh seeds, but one placebo interval
fails precision: joint robustness PARK. DIAG-015 adds 288 rows plus warmup; fixed idle-gap
attenuation criterion unsupported. No timing policy adopted or original guard repaired.

Audit PASS: 672 rows plus three warmups =675 serial measurement windows, disjoint from
122 build/test/fault windows; all 32 wall/thread intervals recomputed from raw data.
Source hashes, fixed schedules and workspace/pristine-source/diff checks pass. All raw
rows/failures/patches retained. No child active, publishing, git retry or runtime/STOP/
permission edits. Exact backend/model/cost unknown; independent reviewer startup failed.
Confirmation and adversarial review are sequential. Frequency/effective QoS/migration
and committed provenance remain unresolved. The method record corrects an extra flag
in the checker prompt; actual timing command/binary was never changed.

Totals: six harnesses, twelve baselines, twenty-three diagnostics, sixteen boundary
suites /32 distinct boundary fault types; four sequential populations; zero accepted,
two rejected, two parked optimizations. Next: new preregistered coordinator-bookkeeping
placebo (buffer after block vs current per-pair serialization, directly measured parent
CPU/launch gaps), or separately qualified runner. It is untested, not a remedy. Avoid
unchanged failed warmup/gap/duration/QoS/caller/placement schedules; no pooling harness
versions or replacing original unresolved guards. Final worker still owes MORNING-REPORT.md
before07:00UTC /08:00Europe/Lisbon. Main source stays baseline for morning review.

Round13 DIAG-016 completes384rows+warmup. Coordinator CPU manipulation succeeds;
attenuation criterion unsupported.24diagnostics;source NONE/existingPARK unchanged.
Next inspect child-wait implementation or extend compact-index boundary coverage.

Round13 DIAG-017 completes384rows+warmup and4transportcontrols. Fixedcriterion
unsupported;pipecontrast/placeboprecision insufficient.25diagnostics,sourceNONE.
No unchangedretry. Compactindex/leafID primitiveboundarycoverage next.

Round13 BOUNDARY-017/018 pass8source/buildcells each and4faultcontrols.18suites/
36distinctfaulttypes. Registryinitialcompilefailure retained,only API namefixed.
Mainbaselinepreserved. DIAG-016/017 unsupported;25diagnostics.

Round13 DIAG-018 completes48discovery+48freshmirroredrows+2warmups. Observed
completiondelay supportedlocally;6transport/status/timeoutcontrolspass. No precision
remedy or sourceguardreplacement.26diagnostics;sourceNONE/existingPARK unchanged.
No moretimingthisround;read-onlyaudit/report/handoff next.

## Round 13 completed handoff

Canonical [ROUND-013](../experiments/OVERNIGHT-2026-10-17/ROUND-013.md). Main source,
header, root referee, adapter and original tests retain their hashes. Source NONE;
EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. No new population, baseline, harness
or source adoption.

BOUNDARY-017 passes all eight source/build cells: 1,048,624 ID stores, 4,096 tag
stores and 524,288 mask patterns each. BOUNDARY-018 passes all eight cells: 38 fixtures,
1,458,668 registrations/releases, 81,310 replacements and 602 full registry audits
per cell. All logical digests agree. Four new deliberate faults detected. Initial
registry compile failure retained; only allocator API name corrected, no checks weakened.

DIAG-016/017 each complete 384 rows plus warmup; fixed precision-remedy criteria fail.
Coordinator CPU manipulation succeeds; pipe transport attenuates contrast descriptively,
but placebo precision remains insufficient. No policies adopted or original guards repaired.
DIAG-018 adds 48 discovery + 48 fresh reversed-order rows and two warmups, supporting
only observer-to-Python-return wall delay locally. Six transport/status/timeout controls
pass. Wrapper changes launch conditions; no exact kernel-exit or frequency claim.
Benchmark A/A precision remains mixed; no normalization or source-guard substitution.

Audit PASS: 868 serial measurement windows disjoint from 52 validation windows;
52 raw-derived intervals recomputed. Source/snapshot/raw hashes, schedules, journals,
workspace/pristine-source and diff checks pass. All failures, raw rows and patches
retained. No active child, publishing, protected git retry, runtime/STOP or permission
edits. Backend/model/cost unknown; independent reviewer startup failed. Confirmation
and review are sequential, not independent agents. Frequency/effective QoS/migration,
independent review and committed provenance remain unresolved.

Totals: six harnesses, twelve baselines, twenty-six diagnostics, eighteen boundary
suites / 36 distinct boundary fault types; four sequential populations; zero accepted,
two rejected, two parked optimizations. Next: preregister public-API leaf retirement/
allocation during active member resize and subsequent deferred-ID reuse, with an
independent sorted-vector oracle and observed coverage. Synthetic registry tests do
not establish reachability. Performance needs a separately qualified runner or a
new method; do not repeat failed bookkeeping/transport/placebo schedules unchanged.
Keep main baseline for morning review. Final worker still writes MORNING-REPORT.md
before 07:00 UTC / 08:00 Europe/Lisbon.

Next-fixture details: [source notes](../experiments/OVERNIGHT-2026-10-17/ROUND-013-NEXT-FIXTURE.md).
Lookup/rank verification itself advances rehash; capture deferred-ID coverage before
full lookup checks. Small rank deletion may retain the active window; recipe untested.

Round14 BOUNDARY-019 passes8source/buildcells,4fixtures/32modelchecks each; two
faultcontrols detected, one newdistincttype.19suites/37faulttypes. Initial invalid
stale-cursor assumption retained; actual public removal repairs cursor. No source
adoption or timingclaim. BOUNDARY-020 active-resize relocation preregistered next.

Round14 BOUNDARY-020 passes8source/buildcells,4fixtures/32modelchecks each; actual
retired-defrag-cursor restart during active resize, exact allocation visits and
accounting pass. Bothnewfaults detected.20suites/39distinctfaulttypes. Original43tests
pass all8unchangedsource/buildcells. SourceNONE/existingPARK unchanged.

Round14 fresh mutation extension passes8cells/8fixtures/448checks each, bothfaults
detected; failedfirstcoverage retained. COUNTERS-007 three whole-oracle captures
confirm member-cursor repair and defrag recovery, no member-NULL/freecursor path.
27diagnostics;20suites/39faulttypes. SourceNONE/PARK unchanged; no speedclaims.

Round14 shrinkingextension passes8cells and neworientationfault; separatecensus
observes8EOFcursorfallbacks, freed-IDbranch stillzero. BOUNDARY-021 baseline native/
sanitizer pass131080naturalresizes/2wraps each; zero-generationfault detected.
21suites/41distinctfaulttypes;27diagnostics. SourceNONE/PARK unchanged. No more
experimental runs planned; read-only audit and handoff next.

## Round 14 completed handoff

Canonical [ROUND-014](../experiments/OVERNIGHT-2026-10-17/ROUND-014.md).
Main source, header, root referee, adapter and original tests retain their hashes.
Source NONE; EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. No timing benchmark,
new harness, baseline qualification or population ran.

BOUNDARY-019 public lifecycle and BOUNDARY-020 active-resize relocation pass all
eight source/build cells, four fixtures and 32 model checks each. The fresh mutation
extension passes eight cells with eight fixtures and 448 model checks each. The
shrinking extension passes eight cells with four fixtures and 88 model checks each,
including EOF cursor and later ID reuse. BOUNDARY-021 baseline native/sanitizer each
pass 131,080 natural resizes, two generation wraps and 274 model checks. Variants
and full high-water model verification are not claimed for the wrap test.

Eight deliberate fault runs detect five new distinct types and three repeats. Two
initial fixture coverage failures and a fault-generator preflight failure remain.
No existing check was weakened. Four COUNTERS-007 captures distinguish repaired
member cursors, retired defrag recovery and EOF fallback; the freed-member-cursor
branch remains unobserved. These are execution counts, not time profiles. Use mapped
branch files; initial snippets mishandled macro file IDs. Mutation FIXTURE field
`final` means quiescent allocations, not cardinality.

Audit PASS: 2,863 hashes, 120 serial command windows, four captures, raw branches
recomputed, and original 43 tests in all eight source/build cells. Workspace,
pristine-source and diff checks pass. All prior immutable evidence remains.

Totals: 6 harnesses / 12 baselines / 27 diagnostics / 21 boundary suites / 41 distinct
fault types; 4 sequential populations; 0 accepted / 2 rejected / 2 parked.
Reviewer startup failed; confirmation and review are sequential. Exact backend,
model and cost are unknown. No active child, publishing, git retry, runtime/STOP
or permission edits. Frequency, effective QoS, migration, independent review and
committed provenance remain unresolved. Final worker owes MORNING-REPORT.md by
07:00 UTC / 08:00 Lisbon.

Next: [growth-side wrap recipe](../experiments/OVERNIGHT-2026-10-17/ROUND-014-NEXT-FIXTURE.md).
Public Reserve(29) plus shrink-first cycles may reverse generation parity. Require
observed growth wrap/new-leaf coverage and full models at high and low water.
This recipe is untested. Preserve source baseline and avoid unchanged failed timing
protocols.

Round15 growth-side wrap extension passes8cells,131094models and12126950exactresults each. Zero-generation fault caught; singleton batch migration fault SURVIVES. Multi-member extension next; counts21suites/41faulttypes unchanged, sourceNONE/PARK unchanged.

Round15 multi-member wrap extension passes8cells/4fixtures,262188models and24254190exactresults each. Both faults detected, including previously surviving batch-migration fault. Initial12member coverage failure retained; new13member plan passes. Counts21suites/42faulttypes/27diagnostics; scan-interval BOUNDARY-022 in progress.

Round15 BOUNDARY-022 passes8cells,20models/684SCAN calls each including128growth/128shrink active calls; bothfaultsdetected. Counts22suites/44faulttypes/27diagnostics. COUNTERS-008 separate reachability captures next; no timings/sourceadoption.

Round15 COUNTERS-0083captures PASS; actual natural-wrap skipzero and colliding-SCAN paths confirmed.28diagnostics/22suites/44faulttypes; sourceNONE/PARK unchanged. Same-sized cleanup interval extension next.

Round15 cleanup extension passes8cells/10models/432SCAN calls each, active64→64resize/clone/stale-position coverage. New fault detected; invalid initial revision precondition retained.22suites/45faulttypes/28diagnostics. Fresh-seed debug-enabled/disabled validation next, no sourceadoption.

## Round 15 completed handoff

Canonical [ROUND-015](../experiments/OVERNIGHT-2026-10-17/ROUND-015.md). Main source,
header, root referee, adapter and original tests retain their hashes. Source NONE;
EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. No timing benchmark, harness, baseline
qualification or population ran.

BOUNDARY-021 growth wrap passes8cells:131094full low/high models,2natural growth wraps
per cell. Multi-member extension passes8cells:262188models,4wraps; actual new generation1
leaves observed. BOUNDARY-022 colliding SCAN passes8cells/684calls each, including128active
growth and128active shrink calls. Same-size cleanup extension passes8cells/432calls each,
with56/256destination members,5uncopied leaves, active cloning and stale-position fallback.
Fresh-seed confirmation passes48cells across all3final oracles/control+A+B+C/native+ASan/
debug-on+off; logical digests agree. Every oracle/unconditional assertion remains active.

Seven fault runs:6detections,1retained singleton-batch survival. Multi-member coverage
catches the previously surviving fault. Four new distinct fault types; two zero-generation
repeats. Initial12member multi-leaf and revision-change precondition failures are retained.
No production bug or weakening of existing checks. COUNTERS-0083whole-oracle captures
confirm actual skip-zero/batch and colliding/displaced SCAN paths; these are not timeprofiles.

Audit PASS:1512hash checks,190serial command windows,16new patch reconstructions and raw
branch mappings. Separate audit checks256frozen files and all12optimization patches.
Workspace/pristine-source/diff checks pass; original43tests not rerun, round14 evidence kept.
All children finished. No publishing, git retry, credentials, runtime/STOP or permission edits.

Totals6harnesses/12baselines/28diagnostics/22boundary suites/45distinct fault types;
4sequential populations,0accepted/2rejected/2parked. Reviewer startup failed; confirmation
and review are sequential, not independent agents. Exact backend/model/token cost unknown;
supervisor records usage separately. Frequency/effective QoS/migration, independent review
and committed provenance remain unresolved. Root baseline stays for morning review.

Next [live-cursor natural-widening recipe](../experiments/OVERNIGHT-2026-10-17/ROUND-015-NEXT-FIXTURE.md)
is preparation only. Preregister public construction near observed widening, preserve all
continuous anchors and verify cursor interval/termination while ID width changes. Do not
hardcode prior member counts as portable geometry. Performance needs distinct qualification;
no unchanged failed timing retries. Final worker owes MORNING-REPORT.md by07:00UTC/08:00Lisbon.

Round16 BOUNDARY-023 passes16cells: live cursor spans actual narrow→wide migration,
2047mixed-width calls/cell; exact intervals/anchors/models/memory pass. Bothfaults
detected; initial width-fault classifier mismatch retained/read-only audited.23suites/
46faulttypes/28diagnostics. SourceNONE/PARK unchanged. Mixed-width relocation extension next.

Round16 relocationextension48cells PASS, bothfaults detected (one new). COUNTERS-009
fourcaptures PASS; actual mixed-width/clone/relocation branches, no timings.23suites/
47faulttypes/29diagnostics; sourceNONE/PARK unchanged. External-member extension running.

Round16 external-member extension48cells PASS: actual mixed-width clone/relocation with
3088external buffers, exact ownership/interval/anchor/accounting checks.23suites/47faulttypes/
29diagnostics unchanged; sourceNONE/PARK unchanged. Narrowing/renumbering extension next.

Round16 live narrowingextension16cells PASS,4096continuous anchors survive bulk
renumbering/narrowing, newfault detected. Externalfault detected(repeat). Initialcompile
error retained,cast-only attempt002.23suites/48faulttypes/29diagnostics; sourceNONE/PARK.
Freshseed debug-disabled64cell confirmation running; no new semantic trial planned.

## Round 16 completed handoff

Canonical [ROUND-016](../experiments/OVERNIGHT-2026-10-17/ROUND-016.md). Main source,
header, root referee, adapter and original tests retain their hashes. Source NONE;
EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. No timing benchmark, new harness,
baseline qualification or population ran.

BOUNDARY-023 passes 16 cells carrying one live cursor across natural narrow→wide
migration. Clone/relocation and external-ownership extensions each pass 48 cells;
narrowing/renumbering passes 16. Fresh-seed debug-disabled confirmation passes 64 more:
192 semantic source/build/seed/mode cells total. Every callback checks exact current
bytes/length/score; independent per-call hash intervals, continuous anchors and bounded
termination pass. Full lookup/ordered models, sampled ranks, ownership and exact usable
bytes pass. Natural narrowing retains 4,096 anchors while compacting survivor IDs.

Six deliberate faults are detected, three new distinct types. Initial width-fault
classifier mismatch was a real production abort, audited without rerun. Initial
narrowing compile failed on void* typing; a cast-only correction is separately frozen.
Initial workspace link audit ran before the report existed; its failure is retained.
No test was weakened. ASan symbolizer warnings in fault logs remain; no escalation.

COUNTERS-009 completes six whole-oracle captures: actual mixed width, active clone/
relocation, external accept/decline and dense renumber/rebuild. These are execution
counts, not hotness or CPU time. Audit PASS: 1,719 hashes, 277 serial command windows,
11 new patch reconstructions and raw branch mappings. Separate audit checks 256 frozen
files and all 12 optimization patches. Workspace/pristine-source/diff checks pass.
Original 43 tests were not rerun; unchanged round14 evidence remains. All children done.

Totals: 6 harnesses / 12 baselines / 29 diagnostics / 23 boundary suites / 48 distinct
fault types; 4 sequential populations; 0 accepted / 2 rejected / 2 parked. Reviewer
startup failed; confirmation/review are sequential. Exact backend/model/token cost
unknown; supervisor records usage separately. Frequency/effective QoS/migration,
qualified guards, independent review and committed provenance remain unresolved.
No publication, git retry, credentials, supervisor/runtime/STOP or permission changes.

Next: [score moves during actual mixed-width migration](../experiments/OVERNIGHT-2026-10-17/ROUND-016-NEXT-FIXTURE.md).
This is preparation only; preregister and use a true sorted current-score model before
running. No unchanged failed timing retries or substitution for the original guard.
Keep main baseline until separate morning review. Final worker still owes
MORNING-REPORT.md by 07:00 UTC / 08:00 Europe/Lisbon.

Round17 BOUNDARY-024 passes16cells:258cross-leaf score moves/2signed-zero updates each,
both cross-ownership directions, live cursor/current-score models and exact memory.
Both new faults detected;24suites/50faulttypes/29diagnostics. SourceNONE/PARK unchanged.
External-member score-transfer extension next; root source preserved.

Round17 external score extension passes16cells,260external pointer-preservation checks
each (259detach/reinsert,1in-place in census), exact ownership/SCAN/models/memory. New
omitted-detach fault detected. COUNTERS-010 two captures PASS actual update/index-move
branches, no timingclaim.24suites/51faulttypes/30diagnostics; sourceNONE/PARK unchanged.
Finite-extreme/equal-score extension running with separate frozen oracle.

Round17 finite-ties extension passes16cells/288range checks each, but equal-neighbor
fault SURVIVES. Preserved honestly; no new fault count. New preregistered adjacent
255/256and511/512score ties target actual in-place rejection; original oracle frozen.
Counts24suites/51faulttypes/30diagnostics, sourceNONE/PARK unchanged.

Round17 adjacent-tie extension passes16cells/336range checks each; added score updates
force same-leaf key reordering. Previously surviving equal-neighbor fault now detected;
original survivor preserved.24suites/52faulttypes/30diagnostics; sourceNONE/PARK unchanged.
Fixed64cell fresh-seed debug-disabled confirmation in progress.

Round17 batch promotion initial8+8cells pass actual schedule and detect stale-table
cache UAF; retained scope mismatch omitted ID1 batch lane. One-expression corrected
attempt002 discovery8cells passes and repeats detection; fresh8cells completing.
No new suite;24suites/53distinctfaulttypes/30diagnostics; sourceNONE/PARK unchanged.
No further experimental trial this round; curation, audit and handoff next.

## Round 17 completed handoff

Canonical [ROUND-017](../experiments/OVERNIGHT-2026-10-17/ROUND-017.md). Main source,
header, root referee, adapter and original tests retain their hashes. Source NONE;
EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. No timing benchmark, new harness,
baseline qualification or population ran.

BOUNDARY-024 and extensions record160passing semantic cells:144final-scope cells,
including72fresh confirmation, plus16retained initial batch cells with an ID1 lane
coverage gap. Six sorted current-score models per cell preserve exact bits, binary
order, live SCAN intervals/continuous anchors, external ownership and usable bytes.
Finite/neighbor fixtures check288/336range counts. Actual copied/uncopied score moves
and promotion inside a16-lane zbtreeScores call are observed. Corrected batch recipe
changes one expression only; all checks/seeds/bounds preserved.

Seven deliberate-fault runs:6detections,1retained equal-neighbor survival,5new types.
Stronger neighbor fixture detects the survivor; final batch fixture repeats stale-cache
ASan UAF detection. Four whole-oracle captures confirm actual update/index/lexical
branches; they are execution counts, not CPU-time profiles. Symbolizer warnings remain.

Audit PASS:2268hashes,286serial command windows,15new patch reconstructions and4raw
branch mappings. Separate audit checks256frozen files/all12optimization patches.
Two verifier errors about prior manifest sealing/serialization are retained and fully
corrected without experimental reruns. Workspace/pristine-source/diff pass. Original
43tests not rerun; unchanged round14 evidence retained. All children finished.

Totals6harnesses/12baselines/30diagnostics/24boundary suites/53distinctfaulttypes;
4sequential populations,0accepted/2rejected/2parked. Reviewer startup failed; reviews
and confirmation are sequential. Exact backend/model/token cost unknown; supervisor
records usage separately. Frequency/effective QoS/migration, qualified guards,
independent review and committed provenance remain unresolved. No publication, git
retry, credentials, supervisor/runtime/STOP or permission changes.

Next: [smaller/all-miss batch promotion](../experiments/OVERNIGHT-2026-10-17/ROUND-017-NEXT-FIXTURE.md),
preparation only. No unchanged failed timing retries or guard substitution. Keep main
baseline for morning review. Final worker still owes MORNING-REPORT.md by07:00UTC /
08:00Europe/Lisbon; this was not the final round.

Round18 BOUNDARY-025 discovery passes8cells,18partial/all-miss promotion clones each,25models and21,864,700exact iterator/member results.25suites/53distinctfaulttypes/30diagnostics; sourceNONE/priorPARK unchanged. Freshconfirmation and sensitivity controls pending.

Round18 BOUNDARY-025 fresh8cells pass; all3promotion-specific faults detected,1new output-overrun type.16semantic cells total,25suites/54faulttypes/30diagnostics. Prior audit checks702unchanged files. SourceNONE/priorPARK unchanged. HARNESS-007 validation running.

Round18 HARNESS-007attempt002 passes1,080fixture cells,14invalid inputs and3reporting faults. Initial zero-tick/fabricated-rate failure retained, separate reporting correction frozen.7harnesses/12baselines/30diagnostics/25boundary suites/54faulttypes. SourceNONE/priorPARK unchanged. AA-012 fixed240row batch qualification starts next.

Round18 AA-012240rows+warmup complete: long-hit320/b16 and mixed16/b16 jointlyqualify; primaryhit16/b16,hit16/b1,miss16/b16 PARK. All invariants pass; no sourcecomparison yet.7harnesses/13baselines/30diagnostics/25suites/54faulttypes. SourceNONE/priorPARK unchanged. Scoped profiles of qualified subsets next.

Round18 PROFILE-004 two calibrations/eight scoped captures pass;31diagnostics. EXP-006 proposalA selected by three sequential passes/chair; three isolated inline-tag implementations frozen. Original/raw/tag/batch validation in progress. No independent agents, exactbackend/model/costunknown. SourceNONE; priorPARK unchanged.

Round18 EXP-006 completes fifth sequential two-stage population. All4sources pass43tests/raw/tag/batch bothbuilds;360screen+96freshrows retained. Cfreshprimary passesbothseeds; longguard firstseedfailsuncertainty bound; singlelane screeningregression concerning. C/PARK,sourceNONE;0accepted/2rejected/3parked.16matchedprofiles/4calibrations pass; allpatches/rootbaseline preserved.7harnesses/13baselines/31diagnostics/25suites/54boundaryfaulttypes.

## Round 18 completed handoff

Canonical [ROUND-018](../experiments/OVERNIGHT-2026-10-17/ROUND-018.md). Main source,
header, root referee, adapter and original test entry remain unchanged. Source NONE.
EXP-006 is C/PARK; EXP-004 A/PARK and EXP-005 PARK/NONE remain.

BOUNDARY-025 passes 16 semantic cells, each with 18 partial/all-miss promotion clones,
25 sorted models and 21,864,700 exact iterator/member results. Three promotion-specific
faults detected, one new boundary fault family. Original live cursor/ownership checks
remain. HARNESS-007 adds a separate batch referee; corrected attempt passes 1,080
fixtures, 14 invalid-input checks and three reporting controls. Initial zero-wall-tick
rate-reporting failure is retained with its original snapshot; no child remains active.

AA-012 completes 240 rows plus warmup: long hits and mixed short batches qualify both
seeds; short hits, single-lane hits and misses PARK. PROFILE-004 captures both qualified
subsets. EXP-006 completes the fifth sequential proposal/chair and implementation
population. All four sources pass original tests, raw guard pages, exact tag matching
and batch fixtures in native/sanitizer builds. Protected-page helper validation passes
and detects an overread control. All 15 optimization patches remain.

EXP-006 screening 360 rows and fresh confirmation 96 rows retain all observations.
C passes fresh primary bounds both seeds but fails one long-key guard uncertainty
bound; single-lane screening regression remains a substantive concern. C/PARK, never
source adoption. Matched profiles show memchr removed and work in leaf lookup; no
frequency, PMU, unbiased time-share or complete guard-mechanism claim.

Audit PASS: 5,839 hashes, 2,253 serial command windows, 697 timing windows, 16 profiles
and four calibrations, 88 raw-derived intervals, 32 patch reconstructions. Two sanitizer
logs curated only after raw originals and prior manifests were preserved in scratch.
All experimental children finished before 05:33 UTC. No further trials this round.

Totals: 7 harnesses, 13 baselines, 31 diagnostics, 25 named boundary suites, 54 distinct
boundary fault types; 5 sequential populations; 0 accepted, 2 rejected, 3 parked.
Reviewer startup failed; confirmation/review are sequential. Exact backend/model/cost
unknown; supervisor records CLI usage separately. Committed provenance and independent
review remain pending. No publishing, git retry, runtime/STOP or permission changes.

Next: [batch-size guard investigation](../experiments/OVERNIGHT-2026-10-17/ROUND-018-NEXT-FIXTURE.md)
with a new preregistered profile/diagnostic or a qualified runner. Do not rerun unchanged
schedules, drop long-key blocks, or treat primary-only gains as adoption. Preserve main
baseline for morning review. Final worker still owes MORNING-REPORT.md by 07:00 UTC /
08:00 Europe/Lisbon; this was not the final round.

Round18 final workspace/pristine-source and whitespace checks PASS. Final audit checks 5,839 hashes after excluding two intentionally updated shared ledgers from prior evidence; final ledgers are sealed in ROUND-018-SHA256.json. All children finished.

Round19 PROFILE-005 completes8single-lane captures/4calibrations. Baseline memchr leads; C leaf lookup leads, no unbiased time-share or frequency claim.32diagnostics; sourceNONE/EXP-006C-PARK unchanged. New prefetched/nonprefetched batch-size factorial preparation underway; initial ANSI-classifier failure retained.

Round19 DIAG-019 completes576fixed rows,332validation/codegen commands; all invariants pass.0/8AA cells qualify, attenuation criterion fails discovery/freshseeds. Prefetch-removal remedy unsupported;33diagnostics. SourceNONE/EXP-006C-PARK unchanged; no retry. SUMMARY top table repaired to match prior round18 recorded totals.

Round19 BOUNDARY-026 passes32source/build/seed cells including16freshdebug-disabled; each1345keys/6models/342975batches/2743800lanes/1567343exactresults. Both lane-reuse controls detected;26suites, historical54faulttypes unchanged pending taxonomy review.33diagnostics; sourceNONE/EXP-006C-PARK unchanged. Initial missing-math.h compile failure retained.

Round19 COUNTERS-011 completes16scoped captures plus reset/dumpcontrol0/20/0. Same leaf/index/hash logical branch census acrossbatch1/16,control/C,prefetchon/off perseed; APIcallcount differsasexpected.34diagnostics; no time/frequency claim or guardrepair. SourceNONE/EXP-006C-PARK unchanged. All experiments finished; audit andhandoff next.

## Round 19 completed handoff

Canonical [ROUND-019](../experiments/OVERNIGHT-2026-10-17/ROUND-019.md). Source adoption
NONE; EXP-006 C/PARK, EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. Main source,
header, root referee, adapter and original tests retain their starting hashes.

PROFILE-005: eight scoped single-lane captures/four calibrations pass; changed memchr
versus leaf attribution is descriptive. DIAG-019: 332 validation/codegen commands and
576 fixed rows complete. None of eight A/A cells qualifies; prefetch-removal attenuation
criterion fails both discovery and both fresh seeds. No remedy, row exclusion or gate
change. Caller instructions match control/C except five panic-line immediates per mode.

BOUNDARY-026 passes 32 source/build/seed cells, including 16 fresh debug-off cells.
Each checks 1,345 binary-prefix keys, six live sorted models, 342,975 batches,
2,743,800 lanes and 1,567,343 exact-score results. Both deliberate lane-reuse controls
are detected. They are reported separately from the historical 54 distinct fault types
pending taxonomy review. Initial missing-header and ANSI reporting failures preserved.

COUNTERS-011: public LLVM reset/dump scope control 0/20/0 passes; sixteen captures
show identical leaf/index/hash logical paths across batch sizes and source/prefetch
conditions per seed. API-call counts differ as expected. No timing/PMU/frequency claim.

Audit PASS: 7,455 hashes, 1,051 serial command windows, 60 raw-derived intervals,
1,080 branch mappings and 33 patch reconstructions, including all 15 optimization
patches. Workspace/pristine-source and whitespace checks pass. Experimental children
finished at 05:50:14 UTC. No more trials this round. Initial caller-audit assertion is
documented and corrected without experimental reruns. Prior immutable evidence stays.

Totals: 7 harnesses / 13 baseline explorations / 34 diagnostics / 26 named boundary
suites; 54 previously catalogued distinct boundary fault types plus two unclassified
lane-reuse controls; 5 sequential populations; 0 accepted / 2 rejected / 3 parked.
SUMMARY's stale top table was reconciled to recorded round18 totals before additions.
Reviewer startup failed; confirmation/review sequential, exact backend/model/token cost
unknown. Supervisor records CLI usage separately. No publishing, git retry, credentials,
permission or supervisor/runtime/STOP changes. Frequency/effective QoS/migration,
qualified guards, independent review and committed provenance remain unresolved.

Next: [candidate cross-boundary matrix](../experiments/OVERNIGHT-2026-10-17/ROUND-019-NEXT-FIXTURE.md).
Three exact frozen oracle sources and sanitizer commands are inspected in its preflight
manifest, but EXP-006 compatibility with those histories is NOT RUN. Preregister a
bounded source/build/seed matrix; source-included oracles must not link a second .c copy.
Do not repeat the failed timing schedule or reinterpret counters as speed. Keep main
baseline for morning review. Final worker still owes MORNING-REPORT.md by 07:00 UTC /
08:00 Europe/Lisbon; round19 was not final. Candidate matrix records superseded decisions.

Round19 finalizer self-match false positive retained as attempt001; stricter concrete-path scanner correction and final sealing only, no experimental rerun. Final hashes/checks are in ROUND-019-SHA256.json and ROUND-019-FINAL-CHECKS.json.

Round20 in progress: fixed EXP-006 cross-boundary matrix discovery40cells PASS; fresh40cells running. Exact BOUNDARY-023/025 oracles and candidate snapshots preserved. Fivefault transfers, scalarfallback and dense short-leaf promotion extensions preregistered. No timings/sourceadoption; counts unchanged. Reviewer startup failed; sequential review only.

Round20 cross-boundary extension COMPLETE:80semantic cells/48builds pass exact EXP-006control/A/B/C across partialpromotion, narrowing and3external-relocation modes; freshdebug-off confirmation included. Logicaldigests agree. No new named suite/harness/baseline/diagnostic/population; counts remain7/13/34/26 and0accepted/2rejected/3parked. Faulttransfers next; sourceNONE/C-PARK unchanged.

Round20 sensitivity transfer COMPLETE:all5existing faults on EXP-006C detected at intended boundaries (promotionUAF, last-hitmask, outside-countcanary, compactedID, clonedexternalownership). Repeated controls only; historical fault counts unchanged. Scalarfallback branch validation running; mainbaseline/sourceNONE/C-PARK unchanged.

Round20 scalarfallback COMPLETE:16semantic cells/16builds plus16preprocessing checks PASS. Exactpreprocessed code differs only in B/Chelper;1,585,152first-match and198,144guard-page checks per relevantcell agree. Deliberatezero-spanread detected. This is forcedfallback onM1, NOTbig-endianexecution. No new suite/diagnostic/faultfamily; sourceNONE/C-PARK unchanged. Densepromotion extensionrunning.

Round20 densepromotion extension COMPLETE:8control/C native/sanitizer cells, two freshseeds,36promotion cases/264lanes and68dense-hit leaf checks each;43models and over36million exact results/cell. All original ownership/SCAN/score assertions retained. No new named suite/diagnostic/population/faulttype; sourceNONE/C-PARK unchanged. All experimental children ended06:17:46UTC; auditPASS3361hashes/204serialwindows/22patches.

## Round 20 completed handoff

Canonical [ROUND-020](../experiments/OVERNIGHT-2026-10-17/ROUND-020.md). Source adoption
NONE; EXP-006 C/PARK, EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. Main source,
header, root referee, adapter and original tests retain their hashes. No new timings.

Cross-boundary compatibility passes80 fixed control/A/B/C native/sanitizer cells and
48 builds across partial promotion, widening/narrowing and three external-relocation
modes; fresh debug-off confirmation included. Five transferred C faults detected at
intended boundaries. Scalar fallback passes16 cells/16 builds/16 preprocessing commands;
whole program equality holds except B/C helper selection. First-match/page guards pass,
zero-span-read control detected. This is not actual big-endian execution.

Dense promotion passes8 control/C cells and8 builds:36 cases/264 lanes,68 dense-hit leaf
observations,43 models and over36million exact results each. All original ownership,
SCAN, score and accounting checks remain. A/B not run on this new fixture. All six
fault controls repeat existing families; no new production bug or fault count claimed.

Audit PASS:3,361 hashes,204 serial experimental command windows,22 reconstructed patches
including all15 optimization patches; prior audit checks2,149 immutable files. Workspace/
pristine-source and whitespace checks pass. Experimental children ended06:17:46UTC.
Post-hoc static assembly inventory adds no timing/causal claim or diagnostic count.

Totals unchanged:7 harnesses/13 baselines/34 diagnostics/26 named boundary suites;
5 sequential populations;0 accepted/2 rejected/3 parked. Historical54 boundary fault
types plus two unclassified round19 lane controls remain. Reviewer startup failed;
review/confirmation sequential, exact backend/model/token cost unknown. Supervisor
records CLI usage separately. No publishing, git retry, credentials, permission or
supervisor/runtime/STOP edits. Qualified guards, independent review, committed
provenance, frequency/effective QoS/migration and actual portability remain unresolved.

Next: [morning report preparation](../experiments/OVERNIGHT-2026-10-17/ROUND-020-NEXT.md).
The queued cross-boundary work is complete. Final worker must write MORNING-REPORT.md
before07:00UTC/08:00Lisbon, preserving rejected/superseded decisions and main baseline.
Do not rerun failed timing schedules unchanged or equate correctness with acceptance.

Round20 final bounded extension now running:8fixed EXP-006source/build cells on BOUNDARY-021 naturalgeneration wrap with fresh94503/94521 seeds; all existing checks retained. Earlier104cell checkpoint and469sealed files preserved in scratch/round020-checkpoint with ROUND-020-CHECKPOINT-INDEX.json. Final handoff/seal will supersede checkpoint; no timing/count/source decision change.

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


## Latest: night preparation, five sizes, Lemire review

Shared M1/M6 plan: experiments/NIGHT-EXPLORATION-001/README.md. Prepared only; no
overnight start. Supervisor supports --prompt-file/--campaign-dir/--host-label and
six real process-control tests passed. New runner includes 1M with 600s timing cap;
old four-size results preserved, analyzer backward compatibility checked. User wants
all plans pushed and both hosts to follow the same queue. Lemire template and pinned
counters v3.2.0 inspected; adaptation notes saved. No tree source change.


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
