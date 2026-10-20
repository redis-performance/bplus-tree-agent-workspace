# Intel iterator: measured TMA assessment

**Baseline classified; no candidate accepted.** Twelve 10-second captures on Intel
Sapphire Rapids: six L2 classifications and six exploratory L3 drill-downs.
Source remains NONE; all 33 historical decisions are unchanged.

## TMA classification

Clang 18, `-O3`, integer scores, forward iteration, all outputs (`mask=7`),
16-byte members, seed7103. Each tree is the arithmetic mean of 30 one-second
intervals from three L2 captures. All L2 events report **100% scheduling**.

```text
Pipeline Slots (100%) — Intel baseline, 100,000 members
├── Frontend_Bound       0.8%                                    Instruction supply
├── Bad_Speculation      3.2%  █                                 Wrong-path/discarded work
├── Backend_Bound       13.2%  █████                             Data supply / execution
│   ├── Memory_Bound         8.5%  ███                               Memory stalls
│   └── Core_Bound           4.7%  ██                                Execution / dependencies
└── Retiring            82.7%  █████████████████████████████████ Retired work, including overhead
```

```text
Pipeline Slots (100%) — Intel baseline, 1,000,000 members
├── Frontend_Bound       0.7%                                    Instruction supply
├── Bad_Speculation      2.8%  █                                 Wrong-path/discarded work
├── Backend_Bound       22.0%  █████████                         Data supply / execution
│   ├── Memory_Bound        16.5%  ███████                           Memory stalls
│   └── Core_Bound           5.5%  ██                                Execution / dependencies
└── Retiring            74.5%  ██████████████████████████████    Retired work, including overhead
```

L1 sums are 99.92% / 99.97% before display rounding; no renormalization.
Retiring is a slot classification, not proof that every instruction is useful or
that increasing this percentage makes a program faster.

## What this changes

**Memory Bound grows 8.55% → 16.47% of slots with tree size; Frontend Bound remains
below 1%.** This prioritizes a matched test of the existing Intel B cached-offset
patch over a generic instruction-supply hypothesis. It does not establish B's cause
or benefit: no candidate was captured here.

The next comparison must qualify its baseline first, then report baseline/B trees,
cycles and instructions per visited element, and qualified primary/guard timings.
The hypothesis is that B removes iterator work/dependent loads. No reduction in
work/cycles, or a qualified guard loss, rules out advancing that exact patch.
A smaller stall percentage alone is insufficient; previous PARK remains.

## Deeper diagnostics: different denominators, limited scheduling

L3 captured **8–16% event scheduling** for most measured events. These raw metrics
are exploratory and are deliberately outside the slot trees:

| Metric | 100K mean | 1M mean | Collector denominator |
|---|---:|---:|---|
| L1_Bound | 1.02% | 1.30% | `% Stalls <` |
| L2_Bound | 0.10% | 0.20% | `% Stalls <` |
| L3_Bound | 8.14% | 16.13% | `% Stalls <` |
| DRAM_Bound | 0.01% | 0.00% | `% Stalls <` |
| Ports_Utilization | 16.32% | 14.77% | `% Clocks <` |

These are not additive shares of total slots. The L3 signal suggests checking
LLC-hit latency with a smaller event set; it does **not** establish DRAM saturation,
justify a prefetch patch, or qualify any candidate. Do not pool L2 and L3 captures.

## Glue defects reproduced on these measurements

1. **Wrong CPU scope:** deployed 0.2.2 and upstream `71dea5e` translate a supplied
   PID into `-C 0`. This diagnostic uses the glue's `ToplevRunner` with explicit
   `-C 2`, no PID argument, and checks workload affinity before each capture.
2. **Wrong bottleneck ranking:** unmodified `query_bottlenecks` returns **MUX**;
   its unit filter excludes the actual `% Slots` / `% Slots <` categories.
3. **Misleading funnel:** `get_funnel` includes MUX as another root and renders
   `% Stalls`, `% Clocks` and `% Uops` children as though they were pipeline slots.
   The report generator instead admits only the four known roots and exact slot
   units; deeper incompatible units retain their original labels.

[Actual MCP calls](topdown-mcp-calls.json) · [Reconstruction/reproductions](analyze.py)
· [Validation](VALIDATION.json). No upstream installation or PR was changed.

## Provenance and limits

- Tree source: `f20711d9a1e90c72218ac3adf3ef4cafcd3f36cf`; original tree/referee files
  unchanged. [Source/binary hashes](evidence/l2/inputs-sha256.txt),
  [compiler/tool metadata](evidence/l2/environment.json),
  [CPU2 collector command](evidence/l2/collector-command.json).
- Native original correctness **43/43**, plus a completed 100K iterator smoke with
  matching checksum. The separate diagnostic driver adds a readiness stop after
  fixture/oracle/warmup and multiplies requested operations by200. It is **not** a
  qualified timing binary; no speed or historical-profile transfer is claimed.
- Each long diagnostic process remains alive through its three windows and is then
  terminated. Post-run whole-workload checksum validation is therefore unavailable.
- CPU-scoped collection includes any activity on CPU2. L3 `/proc` snapshots show
  CPU2 100% busy, sibling50 0% busy, and workload accounting within three ticks of
  CPU2 busy time. L2 sibling occupancy was not recorded; SMT was not disabled.
  Clock state/NUMA residency and independent confirmation remain unmeasured.
- Collector: installed topdown0.2.2, pmu-tools2026.4.7.0, model5.1-full;
  controller analysis/MCP: topdown0.3.1 at `71dea5e`, isolated SQLite. Run IDs in
  [analysis.json](analysis.json) identify imported captures; DB wall times are
  explicitly ingestion times. Raw interval timestamps are preserved.
- [L2 raw evidence](evidence/l2/), [L3 raw evidence](evidence/results/),
  [failed initial operation-cap launch](evidence/attempt001/). No samples were
  discarded from successful captures; the failed launch produced none.
- Intel coordinator restored and recovery timer inactive; no remaining owned
  workload. ARM/AMD SSH checked, but their services and workloads were not changed.
- Single Codex controller; exact model/token costs unknown. No independent reviewer
  or optimization population was run. CPU-perf consultations are recorded separately;
  its library has 0/287 sources indexed, so it supplies no retrieved supporting passages.

[All experiment TMA classifications](../TMA-COVERAGE.md) ·
[Reporting rule](../../docs/TMA-REPORTING.md) · [Activity](ACTIVITY.md)
