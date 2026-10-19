# Experiment summary

## Latest: EXP-008 short-range crossover, 19 October (Apple M1)

[Raw-audited results](EXP-008/RESULTS.md): no cutoff qualifies; count16/count96 gains
fail and count16 A/A precision is insufficient. Broader scalar thresholds show large
short-range losses. A count1-only path is the next narrow hypothesis, pending a separate
experiment. 15,360 processes / 1,981,440 batches; raw audit and native/sanitizer checks
pass. No confirmation or source adoption. [M6 replication guide](REPLICATE-LATEST.md).

## Earlier: EXP-007 bulk specialization, 19 October

[Fresh results](EXP-007/RESULTS.md): B reduces primary full-leaf elapsed time by
33.14% and aligned 8/64-bit full leaves by about 43%. Qualified short-range losses
block universal adoption; experiment PARK / source NONE. Native/sanitizer checks and
raw audits pass; both real three-agent population steps and cross-author reviews
are complete.
No scalar iterator gain is claimed. Current optimization totals are 0 accepted /
2 rejected / 5 parked across seven populations; all 21 patches are retained.

## Earlier: focused decoder benchmark, 19 October

The [new decoder harness and results](EXP-004/decoder-microbench-2026-10-19/README.md)
are ready. One new harness/diagnostic follows the overnight totals below. A fixed
12.58-second matrix found EXP-004 A slower for aligned 8-bit and 64-bit scores;
this limits the generality of the earlier iterator gains. Release/sanitizer checks
and raw-data audit pass. No source adoption; at that checkpoint the optimization totals
were 0 accepted / 2 rejected / 3 parked. Overnight execution remains stopped.

| Category | Count |
|---|---:|
| Preparation completed | 1 |
| Harnesses locally validated (7 overnight + 2 focused decoder referees + EXP-008) | 10 |
| Historical overnight baseline explorations | 13 |
| Post-overnight focused A/A campaigns (decoder + two bulk campaigns) | 4 |
| Optimisations accepted / rejected / parked | 0 / 2 / 5 |
| Population rounds executed | 7 (5 sequential fallback + 2 multi-agent) |
| Historical overnight additional measurement diagnostics | 34 |
| Post-overnight focused decoder investigations | 3 |
| Additional boundary oracle suites validated | 26 |

The initial standalone library, direct API harness and upstream test entry point are ready.
See [PREP-001](PREP-001/README.md) for validation and remaining coverage.
The [local M1 exploration](EXP-001/local-m1-2026-10-17/README.md) completed 144 processes,
984 measured rows and four profiles. Only one workload cell meets the local precision
gate; suite qualification is parked. No speedup claims or selected candidates.

[HARNESS-001](OVERNIGHT-2026-10-17/HARNESS-001/README.md) adds traversal duration and
scheduling observations; correctness and ASan/UBSan passed. Three targeted
requalification runs are complete; lookup precision remains unresolved.

[AA-001](OVERNIGHT-2026-10-17/AA-001/README.md): 192 new observations, 2/8 traversal
cells qualified, lookup/rank/update parked. New scan profiling denied; no population
or candidate selected. Separate harness revision remains uncommitted due sandbox.

[DIAG-001](OVERNIGHT-2026-10-17/DIAG-001/README.md) completed 72 checked windows;
process/fixture reuse did not meet its fixed variance-reduction criterion.

The first two boundary oracle suites pass release/debug and ASan/UBSan. Three scoped Clang
execution-count profiles validate code-path coverage; time-profile validation remains
open. No independent agents ran and no optimisation population was executed.

[AA-002](OVERNIGHT-2026-10-17/AA-002/README.md): 96 larger-fixture rows; only rank16
qualifies. Lookup comparisons PARK, no matching rank time profile, selection NONE.

[BOUNDARY-003](OVERNIGHT-2026-10-17/BOUNDARY-003/README.md) adds natural wide-ID coverage;
two seeds pass release/debug + sanitizers and two intentional faults are detected.

[DIAG-002](OVERNIGHT-2026-10-17/DIAG-002/README.md): adjacent dependent-add brackets
do not meet the fixed lookup-variation association criterion; clock remains unknown.

