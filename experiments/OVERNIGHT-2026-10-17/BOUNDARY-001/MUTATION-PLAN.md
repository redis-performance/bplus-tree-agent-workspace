# Oracle discrimination controls

After the unmodified baseline passed release and ASan/UBSan, test four intentional
faults in separate scratch source files. These are test-strength controls, never
optimisation implementations/population variants. Preserve each patch/build/output.

1. Normalize decoded signed zero to positive zero.
2. Truncate raw lookup member length at the first NUL byte.
3. Return forward rank one too large.
4. Suppress scan callbacks for 320-byte members while preserving cursor progress.

Expected outcome for each: the new oracle fails, with a specific semantic assertion.
A build failure or timeout is inconclusive, not a detected fault. Each child <=120s.
Do not apply any fault to root source or the frozen A/A snapshots. No timings/claims.
