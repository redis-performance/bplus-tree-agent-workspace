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


## AWS AMD native checkpoint — 19 October 2026

[LOWERBOUND-001](../experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/002-lowerbound/implementation-selection.md) is REJECT/NONE: three sequential proposals and three isolated implementations, 144 comparison rows. All three fail both 2% primary gates. Root independent review/audit supports the decision. All patches and raw rows retained; baseline source unchanged. AMD totals: one completed population, zero accepted, one rejected, zero parked. Scoped perf control failures and corrected FIFO controls retained. Packed-score census complete; new builder-write preparation has fresh profiles and full-pass A/A running. Deadline08:00UTC, no new experiments after07:15UTC.


## AWS AMD BUILDER-WRITE-001 — 19 October 2026

BUILDER-WRITE-001 REJECT/NONE: 144 processes, all 36 effects slower. A +1.039%/+1.362%, B +1.250%/+1.745%, C +5.777%/+2.766% median elapsed at 100K/1M; no guards or confirmation. All patches/raw rows retained. AMD totals: 2 populations, 0 accepted, 2 rejected, 0 parked. Baseline source unchanged. Evidence: `experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/004-builder-write/implementation-selection.md`.


## AWS AMD FULL-CHUNKS-001 — 19 October 2026

FULL-CHUNKS-001 REJECT/NONE: 144 serial processes, 36 effects, no block reaches 2% improvement. A −0.609%/+0.380%, B +0.265%/+0.403%, C −0.824%/+0.854% median elapsed at 100K/1M. All patches/raw evidence retained. AMD totals: 3 populations, 0 accepted, 3 rejected, 0 parked. Baseline source unchanged. Evidence: `experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/005-full-chunks/implementation-selection.md`.


## AWS AMD SCAN-TAGS-001 — 19 October 2026

SCAN-TAGS-001 PARK/NONE:144processes/36effects. A−5.255%/−4.360% and B−4.279%/−4.297% median100K/1M elapsed changes meet every-block dual-primary gate; C−3.790%/−2.143% fails1M block gate. Failed1M A/A and missing guards prevent qualification. A receives one matched mechanism diagnostic by fixed alphabetical priority, not superiority. AMD totals4populations:0accepted,3rejected,1parked. Baseline source unchanged. Evidence: `experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/008-scan-tags/implementation-selection.md`.


## AWS AMD delete diagnostic — 19 October 2026

Delete-offset diagnostic chair101895e82 selectsNONE:1M AA noise up to4.682% versus approximate5.496% loop attribution,100K sparse samples. Three actual proposals retained; no implementation/retry/new optimization count. AMD totals remain4populations:0accepted,3rejected,1parked. AMD host idle; independent Intel scan B review next, no runner access before handover. Evidence: `experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/009-delete/DECISION.md`.

2026-10-19T04:39:02.477458+00:00: AMD separate corrected-adapter baseline13e459ff8 complete,11/40qualified,29short/noisy; all raw rows and chart retained. Intel independent primary confirmation/guard/profile reviews complete; adoptionNONE.
