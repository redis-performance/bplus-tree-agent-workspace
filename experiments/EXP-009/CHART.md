# EXP-009 fresh baseline A/A chart

The chart displays all six control blocks at each primary size:100K6/6 qualify,1M3/6 qualify. All48windows exceed10ms. Every run uses the same unchanged baseline binary; these points are not candidate gains. The fixed±1% band and every failed block remain visible.

- [PNG](aa-controls.png), [SVG](aa-controls.svg), [exact data and all48retained rows](aa-controls.json).
- [Source summary](bench-results/aa/summary.json), [all96raw streams](bench-results/aa/public-raw-manifest.json).
- [Decision and limitations](RESULTS.md).

Reproduce from the repository root with the existing offline plotting environment:

```sh
uv run --offline --with matplotlib python experiments/EXP-009/plot-aa.py
```

The renderer independently reconstructs every block's integer gate, verifies it against the retained summary and records input/artifact checksums. The generated JSON identifies the plotting version and source hashes. Point labels are rounded for display; decisions use exact integers. Window ranges are observed extrema, not confidence intervals or individual-query latency percentiles.
