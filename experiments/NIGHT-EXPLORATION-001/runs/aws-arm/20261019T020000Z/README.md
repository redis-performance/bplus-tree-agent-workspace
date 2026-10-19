# AWS ARM overnight results

**Source NONE:2 measured populations,0 accepted/1 rejected/1 parked;2 separate architecture
replications, both PARK.** See the [morning report](MORNING-REPORT.md) for complete decisions,
evidence, patches, baseline identities and remaining gates.

**Campaign complete; lease RELEASED and OSS coordinator restoration VERIFIED.** Root observed all three live coordinators RUNNING during08:00:20–08:00:25UTC /09:00:20–09:00:25Lisbon, with inactive owned slices, no owned units/PIDs and fresh saved RUNNING status matching live PIDs. [Immutable release proof06785a454](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/06785a454b6f7b6ef2b45a8db4bafe12a40531a6/experiments/NIGHT-EXPLORATION-001/reviews/aws-release-final.json). This records the observed audit interval, not guaranteed future uptime.

Independent Intel raw review [16f074fbe](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/16f074fbe/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/025-arm-mask-raw-review/REVIEW.md) verifies all48 rows/12blocks of exact historical EXP-005 A replication, schedules, semantics, memory and identities. The outcome remains PARK/sourceNONE; qualified broader guards, fresh confirmation and matched profiling are still missing.

- [Original baseline](001-baseline/summary.csv):120 processes/960 rows,18/40 qualified.
- [Corrected adapter baseline](013-corrected-adapter-baseline/RESULT.md):120 processes/
  960 rows,21/40 qualified; distinct identity, no old/new speed claim.
- [Decoder](003-decode/RESULT.md):PARK; [iterator replication](005-iterator/RESULT.md):PARK.
- [Corrected NEON](017-corrected-neon/RESULT.md):REJECT; all three fail both primaries.
- [Exact historical mask replication](026-exp005A-replication/RESULT.md):PARK; both primary screens pass, broader gates missing.
- [Fold follow-up](021-fold-predicate-review/COMMON-PACKET.md):chairNONE, no implementation.
- [Independent reviews](023-amd-iterator-review/RAW-REVIEW.md), [activity](ACTIVITY.md),
  [status](STATUS.md), [handoff](HANDOFF.md).

Earlier milestone descriptions and superseded states remain in ACTIVITY and Git;
immutable experiment reports and evidence seals are unchanged.

## Historical milestone log (superseded by final status above)

### Additive preparation update — 2026-10-19T06:22:00.520959+00:00

Root requested a separate [corrected ARM score-only iterator diagnosis](024-corrected-iterator/PLAN.md). Plan/execution freeze prepared; no launch, pending root and independent AMD review plus post-ambient idle handoff. Morning results and all prior decisions remain unchanged.

Profile-only024 completed: [immutable result](024-corrected-iterator/PROFILE-RESULT.md),51 commands/6 captures/970 samples, controls pass. No A/A/candidate yet; runner idle for independent raw review and root phase grant.

024 baseline now complete: [result](024-corrected-iterator/RESULT.md),48 A/A rows/12 blocks; bothsizes qualify. SourceNONE/counts unchanged, no candidate/proposal authorized. Runner idle awaiting independent raw review/root decision.

2026-10-19 07:17 UTC: exact historical EXP-005 A native replication completed48 rows/12blocks, all primaries pass (100K elapsed−7.86..−7.74%,1M−7.39..−6.96%). PARK/sourceNONE because broad guards, fresh confirmation and matched profile remain missing. Correctness570 commands and independent native static reviews pass; independent raw review pending. New-population counts unchanged2 (0accepted/1rejected/1parked); separate architecture replications now2, bothPARK. No new experiments after cutoff; ARM idle, leaseACTIVE until08UTC, restoration pending. See [result](026-exp005A-replication/RESULT.md).

## Fresh authorized follow-up — 2026-10-19 08:27 UTC

The overnight lease/release proof above remains final. A separate user-authorized ARM-only lease now runs until10:15UTC. Exact historical EXP-005 A follow-up027 preparation is running after rootf90655754 and AMDd17da59d9 reviews; no timing has begun. SourceNONE, all old decisions and evidence unchanged. [Frozen plan](027-mask-followup/PLAN.md), [preparation](027-mask-followup/PREPARATION.md). Fresh lease is ACTIVE; its later restoration has not yet occurred.

