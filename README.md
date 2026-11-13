# Standalone B+ tree experiments

Packed B+ tree and compact member-index benchmarks from [Redis PR #15635](https://github.com/redis/redis/pull/15635). Standalone C; no Redis server.

**35 experiment attempts: 18 parked · 17 rejected · 0 approved.**
ARM 25 · Intel 5 · AMD 5. Includes 23 new populations, 5 replications and 7 qualification attempts; shared Apple history counted once. Tree source unchanged.

Historical architecture charts (through20 October; current counts above):

![Experiment outcomes by architecture](experiments/EXPERIMENT-FLOWS-20261020/overview.png)

**Experiment flows:** [All experiments](experiments/EXPERIMENT-FLOWS-20261020/all-attempts.svg) · [ARM](experiments/EXPERIMENT-FLOWS-20261020/arm.svg) · [Intel](experiments/EXPERIMENT-FLOWS-20261020/intel.svg) · [AMD](experiments/EXPERIMENT-FLOWS-20261020/amd.svg) · [Follow-ups](experiments/EXPERIMENT-FLOWS-20261020/followups.svg) · [Evidence ledger](experiments/EXPERIMENT-FLOWS-20261020/README.md)

## What matters

**Current-unstable ARM lookup:** exact baseline `ee8e7f701`;12/12 A/A blocks pass. Three scalar variants improve discovery medians1.39–1.84%, below the2% gate. Rejected; source selection NONE. [Results](experiments/ARM-LOOKUP-GAP-001/RESULTS.md).

**Intel follow-ups:**16 configurations /48 TMA windows pass. Iterator B: Memory Bound34.07→28.15% at1M; strongest parked lead, no speedup claim. [Results and next gates](experiments/INTEL-FOLLOWUP-001/README.md).

- **ARM mask:** primary gains survived, but qualified guards regressed. [Rejected](experiments/ARM-MASK-FOLLOWUP-001/RESULTS.md).
- **Intel scan:** primary gains and confirmation passed; a qualified guard regressed. [Rejected replication](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/014-scan-supplement/README.md).
- **AMD scan / Apple decoder leads:** unresolved controls or guards prevent adoption. [Decisions](experiments/EXPERIMENT-FLOWS-20261020/README.md).
- **Latest M6 lookup:** clock-bracket harness validated; 1M precision still fails. [Parked](experiments/M6-CLOCK-BRACKET-001/RESULTS.md).

## Run

C11 compiler, Make and Python 3; macOS or Linux.

```sh
make -j2
make check
make sanitize
build/btree-bench --size 100000 --ops 1000000 --member-bytes 16 --seed 1
```

[Tree benchmark guide](docs/MICROBENCHMARKS.md) · [Decoder guide](docs/DECODER-MICROBENCHMARK.md) · [Five-size matrix](experiments/SIZE-MATRIX-001/README.md)

## Evidence and rules

[Five-host baselines](experiments/NIGHT-EXPLORATION-001/baseline-charts/README.md) · [Corrected-adapter baselines](experiments/NIGHT-EXPLORATION-001/corrected-adapter-charts/README.md) · [Experiment log](experiments/EXPERIMENTS.md) · [Summary](experiments/SUMMARY.md)

Acceptance requires correctness, qualified controls and guards, profiles, fresh confirmation and independent review. [Population protocol](docs/POPULATION.md) · [Required performance MCP workflow](docs/PERFORMANCE-MCP.md)

[Source](src/) · [Tests](tests/) · [Source manifest](source-manifest.json) · [Extraction notes](docs/STANDALONE.md) · [Licensing](NOTICE.md)
