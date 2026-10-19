# Experiment log

## 19 October: focused decoder diagnostic

[EXP-004 decoder microbenchmark](EXP-004/decoder-microbench-2026-10-19/README.md)
adds one isolated harness/diagnostic after the overnight campaign. Release and
ASan/UBSan validation passed for baseline/A. The fixed matrix completed 960 serial
processes / 123,840 batches in 12.58 seconds. Forward 8-bit/64-bit layouts show A
15.65%/10.39% slower by paired median time, separated from same-cell A/A ranges.
All rows retained and independently reconstructed from raw CSVs. Main source NONE;
EXP-004 A/PARK and 0 accepted / 2 rejected / 3 parked unchanged. No new population
or overnight restart; original iterator guard remains unresolved.

Append-only decisions and evidence; correct earlier records with a dated addendum.
Preparation and baseline qualification do not count as accepted optimisations.

| ID | Date | Purpose | Status | Decision |
|---|---|---|---|---|
| [PREP-001](PREP-001/README.md) | 2026-10-17 | Extract standalone tree, validate adapter, prepare microbenchmarks and population protocol | COMPLETE | No source optimisation |
| [EXP-001](EXP-001/README.md) | 2026-10-17 | Qualify standalone baseline, A/A precision and profiles | PLANNED | NOT RUN |

Accepted: **0**. Rejected: **0**. Parked: **0**. Population rounds executed: **0**.

## 2026-10-17 — EXP-001 local M1 addendum

User authorised local benchmarks and CPU Performance Engineering MCP exploration.
[Run and findings](EXP-001/local-m1-2026-10-17/README.md): 144 serial processes, 984 rows,
four sampled profiles, generated-code inspection and allocator/clock probes. All checksum
checks pass. Baseline qualification PARKED: only 1/41 cells meets the preregistered gates;
frequency and placement remain unmeasured. Short-key leaf-tag scanning, long-key hashing
and the allocator's 320/321-byte size class are documented follow-ups. No source candidate,
population decision or accepted optimisation. Optimisation counts above remain unchanged.

## 2026-10-17 — overnight continuation authorised

User requested experimentation through the night. [Campaign plan](OVERNIGHT-2026-10-17/PLAN.md)
sets 18 October 08:00 Lisbon as the endpoint, starting with harness observability and
duration, then A/A requalification and the two population stages where evidence permits.
A local supervisor preserves transcripts and usage under ignored scratch/; curated
results and candidate patches remain drafts for morning review. This orchestration
entry is not a measured result or an optimisation decision. Counts are unchanged.

## 2026-10-17 — HARNESS-001 observability revision

[Harness evidence](OVERNIGHT-2026-10-17/HARNESS-001/README.md): release and sanitizer
validation passed. Repeated traversals, effective callback counts/checksums, thread CPU
time, boundary CPU IDs and queried QoS added. Effective QoS/frequency remain unknown.
Decision: locally validated referee revision, pending frozen A/A requalification and
morning commit review. Source candidate NONE. Optimisation/population counts unchanged.

## 2026-10-17 — AA-001 targeted requalification and scan profile attempt

[AA-001](OVERNIGHT-2026-10-17/AA-001/README.md): 192 serial rows, all checks pass;
2/8 cells (iterate16, scan16) qualify locally. Lookup/rank/update and suite PARK.
No timing rows excluded. [Scan profile](OVERNIGHT-2026-10-17/SCAN-PROFILE-001/README.md)
failed because sample cannot examine the child in this worker; no escalation/retry.
Source selection NONE. Optimisation/population counts remain unchanged.

## 2026-10-17 — DIAG-001 process/fixture reuse

[Diagnostic](OVERNIGHT-2026-10-17/DIAG-001/README.md): all 42 serial processes /
72 windows pass functional invariants. Preregistered reduction-in-variation criterion
met in only 1/6 blocks; hypothesis not supported. Do not adopt reuse as a precision
remedy. AA-001 PARK persists; source selection NONE. No optimisation counts added.

## 2026-10-17 — additional boundary and execution-count evidence

[BOUNDARY-001](OVERNIGHT-2026-10-17/BOUNDARY-001/README.md) and
[BOUNDARY-002](OVERNIGHT-2026-10-17/BOUNDARY-002/README.md) pass release/debug and
ASan/UBSan; four isolated intentional faults are detected. No baseline bug observed.
[COUNTERS-001](OVERNIGHT-2026-10-17/COUNTERS-001/README.md) collects three scoped
Clang execution-count profiles with verified loop counts; these are not CPU-time
profiles and do not close the scan profiling gate. Source selection NONE.
Optimisation counts remain 0 accepted / 0 rejected / 0 parked; population rounds0.

## 2026-10-17 — AA-002 large-fixture requalification

[AA-002](OVERNIGHT-2026-10-17/AA-002/README.md): 96 serial observations, all functional
checks and hashes pass. Rank16 alone qualifies (1/4); hit16/miss16/hit320 remain PARK.
No rank time profile and unqualified lookup guards: source selection NONE. No
population or optimisation count added. Fixed schedule complete, no excluded rows.

## 2026-10-17 — BOUNDARY-003 natural widening

[BOUNDARY-003](OVERNIGHT-2026-10-17/BOUNDARY-003/README.md): two seeds pass release/debug
and ASan/UBSan; natural next leaf ID70834, active widening and mutation-scan continuity
validated. Two isolated fault controls detected. No source bug/candidate or optimisation
count. Agent startup failed; sequential coordinator review only, selection NONE.

## 2026-10-17 — DIAG-002 execution-rate bracket diagnostic

[DIAG-002](OVERNIGHT-2026-10-17/DIAG-002/README.md):24 checked lookup windows with
adjacent dependent-add brackets. Preregistered association/normalization criterion not
met; no demonstrated precision remedy. No clock/frequency claim; lookup PARK and
selection NONE unchanged. Additional diagnostic count only, no optimisation/population.

## 2026-10-17 — BOUNDARY-004 relocation API

[BOUNDARY-004](OVERNIGHT-2026-10-17/BOUNDARY-004/README.md): four fixtures pass
release/debug and ASan/UBSan,2673 full model checks per build. Exact usable-size
accounting, relocated pointers and clone ownership validated; two intentional faults
detected. No source bug/optimisation candidate; source selection NONE, counts unchanged.

## 2026-10-17 — DIAG-003 access-order diagnostic

[DIAG-003](OVERNIGHT-2026-10-17/DIAG-003/README.md):24 checked windows, six serial
processes, fixed repeated-versus-reshuffled schedule complete. Preregistered advantage
criterion not met; no fixture-history remedy established. Lookup PARK, source NONE;
additional diagnostic count only. Root source/referee unchanged; no independent agent.

## 2026-10-17 — BOUNDARY-005 controlled probe boundaries

[BOUNDARY-005](OVERNIGHT-2026-10-17/BOUNDARY-005/README.md): strengthened fixture
passes release/debug and ASan/UBSan,622 model checks/build, two faults detected.
Initial failed preconditions preserved; final fixture forces distance23 lookup
wraparound without weakening checks. Source NONE; no optimisation count added.

## 2026-10-17 — BOUNDARY-006 bulk-deletion thresholds

[BOUNDARY-006](OVERNIGHT-2026-10-17/BOUNDARY-006/README.md):48 cases/build straddle
absolute/relative rebuild cutoffs,24 start during active resize. Release/debug and
ASan/UBSan pass240 verifications/build; two fault controls detected. Source NONE;
additional correctness coverage only, no optimisation count.

## 2026-10-17 — DIAG-004 construction-history diagnostic

[DIAG-004](OVERNIGHT-2026-10-17/DIAG-004/README.md):48 checked rows, fixed schedule
complete. Ascending-insertion advantage not supported; contrary local pattern is
exploratory fixture sensitivity, not a source speed claim. Fresh independent-query
follow-up motivated. Lookup PARK, source NONE; optimisation counts unchanged.

## 2026-10-17 — DIAG-005 construction/query interaction

[DIAG-005](OVERNIGHT-2026-10-17/DIAG-005/README.md):48 fresh-seed processes pass all
controls; fixed interaction criterion supported locally. Independent query permutation
largely removes construction contrast. Add fixture coverage; no cache/frequency or
source speedup claim. Lookup PARK, source NONE; optimisation counts unchanged.

## 2026-10-17 — COUNTERS-002 query-order path frequencies

[COUNTERS-002](OVERNIGHT-2026-10-17/COUNTERS-002/README.md):four captures pass scoped
entry/reset checks. All tree function/region/branch counts match between S/I queries
within construction arm. Path-frequency control validated, no time-profile claim.
Source NONE, lookup PARK; optimisation/population counts unchanged.

## 2026-10-17 — overnight round4 harness decision

[HARNESS-002](OVERNIGHT-2026-10-17/HARNESS-002/README.md): isolated independent-query
referee revision passes release/debug and ASan/UBSan, original tests and80 new fixture
cells/build. Root source/referee preserved. Locally validated, uncommitted; qualification
pending AA-003. Two harness revisions, optimisation/population counts unchanged at zero.

[AA-003](OVERNIGHT-2026-10-17/AA-003/README.md):96 independent-query A/A rows,0/4
cells qualify unchanged precision gate; all semantics/memory stable. Qualification PARK,
source NONE. Four baseline explorations complete; optimisation/population counts zero.

