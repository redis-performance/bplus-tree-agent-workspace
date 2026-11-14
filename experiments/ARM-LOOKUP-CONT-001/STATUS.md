# Overnight continuation active

Authorized through **14 November 2026, 07:24:14 UTC**, with final 30 minutes for review, reporting and verified cleanup. No source is accepted.

- H1/H3/H4/H5/H6: independently reviewed REJECT; all patches and raw rows retained, no unchanged retries.
- [H2: PARK / NONE](H2-RESULTS.md). Original discovery and guards pass, but held-out ARM seed43 fails one A/A block at −3.601147%. Independent review audits all 864 held-out rows, including the cross-host scheduling deviation. Intel passes cannot replace ARM qualification. The original failure remains closed and retained.
- [H7: static REJECT / NONE](H7-RESULTS.md). All three target raw frames grow176→192 bytes, violating the frozen gate. No timing ran; this unmeasured screen adds no completed timing attempt.
- H8: three isolated range-first classification variants pass correctness and source review. ARM lookup and supplemental generic consumer static reviews pass. No timing or acceptance yet.
- [Q4](ARM-PROFILER-OFF-QUALIFICATION.md): a distinct baseline-only isolation protocol is prepared. The previously active ARM profiler had unrestricted affinity. Concrete independent deployment review passed after correcting overlapping recovery runtimes. Q4 is now running with Parca stopped and recovery scheduled at07:12 and about07:15:30, before the07:20 lease deadline. Q4 cannot retroactively pass H2.
- AMD: both original compiler controls failed; no candidate timing. Runner released and independently verified. ARM/AMD pipeline categories remain unavailable where scope/formula evidence is missing.

ARM and Intel retain bounded reservations with independent cleanup. Current completed ledger: **46 attempts, 24 PARK, 22 REJECT, 0 approved; ARM34 / Intel6 / AMD6; 29 populations, 5 replications, 12 qualifications**. Active and unmeasured work is excluded. Upstream remains ee8e7f701. Standalone evidence does not establish server-command recovery.
