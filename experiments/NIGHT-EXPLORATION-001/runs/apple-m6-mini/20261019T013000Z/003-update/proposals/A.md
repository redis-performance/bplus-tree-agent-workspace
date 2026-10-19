Three sequential passes by one Codex/GPT-6-family worker, not independent agents. Exact serving model/token costs unknown. All inspect the same source/frozen referee/census/profile/A-A.

# Pass A: retain records on exact pack failure

Hypothesis M6-UPDATE-REPACK-001: after both neighbor checks pass but current score
encoding rejects a value, re-encode score fields and relocate only offset/tag arrays
within the existing allocation when headroom permits. Preserve record bytes, leaf ID,
count, ownership and index. Expected gain: avoid delete/reinsert, descent, record copy
and possible allocation for these position-preserving updates. Primary100K/1M preserve.
Census shows1517/11058 early pack failures; release source uses remove/reinsert for all.
Sparse initial profiles capture allocation; long captures establish amortization limits.
A change to leaf packing will not repair lookup cost or true reorder cases. Risks:
metadata overlap, reversed physical orientation, shift64/width0, full-head fallback,
last-score ancestor maximum, signed zero/exact bits. Falsify with no dual-primary
improvement, any semantic fault or >1% required guard/memory regression. Portable C.
