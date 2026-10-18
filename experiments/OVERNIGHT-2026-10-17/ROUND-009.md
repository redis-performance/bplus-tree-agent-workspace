# Round 9 — exact zero signs, controlled placement, and score-mask arithmetic

**No source was accepted. EXP-005 is PARK/NONE; EXP-004 remains A/PARK.**
The main source, header, and referee retain their prior-round hashes. This is not the
final campaign round; the final worker still owes MORNING-REPORT.md before 07:00 UTC.

The worker began at 01:20:52 UTC on 18 October 2026. Its deadline is 01:50:52 UTC,
with no new work after the 01:49:22 handoff cutoff. All experimental measurements
finished before 01:39 UTC. The remaining work audited evidence and reconciled records.

## Completed work

BOUNDARY-014 exercises equal numeric scores with distinct +0/-0 bits through real
updates, cloning, minimum deletion, physical reversal, refill, and alternating-edge
removal. It covers 24 fixed fixtures per build: 97/513 members, binary lengths
16/319/320, ascending/descending insertion, and two hash seeds. The independent scalar
packed reader and public API model pass 22,080 full checks and 46,005,384 exact-score
results per build. Both physical orders and 626 first-leaf reversal opportunities
are observed. Control and all three retained EXP-004 variants pass release/debug and
ASan/UBSan, with identical output. Two deliberate faults are detected.

The first control attempt failed a new test's allocation assertion: queries advanced
an active index rehash. This was a test-precondition mistake, not a source defect.
Its snapshot, oracle patch, and failure remain. Attempt 002 explicitly settles rehash
before the same read-only memory equality check; no exact-score or existing check
was weakened.

DIAG-012 isolates iterator placement more carefully than the prior caller experiment.
It inserts a fixed total of 64 unreachable padding bytes before/after the iterator,
using offsets 0/16/32/48. Only the iterator's named symbol moves; the complete
274-instruction caller and 155-instruction iterator match after relocation normalization.
The diagnostic passes 1,024 mode fixtures across release and sanitized assembly, plus
four upstream runs with all 43 tests passing. The successful preparation has 23 commands.

All 480 fixed timing rows and four prospective warmups complete. Both placebo mask6
A/A controls pass the fixed precision criterion. The preselected 16-byte shift fails
its material-effect criterion on both seeds: the placement hypothesis is unsupported.
Other offsets are descriptive. This does not establish a cache/predictor mechanism,
qualify the original EXP-004 executable, or clear its guard.

Two preparation corrections are retained: Clang's upstream-test assembly contains
non-UTF-8 string bytes, so the second snapshot uses byte-preserving Latin-1 handling;
and the initial caller audit stopped at the shared return before later mask blocks.
The full caller audit was corrected before any timing. No timing row was dropped.

EXP-005 tests one new hypothesis: simplifying the nonzero packed-score width mask,
while preserving the original cross-word predicate. Three separate sequential
proposal passes and a chair select it; three isolated implementations follow. These
were not independent agents. A uses a right-shift mask, B uses defined unsigned wrap,
and C uses modular negation. The baseline remains a control throughout.

All 1,096 validation commands pass: original tests, mode fixtures, mixed mutations,
exhaustive bitstream decoding, and real signed-zero mutations in both builds.
AA-009 retains 72 rows and one prospective warmup, qualifying masks 0/4/7 on a fresh
seed. It does not repeat the previously failed mask6 qualification schedule.

The 180-row screening provisionally prefers C on the qualified subset. The precommitted
216-row fresh confirmation includes all three candidates. C's primary interval fails
the required improvement bound on both fresh seeds. Its tested no-output/full-output
guards pass, while score-plus-length remains an adverse, unqualified screening result.
A/B also fail fresh primary requirements. Final selection is NONE; EXP-005 is PARK.

