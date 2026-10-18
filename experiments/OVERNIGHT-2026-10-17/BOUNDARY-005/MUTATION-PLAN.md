# Fixed sensitivity controls after baseline attempt3 passes

Two separate isolated ASan/UBSan/debug snapshots, root source unchanged. One run each,
120s child limit. Save all outcomes, including undetected controls; do not modify the
oracle after observing them.

1. Clear the tag at index deletion as well as marking its ID deleted. This incorrectly
   makes a tombstone an unused slot and may terminate a later collision probe early.
   Expected: sorted-vector lookup/invariant failure following the controlled deletions.
2. Make zbtIndexRecordHomeTag a no-op. Expected: lookup false negatives beyond the home
   bucket because its missing-member filter fails to reflect inserted hashes.

These intentional faults are test-strength controls, not optimisation candidates.
