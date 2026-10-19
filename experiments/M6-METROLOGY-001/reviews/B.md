# B — independent schedule and endpoint diagnostic

All 48 public raw CSV rows and 96 stdout/stderr streams reconstruct exactly against their journal/hash publication and frozen schedule. All 12 ABBA blocks and the original wall decisions agree: 100K 6/6, 1M 3/6. Source NONE and EXP009 PARK remain unchanged. No native benchmark/profile/build/source edit occurred. This is not an optimization population. Participant /root/followup_proposal_b; exact serving model/token/currency costs unknown.

The diagnostic hypothesis that descheduling alone sufficiently explains all three failed 1M wall controls is not supported. Each of those blocks also exceeds the same ±1% threshold when reconstructed from recorded thread CPU time. This recorded contrast diagnostic does not identify the physical cause. In particular it does not formally falsify physical descheduling-only without a measured wrapper/accounting-error bound. Thread CPU time never replaces the preregistered wall clock.

|Members|Block|Seed|Wall contrast|Thread contrast (diagnostic)|Original wall gate|Thread±1%|Residual contrast ms|
|---:|---:|---:|---:|---:|---|---|---:|
|100,000|1|1|+0.066263%|+0.062961%|pass|within|+0.039749|
|100,000|2|2|+0.220646%|+0.237541%|pass|within|-0.195543|
|100,000|3|3|-0.016887%|+0.004118%|pass|within|-0.247459|
|100,000|4|1|+0.299162%|+0.288096%|pass|within|+0.134293|
|100,000|5|2|+0.147094%|+0.146667%|pass|within|+0.007416|
|100,000|6|3|-0.636548%|-0.629651%|pass|within|-0.092625|
|1,000,000|1|1|-0.614488%|-0.619500%|pass|within|+0.050832|
|1,000,000|2|2|-0.593165%|-0.596221%|pass|within|+0.027126|
|1,000,000|3|3|-1.414059%|-1.401384%|**FAIL**|**outside**|-0.183208|
|1,000,000|4|1|+0.841157%|+0.843931%|pass|within|-0.018460|
|1,000,000|5|2|+1.036273%|+1.008640%|**FAIL**|**outside**|+0.354667|
|1,000,000|6|3|+2.567325%|+2.542454%|**FAIL**|**outside**|+0.342167|

Each contrast uses the same four original rows, with outer positions 0+3 versus inner 1+2. The last column is the difference between inner and outer **sums** of signed wall−thread residuals. For failed 1M blocks 3/5/6, wall contrasts are −17.538/+12.683/+31.341ms; residual contrasts are −0.183208/+0.354667/+0.342167ms. These are paired-sum arithmetic decompositions, not causal fractions of descheduled time. The thread brackets surround slightly wider code than wall brackets, so residuals include clock-edge/accounting differences and cannot be read as exact off-CPU duration.

## Repetition and temporal order

All six seeds/positions retain the original deterministic order, with size order alternating by block and seeds 1/2/3 repeated in blocks 4/5/6. For 1M, each first seed occurrence has a negative inner-pair contrast, while each repeat is positive. Seed 1 changes−0.614488→+0.841157%; seed 2−0.593165→+1.036273%; seed 3−1.414059→+2.567325%. The thread contrasts show the same sign reversals. A stable fixture/seed effect alone does not explain these repeated-seed differences. Time/context interactions remain possible.

This is a post-hoc pattern in six blocks, not a validated temporal mechanism. Repetition simultaneously changes temporal half and which size executes first. Position summaries and all raw rows are in B.json; averaging complementary contrasts would hide the very failed blocks and is not allowed. ABBA ideally cancels equally spaced linear drift, but process-start timestamps include construction/warmup/postvalidation and do not reveal equally spaced timer-window centers. No observed sign flip uniquely implies nonlinear drift, warmup insufficiency, DVFS or cache behavior.

## CPU endpoint associations

- 100,000: endpoint changes 10/24; pair counts {'6->6': 8, '6->7': 5, '7->6': 5, '7->7': 6}; signed wall−thread residual 0.623167–0.995250ms.
- 1,000,000: endpoint changes 10/24; pair counts {'6->6': 6, '6->7': 8, '7->6': 2, '7->7': 8}; signed wall−thread residual 0.704833–1.058542ms.

Both sizes observe only endpoints 6/7, with both unchanged and changed pairs represented across ABBA positions. B.json retains every position and pair stratum without dropping a row or pooling size-specific ns/query. The grouping is unbalanced and post-hoc. Endpoint equality does not establish no migration; endpoint difference says nothing about residence duration, frequency or CPU type. The same binary, fixture seed and outputs remain constant within each quad; endpoints were neither assigned nor randomized. Therefore the endpoint associations do not support a causal core-placement correction.

## MCP availability and shared consultation

Own availability check at 11:33:43 UTC: no cpu-perf/library_status/check_evidence tool was exposed in ALL_TOOLS; list_mcp_resources exposed only codex_apps, no cpu-perf server. I consumed the **shared root consultation** explicitly permitted by docs/PERFORMANCE-MCP.md, not calls claimed as my own. Root's local stdio journal contains successful initialize,library_status,ask and read_source calls at 11:32:55–11:32:56 UTC. Server 0.1.1 uses bundled list commit deb5a0bac467. Initial coverage was 0/287 indexed and ask returned no source passage. Root subsequently retrieved the primary [LLVM benchmarking guidance](https://llvm.org/docs/Benchmarking.html), which states “low noise is required, but not sufficient.” That supports the bias limitation; it supplies no Apple-clock causal explanation. Full request inputs, actual response hashes and shared-journal identity are in B.json. No unread lead or M4 benchmark figure is treated as evidence for M6.

## Method recommendation: NONE

The data do not justify a new corrective method now. Replacing wall acceptance with thread time fails even descriptively in the same three 1M blocks. More work, longer windows, warmup inflation, favorable endpoint filtering or complementary-block averaging is not an evidence-supported new protocol. EXP009 already targets 600ms windows;023's separate corrected scan controls failed at224–260ms;012 used 100M iterator items and three warmups yet retained failed controls. Those contracts are different and are context, not pooled measurements or proof that any knob cannot work.

HARNESS-003 already introduced case-matched miss warmup over HARNESS-002, explicitly without proving precision or a hardware mechanism. EXP009 uses the already matched hit-query warmup; that is not a novel intervention. 017 already considered resident-worker/context controls and selected NONE because candidate/mutation/guard transfer and isolation were not concrete. Rebranding that unexecuted method now would not supply missing transfer evidence. The current offline result shows variation also in the recorded thread clock; different bracket coverage, accounting errors and physical causes remain unresolved, so it cannot select a cause. A future proposal needs distinct observable causal/context control, preserved wall-clock gates and candidate/guard transfer before any native launch; no such ready method follows from these retained endpoints alone.

Reproduce this offline report: `python3 experiments/M6-METROLOGY-001/analyze-b.py`. It imports no driver and spawns no child. All input/row hashes are rechecked after analysis. Historical context is read from the shared root checkout because the partial EXP009 worktree does not materialize those campaign files. No new peer review was read.
