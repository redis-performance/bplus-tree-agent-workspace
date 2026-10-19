# Campaign chart index

## M6 caller specialization (006)

PNG/SVG and exact chart JSON copied from M6 revision `913d22e924d84599c8b4b14eee802c12b9b28fa9`.
All implementations fail the declared dual-primary gate; source unchanged.
Negative values are elapsed-time reductions. Segments are observed six-block
min–max, not confidence intervals.100Kcontrols qualify;1Mcontrols fail.

[Result](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/913d22e924d84599c8b4b14eee802c12b9b28fa9/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/RESULTS.md), [reproduction script](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/913d22e924d84599c8b4b14eee802c12b9b28fa9/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/plot-results.py),
[independent raw audit](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/913d22e924d84599c8b4b14eee802c12b9b28fa9/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/INDEPENDENT-AUDIT.md). Source directory contains
all frozen reproduction inputs; this folder contains presentation copies.


## Intel scan discovery

`intel-scan-discovery.png/svg/json` are generated directly from the independently
reconstructed [raw audit](../reviews/aws-intel-scan-raw-audit.json), worker discovery
revision5534ca6e7. Reproduce with `python3 scripts/plot-intel-scan-discovery.py` from
the repository root. Every dot is a paired ABBA effect; lines are observed ranges,
not confidence intervals. The shaded band is±1%; both baseline A/A controls qualify.
At this discovery checkpoint, B advanced by preregistered source preference.
The [current decisions](../AWS-DECISIONS.md) record the later guard outcomes;
source remains NONE. This chart
is a discovery checkpoint, not a portable or whole-operation-suite performance claim.

## M6 adapter/compiler-contract diagnostic

Pinned source: [7c8f5c0bd results](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/7c8f5c0bd/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/012-contract-diagnostic/RESULTS.md), [raw independent audit](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/7c8f5c0bd/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/012-contract-diagnostic/INDEPENDENT-AUDIT.md), [reproduction and exact data](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/7c8f5c0bd/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/012-contract-diagnostic/CHART.md). Copied PNG/SVG/data are byte-identical to that commit. All eight effects conditional (zero ofeight workloads qualify controls onbothadapters); no tree acceptance or candidate population. The source tree and exact owned memory are unchanged. Six points and observed ranges are not confidence intervals.

## M6 exact decoder replications

The combined four-panel chart shows EXP-004 focused scalar decoding, EXP-007
private bulk variants, EXP-008 cutoffs and EXP-007 A fresh same-M6 confirmation.
All six paired block effects, observed ranges, medians and relative A/A controls
are retained. All individual windows are below10ms; full qualification is0/210
discovery cells and0/30 fresh cells. No tree adoption or independent-machine
confirmation is claimed. The original legacy adapter remains part of this frozen
replication identity; the corrected baseline stays separate.

Pinned source: `a9df242d4c0b68c4c1bc6482a155f7d16c199a7f`. [Report](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/a9df242d4c0b68c4c1bc6482a155f7d16c199a7f/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications/RESULTS.md),
[data](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/a9df242d4c0b68c4c1bc6482a155f7d16c199a7f/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications/decoder-replications.json),
[plot script](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/a9df242d4c0b68c4c1bc6482a155f7d16c199a7f/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications/plot.py),
[raw and audits](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/a9df242d4c0b68c4c1bc6482a155f7d16c199a7f/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications).
From that checkout, run `python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications/plot.py` with Matplotlib.
The main copies are byte-identical PNG/SVG/JSON artifacts.

M6 member-index profile: `m6-member-profile.{png,svg,json}` is pinned to source commit `0e7325081`. Regenerate from the source directory with `uv run --with matplotlib python <source-directory>/plot.py`. The figure conserves all 16 captures and 2,469 observations; counts do not establish costs, time shares or speed. File hashes are in `m6-member-profile-publication.json`.

M6 fresh SCAN controls: `m6-neon-aa.{png,svg,json}` is pinned to 8bcd75d704eae2b4f45131531a3d8177cb852c09. Regenerate with `uv run --with matplotlib python <source-directory>/plot-aa.py`. All twelve A/A blocks are shown; no candidate comparison ran. File hashes are in `m6-neon-aa-publication.json`.


ARM exact historical mask replay: `aws-arm-mask-primary.{png,svg,json}` retains all
12 qualifying baseline A/A effects and12 candidate primary effects. Screen source
`6bcd8e575`, baseline source `73c9e313f`, root control audit `27a4afee1`. Decision PARK,
no source adoption: guards, fresh confirmation and matched candidate profile remain
missing. Medians−7.766545%/−7.101923% are elapsed changes in forward score-only16B/50M
visits, not a general tree improvement or causal instruction-cost estimate.
Regenerate from the repository root with `python3 scripts/render-aws-arm-mask-primary.py`.
The JSON records exact effects, artifact hashes and renderer hash. Root visually
inspected the figure; plotted values independently agree with raw audit and Intel
16f074fbe. Original baseline/discovery artifacts are unchanged.
