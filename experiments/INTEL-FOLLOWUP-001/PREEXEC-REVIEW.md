# Independent pre-execution review

**GO for the frozen bounded diagnostic session, subject to successful runtime
ownership/identity/correctness preflight.** This includes the two one-shot capability
probes and16-configuration L2 schedule. Matched PEBS/LBR collection requires the
separate hash-bound controller plus independent probe review; no decision by240s
means both deep methods remain unavailable. No retry or source/timing acceptance.

Reviewer `/root/intel_b_review`, Codex; actual model/token costs unknown. Exact
[reviewed hashes](PREEXEC-HASHES.json) bind this verdict. Python AST parsing and
`bash -n` pass. This reviewer performed no remote workloads or host changes.

## Closed findings

- Isolation/topology/affinity/accounting failures now stop remaining work after
  preserving failed records. Launches and probes retain STARTED/INCOMPLETE evidence.
- TMA streams are persisted before fallible post-capture scope checks. Deep stage
  command streams, raw identity and failed scope remain available. Timeout124
  aborts the sweep and returns to owned-group cleanup; descendants cannot remain
  while later configurations continue.
- Ownership preflight rejects unknown/unreadable reservations, direct perf/toplev,
  named collectors and native workers, active containers and competing capture
  units. The three old release exceptions require explicit release evidence and
  dead recorded PIDs. Full process/cgroup inventory remains private, outside results.
- The worker PGID is recorded. Exit/recovery removes and checks non-zombie group
  members before sibling/coordinator restoration and RELEASED. Recovery targets
  exactly `bplus-intel-followup-001.service`; operator declares RuntimeMaxSec1620
  and TimeoutStopSec15. The independent recovery timer is30minutes; owned work
  is bounded25minutes. Fresh final live restoration proof is still required.
- Original sibling topology2,50 and online state are saved. Offline observations
  accept topology2 or2,50 only with the original pair and CPU50 offline verified.
  Release verifies original topology and online state. This accounts for x86
  [CPU-offline sibling-mask removal](https://github.com/torvalds/linux/blob/master/arch/x86/kernel/smpboot.c).
- Probe decisions bind the exact protocol and both raw hashes, retain reviewer
  evidence identity, reject malformed/stale inputs, and default unavailable.

## Collection interpretation gates

All three L2 windows are required per configuration, and both matched builds must
qualify. Roots must be finite total-slot shares with the frozen sum tolerance,
exact intervals and100% scheduling. Deep methods require both windows, exact
intended event/precision/filter, at least200 intended samples,99.5% scheduling,
zero recorded loss/throttle and their predeclared data-field/branch-stack coverage.
Auxiliary events are excluded from load denominators. Controller and reviewer must
reconstruct these facts from actual probe data before enabling each method.

This is a different host with CPU50 offline. Keep it separate from old profiler
captures; it neither explains their timing failures nor repairs old ownership or
annotation-denominator limitations. Ambient collectors are disclosed, stateful
update phases remain ordered, and there are no in-window operation counts. PEBS
ldlat30 samples describe a selected population; cycles-triggered LBR observations
are not unbiased branch/mispredict rates. Prior rejected/parked decisions remain.

## TMA classification

Before execution, Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring,
including Memory/Core children, are **unavailable**. The protocol obtains fresh
measured partitions; historical percentages must not fill them in.

Own CPU-perf availability/ask records and interpretation limits are in
[design review](INDEPENDENT-DESIGN-REVIEW.md) and
[offline review](INDEPENDENT-OFFLINE-REVIEW.md). No MCP claim substitutes for the
probe gates or raw evidence. Earlier HOLD findings are closed by the hashes below.

| Reviewed file | SHA256 |
|---|---|
| protocol.json | `724a4379229055c9a69cae68683faedadf5ee9ce48752993c05b16899fba3ba9` |
| collect.py | `04c591029afa5f7b6b7d96bfb911853d167c8db6e2776c9b0816f04aa09d8f07` |
| validate.py | `bf9ea7b51c670ebdf45258e09130f0e71f611f6c2112f5932bd96a7309708544` |
| preflight.py | `be224230dac55113e5b15cf502a2182003054e0736fbd4664ae67e17e1be7a8e` |
| run.sh | `722aa3bc5639aac2b8b3ab99ec2c5d470e42a1a4cb7a1a1d15eb366fc46881ac` |
| restore.py | `b8f63c4d0b8f99b80db00014f60e447ff479e9b110bdbedcf62868542bf44725` |
