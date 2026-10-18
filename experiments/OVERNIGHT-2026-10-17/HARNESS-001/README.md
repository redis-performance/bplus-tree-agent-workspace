# HARNESS-001 — duration and scheduling observations

Separate referee revision, 2026-10-17 round 1. No tree source changes. Base workspace
commit `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c`; source remains the pinned Redis PR head.
This is harness/baseline work, not an optimisation experiment or population round.

Changes: thread CPU time alongside primary wall time; boundary CPU IDs where supported;
queried QoS class/relative priority; fixed configurable lookup warm-up passes and measured
warm-up duration; complete repeated iterator/scan passes using ceil(ops/size), actual
visit/callback denominators, score checksums and full binary-member scan verification.
The scan reference permits duplicate callbacks, retaining the previous coverage checks.
Existing point/mutation cases and their checks remain intact.

## Method sources and API inspection

Called CPU Performance Engineering `ask` first with an exact methods question. Its
retrieved external passages were unrelated and are not evidence for this revision.
Then read methods, code and limits of both repository benchmarks:

- [05 measurement pitfalls](https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/05-measurement-pitfalls/README.md):
  consumed results, repeated observations, explicit warm-up and retained spread.
- [14 P/E cores](https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/14-pcore-vs-ecore/README.md):
  "Wall time is the primary measure" in its code; thread CPU time and boundary CPU IDs
  are supplementary observations. No M4 Pro measurements, numbering or frequencies adopted.

Inspected the installed macOS SDK `pthread.h`, `pthread/qos.h`, `_time.h`, and Mach
thread policy definitions before compiling. `pthread_cpu_number_np` is available since
macOS 11; its documentation explicitly does not guarantee the thread is still on that
CPU when the function returns. Runtime availability is guarded. `pthread_get_qos_class_np`
documents "Gets the requested QOS class and relative priority of a thread." Therefore
fields are labelled `qos_reported_*`, and `qos_effective=unknown`; overrides/clamps are
not observed. Linux uses sched_getcpu and unavailable QoS. No scheduling policy changed.
CPU numbers remain opaque. Clock/frequency, within-window migration and effective QoS
remain unknown. Raw thread/wall ratios are never clipped or substituted for wall time.

## Validation

Release and ASan/UBSan builds passed without compiler warnings. Original embedded tests
passed in both builds. `tests/test_microbench.py` passed all three groups in both builds:
binary lengths 8/16/319/320/321, sizes 1/31/128/1000, seeds 1/101, partial/full/repeated
traversal budgets, all eight cases, memory/count/checksum invariance and invalid warm-up
arguments. Each subprocess has a 120-second timeout. Logs and commands: [validation](validation/).
Smoke rows are functional evidence only, not performance comparisons.

Sequential review (same coordinator, not independent agents): checked scan duplicate
semantics against zbtreeScan, which does not mutate its tables; checked size/count bounds,
unchanged assertions, timer order, unsupported-platform sentinels, and SDK QoS semantics.
Attempt to start a separate reviewer failed before any agent ran (thread-store context
load error). No independent reviewer or token cost is invented. Backend/model unknown;
supervisor records actual CLI token usage separately.

Decision: harness validated locally; baseline requalification required. Commit status
and frozen file/binary provenance are recorded separately before measurement. No source
candidate selected (`NONE`); optimisation counts remain 0 accepted / 0 rejected / 0 parked.
