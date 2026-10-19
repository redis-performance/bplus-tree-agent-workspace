# AWS worker publications — campaign complete

All three runner leases are released. Live verification passed on 19 October,
08:00:20–08:00:25 UTC (09:00:20–09:00:25 Lisbon): OSS coordinators RUNNING,
owned slices inactive and no owned units or processes remaining.
[Morning report](AWS-MORNING-REPORT.md) · [Live proof](reviews/aws-release-final.json).

The branch snapshots below retain their original observations. The release proof
above supersedes any earlier active-lease wording in those snapshots.

| Host | Final measurement status | Published revision | Evidence |
|---|---|---|---|
| Intel | Complete; corrected replication PARK before candidate timing | `208dff5cc` | [Status](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/208dff5cc842c0f3eed41901681ddb9f44fb67ee/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/STATUS.md), [activity](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/208dff5cc842c0f3eed41901681ddb9f44fb67ee/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/ACTIVITY.md), [handoff](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/208dff5cc842c0f3eed41901681ddb9f44fb67ee/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/HANDOFF.md) |
| AMD | Complete; corrected replication REJECT, baseline iterator NONE | `b3c2eb5fd` | [Status](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b3c2eb5fd7783f0da9e0856dd3764197a58109dd/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/STATUS.md), [activity](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b3c2eb5fd7783f0da9e0856dd3764197a58109dd/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/ACTIVITY.md), [handoff](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b3c2eb5fd7783f0da9e0856dd3764197a58109dd/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/HANDOFF.md) |
| ARM | Complete; corrected NEON REJECT, historical mask primary PARK | `03ae0b8cc` | [Status](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/03ae0b8cc5f58dad1c490f24bffb8faf4f56b73c/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/STATUS.md), [activity](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/03ae0b8cc5f58dad1c490f24bffb8faf4f56b73c/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/ACTIVITY.md), [handoff](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/03ae0b8cc5f58dad1c490f24bffb8faf4f56b73c/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/HANDOFF.md) |

Eight measured populations remain 0 accepted / 5 rejected / 3 parked; replications
are separate. All 24 population patches and raw results are retained. Source NONE.
The local status publisher has stopped. Historical detached CLI launch failures are
retained; native-agent serving models, measured tokens and monetary costs are unknown.