[PROFILE-002](OVERNIGHT-2026-10-17/PROFILE-002/README.md): public self-process SIGPROF
sampler passes two known-function calibrations and captures12 scoped baseline profiles.
All symbols resolved and semantic checks pass; memchr/SipHash/rank evidence retained.
Descriptive sampled-PC counts only, not precision remedy or unbiased time fractions.
Eight additional diagnostics complete; source NONE, lookup PARK unchanged.

[BOUNDARY-007](OVERNIGHT-2026-10-17/BOUNDARY-007/README.md):36 lexical fixtures,180
model checks,4075200 seeks/build pass release/debug+ASan/UBSan; two faults detected.
Seven boundary suites now validated,14 fault controls total. No source decision change.

[BOUNDARY-008](OVERNIGHT-2026-10-17/BOUNDARY-008/README.md):18 append-batch fixtures/
162 model checks per build pass release/debug+ASan/UBSan; borrowed-buffer and missing-
flush faults detected. Eight boundary suites/16 fault controls; source NONE unchanged.

[DIAG-006](OVERNIGHT-2026-10-17/DIAG-006/README.md):48 fixed same-executable sampler
off/on rows meet the predeclared bounded-perturbation diagnostic criterion. It does not
qualify source guards or establish unbiased profiles. Nine diagnostics complete; source
NONE/lookup PARK unchanged. Instrument output moved after thread timer in this snapshot.

## 2026-10-17 — overnight round5 DIAG-007 phase diagnostic

[DIAG-007](OVERNIGHT-2026-10-17/DIAG-007/README.md):24 processes/384 consecutive
windows, all controls pass. Only1/4 cells meets the phase criterion (required2); overall
hypothesis unsupported. Source NONE/lookup PARK unchanged;10 additional diagnostics.
No rows filtered, source candidate, population or independent agent.

## 2026-10-17 — BOUNDARY-009 batched-score API

[BOUNDARY-009](OVERNIGHT-2026-10-17/BOUNDARY-009/README.md):526590 batches/7883000
score slots per build pass release/debug+ASan/UBSan, including28 active-resize batches;
two planned faults detected. Nine suites/18 faults; source NONE unchanged.

## 2026-10-17 — DIAG-008 warmup-operation intervention

[DIAG-008](OVERNIGHT-2026-10-17/DIAG-008/README.md):48 fresh-seed ABBA processes/
768 windows, all controls pass. Primary short-miss phase-contrast criterion supported;
secondary long-key contrast not supported. Warrants isolated miss-warmup referee change,
not frequency/cache attribution or precision cure.11 diagnostics; source NONE/PARK.

## 2026-10-17 — HARNESS-003 miss warmup

[HARNESS-003](OVERNIGHT-2026-10-17/HARNESS-003/README.md): isolated miss-operation
warmup and explicit warmup_case;43 upstream tests, three referee groups and80 query
cells/build pass release/debug+sanitizers. Third harness revision; AA-004 preregistered,
qualification pending. Main source/referee untouched; source NONE.

## 2026-10-17 — AA-004 qualification decision

[AA-004](OVERNIGHT-2026-10-17/AA-004/README.md):96 fresh-seed rows,0/4 cells qualify
unchanged precision gate. All semantics/memory controls pass. Warmup phase improvement
did not establish noise remedy. Fifth baseline exploration; source NONE/lookup PARK.

## 2026-10-17 — BOUNDARY-010 guarded raw buffers

[BOUNDARY-010](OVERNIGHT-2026-10-17/BOUNDARY-010/README.md):four fixtures/33 lengths,
260 guarded mappings/652 raw queries per build pass release/debug+ASan/UBSan; both
overread/truncated-hash faults caught. Initial missing-header compile failure retained,
only required header added in separate final snapshot.10 suites/20 faults; source NONE.

## 2026-10-17 — DIAG-009 timer delivery-rate calibration

[DIAG-009](OVERNIGHT-2026-10-17/DIAG-009/README.md):18 fixed known-function runs
pass calibration, but requested1000/3001us rate-equivalence criterion fails; overall
hypothesis unsupported. Corrected stop/dump calibration interface preserved in new
snapshot. No clock/profile-share claim;12 diagnostics/source NONE/lookup PARK.

Round5 capability preparation (not a new measurement decision): a one-shot public QoS
setter probe succeeds, inherited user-interactive->user-initiated in a short-lived child.
AA-004 already reports user-interactive. Effective QoS/placement/frequency unknown; all
counts and NONE/PARK decisions unchanged. Probe/SDK hashes in ROUND-005-QOS-PROBE.json.

## 2026-10-18 — DIAG-010 requested QoS

[DIAG-010](OVERNIGHT-2026-10-17/DIAG-010/README.md):96 fixed serial ABBA rows pass
all controls; user-initiated request does not meet primary repeatability criterion.
13 diagnostics; source NONE/lookup PARK, no population or general harness change.

## 2026-10-18 — BOUNDARY-011 clone ownership

[BOUNDARY-011](OVERNIGHT-2026-10-17/BOUNDARY-011/README.md):12 fixtures/build,74 full
model checks and22 clone audits pass release/debug+sanitizers; two faults detected.
Fault-driver matcher failed because accounting caught shallow copying earlier; original
failure retained and audited.11 suites/22 faults; source NONE/lookup PARK unchanged.

## 2026-10-18 — traversal profile and A/A decisions

PROFILE-00312 scoped captures/two calibrations establish descriptive traversal coverage.
AA-00596 rows qualify iterate16/320 only; scan/lookup/suite PARK.14 diagnostics,6 baseline
explorations. EXP-002 begins three sequential proposals/chair and three isolated iterator
implementations; agents unavailable. No acceptance/source baseline change.

## 2026-10-18 — EXP-002 PARK, selected C

[EXP-002](EXP-002/README.md) completes three sequential proposals/chair, three isolated
implementations and measured selection.64 validation commands pass original+lexical+score
oracles in release/sanitizers.72 screening rows select C via predeclared overlap/smaller
patch rule;24 fresh-seed rows confirm and four matched profiles support dispatch/register
isolation. Final PARK: reverse/full-output performance guards, independent review and
committed provenance missing.1 sequential population round,0 accepted/0 rejected/1 parked.
All patches/source/raw evidence retained; main source baseline unchanged.

## 2026-10-18 — HARNESS-004 iterator mode referee

[HARNESS-004](OVERNIGHT-2026-10-17/HARNESS-004/README.md) passes640 cells/build plus
original tests in release/sanitizers;three referee sensitivity faults caught. Both
directions/all masks/four encodings covered;root preserved. Fourth harness revision,
AA-006 preregistered. EXP-002 PARK unchanged;no new optimisation/population count.

## 2026-10-18 — AA-006 expanded iterator precision

[AA-006](OVERNIGHT-2026-10-17/AA-006/README.md):336 fixed rows,all functional/memory
controls pass;10/14 modes qualify. Four forward mixed-output modes PARK. Seventh
baseline exploration;EXP-002 expanded guards preregistered,source baseline preserved.
Optimisation/population counts unchanged.

## 2026-10-18 — EXP-002 expanded guards supersede PARK: REJECT/NONE

[Expanded evidence](EXP-002/guard-extension/README.md):control/A/B/C pass5144 validation
commands (original tests+640cells/build).504 fixed discovery rows show qualified guard
regressions.216 fresh-seed rows confirm no-output regression for ALL three on BOTH seeds;
B/C full-output also confirms. Eight matched profiles/two calibrations pass;codegen
supports extra dispatch on fallback. REJECT these implementations,selection NONE.
Main source unchanged;all patches preserved.0 accepted/1 rejected/0 parked;one sequential
population round. Four unqualified iterator modes and lookup/suite precision remain PARK.
No independent agent or portable headline claim;morning commit review pending.

## 2026-10-18 — BOUNDARY-012 mutation/iterator coverage

[BOUNDARY-012](OVERNIGHT-2026-10-17/BOUNDARY-012/README.md):control/A/B/C each pass
release/debug+sanitizers,1032 model checks/2176436 iterator results per build. Both
faults detected;first driver message mismatch retained/audited.12 suites/24 faults;
source baseline untouched. EXP-003 member-decoder outlining population now planned
from current profile/A/A evidence;three sequential proposals/chair and isolated variants.

## 2026-10-18 — EXP-003 REJECT/NONE

[EXP-003](EXP-003/README.md):second population round (three sequential proposals/chair,
three isolated member-decoder outlining implementations).1064 validation commands pass.
504fixed screening+216fresh rows confirm full-output regressions for ALL3 on BOTH seeds.
12matched profiles/two calibrations pass;codegen reduces register saves but introduces
member-helper work. REJECT/NONE,root unchanged,all losing patches preserved. Counts:
0accepted/2rejected/0parked;two sequential population rounds. Four AA-006 modes and
lookup/suite still PARK;independent confirmation/review and commit provenance absent.

## 2026-10-18 — COUNTERS-003 packed-path census

[COUNTERS-003](OVERNIGHT-2026-10-17/COUNTERS-003/README.md):320 serial runs pass
structural/score/member/state invariants. Narrow-width coverage supported in all four
preregistered primary fixtures;64-bit and cross-word paths still require coverage.
Post-run native/ASan owned-byte equality assertion retained;read-only audit isolates
allocator reporting,all structural fields match.15diagnostics;source NONE.

