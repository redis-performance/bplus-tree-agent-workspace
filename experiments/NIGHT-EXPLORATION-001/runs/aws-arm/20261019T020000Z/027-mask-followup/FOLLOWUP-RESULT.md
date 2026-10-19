# Fresh ARM mask continuation: REJECT, source NONE

The exact historical EXP005 A patch is rejected in this fresh corrected-adapter ARM session. The fixed primary improved in every block, but nine independently qualified iterator guard cells regressed by more than 1% in all six blocks. The broader guard failures override the primary gain. This does not rewrite historical EXP005 or overnight 026 PARK decisions.

Exact baseline source is 13e459ff8; the immutable historical patch is ca14579cbf4325816d5511697cb0bec5ab0e618ef661830acbc4bfe72a5cc88f. Actual baseline binary 330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc and candidate b1cb9e4b2a1df204a75b4b4a3264364c3f0b5b46dbf475bae72c3c9a3ee5811d were preserved. No algorithm was retuned or adopted.

All six frozen measurement phases completed: 4,272 processes and 5,952 raw benchmark rows. Fresh primary A/A qualified both sizes, and candidate primary gains were 6.59–7.92%. Original guards qualified 18/29 required cells; 17 passed comparison and 100-member SCAN had a mixed loss, while 11 required controls stayed unresolved. Iterator controls qualified 43/82; comparison produced 30 passes, 4 mixed losses, 9 all-block regressions, and 39 unresolved controls. No short iterator controls occurred.

## Demonstrated iterator regressions

All entries use the unchanged HARNESS-004 score-only mask 4, 16-byte members, 20M requested visits, three warmup passes and fixed six ABBA blocks. This guard frontend is distinct from the 50M primary frontend; its qualified measurements are not pooled with primary timings.

| Cell | Size | Score encoding | Direction | Paired elapsed increase, six-block range |
|---|---:|---|---|---:|
| g004 | 100,000 | integer | forward | +2.573% to +2.997% |
| g012 | 100,000 | integer | reverse | +8.271% to +8.510% |
| g020 | 1,000,000 | integer | forward | +2.712% to +3.104% |
| g028 | 1,000,000 | integer | reverse | +2.964% to +3.523% |
| g033 | 100,000 | fraction | forward | +2.755% to +2.987% |
| g037 | 100,000 | fraction | reverse | +8.485% to +8.635% |
| g041 | 100,000 | wide | forward | +2.651% to +3.083% |
| g049 | 100,000 | zero | forward | +2.711% to +3.005% |
| g053 | 100,000 | zero | reverse | +7.327% to +8.490% |

All semantic output and tree-owned byte comparisons passed. Both original and continuation correctness records remain intact: original 027 preparation is FAILED because injected signed-zero corruption triggered a valid earlier assertion than its registered needle; separate 028 ran only six previously unstarted commands. The independently reviewed composite establishes correctness eligibility without rewriting that failed attempt.

## Evidence and remaining limits

- [Primary control result](PRIMARY-AA-RESULT.md), immutable 53e193c5b; [primary replication](PRIMARY-REPLICATION-RESULT.md),451456c2f.
- [Original control result](ORIGINAL-AA-RESULT.md),1329e440a; [original comparison](ORIGINAL-COMPARISON-RESULT.md),4c7668661.
- [Iterator control result](ITERATOR-AA-RESULT.md),8ed45423c; [iterator comparison](ITERATOR-COMPARISON-RESULT.md),f30ac4330. Each has its own complete raw rows, publication map and evidence seal.
- [Frozen matched profile](../029-mask-matched-profile/PLAN.md) remains prepared and UNEXECUTED. Independent held-out confirmation remains UNEXECUTED and was already ineligible after original guard precision failures. Neither is required to establish the measured guard rejection, and no mechanism or acceptance claim is made.
- Uniform identical-bit width-zero performance coverage remains missing; alternating signed-zero ties do not fill it. Unqualified cells remain unresolved. No new runs, retries, changes to counts or discarded blocks occurred.

The final independent raw review and fresh lease restoration proof are recorded additively in campaign status after publication. At this report's preparation the runner was verified idle; fresh lease release was still pending parent verification. Original 08 UTC release history is separate.

## Final independent review and release

Intel independent raw audit [d3cc358f2](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/d3cc358f2/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/029-arm-guard-raw-review/iterator-comparison-f30ac4330/REVIEW.md) confirms the complete comparison and A/A reconstruction and REJECT decision. Root independently reaches the same decision.

ARM lease is RELEASED. The [canonical immutable live proof](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/2a53fc3f3/experiments/ARM-MASK-FOLLOWUP-001/RELEASE-FINAL.json) records coordinator RUNNING with matching saved/live process identity, inactive owned slice, zero owned units/processes and no inspection errors, verified 2026-10-19T10:03:25.494971+00:00–2026-10-19T10:03:27.123716+00:00. The release-attempt marker is10:03:18UTC; it is not an exact restoration-completion timestamp. No further workloads are pending.
