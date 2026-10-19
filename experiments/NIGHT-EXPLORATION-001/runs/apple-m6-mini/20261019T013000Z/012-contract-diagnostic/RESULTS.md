# Matched adapter diagnostic — all effects conditional

Completed 2026-10-19T04:23:24.629412+00:00. This is a standalone adapter/compiler-contract diagnostic, not a tree candidate, optimization population or acceptance. The truthful `_Noreturn` adapter correction was separately reviewed and committed before these observations. Tree source C/header remain unchanged.

Both phases complete:384 separate-adapter A/A processes and192 old/new ABBA processes. Operation timers sum117.249697s and58.691230s respectively; phase wall199.857468s and100.236612s. All children reaped. All fixed fixture, member/order/exact-score/count/checksum/fingerprint and owned-memory invariants pass. No retry, count change or discarded row.

Only3/16 A/A adapter/workload cells qualify; no workload has qualifying controls for BOTH adapters. All windows exceed10ms. Therefore **all eight comparison effects remain conditional**. The comparison was explicitly preregistered even with failed controls. All48 comparison block memory effects are exactly0%. No historical timing subtraction or old/new baseline pooling.

|Members|Contract|Median new/old elapsed change|Six-block observed range|Both controls qualify|
|---|---|---|---|---|
|100,000|integer-full-forward|-6.081%|-7.119% to -4.618%|No|
|100,000|integer-full-reverse|-8.122%|-9.372% to -7.037%|No|
|100,000|integer-score-forward|-1.966%|-7.808% to +8.308%|No|
|100,000|fraction-full-forward|-3.434%|-5.694% to -0.077%|No|
|1,000,000|integer-full-forward|-4.674%|-6.937% to -2.682%|No|
|1,000,000|integer-full-reverse|-7.058%|-9.229% to -5.837%|No|
|1,000,000|integer-score-forward|-9.864%|-18.417% to -2.722%|No|
|1,000,000|fraction-full-forward|-5.164%|-6.668% to -3.661%|No|

Negative means less elapsed time. Integer full-output forward/reverse show lower elapsed time in all six observed blocks at both sizes, but failed controls prevent a qualified performance claim. The100K score-only result spans both signs; medians alone conceal that instability.

The two builds compile identical target/referee source paths and use identical flags, assertion evaluation, allocator and hashing. Their adapter declaration/definition differ only by the truthful non-returning contract. Matching panic filename literals avoid source-path differences. The reviewed static effect is155→114 iterator instructions with no normal96-byte frame; these observations do not isolate instruction/cycle costs.

Root and independent driver reviews passed before freeze publication9e2657483; A/A evidence published26c2e139f before comparison launch. Exact authorization and launch records are retained. Source/referee/binary identities are in freeze.json; all576 raw rows and process logs remain public, with original private command/log copies hashed in ignored scratch.

[Independent audit](INDEPENDENT-AUDIT.md) PASS:576rows/144exact effects,604command records,1208public/private log pairs,22frozen identities, seven independently reconstructed fixture fingerprints and nine checksum contracts. All576measured UTC intervals are serial, reaped and within budgets. [Chart](CHART.md) shows every block, median, observed range and qualification limit; root visually inspected the PNG. The descriptive endpoint census is independently verified. No tree optimization accepted; completed candidate counts remain12populations,0accepted/7rejected/5parked,36patches/15performanceharnesses plus one adapter revision and one proposal-only NONE review. This diagnostic adds no candidate population.

Next: obtain a fresh baseline-only iterator profile under the corrected adapter before selecting any new tree hypothesis. The previous009 profile remains valid for its original adapter only. No cache replication is selected. Participant/root and actual agents A/B/C: inherited Codex/GPT-6 family; exact serving model/token/currency costs unknown.
