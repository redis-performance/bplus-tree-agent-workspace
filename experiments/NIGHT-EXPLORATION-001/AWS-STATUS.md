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
| AWS Intel | Xeon Platinum 8488C, Sapphire Rapids | Clang 18.1.3 | CPU 2; SMT sibling 50 | Running | Pending profiles |
| AWS AMD | EPYC 9R45, Zen 5 | Clang 18.1.3 | CPU 2, no SMT sibling | Running | Pending profiles |
| AWS ARM | Neoverse V2, Graviton | Clang 18.1.3 | CPU 2, no SMT sibling | Running | Pending profiles |

Baseline source/referee commit: `8fab511e` (only Linux affinity metadata differs
from `9c192c9c`; target source unchanged). Each host runs 100/1K/10K/100K/1M members,
eight operations, 16-byte members, seeds 1/2/3, six same-binary ABBA blocks. Native
and ASan/UBSan validation precede timing. The per-host timing budget is 1200 seconds;
results are never pooled. The initial jobs are managed by systemd, bounded to
1800 seconds, and all baseline children inherit CPU2 affinity.

Next: collect and audit each baseline, add its measured series to the existing
[baseline chart](baseline-charts/m1-m6-baseline.png), profile locally on each host,
and apply [population gates](../../docs/POPULATION.md). The exact shorter-side rank
candidates rejected on both Apple hosts are skipped; lookup/update/decoder work
requires fresh AWS profile evidence. No speed claim or candidate acceptance yet.

[Activity log](AWS-ACTIVITY.md). [Worker contract](AWS-WORKER.md). Workers use existing Codex CLI configuration,
with no permission changes. Actual backend/model and measured usage are retained
when available; no invented agent identities or costs.
