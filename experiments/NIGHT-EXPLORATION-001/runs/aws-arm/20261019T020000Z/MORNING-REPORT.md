**Latest ARM closeout 2026-10-19T11:28:34.271520+00:00: RELEASED, source NONE.** The dual-frontend diagnostic is complete; root verified live coordinator restoration11:24:35–37UTC at [132cf5be7](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/132cf5be7/experiments/ARM-FRONTEND-DIAGNOSTIC-001/RELEASE-FINAL.json). Exact candidate remains REJECT. Instrumented instruction reductions do not explain native timing: only2/12 source/cell transfers qualify (zero complete pairs), strict tree attribution stays FALSE. See [diagnostic closeout](030-frontend-diagnosis/CLOSEOUT.md). No additional runner work pending.

# AWS ARM morning results — 19 October 2026

**Source adoption NONE. Two measured ARM optimization populations: 0 accepted,
1 rejected, 1 parked. Two separate architecture replications: both PARK.** No qualified
whole-tree gain is claimed. Host: AWS ARM Neoverse V2, Clang18.1.3, serialCPU2.

**Campaign complete; lease RELEASED and OSS coordinator restoration VERIFIED.** Root observed all three live coordinators RUNNING during08:00:20–08:00:25UTC /09:00:20–09:00:25Lisbon, with inactive owned slices, no owned units/PIDs and fresh saved RUNNING status matching live PIDs. [Immutable release proof06785a454](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/06785a454b6f7b6ef2b45a8db4bafe12a40531a6/experiments/NIGHT-EXPLORATION-001/reviews/aws-release-final.json). This records the observed audit interval, not guaranteed future uptime.

Independent Intel raw review [16f074fbe](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/16f074fbe/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/025-arm-mask-raw-review/REVIEW.md) verifies all48 rows/12blocks of exact historical EXP-005 A replication, schedules, semantics, memory and identities. The outcome remains PARK/sourceNONE; qualified broader guards, fresh confirmation and matched profiling are still missing.

Updated: 2026-10-19T08:03:18.494652+00:00.

## Baselines and identities

| Baseline | Completed evidence | Qualification and limits |
| --- | --- | --- |
| Original8fab511e | [001 summary](001-baseline/summary.csv),120 processes/960 rows/40 cells; five sizes100 through1M, eight operations,16-byte members, seeds1–3, six same-binary ABBA blocks |18/40 cells qualify at±1% and10ms;11 short and19 precision failures overlap. Root audited/published the five-host chart. |
| Corrected adapter13e459ff8 | [013 result](013-corrected-adapter-baseline/RESULT.md),120 processes/960 rows/40 cells; same original matrix in an isolated detached checkout |21/40 qualify;11 short and15 precision failures overlap. `_Noreturn` adapter correction and isolated build path form a distinct harness identity. No old/new speed claim. |
| Corrected SCAN controls | [015 result](015-corrected-scan-aa/RESULT.md),48 processes/12 blocks,100K/1M,5M requested operations, seeds401–403 twice |Both primaries qualify. Actual frozen binary869425ed... is the control for017 and019. |
| Corrected score-only iterator controls | [024 result](024-corrected-iterator/RESULT.md),6 scoped captures and48 A/A rows/12blocks,50M operations, seeds701–703 twice |Both qualify; actual013 binary330b39a9 is the unchanged026 control. Independent AMD profile/AA reviews pass. |
| Fresh fold-follow-up controls | [020 result](020-fold-predicate-aa/RESULT.md),48 processes/12 blocks, same binary and5M operations, seeds701–703 twice |Both qualify; minimum417.860/531.751ms. Controls support only their own session and do not rescue earlier failures. |

Original source8fab511e0e6ec7d4808546cd50064c6bf299e695 and corrected adapter
13e459ff8800be3f02b6b45c87dd7b0c39453fa9 share tree source SHA
d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 and header SHA
496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83. Original source,
referee, binaries and evidence were preserved. Corrected timings were never pooled
with original8fab or another architecture. The corrected SCAN5M-op timing binary is
869425ed06643058e561df05177d1b85c42c9f662c5a80654c25caca02349055.

