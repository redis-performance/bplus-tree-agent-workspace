# Standalone B+ tree experiments

Packed B+ tree and compact member-index benchmarks from [Redis PR #15635](https://github.com/redis/redis/pull/15635). Standalone C; no Redis server.

**Overnight continuation active through 14 November,07:24UTC.** Current baseline is Redis unstable [`ee8e7f701524`](https://github.com/redis/redis/commit/ee8e7f70152404649ac947157fd662d11b4a00d5). Three helper-boundary candidates are rejected: the best membership gain(6.79%) regresses guards. H2-B passes all original and supplemental ARM/Intel guards; fresh confirmation remains. H3 is rejected after Intel guard failures. Further independent hypotheses remain active. [Live status](experiments/ARM-LOOKUP-CONT-001/STATUS.md) · [Queue](experiments/ARM-LOOKUP-CONT-001/OVERNIGHT.md) · [Helper results](experiments/ARM-LOOKUP-CONT-001/H1-RESULTS.md).

**44 completed experiment attempts: 23 parked ·21 rejected ·0 approved.** ARM32 ·Intel6 ·AMD6. Includes27 populations,5 replications,12 qualifications; active work excluded. AMD controls failed; no AMD candidate timing. [Earlier sealed ARM investigation](experiments/ARM-LOOKUP-GAP-001/RESULTS.md).

Historical architecture charts (through20 October; current counts above):

![Experiment outcomes by architecture](experiments/EXPERIMENT-FLOWS-20261020/overview.png)

**Experiment flows:** [All experiments](experiments/EXPERIMENT-FLOWS-20261020/all-attempts.svg) · [ARM](experiments/EXPERIMENT-FLOWS-20261020/arm.svg) · [Intel](experiments/EXPERIMENT-FLOWS-20261020/intel.svg) · [AMD](experiments/EXPERIMENT-FLOWS-20261020/amd.svg) · [Follow-ups](experiments/EXPERIMENT-FLOWS-20261020/followups.svg) · [Evidence ledger](experiments/EXPERIMENT-FLOWS-20261020/README.md)

## What matters

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

[Current investigation source](experiments/ARM-LOOKUP-GAP-001/current/) · [Historical source](src/) · [Tests](tests/) · [Historical source manifest](source-manifest.json) · [Extraction notes](docs/STANDALONE.md) · [Licensing](NOTICE.md)
