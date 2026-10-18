# Round18 — partial promotion coverage and inline tag-search experiment

**Source adoption NONE. EXP-006 is C/PARK.** EXP-004A/PARK and EXP-005PARK/NONE
remain. Main source/header, root referee, adapter and original test entry retain
their hashes. The new experimental preference is kept only in isolated snapshots.

Round deadline05:39:21UTC; handoff cutoff05:37:51UTC. Experimental children finished
before05:33UTC. This is not the campaign's final round; final worker owes the morning
report before07:00UTC /08:00Lisbon.

## Completed work

[BOUNDARY-025](BOUNDARY-025/README.md) passes16source/build/seed cells, including8fresh
confirmations with debug-only assertions omitted. Each cell exercises18active-resize
clones covering counts1/2/3/7/15/16 and all-hit/all-miss/alternating layouts; count1
alternating is a hit. Every batch enters narrow/wide migration and exits promoted.
Exact hit masks, hit scores, outside-count canaries, null count0, independent sorted
models, clone ownership and tree-owned usable-byte sums pass. Original liveSCAN and
260external-pointer score-transfer checks remain. Private state is only observed.

Each cell checks25models and21,864,700iterator/member results. Full lookup/rank checks
are delayed until after transition; ranks remain sampled. Entry with count-1uncopied
leaves plus inspected one-step-per-lookup code predicts last-lane completion. Precise
internal lane is not separately instrumented. Three promotion-specific faults are
caught: stale-table cache, omitted final hit, and outside-count output write. Only the
last adds a new distinct boundary fault family. No production defect was discovered.

[HARNESS-007](HARNESS-007/README.md) adds an isolated steady-state public batched lookup
benchmark with independent query shuffle, accurate partial-batch/API-call/hit counts,
checksums, memory guard, wall/thread time, boundary CPUs and reported QoS. Timed scope
includes batch assembly, exact masks and checksum consumption. Root referee unchanged.
Attempt002 passes1,080fixture cells,14invalid-input checks and3reporting faults.

The first validator caught elapsed_ns0 for a one-operation fixture with a fabricated
rate from a1nsfallback. All original source/output/failure evidence is retained.
A separately frozen correction reports elapsed_zero1 and rate0 as unavailable.
All semantic and positive-duration checks remain, as does A/A's10ms minimum window.
Initial manifest status running means its assertion stopped the driver, not an active child.

[AA-012](AA-012/README.md) completes240fixed rows plus retained prospective warmup.
Long-hit320/batch16 and mixed16/batch16 qualify on both seeds. Preregistered primary
short-hit/batch16, short-hit/batch1 and miss/batch16 PARK. Every invariant and duration
check passes. SixABBA blocks/cell/seed, wall metric primary, all raw rows retained.
Qualified subsets do not replace any original or additional unqualified guard.

[PROFILE-004](PROFILE-004/README.md) passes2calibrations and8scoped captures. Memchr
leads mixed short batches; SipHash leads long hits. This supports a new hypothesis
population, not a speed claim. Requested intervals are not measured effective cadence.

## EXP-006 population and decision

[EXP-006](../EXP-006/README.md) completes both population stages as three separate
sequential proposal passes/chair and three isolated implementation passes. Agent startup
failed; these were not independent agents. Chair selected bounded inline leaf tag search,
parking query prefetch and rejecting unmeasured length-filtering for current fixtures.

Abytewise, B8-byte word search and C16-byte unrolling share exact source/referee/flags/
allocator. All four sources pass original43tests, raw guard pages,1,585,152first-match
checks and36batch fixtures per native/sanitizer build. Added protected-page regression
validation passes198,144tag checks/build/source and detects a deliberate overread.
This regression addition is part ofEXP-006, not another named boundary campaign.

360serial screening rows find no implementation passing both declared gates. Aregresses;
B/Cshow exploratory primary gains. The predeclared rule choosesC for fresh falsification.
96fresh confirmation rows show primary benefit bounds pass bothseeds, but one long-key
guard uncertainty bound fails. **C/PARK; sourceNONE.** The single-lane screening guard
also shows concerning regressions on bothseeds, though its A/A failed. This concern
must be resolved before adoption; it cannot be dismissed because primary improved.

[Selection](../EXP-006/implementation-selection.md) retains raw-derived intervals,
per-member rates and exact owned bytes, including the large long-key block contrasts.
No outlier removed, threshold changed, count extended or original guard substituted.
Matched8candidate captures plus two new calibrationcontrols pass; memchr attribution
disappears and leaf lookup work remains. Assembly confirms all3candidate leaf searches
remove the call. These establish code transformation, not unbiased time shares or
stable frequency. No PMU evidence; guard behavior is not fully explained.

## Verification and evidence

Principal commands (all exact compiler/child commands are recorded in linked manifests):

```sh
python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-025/run.py
python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-025/confirmation/run.py
python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-025/faults.py
python3 experiments/OVERNIGHT-2026-10-17/HARNESS-007/attempt-002/validate.py
python3 experiments/OVERNIGHT-2026-10-17/HARNESS-007/attempt-002/faults.py
python3 experiments/OVERNIGHT-2026-10-17/AA-012/run.py
python3 experiments/OVERNIGHT-2026-10-17/PROFILE-004/run.py
python3 experiments/EXP-006/validate.py
python3 experiments/EXP-006/measure.py screen
python3 experiments/EXP-006/measure.py confirm
python3 experiments/EXP-006/profile-results/run.py
python3 experiments/EXP-006/tag-guard/run.py
python3 experiments/EXP-006/codegen.py
python3 experiments/OVERNIGHT-2026-10-17/verify-round018.py
```

[Audit](ROUND-018-VERIFY.json) passes5,839SHA256 checks,2,253serial command windows,
697timing windows (696rows+warmup),16profiles/4calibrations,88raw-derived wall/thread
intervals and32patch reconstructions. All12old optimization patches plus3new patches
remain. Every experimental child is bounded to120s. Final audit excludes two
intentionally updated shared ledgers from the prior-round comparison; their final
hashes are recorded separately. Workspace/pristine-source and git diff --check pass. Two sanitizer logs are publicly
curated, preserving raw originals and prior manifests under ignored scratch with hashes.

CPU MCP ask, benchmark05/14 methods/code and evidence checker were consulted. Irrelevant
retrieval was not attributed as support; no M4 measurements/CPU numbering transferred.
Checker returned no_number for qualitative claims and drop_number for the quantitative
local claim because required context (especially frequency) is incomplete; it also failed
to parse some supplied context. This is not tool approval. No portable headline gain.

## Handoff

Totals: **7harnesses /13baseline explorations /31diagnostics /25named boundary suites /
54distinct boundary fault types;5sequential populations;0accepted /2rejected /3parked.**
This round adds one harness, one baseline, one profile diagnostic, one boundary suite,
one boundary fault type and one parked optimization population. Other regression/referee
fault controls are reported separately, not inflated into named-boundary counts.

Exact backend/model/token cost unknown; supervisor records actual CLI usage separately.
Confirmation and [adversarial review](../EXP-006/review/adversarial.md) are sequential.
Frequency/effective QoS/migration, qualified guards, independent review, portability and
committed provenance remain unresolved. No publishing, git retry, credentials, runtime/
STOP/supervisor/permission changes. Main baseline remains for separate morning review.

Next concrete action: investigate the [batch-size guard concern](ROUND-018-NEXT-FIXTURE.md)
with a genuinely new preregistered diagnostic/profile or qualified runner. Do not repeat
failed schedules unchanged or drop the long-key blocks. Final worker writes morning report.
