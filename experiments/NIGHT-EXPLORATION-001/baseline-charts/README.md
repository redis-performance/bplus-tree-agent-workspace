# Five-host baseline charts

Measured Apple M1, Apple M6, AWS Intel Sapphire Rapids, AMD Zen5 and ARM NeoverseV2
baselines. Each host has40cells: eight operations, five sizes,24observations/cell.
Dots show median batch-average ns/op; whiskers show the complete observed min–max.
Each panel has its own y-axis. Host/compiler/placement differences are not
candidate gains. AWS runs inherit CPU2 affinity; Apple runs are unpinned.

![Five measured host baselines](m1-m6-baseline.png)

The original image URL is preserved. [Combined SVG](m1-m6-baseline.svg).
Individual charts: [M1](apple-m1-baseline.png), [M6](apple-m6-baseline.png),
[Intel](aws-intel-baseline.png), [AMD](aws-amd-baseline.png), [Graviton](aws-arm-baseline.png).

[sources.json](sources.json) pins published Git revisions, source paths and SHA256
of all five summaries. AWS baseline code/referee is8fab511e; raw evidence is pinned
at4e8edf65. All hosts completed native and ASan/UBSan validation. No pooled samples.

| Host | Compiler | Cells outside ±1% A/A | Placement |
|---|---|---:|---|
| Apple M1 | Apple Clang17 |39/40| Unpinned |
| Apple M6 | Apple Clang21 |36/40| Unpinned |
| AWS Intel | Clang18.1.3 |27/40| CPU2; SMT sibling50 |
| AWS AMD | Clang18.1.3 |30/40| CPU2; no SMT |
| AWS Graviton | Clang18.1.3 |19/40| CPU2; no SMT |

Each AWS host also has11cells with a shortest window below10ms. Small claimed gains
require fresh targeted controls and guards; this inventory does not qualify them.
All sources use-O3,16-byte members, seeds1/2/3 and six same-binary ABBA blocks.

Reproduce without rerunning benchmarks:

```sh
python3 scripts/plot-host-baselines.py experiments/NIGHT-EXPLORATION-001/baseline-charts
```

The generator verifies SHA256,200host cells,24observations/cell and min/median/max
ordering before rendering. PNGs are embedded for GitHub; SVGs are exportable.

[Source parity audit](source-parity.json): target source/header, referee, adapter,
vendored support, upstream test entry point and Makefile are byte-identical across
all five baselines. Compiler, OS, allocator and placement differences remain.
