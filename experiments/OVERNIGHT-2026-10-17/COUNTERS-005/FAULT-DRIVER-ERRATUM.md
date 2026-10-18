The no-reversal child aborted at the intended structural predicate. The zero-sign child
also aborted, but at the earlier iterator-copy exact-score check (mask0) rather than the
later direct-score output assertion anticipated by the driver. The driver therefore
failed after preserving both raw children and marked the second detection false.

The read-only audit matches the actual earlier predicate and SIGABRT against unchanged
stderr hashes. Both faults were detected by meaningful intended oracles; no child was
rerun and no oracle/source/measurement rule was weakened. Original driver/manifest stay
unchanged. `fault-audit.json` is the corrected sensitivity classification.
