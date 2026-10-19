# Corrected adapter baseline: independent ARM requalification

Source 13e459ff8800be3f02b6b45c87dd7b0c39453fa9, detached Git worktree so runner HEAD provenance is exact.
Source tree remains original8fab; adapter _Noreturn declarations and isolated --build
runner option are the distinct reviewed harness identity. Existing8fab builds/results
are immutable. This is same-binary A/A, not an old/new speed comparison, optimization
population, candidate acceptance or repair of prior failed controls.

Run exact committed scripts/run-size-matrix.py --build build/adapter-requalification
--ops1000000 --member-bytes16 --budget-seconds1200. Sizes100/1K/10K/100K/1M,
all eight original operations, seeds1/2/3 twice, six same-binary ABBA blocks percell:
120 serial processes/960 rows/40 cells. CPU2 via owned remote helper, exclusive ARM.
Native-O3 and ASan/UBSan-O1 builds/original43 tests each plus five sanitizer size
validation commands (seven total runner validations) precede timing. Original runner
keeps flags, allocator, assertions, hashing, schedule and per-command30s caps fixed.

One owned job hardcap1800s including validation; timing hardcap1200s. No retries,
operation-count changes, exclusions, adaptive duration changes or discarded blocks.
Every raw output/failure retained. Source/referee/binary SHA before/after, compiler and
inherited CPU affinity recorded. Fixed original analyzer qualification: report each
cell's six A/A effects and minimum window; unresolved precision is PARK for thatcell,
not a reason to rerun. No transfer of measurements between architectures or identities.

Job queues after exact B portability job completes. Fetch objects and detachedworktree
creation cannot update original HEAD/builds. No Intelrunner actions. Backend native
Codex; exact model and measured token/USD costs unknown.
