# Population-based decisions

Adapted from the selection and implementation populations in
[HDR's pipeline](https://github.com/redis-performance/hdr-agent-workspace/blob/22c42ac78afdc83c2fdc5e4e106ee5e094eed254/README.md#optimization-pipeline).
The default population is three; the chair does not count as a fourth proposal.
The baseline remains a control throughout. Models are session choices, not hardcoded.

## Prerequisites

Create an experiment with `scripts/new-experiment.py EXP-002 "Short title"`.
Freeze source and harness commits, binary hashes, host description, compiler/linker flags,
allocator, datasets/seeds, primary objective, guard workloads, run budget and decision
thresholds in its README. Capture a qualified A/A baseline and baseline profile first.
No profiles yet means preparation, not an evidence-backed selection.

## Step 1 — population-based hypothesis selection

Give proposers A/B/C the same frozen source, baseline results/profile, playbook and
experiment history. They produce separate files in `proposals/` without reading one
another's proposals. Require bottleneck evidence, one falsifiable hypothesis, exact target,
expected mechanism, correctness risks, workload predictions and falsification criteria.
Suggested distinct lenses: tree search/score packing; member-index probes/rehash;
allocation/leaf movement. These are lenses, not predetermined winners.

The chair writes `selection.md`, ranks evidence quality, expected useful gain, correctness
risk, scope, novelty and portability, then chooses one hypothesis or `NONE`. Record all
three rankings, rejection/parking reasons and any dissent. Do not combine hypotheses
after voting. If all lack evidence, request a better profile or fixture rather than code.

## Step 2 — population-based implementation selection

Each implementer A/B/C receives the same winning hypothesis and exact baseline commit.
Create one worktree per variant; do not share mutable source or build directories.
Each writes `variants/<id>/implementation.md` plus a patch with its distinct implementation
choices, touched functions and semantic risks. Keep the referee files identical.

Build and validate each variant. A correctness or sanitizer failure makes it ineligible.
Measure passing variants **serially** against the unchanged baseline using identical
fixtures and same-session ABBA blocks. Preserve failed builds and rejected patches too.
`implementation-selection.md` compares every variant, including failures, target/guard
results, memory, uncertainty and profile evidence. Select the best passing variant or
`NONE`; ties within noise are not wins. Favour the smaller change among equivalent results.

After selection, run a fresh confirmation with the chosen variant and baseline. Predeclare
additional seeds/cases so selection over three variants does not turn measurement noise
into a published win. Discovery measurements do not count as confirmation.

## Separate two-step validation

1. **Benchmark:** report ns/op, ops/sec, owned bytes and bytes/member. Qualify A/A, run at
   least three ABBA blocks, retain raw CSV and paired effects, show dispersion/uncertainty.
   Default gate: >=2% primary improvement with no demonstrated >1% guard or memory loss.
   A/A noise must be sufficiently below the claimed gain and regression guard; otherwise PARK.
2. **Profile:** compare baseline and selected variant hot symbols, instructions/cycles,
   branch/cache behaviour where supported, and explain whether the proposed mechanism
   changed. Whole-process profiles include fixture setup: disclose that boundary and do
   not call whole-process counters timed-loop counters. An unexplained timing win stays PARKED.

An adversarial reviewer then checks semantics/ownership, portability/UB, test strength,
measurement validity and maintainability. Every lens must pass before ACCEPT. Acceptance
in this workspace is separate from opening or merging an upstream PR.

## Decision record

Use the headings in `experiments/TEMPLATE.md`. ACCEPT commits the winning source and
evidence; REJECT records the reason and keeps patches; PARK records the precise missing
evidence and a revisit condition. Preserve population membership, per-agent provenance,
all votes, costs and counterarguments. Append the outcome to the log and update shared
memory and the summary. A sequential multi-pass fallback must be labelled as such.