## Measured decisions

| Work | Outcome and retained evidence |
| --- | --- |
| Count-one decoder003 | **PARK/NONE.** [Result](003-decode/RESULT.md),2784 screen rows and1391 A/A rows. Required primary precision fails; conditional EXP-007B helper leads are not whole-tree/root gains. A/B/C executable text is identical, so no ranking. Root independent audit46c0ce2c2. Patches:[A](003-decode/variants/A/candidate.patch),[B](003-decode/variants/B/candidate.patch),[C](003-decode/variants/C/candidate.patch). |
| Iterator005 replication | **PARK/NONE.** Exact Intel A/B hypotheses replicated on ARM with576 rows/144 paired blocks. Both primary controls fail; no qualified winner. A adds8 bytes iterator state; B preserves16 bytes. [Result](005-iterator/RESULT.md),[independent review](005-iterator/INDEPENDENT-REVIEW.md), rootb0c5a43e2. Patches:[A](005-iterator/variants/A/candidate.patch),[B](005-iterator/variants/B/candidate.patch). Counted separately from new populations. |
| Exact historical EXP-005 A026 replication | **PARK/NONE.** [Result](026-exp005A-replication/RESULT.md),48 rows/12blocks, every primary passes:100K elapsed−7.86..−7.74%,1M−7.39..−6.96%. Missing broad guards, independent confirmation and matched profiling prevent acceptance. [Exact historical patch](026-exp005A-replication/candidate.patch),570 validation commands, root/AMD static reviews pass; final independent Intel raw review16f074fbe passes. Separate replication, not a new population. |
| Corrected native NEON017 | **REJECT/NONE.** Actual three independent proposals and three isolated implementations;145 validation commands pass, then all144 discovery rows/36 blocks complete. Every candidate fails both primary speed gates in every block. [Result](017-corrected-neon/RESULT.md),[comparison freeze](017-corrected-neon/comparison-freeze.json),[A](017-corrected-neon/variants/A/candidate.patch),[B](017-corrected-neon/variants/B/candidate.patch),[C](017-corrected-neon/variants/C/candidate.patch). |

NEON paired elapsed increases at100K/1M: A+96.89–102.01%/+68.98–72.40%;
B+76.65–78.59%/+54.84–55.83%; C+98.89–101.80%/+68.35–69.84%. No variant survived,
so the preregistered [held-out confirmation](017-corrected-neon/CONFIRMATION-PLAN.md)
was not triggered. Correctness included eight original43-test runs,56 semantic suite
runs, six portable V2 runs and eight detected faults. The overread negative was
caught by cardinality assertion, not a demonstrated guard-page fault. Root and AMD
independent native, protocol and raw reviews are retained in the shared campaign.

## Diagnoses and decisions before implementation

- [002 lookup](002-lookup/RESULT.md): NONE after incorrect instruction attribution
  was discovered. Original interpretation, erratum and three unmeasured patches
  remain. Zero sampled cycles was not treated as proof of zero cost.
- [004 update](004-update/PROFILE.md): eight profiles/40 checks and three explicitly
  sequential proposal passes; NONE. No unsupported candidate or impossibility claim.
- [009 original SCAN packet](009-scan-profile/COMMON-PACKET.md) and
  [010 controls](010-scan-native/AA-RESULT.md):100K qualifies;1M first block+1.88927%
  fails. Actual three-proposer chaird57515154 selects NONE, with no retry or code.
- [014 corrected SCAN packet](014-corrected-scan-profile/COMMON-PACKET.md): six
  scoped captures and validated controls; all-match helper plus local setup has
 36.93%/33.13% sampled period.209 original/diagnostic instruction encodings match,
  with the actual015 binary mapping separately verified before017.
- [018 code generation](018-neon-codegen-diagnosis/README.md): read-only existing
  assembly identifies repeated35-instruction fold-predicate reconstruction per16-byte
  chunk and other loop differences; static instructions are not measured cycles.
