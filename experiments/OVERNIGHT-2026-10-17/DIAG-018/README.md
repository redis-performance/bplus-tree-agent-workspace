# Observed completion delay — locally supported and repeated

Discovery and fresh reversed-order confirmation each complete48 benchmark rows plus
one prospective warmup. Both stages meet the preregistered observer-to-parent-return
wall-delay criterion on both seeds. This identifies a local completion-transport
effect; it does not establish a stable benchmark clock or a precision remedy.

The POSIX wrapper blocks in waitpid, records its observation of child completion,
and returns. Python measures its return using the same CLOCK_MONOTONIC clock.
The interval includes observer output/teardown and parent scheduling; it is not the
exact kernel-exit delay. The wrapper changes the launch environment. Benchmark wall
A/A precision remains mixed, and DIAG-017's failed precision criterion is unchanged.
No timing policy is adopted and no original source guard is replaced.

Six transport/status/timeout controls pass: binary stdout/stderr, nonzero exit-code
propagation, and alarm-triggered kill/reap under both transports. The wrapper's own
110-second child bound precedes Python's120-second wrapper limit. Every observation
and failure remains. No source or referee changes were made for these timings.

[Plan](PLAN.md), [observer source](wait_observer.c), [freeze](freeze.json),
[validation](validation.json), [discovery manifest](manifest.json), [summary](summary.json),
[confirmation plan](CONFIRM-PLAN.md), [fresh manifest](confirm/manifest.json),
[fresh summary](confirm/summary.json). Discovery/fresh confirmation are separate
sequential coordinator passes, not independent agents or machines.

Local M1/macOS26.3, one benchmark thread; unchanged HARNESS-006, ambient allocator,
Apple clang17 O3. Observer uses C11/O2; exact commands are retained. Frequency/core
residency/effective QoS unknown; no M4 result transferred. Evidence checker returns
no_number on the qualitative claim. Diagnostic26; source NONE, EXP-004 A/PARK and
EXP-005 PARK/NONE unchanged. Exact backend/model/token cost unknown.