## 2026-10-18 — EXP-004 PLANNED

Three sequential proposals/chair select equivalent cross-word predicate simplification.
Three isolated implementations prepared;correctness and fresh baseline requalification
precede any timing. Main source untouched;no decision or new optimisation count yet.

## 2026-10-18 — BOUNDARY-013 packed-score geometry

[BOUNDARY-013](OVERNIGHT-2026-10-17/BOUNDARY-013/README.md):85760leaves/2572800exact-bit
checks per build pass release/debug and sanitizers;two deliberate faults detected.
Also passes all EXP-004 variants.13suites/26faults;root baseline preserved.

## 2026-10-18 — AA-007 current-round subset

[AA-007](OVERNIGHT-2026-10-17/AA-007/README.md):240fixed rows,all controls pass;6/10
cells qualify including EXP-004 primary/no-output/full-output. Four previously qualified
cells now PARK;four prior failures not rerun. Eighth baseline exploration. Root unchanged.

## 2026-10-18 — EXP-004 provisional A/PARK

[EXP-004](EXP-004/implementation-selection.md):third sequential population round;
1080validation commands pass,504screen+216fresh rows provisionally prefer A.12profiles/
2calibrations pass;cross-word branch removed. PARK for unqualified mixed-output guard/
broader operations/independent review/commit provenance. Long guard diagnostic planned.
0accepted/2rejected/1parked. Root source unchanged;all patches retained.

## 2026-10-18 — AA-008 duration diagnostic fails joint qualification

[AA-008](OVERNIGHT-2026-10-17/AA-008/README.md):96rows,all checks pass,2/4cells qualify.
Only one mask6 seed qualifies;long-guard source comparisons skipped per preregistration.
No precision cure;EXP-004 remains A/PARK. Ninth baseline;source baseline preserved.

## 2026-10-18 — DIAG-011 caller context unsupported

[DIAG-011](OVERNIGHT-2026-10-17/DIAG-011/README.md):144fixed rows,all controls pass;
interaction criterion fails one of two seeds.8profiles/2calibrations pass;codegen shows
Clang already unswitches mask6 caller tests,contradicting per-element-test premise.
384fixture runs+4builds pass;pre-timing cardinality erratum retained.16diagnostics;
EXP-004 remains A/PARK;referee not replaced,source baseline unchanged.

## 2026-10-18 — BOUNDARY-014 signed-zero physical mutation

[BOUNDARY-014](OVERNIGHT-2026-10-17/BOUNDARY-014/README.md): control/A/B/C pass both
builds;22,080modelchecks/46,005,384exactresults each. Bothphysicalorders,626reversal
opportunities;twofaultsdetected. First active-rehash memory precondition failure
retained/corrected explicitly.14suites/28faults;sourceNONE,EXP-004 A/PARK unchanged.

## 2026-10-18 — DIAG-012 controlled placement unsupported

[DIAG-012](OVERNIGHT-2026-10-17/DIAG-012/README.md):480rows+4warmups,allcontrols pass.
Bothplacebo A/Acontrols qualify;preselected16-byte effect criterion fails.1024fixtures
and4upstreamruns pass;complete instruction/symbol isolation audited.17diagnostics,
EXP-004 A/PARK unchanged. Preparation/audit corrections retained before timing.

## 2026-10-18 — EXP-005 planned

Three sequential proposals/chair select nonzero-width mask arithmetic;three isolated
implementations frozen over unchanged baseline,not combined with EXP-004. Validation
and fresh primary A/A precede comparisons. No new optimization decision/count yet.

## 2026-10-18 — AA-009 score-mask subset qualifies

[AA-009](OVERNIGHT-2026-10-17/AA-009/README.md):72fixedrows+1warmup,all3cells0/4/7
qualify;freshseed20101. Tenthbaseline. EXP-0051096validationcommands pass;180row
screening next. Previously failed mask6 schedule not repeated. Rootbaselinepreserved.

## 2026-10-18 — EXP-005 PARK/NONE

[EXP-005](EXP-005/implementation-selection.md):fourthsequentialpopulation,1096validation
commands pass;180screenrows provisionally preferC,but216freshrows fail primary bound.
12profiles/2calibrations pass;A/C hotinstructions match modulo panicliteralrelocations.
No source selected;allpatches kept.0accepted/2rejected/2parked. Mainbaselineunchanged.

## 2026-10-18 — round10 referee and layout coverage

[HARNESS-005](OVERNIGHT-2026-10-17/HARNESS-005/README.md) validates1,408cells/build plus
originaltests and3faults. Fifthharness; first fault-driver message mismatch retained.
[COUNTERS-004](OVERNIGHT-2026-10-17/COUNTERS-004/README.md) passes96children; descending
fixtures contain only64reversed members. Eighteenthdiagnostic; no speed claim/sourceNONE.

## 2026-10-18 — AA-010 new fixture precision

[AA-010](OVERNIGHT-2026-10-17/AA-010/README.md):384fixedrows,14/16cellseeds qualify;
sixofeightcells passbothseeds. TwointegerforwardcellsPARK. Eleventhbaseline;no oldguard
replacement. EXP-004 ordered-guards preregistered; retainedthreevariants only.

## 2026-10-18 — EXP-004 new guards pass; A/PARK unchanged

[Ordered guards](EXP-004/ordered-guards/README.md):1,194validationcommands pass.
432screen+432fresh rows and12profiles/2calibrations complete. All3variants pass allsix
newguards onbothfreshseeds; originalinteger mixed-outputguard remains unresolved.
Existing4populations;0accepted/2rejected/2parked. Mainbaseline andallpatches preserved.

## 2026-10-18 — compact reversed-leaf coverage established

[COUNTERS-005](OVERNIGHT-2026-10-17/COUNTERS-005/README.md):672structuralchildren pass
inbothbuilds. Public-API minimum-deletion recipe yieldsonefullyreversedleaf for n1..95,
includingclone/refillhistories;2faultsdetected. Nineteenthdiagnostic,sourceNONE.

## 2026-10-18 — BOUNDARY-014 compact sizes

[Compact extension](OVERNIGHT-2026-10-17/BOUNDARY-014/compact-extension/README.md)
passes all eight semantic runs: 1,940 fixtures, 289,060 model checks and 86,570,560 exact
results per build. Both retained faults detected. Cross-build whole-output equality
prediction fails only on aggregate physical-leaf counters; original failure retained,
no rerun or weakened oracle. Suite/fault-type counts unchanged; source NONE.

## COUNTERS-006 — allocator-capacity factorial (round 11)

Twelve unit and twelve semantic cells pass; fixed capacity policies produce identical
physical results across O1/O3/native/ASan, while ambient differs and capacity policy
changes orientation counts. Supported structural diagnostic; no optimization decision.
[Evidence](OVERNIGHT-2026-10-17/COUNTERS-006/README.md). 20 diagnostics; other counts unchanged.

## HARNESS-006 — compact-history referee (round 11)

Sixth isolated referee passes2,560fixtures/build,originaltests/invalid-input checks
and three sensitivity faults. Main source unchanged.
[Evidence](OVERNIGHT-2026-10-17/HARNESS-006/README.md). No optimization count change.

## AA-011 — compact A/A (round 11)

384rows complete;1/8jointcellsqualifies. Initialstale-traversalliteral analysis retained;
correctedanalysis applies original roundingrule,no reruns/thresholdchanges.12baselines.
[Evidence](OVERNIGHT-2026-10-17/AA-011/README.md). EXP-004 compact guard extension planned.

## EXP-004 compact guard extension — A/PARK unchanged (round 11)

1770validationcommands,144comparisonrows+4warmups,12profiles/2calibrations complete.
A/B passnewguardbothfreshseeds;C inconclusiveonone. SevenothercompactguardsPARK.
[Evidence](EXP-004/compact-guards/README.md). Countsunchanged:0accepted/2rejected/2parked.

## DIAG-013 — compact warmup intervention unsupported (round 11)

192rows+1warmup;longerwarmup halvesbiasin3/4pairs butonly1/4longintervalqualifies,
requiredall4. No policyadopted,AA-011 unchanged.21diagnostics.
[Evidence](OVERNIGHT-2026-10-17/DIAG-013/README.md).

Round11 final audit:720measuredrows+6warmups,26profiles+6calibrations,758serialwindows;
72intervals recomputed,7017timestamped nonmeasurementcommands disjoint. COUNTERS-006
fresh confirmation16cells passes; EXP-004 exact-mask profiles pass. Source NONE,
A/PARK unchanged. [Complete report](OVERNIGHT-2026-10-17/ROUND-011.md).

## 2026-10-18 — BOUNDARY-015 mixed finite-score capacity oracle

[BOUNDARY-015](OVERNIGHT-2026-10-17/BOUNDARY-015/README.md) passes 24 cells, each with
96 fixtures, 2,751 model checks and all 43 original tests. Both controlled capacity
policies yield identical complete output across baseline/A/B/C and native/sanitizer
builds. Ambient logical results agree; physical layouts can differ. Two new source
faults are detected. Initial invalid SCAN uniqueness assertion and complete failed
snapshot retained; corrected oracle honors documented duplicate semantics. No existing
check weakened. Fifteen boundary suites / 30 distinct boundary fault types; six harnesses,
twelve baselines, twenty-one diagnostics and optimization counts unchanged. Source NONE;
EXP-004 A/PARK and EXP-005 PARK/NONE. No new population or acceptance.