Twelve matched descriptive profiles and two calibrations pass. A/C remove one static
mask instruction, and their iterator instructions/addresses match after normalizing
four panic-message relocations. Their full binaries differ. This limits any claim
that C is intrinsically better than A; static counts cannot override failed fresh
measurement gates. All patches remain available for morning review.

## Commands and evidence

Exact arguments, compiler flags, source/binary hashes, stdout, and stderr are recorded
in the linked manifests. Commands below were run from the repository root.

- `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-014/run.py`: preserved initial
  precondition failure. `run-attempt002.py` and `faults.py`: PASS.
- `python3 experiments/OVERNIGHT-2026-10-17/DIAG-012/prepare.py`: preserved UTF-8 read
  failure. `prepare-attempt002.py`, `audit-codegen.py`, and `validate.py`: PASS.
- DIAG-012 `run.py` and `analyse.py`: complete; primary hypothesis unsupported.
- `python3 experiments/EXP-005/prepare.py` and `validate-one.py experiments/EXP-005/<variant>`
  for control/A/B/C: PASS.
- AA-009 `run.py` and `analyse.py`: 3/3 planned cells qualify.
- EXP-005 `run.py`, `analyse.py`, `confirm.py`, `analyse-confirm.py`, `profile.py`,
  `analyse-profile.py`, and `codegen.py`: complete; final PARK/NONE.
- `python3 experiments/OVERNIGHT-2026-10-17/verify-round009.py`: PASS. It independently
  recomputes 76 wall/thread intervals from raw rows, verifies snapshots and patches,
  checks profile conservation, and verifies serial measurement windows.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check`: PASS.

[Boundary evidence](BOUNDARY-014/README.md), [placement evidence](DIAG-012/README.md),
[qualification](AA-009/README.md), [EXP-005 decision](../EXP-005/implementation-selection.md),
[adversarial review](../EXP-005/REVIEW.md), [audit](ROUND-009-VERIFY.json),
[method record](ROUND-009-METHOD.json). Raw profiles and full candidate assembly stay
under ignored scratch with checksums. Public summaries contain no private machine paths. The final curation scan initially
matched its own generic path-prefix literals in the verifier; that self-match is
recorded separately. Splitting literal construction preserves the same byte checks.

The round preserves **948 measured rows, five prospective warmups, twelve profiles,
and two calibrations: 967 serial measurement windows**. No measured child failed or
timed out. Preparation/test failures are retained separately and explained above.

## Decisions, uncertainty, and handoff

Campaign totals: four harness revisions, ten baseline explorations, seventeen additional
diagnostics, fourteen boundary suites with 28 detected faults, and four sequential
population rounds. Optimizations: **zero accepted, two rejected, two parked**.
EXP-002/003 stay rejected. EXP-004 stays A/PARK; EXP-005 is PARK/NONE.

The independent reviewer failed to start before executing. All reviews and fresh-seed
confirmation were by the coordinator, and are explicitly sequential. Exact backend,
model, and costs are unknown; the supervisor records actual CLI usage separately.
Git metadata denial was not retried. No source adoption, publishing, permission changes,
supervisor/runtime/STOP edits, or detached process was used.

Frequency, effective QoS, within-window migration, and sampling bias remain unknown.
CPU MCP ask and methods/code 05/14 were consulted; irrelevant retrieved passages were
not used as support. No M4 numbers were transferred. Both evidence checker responses
were drop_number; no speed headline is claimed. Independent confirmation/review,
broader performance guards, and committed provenance remain acceptance requirements.

Next concrete work: prepare a separate iterator fixture covering monotonic construction
and alternating signed-zero scores, using the actual physical-order paths established
by COUNTERS-003 and BOUNDARY-014. Validate exact bits and masks, freeze it, and preregister
its own qualification before comparing retained candidates. This is a new fixture,
not a replacement for the original failed guard. Alternatively obtain independently
controlled runner evidence when a real campaign requires it. Do not repeat unchanged
mask6 duration/QoS/caller/placement trials or pool A/C results to clear a threshold.
Keep main source baseline until the separate morning review.
