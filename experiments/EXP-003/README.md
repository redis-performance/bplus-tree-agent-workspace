# EXP-003 — Outline iterator member decoding

Date2026-10-18. **REJECT; selection NONE.** Main source remains baseline. All three
isolated implementations improve the primary screening case but confirm full-output
guard regressions on BOTH fresh seeds. No speed/memory tradeoff was authorised.

## Hypothesis and populations

Baseline HARNESS-004 exact source/referee,AA-00610/14qualified modes,PROFILE-003 and
EXP-002 guard profiles/codegen. One hypothesis:outline member decoding under existing
ele||len test to reduce register saves on score/no-output paths without an extra public
entry guard. Three sequential proposals/chair select this over unproven duplicate hash
elimination and incompletely attributed packed-score specialization. Not independent agents.

Three isolated implementations:A pointer-return/length-out helper;B void helper handles
optional outputs;C aggregate pointer/length return. Same baseline,compiler/options,
allocator,assertions and referee. Original score decoder/state unchanged. All patches
retained. Actual backend/model/cost unknown;reviewer startup failed this round.

## Correctness and benchmark evidence

Control/A/B/C pass release and ASan/UBSan original43 tests,128 fixed iterator mode
cells/build and BOUNDARY-012 mixed mutation oracle:1064 validation commands total.
No functional/sanitizer failure. Frozen source/binary hashes and stdout/stderr retained.

504 fixed screening rows,3ABBA blocks/variant/mode;all controls pass. All three primary
intervals pass but qualified member-output guards regress. Four unqualified modes
remain diagnostic,not evidence of passed guards. Selection NONE.

216 fixed fresh confirmation rows,seeds10103/10111,3blocks/variant/mode/seed. Full-output
guard regression confirms for A/B/C on BOTH seeds under unchanged threshold. REJECT
represented implementations. This is same-coordinator fresh data,not independent review.
[Screening](SUMMARY.md),[fresh confirmation](CONFIRMATION.md),[plans](PLAN.md),
[fresh/profile plan](CONFIRMATION-PLAN.md),[freeze](freeze.json).

## Profile validation and limits

12 matched descriptive captures and two known-function calibrations pass;all symbols
resolve. Member-output samples reach the outlined helper;score/no-output samples stay
in public iterator. Saved codegen shows baseline six register-pair saves versus A/C five
and B four,but full-output paths now shuffle arguments and call the helper. Supports
register-pressure reduction with an added member-call cost;does not assign exact cycles
or prove sole causation. Some timer-boundary samples retained. No unbiased time shares.
Instrumented timing never used for source comparison.

[Profile summary](profiles/SUMMARY.md),[entry codegen](profiles/ENTRY-ASSEMBLY.md).
Frequency/effective QoS/within-window residency remain unknown;local M1/arm64/macOS26.3,
Clang17,C11,-O3,-g,-fno-omit-frame-pointer,libc,one unpinned thread. CPU MCP checker
consulted;drop_number caveat,no portable speed headline. Public evidence/commands/hashes
retained,raw PCs/full assembly under ignored scratch. Uncommitted provenance until
morning review;no git retry,publishing,permission/runtime/STOP changes.

## Decision and follow-up

[Adversarial review](review/ADVERSARIAL.md) is sequential. Both population stages completed,
no eligible implementation. New work should profile score-width/record-layout paths
before another hypothesis;do not rerun either rejected dispatch/outlining matrix
unchanged. Preserve all A/B/C patches and control. Four AA modes/lookup/suite remain PARK.
Independent review/confirmation and committed provenance mandatory for future ACCEPT.