## 2026-10-18 — DIAG-014 predecessor workload discovery

[DIAG-014](OVERNIGHT-2026-10-17/DIAG-014/README.md) completes96target+96predecessorrows
andoneprospectivewarmup,allcontrols pass. Zero-trim-f6 meetsbothfreshseed directional
criteria;integer/no-output doesnot. Discovery supports predecessor sensitivity under
the combinedworkload/durationintervention,not frequencycausality or a noise remedy.
Freshmirrored-treatment/placeboconfirmation preregistered.22diagnostics;othercounts
unchanged. SourceNONE;EXP-004A/PARK andEXP-005PARK/NONE unchanged.

## 2026-10-18 — DIAG-014 mirrored confirmation and placebo: PARK

Freshconfirmationcompletes192rows+warmup. Reversed-labelOTHER/SAMEcontrast meetsboth
freshseedbounds;oneoftwoplacebointervalsfailsfixedprecision. Jointcriterionfails:
robustnessPARK;no timingpolicyadoption orsourceguardrepair. Discoveryandall384rows
+2warmups retained.22diagnostics;allothercounts andsourcePARK decisionsunchanged.

## 2026-10-18 — BOUNDARY-016 packed overlap geometry

[BOUNDARY-016](OVERNIGHT-2026-10-17/BOUNDARY-016/README.md) passes8source/buildcells,
each146,250packedinsert/deleteoperations againstanindependentbitreference. Complete
bufferdigestsagree;bothnewoverlap/tailfaultsdetected.16boundarysuites/32faulttypes;
othercountsunchanged. Rootbaselinepreserved;sourceNONE andexistingPARK unchanged.

## 2026-10-18 — DIAG-015 idle-gap intervention: unsupported

[DIAG-015](OVERNIGHT-2026-10-17/DIAG-015/README.md) completes 144 target and 144
predecessor rows plus one prospective warmup. All invariants pass. The predeclared
attenuation criterion fails: neither gap contrast/placebo qualifies on either seed,
and neither interaction clears its bound. No idle policy adopted. Twenty-three
diagnostics; source NONE, existing optimization PARK decisions and other counts unchanged.

## 2026-10-18 — round 12 final reconciliation

[Round 12](OVERNIGHT-2026-10-17/ROUND-012.md) retains both new passing boundary suites,
all four detected faults, the initial invalid SCAN assertion, and every timing row.
DIAG-014 robustness PARK and DIAG-015 unsupported leave source NONE and optimization
counts at0accepted/2rejected/2parked, four sequential populations. Current totals:
six harnesses, twelve baselines, twenty-three diagnostics, sixteen boundary suites /
32 distinct boundary fault types. Audit PASS:675 serial measured windows,122 disjoint
build/test/fault windows and32 raw-derived intervals. Main baseline preserved.

## 2026-10-18 — DIAG-016 coordinator bookkeeping: unsupported

384 measured rows plus warmup pass invariants and manipulation checks. Both buffered
contrasts remain outside equivalence and one buffered placebo fails precision.
No policy adoption;24 diagnostics, all other counts and source decisions unchanged.
See [DIAG-016](OVERNIGHT-2026-10-17/DIAG-016/README.md).

## 2026-10-18 — DIAG-017 completion transport: unsupported

384rows+warmup pass all invariants. Both transport success/timeout controls pass.
Pipe contrast attenuates descriptively, but one contrast and both placebo intervals
fail precision. Fixed criterion unsupported, no source guard or policy adoption.
25 diagnostics; other counts unchanged. [Evidence](OVERNIGHT-2026-10-17/DIAG-017/README.md).

## 2026-10-18 — BOUNDARY-017/018 compact storage and leaf-ID lifecycle

Both suites pass all eight source/build cells with identical logical digests. Each
index cell validates1,048,624 ID stores/4,096 tag stores/524,288 mask patterns. Each
registry cell validates38fixtures/1,458,668 registrations/602fullaudits. Fournew
faults detected. Initial registry compilefailure retained; only allocator API name
corrected.18suites/36distinctfaulttypes. Allsource/PARK/optimizationcounts unchanged.
[Storage](OVERNIGHT-2026-10-17/BOUNDARY-017/README.md), [registry](OVERNIGHT-2026-10-17/BOUNDARY-018/README.md).

## 2026-10-18 — DIAG-018 observed completion delay: supported locally

Discovery and fresh mirrored confirmation each48rows+warmup meet the narrow
observer-to-parent-return wall-delay criterion on bothseeds. Six transport/status/
timeoutcontrols pass. No exactkernel-exit or frequencyclaim; launchwrapper changes
environment and benchmarkprecision remainsmixed. No policy/sourceguardadoption.
26diagnostics; allothercountsunchanged. [Evidence](OVERNIGHT-2026-10-17/DIAG-018/README.md).

## 2026-10-18 — round 13 final reconciliation

[Round 13](OVERNIGHT-2026-10-17/ROUND-013.md) adds two passing boundary suites, four
fault types, and three diagnostics: two unsupported precision interventions and one
locally repeated observed-completion-delay finding. All 864 measured rows plus four
warmups remain. Audit passes 868 serial measurement windows, 52 disjoint validation
windows and 52 raw-derived intervals. Source NONE; EXP-004 A/PARK, EXP-005 PARK/NONE.
Totals: six harnesses, twelve baselines, twenty-six diagnostics, eighteen boundary
suites / 36 distinct fault types; four sequential populations, 0 accepted / 2 rejected /
2 parked optimizations. Main baseline preserved; no policy or source adoption.

## 2026-10-18 — round14 public lifecycle coverage

[BOUNDARY-019](OVERNIGHT-2026-10-17/BOUNDARY-019/README.md) passes all8source/build
cells,4fixtures/32modelchecks each. Both controls detected; one new distinct fault
type (cursor repair), premature-reuse fault repeats earlier synthetic coverage.
Initial invalid stale-cursor assertion and mutation-generator preflight preserved.
Source NONE; EXP-004 A/PARK and EXP-005 PARK/NONE unchanged.19boundary suites,
37distinct boundary faulttypes; no new timing/harness/baseline/population count.

## 2026-10-18 — round14 active-resize relocation coverage

[BOUNDARY-020](OVERNIGHT-2026-10-17/BOUNDARY-020/README.md) passes all8source/build
cells,4fixtures/32modelchecks each. Actual retired-defrag-cursor restart observed,
active resize preserved, exact quiescent allocation visits and ownership checked.
Both new faults detected.20boundary suites/39distinctfaulttypes. Original43tests
also pass each source/build cell in BOUNDARY-019. Source NONE/existing PARK unchanged;
no new timing/harness/baseline/population count.

## 2026-10-18 — round14 fresh mutation and recovery census

[BOUNDARY-020 fresh extension](OVERNIGHT-2026-10-17/BOUNDARY-020/mutation-extension/README.md)
passes8source/buildcells,8fixtures/448checks each. Both existing faults detected.
First failed header-move coverage retained; second plan forces header moves without
relaxing assertions. Output final means quiescent allocations, not membercount.
[COUNTERS-007](OVERNIGHT-2026-10-17/COUNTERS-007/README.md) completes3whole-oracle
coverage captures. Actual member-cursor repair and retired-defrag recovery observed;
freed-member-cursor/fallback unobserved. Not a timeprofile or unreachability proof.
27diagnostics;20boundarysuites/39distinctfaulttypes; sourceNONE/existingPARK unchanged.

## 2026-10-18 — round14 shrinking resize and natural generation wrap

[BOUNDARY-019 shrinking extension](OVERNIGHT-2026-10-17/BOUNDARY-019/shrink-extension/README.md)
passes8cells/4fixtures/88checks each, with one new scan-orientation fault detected.
[Separate COUNTERS-007 capture](OVERNIGHT-2026-10-17/COUNTERS-007/shrink-extension/README.md)
observes8end-of-list cursor fallback entries; freed-ID cursor remains unobserved.
[BOUNDARY-021](OVERNIGHT-2026-10-17/BOUNDARY-021/README.md) validates two native/
sanitizer baselinecells:2seeds/131080natural resizes/2wraps each; zero-generation
fault detected. Variants/high-water full-model extension not claimed.21boundary
suites/41distinctfaulttypes;27diagnostics. SourceNONE/PARK unchanged; no timing,
harness, baseline or population added. All source remains for morning review.

Round14 final audit: [report](OVERNIGHT-2026-10-17/ROUND-014.md),
[audit](OVERNIGHT-2026-10-17/ROUND-014-VERIFY.json).120serialcommandwindows,4branch
captures,2863hashchecks and original43tests in8cells PASS. No timing benchmark.
Source NONE; priorPARK unchanged. Counts21suites/41distinctfaults/27diagnostics;
othercounts unchanged. Next growth-side naturalwrap/fullhigh-water coverage.

## 2026-10-18 — round15 growth-side generation wrap

