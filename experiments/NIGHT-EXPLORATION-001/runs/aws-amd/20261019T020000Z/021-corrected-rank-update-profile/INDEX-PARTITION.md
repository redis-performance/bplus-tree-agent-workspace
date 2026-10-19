# Read-only index-reference/ID-write partition

Existing021 captures only; no new workload. Categories assign each top-IP sample once; caller addresses at other IPs are used only to classify reference-call ancestry, not added to sampled cost. All denominators retain unknown/control samples. SourceNONE.

| Update members | Reference search | SetId inside Move | Other Move |
|---|---:|---:|---:|
|100000|3.396% / 247events|0.192% / 14events|0.452% / 33events|
|1000000|2.317% / 385events|7.921% / 1315events|0.072% / 12events|

Reference search is only3.396%/2.317% of sampled period, distinct from SetId0.192%/7.921%. At1M,1311of1315 exclusive SetId events (99.7% of its period) land on the unconditional jump immediately after the narrow-ID store, with exact same source/code in actual015 timing binary. This does not prove that the branch is expensive, that a store is redundant or that cache-miss latency is removable. Rank TagMask similarly concentrates96.03% of its exclusive period on XOR immediately after the bucket load; sdsType99.7–99.9% is on the first-header-load successor. These observations agree with keeping the earlier query-length NONE and avoiding arithmetic conclusions from coarse source attribution.

Reference ancestry further narrows the saved-current-pointer idea: at100K47.22% of reference periods are under insertion/split and34.66% under merge, versus16.11% through direct IndexMove→UpdateScore. At1M54.02% are insertion/split and32.73% merge, versus12.21% direct. These direct-chain subsets are roughly0.547%/0.283% of all operation period, respectively; a small remainder has shorter recorded stacks. Thus most reference samples concern structural movement of members, not simply re-finding the currently updated member. The sum of all reference period is not an estimate of work removable by caching that member’s bucket pointer.

The saved pointer would also need a proof covering zbtIndexReserveLeafId, deletion/merge, insertion/split, active migration, narrow/wide tables, tombstones and revisions; the existing position does not authorize bypassing those invariants. No such proof, distinct optimization hypothesis or candidate is proposed. Read-only partition supports NONE rather than using a7.9% ID-write label as presumed redundant-search headroom.

Callchains and source-linked instructions are sampled evidence, not an exact census; stack truncation/skid remain limits. All1395actual timing instruction mappings and raw frames stay retained.
