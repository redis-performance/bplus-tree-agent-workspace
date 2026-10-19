# Latest M1 and M6 baseline charts

These figures use the two overnight baselines linked from the root README, not the
earlier M1 preparation run. Each host has 40 cells: eight operations, five sizes,
24 observations per cell. Dots show median batch-average ns/op; whiskers show the
full observed min–max. The combined chart overlays both hosts in each operation panel,
with blue circles for M1 and orange squares for M6. Each panel has its own y-axis.
These are host baseline costs with different compilers, not candidate gains.

![Apple M1 and M6 baselines overlaid](m1-m6-baseline.png)

[Combined SVG](m1-m6-baseline.svg) · [Individual M6 chart](apple-m6-baseline.png) ·
[Individual M1 chart](apple-m1-baseline.png)

[sources.json](sources.json) pins the exact published Git revisions, source paths
and SHA256 of both summary snapshots. The original host reports retain raw rows,
A/A variation and short-window checks. Both hosts remain separate; no pooled rows.
M6 uses Apple Clang 21 and M1 Apple Clang 17, both at -O3.

Reproduce from the repository root with matplotlib installed:

```sh
python3 scripts/plot-host-baselines.py experiments/NIGHT-EXPLORATION-001/baseline-charts
```

The generator verifies checksums, all 80 cells, 24 observations per cell and
min/median/max ordering before rendering. PNGs are embedded for GitHub display;
[Apple M6 SVG](apple-m6-baseline.svg) and [Apple M1 SVG](apple-m1-baseline.svg) are
also available for export. No benchmark rerun is needed to reproduce these charts.

## Architecture coverage

| Platform | Architecture | Baseline status | Host details |
|---|---|---|---|
| Apple M1 | arm64 | Measured | Apple Clang 17 |
| Apple M6 | arm64 | Measured | Apple Clang 21 |
| Intel | x86-64 | **NOT RUN** | CPU model, compiler and runner pending |
| AMD | x86-64 | **NOT RUN** | CPU model, compiler and runner pending |
| AWS Graviton | arm64 | **NOT RUN** | Generation, compiler and runner pending |

The combined chart reserves legend entries for the three unmeasured platforms.
It plots no values for them. sources.json keeps placeholders separate from measured
hosts; no zero-valued data or results from the HDR project are imported.
The architecture layout follows hdr-agent-workspace's C performance by architecture
section (local reference revision 9bf3a84). Actual hardware is selected only when
a B+ tree campaign is run on that host, using the same five-size/eight-operation
definitions and separate correctness, A/A, raw evidence and source/toolchain pins.