[BOUNDARY-021 growth extension](OVERNIGHT-2026-10-17/BOUNDARY-021/growth-extension/README.md)
passes all8cells:131080resizes,2growthwraps,131094modelchecks and12126950exactresults
each. Every low/high phase checked; actual newleaf generation1 observed. Zero-generation
fault detected again; singleton batch-marked-migrated fault SURVIVES. Retained as test
strength limitation; new multi-member fixture preregistered next. Counts unchanged:
21suites/41distinctfaulttypes/27diagnostics; sourceNONE/priorPARK unchanged.

## 2026-10-18 — round15 multi-member natural wrap extension

[BOUNDARY-021 multi-member extension](OVERNIGHT-2026-10-17/BOUNDARY-021/batch-extension/README.md)
passes8cells ×4fixtures:262160naturalresizes,4growthwraps,262188models and24254190
exactresults each. Both faults detected; previously surviving premature batch-migration
fault now caught with2members. Initial12member two-leaf coverage failure retained;
new13member recipe passes unchanged coverage requirement. Counts21suites/42distinct
faulttypes/27diagnostics. SourceNONE/priorPARK unchanged; no speedclaim.

## 2026-10-18 — round15 colliding SCAN interval oracle

[BOUNDARY-022](OVERNIGHT-2026-10-17/BOUNDARY-022/README.md) passes all8source/build
cells:2seeds,20models,684SCAN calls with128active growth/128active shrink calls each.
Every call checks independent scalar-reversed hash interval completeness; duplicates
legal, exact values/continuous anchors preserved. Both new faults caught. Totals now
22suites/44distinctfaulttypes;27diagnostics, all other counts unchanged. SourceNONE
and priorPARK unchanged. Separate branch census preregistered next; no speed claim.

## 2026-10-18 — round15 natural-wrap / colliding-SCAN census

[COUNTERS-008](OVERNIGHT-2026-10-17/COUNTERS-008/README.md) passes3serial whole-oracle
execution-count captures. Zero-skip branches2/4, active batch flushes2/6; collidingSCAN
records256active calls and actual displaced/multiple-tag/reach-rejection paths. Not time
profiles or speed evidence.28diagnostics;22suites/44faulttypes; sourceNONE/PARK unchanged.

## 2026-10-18 — round15 same-sized cleanup interval extension

[BOUNDARY-022 cleanup extension](OVERNIGHT-2026-10-17/BOUNDARY-022/cleanup-extension/README.md)
passes8cells,10models/432SCAN calls each. Actual64→64cleanup has56/256destination
members and5uncopied leaves; active clone and stale-position fallback pass. Equal-mask
destination-omission fault detected. Initial invalid revision precondition preserved;
new plan checks equal-before/different-after actual resize. Counts22suites/45faulttypes/
28diagnostics; sourceNONE/priorPARK unchanged. No performance claim.

Round15 final confirmation/audit: [report](OVERNIGHT-2026-10-17/ROUND-015.md),
[confirmation](OVERNIGHT-2026-10-17/ROUND-015-CONFIRMATION/README.md).48freshseed
debug-on/off cells pass, bringing this round to80passing semantic source/build cells.
1512hashes/190serial windows/16new patches and3raw branch captures audit PASS. Separate
retained-candidate audit validates256frozen files and all12patches. Counts28diagnostics/
22suites/45faulttypes, othercounts unchanged. SourceNONE/priorPARK unchanged.

## 2026-10-18 — round16 live natural-widening cursor

[BOUNDARY-023](OVERNIGHT-2026-10-17/BOUNDARY-023/README.md) passes16cells, two seeds,
three full models and16384live calls per cell, including2047mixed-width calls. Exact
interval completeness, continuous anchors, memory and clone checks pass. Both planned
faults detected; width fault classifier initially mislabeled production abort, retained
and audited without rerun.23suites/46distinctfaults; sourceNONE/existingPARK unchanged.

## 2026-10-18 — round16 mixed-width relocation and reachability

[Relocation extension](OVERNIGHT-2026-10-17/BOUNDARY-023/relocation-extension/README.md)
passes48cells: active clone-and-free, all-move and selective decline while the SCAN
cursor remains live. Exact allocation visits/releases/accounting and anchors pass. Two
faults detected, one new;23suites/47faulttypes.
[COUNTERS-009](OVERNIGHT-2026-10-17/COUNTERS-009/README.md) four fixed captures pass
actual wide/narrow ID, dual-table scan, active clone/relocation/decline reachability.
29diagnostics; no timings or sourceadoption; existingPARK unchanged.

## 2026-10-18 — round16 external mixed-width ownership

[External extension](OVERNIGHT-2026-10-17/BOUNDARY-023/external-extension/README.md)
passes48cells;3088external buffers are deep-copied or moved/declined during live natural
widening. Exact allocation accounting/visits and all cursor invariants pass. No new
suite/diagnostic/sourceadoption;23suites/47faulttypes/29diagnostics, existingPARK unchanged.

## 2026-10-18 — round16 live cursor through narrowing and renumbering

[Narrowing extension](OVERNIGHT-2026-10-17/BOUNDARY-023/narrowing-extension/README.md)
passes16cells; public bulk deletion narrows the index and compacts IDs while keeping a
nonzero SCAN cursor. All4096continuous anchors and per-call current intervals pass;
allremoved members are absent. New stale-renumbered-ID fault detected. First build type
error retained; corrected read-only cast in separate attempt002. External shallow-clone
fault detected (repeat type).23suites/48faulttypes/29diagnostics, sourceNONE/PARK unchanged.

Round16 final confirmation/audit: [report](OVERNIGHT-2026-10-17/ROUND-016.md).
64 fresh-seed debug-disabled cells pass; 192 semantic cells total. Six branch captures,
1,719 hash checks, 277 serial command windows and 11 new patches audit PASS; separate
audit checks 256 frozen files/all12 candidate patches. Six fault detections include
three new types; compiler/classifier/documentation failures retained. Counts29diagnostics/
23suites/48faulttypes; sourceNONE and priorPARK unchanged.

## 2026-10-18 — round17 score moves during mixed-width live SCAN

[BOUNDARY-024](OVERNIGHT-2026-10-17/BOUNDARY-024/README.md) passes16cells,258cross-leaf
score moves and2signed-zero updates each. Both cross-ownership directions, current
score models, intervals/anchors and memory pass. Two new deliberate fault types
detected;24suites/50faulttypes/29diagnostics. SourceNONE; existingPARK unchanged.

## 2026-10-18 — round17 external score transfers and observed paths

[External extension](OVERNIGHT-2026-10-17/BOUNDARY-024/external-extension/README.md)
passes16cells and catches omitted detach. [COUNTERS-010](OVERNIGHT-2026-10-17/COUNTERS-010/README.md)
passes2whole-oracle captures, distinguishing in-place updates, reinsertion, external
detach and three index-move branches.24suites/51faulttypes/30diagnostics; no timings,
sourceNONE and existingPARK unchanged.

## 2026-10-18 — round17 finite-tie coverage and surviving control

[Finite-ties](OVERNIGHT-2026-10-17/BOUNDARY-024/finite-ties/README.md) passes16cells
and288range counts each; planned equal-neighbor fault survives. New adjacent-tie
recipe preregistered separately; old outputs preserved. Counts24/51/30 unchanged;
sourceNONE/PARK unchanged.

## 2026-10-18 — round17 actual equal-neighbor rejection

[Neighbor extension](OVERNIGHT-2026-10-17/BOUNDARY-024/tie-neighbors/README.md) passes
16cells/336range counts each. Binary-key ordering forces two same-leaf reorders;
the previously surviving fault is detected. Old survivor retained;24suites/52faulttypes/
30diagnostics. SourceNONE/PARK unchanged; fresh-seed confirmation underway.

## 2026-10-18 — round17 batch promotion and stale-cache sensitivity

[Batch extension](OVERNIGHT-2026-10-17/BOUNDARY-024/batch-promotion/README.md) completes
initial8discovery+8fresh cells and detects deliberate stale-table heap-use-after-free.
ID1 batch lane scope mismatch retained; one-expression attempt002 adds actual alternating
ID1/2 lanes, preserves checks, passes8discovery cells and repeats detection.
24suites/53faulttypes/30diagnostics; no new source or timing acceptance.

Round17 final [report](OVERNIGHT-2026-10-17/ROUND-017.md):160passing semantic cells,
including144final-scope/72fresh cells and16retained initial batch scope-gap cells.
Corrected batch8+8cells pass.6fault detections/1survivor,5new types;4branch captures.
Audit2268hashes/286serial windows/15patches PASS;12prior candidate patches preserved.
Two audit errors retained/corrected; no experimental rerun. Counts30diagnostics/24suites/
53faulttypes; sourceNONE and allpriorPARK unchanged.

Round18 BOUNDARY-025 discovery passes8cells,18partial/all-miss promotion clones each,25models and21,864,700exact iterator/member results.25suites/53distinctfaulttypes/30diagnostics; sourceNONE/priorPARK unchanged. Freshconfirmation and sensitivity controls pending.

Round18 BOUNDARY-025 fresh8cells pass; all3promotion-specific faults detected,1new output-overrun type.16semantic cells total,25suites/54faulttypes/30diagnostics. Prior audit checks702unchanged files. SourceNONE/priorPARK unchanged. HARNESS-007 validation running.

Round18 HARNESS-007attempt002 passes1,080fixture cells,14invalid inputs and3reporting faults. Initial zero-tick/fabricated-rate failure retained, separate reporting correction frozen.7harnesses/12baselines/30diagnostics/25boundary suites/54faulttypes. SourceNONE/priorPARK unchanged. AA-012 fixed240row batch qualification starts next.

