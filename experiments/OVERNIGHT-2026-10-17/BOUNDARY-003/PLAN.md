# BOUNDARY-003 preregistration — natural wide-ID transition

Correctness experiment, not performance measurement or an optimisation candidate.
Base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c, source unchanged; additional oracle only.
Include the original source in the test translation unit to observe private counters;
never change IDs, resize thresholds or implementation fields. Build with REDIS_DEBUG,
release -O3 and ASan/UBSan -O1. All commands, failures and hashes retained.

Fixed seeds7 and19, one child per seed/build, <=120s each. Build 850000 sorted-score
319-byte binary members through the public append API. These inline records naturally
create more than65535 leaves. Require actual narrow-to-wide active migration and
next_score_leaf_id>65535, then add4096 external binary members at320/321/1024 bytes.
Scan while natural widening is active, checking all live bytes/scores and complete
coverage, allowing legal duplicate callbacks. Require no field mutation by the test.

Full model checks: raw lookups, sorted iteration both ways, sampled ranks/seeks, exact
score bits, scan membership. Delete an interior rank range, reinsert with negative
scores, exercise scan with inter-call score moves and delete/reinsert churn. Every
member present throughout must be returned; every callback must currently be live.
Track largest table scan-group count; enforce bounded scan completion. Clone, free
original, verify clone to detect shared external ownership. Sanitizers cover memory
safety. These checks complement existing forced-ID tests, not replace/weaken them.

If baseline fails, preserve exact seed/stage and investigate the oracle contract first.
Do not silently alter fixture counts or assertions to get a pass. A test-strength
mutation control will be separately preregistered if time permits. No speed claims.
Backend/model unknown; single coordinator unless an actual reviewer successfully runs.
