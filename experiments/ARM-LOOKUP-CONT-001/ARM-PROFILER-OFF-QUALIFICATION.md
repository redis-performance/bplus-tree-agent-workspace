# Q4: ARM baseline qualification with the background profiler stopped

This is a separately preregistered isolation condition, not a retry of the original condition. Original H2 remains PARK/NONE: its seed-43 A/A miss block failed by -3.6011466% before candidate comparison. All failed rows and the original decision remain retained. No cause has been established for its single 3.163-second row among three rows near 2.94 seconds.

A fresh process/thread audit found the system Parca service active with 39 threads across two processes, each allowed on CPUs 0–95. Its systemd CPUAffinity and AllowedCPUs settings are empty. Earlier operational wording that placed Parca on CPU0 described an observation, not verified affinity; it must not be used as an isolation guarantee. The workload/controller affinities remain CPU2/CPU0. Intel already uses a separately qualified condition with Parca stopped.

The changed condition is explicit: temporarily stop the existing Parca service on the owned ARM runner. Save its active state and unrestricted affinity policy, then install and independently review cleanup that resumes the exact paused coordinator and restores that service through two independently armed release timers. Do not stop it until that recovery path is ready. No service configuration, frequency, PMU sysctl, CPU topology, source, compiler, allocator, query fixture or inner timing loop changes. Check absence of the service and its processes before every child. A passing new control would qualify this condition; it would not prove the profiler caused the old failure.

## Frozen baseline-only sequence

Reuse the exact original ARM lookup ELFs and all frozen sources/referees. No candidate executable is run, including verification. Source is upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, C SHA-256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.

Run these complete six-case cohorts in order, stopping before the next cohort if any gate fails:

1. GCC15.2/LTO seed43, the seed whose original condition failed.
2. GCC15.2/LTO seed29.
3. GCC15.2/LTO seed17.
4. GCC13 native seed17, to qualify subsequent native screening under the same changed isolation.

For each cohort, hit/score/miss/inline256/external384/update use the original semantics and separate process fixtures. Native sweeps are 50,000/50,000/100,000/20,000/20,000/20,000; target LTO uses five times those counts. Warmup remains 1,000. Each case has three ABBA blocks with the same baseline binary on both labels: 72 rows per cohort, at most 288 rows overall. No adaptive counts, new seed, dropped row, second attempt or candidate admission after failure.

Every row must match the independent operation/checksum model and exact ELF/source/referee pins, and last at least 250 ms. Every A/A block must have absolute elapsed contrast at most 1%, with identical owned-memory endpoints. Preserve stdout/stderr, commands/timestamps, rows and all failed blocks. Whole-process child CPU time, context switches and faults may be collected outside the unchanged timed loop as diagnostics; they include setup/warmup and cannot replace its wall-time metric or retroactively diagnose the old sample.

Each process is guarded by the live owned lease, exact paused coordinator identity, both cleanup timers, CPU2 affinity, CPU0 controller, no Docker work, inactive Parca and immutable identities. Reuse existing baseline bytes; no builds, profiling, archive transfers or consultations run on the runner during Q4. The controller may check bounded completion state but will fetch archives only after the entire Q4 unit is inactive.

This qualification selects no source. Any later candidate validation under this condition requires a separate frozen admission, complete comparisons and held-out confirmation, matching profiles, existing guards and independent final review. It must report the original H2 PARK alongside new evidence. A failed Q4 stops this path without another unchanged attempt.

## Evidence limits

Actual cpu-perf stdio discovery, library_status and ask used the failed rows and proposed isolation difference. Coverage is 3/287 linked sources and 158 passages. Two generic perf_event_open event-description passages were retrieved; neither attributes the interruption to Parca or predicts successful qualification. The unrestricted affinity audit is direct operational evidence, not a retrieved causal result. A follow-up consultation records that corrected affinity fact separately from the earlier CPU0 assumption.

ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and child pipeline shares remain unavailable under the existing collector scope/formula limits. This baseline qualification collects no candidate profile and supplies no optimization gain.

## Deployment admission

Offline review cleared collector SHA531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743 and cleanup SHA7bd7d2437743bb2cbb6bc290c6ae4a556f09e41b38d2deeaa984516a7edf3c35. Eighteen synthetic collector tests and bounded mocked recovery tests pass. Independent concrete review rejected the first staged timer schedule because the backup could exhaust its runtime while waiting for the primary cleanup lock. Parca stayed active throughout that rejected staging; its evidence remains retained.

The corrected calendar primary fires07:12:00 UTC. The monotonic backup maps to07:15:29.780 UTC,209.780 seconds later. Each cleanup has180 seconds runtime plus15 seconds stop allowance; the backup bound ends75.220 seconds before the07:20 lease deadline. Both new paths were verified active before retiring previous timers. Exact numeric clock properties, a wall/monotonic/boot anchor, immutable lease generation, plain cleanup bytes, command hashes and saved unrestricted service policy are joined in the private operational record. The saved thread count was41 at staging versus39 at the earlier audit; every observed thread retained CPUs0–95. No stable thread-count claim is made.

[Independent deployment review](reviews/Q4-DEPLOYMENT.md) approved this exact record, then live preflight passed after stopping Parca. The fixed baseline-only sequence is admitted. No candidate executes; original H2 remains PARK. The collector requires a five-minute margin before the earlier recovery trigger, and the overall task retains its06:54 final-admission cutoff. The sequence subsequently closed PARK at its first target43 cohort; [all rows and the result](Q4-RESULTS.md) remain retained. No candidate was admitted.
