# Corrected-adapter iterator profile: descriptive baseline complete

All 16 fixed captures meet the preregistered 25-PC minimum (35–75 PCs each). Source adoption remains **NONE**; no tree hypothesis is selected by this report. The corrected iterator has 114 static instructions and no normal-path stack frame. The remaining 16-byte frame belongs solely to the failing external-pointer assertion path; that cold region has zero captured PCs.

The baseline target remains `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`, with the corrected `_Noreturn` standalone adapter and unchanged decoder, scanner, layout, hash, allocator and assertions. The exact preparation freeze is `f5981f8a001f33ebc1ce06a3394d797afe21bfcabb98fec48ad28ea4c0cf3313`; profile binary SHA-256 is `e8b58ec2a89742221c00772c42493db2269fbd263c692a8db1474adb61066624`. Flags and all input identities are in [freeze.json](freeze.json).

The root authorized an exclusive runner against that exact freeze. Captures ran serially from 04:29:21.425709 to 04:29:29.623856 UTC; the driver records 8.198410291 seconds of phase wall time solely for budget accounting. All 30 preparation/capture child records show zero exit, no timeout and reaped processes. No new child was launched for this analysis. All frontend elapsed/thread-time fields remain unused.

## Retained evidence and checks

The fixed matrix is 100K/1M members × integer full forward, integer full reverse, integer score-only forward, fractional full forward × seeds 1/2. Each capture visits exactly 100,000,000 items, after three full warmup traversals, with 16-byte binary members and the fixed requested 1000 µs sampler interval. No capture was repeated or retuned. Integer scores are `i - n/2`; fractional scores add `0.25`. Random insertion permutations and hash seeds are fixed by the published seed and construction fingerprint.

The retained capture outputs pass exact counts/checksums, tree length and owned-memory invariants, full member/order/score-bit verification, copied iterator next-state checks, nullable-output sentinels and repeated end checks from the unchanged frontend. Preparation retains eight bounded native/ASan/UBSan checks (four contracts each), plus explicitly reused original 43-test evidence under matching corrected-baseline identities; these tests were not rerun during analysis.

Analysis independently reconstructed every public PC bin from the private raw PC rows, verified all 60 public/private command-log stream pairs, matched all 16 commands and environment overrides to the frozen plan, and rehashed all 18 frozen inputs and three binaries. Every iterator PC is aligned to one of the 114 mapped instructions; all symbol counts and per-capture totals reconcile. Historical known-work sampler controls remain historical reused controls, not fresh corrected-adapter calibrations. See [ANALYSIS-AUDIT.json](ANALYSIS-AUDIT.json), [capture-status.json](capture-status.json) and [validation.json](validation.json).

## Observed regions

The table preserves each size, contract and seed. Entries are sampled-PC counts, not executed-instruction counts, costs, unbiased time shares or percentages. Member includes offset-table base, physical mapping/record address and packed prefix decoding. Score includes optional-output selection, width/orientation, packed word/extraction, mask/shift and ordered-score reconstruction. Output includes member pointer, length and score stores; advance includes direction, position and leaf transitions. Entry and return remain separate. Empty/end-return and cold panic are zero in every row.

| Members | Contract | Seed | All PCs | Iterator PCs | Entry | Member | Score | Output | Advance | Return | Other symbols |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100000 | integer-full-forward | 1 | 55 | 46 | 4 | 10 | 16 | 8 | 6 | 2 | 9 |
| 100000 | integer-full-forward | 2 | 56 | 43 | 5 | 9 | 13 | 8 | 6 | 2 | 13 |
| 100000 | integer-full-reverse | 1 | 61 | 51 | 2 | 9 | 25 | 10 | 5 | 0 | 10 |
| 100000 | integer-full-reverse | 2 | 75 | 52 | 4 | 13 | 17 | 12 | 6 | 0 | 23 |
| 100000 | integer-score-forward | 1 | 48 | 39 | 9 | 0 | 16 | 9 | 2 | 3 | 9 |
| 100000 | integer-score-forward | 2 | 42 | 36 | 4 | 0 | 16 | 13 | 1 | 2 | 6 |
| 100000 | fraction-full-forward | 1 | 51 | 44 | 6 | 6 | 11 | 10 | 11 | 0 | 7 |
| 100000 | fraction-full-forward | 2 | 67 | 51 | 3 | 7 | 24 | 11 | 5 | 1 | 16 |
| 1000000 | integer-full-forward | 1 | 63 | 49 | 6 | 10 | 16 | 9 | 5 | 3 | 14 |
| 1000000 | integer-full-forward | 2 | 73 | 59 | 6 | 10 | 19 | 14 | 7 | 3 | 14 |
| 1000000 | integer-full-reverse | 1 | 68 | 54 | 3 | 14 | 27 | 6 | 4 | 0 | 14 |
| 1000000 | integer-full-reverse | 2 | 69 | 54 | 6 | 8 | 25 | 7 | 8 | 0 | 15 |
| 1000000 | integer-score-forward | 1 | 35 | 25 | 3 | 0 | 11 | 8 | 3 | 0 | 10 |
| 1000000 | integer-score-forward | 2 | 48 | 33 | 9 | 0 | 12 | 8 | 4 | 0 | 15 |
| 1000000 | fraction-full-forward | 1 | 63 | 52 | 4 | 20 | 18 | 5 | 3 | 2 | 11 |
| 1000000 | fraction-full-forward | 2 | 63 | 46 | 5 | 11 | 13 | 11 | 4 | 2 | 17 |