[BOUNDARY-004](OVERNIGHT-2026-10-17/BOUNDARY-004/README.md) validates standalone
relocation ownership/accounting, four fixtures in release/debug and ASan/UBSan;
two intentional faults detected. All source optimisation counts remain zero.

[DIAG-003](OVERNIGHT-2026-10-17/DIAG-003/README.md):24 fixed windows with matched
access-array footprints; repeated-order advantage criterion not met. Lookup PARK,
source NONE; no access-history remedy or causal cache inference.

[BOUNDARY-005](OVERNIGHT-2026-10-17/BOUNDARY-005/README.md): controlled bucket
wraparound, tombstone reuse, tag-mask false candidates and insertion revision coverage
pass both builds; two intentional faults detected. Initial fixture failures retained.

[BOUNDARY-006](OVERNIGHT-2026-10-17/BOUNDARY-006/README.md):48 bulk-delete boundary
cases pass both builds, including24 active resizes; two semantic faults detected.

[DIAG-004](OVERNIGHT-2026-10-17/DIAG-004/README.md):48 fixed construction-history
rows; ascending advantage hypothesis fails. Contrary local pattern motivates fresh
independent-query-order coverage; no source or causal claim.

[DIAG-005](OVERNIGHT-2026-10-17/DIAG-005/README.md):48 fresh-seed factorial rows
support a local construction/query-order interaction. Independent query coverage
is warranted; no causal mechanism, noise remedy or source acceptance established.

[COUNTERS-002](OVERNIGHT-2026-10-17/COUNTERS-002/README.md):four scoped captures
validate identical aggregate tree function/region/branch counts between query orders
within construction arm. Execution-frequency control only, not time profiling.

[HARNESS-002](OVERNIGHT-2026-10-17/HARNESS-002/README.md): independent query seed/order
validated in an isolated snapshot; AA-003 preregistered, qualification pending.

[AA-003](OVERNIGHT-2026-10-17/AA-003/README.md):96 independent-query rows,0/4 qualify;
lookup PARK, source NONE. No claim that decoupling cures measurement noise.

[PROFILE-002](OVERNIGHT-2026-10-17/PROFILE-002/README.md):12 scoped self-process
profiles and two calibrations succeed; coarse symbol evidence, no source win.

[BOUNDARY-007](OVERNIGHT-2026-10-17/BOUNDARY-007/README.md):equal-score lexical
bounds and optional iterator output masks pass both builds; two faults detected.

[BOUNDARY-008](OVERNIGHT-2026-10-17/BOUNDARY-008/README.md):append-batch buffer
ownership, count/byte flush and active-resize coverage pass; two faults detected.

[DIAG-006](OVERNIGHT-2026-10-17/DIAG-006/README.md):48 sampler off/on rows satisfy
the fixed diagnostic bound, without resolving source qualification or sampling bias.

[DIAG-007](OVERNIGHT-2026-10-17/DIAG-007/README.md):384 fixed contiguous windows;
early/late phase hypothesis unsupported overall, all controls pass. No noise remedy.

[BOUNDARY-009](OVERNIGHT-2026-10-17/BOUNDARY-009/README.md): exhaustive batched-score
masks, output bounds, exact scores and resize coverage pass both builds; two faults caught.

[DIAG-008](OVERNIGHT-2026-10-17/DIAG-008/README.md):768 windows support primary
miss-warmup phase intervention; separate harness revision/fresh A/A still required.

[HARNESS-003](OVERNIGHT-2026-10-17/HARNESS-003/README.md): isolated miss warmup
validated; fresh AA-004 qualification preregistered.

[AA-004](OVERNIGHT-2026-10-17/AA-004/README.md):96 miss-warmup A/A rows,0/4 qualify;
lookup PARK/source NONE. Phase improvement does not establish comparison precision.

[BOUNDARY-010](OVERNIGHT-2026-10-17/BOUNDARY-010/README.md): raw input guards, binary
length/ownership and exact scores pass both builds; two faults detected, first build
failure retained.

[DIAG-009](OVERNIGHT-2026-10-17/DIAG-009/README.md):18 known-function runs pass
calibration; rate-equivalence hypothesis unsupported, corrected helper interface saved.

