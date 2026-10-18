# Test-strength controls, written before runs

Two isolated intentional faults, release/debug build, seed7, <=120s child each.
No performance timing and no optimisation candidate. Original source untouched.

1. Delay narrow-to-wide upgrade past the 16-bit ID range by replacing
   ZBT_INDEX_WIDE_ID_AT with UINT32_MAX/2. Expect an ID-range or widening assertion.
2. Omit the smaller-table traversal in zbtreeScan. Expect the active-natural-widening
   complete-membership scan to detect missing live entries.

Save exact patches, source/binary hashes, stdout/stderr and exit codes. A fault that
passes means this oracle has not demonstrated sensitivity to it; preserve that result.
Agent review startup failed before any agent ran; review is sequential, not independent.
