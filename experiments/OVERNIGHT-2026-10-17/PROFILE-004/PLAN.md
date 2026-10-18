# PROFILE-004 — qualified batched lookup subsets

Before captures: frozen HARNESS-007attempt002 baseline, unchanged source and allocator,
O3-DREDIS_DEBUG with existing flags. Add only inspected macOS arm64 self-sampler from
DIAG-009, stop before thread endpoint, dump after endpoints. Diagnostic-only binary;
its timings never enter A/A or candidate tables. Public own-process APIs, no external
inspection retry. Source/profile harness patch and hashes retained.

Build profile and calibration binaries, dsym both, then two200million-iteration
known-arithmetic calibrations at requested1000us/3001us. Require>=20samples,>=90%known
function, nooverflow. If failed stop captures, never adjust counts after seeing results.
Then8fixed serial captures: seeds80703/query80719 and80711/query80723; each requested
1000/3001us; long hit320/batch16=20millionmembers and mixed16/batch16=50millionmembers.
n8192,warmups3. Require>=100samples for useful symbol attribution, nooverflow, no
unknown symbols, correct counts/checksums. Mark insufficient without extending count.
All children<=120s; whole capture phase240s. No overlapping builds/tests/agent work.

Counts are descriptive interrupted PCs, not unbiased time shares or PMU metrics.
Cadence, phase aliasing, sampling perturbation/layout, frequency and effective QoS
remain unknown. Relevant earlier calibration/API inspection is retained; helper
interface is the corrected DIAG-009stop/dump split. Do not transfer M4 results.
Only after profiles may separate sequential hypothesis proposals inspect evidence.
Short-keyhit primary AA-012 failed; long/mixed qualifications do not repair it or any
originalguard. Source acceptance still requires every existing gate and morningreview.