- [019 matched profile](019-neon-matched-profile/RESULT.md):12 fixed baseline/B
  captures,28 executions/52 commands,17482 samples. Full-process PMU capture with
  explicit timed-call-site filtering, not physically scoped PMU. Candidate predicate
  reconstruction is17.67%/16.87% of timed sampled period;70 incomplete samples and
  all other categories remain. This does not establish recoverable baseline-relative
  gain against the prior55–79% B loss. Root and AMD45ecc704e independently audit it.
- [021 fold follow-up](021-fold-predicate-review/COMMON-PACKET.md): actual independent
  proposals from ARM/AMD/Intel; ARM conditional dispatch, AMD/Intel NONE. Root chair
  [0bbb1a47b selection](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/0bbb1a47b/experiments/NIGHT-EXPLORATION-001/reviews/aws-arm-fold-predicate-population/selection.md)
  selects **NONE**. No implementation or candidate timing;017 rejection remains final.
- [022 baseline attribution](022-baseline-mask-attribution/README.md): read-only
  exclusive209-instruction partition of existing019 samples. Word-mask construction
 10.79%/13.68%, byte recheck5.47%/3.17%, position output2.06%/1.18%. The optional
  forward-fold subset3.014%/1.989% is nested, not additive or a causal upper bound.
  Rootc0cf74241 independently verifies the partition and samples; chairNONE unchanged.

## Shared referees, portability and independent reviews

[007 focused SCAN referee](007-scan-guards/RESULT.md), immutable2ab283daa, passes108
baseline cells/368 commands/eight negative controls with independent root review.
Dense/folded tags use real hashes and independent outputs. Descending fixtures expose
only one reversed64-member leaf; no active resize or wide IDs are claimed there.
[011 supplemental referee](011-scan-supplement/README.md), immutableec21ce601, passes
378 commands,90 models,180 native/sanitizer census cells and16 negative controls.
Public APIs produce real active resize and small fully reversed trees at member
lengths8/319/320/321/1024;319 has no full16-byte tag chunk. No wide-ID or combined
active-resize/reversal coverage is claimed. Structural chunk availability is not
counted as dynamic helper invocation. Pre-freeze failures are preserved. Intel owns
all performance use of these frozen referees; ARM baseline correctness is not an
Intel guard result.

[006 AMD contribution](006-amd-scan-review/implementation-C/candidate.patch) is an
independently authored proposal and implementationC in the AMD population, with
actual ARM portable correctness evidence. [012 exact selectedB portability](012-selected-b-portability/RESULT.md)
separately validates unchanged Intel-selected SSE2 B source204edc2c... through its
natural ARM fallback: original43 tests and V2 oracle pass native and ASan/UBSan.
Neither check measured candidate ARM speed or repaired failed ARM controls.
Independent AMD deletion proposal008 recommended NONE; root101895e82 agreed.

[023 independent AMD iterator reviews](023-amd-iterator-review/RAW-REVIEW.md) cover
plan, frozen execution,51 commands,1218 scientific samples and48 A/A rows. Published
review58fec78b7 confirms100K first-block precision failure+2.4309%,1M qualification,
exact sampled tree mappings and caller gaps. It checks public evidence/manifests,
not live AMD binaries. ARM also independently reviewed the shared corrected-baseline
auditor; root incorporated the reported hardenings at50d64664a.

## Remaining gates and handoff

No candidate is eligible for adoption. Decoder and iterator evidence remains PARK;
NEON rejection and proposal-only NONE decisions are final for their frozen rounds.
Any future supported hypothesis needs a fresh preregistered population, qualified
controls for required cases, correctness and benchmark validation, every required
guard including owned memory, independent held-out confirmation, matched profile
validation and adversarial review. A new harness requires its own baseline identity.
Do not rerun failed schedules unchanged, discard a first block, rank identical code,
or use another host's results to fill a missing gate.