[DIAG-010](OVERNIGHT-2026-10-17/DIAG-010/README.md):96 serial requested-QoS rows,
all controls pass; primary repeatability hypothesis unsupported. No new A/A remedy.

[BOUNDARY-011](OVERNIGHT-2026-10-17/BOUNDARY-011/README.md):12 clone fixtures/build,
active-resize/free-ID state, exact contents and disjoint allocation ownership pass.
Two faults caught; fault-driver message mismatch retained and audited.

[PROFILE-003](OVERNIGHT-2026-10-17/PROFILE-003/README.md):12 traversal captures and
two calibrations pass; descriptive scan/iterator hot-symbol coverage.

[AA-005](OVERNIGHT-2026-10-17/AA-005/README.md):96 fresh traversal rows;2/4 qualify
(forward iterate16/320), both scans PARK. EXP-002 sequential populations in progress.

[EXP-002](EXP-002/README.md): both population stages completed as sequential passes;
three isolated iterator variants pass correctness/screening, C selected;24 fresh-seed
confirmation rows and four matched profiles pass. PARK for reverse/output-mode guards,
independent confirmation/review and committed provenance. Main baseline preserved.

[HARNESS-004](OVERNIGHT-2026-10-17/HARNESS-004/README.md):640 iterator fixture cells/build
and original tests pass release/sanitizers;three referee faults detected. AA-006 pending.

[AA-006](OVERNIGHT-2026-10-17/AA-006/README.md):336 fixed rows,10/14 iterator modes
qualify. Mixed-output masks2,3,5,6 remain PARK;all invariants pass.

[EXP-002 expanded guards](EXP-002/guard-extension/README.md) supersede provisional C:
504 discovery+216 fresh rows confirm regressions for all3 implementations;REJECT/NONE.
Eight matched profiles/two calibrations pass;main source stays baseline.

[BOUNDARY-012](OVERNIGHT-2026-10-17/BOUNDARY-012/README.md):dynamic masks/nonboolean
reverse/iterator copies after mixed edits pass all4 source variants,both builds;two faults caught.

[EXP-003](EXP-003/README.md):member-decoder outlining completes both sequential populations;
504screen+216fresh rows confirm all3 full-output regressions. REJECT/NONE.12profiles/2calibrations
and correctness/sanitizers pass;root baseline preserved.

[COUNTERS-003](OVERNIGHT-2026-10-17/COUNTERS-003/README.md) completes the packed-layout census;320 valid child runs,retained allocator cross-build driver assertion. No speed claim.

[BOUNDARY-013](OVERNIGHT-2026-10-17/BOUNDARY-013/README.md) adds exhaustive packed-reader geometry and two detected faults;13suites/26faults total.

[AA-007](OVERNIGHT-2026-10-17/AA-007/README.md):6/10cells qualify on240current-round rows;four newly parked modes are not eligible guards.

[EXP-004](EXP-004/implementation-selection.md) provisionally selects A/PARK;new long-duration guard qualification pending. No accepted optimisation.

[AA-008](OVERNIGHT-2026-10-17/AA-008/README.md) fails joint longer-duration qualification;long guard comparisons skipped,EXP-004 stays A/PARK.

[DIAG-011](OVERNIGHT-2026-10-17/DIAG-011/README.md) fails the two-seed caller interaction criterion;compiler already unswitches mask6 tests. No referee replacement or candidate acceptance.

[BOUNDARY-014](OVERNIGHT-2026-10-17/BOUNDARY-014/README.md): exact zero signs through
real physical-order mutations pass control/all retained variants/both builds;two faults
detected.14suites/28faults;first test precondition failure retained.

[DIAG-012](OVERNIGHT-2026-10-17/DIAG-012/README.md):controllediteratorplacement criterion
unsupported;480rows+4warmups,1028validationruns pass. Original guard remains PARK.

[AA-009](OVERNIGHT-2026-10-17/AA-009/README.md):72rowsqualify3/3current masks0/4/7;
otherguardqualificationunchanged. EXP-005validates1096commands before screening.

[EXP-005](EXP-005/README.md):PARK/NONE;Cscreeningpreference failsfreshprimarybound.
1096validationcommands,396comparisonrows,12profiles/2calibrations;allpatches retained.

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

