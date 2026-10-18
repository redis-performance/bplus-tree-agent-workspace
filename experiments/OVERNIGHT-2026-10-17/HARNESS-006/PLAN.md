# HARNESS-006 — compact deletion-history fixtures

Separate additive referee revision over frozen HARNESS-005. Introduce trimmed,
trimmed-clone and trimmed-cycle construction through the public API recipe validated
in COUNTERS-005: adjacent finite smaller sentinel, ascending insert, delete minimum;
optionally clone or reinsert/remove sentinel. Root source/referee stays unchanged.

Retain original timing loop, exact model checks, optional output/state-copy checks,
exhaustion sentinels, folded score checksum, traversal rounding, observed QoS/thread
time/boundary IDs and unchanged per-window tree-owned memory guard. Fingerprint encodes
the requested history. No assumption of equal allocated bytes across build types.
No claim that every n/member width retains one reversed leaf: structural census remains
separate evidence. All children <=120s; no overlapping measured work.

Validation: original 1,408 HARNESS-005 fixtures plus 1,152 new cells: n1/31/32/95,
bytes16/320,integer/wide/alternating-zero,three new histories,two directions,eight masks.
Both release and ASan/UBSan, original upstream tests and invalid inputs. Three sensitivity
faults are rechecked in isolated snapshots: corrupt length, exact-score sign and iterator
state; failures must be caught by semantic assertions. Preserve any driver failures.
Freeze exact file/binary hashes before separately preregistering profile and A/A.
This is referee work, not a source optimization population. Backend/model/cost unknown.
