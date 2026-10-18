# HARNESS-006 — compact deletion-history referee

Locally validated separate revision; no root source/referee changes. Adds trimmed,
trimmed-clone and trimmed-cycle histories through public B+ tree APIs. Existing timing
loop, checksum, exact semantic oracle, output masks, iterator-copy checks, exhaustion
sentinels, effective traversal counts and per-window tree-owned memory guard remain.

Release and ASan/UBSan each pass 2,560 fixture cells: all 1,408 prior cases plus 1,152
compact-history cells. Original upstream tests pass in both builds; all five invalid-input
cases/build return the required status2. Three isolated sanitizer fault controls abort
on semantic assertions: bad length, erased zero sign, corrupted iterator position.
5,136 validation commands complete with expected results; fault builds/runs are additional.

The harness is compiled separately from the unchanged tree source. Structural census
results do not substitute for timings. Capacity-policy diagnostic adapters are not used.
No assumption of fixed frequency or equal native/ASan allocation sizes. Public boundary
CPU IDs can remain unavailable; reported QoS does not prove effective scheduling policy.

[Plan](PLAN.md), [patch](harness.patch), [freeze](freeze.json),
[validation](validation.json), [fault controls](faults.json),
[separate profile plan](PROFILE-PLAN.md). A/A qualification is separately preregistered
as AA-011. This sixth referee revision remains uncommitted pending morning review.
Backend/model/cost unknown; independent reviewer startup failed, so review is sequential.
