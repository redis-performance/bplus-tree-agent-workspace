# Matched Intel SCAN profiles — diagnostic only

All120 preregistered captures completed in160.31s under600s. Ten repetitions of each baseline/B×100K/1M×seed301–303 pair,5M requested operations,alternating source order. Native original-versus-disabled controls and separately matched sanitizer controls pass; known-work sampler records67/67 enabled samples and zero disabled samples with equal checksum. Exact base/B callback/checksum/owned-byte semantics and CPU2 endpoints match. No timing schedule extension, retry or interim selection.

| Size | Source | Captured samples | Helper samples | Helper / million actual callbacks | Helper share |
|---|---|---:|---:|---:|---:|
| 100000 | base | 1305 | 337 | 2.1896 | 25.82% |
| 100000 | B | 1258 | 316 | 2.0531 | 25.12% |
| 1000000 | base | 1740 | 419 | 2.7884 | 24.08% |
| 1000000 | B | 1712 | 316 | 2.1030 | 18.46% |

At100K helper counts fall337→316 (−6.23% normalized by identical callback totals), a21-sample difference too small for a precise mechanism claim. At1M they fall419→316 (−24.58%), with helper share24.08→18.46%; this is directional evidence consistent with less sampled helper work. Total captured samples fall1305→1258 and1740→1712 respectively. These sampling ratios are not elapsed-time speedups or exact CPU-cycle attribution. Discovery and independently confirmed elapsed effects remain separate evidence.

Matched disassembly confirms B executes bounded16-byte movdqu/pcmpeqb/pmovmskb mask extraction and nonzero-bit enumeration within ScanSlot; baseline retains its word scanning structure. No source change was made for profiling. Both isolated builds use identical relative source/output paths, flags and sampler scope. Exact sourcebaseline8fab511e and Bsource204edc2c; original timing binaries remain untouched. Read-only post-phase checks verify24 diagnostic source/referee/binary artifacts and22 original baseline/B artifacts before the next workload.

Sampler10ms interval,2-byte PC buckets,scale65536; all capture metadata/text ranges/raw histograms and LLVM18 inline maps retained. Sixteen-bit overflow is excluded by captured max-bin checks and conservative CPU-duration bounds. Each group has30 captures; actual callbacks153,912,000 at100K and150,264,100 at1M. Shares use only captured in-range executable-text samples. libc/outside-range/lost/missed samples are excluded or unknown; inline-inclusive shares overlap and bucket/source boundaries are approximate. Setup/warmup/postvalidation are outside scope; small timer edges remain. No PMU permissions or -pg instrumentation.

Earlier unexecuted12-capture v1 remains preserved. v2 was frozen0f39b54f1 and reviewed before any candidate capture because known baseline131/174samples was too coarse, not because of interim results. Original full guards remain24/80 unresolved, so **PARK/source NONE** persists; no new optimization population or acceptance. Focused validation/guards are next, then corrected-adapter baseline in a separate worktree.

Evidence: [plan](PLAN.md), [schedule](capture-schedule.json), [captures](captures.json), [raw audit](profile-audit.json), [binary/source freeze](build-freeze.json), [diagnostic post-hashes](post-phase-hashes.json), [original post-hashes](original-post-phase-hashes.json), [serial commands](processes.json). Exact backend/model/token costs unknown.