Round18 AA-012240rows+warmup complete: long-hit320/b16 and mixed16/b16 jointlyqualify; primaryhit16/b16,hit16/b1,miss16/b16 PARK. All invariants pass; no sourcecomparison yet.7harnesses/13baselines/30diagnostics/25suites/54faulttypes. SourceNONE/priorPARK unchanged. Scoped profiles of qualified subsets next.

Round18 PROFILE-004 two calibrations/eight scoped captures pass;31diagnostics. EXP-006 proposalA selected by three sequential passes/chair; three isolated inline-tag implementations frozen. Original/raw/tag/batch validation in progress. No independent agents, exactbackend/model/costunknown. SourceNONE; priorPARK unchanged.

Round18 EXP-006 completes fifth sequential two-stage population. All4sources pass43tests/raw/tag/batch bothbuilds;360screen+96freshrows retained. Cfreshprimary passesbothseeds; longguard firstseedfailsuncertainty bound; singlelane screeningregression concerning. C/PARK,sourceNONE;0accepted/2rejected/3parked.16matchedprofiles/4calibrations pass; allpatches/rootbaseline preserved.7harnesses/13baselines/31diagnostics/25suites/54boundaryfaulttypes.

[Round 18 complete](OVERNIGHT-2026-10-17/ROUND-018.md): EXP-006 C/PARK, source NONE. Fifth sequential population; 360 screening + 96 fresh rows. Fresh primary passes; long-key uncertainty and single-lane guard concerns block adoption. Totals 7 harnesses / 13 baselines / 31 diagnostics / 25 boundary suites / 54 distinct boundary fault types; 0 accepted / 2 rejected / 3 parked. All 15 candidate patches retained. Audit passes; no further trial this round.

Round19 PROFILE-005 completes8single-lane captures/4calibrations. Baseline memchr leads; C leaf lookup leads, no unbiased time-share or frequency claim.32diagnostics; sourceNONE/EXP-006C-PARK unchanged. New prefetched/nonprefetched batch-size factorial preparation underway; initial ANSI-classifier failure retained.

Round19 DIAG-019 completes576fixed rows,332validation/codegen commands; all invariants pass.0/8AA cells qualify, attenuation criterion fails discovery/freshseeds. Prefetch-removal remedy unsupported;33diagnostics. SourceNONE/EXP-006C-PARK unchanged; no retry. SUMMARY top table repaired to match prior round18 recorded totals.

Round19 BOUNDARY-026 passes32source/build/seed cells including16freshdebug-disabled; each1345keys/6models/342975batches/2743800lanes/1567343exactresults. Both lane-reuse controls detected;26suites, historical54faulttypes unchanged pending taxonomy review.33diagnostics; sourceNONE/EXP-006C-PARK unchanged. Initial missing-math.h compile failure retained.

Round19 COUNTERS-011 completes16scoped captures plus reset/dumpcontrol0/20/0. Same leaf/index/hash logical branch census acrossbatch1/16,control/C,prefetchon/off perseed; APIcallcount differsasexpected.34diagnostics; no time/frequency claim or guardrepair. SourceNONE/EXP-006C-PARK unchanged. All experiments finished; audit andhandoff next.

[Round 19 complete](OVERNIGHT-2026-10-17/ROUND-019.md): 576-row prefetch diagnostic fails fixed precision/attenuation gates; eight sampled profiles and sixteen scoped counter captures retain mechanism limits. New heterogeneous batch oracle passes32cells and two lane-reuse controls. Totals7harnesses/13baselines/34diagnostics/26boundary suites; historical54faulttypes plus2unclassified controls;5sequential populations;0accepted/2rejected/3parked. SourceNONE, EXP-006C/PARK unchanged. AuditPASS; all15patches and mainbaseline preserved. Next frozen cross-boundary compatibility matrix is preparation only.

Round20 cross-boundary extension COMPLETE:80semantic cells/48builds pass exact EXP-006control/A/B/C across partialpromotion, narrowing and3external-relocation modes; freshdebug-off confirmation included. Logicaldigests agree. No new named suite/harness/baseline/diagnostic/population; counts remain7/13/34/26 and0accepted/2rejected/3parked. Faulttransfers next; sourceNONE/C-PARK unchanged.

Round20 sensitivity transfer COMPLETE:all5existing faults on EXP-006C detected at intended boundaries (promotionUAF, last-hitmask, outside-countcanary, compactedID, clonedexternalownership). Repeated controls only; historical fault counts unchanged. Scalarfallback branch validation running; mainbaseline/sourceNONE/C-PARK unchanged.

Round20 scalarfallback COMPLETE:16semantic cells/16builds plus16preprocessing checks PASS. Exactpreprocessed code differs only in B/Chelper;1,585,152first-match and198,144guard-page checks per relevantcell agree. Deliberatezero-spanread detected. This is forcedfallback onM1, NOTbig-endianexecution. No new suite/diagnostic/faultfamily; sourceNONE/C-PARK unchanged. Densepromotion extensionrunning.

Round20 densepromotion extension COMPLETE:8control/C native/sanitizer cells, two freshseeds,36promotion cases/264lanes and68dense-hit leaf checks each;43models and over36million exact results/cell. All original ownership/SCAN/score assertions retained. No new named suite/diagnostic/population/faulttype; sourceNONE/C-PARK unchanged. All experimental children ended06:17:46UTC; auditPASS3361hashes/204serialwindows/22patches.

[Round20 completed](OVERNIGHT-2026-10-17/ROUND-020.md):104 semantic cells and six repeated
fault controls pass their scoped criteria. No new timing/population/source adoption;
counts remain7 harnesses/13 baselines/34 diagnostics/26 named boundary suites,
5 sequential populations,0 accepted/2 rejected/3 parked. Audit passes3,361 hashes,
204 serial experimental windows and22 reconstructed patches. Exact source baseline
preserved; independent review and performance guards remain pending.

Round20 final extension supersedes its104-cell checkpoint:112 semantic cells pass,
six repeated fault controls detected. Generation-wrap adds8 control/A/B/C cells with
two fresh fixed seeds; all original counts/checks retained. Final audit3960 hashes,
220 serial experimental windows,23 patch reconstructions; old469-file checkpoint
preserved. Counts unchanged7/13/34/26,5 populations,0 accepted/2 rejected/3 parked.
No timings or source adoption; final child ended06:25:59UTC. See canonical round20.

## 19 October: EXP-007 per-leaf bulk specialization completed

[EXP-007](EXP-007/RESULTS.md) completes both real three-agent population steps.
Private bulk helper B is shortlisted; fresh primary uses 33.14% less elapsed time,
aligned 8/64-bit full leaves about 43% less. Three short-range regressions repeat;
their discovery controls qualified. B fails as an all-range replacement. Experiment
PARK retains the bulk opportunity; production source NONE. Scalar iterator unchanged.
Discovery/fresh total 4320 serial processes / 557280 batches in 67.65 seconds;
eight native/sanitizer suites plus 272 boundary-base commands pass. Raw audit checks
8640 hashes and 2160 paired effects. Assembly confirms per-range dispatch and retained
outputs. Two external profiles succeed, including warm-up; no cycle attribution.
Totals: six optimization populations (five historical sequential, one multi-agent),
0 accepted / 2 rejected / 4 parked, all 18 candidate patches retained. Next distinct
experiment: scalar-short / specialized-long crossover. Overnight remains stopped.


## 19 October: EXP-008 hybrid cutoff discovery on Apple M1

[EXP-008](EXP-008/RESULTS.md) tested scalar cutoffs 4/8/16 against frozen EXP-007 B.
All eight release/sanitizer suites pass. The 15,360-process / 1,981,440-batch discovery
completed in 265.83s; independent raw audit passes 30,720 file hashes and 7,680 paired
effects. No variant meets the count16/count96 gain gates, and count16 A/A fails fixed
precision, so confirmation is skipped. The broad fallback is PARK. Count1-only remains
a falsifiable lead for a separate experiment, not an accepted optimization. These local
observations are Apple M1 only; the seven-field evidence screen says missing frequency,
turbo/SMT and actual core use prevent portable quantitative claims. [M6 replication
runbook](REPLICATE-LATEST.md) keeps host data separate. Production source is unchanged.


## 2026-10-19 — four-size sorted-set baseline (Apple M1)

[SIZE-MATRIX-001](SIZE-MATRIX-001/README.md) completes all eight standard operations
at 100/1K/10K/100K members with 16-byte keys: 96 serial processes, 768 rows and
24 observations per cell in 79.03 seconds of timing. Native and sanitizer upstream
tests (43 each), plus sanitizer benchmark coverage at all four sizes, passed.
Raw hashes and all 32 cells were reconstructed by the analysis script. Same-binary
variation exceeds 1% in at least one block in every cell; 10 cells have windows
below 10 ms. Baseline coverage is complete; no optimization or precision claim.
Plan, scripts, raw data, summaries and chart are retained. M6 rerun commands are in
[REPLICATE-LATEST.md](REPLICATE-LATEST.md); keep new host results separate.
Source and optimization/population counts are unchanged.


## 2026-10-19 — shared overnight plan and five-size extension

