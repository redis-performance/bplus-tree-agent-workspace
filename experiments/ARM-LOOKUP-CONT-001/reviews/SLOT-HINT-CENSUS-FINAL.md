# Slot-hint census independent semantic review

**PASS for the observed structural census. Selected source remains NONE.** All twelve raw outputs pass the frozen strict checker and the independent reductions described below. The slot-zero policy has nonzero useful exposure in these fixed fixtures, so the protocol's zero-primary-exposure closure does not apply. This establishes neither a speed improvement nor candidate admission, correctness over unobserved histories, qualification or adoption.

| Evidence | SHA256 |
|---|---|
| Frozen source directory manifest | `f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b` |
| Frozen strict checker | `9c415e2a56faa6edd7babdd1e7c9c74cc03d38227f16637faf2a13af4c742c04` |
| Native ELF | `8facf50e3c68a07ecc738aed446a0f0f9290e85e5d69c26e82d727e98031687c` |
| LTO ELF | `0a9c7f0dca40d181bd8770dcd0c46c7eb9030ca584749dfc2e0db6514cedaf39` |
| Fetched raw archive | `d255033ba0473657a09eee23aedaadc9f65711f617f722f02a3ded482e8a9051` |
| Independent semantic reductions and raw-output hashes | `7b6eabc1eec8cff7751f271079c940e85d588efeac54c37991a3be13f6b6f4ac` |

The reviewer authored proposal B and the earlier design/source/target-code reviews, and supplied preparation findings. The diagnostic implementation, collector and operational review have separate authors. This review used fetched raw files only; it launched no fleet action, C executable or measurement. See the [source review](SLOT-HINT-CENSUS-CODE.md) and [exact target-code review](SLOT-HINT-CENSUS-TARGET-CODE.md) for instrumentation and emitted-code limits.

I independently hashed the raw archive and matched its saved stdout/stderr bytes to the fetched files. Both sets of six files were parsed through the frozen `loads()` before `check_all()`, retaining duplicate-key rejection. Both derived checker results exactly match their saved validation outputs. All six native/LTO stdout pairs are byte-identical; all twelve diagnostic stderr files are empty. The command log has twelve diagnostic and two validation entries, all return code zero, in the fixed case order. Diagnostic commands select the reviewed native/LTO ELF path and exact case. The config hash joins the admission record, its 105 input pins still match the frozen inputs, and both retained ELF hashes independently match. Live process identity, fetch isolation and reservation compliance are the separate operational audit's responsibility.

In addition to rerunning the reviewed checker, I independently reduced raw leaf events into terminal/stale partitions and unique useful-query sets, reduced filter events by consumer and outcome, replayed actual allocation/promotion/release records, checked immediate and validation memory endpoints, and checked the absence of counted mutations. Those reductions agree with all reported totals. A useful query requires a full shadow predicate success and the original leaf search succeeding; no shadow success replaced an original lookup.

| Case | Useful queries / counted queries | Exposure | Original leaf-call events | Tree-owned bytes before / after / validation |
|---|---:|---:|---:|---:|
| hit | 124 / 500 | 24.8% | 502 | 14,272 / 14,272 / 14,272 |
| score | 124 / 500 | 24.8% | 502 | 14,272 / 14,272 / 14,272 |
| miss | 0 / 500 | 0% | 9 | 14,272 / 14,272 / 14,272 |
| long | 118 / 500 | 23.6% | 503 | 146,656 / 146,656 / 146,656 |
| external | 126 / 500 | 25.2% | 501 | 217,600 / 217,600 / 217,600 |
| update | 248 / 1,000 | 24.8% | 1,004 | 14,432 / 14,432 / 14,432 |

Exposure percentages are query counts, not time saved or a speed prediction. Query and event denominators are distinct: collision candidates can create more than one original leaf-call event per query. The seed17, 500-member fixtures, 1000 warmup sweeps, one counted read sweep or two counted update sweeps are unchanged. Original hits are 500 for each successful read case, zero for miss and 1000 for update; the score sum is exactly 125250 for score and zero for the other reported models. Native/LTO agreement is agreement of these deterministic structural observations, not an independent performance replication.

The observed terminal partition is specific and limited. Hit/score each have 376 nonzero-index-slot events, two full-predicate failures and 124 successes. Miss has five nonzero-slot events and four full-predicate failures. Long has 379 nonzero-slot events, five disabled hints, one full-predicate failure and 118 successes. External has 374 nonzero-slot events, one disabled hint and 126 successes. Update has 752 nonzero-slot events, four full-predicate failures and 248 successes. There are **no out-of-range, wrong-tag or stale hint events**. Every enabled observed slot-zero hint is classified unchanged by the seed predicate; a failed current-query predicate does not imply stale seed identity.

The filter census observes only lookup consumers. Hit/score have eleven reached filter evaluations each, long six, external seven and update twenty-two; all are original positives and remain folded positives. Miss has 500 reached filter evaluations: eleven original positives, 487 negatives under both mappings, and two original negatives that become folded positives. The added positives occur at query IDs456 and480. No original positive becomes negative. The original branch decisions remain in force: those two shadow positives execute no added displaced probes or leaf searches. They do not quantify the cost of a real folded-filter implementation or a complete alternative control-flow path. Reference-maintenance and direct-scan consumer counts are zero in every case.

All initial hints are from CopyLeaf, not Rebuild. Across the two live tree tables the initial snapshots contain 248 hints for hit/score/miss/update, 236 for long and 252 for external; these are not counts of useful target queries. Setup lifecycle records show six allocations, four promotions and six releases for the short/update fixtures, or twelve allocations, ten promotions and twelve releases for long/external. Generations increase monotonically and registry slots are reused after release. There are no duplicate-table or defrag-rebind events, and address reuse itself is not recoverable from address-free output. All observed tables use narrow IDs. Maximum leaf ID observed in counted leaf events is33 for long and5 for the others; this supplies no large-ID boundary coverage.

Most importantly, **every case, including update, has zero counted mutation events and zero ID-write, invalidation, seed-attempt and seed totals in warmup, counting, validation and cleanup**. All seeding activity is in setup. There is no active resize in any counted query. Update's first and second sweeps have exactly the same 124 useful query positions, yielding 248 useful query IDs. This is stable-hint exposure across the prescribed updates; it is not runtime validation of invalidation/reseed, stale hints, reference moves, Rebuild seeding, receiving-table large IDs, duplication, defrag or scan. Their synthetic/static checks remain preparation evidence only. Full setup seed bytes/history are C-asserted evidence rather than independently reconstructed from JSON.

The original model and final validation assertions succeed in all twelve runs. The final two lifecycle events release the remaining source and target table generations after the counted phase; the replay ends with no live generations. Each final record asserts the post-original-free completion fence and absent active contexts, consistent with the previously reviewed source placement after both trees and member/miss buffers are freed. This is evidence of successful completion of that instrumented cleanup path, not a general allocator leak detector. Immediate memory endpoints equal the independent fixed baseline values; they do not measure the prospective implementation's memory overhead or prove its <=1% memory guard, because shadow state lives outside tree ownership.

No execution-time measurement, PMU counters or performance comparison was collected. No changes to the frozen policy, fixtures, bounds or source are justified by these observations alone. H2 and Q4 remain PARK, H2R1 remains unadmitted, ARM remains released, and this diagnostic adds no optimization approval or performance attempt. A future implementation requires separate admission and the unchanged correctness, portability, memory, performance and confirmation gates.

The prior source consultation supplied no supporting passage. TMA remains uncollected:

| TMA category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

All child categories are unavailable. Structural exposure is not a substitute for those shares.
