# Sensitivity transfer preregistration

After all80 normal cells pass, transfer five existing BOUNDARY-025/023 faults onto
exact EXP-006 C, one separate snapshot per fault: cached table after promotion,
last-hit omission, outside-count write, stale renumbered leaf ID, shallow external
clone. The first three use partial_batch_promotion_oracle.c; fourth narrowing;
fifth external relocation mode0. Seed92503, REDIS_DEBUG, O1ASan/UBSan, unchanged
oracles/adapter. One build/run per fault, serial120s children, no retries. Use same
common flags as matrix. All snapshots/patches/hashes/raw logs retained; raw sanitizer
paths stay in scratch, public stderr replaces only workspace path with <workspace>.

Build failure is infrastructure/incomplete, not detected fault. A run is detected
only for a nonzero non-timeout exit with oracle assertion, source assertion or
ASan/UBSan failure; exact message reviewed. Timeout is inconclusive; successful exit
is SURVIVED and does not justify adjusting checks. Record the failure location to
avoid claiming it reached the intended boundary if it fails earlier. Stop starting
children at06:27UTC. These are repeated controls, not new distinct fault types,
production bugs, correctness proof, performance observations or source acceptance.
