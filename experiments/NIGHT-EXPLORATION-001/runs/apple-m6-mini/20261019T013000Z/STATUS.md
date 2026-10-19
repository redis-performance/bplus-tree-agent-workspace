# M6 driver campaign — lookup dual-primary REJECT; optional target next

Updated 2026-10-19T02:36:08.646356+00:00. Round4 ends02:55:27 UTC. Campaign ends08:00 UTC /09:00 Lisbon;
start no experiments after07:15 UTC. Source selection **NONE**, baseline hashes unchanged.

| Target | Status | M1 action / evidence |
|---|---|---|
| Five-size baseline | COMPLETE | Launcher baseline-attempt002,120processes/960rows; do not rerun. |
| RANK-001 | REJECT/NONE | All100K blocks regress;skip exact candidates. [Results](002-rank/RESULTS.md). |
| UPDATE-001 | REJECT/NONE | No100K winner;1M transient-packing lead only. [Results](003-update/RESULTS.md). |
| LOOKUP-001 | REJECT/NONE | No dual-primary winner;B100K exploratory lead only. [Results](004-lookup/RESULTS.md). |
| Optional/confirmation | NEXT | No eligible dual-primary contender; choose DECODE-001 or ITERATE-001 from profile. |

Lookup **M6-LOOKUP-PHYSICAL-001**, exact patch/harness/binary identity in
[freeze](004-lookup/comparison-freeze.json) and[patch manifest](004-lookup/implementation-manifest.json).

| Variant | 100K median / range | 1M median / range | Decision |
|---|---:|---:|---|
| A | -1.328% / -2.646..+0.333% | -0.407% / -3.083..+3.568% | REJECT dual primary |
| B | -4.800% / -6.243..-3.482% | +0.428% / -3.926..+5.681% | REJECT dual primary |
| C | -1.095% / -1.662..-0.320% | -1.389% / -3.241..+2.396% | REJECT dual primary |

B passes100K each block, no candidate passes1M.100K A/A max0.745% qualifies;1M4.184%
fails. No primary relabeling, adoption shortlist, freshconfirmation, full candidate
performance guards, candidate-profile validation or independent review. All patches kept.
Both population steps sequential, not independent agents. Exact serving model/cost unknown.

All4 sources pass original43tests per native/sanitizer build,20 publicsize/lengthcells
per build, private4160cells/515840exactscore-position-outputchecks per build. Two
physical-decode faults detected. Baseline profiler4/6sufficient; smaller miss captures
remain insufficient, not repeated. Audit222rows/48effects/3patches/524serialwindows PASS.
Last experimental child02:33:28 UTC. No further lookup trial is eligible.

Publication: profile/referee e18d69d0;chair e1f3b73c;candidate freeze94e4e897 acknowledged.
Current decision/handoff requests coordinator publication next. Coordinator alone
commits/pushes. Git worktree denied once previously;separate copiedbuilds used,no retry.
Cached published M1 branch4c48fa7e inspected; exact physical-score patch/harness onM1
NOT RUN, no host pooling. Prior remote DNS failure retained, no credential changes.
Launcher metadata verifies AppleM6;directsysctl unavailable and not retried.
Frequency/DVFS/performance-core residency/migration/PMU unknown. Self-sampled PCs
identify regions only. No external profiler permission retry or permission changes.

Recorded branch totals **10 populations**(8 sequential+2 multi-agent),
**0 accepted /5 rejected /5 parked;30 retained patches /13 validated harnesses**.
M1 night counts separate pending reconciliation. Next action inHANDOFF.md.
