# Latest M6 candidate screen

PNG/SVG and exact chart JSON copied from M6 revision `913d22e924d84599c8b4b14eee802c12b9b28fa9`.
All implementations fail the declared dual-primary gate; source unchanged.
Negative values are elapsed-time reductions. Segments are observed six-block
min–max, not confidence intervals.100Kcontrols qualify;1Mcontrols fail.

[Result](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/913d22e924d84599c8b4b14eee802c12b9b28fa9/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/RESULTS.md), [reproduction script](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/913d22e924d84599c8b4b14eee802c12b9b28fa9/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/plot-results.py),
[independent raw audit](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/913d22e924d84599c8b4b14eee802c12b9b28fa9/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/INDEPENDENT-AUDIT.md). Source directory contains
all frozen reproduction inputs; this folder contains presentation copies.


# Intel scan discovery

`intel-scan-discovery.png/svg/json` are generated directly from the independently
reconstructed [raw audit](../reviews/aws-intel-scan-raw-audit.json), worker discovery
revision5534ca6e7. Reproduce with `python3 scripts/plot-intel-scan-discovery.py` from
the repository root. Every dot is a paired ABBA effect; lines are observed ranges,
not confidence intervals. The shaded band is±1%; both baseline A/A controls qualify.
B advances by preregistered source preference, not a claim of superiority over A.
Guards, fresh confirmation and profile validation remain; source NONE. This chart
is a discovery checkpoint, not a portable or whole-operation-suite performance claim.
