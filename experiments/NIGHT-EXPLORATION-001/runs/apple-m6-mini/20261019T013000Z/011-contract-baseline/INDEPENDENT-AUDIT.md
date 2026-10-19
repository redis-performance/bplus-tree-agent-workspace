# Corrected-adapter baseline audit — PASS, 5/40 cells qualified

All120 raw CSV files,120 stderr hashes and960 result rows agree with the manifest.
Independent exact arithmetic reproduces all40 saved cell summaries and240 block
effects. **Five cells qualify;14 cells have a window below10ms.** The preliminary
15-short-cell count was incorrect; there is no exactly10ms boundary case.

Reviewer `/root/followup_proposal_c`, inherited GPT-6/Codex family; exact model,
token usage and monetary cost unknown. This independently audits root's new baseline
data. I authored the earlier private adapter-contract review, so this is not an
independent second semantic review of that adapter. No build, benchmark rerun,
profile, source change, agent launch or Git write was performed.

## Reconstruction and validation

The read-only `independent-audit.py` does not import the runner or its analyzer.
It checks the exact retained order: six blocks, seeds1/2/3 twice, rotating five-size
order, four ABBA processes per size, all eight operation rows per process,16-byte
members and1million requested operations. Every process has the expected command,
zero recorded exit status, unique artifacts and matching CSV/stderr SHA256.

The audit checks integer operation counts against each operation's contract:
whole-tree insert/delete, complete rounded iterator traversals, scan's verified
possibly duplicated count, and exact requested counts for ordinary query/update
loops. Seed, size, length, requested counts and warmup metadata agree. Checksums
are equal within every ABBA block; known integer-fixture sums and count checksums
are independently checked where determinable. Lookup and rank checksums agree.
Owned bytes are exactly equal across all four sides of every cell/block; all240
paired owned-memory effects are zero.

Each A/A effect is reconstructed with exact rational arithmetic from integer
elapsed/operation ratios. Equal counts are checked before comparing the inner B
pair with the outer A pair. Medians, extrema, shortest windows, owned-byte medians,
block effects and maximum absolute effects match both saved summary formats within
1e-8 of the exact reconstruction. The JSON retains all exact effect fractions.

All seven validation records have zero exit status and their retained outputs agree:
43 original tests pass in each native and ASan/UBSan build, followed by eight-case
sanitized checks at100/1K/10K/100K/1M using seed101 and2n+1 requested operations.
The audit hashes those14 validation stdout/stderr files now. Their hashes were not
stored in the original manifest, so they are current evidence hashes rather than
proof of an earlier validation-log freeze. No validation was executed again.

## Identity and timing limits

All eleven current source/referee/build-script hashes exactly match the manifest
and the corresponding blobs in commit `7f299a5f5d2742141e5e9d9963e8f71e9a421466`.
The tree C/header remain the unchanged `d9123c…` / `496e72…` identities. Both corrected
adapter hashes exactly match the private `_Noreturn` patch reviewed in010. The
timing binary matches its manifest hash before, after and at this audit:
`1cc8f9d3eb4ae3fcc9a77b42bd38f8f0f06ef59967a5b6e0d38534d0d89c6b67`.
The recorded publication acknowledgement precedes launch, and launch/start/finish
metadata agree with the preregistered absolute stop. This audit checks the retained
acknowledgement and local commit contents; it performs no new remote publication
verification.

The manifest's160.052970917seconds is **aggregate subprocess-loop wall time**, which
includes fixture setup, warmup, per-process correctness checks and process/driver
overhead. The sum of
the960 individual operation timers is71.958584seconds. The complete manifest span,
including builds and pre-timing checks, is180.821794seconds. These are distinct
quantities and must not be labeled interchangeably.

The frozen driver uses synchronous subprocess calls in the recorded order and
enforces its timeouts. It records no per-child UTC start/end intervals. Therefore
this audit supports serial driver control flow but cannot produce an interval-based
nonoverlap certificate, exact per-child duration audit, proof that the host was
otherwise idle, or exact timing-phase UTC boundaries. Frequency, DVFS, residency
and PMU remain unknown. No interval or hardware observation was invented.

## Qualified subset and interpretation

Qualification requires every absolute A/A block effect<=1% and every operation
window>=10ms. The five qualifying cells are:

| Size |Operation|Maximum absolute A/A effect|Shortest window|
|---:|---|---:|---:|
|100|update|0.831117%|119.560ms|
|10K|update|0.983312%|277.364ms|
|100K|lookup-hit|0.827836%|43.678ms|
|100K|scan|0.882884%|46.586ms|
|100K|update|0.862990%|317.515ms|

The14 short cells are insert/delete at100,1K and10K; lookup-miss at100,1K and10K;
and iteration at all five sizes. Every row is retained, and35/40 cells remain
unqualified. Coverage and correctness pass, while fine precision remains incomplete.
This is a new corrected-adapter baseline, not a source optimization or a paired
old-versus-new adapter experiment. It does not establish an adapter speedup, transfer
qualification from earlier runs, rehabilitate rejected candidates or change source
selection from NONE. Old-adapter evidence remains valid under its original identity.

Reproduce the read-only audit from the repository root:

```sh
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/011-contract-baseline/independent-audit.py
```

`INDEPENDENT-AUDIT.json` preserves the exact reconstruction, identities, raw hashes,
validation evidence, qualified subset and audit limitations.
