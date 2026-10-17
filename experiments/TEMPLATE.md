# {ID} — {TITLE}

Date: {DATE}
Status: PLANNED
Decision: NOT RUN

## Frozen context

- Source baseline commit / candidate commit / harness commit: TBD
- PR provenance head: a7ecd959374d66847c095250bf2d373edf7316c5
- Compiler, flags, linker, allocator, binary hashes: TBD
- Generic host/CPU, OS, affinity, frequency/cache context: TBD
- Case/cardinality/member length/score distribution/access order/seeds: TBD
- Primary metric and minimum effect, regression/memory guards, run budget: TBD
- A/A precision and baseline profile: NOT RUN
- One falsifiable hypothesis and predicted mechanism: TBD

## Population step 1 — hypothesis selection

| Proposer | Actual agent/model | Hypothesis | Profile evidence | Chair rank / rationale |
|---|---|---|---|---|
| A | NOT RUN | TBD | TBD | TBD |
| B | NOT RUN | TBD | TBD | TBD |
| C | NOT RUN | TBD | TBD | TBD |

Chair identity: TBD. Winner: NOT RUN (use NONE when no proposal qualifies).
Decision and dissent: selection.md. All proposal files: proposals/.

## Population step 2 — implementation selection

| Variant | Actual agent/model / base | Patch | Correctness | Primary / guards / memory | Verdict |
|---|---|---|---|---|---|
| A | NOT RUN | TBD | NOT RUN | NOT RUN | NOT RUN |
| B | NOT RUN | TBD | NOT RUN | NOT RUN | NOT RUN |
| C | NOT RUN | TBD | NOT RUN | NOT RUN | NOT RUN |

Measured selection: implementation-selection.md. Winner: NOT RUN.
Keep every patch and failed result. Worktree/build isolation evidence: TBD.

## Correctness gate

Upstream tree tests: NOT RUN. ASan/UBSan: NOT RUN.
Target-specific regression/model/boundary checks: NOT RUN.
Referee identity across variants: TBD.

## Validation step 1 — benchmark

| Case | Compiler/arch | Baseline ns/op | Candidate ns/op | Paired effect / uncertainty | Owned bytes | Guard |
|---|---|---|---|---|---|---|
| TBD | TBD | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |

A/A precision: TBD. Serial ABBA raw paths: TBD. Fresh confirmation/held-out seeds: TBD.
Document effective operation counts and all exclusions; no post-hoc objective changes.

## Validation step 2 — profile

Baseline/candidate hot symbols and instructions/cycles/branch/cache evidence: NOT RUN.
Timed region versus whole-process capture boundary: TBD.
Does the profile support the hypothesis, and what is now limiting? TBD.

## Adversarial review and final decision

Reviewer identity, exact commit, five lenses, verdict: NOT RUN.
ACCEPT / REJECT / PARK, reasoning, dissent and revisit condition: NOT RUN.
Upstream action: none requested. Evidence hashes and reproduction commands: TBD.
Append result to EXPERIMENTS.md, update SUMMARY.md/README counts and shared memory.

## Cost

Append measured usage to ../token-ledger.tsv. Unknown is unknown, never zero by assumption.
