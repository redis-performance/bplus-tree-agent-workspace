# EXP-008 — Short-range scalar fallback for bulk score decoding

Date: 2026-10-19
Status: PREPARED — awaiting frozen-run start
Decision: PENDING — no candidate selected

## Frozen context

- Source baseline: EXP-007 original root source at `4fd3a3fdbce5acca18ee292642a3d80a79f50362`; bulk helper frozen from EXP-007 B; EXP-008 referee commit pending.
- PR provenance head: a7ecd959374d66847c095250bf2d373edf7316c5
- Compiler, flags, linker, allocator, binary hashes: TBD
- Generic host/CPU, OS, affinity, frequency/cache context: TBD
- Case/cardinality/member length/score distribution/access order/seeds: TBD
- Primary: width60 forward count16; secondary width60/count96, both >=2% faster. Guard limit1%; A/A cells failing ±1% all-block precision remain unresolved. Discovery budget300s; fresh confirmation180s.
- A/A precision: NOT RUN; baseline profile: NOT RUN
- Hypothesis: a per-range scalar path through count 8 removes short-range overhead while retaining EXP-007 B bulk decoding above 8.

## Population step 1 — hypothesis selection

| Proposer | Actual agent/model | Hypothesis | Profile evidence | Chair rank / rationale |
|---|---|---|---|---|
| A | NOT RUN | TBD | TBD | TBD |
| B | NOT RUN | TBD | TBD | TBD |
| C | NOT RUN | TBD | TBD | TBD |

Chair identity: `/root`. Winner: scalar for counts <=8, B bulk for counts >8. Rationale and dissent: selection.md.
Decision and dissent: [selection](selection.md); [preregistered plan](PLAN.md). All proposal files: proposals/.

## Population step 2 — implementation selection

| Variant | Actual agent/model / base | Patch | Correctness | Primary / guards / memory | Verdict |
|---|---|---|---|---|---|
| A | independent implementer; baseline4fd3a3fd | variants/A/policy.inc | release + ASan/UBSan decoder suites passed | pending timing | pending timing |
| B | independent implementer; baseline4fd3a3fd | variants/B/policy.inc | release + ASan/UBSan decoder suites passed | pending timing | pending timing |
| C | independent implementer; baseline4fd3a3fd | variants/C/policy.inc | release + ASan/UBSan decoder suites passed | pending timing | pending timing |

Measured selection: implementation-selection.md. Winner: NOT RUN.
Keep every patch and failed result. Worktree/build isolation evidence: detached baseline worktrees and separate output binaries; build manifests are retained.

## Correctness gate

Upstream tree tests: out of scope. ASan/UBSan: passed for all four binaries.
Target-specific regression/model/boundary checks: passed for all four binaries (1,820-case exhaustive self-test and Python oracle groups).
Referee identity across variants: common kernel, adapter, helper bytes, and checksum/materialization barrier.

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
