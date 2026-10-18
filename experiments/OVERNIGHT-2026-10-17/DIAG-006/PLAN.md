# DIAG-006 preregistration — self-sampler perturbation

New diagnostic following PROFILE-002, not another precision trial. Hypothesis: enabling
its own-process signal sampler changes total loop wall time by less than5% in two scoped
lookup cases. This characterizes profiler perturbation only; it cannot qualify1% source
guards, establish unbiased sample distributions or rescue failed AA-003.

Separate frozen snapshot over PROFILE-002. Same exact executable for off(A)/on(B),
PROFILE_USEC=0/1000. Off skips timer arming; both routes install same inactive handler
at startup. Split stop from dump so thread-clock endpoint precedes profile output.
Sampler boundary syscalls still affect thread interval; no clock/residency inference.
No target-source change; only diagnostic harness/header. Root referee unchanged.

100000 members,held-out construction/hash seed1103,query seed1201,independent queries,
10 fixed warmups. Two cells hit16:10000000 operations,hit320:5000000. Six serial ABBA
blocks per cell,rotate order on even blocks;48 measured fresh processes. No excluded
normal warmup; tiny release/sanitizer smoke is prospective nonmeasurement validation.
Child<=120s,total<=240s; no builds/tests/profiles/local agents overlap measurement.

Each row>=100ms,checksums/counts/memory/fingerprints stable. Disabled captures0 samples;
enabled>=50, no overflow. Wall time primary. Report six effects100*(mean(B)/mean(A)-1),
95% descriptive t(df5) interval. Support bounded-perturbation hypothesis only if both
whole intervals lie within[-5,+5]% and all controls pass. Otherwise unresolved/unsupported,
not delete rows,change thresholds,add samples or call a source regression. This is an
explicit diagnostic bound selected before outcomes, not altered optimisation criteria.
Preserve all raw CSV and profile dumps, failures and exact commands/hashes.

Same established M1/macOS26.3,one thread,4P+4E installed,no SMT,Clang17,-O3/C11/debug
symbols/original assertions/libc. Clock/effective QoS/residency unknown. No M4 numbering
or data transfer. CPU MCP method review and PROFILE-002 calibration already available;
consult evidence checker before claim. Review sequential,backend/model/cost unknown.