[NIGHT-EXPLORATION-001](NIGHT-EXPLORATION-001/README.md) is prepared for separate M1/M6
eight-hour runs: rank, update-path workloads, single-query lookup, optional single-score
decode, confirmation and final report. Both population steps, budgets, host isolation
and explicit stop/skip rules are documented. Supervisor custom prompt/host evidence
support passes six process-control tests. No overnight campaign started.
The size runner now includes 1M: 120 processes / 960 rows / 40 cells, with a separately
frozen [extension plan](SIZE-MATRIX-001/PLAN-5-SIZES.md). Original data remains intact.
[Lemire template notes](NIGHT-EXPLORATION-001/LEMIRE-NOTES.md) record inspected revisions
and concrete measurement lessons. No optimization candidate selected or adopted.


## 2026-10-19 — five-size Apple M1 baseline complete

[Five-size results](SIZE-MATRIX-001/apple-m1-five-sizes/SUMMARY.md): all eight operations
at 100/1K/10K/100K/1M, 16-byte members, 24 observations per cell; 120 processes /
960 rows / 40 cells in 351.43 seconds of timing. Native/ASan-UBSan upstream tests
passed (43 each), plus sanitizer benchmark coverage at every size. Source and raw
hashes verified. 39 cells have an A/A block outside ±1%; 11 have <10 ms windows.
These are exploratory baseline costs; no candidate or source adoption. Original
four-size data preserved. README now shows the five-size chart. Shared overnight
plan and [C benchmark review](NIGHT-EXPLORATION-001/BENCHMARK-REVIEW.md) are published;
night campaigns remain unstarted. M6 rerun instructions preserve per-host results.


## 19 October 2026 — AWS overnight launch

Three user-authorized hosts (Intel Sapphire Rapids, AMD Zen 5, ARM Neoverse V2)
passed SSH preflight; OSS coordinators stopped, five-size baselines running from
8fab511e with Clang18/CPU2. Independent release timers restore OSS at08:00UTC /
09:00Lisbon. [Live status](NIGHT-EXPLORATION-001/AWS-STATUS.md). Public Git/README/chart updates requested after
completed evidence. No new optimization decision; population counts unchanged.


## 19 October — AWS baselines complete and native workers active

All three AWS baselines pass seven native/sanitizer validation stages and raw audit:
120processes/960rows/40cells each, frozen8fab511e. Intel338.54s/27noisy cells,
AMD325.44s/30noisy cells, ARM377.83s/19noisy cells;11short cells each. Results
committed4e8edf65; five-host README chart now measured. Source adoption NONE and
optimization counts unchanged. Detached CLI workers failed bwrap uid-map setup;
original reports preserved, supervisors stopped. Native agents independently
verified SSH and continue on host branches, no permission changes. Deadline08:00UTC.


## 19 October — AWS AMD LOWERBOUND-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/865beadd/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/002-lowerbound/implementation-selection.md). Three sequential proposal passes and three isolated
implementations tested lazy packed-member metadata decoding in leaf lower-bound
search. All fail the 2% primary improvement gate at 100K and 1M. Median effects
for A/B/C are −0.434/−0.037/−1.281% at 100K and +0.441/+0.819/−0.702% at 1M.
No fresh confirmation or full performance guards were run after rejection.

Root independently reconstructed all 36 effects from 144 raw CSV processes and
verified serial windows, checksums, operation counts, seeds and owned-memory equality.
The difference from effects calculated using rounded ns/op is below 0.00015 percentage
points. All native/sanitizer and targeted semantic checks passed before timing.
The 1M A/A control remains unqualified. All three patches are retained; source NONE.

AWS measured optimization populations: **1**; **0 accepted / 1 rejected / 0 parked**.
ARM withdrew one unmeasured index-mask proposal after correcting profile attribution;
it is not counted as a completed measured population. Intel's screen is in progress.
Historical Apple counts remain separately scoped, not silently combined with these.


## 19 October — AWS Intel SIMD-LOOKUP-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b8945b4d/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup/implementation-selection.md).
Three sequential proposal passes and three isolated bounded SSE2 tag scanners were
measured against the frozen baseline. All three slow successful lookup in every
primary block: median A/B/C effects are +11.870/+9.236/+10.614% at 100K and
+9.654/+8.994/+3.891% at 1M (positive means slower). Source selection **NONE**.

Root independently audited 432 raw processes and 108 paired blocks, serial windows,
CPU2 boundaries, operation counts, seeds, checksums, fixture fingerprints and owned
memory. Native/sanitizer correctness and targeted first-match bounds checks passed.
The 1M A/A control remains unqualified; no fresh confirmation or full adoption guards
were needed after rejection. Instrumented whole-process gprof is not a scoped PMU
measurement. All three losing patches remain available on the host branch.

AWS completed measured populations: **2 — 0 accepted / 2 rejected / 0 parked**.
ARM's withdrawn, unmeasured index-mask proposal is excluded from this count.


## 19 October — AWS AMD BUILDER-WRITE-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/f3fcad103/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/004-builder-write/implementation-selection.md).
Three isolated implementations tested fixed encoding metadata while constructing a
new forward leaf. Fresh controls qualified both primaries, and native/sanitizer plus
finite-boundary, signed-zero and packed-decoder checks passed. Every measured primary
block was slower. Median A/B/C effects were +1.039/+1.250/+5.777% at100K and
+1.362/+1.745/+2.766% at1M. Both cases used one million updates per process.

Root independently reconstructed all144 raw processes and36 paired effects, verifying
serial windows, CPU2 boundaries, fixed operations/seeds, checksums and owned memory.
No fresh confirmation or full performance guards were warranted after rejection.
All three patches remain available; source selection **NONE**.

AWS completed measured populations: **3 — 0 accepted / 3 rejected / 0 parked**.
Unmeasured chair-NONE diagnostics are excluded; ARM's decoder population is ongoing.


## 19 October — AWS ARM COUNT-ONE-001: PARK / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/e4c5398b2/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/RESULT.md).
Three sequential isolated source implementations completed29-cell screens, alongside
the unchanged scalar-root adapter:2784 processes/696 paired effects. Relative to the
unadopted EXP007B bulk helper, A/B/C primary medians were−8.321/−8.263/−11.372%.
Count-eight guard medians were+1.931/+1.725/+1.804%. These are conditional private
helper observations, not whole-tree gains or strictly qualified regression claims.

Longer controls still failed both primary A/A gates; the count-eight bulk control
also narrowly failed. Its final unrelated guard block stopped at the fixed budget,
leaving three uninterpreted rows. All candidate linked text sections match, so their
sampled differences cannot select an implementation. Native/sanitizer checks passed;
full176-cell guards, fresh confirmation and candidate profile validation were not run.
Root independently audited4175 raw CSVs (1391 longer-control+2784 comparison rows),
including hashes, serial windows, CPU2 boundaries, fixture outputs and fixture bytes.
Source adoption and implementation winner remain **NONE**.


## 19 October — AWS AMD FULL-CHUNKS-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b02b79b30/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/005-full-chunks/implementation-selection.md).
Three sequential isolated implementations separated full64-bit packed-move chunks
from the partial tail. Correctness and both fresh primary A/A controls passed, but
no measured primary block reached2% improvement. Median A/B/C effects were
−0.609/+0.265/−0.824% at100K and+0.380/+0.403/+0.854% at1M.
Root independently reconstructed144 raw processes/36 effects and verified serial
CPU2 runs, exact operations/seeds, checksums and owned-byte equality. No full guards
or fresh confirmation were warranted. All patches remain available; source **NONE**.

AWS completed measured populations: **5 — 0 accepted / 4 rejected / 1 parked**.
Intel's iterator population is ongoing. Unmeasured chair-NONE diagnostics are excluded.


## 19 October — AWS Intel ITERATOR-CACHE-001: PARK / NONE

The fixed exploratory screen completed566/576 processes,141 complete ABBA blocks
and two trailing rows before its300-second ceiling. No extension or repaired timing
schedule followed. Pointer-cache A and32-bit-offset B show conditional primary leads:
100K medians−7.574/−6.023%,1M−6.559/−4.643%. The100K primary A/A fails; fractional
guards have noisy slowdowns, and the last1M block is incomplete for all variants.
16-bit-offset C is observed slower in forward/full and score-only cases. No winner.
A increases64-bit iterator state16→24 bytes; B/C remain16. Tree-owned bytes match.

All original43 tests pass per source/native-sanitizer build, plus1,920 iterator
fixtures/source and28,192 pre-screen state checks/build. A separate additive oracle
passes89,428 total checks/build, including direction toggles and mutation followed
by explicit reinitialization. Two missing-reset fault controls are detected. Root
independently reconstructs192 A/A and566 comparison rows, verifies the exact frozen
schedule prefix, hashes, serial windows, CPU2, fixture/checksum and owned-byte parity.
Full performance guards, fresh independent confirmation and acceptance review remain
pending. ARM is separately profiling exact retained A/B patches for possible native
replication; its measurements cannot repair this Intel schedule. Source remains NONE.

AWS completed measured populations: **6 — 0 accepted / 4 rejected / 2 parked**.
Unmeasured diagnostics and architecture replications are not new implementation
populations. Decision: Intel branch `f320d3f67`.


## 19 October — ARM iterator architecture replication: PARK / NONE

