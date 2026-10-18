# PROFILE-005 — single-lane hit guard mechanism

Preregistered 2026-10-18 before capture. Frozen EXP-006 control/C, HARNESS-007 attempt002,
unchanged allocator/assertions/hash/flags: Apple Clang17 C11 O3-g-Wall-Wextra-Werror
-fno-omit-frame-pointer-DREDIS_DEBUG, local M1 arm64, one unpinned thread.
Two isolated diagnostic profile snapshots add only the inspected DIAG-009 self sampler.
Each source: two 200million known-arithmetic calibrations at requested 1000/3001us;
require >=20 samples, >=90% known function, zero unknown/overflow. Then four fixed
captures: seeds81903/query81919 and81911/query81923, both intervals, hit16/batch1,
n8192,50million requested members,three warmup passes. Require >=100 samples and
zero unknown/overflow; insufficient stays insufficient, never extend counts.
Build all binaries before captures within each source; run control then C serially.
All children <=120s, each source capture budget240s, absolute stop06:02UTC.
Capture interrupted PCs, exact CSV counts/checksums and full symbols/assembly.
These are descriptive scoped samples, not unbiased time fractions or PMU counts.
Frequency, effective QoS, within-window migration and sampler phase remain unknown.
No A/A or acceptance timings come from these binaries; previous guard failures remain.
Independent reviewer startup failed before running; coordinator sequential review only.
Exact backend/model/token cost unknown. No root source or old evidence changes.