Raw rows, failed attempts, losing patches, source/compiler/referee provenance and
checksums remain published. Large raw perf binaries remain in retained local/runner
artifacts with recorded hashes; public exports disclose redaction. Chronology is in
[ACTIVITY](ACTIVITY.md) and Git. Failed external CLI attempts remain preserved; native
work used authorized tools without permission changes. Actual participant/root/aws_arm,
native Codex backend; exact model and measured token/monetary cost are unknown.

Root owns central reporting and the scheduled08:00UTC lease release. Record actual
job termination, lease release and OSS restoration separately when observed; this
report does not assert those events have occurred.

## Addendum after the initial report — 2026-10-19T06:35:09.380034+00:00

Root requested a separate [corrected ARM score-only iterator baseline diagnosis](024-corrected-iterator/RESULT.md),
then granted each phase after independent review and a verified post-observer idle
handoff. It is distinct from old8fab full-member replication and AMD029. Fixed profile
passes51 commands/six captures/970 samples; root and AMDd42ca4ef2 independently verify
controls and actual013 code mapping. Fixed50M-op A/A completes48 rows/12 blocks:
100K/1M both qualify, maximum absolute variation0.053911%/0.371524%, minimum windows
166.240/186.780ms. No priming/calibration/retry or candidate measurement. SourceNONE,
population counts and all prior decisions remain unchanged. Raw A/A review/root next
step remain pending; runner is idle. LeaseACTIVE/restorationPENDING still applies.

2026-10-19 07:17 UTC: exact historical EXP-005 A native replication completed48 rows/12blocks, all primaries pass (100K elapsed−7.86..−7.74%,1M−7.39..−6.96%). PARK/sourceNONE because broad guards, fresh confirmation and matched profile remain missing. Correctness570 commands and independent native static reviews pass; independent raw review pending. New-population counts unchanged2 (0accepted/1rejected/1parked); separate architecture replications now2, bothPARK. No new experiments after cutoff; ARM idle, leaseACTIVE until08UTC, restoration pending. See [result](026-exp005A-replication/RESULT.md).


## Final handback and review

**Campaign complete; lease RELEASED and OSS coordinator restoration VERIFIED.** Root observed all three live coordinators RUNNING during08:00:20–08:00:25UTC /09:00:20–09:00:25Lisbon, with inactive owned slices, no owned units/PIDs and fresh saved RUNNING status matching live PIDs. [Immutable release proof06785a454](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/06785a454b6f7b6ef2b45a8db4bafe12a40531a6/experiments/NIGHT-EXPLORATION-001/reviews/aws-release-final.json). This records the observed audit interval, not guaranteed future uptime.

Independent Intel raw review [16f074fbe](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/16f074fbe/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/025-arm-mask-raw-review/REVIEW.md) verifies all48 rows/12blocks of exact historical EXP-005 A replication, schedules, semantics, memory and identities. The outcome remains PARK/sourceNONE; qualified broader guards, fresh confirmation and matched profiling are still missing.

Earlier timestamped pending/active statements above are retained as historical milestones and are superseded by this verified final state. No experiment decision or sealed artifact changed.

2026-10-19T10:07:19.561680+00:00

Fresh follow-up completed and ARM lease RELEASED. Root's [immutable live release proof](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/2a53fc3f3/experiments/ARM-MASK-FOLLOWUP-001/RELEASE-FINAL.json) verifies the OSS coordinator RUNNING, saved/live identity agreement, inactive owned slice, no owned jobs or processes and no inspection errors at 2026-10-19T10:03:25.494971+00:00–2026-10-19T10:03:27.123716+00:00. The10:03:18 marker identifies release-attempt start, not exact restoration completion. No further workload is pending.

Fresh exact historical mask replication is REJECT/sourceNONE: nine qualified iterator guards lose >1% in every block. Intel independent raw auditd3cc358f2 confirms all1,968 comparison and1,968 AA rows,43 qualified cells (9REJECT/30PASS/4mixed) and39 unresolved controls. The50M primary gain does not override those guards. Matched profile and held-out confirmation remain UNEXECUTED. Historical overnight026 PARK and08UTC fleet release remain separate. See [consolidated fresh result](027-mask-followup/FOLLOWUP-RESULT.md).
