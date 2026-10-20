# Activity — 20 October 2026

- Read shared state and mandatory CPU-perf workflow; checked main at `f20711d9a`.
- Found fleet in the explicitly supplied OSS workspace at `.claude/fleet.md` after
  initially checking the wrong location. SSH succeeded for Intel/AMD profilers and
  secondary ARM. Only the idle Intel profiler was reserved for bounded diagnostics.
- Inspected topdown upstream `71dea5e` and deployed Intel0.2.2. Reproduced hardcoded
  CPU0 for a supplied PID. Used existing collector `extra_args` for explicitCPU2.
- Reserved Intel with a local flock, stopped its idle coordinator, armed independent
  recovery. Original43 tests and100K smoke passed. First launch failed the existing
  100M operation cap before capture; evidence retained and coordinator restored.
- Added a separate readiness/long-window diagnostic driver, preserving the original
  driver and tree. Captured3×10s L2 windows at100K and1M. Restored the coordinator.
- New L3 drill-down after L2 result: same binary,3×10s at each size, with workload/
  CPU2/sibling50 accounting. Restored coordinator again; final live check confirmed
  RUNNING, recovery timer inactive and no owned iterator process.
- Reconstructed all3240 raw metric rows. L2 100% scheduling; L3 mostly8–16%, with
  incompatible Slot/Stall/Clock/Uop denominators. Preserved all captures and limits.
- Imported exact captures into an isolated controller SQLite database, with labelled
  ingestion timestamps. Made six real topdown MCP calls: list, query, three funnels,
  explain. Reproduced MUX-only ranking and mixed-unit funnel defects.
- CPU-perf library_status/ask called before collection and after findings: zero
  indexed supporting passages. Bibliographic suggestions are not causal evidence.
- Added measured TMA report, per-experiment historical supplements (33 attempts in31
  files), coverage index and mandatory Codex/Claude report rule. All historical source
  report hashes remain intact. No source adoption, new population, candidate timing,
  upstream change or current runner lease. Exact model/token costs unknown.
