# BOUNDARY-006 — exact bulk-deletion rebuild thresholds

New correctness experiment, no timing/source candidate. Existing wide-ID suite covers
one large rebuild; this suite targets both sides of the >1024 and >=length/10 branch.
Two seeds11/111, sizes7169/10240/10260/14337; cut lengths respectively(1024,1025),
(1024,1025),(1025,1026),(1432,1433). For every pair, delete prefix/middle/suffix:
48 cases/build. At7169 and14337 ordinary insertion has just initiated natural resize;
assert it is active before deletion. Do not drain it with preparatory lookup checks.
Verify a duplicate first, and scan the original without progressing migration.

Construct unique mixed binary8/319/320/321/1024-byte members and equal-score groups
of three, preserving signed zero for first group. Model checks direct/raw/batched
lookup, both iteration directions, sampled ranks/seeks, full scan, exact score bits,
key lengths/bytes and ownership. Test batch counts0..16, repeated members and output
canaries. Use only public mutation APIs; private tree fields are read-only observations.

Before cut, compute expected rank order independently. After cut verify count and all
survivors/absences. Observe dense renumbered leaf IDs and completed migration on rebuild
arm; unchanged next-ID counter on incremental arm. Duplicate, free original, verify
copy; reinsert all deleted members, verify; delete full range using ULONG_MAX, verify
empty. Retain any failing case and its exact source; never relax checks to pass.

Release/debug and ASan/UBSan runs, child limit120s. Preserve all commands, patches,
source/binary hashes, stdout/stderr. Follow with two separately preregistered isolated
fault controls. No measurement, no independent confirmation claim; reviewer startup
failed, sequential coordinator review. Backend/model/token cost unknown. Root source
and frozen harness unchanged; no git/worktree/sample-denial retry.
