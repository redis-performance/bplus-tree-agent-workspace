# Execution freeze — awaiting code review and launch grant

Approved preparation plan af2131b80 is unchanged. No runner access, benchmark execution
or timing occurred while preparing these drivers. Root must issue the launch grant.

The remote owned directory is scratch/amd-corrected-iterator-13e459ff8 beneath the
existing checkout. Copy only frozen inputs there; source/profile/aa directories must
not already exist. run-profile.py archives exact13e sources into its own source folder.
No existing timing checkout HEAD, source or binaries are modified. Profile runs through
profile-job.sh under the existing remote-bounded-job.py lease with600s outer cap and
CPU2; children are capped by120s and remaining phase time. AA uses aa-job.sh under a
separate300s lease cap,30s child cap. The @REPO@ and @PERF@ placeholders are resolved
from the existing authorized private config; no private value appears in this freeze.

commands.json pins all51 profile subprocess argv/cwd and the three permitted profile
environment variables. The driver verifies the next exact command before execution and
records start/end/exit with raw stdout/stderr, including partial timeout output. Both
job wrappers use set -eu and clear inherited PROFILE_DISABLE/BPLUS_PERF_CTL/BPLUS_PERF_ACK.
Enabled profile calls explicitly remove PROFILE_DISABLE; all disabled modes set it1.
Every job requires actual affinity exactlyCPU2. Source and protected binary hashes are
checked before/after; the diagnostic build hash manifest is written before controls.

The51 commands are archive/compiler2, four frontend builds plus known-control build5,
original43 suite1, six native original/disabled pairs12, one sanitizer pair2, iterate
disabled-stat1, known plain/disabled-stat/enabled-stat/sample/report/export6, four
source-linked disassemblies4, and six tree sample/report/export triplets18.
Scientific profiles are only six iterate captures; the known control is a seventh
separate raw data file and is excluded from every tree summary and code map.

Known-work controls require exact independently computed checksums, zero/not-counted
disabled counters, positive enabled cycles/instructions/branches, nonnegative branch
misses, at least20 known_work samples, >80% of control sampled period, zero outside_work
samples. Unknown/control frames remain in that denominator. Failure occurs before any
scientific capture. Four disassemblies cover known control, native original, diagnostic
and actual unchanged015 timing binary. Tree code mapping records exact-byte matches,
differences and unmapped IPs; no address-only equivalence or relocation normalization.
Loss counts are explicitly reported; no lost-event correction or inference of perfect
sampling is made. A sampled region's causal significance remains a later review matter.

Profile audit reconstructs the exact command list, six original/disabled/sampled semantic
contracts, sanitizer rounding, known controls, losses and all sample denominators. It
rechecks seven raw perf hashes when raw files are available; public artifacts explicitly
state when raw data remains local. The wrapper runs this audit and code mapping before
returning. AA refuses to start unless both complete audit and mapping outputs exist.

A/A uses the actual015 executable1ecbe6a4 unchanged. It checks all target/referee hashes,
records profile audit/mapping/freeze hashes, then follows fixed701–703 twice, alternating
size order,48 same-binary ABBA rows. Per-row runtime checks enforce iterate/size/ops/
memberbytes/seed/CPU2,50M visits,500/50 traversals, one warmup, exact expected checksum
and block semantic/memory equality. audit-aa.py reconstructs every raw row and effect,
with both-size all-block±1% and10ms floor. No failed control gets a retry or count change.

LOCAL-CHECKS.json records only local Python parse, schedule and synthetic parser tests,
plus14 small arithmetic-oracle crosschecks. No compiler or workload was executed.
Execution sources, command manifest, audits and wrappers are bound by execution-freeze.json;
its hash is included in completed profile and A/A evidence. Unknown model/cost unchanged.
No candidate/source adoption. Await root review and launch grant.
