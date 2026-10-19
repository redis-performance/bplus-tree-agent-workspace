# Corrected ARM NEON discovery result

Discovery complete: 144 processes / 36 complete paired blocks, serial CPU2. Population decision: **REJECT; source NONE**. All three candidates failed both primary performance gates in every block. Source adoption remains **NONE**. This is the distinct corrected-adapter baseline 13e459ff8; original 8fab failed controls remain final.

| Variant | Size | Paired effect range | Median | All six primary gates |
|---|---:|---:|---:|---|
| A | 100000 | +96.8901% to +102.0134% | +100.1689% | False |
| A | 1000000 | +68.9822% to +72.4014% | +69.8977% | False |
| B | 100000 | +76.6525% to +78.5938% | +78.1607% | False |
| B | 1000000 | +54.8418% to +55.8272% | +55.3419% | False |
| C | 100000 | +98.8941% to +101.7997% | +100.0746% | False |
| C | 1000000 | +68.3541% to +69.8445% | +69.4570% | False |

Every-block primary survivors, in preregistered maintenance order: NONE. Selected solely for further gates: **NONE**. This does not rank implementation speed or establish acceptance.

Run interval: 2026-10-19T05:20:35.630388+00:00 to 2026-10-19T05:24:11.265724+00:00; 215.635 seconds within the fixed 300-second cap. No retries, excluded rows, source changes or count changes. All observed fixture checksums, actual operations, owned memory, traversal and warmup counts match within each paired block. Frozen source/referee and binary identities passed checks before and after the complete schedule.

Correctness: prior frozen validation passed 145 command outcomes, including eight original 43-test runs, 56 semantic suite runs, six forced-portable V2 runs and eight detected faults. The overread negative was detected through the cardinality assertion; it is not evidence of a negative guard-page signal. Root and independent AMD coverage reviews preceded timing.

No candidate is eligible for confirmation or acceptance because all failed discovery. Independent confirmation, all required qualified guards, matched profile and independent final review would have been required for any survivor. The held-out confirmation contract was committed at 0d5650c24 before discovery data; its conditional execution is not triggered because no primary survivor exists. Missing or noisy guards mean PARK. No source is adopted.

Raw per-process stdout/stderr and exact command records are in screen/. screen-audit.json reconstructs the fixed schedule, serial intervals, paired invariants and every effect. comparison-freeze.json binds the exact original AA timing binary and three implementation binaries. No timings are pooled with another host or older adapter identity.
