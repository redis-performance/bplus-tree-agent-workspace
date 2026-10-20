# TMA in every experiment report

Required for Codex and Claude, including follow-ups and parked/rejected work.
Use [topdown-profiler](https://github.com/redis-performance/topdown-profiler);
the CPU-perf methodology consultation remains a separate requirement.

Include this classification **inside each new experiment report**. Historical
sealed reports retain their original bytes and have adjacent `TMA.md` supplements,
listed in the [coverage index](../experiments/TMA-COVERAGE.md).

```text
Pipeline Slots (100%) — <architecture / workload / baseline or candidate>
├── Frontend_Bound      <measured %>  Instruction supply
├── Bad_Speculation     <measured %>  Wrong-path/discarded work
├── Backend_Bound       <measured %>  Data supply / execution
│   ├── Memory_Bound    <measured %>  Include measured L1/L2/L3/DRAM children
│   └── Core_Bound      <measured %>  Execution resources / dependencies
└── Retiring            <measured %>  Retired work
```

The four L1 shares describe the same denominator and sum to approximately 100%.
Children are shares of **total slots**, not a second independent 100%; show only
supported/measured children. Preserve residuals and rounding rather than silently
rescaling. Retiring includes overhead: a higher fraction alone is not a speedup.

Beside the tree, include:

- Exact machine architecture, source and binary hashes, compiler/flags, workload,
  fixture, seed, CPU/PID/core scope and SMT sibling state.
- Tool/collector version, capture commands and run IDs, raw output/checksums,
  window count/duration, multiplexing/unsupported events and variability.
- Baseline and candidate trees from matched captures. State the next falsifiable
  question and what observation would rule it out. TMA does not replace timing gates.

If no valid capture exists, retain the four category names with `unavailable`,
explain why, and name the required collection. Never invent numbers to fill the tree.
Linux ARM/AMD collector coverage differs from Intel; label approximations and
unsupported levels. Apple PMU data is not interchangeable with Neoverse TMA.

Before collecting, verify the glue's actual command. Upstream `71dea5e` and the
observed Intel 0.2.2 deployment select CPU0 when given PIDs. Our explicit CPU2
diagnostic bypasses that path through `ToplevOptions(pids=None, extra_args=['-C','2'])`;
it measures CPU-wide activity and must be labelled accordingly. Preserve raw CSV:
the current analysis filter drops toplev `% Slots` units and may rank `MUX` instead.
See the [measured assessment](../experiments/TOPDOWN-ASSESSMENT-20261020/README.md).
