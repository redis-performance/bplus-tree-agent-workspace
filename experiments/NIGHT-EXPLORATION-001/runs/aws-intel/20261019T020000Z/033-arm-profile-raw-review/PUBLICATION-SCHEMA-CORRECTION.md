# Metadata-only publication correction

First local audit of immutable266360cfb stopped before row reconstruction: PUBLICATION.json includes38 explicitly private-only perf.data entries without public_sha256. The initially frozen auditor e7c5a3b16 tried to open the first unavailable .data path. Original auditor/freeze remain in Git history. This correction checks all public hashes, requires the exact private-only declaration and .data suffix, and joins all38 private raw hashes exactly to result.json. It does not assert rehashing unavailable binaries.

The same metadata revision adds explicit published preflight/postcheck/helper receipt schema joins (source identities, lease/slice/CPU, complete frozen inputs, timer/preflight state, empty owned units/PIDs, serial timestamps and whole1200s wrapper bound). No raw arithmetic, samples, counters, scope/mapping thresholds, workload or producer artifact changed. This is local evidence reprocessing, not measurement retry.
