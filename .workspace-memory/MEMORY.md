# Shared memory

Latest: [EXP-007 bulk decoder results](../experiments/EXP-007/RESULTS.md).
Completed both real three-agent population steps. B shortlist gives -33.14% primary
and about -43% aligned full-leaf elapsed time on fresh seeds, but three qualified
discovery guard regressions prevent universal use. Experiment PARK, source NONE.
Six optimization populations: five historical sequential, one actual multi-agent;
0 accepted / 2 rejected / 4 parked. All 18 patches retained. Overnight remains stopped.

Latest: [19 October focused decoder benchmark](../experiments/EXP-004/decoder-microbench-2026-10-19/README.md)
is implemented, validated and locally run. EXP-004 A is slower in aligned 8/64-bit
kernel cases despite fewer static branches. One new harness/diagnostic; no new
optimization population or source adoption. Overnight remains stopped. Original
iterator guard and A/PARK remain. See the report for commands, raw evidence and limits.

- [Live status](LIVE-STATUS.md): preparation state and next action.
- [Handoff](handoff.md): user scope, source pin, evidence and remaining work.
- [Preparation evidence](../experiments/PREP-001/README.md).
- [Local M1 baseline and CPU MCP exploration](../experiments/EXP-001/local-m1-2026-10-17/README.md):
  user-authorised timings; all checks pass, precision qualification parked, profiles and
  allocator/codegen evidence retained; no source candidate.

This repository is the shared memory for all agents. Recheck live upstream state before
refreshing source. The pinned source manifest remains the baseline provenance.

- [Overnight harness revision](../experiments/OVERNIGHT-2026-10-17/HARNESS-001/README.md):
  repeated traversals and scheduling observations; separate requalification required.

- [Overnight round1 handoff](../experiments/OVERNIGHT-2026-10-17/ROUND-001.md):
  harness + targeted qualification, reuse diagnostic, two boundary suites and scoped
  execution counts. Source selection NONE; suite PARK; no independent agents ran.

- [Overnight round2 handoff](../experiments/OVERNIGHT-2026-10-17/ROUND-002.md):
  larger-fixture A/A96 rows (rank only qualifies), add-bracket diagnostic24 windows
  unsupported, natural-ID and relocation suites pass both builds with four detected
  faults. Lookup PARK, source NONE; no independent agent could start. Root unchanged.

- [Overnight round3 handoff](../experiments/OVERNIGHT-2026-10-17/ROUND-003.md):
  120 diagnostic windows; fresh-seed construction/query interaction supported, prior
  advantage hypotheses unsupported. Four scoped path-count captures match query modes;
  two boundary suites and four fault controls pass. Source NONE, lookup PARK. Next
  isolated independent-query referee revision and preregistered A/A; root frozen.

- [Overnight round4 handoff](../experiments/OVERNIGHT-2026-10-17/ROUND-004.md):
  independent-query HARNESS-002 validated; AA-00396 rows all four cells PARK. Public
  self-process profiler succeeds (two calibrations,12 captures);48-row perturbation
  diagnostic supports only coarse bound. Lexical/append-batch suites and four faults
  pass. Source NONE; root unchanged. Next distinct placement/phase diagnostic or
  fixture coverage; all acceptance/population gates and morning commit review pending.

- [Overnight round5 handoff](../experiments/OVERNIGHT-2026-10-17/ROUND-005.md):
 1152 phase/intervention windows, validated HARNESS-003 miss warmup,AA-00496 rows all
 PARK,18 timer calibrations, batched-score/guard-page suites and four fault controls.
 Source NONE/root preserved.3 harnesses,5 baselines,12 diagnostics,10 suites/20 faults.
 Next distinct placement diagnostic or uncovered fixture; calibration helper corrected.

- [Round6 handoff](../experiments/OVERNIGHT-2026-10-17/ROUND-006.md): QoS diagnostic
  unsupported; clone suite passes; traversal profiles/A/A establish iterator subset.
  [EXP-002](../experiments/EXP-002/README.md) completes both sequential populations,
  selects isolated C with fresh confirmation/profile evidence; PARK for broader guards,
  independent review and committed provenance. Main baseline preserved.

- Round7 in progress:HARNESS-004 iterator mode referee and AA-00610/14 qualified.
  EXP-002 expanded guards/fresh seeds supersede C/PARK with REJECT/NONE. Boundary012
  mixed mutation/mask oracle passes all4variants/both builds;two faults detected.
  New EXP-003 outlining member decoder validates next;root baseline preserved.

- [Round7 completed](../experiments/OVERNIGHT-2026-10-17/ROUND-007.md):HARNESS-004 and
  AA-00610/14qualification;expanded EXP-002 guards reject all3,superseding C/PARK.
  New EXP-003 member-outlining population also rejects all3 on fresh guards.1776rows,
  20profiles/4calibrations,boundary012 pass;root baseline/all patches preserved.

- Round8 in progress:COUNTERS-003 structural census complete,320passing children;
  cross-build allocator-only audit retained.15diagnostics;main baseline untouched.

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

- [Round 8 completed](../experiments/OVERNIGHT-2026-10-17/ROUND-008.md): EXP-004 A/PARK,
  1,200 measured rows,20 profiles/4calibrations; packed census and exhaustive decoder
  oracle pass. Longer duration and caller hypotheses do not clear mask6. All source
  baseline/patches preserved;3sequential populations,0accepted/2rejected/1parked.

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


19October2026 AWS Intel native lookup: **REJECT/NONE**,1completed sequential population(0accepted/1rejected/0parked),3retained patches.432rows/108blocks, all variants slow both primaries; baseline source unchanged. [Intel evidence](../experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup/implementation-selection.md). Other-host and historical counts remain separate.


19October2026 AWS Intel update diagnosis **NONE**: separate validated five-pattern referee,360semanticcells,15scopedprofiles+disabledcontrol,25censuscells,600baseline rows/25cells(2qualified). No newimplementationpopulation; Intelcount stays1measuredpopulation/1REJECT/3retainedpatches. See experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/003-update/README.md. Source unchanged.
