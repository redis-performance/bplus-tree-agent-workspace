# RANK-001 — Apple M1 round 1 profile and qualification

Source selection: **NONE**. Exploratory hypothesis A selected for a later implementation population; no source candidate has been built or timed. Launch HEAD `77d32df82cd5da02b95c6afb6193fcf83f67223f`; tree SHA256 `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`; referee `bench/microbench.c` SHA256 `b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde`. Actual host and all hashes are in `../HOST-MANIFEST.json`.

## Baseline and A/A

The full five-size matrix in `../001-baseline/matrix/` validated 120 processes, 960 rows and 40 cells; native, ASan/UBSan and size-specific sanitizer checks passed. Its timing was 388.7 seconds. Rank A/A exceeded ±1% at all five sizes. The rank-only `qualify.py` calibrated three baseline observations per cell and froze operation counts (10K 576,323; 100K 305,781; 1M 118,521) before six serial ABBA blocks per size. All 72 timed processes have hashed raw CSVs. A/A max absolute block effects: 1.32%, 37.66%, 6.71%; all three cells fail the strict gate. Minimum windows: 49.49, 35.39, 47.87 ms. Same-binary control variation precludes fine-grained adoption. No outlier was removed or block rerun.

## Public profile and code

External macOS `sample` failed both process-name and direct-PID attachment under the sandbox; the failures are retained. A copied, instrumented referee uses the repository's previously validated SIGPROF self sampler with a 1,000 microsecond **requested** interval. It captured 384/779/1,078 interrupted PCs at 10K/100K/1M with zero overflow and valid checksums. PCs within the release `zbtreeRank` accumulation instruction range numbered 89/154/154. `memchr` resolved in 183/337/618 PCs. See `profile/profile-summary.json` for exact symbol counts and hashes. These observations identify code regions; cadence, sampling bias and signal overhead prevent reading the ratios as exact runtime fractions. Instrumented elapsed times are excluded from A/A and comparisons.

Release disassembly `profile/zbtreeRank.asm` and instrumented disassembly show Clang already vectorizes groups of eight child-count additions with NEON `add.2d`. No explicit SIMD assumption is warranted. The CPU Performance Engineering MCP was consulted on benchmark interpretation; returned sources did not establish a machine-specific timing claim. Frequency, actual core residency and hardware counters remain unknown.

## Private diagnostic and decision

`accumulation-diagnostic.c` pre-resolves leaf/position outside its timer, verifies every rank, and separately times only existing rank accumulation with consumed results. Observed 5M-operation batch averages were 31.56/42.28/86.77 ns per operation at 10K/100K/1M. These are private-kernel observations with a different cache path and **cannot be subtracted from public rank**. The separate census found mean parents 2/3/3 and mean preceding siblings 13.376/27.823/37.418; suffix and choice censuses are retained. A sanitizer count pass passed at 100K. Source-included diagnostic binaries stayed in scratch; source and binary hashes are recorded in files or handoff.

Three proposal passes and the chair record are in `proposals/` and `selection.md`. The chair chose a layout-preserving shorter-side sum for a bounded exploratory implementation population. There were no independent agents, candidate variants, candidate timings, fresh confirmation, adversarial review or adoption in round 1. Git add was denied by the worktree index lock; exact metadata fix patch and hashes are retained under `../001-baseline/`, with commit provenance pending. The remote M6 status is UNKNOWN after a DNS failure.

Next: check M6 publication, freeze the exact exploratory comparison/guard schedule, create three isolated source snapshots/builds from launch HEAD, implement the same shorter-side hypothesis three ways, validate and measure serially. Preserve all patches. Stop if a matching M6 discard becomes visible. Do not turn these diagnostic samples or noisy A/A rows into an acceptance claim.