Exact Intel iterator A/B patches completed independent ARM screens: 192 A/A plus
192 processes per candidate, 576 total and 144 complete ABBA blocks. Both primary
controls fail (100K −2.523..+1.985%; 1M −3.997..+0.735%), so favorable observations
remain conditional. Primary medians for A/B are −10.812/−12.623% at 100K and
−7.446/−9.631% at 1M. There is no qualified A-versus-B ranking. A uses 24-byte
iterator state and B 16 bytes on this host; tree-owned bytes are identical.

Root independently reconstructed every raw row and effect, checked the full seal,
exact frozen schedules, serial windows, CPU2, fixture/checksum and memory parity.
A fresh read-only SSH check confirms the baseline/A/B binaries still match the
pre-screen hash manifest. Original tests and additive state checks pass. Broader
guards, fresh confirmation and candidate profiles remain absent. Source NONE.

This is one parked architecture replication of an existing population. Completed
AWS population counts stay **6 — 0 accepted / 4 rejected / 2 parked**, plus
**1 parked architecture replication**. Intel and ARM timings are not pooled.
Result pin: ARM `ca5ffa2a8`; independent audit is
`reviews/aws-arm-iterator-cache-raw-audit.json` in the night campaign.


## 19 October — AWS AMD SCAN-TAGS-001: PARK / NONE

Three actual agents separately authored proposals and isolated implementations,
with a fourth agent chairing and reviewing. The selected hypothesis replaces the
all-match leaf-tag loop with exact bounded SSE2 masks and retains a portable
fallback. All three patches remain immutable. Native/sanitizer, exact-position,
scan/resize/widen and fallback checks pass; all eight deliberate faults are caught.

The fixed 144-process screen completes all 36 ABBA effects. A/B show roughly
5.25/4.28% lower elapsed time at 100K and 4.36/4.30% at 1M, meeting the 2% gate in
every block. C misses the every-block 1M gate. Fresh 1M A/A fails, so no qualified
implementation winner follows. One alphabetical-priority A profile finds about
12% fewer instructions/branches but under 1% lower cycles, which does not validate
the 4–5% exploratory elapsed magnitude. Dense/folded/reversed/resize performance
guards remain missing. Decision PARK; source NONE.

Root independently reconstructs all 48 A/A and 144 comparison rows, verifies the
exact schedules, serial CPU2 windows, requested work, actual callback counts,
checksums and owned bytes. Effects reconstructed from integer elapsed times differ
from the worker's rounded ns/op calculation by at most 0.000654 percentage points.
Decision/profile pin: AMD `9f96d0518`; independent audit in the night campaign is
`reviews/aws-amd-scan-raw-audit.json`.

AWS completed populations: **7 — 0 accepted / 4 rejected / 3 parked**, plus
**1 parked ARM architecture replication**. Intel's separately preregistered scan
controls qualify and exact A/B replication is preparing; those measurements cannot
repair AMD's failed control. Full guards, fresh confirmation, profile validation
and final review remain mandatory before any acceptance recommendation.


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
[Chair and participant evidence](NIGHT-EXPLORATION-001/reviews/aws-amd-delete-population/selection.md).


## 19 October 04:01 UTC — Native ARM scan chair selects NONE

All three actual independent proposals identify bounded native-vector all-match
comparison as plausible, conditional on qualification. Fresh5M-op controls fail
first1M block at+1.889270895%;100K qualifies. Root independently verified48 raw rows,
12 blocks and107 sealed files, exactsource/referee/driver hashes, serialCPU2, callbacks,
checksums and owned memory. NONE before implementation: no retry or failed-row removal.
All proposals/profile/controls remain. No candidate or new measured population.
[Chair](NIGHT-EXPLORATION-001/reviews/aws-arm-native-scan-population/selection.md),
[raw audit](NIGHT-EXPLORATION-001/reviews/aws-arm-native-scan-aa-audit.json).
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
[Root audit](NIGHT-EXPLORATION-001/reviews/aws-intel-scan-confirmation-raw-audit.json).

This closes only the fresh independent primary-confirmation gate. Full original
controls qualify57/80; diagnostic full B guards, focused guards and matched profiles
remain. **PARK/source NONE**, not acceptance or a portable/full-suite speedup.
Measured population counts remain7 (0 accepted/4 rejected/3 parked).


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
[Audit summary](NIGHT-EXPLORATION-001/reviews/aws-intel-original-guards-independent-summary.json).
Measured AWS populations remain7:0 accepted/4 rejected/3 parked; no new population.


## 19 October 04:42 UTC — Profile, portability and corrected-baseline checkpoints

Independent review5bffe4d28 reconstructs all120 matched Intel captures. Helper
samples base→B are337→316 at100K and419→316 at1M, with matched callback denominators.
The21-sample100K gap is coarse;1M is directionally stronger. SSE2 codegen is present,
but these are captured-text samples from diagnostic layouts, not exact cycles or
a quantitative explanation of elapsed gains. All24 diagnostic and22 original
post-phase hashes match. The24 unresolved original guards still prevent adoption.
[Independent profile summary](NIGHT-EXPLORATION-001/reviews/aws-intel-matched-profile-independent-summary.json).

Exact B also passes native ARM original43 tests and V2 oracle299664 checks in both
release and ASan/UBSan through the natural portable fallback. Root verified the
24-file seal, exact source identity and14.2-second bounded CPU2 job. This is
correctness only, not performance qualification or big-endian coverage.
[Portability review](NIGHT-EXPLORATION-001/reviews/aws-selected-b-native-arm-review.json).

Separate corrected-adapter baselines on13e459ff8 now complete on AMD and ARM. Root
independently reconstructs120 processes/960 rows/240 blocks per host, exact schedules,
raw hashes, source/runner identities, validation commands, paired memory and summaries.
AMD qualifies11/40:11short plus18other noisy cells. ARM qualifies21/40:11short plus
8other noisy cells. All seven native/sanitizer stages pass on each host. M6's separate
corrected baseline also audits successfully with5/40 qualified; Intel remains queued.
[AMD raw audit](NIGHT-EXPLORATION-001/reviews/corrected-aws-amd-baseline-audit.json),
[ARM raw audit](NIGHT-EXPLORATION-001/reviews/corrected-aws-arm-baseline-audit.json).

AMD and ARM will reassess scan only under the corrected identity, starting with
separately frozen baseline profiles and48-row A/A controls at5M requested operations,
100K/1M members and seeds401–403 twice. No candidate timing is yet authorized.
Failed controls stop that new comparison without retry. These new harness results
do not repair or replace any original8fab511e decision. Source NONE; measured
AWS population counts remain7:0 accepted/4 rejected/3 parked.


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
measured. [Chair and proposals](NIGHT-EXPLORATION-001/reviews/aws-arm-corrected-scan-population/selection.md).
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
[Independent audit](NIGHT-EXPLORATION-001/reviews/aws-amd-corrected-B-independent-audit.json).

All three corrected ARM NEON implementations are sealed independently: A=a223b96b1,
B=9b2456c01,C=3b137666b. Root static review finds no blocker and exhaustively verifies
65,536 lane-match patterns for each of the two reduction methods. Native correctness,
codegen and timing remain pending. Frozen maintenance scores A28/B26/C26 give B,C,A
preference only among implementations passing every primary block, not a speed ranking.
[Review and retained patches](NIGHT-EXPLORATION-001/reviews/aws-arm-corrected-scan-population/implementation-static-review.md).

Intel focused A/A completes864 rows/216 blocks,22/36 qualified cells,14 precision
failures and no short windows. Root independently checks immutable c5a734191 raw data,
all36 retained fixture hashes, frozen schedules, serialCPU2, semantic/memory parity and
24 post-phase source/referee/binary identities. Full fixed candidate comparison continues,
retaining all failed-control cells. No new accepted source; completed AWS populations
remain7 (0 accepted/4 rejected/3 parked), plus separate replications.
[Focused control audit](NIGHT-EXPLORATION-001/reviews/aws-intel-focused-aa-independent-audit.json).


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
[Native review and grant](NIGHT-EXPLORATION-001/reviews/aws-arm-corrected-scan-population/native-validation-review.json).
Completed population counts remain seven until this round is measured.

The independent full Intel focused audit223d6d7de reconstructs 2,052 processes and
432 paired effects: all 22 qualified guard cases pass; 14 noisy controls remain
unresolved. Across all candidate blocks, changes range from−24.951% to+0.260%, but
unqualified rows remain exploratory. Original 24 guard gaps still block adoption.
[Independent summary](NIGHT-EXPLORATION-001/reviews/aws-intel-focused-independent-summary.json).

AMD's separate corrected rank/update profile survey4ed690fd1 completes 74 commands
and 12 scoped captures with matched controls and actual timing-binary mapping.
Sampled instruction locations identify index probing/ID stores as diagnostic topics;
load/store adjacency and sampling skid prevent calling their arithmetic removable.
No new hypothesis is selected. Intel's corrected baseline runs before its frozen
supplemental guards; a distinct corrected SCAN profile/control plan is queued later.

The05:08 live release preflight verifies all three coordinators remain stopped,
all host timers still target08:00UTC/09:00Lisbon, and cgroup inspection reports no
errors. This is not release proof; the final live auditor remains scheduled08:00:20.
[Sanitized preflight](NIGHT-EXPLORATION-001/reviews/aws-release-preflight-0508.json).
