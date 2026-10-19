# ARM mask follow-up — current evidence

**Primary gate passes; overall candidate remains PARK / source NONE pending guards,
independent confirmation and matched profiling.** No production source change or new
optimization population. This is a fresh-session replication of exact historical EXP-005 A.

| Fresh primary fixture | Control blocks qualified | Candidate blocks passing ≥2% | Median elapsed change | Candidate block range |
|---|---:|---:|---:|---:|
| 100K members | 6/6 | 6/6 | −7.780706% | −7.923028% to −7.534120% |
| 1M members | 6/6 | 6/6 | −7.212021% | −7.704460% to −6.592530% |

Both phases contain 48 serial processes, twelve ABBA blocks total, on the same dedicated
AWS ARM Neoverse V2 runner / CPU 2. Each process performs 50M forward score-only visits with
16-byte members and one warm-up. Seeds 1101–1103 are repeated for six blocks per size.
The exact baseline/candidate binaries are preserved; source, referee, compiler options,
allocator, checksums and tree-owned bytes match the frozen contract. Control maximum
absolute effects are 0.490027%/0.281102%, below the preregistered ±1% gate; minimum control
windows are 166.240414/186.987521ms. Timings from the overnight session are not pooled.

![Fresh exact candidate primary comparison](charts/primary-replication.png)

[Control chart](charts/primary-AA.png) · [Root control audit](PRIMARY-AA-ROOT-AUDIT.json)
· [Root candidate audit](PRIMARY-REPLICATION-ROOT-AUDIT.json).

## Correctness and provenance

The original preparation remains **FAILED** at its frozen diagnostic registration:
a deliberate sign fault was caught by the earlier copied-next exact-score assertion,
while the script expected the later current-score assertion. That raw attempt remains
unchanged. A separately reviewed 180s continuation ran only six commands that had never
started, taking 6.416300s. No original command was repeated, and no referee was weakened.

The reviewed composite covers 2,048 normal iterator-mode runs, four original 43-test suite
runs, 12 additional oracle runs, and 14 detected injected faults. Both phases preserve all
4,241 original raw artifacts,513 copied source/oracle files, six protected timing binaries
and four native guard binaries. Root and independent AMD audits agree. All public raw
artifacts, failure records, patches, plans and reviews remain in Git.

## Remaining gates and limits

The frozen plan contains 82 required iterator guard cells plus 29 required original-operation
cells; 11 original cells are prospectively declared diagnostics. A qualified diagnostic
loss still blocks progression. Unqualified required controls mean PARK; no retries,
threshold changes or post-result count tuning are permitted. Every phase needs a separate
root grant and must fit the fixed 10:15UTC lease deadline. Live handback proof is required.

Uniform identical-bit width-zero performance remains an explicit fixture gap. Existing
alternating signed-zero coverage does not close it. ARM timings do not qualify other
architectures or imply portable adoption. Independent held-out seeds 1201–1203 and matched
profiles remain unexecuted at this checkpoint; primary instruction differences alone do
not establish the cause of the timing improvement. Exact serving model/token/currency
costs are unknown. Historical eight AWS populations remain 0 accepted / 5 rejected / 3 parked.

## Immutable raw evidence

- [Original failed preparation8cdebdcba](https://github.com/redis-performance/bplus-tree-agent-workspace/tree/8cdebdcba/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/validation)
- [Six-command suffix19fd53594](https://github.com/redis-performance/bplus-tree-agent-workspace/tree/19fd53594/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/028-mask-validation-continuation)
- [Fresh controls53e193c5b](https://github.com/redis-performance/bplus-tree-agent-workspace/tree/53e193c5b/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/primary-AA)
- [Fresh primary comparison451456c2f](https://github.com/redis-performance/bplus-tree-agent-workspace/tree/451456c2f/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/primary-replication)
