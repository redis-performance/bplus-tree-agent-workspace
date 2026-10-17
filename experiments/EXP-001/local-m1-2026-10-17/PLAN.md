# Local baseline and CPU-methodology exploration

User authorisation (2026-10-17): run microbenchmarks locally and explore the CPU
Performance Engineering methodology via its MCP. This scopes the run to this Mac,
overriding the default dedicated-runner preference for this experiment.

Baseline source/harness: workspace 0a36e68475b2ead629d98ed3fb4cda32a8332139;
tree files remain identical to PR head a7ecd959374d66847c095250bf2d373edf7316c5.
No source or referee modification is planned. Initial 100K/16-byte calibration is
recorded separately and excluded from analysis. Builds finish before measurements.

## Preregistered measurement

- Apple M1, 4 performance + 4 efficiency cores, 16 GiB RAM; one benchmark thread.
- macOS 26.3; Apple Clang 17.0.0; C11 -O3 -g -Wall -Wextra
  -fno-omit-frame-pointer; libc; no LTO, fast-math or native-architecture flag.
- No affinity or fixed frequency. Actual executing core, DVFS frequency and turbo
  state are unobserved. No SMT. No P-core residency claim. Record load averages.
- A and B are the exact same binary, with checked SHA-256 and no source change.
- Six ABBA blocks, four fresh processes per block/cell. Cells rotate within each
  block; each ABBA group is serial. No concurrent profiling or compilation.
- Cells: all eight cases at 1K/16 bytes and 100K/{16,319,320,321} bytes, 1M requested
  point operations; lookup-hit alone at 1M/16 bytes, 10M operations. Seed 1 throughout.
- Use the harness's existing pre-generated inputs, shuffled repeated permutation,
  lookup warm-up and post-timing checks. No claim of cache-cold or iid access.
- Collect every raw row. No outlier deletion. Report per-cell median/min/max/CV,
  block-paired B/A effects, and a 95% Student-t interval over six block effects.
  That interval is descriptive and assumes independent approximately normal block
  effects; six blocks on a shared laptop cannot establish universal precision.
- Qualify a cell only if its entire interval lies within +/-1%, and every timed
  interval is >=10 ms. This is a conservative campaign control, not a source rule.
  Short traversal cases stay exploratory rather than changing the frozen harness.
- Budget: 600 seconds for the matrix; each child <=90 seconds. If exhausted, record
  incomplete cells and do not count them as qualified. Stop on correctness failure.

## After timing

Sample separate long-running lookup/update processes using macOS sample if permitted.
Profiles are diagnostic and excluded from timing aggregates; capture may include
setup/cleanup. Inspect optimised generated assembly and compiler remarks for sampled
functions. Lack of PMU counters means no asserted cache/branch/stall bottleneck.
Record evidence-backed follow-up measurements; no population selection or optimisation
acceptance in this baseline-only experiment.

## MCP use

Consulted cpu_perf.ask, get_benchmark(05-measurement-pitfalls), and read_source for
Hoefler/Belli's scientific benchmarking paper. Apply consumed results, repeated fresh
processes, explicit warm-up, machine/build/workload provenance, spread/uncertainty and
generated-code inspection. Do not transfer the library's Apple M4 Pro timings to M1.
Exact queries and source links are recorded in METHODOLOGY.md.
