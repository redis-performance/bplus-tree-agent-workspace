# Local M1 baseline: measurements complete, qualification parked

Completed the user-authorised local run with the unchanged standalone tree and referee:
**144 serial benchmark processes, 984 result rows, 41 workload cells, 24 observations per
cell**. Every process exited successfully and every checksum was stable within its cell.
Six ABBA blocks completed in 356.4 seconds. A and B were the identical executable.

**Decision: PARK baseline qualification for small optimisation claims.** Only the 1K,
16-byte score-update cell passed the preregistered interval/duration gates; 40/41 did
not. This does not invalidate the functional checks or erase exploratory observations.
It does mean this setup cannot enforce the proposed 1% guard across the workload suite.
No candidate was implemented, selected or accepted. Optimisation counts remain zero.

## Reproduction and machine boundary

- Apple M1 ARM64, 4 performance + 4 efficiency cores, 16 GiB RAM; one benchmark thread,
  no SMT. Actual executing core and its microarchitecture residency were not measured.
- macOS 26.3; Apple Clang 17.0.0 (`clang-1700.6.3.2`); C11, `-O3 -g -Wall -Wextra
  -fno-omit-frame-pointer`, libc allocator, no LTO or fast-math.
- DVFS/frequency/turbo state and core placement were not controlled; no PMU data.
  One-minute load averages ranged 1.51–3.58. Thermal queries before/after reported no
  recorded warnings; that does not establish a constant clock or thermal state.
- Workspace source/referee at `0a36e68475b2ead629d98ed3fb4cda32a8332139`; tree source
  at PR #15635 `a7ecd959374d66847c095250bf2d373edf7316c5` remains byte-identical.
- Binary SHA-256: `f191112244778172eaa2205cee56a8018384f3c8c8538a777ef8e9f57e19e788`,
  checked again after timing. All builds completed before the matrix.

The [plan](PLAN.md), [driver](run-local.py), [manifest](manifest.json), [raw CSVs](raw/),
[analysis script](analyse.py), [full table](SUMMARY.md), and [JSON summary](summary.json)
record the complete method. The runner refuses to overwrite its manifest; use a new
experiment directory for another run. Calibration is excluded. Profiles are separate
processes and excluded from timing aggregates. No samples or outliers were removed.

## Exploratory observations

The following are **unqualified local timing observations**, not accepted optimisation
claims or portable performance figures. Each value is the median of 24 batch-average
ns/op measurements. The full table includes min/max, CV and block-paired uncertainty.
The MCP's seven-field audit rejects promotion of these rates because frequency is missing.

| 100K members | 16 bytes | 319 bytes | 320 bytes | 321 bytes |
|---|---:|---:|---:|---:|
| Insert ns/op | 469.85 | 1114.65 | 681.32 | 689.03 |
| Hit lookup ns/op | 81.53 | 373.84 | 310.07 | 318.82 |
| Score update ns/op | 608.16 | 1426.73 | 823.62 | 827.55 |
| Initial tree-owned usable bytes | 2,984,176 | 37,963,760 | 35,457,776 | 41,857,776 |

For the 100K/16-byte lookup control, the paired B/A effect interval spans -5.11% to
+2.46%, despite identical code. At 1M/16-byte lookup the observed median is 248.65 ns/op;
that cell also fails qualification. This size sensitivity is not proof of cache misses:
fixtures, cache state, placement and the hash/index/leaf work all affect the result.

The 319/320 boundary changes inline versus external member storage. Different key
lengths are different workloads, not baseline/candidate source variants; this table does
not justify claiming an algorithmic speedup. Fixed integer scores and repeated shuffled
accesses cover only the current fixtures.

The additional 6,400,000 tree bytes at 321 versus 320 bytes have a concrete local
explanation. [The allocator probe](allocator-probe.csv), using the same adapter, returned
320 usable bytes for requests of 320, and 384 for requests of 321, on every repetition.
The external-member path requests member length (`src/zset_btree.c:751`). The 64-byte
allocation-class difference times 100K external members exactly matches the tree total
difference. This is specific to this allocator; it does not measure RSS or fragmentation.

## Sampled code paths

macOS `sample` succeeded for all four independently launched benchmark children. Each
capture requested five seconds at a one-millisecond interval after a one-second startup
delay. These are samples, not exact CPU-time shares or hardware stall events. The caller
stacks mostly identify the timed loops, but no timed-region markers exclude setup/cleanup.

| Profile | Total stack samples | Largest flat samples |
|---|---:|---|
| 100K / 16-byte lookup | 3,836 | leaf `memchr` 2,277; `zbtreeScoreRaw` 433; leaf member search 352; SipHash 342 |
| 100K / 320-byte lookup | 3,826 | SipHash 2,523; leaf `memchr` 780; leaf member search 247 |
| 1M / 16-byte lookup | 3,829 | leaf `memchr` 2,676; SipHash 368; leaf member search 267 |
| 100K / 16-byte update | 3,819 | `memmove` 599; `zbtScoreInsertAt` 471; leaf lower-bound 465; `memchr` 457 |

See [profile summaries](profiles/summary.json) and the sanitised stack files in
[profiles/](profiles/). Raw captures containing process/image metadata remain in ignored
scratch storage. `xctrace` could not run because only Command Line Tools are installed;
Linux perf is absent. No missing event is represented as zero.

The short-key profile and [leaf-search assembly](codegen/zbtScoreLeafFindMember.s) identify
a bounded tag-scan hypothesis worth testing. They do not establish whether the library
call, its data access or another dependency causes the time. Long-key hashing needs its
own control, so a scan-only improvement cannot be assumed to help every lookup workload.
The [code-generation notes](codegen/README.md) also show that some lower-bound updates
already use conditional selects; broad branchless-search claims would be premature.

## Qualification limitations and next experiments

1. **Improve the referee observability first.** Add thread CPU time, actual CPU placement
   where available, verified QoS, an explicit settling/warm-up policy, and reproducible
   duration calibration in a separate harness commit. Requalify before candidate timing.
   Frequency remains a missing seven-field item. The [clock probe](clock-probe.txt) found
   a reported and minimum observed nonzero step of 1 microsecond. Twelve cells have a
   timed interval below our conservative 10 ms gate; small traversals need repeated
   traversals inside a timed batch, with the effective operation count adjusted.
2. **Leaf-tag lookup control.** After qualification, ask three independent proposers to
   evaluate bounded scan alternatives and controls, not to rubber-stamp a predetermined
   winner. Include empty/full leaves, first/last/missing matches, colliding tags, binary
   members, inline/external storage and safe tails. Never substitute the index's folded
   zero-tag rule for raw leaf tags. Any SWAR/NEON proposal must avoid over-reads and retain
   exact member comparisons and portable behaviour.
3. **Long-key lookup control.** Add a focused hash-cost diagnostic, raw versus SDS entry
   points and batch lookup workloads. Preserve the upstream keyed hash/security contract;
   replacing it with a weaker hash is not a valid tree optimisation. Do not subtract a
   microkernel time from request time and call the remainder a measured component.
4. **Update and layout controls.** Split in-place small score changes from the current
   large moves; inspect copying/repacking with targeted fixtures. Study allocator size
   classes separately from the external-storage threshold, and include multiple lengths
   and allocators before making a general memory-policy claim.

These are measured leads, not a completed population vote. Both population stages remain
mandatory for an optimisation round. [METHODOLOGY.md](METHODOLOGY.md) records the MCP
sources and the limits of its retrieved passages; [EVIDENCE-AUDIT.md](EVIDENCE-AUDIT.md)
records its evidence verdict.
