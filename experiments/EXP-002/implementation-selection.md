# Current decision — NONE; REJECT represented implementations

Round7 [expanded guard evidence](guard-extension/README.md) supersedes the historical
provisional selection below. All three confirm guard regressions on fresh seeds.

# Measured selection — C; final decision PARK

All three isolated implementations and control pass release+ASan/UBSan original tests,
lexical optional-output masks and score-boundary oracles. All72 fixed comparison rows
pass controls. A/B/C each pass preregistered primary/guard screening. C selected: best
primary mean, overlapping B interval, smaller patch under the declared tie rule.
See bench-results/SUMMARY.md and summary.json for all means, intervals and raw rows.

Fresh-seed C/control confirmation24 rows passes the same fixed rule in both cells;
see bench-results/CONFIRMATION.md. Four matched descriptive profiles resolve every
sample. Codegen confirms C's forward score-only path no longer saves generic callee-
saved register pairs; generic path is a tail-dispatched noinline fallback. Same decoder,
no changed tree/iterator representation, exact same tree-owned bytes per matched cell.
No exact cycles, unbiased profile fractions, fixed-frequency or portable gain claim.

PARK rather than ACCEPT: reverse/full-member/length-only/no-output performance guards
are missing; generic path now pays dispatch and may regress. Also missing independent
performance confirmation/reviewer and committed provenance. Fresh data here are same-
coordinator confirmation, not independent agent work. Root source remains baseline.
All losing patches A/B retained. Both population stages used explicitly sequential
passes; no independent participants fabricated. Backend/model/token costs unknown.
Next: separate frozen iterator-mode fixture extension, qualify its controls, then
measure selected C against baseline for all output masks and both directions. Add
fresh seeds/score encodings, independent review and morning commit review before acceptance.
