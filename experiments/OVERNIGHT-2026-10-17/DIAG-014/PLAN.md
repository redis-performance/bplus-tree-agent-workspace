# DIAG-014 — compact cross-process predecessor intervention

Preregistered before measurement. AA-011 and DIAG-013's short-warmup rows selected
two compact targets with same-sign A/A bias across seeds: integer/no-output and
alternating-zero/score+length. Those observations motivate this new hypothesis,
not a claim that the mechanism is frequency or scheduler placement.

Hypothesis: the workload executed by the immediately preceding process changes
the next compact target's wall ns/item enough to matter at the 1% guard scale.
Use frozen HARNESS-006 source/binary, size95/bytes16/trimmed/forward, masks0(integer)
and6(alternating-zero), 20m requested items, ceil(20m/95)*95=20000065 effective items,
three warmup traversals. Target and predecessor each run in a fresh process.

Intervention A: predecessor is the SAME target case. B: predecessor is the OTHER
case. All runs use the target's seed. Immediately after each successful predecessor,
launch one target. Keep predecessor stdout/stderr in pre-opened files and defer all
hashing/CSV parsing/manifest serialization until the target has exited. There is no
intentional settling or sleep between predecessor and target. Record actual host
timestamps and monotonic gap. This avoids turning variable coordinator bookkeeping
into the intended intervention, but launch overhead remains part of the method.
The predecessor durations differ by workload; any effect concerns this combined
workload/duration intervention, not instruction mix alone, frequency or cache state.

Fixed seeds43103/43117, six ABBA blocks per target/seed, rotate target and seed order
by block. 96 target rows +96 predecessor rows, plus one prospective binary warmup
with 1m requested items. No additional rows, optional stopping or row exclusion.
Children<=120s, complete schedule<=300s. All children serial; no agents/builds/tests
or profiles during measurement. Stop and preserve a concrete failure rather than
repeating it. First complete BOUNDARY-015 and its fault controls.

Primary metric is target wall ns/effectiveitem; thread time, CPU endpoints and queried
QoS are descriptive. For each target/seed, six effects 100*(mean B / mean A -1),
95% Student-t df5 intervals. Support requires exact count/checksum/fingerprint/memory
invariants, all target windows>=10ms, and at least one target with BOTH seed intervals
entirely above +1% or both entirely below -1%. Otherwise hypothesis unsupported (or
invalid if controls fail). Report every target/seed, predecessor durations and gaps.
No precision-remedy claim, timing normalization, source selection, prior guard repair,
baseline count or performance headline. Preserve unresolved clock/migration uncertainty.