The fixed matrix contains 937 PCs: 734 attributed to `zbtreeIteratorNext`, 190 to its `traverse` consumer, and 13 to `__thread_selfusage` inside the retained sampling boundary. This is bookkeeping over different contracts, not a representative workload distribution. The exact fine-region table and all 16 rows are in [region-summary.json](region-summary.json) and [region-summary.csv](region-summary.csv).

Full-output captures have member-region observations in every size/seed pair; all four score-only captures have zero member-region and member-output PCs, consistent with the optional-output branch in the assembly. Score, output and advance regions are observed in every capture. External-record decode and the cold panic frame have zero sampled PCs in this 16-byte inline-member matrix. Zero PCs do not prove a path never executed.

Within this fixed matrix, the largest single instruction bin is `+0x100: mov x13, #-0x1` (159 PCs), followed by `+0x140: str x10, [x4]` (107). Other observed points include `+0x05c` packed prefix load (56), `+0x0cc` packed score-word load (49), `+0x034` reversed-flag load for member addressing (43), and `+0x188` iterator-position store (31). These locations identify where the sampler interrupted execution. They do not measure the latency of those instructions, establish predecessor stalls, demonstrate cache misses, or justify replacing the mask or output stores.

## Exact assembly mechanism

[pc-map.json](pc-map.json) maps every instruction, not just sampled offsets, to explicit nonoverlapping manual regions and source reference lines. References describe source semantics after optimization; DWARF line attribution is unavailable. Static linked addresses in the assembly/map are not private runtime pointers; published sample bins use symbol-relative offsets only.

Current member work retains score-stream-size arithmetic to find the offset array, optional physical reversal, a 16-bit record-offset load, packed-record prefix decoding, then requested pointer/length stores. Score work retains the original physical-position/bit-position calculation, packed-word load and possible ninth-byte merge, mask/shift, base/orientation reconstruction, ordered-to-double transform and requested score store. Forward/reverse position and leaf transitions remain explicit. These are actual assembly dependencies, but this profile does not establish their critical-path latency or a profitable replacement.

The original-adapter [009 map](../009-iterator-profile/pc-map.json) has 155 instructions, including a 96-byte normal frame with six register-pair saves and matching restores. In the corrected 114-instruction binary, normal entry begins directly with the iterator leaf load and normal returns have no register restores. Only `+0x1a8`/`+0x1ac` create a 16-byte cold panic frame, ending in the sole call at `+0x1c4` to the truthful always-aborting panic handler. The tree source is unchanged. This is a descriptive assembly comparison across adapter identities; no old/new PC populations are pooled or subtracted, and no speed effect is inferred from the 155→114 instruction difference.

## Limits and grounds for later review

The 25-PC floor is a screening sufficiency rule, not a precision guarantee. Each capture has only 35–75 samples; two seeds cannot remove sampling aliasing, interrupt skid, or scheduling effects. The requested 1000 µs interval is not proof of actual cadence. The sampler uses nearest-symbol attribution with explicit offsets, not hardware event counters or source-line cost attribution. The retained boundary includes traversal consumer work and QoS/CPU/thread-clock observations, reflected by the non-iterator samples. No cycles, cache behavior, branch-miss rate, frequency, actual core residency or migration history is established.

This profile covers masks 7 and 4, ordinary integer/fraction scores and 16-byte inline members at 100K/1M. It does not supply all-output-mask, long/external-member, zero/small-size, empty/seek, copied-direction-change/invalidation, physically reversed-leaf, wide finite-score/score-width, signed-zero or portability performance guards. Semantic checks outside the sampling boundary remain useful correctness evidence without adding sampled coverage of those paths.

The corrected baseline now has a trustworthy location inventory for future review: score decode/output, member-address/prefix work and iterator advance are still visible, while the old normal-frame mechanism is absent. This evidence alone does not establish that any extra cached state, early decode, decoder change or other added work would improve public lookup or iteration. A later chair must identify one new causal hypothesis, account for maintenance/state costs, retain full semantic guards, and obtain qualified same-session comparisons, candidate profiling, independent confirmation and adversarial review. This report proposes no tree candidate.

Analysis participant: `/root/followup_proposal_a`, inherited GPT-6/Codex family; exact serving identifier, token usage and currency cost are unknown. The analyst also prepared this frontend/freeze and earlier 007 geometry census; this is not an independent audit of its own harness authorship. Root runner/review and an independent artifact review remain distinct roles. No source/adapter/referee changes, build, capture, timing, Git write or new agent occurred during analysis.

Reproduce the retained-evidence analysis from the repository root with:

```sh
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/013-corrected-iterator-profile/analyze.py
```

The script reads retained evidence and emits only the PC map, region tables, analysis audit and this report. Public artifact hashes are sealed separately in `artifacts-sha256.json`; private raw logs remain scratch-only with preserved hashes.
