# Finite extremes and equal-score movement extension

New preregistered correctness scope, not a retry or modification of BOUNDARY-024.
Freeze a new oracle and isolated control/A/B/C copies. Seeds72503/72511, nativeO3/
debug and O1ASan/UBSan/debug, fixed16cells,120sper child,900stotal, stop on first
failure and retain it. Root source, referee, allocator and prior oracles unchanged.

Keep natural mixed-width construction, first two fractional cross-ownership moves,
all current-score models, current SCAN hash intervals, continuous anchors, bounded
termination and exact owned bytes. Replace subsequent min/max score sequence with
12fixed exact finite bit patterns repeated through128pairs: ±DBL_MAX, ±smallest
subnormal, ±smallest normal, ±zero, ±1 and ±2^53. Members remain continuously present;
allow multiple distinct keys with numerically equal scores, including opposite zero
signs. No NaN or infinity inputs. Two ID0 signed-zero updates remain unchanged.

The true independent sorted model orders numeric scores then binary bytes. Search
the equal-score group after each update for the exact member, bounded512entries
(the fixture introduces at most260changed members plus at most one unchanged match).
Allow a score update to stay in the same leaf; count actual cross-leaf moves separately
and require both cross-ownership classes, rather than asserting every tied update
moves leaf. This changes the new test's coverage predicate; original test stays frozen.

At every full logical model check, compute12single-score interval counts with all4
inclusive/exclusive endpoint combinations directly from the current score vector and
compare zbtreeCountByScore. Equal signed zeros share numeric rank order but retain
exact returned bit patterns. All existing full iteration/lookup, sampled rank/seek,
clone/free-original and SCAN checks remain. No tolerance or normalization of scores.

One isolated deliberate fault: replace equal-score neighbor member comparison in
zbtScoreUpdateInPlace with an unconditional allowed tie, permitting incorrect order.
Require successful sanitizer compilation and actual oracle/assertion/sanitizer
failure; retain survival. SourceNONE, existingPARK unchanged; no performance claim.
