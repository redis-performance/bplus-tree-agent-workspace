# EXP-004 — simplify packed-score cross-word condition

Date2026-10-18. **PARK; provisional preference A; no accepted source.** Main tree stays
baseline. Three equivalent predicates eliminate one conditional branch in score decoding.
Qualified primary improvement survives two fresh seeds,while a possible score-plus-length
regression remains unqualified. Longer-duration A/A fails to qualify both fresh fixtures,
so the preregistered guard-comparison extension is skipped. No gate bypassed.

## Hypothesis and populations

Three separate sequential proposals/chair select a single redundant cross-word predicate
change. These are not independent agents;reviewer startup failed. Proposals B(mask
arithmetic) and C(iterator metadata caching) retained. Three isolated implementations:
A bits+shift>64;B bits>64-shift;C shift>64-bits. Zero-width guard,ninth-byte conditional
read,mask,endianness,layout and iterator state remain unchanged. Same HARNESS-004/base
commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus frozen uncommitted snapshots.

## Validation

Control/A/B/C pass1080commands:original43tests,128iterator-mode fixtures/build,mixed
mutation oracle,and85760synthetic leaves/2572800exact-bit decoder checks per build;
release/debug and ASan/UBSan. Both decoder sensitivity faults detected separately.
All source,referee,binary hashes and validation logs retained. Root source untouched.

AA-007240rows qualifies6/10previously qualified modes.504screening rows select A under
those current gates;B/C fail eligibility from unresolved guard uncertainty.216fresh rows
confirm primary results and A's tested no-output/full-output guards.12matched descriptive
profiles/two calibrations pass. [Screening](SUMMARY.md),[fresh data](CONFIRMATION.md),
[selection](implementation-selection.md),[plans](PLAN.md),[freeze](freeze.json).
The generic confirmation table's selection NONE means no accepted final source;the
provisional screening preference remains A,not a discarded or reselected result.

## Profile and unresolved guard

[Baseline audit](baseline-profile-audit.json) localizes existing sampled PCs to score
work;[matched profiles](profiles/SUMMARY.md) and [assembly](profiles/ITERATOR-ASSEMBLY.md)
show two cross-word conditional branches become one. No exactcycle/unbiasedshare claim,
no proven sole mechanism;layout/predictor/caller interaction remains possible. Mask6
(length+score) diagnostic moves oppositely to score-only/full-output. AA-008 uses fivefold
operation count and two fresh seeds;only one mask6 seed qualifies. Long-guard comparison
was skipped under its fixed gate. Longer duration is not a precision cure.

## Decision and limitations

PARK,A provisional;source selection NONE pending all guards,independent confirmation/
review and committed provenance. No source applied. Local M1/arm64/macOS26.3,one unpinned
thread,AppleClang17,C11,-O3,-g,-fno-omit-frame-pointer,libc;frequency/effective QoS/
within-window residency/sampler bias unknown. CPU MCP checker consulted(drop_number),
no portable speed headline. Actual backend/model/cost unknown;supervisor usage separate.
All losing patches retained. Next distinct caller-context diagnostic or uncovered physical
layout fixture;do not rerun unchanged20m/100m guard precision indefinitely.

## Round11 compact guard extension

[Compact-history evidence](compact-guards/README.md):1770validationcommands pass,
72screen+72freshrows and12profiles/2calibrations complete. A/B pass the solequalified
newguardonbothfreshseeds;C is inconclusive onone. No confirmedregression. A/PARK unchanged;
no newpopulation/adoption and originalmixed-outputguard remainsunresolved.