2026-10-19 08:34 UTC: fresh027 preparation FAILED2118/2124 at retainedzero-sign fault diagnostic mismatch; normal4original43/2048mode/12oracle checks passed, but fullnegative-control gate incomplete. No timing/retry. Independent postidentity/frozen/idle proof passes; freshleaseACTIVE, oldreleasehistoryunchanged. [Immutable failure](027-mask-followup/PREPARATION-RESULT.md).

## Fresh mask continuation —09:15UTC checkpoint

Exact historical EXP005A remains unadopted. Fresh-session primary A/A and all12
primary comparison blocks pass (451456c2f), reproducing7% elapsed improvements on
this ARM host. The full original-operation A/A matrix (1329e440a) qualifies18/29
required cells;11required cells fail precision and all11diagnostic cells are short.
Overall status is PARK, sourceNONE, without retries or retuning. Remaining fixed
guard phases, matched profile and final adversarial review require separate grants;
independent held-out confirmation was reserved for a fully eligible candidate.

Original027 preparationFAILED is preserved. Separately reviewed six-command028
suffix plus immutable composite receipt380ef3109 closes correctness eligibility,
without relabeling that failure or transferring night026 performance. New ARM-only
lease remains ACTIVE until10:15UTC; original08UTC fleet release remains final.

Fresh original comparison4c7668661 completes all120processes/960rows:17qualifiedguards pass; qualified100-member SCAN has a mixed+1.477795% block and remainsPARK. Eleven required controls plus11diagnostic controls remainunqualified. No all-six qualifiedguard regression found; no acceptance. Both full matrices and idleidentity proofs retained.

Fresh027 iterator A/A completed all1,968 processes/82 required cells:43 qualify,39 fail precision, none below10ms. OverallPARK/sourceNONE; no retry or automatic comparison. See [fixed iterator control result](027-mask-followup/ITERATOR-AA-RESULT.md). Independent raw review pending; protected identities unchanged and owned runner idle.

Fresh027 iterator comparison completed all1,968 processes/82 cells:9 qualified all-six-block regressions above1% cause REJECT;30 qualified guards pass,4 qualified mixed cases PARK and39 remain unqualified. SourceNONE. See [fixed iterator comparison](027-mask-followup/ITERATOR-COMPARISON-RESULT.md). Matched profile and held-out confirmation remain unexecuted; no further runner workload pending. Fresh lease restoration remains parent-owned and pending proof.

2026-10-19T10:07:19.561680+00:00

Fresh follow-up completed and ARM lease RELEASED. Root's [immutable live release proof](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/2a53fc3f3/experiments/ARM-MASK-FOLLOWUP-001/RELEASE-FINAL.json) verifies the OSS coordinator RUNNING, saved/live identity agreement, inactive owned slice, no owned jobs or processes and no inspection errors at 2026-10-19T10:03:25.494971+00:00–2026-10-19T10:03:27.123716+00:00. The10:03:18 marker identifies release-attempt start, not exact restoration completion. No further workload is pending.

Fresh exact historical mask replication is REJECT/sourceNONE: nine qualified iterator guards lose >1% in every block. Intel independent raw auditd3cc358f2 confirms all1,968 comparison and1,968 AA rows,43 qualified cells (9REJECT/30PASS/4mixed) and39 unresolved controls. The50M primary gain does not override those guards. Matched profile and held-out confirmation remain UNEXECUTED. Historical overnight026 PARK and08UTC fleet release remain separate. See [consolidated fresh result](027-mask-followup/FOLLOWUP-RESULT.md).

2026-10-19T10:41:39.709554+00:00:030 dual-frontend diagnostic preparation only. Explicit read-only retrieval verified allfour actualELFs/preposthashes; noARMworkload or lease/service changes. Bothfrontends IteratorNext114→113instructions, fourcrossfrontendassertion-address differences. Sixcells/schedules/census+scope prototypes prepared; executablefreeze/review/newlease remainrequired. PriorcandidateREJECT/sourceNONE andfreshleaseRELEASED preserved. See030-frontend-diagnosis/ANALYSIS.md andPLAN.md.
