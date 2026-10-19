# AWS overnight campaign — 19 October 2026

User-authorized work ends at **08:00 UTC / 09:00 Europe/Lisbon**. Stop starting
experiments at 07:15 UTC. Source adoption remains NONE. Existing M1/M6 runs continue
on their own branches; the AWS controller does not alter them.

SSH access was verified on all three reserved hosts. Their OSS coordinators were
stopped and verified stopped at approximately 01:54 UTC. Independent system timers
stop all owned B+ tree cgroups and restore OSS at 08:00 UTC. Existing unrelated
processes remain intact. Private operational details are in ignored controller
scratch and the private fleet inventory, never public evidence.

| Host | Actual CPU | Compiler | Affinity | Baseline | Optimization |
|---|---|---|---|---|---|
| AWS Intel | Xeon Platinum 8488C, Sapphire Rapids | Clang 18.1.3 | CPU 2; SMT sibling 50 | Complete | See live dashboard |
| AWS AMD | EPYC 9R45, Zen 5 | Clang 18.1.3 | CPU 2, no SMT sibling | Complete | See live dashboard |
| AWS ARM | Neoverse V2, Graviton | Clang 18.1.3 | CPU 2, no SMT sibling | Complete | See live dashboard |

Baseline source/referee commit: `8fab511e` (only Linux affinity metadata differs
from `9c192c9c`; target source unchanged). Each host runs 100/1K/10K/100K/1M members,
eight operations, 16-byte members, seeds 1/2/3, six same-binary ABBA blocks. Native
and ASan/UBSan validation precede timing. The per-host timing budget is 1200 seconds;
results are never pooled. The initial jobs are managed by systemd, bounded to
1800 seconds, and all baseline children inherit CPU2 affinity.

All three baselines are complete and raw-audited:120processes/960rows/40cells per
host, seven validation stages each. Intel338.54s, AMD325.44s, ARM377.83s timing.
Cells with >1% A/A variation:Intel27/40, AMD30/40, ARM19/40;11short-window cells
on every AWS host. These are coverage baselines, not blanket precision qualification.
The [baseline chart](baseline-charts/m1-m6-baseline.png) now includes all five hosts.
Profile-led work applies the [population gates](../../docs/POPULATION.md); completed
results are in the [decision ledger](AWS-DECISIONS.md). The exact shorter-side rank
candidates rejected on both Apple hosts are skipped; lookup/update/decoder work
requires fresh AWS profile evidence. No speed claim or candidate acceptance yet.

[Activity log](AWS-ACTIVITY.md). [Worker contract](AWS-WORKER.md). Native workers use
the already authorized session tools, with no permission changes. Actual backend/model and measured usage are retained
when available; no invented agent identities or costs.


## Execution update

Detached Codex CLI launchers failed before any shell command with `bwrap: setting
up uid map: Permission denied`. Their reports and measured CLI usage remain on the
host branches. The failed supervisors were stopped. Three native session agents
then verified SSH independently and continue with the existing authorized tools;
no permission settings changed. Native agent token costs are unknown. The root
session coordinates review, Git updates and reporting through the deadline.

Each host branch has STATUS.md, HANDOFF.md, ACTIVITY.md and NATIVE-STATUS.json.
[Worker dashboard](AWS-WORKERS.md) tracks published host revisions. Sequential
three-pass populations are explicitly labelled when independent slots are unavailable.

## Release verification

A separate read-only controller auditor is scheduled for08:00:20UTC using
`scripts/audit-aws-release.py`. Its02:59UTC live preflight found all three OSS
coordinators still stopped, no active owned job units at that instant, and all
three release timers scheduled for08:00UTC. This is not release proof. The final
audit requires a release marker, saved status, live coordinator PID, inactive
owned slice, and no active owned jobs or remaining cgroup processes. Connection
details and pending output remain private; publish verified generic results after
the timers actually fire. The auditor changes no service state.


## 19 October03:42 UTC — Intel scan primary replication audited

Exact A/B scan replication passes both qualified primary cases on Intel. Root audit
reconstructs48 A/A +96 candidate rows,36 total blocks, frozen hashes, serial CPU2,
callbacks/checksums and exact owned memory. A medians−6.666%/−3.847%; B−6.665%/−3.661%
at100K/1M. B alone advances under the preregistered source preference, not a speed
superiority claim. Full guards, fresh confirmation and matched profiles remain.
Source NONE; AWS counts stay7 populations (0 accepted/4 rejected/3 parked), plus
one parked ARM replication and the in-progress Intel replication. ARM prepares
focused guard fixtures; AMD profiles a distinct deletion offset-adjust loop.
See AWS-DECISIONS.md and reviews/aws-intel-scan-raw-audit.json under NIGHT-EXPLORATION-001.
Lease release remains08:00UTC; live restoration verification is still required.
