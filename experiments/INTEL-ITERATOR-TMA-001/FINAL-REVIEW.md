# Independent result review

**PARK confirmed. Baseline qualification fails two of48 blocks; no candidate timing or source adoption.** Reviewer `/root/intel_b_review`, Codex; exact model/token costs unknown. No SSH, source changes or benchmark rerun by reviewer.

[Independent raw reconstruction](independent-audit.json) checks all192 A/A outputs, exact schedule,24 calibration rows, frozen counts, checksums, fixtures, tree bytes, CPU endpoints, serial execution and deadline.46/48 blocks pass. Both failures are seed1 in the first block:

| Guard | Same-binary inner/outer elapsed difference | Minimum window |
|---|---:|---:|
|100K integer, reverse, mask7|−1.630545%|600.360ms|
|100K fractional, forward, mask7|−1.159596%|602.184ms|

Both exceed the frozen absolute1% threshold. All duration, sibling occupancy and semantic invariants pass; primary controls pass. Favorable signs do not make baseline self-disagreement acceptable. Do not remove first-block rows, relax the threshold, claim candidate improvement or repeat the same failed schedule.

## TMA classification and parser adjudication

All six captures satisfy the original gates after parsing at the actual CSV header:10 intervals each, all four unique finite slot roots, sum100±0.3pp,100% scheduling for every metric, workload/CPU accounting discrepancy≤0.195313%, sibling occupancy≤0.094340%. Means across30 intervals per size:

```text
Pipeline Slots (100%) — secondary Intel baseline,100K
├── Frontend_Bound       1.10%
├── Bad_Speculation      3.20%
├── Backend_Bound       12.09%
│   ├── Memory_Bound     7.80%
│   └── Core_Bound       4.29%
└── Retiring            83.61%

Pipeline Slots (100%) — secondary Intel baseline,1M
├── Frontend_Bound       0.75%
├── Bad_Speculation      2.80%
├── Backend_Bound       22.37%
│   ├── Memory_Bound    16.50%
│   └── Core_Bound       5.87%
└── Retiring            74.07%

Candidate B — uncollected; failed baseline qualification
├── Frontend_Bound     unavailable
├── Bad_Speculation    unavailable
├── Backend_Bound      unavailable
└── Retiring           unavailable
```

Display rounding is preserved. Raw timestamps and original units remain in [capture files](results/); per-capture metric counts/ranges, raw hashes and scope reconstruction are in the independent audit. Build identity is `dc323d69acc36e7852084e0704bcce73cfd8100384a6923c2ef32b64652b86a8`, Clang18.1.3/O3, source `c6112e052`, topdown`71dea5e`, pmu-tools2026.4.7.0, CPU2/NUMA0, sibling50 online. Workload is forward integer iteration, mask7,16-byte members,seed7103. These measurements belong to this host and binary.

The frozen analyzer incorrectly used the first warning line as the CSV header. Each capture has three advisory NMI-watchdog lines before `Timestamp,Area,...`; its independent glue parser still produced130 metric samples. Header-aware reconstruction changes no window, metric, unit or quality threshold. The warning recommends reducing multiplexing; measured scheduling is100%. No watchdog setting was changed. Original [automated profile failure](results/profile-quality.json) and [automated PARK result](results/RESULT.json) are retained intact. Correcting this derived parsing defect does **not** overturn PARK because the two A/A failures are real.

Memory_Bound grows7.80→16.50% while instruction-supply stalls remain small. This supports retaining offset-work investigation as a lead; it neither identifies a causal dependency chain nor establishes B's benefit. Retiring percentages cannot establish speedup. Long profiling processes were terminated, so their completed end-of-run checks are unavailable. CPU-wide and whole-process sibling accounting cannot prove zero instantaneous interference.

## Correctness and provenance

Independent inspection confirms four original test logs report43/43: baseline/B × native/sanitizer. Eight cache-oracle logs pass:28,192 original and89,428 additive state checks each, iterator size16bytes in every build. All64 original/extended-driver pairs match semantic fields. The completed extended-count boundary requests100,000,001 visits, executes100,100,000 whole-traversal visits, and matches its expected checksum.

Recorded driver/source hashes match the frozen input manifest; the frozen calibration binary matches the build hash and protocol hash. All recorded measurement commands select baseline/original executables; none selects `build/B/iterator`. Review cross-checks retained provenance records, not an independent remote binary download. Host reservation, coordinator restoration and process cleanup are reported separately by the controller.

Own CPU-perf availability and shared controller consultation are recorded in [pre-execution review](PREEXEC-REVIEW.md) and [availability evidence](reviewer-mcp-availability.json). The empty source library supplies no supporting passages; no advice is presented as independently sourced proof.

Required next decision: preserve PARK and investigate an independently justified new measurement condition before any comparison. The data does not establish why these two first-block guards failed.
