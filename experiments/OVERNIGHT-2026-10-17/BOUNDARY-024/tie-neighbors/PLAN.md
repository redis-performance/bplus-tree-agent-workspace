# Actual equal-neighbor rejection — new fixture, not a repeat

The finite-ties matrix passes16cells but skip-equal-neighbor-order survives; retain
all prior outputs unchanged. Add two public updates immediately after the first two
fractional moves during the same natural mixed-width resize: ID256from256to255 and
ID511from511to512. Little-endian key bytes make256sort before255, and511after512;
therefore numeric equality with the adjacent key requires within-leaf reordering.
Require neither added operation changes leaf ID (same observed leaf, not a promise
for arbitrary geometry), but full independent sorted current-score order must match.
No private state changes and no stale successful positions. Capture counts and print
these first4moves. Keep every earlier finite pattern, signed-zero, SCAN, anchor,
termination, current-value, memory, clone and structural check in this NEW oracle.
Extend single-score range checks to255/512:14values*4endpoint pairs*6models=336checks.
Expected nonzero-tagged updates260plus2special zero updates; actual cross-leaf count
reported separately and both cross-ownership classes still required.

Fresh seeds73501/73517, control/EXP-004A/B/C, nativeO3/debug and O1ASan/UBSan/debug:
16fixedcells, serial120schildren,900stotal. Freeze before compiling; stop on any
failure and retain recipe. Repeat only the previously surviving fault against this
new coverage. Require successful build plus oracle/assertion/sanitizer failure;
survival remains an honest possible outcome. No optimization or timing claim.
