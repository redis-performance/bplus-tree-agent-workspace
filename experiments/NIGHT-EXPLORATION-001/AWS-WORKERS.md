# AWS worker publications — campaign complete

All three runner leases are released. Live verification passed on 19 October,
08:00:20–08:00:25 UTC (09:00:20–09:00:25 Lisbon): OSS coordinators RUNNING,
owned slices inactive and no owned units or processes remaining.
[Morning report](AWS-MORNING-REPORT.md) · [Live proof](reviews/aws-release-final.json).

All three final branch handoffs record completion and verified release, linking the
immutable release proof. Earlier active-lease entries are preserved as history.

| Host | Final measurement status | Published revision | Evidence |
|---|---|---|---|
| Intel | Complete; corrected replication PARK before candidate timing | `1b1f5c9b9` | [Status](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/1b1f5c9b954bd0c1bd173d38c57e8e93542ea283/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/STATUS.md), [activity](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/1b1f5c9b954bd0c1bd173d38c57e8e93542ea283/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/ACTIVITY.md), [handoff](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/1b1f5c9b954bd0c1bd173d38c57e8e93542ea283/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/HANDOFF.md) |
| AMD | Complete; corrected replication REJECT, baseline iterator NONE | `493c7418b` | [Status](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/493c7418b56c49ed086d8dd02bcf07b620c77cd1/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/STATUS.md), [activity](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/493c7418b56c49ed086d8dd02bcf07b620c77cd1/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/ACTIVITY.md), [handoff](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/493c7418b56c49ed086d8dd02bcf07b620c77cd1/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/HANDOFF.md) |
| ARM | Complete; corrected NEON REJECT, historical mask primary PARK | `e0b1ef25a` | [Status](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/e0b1ef25a583df8c276a368dffe38ab1ffc81cd4/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/STATUS.md), [activity](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/e0b1ef25a583df8c276a368dffe38ab1ffc81cd4/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/ACTIVITY.md), [handoff](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/e0b1ef25a583df8c276a368dffe38ab1ffc81cd4/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/HANDOFF.md) |

Eight measured populations remain 0 accepted / 5 rejected / 3 parked; replications
are separate. All 24 population patches and raw results are retained. Source NONE.
The local status publisher has stopped. Historical detached CLI launch failures are
retained; native-agent serving models, measured tokens and monetary costs are unknown.
