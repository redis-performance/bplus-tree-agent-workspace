# Baseline diagnosis — M6 private materialized decoder

Primary width60/forward/count1 capture has 28 PCs: 18 resolve to
zbtScoreLeafDecodePolicy and 10 to decoder_batch. This clears the minimum25
for the primary, identifies active regions and does not establish exact cost shares.
Reverse/count1 has17 PCs; forward/reverse count96 have6/9. These three captures are
insufficient, preserved without rerun. The sampler is the already calibrated public
self-process SIGPROF/PC collector from 002-rank; it brackets only the measurement loop.
Signals perturb execution. Its binary is separate from all reported timing binaries.
No external profiler permissions were retried; CPU Performance Engineering MCP is
not exposed in this session's actual tool list. PMU/frequency/residency remain unknown.

Release assembly decoder_batch calls zbtScoreLeafDecodePolicy once per leaf, with
a materialized stack array and the same consumed checksum. The policy contains the
inlined frozen bulk dispatch and loops. Thus the short-range policy/call body is a
plausible target for a one-score scalar branch. Code inspection does not demonstrate
a speedup. Count96 observations are only exploratory; missing profile validation
blocks adoption even if elapsed-time guards clear. Raw PCs remain ignored scratch;
profile-base.json keeps exact hashes and sample sufficiency.