[COUNTERS-006](OVERNIGHT-2026-10-17/COUNTERS-006/README.md): twelve allocator/build
factorial cells pass all semantic checks. Fixed capacity removes build differences;
capacity intervention changes orientation counters. Structural hypothesis supported;
source NONE, no timing claim. Root baseline preserved.

[HARNESS-006](OVERNIGHT-2026-10-17/HARNESS-006/README.md) validates compact deletion,
clone and refill histories:2,560fixturecells/build,originaltests,invalid-input checks,
three detected faults. Sixth isolated referee;AA-011 preregistered next.

[AA-011](OVERNIGHT-2026-10-17/AA-011/README.md):384rows,oneofeightcompactguards
qualifiesonbothseeds. Originalstale-countanalysis retained;correctedanalysis follows
preregisteredroundingrule. Sevencompactguards PARK. Twelfthbaseline;sourceunchanged.

[EXP-004 compact guard](EXP-004/compact-guards/README.md):A/B passnewguardbothfreshseeds,
C inconclusiveonone;A/PARK unchanged.144rows+4warmups,1770validationcommands,12profiles/
2calibrations. No newpopulation,primarysubstitution or sourceadoption.

[DIAG-013](OVERNIGHT-2026-10-17/DIAG-013/README.md):192compactwarmupdiagnosticrows,
allinvariants pass;fixedremedycriterionunsupported. No policy/sourcequalification.

[Round 11](OVERNIGHT-2026-10-17/ROUND-011.md) complete:720timingrows,26profiles/6calibrations,
capacityfactorial and16fresh-source correctnesscells. Audit758serialwindows/72intervals
passes. Sixharnesses/12baselines/21diagnostics;optimizationcountsunchanged.

[BOUNDARY-015](OVERNIGHT-2026-10-17/BOUNDARY-015/README.md): mixed finite-score mutation
oracle passes all24 capacity/source/build cells and original tests; two new faults
detected. Initial SCAN precondition error retained and documented. Source NONE.

[DIAG-014](OVERNIGHT-2026-10-17/DIAG-014/README.md): predecessor-workload discovery
criterion supported forzero-trim-f6;192rows+warmup,allinvariants pass. Freshmirrored
confirmation/placebo preregistered. No source or qualification claim.

DIAG-014 freshmirroredconfirmation reproducesbothseedcontrasts butoneplacebointerval
failsprecision. JointconfirmationPARK;no noise policy orguardrepair. Countsunchanged.

[BOUNDARY-016](OVERNIGHT-2026-10-17/BOUNDARY-016/README.md): all8cells pass146,250
packedmovementoperations each;bothnewfaultsdetected,completebufferdigestsmatch.

[DIAG-015](OVERNIGHT-2026-10-17/DIAG-015/README.md): all 288 rows plus warmup complete;
fixed idle-gap attenuation criterion unsupported. No timing policy adopted.

## Round 12 final reconciliation

[Round 12](OVERNIGHT-2026-10-17/ROUND-012.md) adds two boundary suites and two process
history diagnostics. BOUNDARY-015/016 pass all cells and four new fault controls.
DIAG-014's fresh contrast reproduces, but placebo failure leaves robustness PARK;
DIAG-015's idle-gap criterion is unsupported. No timing policy or source adoption.
Audit passes 675 serial measurement windows, 122 disjoint validation windows and
32 independently recomputed wall/thread intervals. Totals in the table are current.

[DIAG-016](OVERNIGHT-2026-10-17/DIAG-016/README.md):384 rows plus warmup pass controls.
Buffered bookkeeping reduces coordinator CPU but fails the fixed attenuation criterion;
unsupported, no policy adopted. Source NONE and existing PARK decisions unchanged.

[DIAG-017](OVERNIGHT-2026-10-17/DIAG-017/README.md):384 rows plus warmup; transport
controls pass, but pipe contrast/placebo bounds fail the fixed attenuation criterion.
Unsupported; no policy adoption or source guard repair.

