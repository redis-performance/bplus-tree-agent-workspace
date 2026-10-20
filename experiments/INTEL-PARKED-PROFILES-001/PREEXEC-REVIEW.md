# Independent profile-sweep review

**GO for the frozen diagnostic sweep. No timing acceptance, candidate adoption or retry authorized by this review.** Reviewer `/root/intel_b_review`, Codex; exact model/token costs unknown. No remote execution by reviewer.

Coverage is36 configurations: iterator baseline/A/B ×6 cells; corrected SCAN baseline/B ×4 cells; baseline update ×10 cells. The two failed iterator guard contracts use exact seed1. Source identities/retained patches are fixed; rejected lookup, iterator C and old-source SCAN remain rejected. Smaller update sizes and broad baseline013 qualification debt remain explicitly outside this triage sweep.

Reviewed readiness hooks occur after fixture construction/oracles/warmup and before profiled work. Extended counts preserve original semantic checks, and iterator/scan rounding bounds are guarded. Frozen20B guard passes and fixture sizes fit unsigned64-bit counts; checksum modular arithmetic is intentional. Long workloads terminate without end-of-run oracle completion; completed native/sanitizer checks are separate prerequisites.

Initial blockers resolved before freeze:

- Original/profile parity includes owned bytes within native mode. Sanitizer logical parity excludes allocator-dependent tree bytes across modes; baseline/candidate comparisons retain full owned-byte equality separately within native and sanitizer modes.
- Timeout partial streams and command/return codes are retained. Counter/sample/report failures become explicit partial collection rather than success. Actual watchdog preambles are preserved and CSV parsing starts at its unique header.
- L2 qualification requires every row's scheduling value, all exactly100%, and five complete sets of four finite slot roots summing100±0.3pp. CPU2 affinity, alive workload, sibling≤1% and workload/CPU accounting≤1% are checked; invalid affinity aborts the configuration. Invalid quality is retained, not retried.
- Active containers abort the sweep. Coordinator stop, owned reservation marker,40minute process-group timeout/cleanup and45minute recovery timer bound runner use. Controller still owns live lease verification and restoration audit.

Three5-second L2 windows, one exploratory L3 window, grouped counters and PID-only cycles samples are collected serially per configuration. Source/build and raw capture identities are retained. Python and shell syntax and36-configuration cardinality pass static review; actual runner validation remains pending.

Interpretation limits remain material: L3 mixed units/low scheduling cannot be added to the slot tree; unsupported counters/lost samples must remain disclosed. No instructions/cycles per operation without observed in-window work. Update tree state changes through sequential windows, so their distributions cannot be assumed stationary. CPU-wide accounting and snapshots do not prove zero interference or constant frequency. This profiler host cannot explain the previous secondary host's A/A failure causally. Higher Retiring or lower Memory_Bound alone is not a throughput improvement.

Own fresh cpu-perf availability and concrete `ask` are in [reviewer-consultation.json](reviewer-consultation.json): checkout`a5a05e6bf7c9`,0/287 sources indexed, no supporting passages. The tool was used without presenting unread leads as evidence. [Inventory](INDEPENDENT-INVENTORY.md) records historical boundaries and excluded rejected work.

## Reviewed hashes

- `protocol.json`: `08d9727e7d82ca0fd3f7e05a71c1b9c8f52ad5700aa7d0d31c7a60e99405f7d3`
- `prepare.py`: `5eda56078be2f5889e26f37cee4df4d2c3c4295a0fd6b2149b9a2144297a8f89`
- `work.py`: `e823303cd9dba8243fa557ab3d238950c54808429df1152ff8949023114f2539`
- `collect.py`: `c5a5fb090ed95ec7c97bd925fcd6be4c5df3d9e12e1bdba61606f10076609348`
- `run.sh`: `39f2b9842dc399dac5a5f9cf0fd63ae3ff440a9d05ac786b02d4f09287c1286f`
- `ready.c`: `68d5d3a2895463d2bab1df5030cb4d27d54d7911c742bc018bbbb3bfa4e0f886`
- `input-manifest.json`: `8fcd669904f1a45adfe953efbd1384e75f28c9159163c105c75a0cf27a69d1f6`

Reviewed UTC: 2026-10-20T14:14:46.644382+00:00
