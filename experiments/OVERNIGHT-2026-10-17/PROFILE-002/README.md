# PROFILE-002 — scoped self-process profiles collected

The public self-process signal sampler passed both fixed known-function calibration
checks and captured all12 planned tree profiles. Every capture exceeds the predefined
minimum sample count; all operation/checksum checks pass, no buffer overflow and no
unresolved symbol. Baseline source and root referee remain unchanged.

[Plan](PLAN.md), [sampler](self_sampler.h), [patch](profile-harness.patch),
[source freeze](freeze.json), [build/smoke/calibration](validation.json),
[capture commands/raw hashes](manifest.json), [symbolication commands](symbolication.json),
[full symbol/location distributions](summary.json), [readable table](SUMMARY.md).
Exact raw PCs, stdout/stderr, dSYM and symbols remain under ignored scratch with hashes.

Short-key lookup captures are led by memchr; long-key lookups are led by SipHash.
Rank captures show both member matching and rank traversal. These observations agree
qualitatively with earlier lookup profiles and add scoped rank evidence. They identify
places for later investigation, not a source winner or performance acceptance.

Only the known arithmetic loop was sampled during both calibrations. Timer request
values are not observed cadences: SDK documentation permits rounding and delivery can
coalesce. Separate requests yielded similar sample densities; no distinct cadence,
anti-aliasing guarantee or hardware frequency is inferred. Captures include small scope
boundary instructions. The instrumented thread timer includes post-loop profile output,
so it must not be used for CPU/wall ratios. Instrumented wall times include signal costs
and must not enter A/A or optimisation comparisons. No overhead correction is claimed.

Local installed SDK declarations/manuals inspected: sys/time.h,getitimer(2),sigaction(2),
sys/_types/_ucontext.h,arm/_mcontext.h,mach/arm/_structs.h,dlfcn.h. The sampler uses
lock-free C atomics checked at startup; handler reads interrupted PC and stores it only.
Symbolication/allocation/I/O happen after timer disarmed and signal blocked. This is
macOS arm64 diagnostic code, not a portable referee extension or production library.

No denied external inspection retried, permission changed or external service contacted.
CPU MCP ask retrieval was unrelated and not supporting evidence. Evidence checker flags
missing frequency and partially parses context; no portable rates/cycles promoted.
Frequency/effective QoS/residency, sampling bias, aliasing, signal overhead and layout
remain unresolved. Review sequential, not independent; exact backend/model/cost unknown.

Decision: profiling method locally useful for coarse diagnostic evidence; source NONE,
AA-003 qualification PARK unchanged. Both population stages still await meaningful
qualified comparisons. Commit-based acceptance pending morning review.