[BOUNDARY-017](OVERNIGHT-2026-10-17/BOUNDARY-017/README.md) and
[BOUNDARY-018](OVERNIGHT-2026-10-17/BOUNDARY-018/README.md) pass all8source/buildcells
each, plus4new faults. Exhaustivecompactindexstorage andleafIDregistrycoverage added.
InitialallocatorAPIcompilefailure retained;36distinctboundaryfaulttypes,sourceNONE.

[DIAG-018](OVERNIGHT-2026-10-17/DIAG-018/README.md):48 discovery and48freshmirrored
rows plus2warmups support observed completion delay locally. Six transport/status/
timeoutcontrols pass. Not a precision remedy or sourceguard; no policyadopted.

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

[BOUNDARY-023](OVERNIGHT-2026-10-17/BOUNDARY-023/README.md):16passing cells carry a live
SCAN cursor through natural narrow→wide migration; independent per-call intervals and
continuous anchors pass. Two faults detected (one new); initial classifier mismatch
retained/read-only audited.23suites/46distinct faults; sourceNONE/existingPARK unchanged.

[Mixed-width relocation](OVERNIGHT-2026-10-17/BOUNDARY-023/relocation-extension/README.md)
passes48cells and two faults (one new);23suites/47faulttypes.
[COUNTERS-009](OVERNIGHT-2026-10-17/COUNTERS-009/README.md) four whole-oracle captures
confirm actual wide/narrow/clone/relocation branches;29diagnostics, no timings. SourceNONE/PARK unchanged.

[External mixed-width extension](OVERNIGHT-2026-10-17/BOUNDARY-023/external-extension/README.md):
48cells pass exact external ownership, relocation/decline and continuing cursor checks.
Counts/sourceNONE/existingPARK unchanged.

[Live narrowing extension](OVERNIGHT-2026-10-17/BOUNDARY-023/narrowing-extension/README.md):
16cells pass cursor continuation through bulk deletion/dense IDs/narrow table; new fault
detected. Initial void-pointer compile failure retained, separate cast-only correction.
23suites/48faulttypes/29diagnostics; sourceNONE/PARK unchanged.

[Round16 completed](OVERNIGHT-2026-10-17/ROUND-016.md): 192 semantic cells including
64 fresh-seed debug-disabled confirmations; six branch captures. All raw/hash/patch/
serial/source checks pass; initial failures retained.29diagnostics/23suites/48faulttypes;
no source adoption or timing claim.

[BOUNDARY-024](OVERNIGHT-2026-10-17/BOUNDARY-024/README.md):16cells pass live mixed-width
score moves with independent current-score order, exact signed-zero values, intervals
and anchors. Both new faults detected.24suites/50faulttypes; sourceNONE/PARK unchanged.

[External score extension](OVERNIGHT-2026-10-17/BOUNDARY-024/external-extension/README.md)
passes16cells and new detach fault; [COUNTERS-010](OVERNIGHT-2026-10-17/COUNTERS-010/README.md)
confirms actual transfer/index branches.24suites/51faulttypes/30diagnostics; no speedclaim.

[Finite-ties](OVERNIGHT-2026-10-17/BOUNDARY-024/finite-ties/README.md) passes16cells;
equal-neighbor fault survives and is retained. No new fault type or source adoption.

[Neighbor extension](OVERNIGHT-2026-10-17/BOUNDARY-024/tie-neighbors/README.md) forces
the missing in-place tie-rejection coverage;16cells pass and prior fault is caught.
24suites/52faulttypes/30diagnostics; original survivor preserved, sourceNONE/PARK unchanged.

[Batch promotion](OVERNIGHT-2026-10-17/BOUNDARY-024/batch-promotion/README.md) catches
a deliberate stale-table cache after actual width promotion. Initial ID1 input-scope
gap retained; corrected attempt separately frozen.24suites/53faulttypes/30diagnostics.

[Round17](OVERNIGHT-2026-10-17/ROUND-017.md) completes144final-scope semantic cells
(72fresh), retains16initial batch scope-gap cells, and audits2268hashes/286serial
windows/15new patches.6fault detections/1survivor,5new types;4branch captures. All12
candidate patches retained.30diagnostics/24suites/53faulttypes; sourceNONE/PARK unchanged.

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
