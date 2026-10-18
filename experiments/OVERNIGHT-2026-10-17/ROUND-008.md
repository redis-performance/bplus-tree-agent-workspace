# Round 8 — a smaller decoder, with an unresolved guard

Worker started 2026-10-18 at 00:54 UTC; round deadline is 01:24:06 UTC. Experimental
runs finished by 01:15 UTC. The remainder of the round audited the evidence and saved
this handoff before the 01:22:36 cutoff. This is not the final campaign round; the final
worker must write MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

**Outcome: EXP-004 is PARKED, with A the provisional preference. No source was accepted
or applied.** The primary result survives fresh seeds, but score-plus-length remains an
unqualified potential regression. Neither a longer duration nor a changed caller cleared
that concern. Root source, headers and the existing referee match the previous round.

## Completed work

- COUNTERS-003 inspected 160 fixed packed-layout fixtures in release/debug and ASan/UBSan,
  for 320 successful child runs. The independent bitwise reader and original iterator
  oracle pass. The four primary fixtures meet the preregistered narrow-width criterion;
  rare 64-bit and cross-word paths remain necessary. These are structural counts, not
  time shares. The post-run driver mistakenly compared native and sanitizer owned-byte
  totals. Its assertion is retained; a read-only audit finds only allocator size reporting
  differs, while every structural field and within-run memory invariant agrees.
- BOUNDARY-013 adds an independent scalar bit writer and exact IEEE-bit decoder oracle.
  Each build passes 85,760 synthetic leaves and 2,572,800 results across widths 0–64,
  valid shifts, ten counts, two seeds and both physical orders. Both intentional faults
  are detected. All scores are finite; no unsupported NaN assumption was introduced.
- EXP-004 completes both population stages: three separate sequential proposals and a
  chair, then three isolated implementations of one equivalent cross-word predicate.
  These were not independent agents. All 1,080 validation commands pass: original tests,
  iterator mode fixtures, mutation checks and the new bitstream oracle, in both builds.
- AA-007 retains 240 A/A rows and one prospective warmup. Six of ten previously qualified
  modes qualify now, including the primary and no-output/full-output guards. Four modes
  become parked; the four earlier AA-006 failures were not rerun.
- EXP-004 retains 504 screening rows and 216 fresh-seed rows. A is the screening
  preference; fresh primary and tested no-output/full-output guards pass. B/C remain
  ineligible from uncertainty. Twelve matched profiles and two calibrations pass.
  Assembly confirms one redundant conditional branch is removed. Sampled PCs do not
  establish a cycle budget or rule out layout and predictor effects.
- AA-008 tests five times the operation count on two new seeds, with score-only controls:
  96 rows plus one prospective warmup. Only one score-plus-length seed qualifies. The
  joint duration hypothesis fails, and the planned 144-row source comparison is skipped
  exactly as required by its preregistration. No large primary gain bypasses this gate.
- DIAG-011 tests dynamic versus literal-mask callers in isolated snapshots. Its 144 rows
  pass all functional and memory controls, but its two-seed interaction criterion fails.
  Eight matched profiles and two calibrations pass. Assembly also contradicts the proposed
  per-item-test mechanism: Clang already unswitches the dynamic mask6 inner loop. Fixed
  callers change registers and layout as well; no causal hardware claim is warranted.
  Its explicit validation matrix passes all 384 fixture processes plus four builds.
  The original plan/progress label had a factor-of-two arithmetic error; a pre-timing
  erratum records it without removing any listed fixture or weakening any check.

This round preserves **1,200 measured rows, two prospective warmups, 20 profiles and
four calibrations**. All 1,226 timing/profile windows are serial. There were no measured
child failures or timeouts. The census post-run assertion and validation-count erratum
are retained and explained, rather than hidden or rerun away.

## Evidence and validation commands

All paths below are repository-relative; manifests record exact compiler flags, commands,
source/binary hashes, stdout and stderr. Raw profile PCs and full assembly remain in
ignored scratch with checksums; curated summaries and excerpts are public artifacts.

- `python3 experiments/OVERNIGHT-2026-10-17/COUNTERS-003/{run,analyse}.py`
- `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-013/{run,faults}.py`
- `python3 experiments/OVERNIGHT-2026-10-17/AA-007/{run,analyse}.py`
- `python3 experiments/EXP-004/prepare.py` and `validate-one.py experiments/EXP-004/<variant>`
- `python3 experiments/EXP-004/{run,analyse,confirm,analyse-confirm,profile,analyse-profile}.py`
- `python3 experiments/OVERNIGHT-2026-10-17/AA-008/{run,analyse}.py`
- `python3 experiments/OVERNIGHT-2026-10-17/DIAG-011/{prepare,validate,run,analyse,profile,analyse-profile,codegen-audit}.py`
- `verify-round008.py`: PASS for source/referee/raw hashes, candidate patch equivalence,
  serial windows, profile count conservation, skipped-comparison gate and public paths.
- `audit-round008-effects.py`: independently recomputes all 86 effect intervals from raw
  rows; PASS. This is a separate coordinator audit, not independent-agent confirmation.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check`: PASS.

The brace lists above abbreviate separate recorded commands; they are not literal shell
invocations. See each experiment's README and manifest for exact reproduction commands.

## Decisions and limits

Campaign totals: four validated harness revisions; nine baseline explorations; sixteen
additional diagnostics; thirteen boundary suites with 26 detected faults; three sequential
population rounds; **zero accepted, two rejected and one parked optimization**.
EXP-002 and EXP-003 remain rejected. EXP-004 is A/PARK; final accepted source is NONE.
All candidate patches and prior evidence remain intact.

The reviewer failed to start before executing. Exact backend/model and token cost are
unknown; the supervisor records CLI usage separately. Fresh seeds are same-coordinator
confirmation. Independent review/confirmation, broader score-consuming operation guards
and committed provenance remain acceptance requirements. Git metadata protection was
not retried. No publication, permission changes, runtime/STOP edits or detached processes.

CPU MCP ask and benchmark 05/14 methods/code were consulted. No M4 Pro CPU numbering,
frequencies or timings were transferred. Evidence checkers were consulted; their heuristic
outputs do not certify a speed headline. Frequency, effective QoS, within-window migration,
sampler cadence/aliasing and hardware causal attribution remain unknown.

## Next concrete action

Keep A and the unchanged control. Before another timing hypothesis, inspect and record
caller/iterator assembly together, including actual mask6 loop bodies. A useful distinct
next diagnostic is controlled code placement with the same frozen caller instructions,
provided it can be validated and preregistered without changing the source acceptance
referee. Alternatively, extend physical-order and signed-zero fixture coverage identified
by COUNTERS-003. Requalify any new fixture before a source comparison.

Do not repeat unchanged 20m/100m mask6 A/A schedules, reuse the unsupported caller-test
removal premise, replace the referee to clear a guard, or treat the primary gain as
acceptance. Preserve the main baseline until separate morning review. Final worker still
owes the campaign-wide MORNING-REPORT.md by 07:00 UTC.
