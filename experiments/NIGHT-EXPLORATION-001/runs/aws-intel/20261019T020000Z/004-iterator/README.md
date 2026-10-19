# Intel iterator cache — PARK / NONE

The fixed exploratory screen stopped at its preregistered 300-second ceiling: **566 of 576 processes, 141 complete ABBA blocks and two trailing rows**. The helper returned1 after the internal budget assertion. No extension, rerun, row exclusion or source adoption. The raw discovery.json status remains running because the assertion interrupted finalization; this report and helper metadata record the actual bounded stop. The ten missing rows are the final 1M integer/full-output/forward block for A/B/C (one pair is present but incomplete). All other cells have six complete blocks.

A pointer cache and B 32-bit offset cache are conditional leads. C 16-bit offset cache regresses full-forward and score-only cases and is rejected. No winner is selected. Both population stages were sequential passes, not independent agents; exact backend/model and token costs remain unknown.

| Cell | Variant | Complete blocks | Median elapsed change | Block range |
|---|---|---:|---:|---:|
| 100000-fraction-forward-7 | A | 6 | -6.671% | -20.066..+3.743% |
| 100000-fraction-forward-7 | B | 6 | -5.078% | -18.241..+7.305% |
| 100000-fraction-forward-7 | C | 6 | +14.929% | +3.600..+26.177% |
| 100000-integer-forward-4 | A | 6 | -1.113% | -1.857..-0.866% |
| 100000-integer-forward-4 | B | 6 | -1.235% | -2.226..-1.106% |
| 100000-integer-forward-4 | C | 6 | +4.228% | +2.552..+4.978% |
| 100000-integer-forward-7 | A | 6 | -7.574% | -10.941..-6.855% |
| 100000-integer-forward-7 | B | 6 | -6.023% | -18.314..-2.615% |
| 100000-integer-forward-7 | C | 6 | +18.430% | +2.285..+26.321% |
| 100000-integer-reverse-7 | A | 6 | -5.430% | -8.100..-4.382% |
| 100000-integer-reverse-7 | B | 6 | -6.173% | -8.789..-2.975% |
| 100000-integer-reverse-7 | C | 6 | -1.966% | -5.540..-0.777% |
| 1000000-fraction-forward-7 | A | 6 | -6.730% | -6.829..-6.525% |
| 1000000-fraction-forward-7 | B | 6 | -4.340% | -4.798..-4.279% |
| 1000000-fraction-forward-7 | C | 6 | +16.510% | +16.216..+17.554% |
| 1000000-integer-forward-4 | A | 6 | -0.944% | -1.074..-0.579% |
| 1000000-integer-forward-4 | B | 6 | -1.026% | -1.156..-0.864% |
| 1000000-integer-forward-4 | C | 6 | +4.326% | +3.257..+4.765% |
| 1000000-integer-forward-7 | A | 5 | -6.559% | -6.780..-6.502% |
| 1000000-integer-forward-7 | B | 5 | -4.643% | -4.916..-4.153% |
| 1000000-integer-forward-7 | C | 5 | +16.578% | +16.376..+17.669% |
| 1000000-integer-reverse-7 | A | 6 | -7.191% | -7.471..-6.956% |
| 1000000-integer-reverse-7 | B | 6 | -5.809% | -5.947..-5.699% |
| 1000000-integer-reverse-7 | C | 6 | -2.843% | -3.221..-2.348% |

Negative elapsed change is faster. The declared primaries are integer/full-output/forward at100K and1M; fractional, reverse and score-only cases are guards. Full output returns member pointer, length and score; timed consumer reads first member byte, length and score bits, with complete member-byte validation outside the window.

100K primary A/A fails (+0.562..+2.950%), while1M qualifies (−0.157..+0.094%). Both A/B have favorable observed primary blocks, but the schedule is incomplete and100K fractional guards exceed+1% in noisy observations. No acceptance, fine ranking, independent fresh confirmation or full guard qualification follows from these rows. A uses24-byte iterator state versus16 baseline; B/C use16 on this64-bit target. Tree-owned memory is exact in every complete block.32-bit layout remains unmeasured.

Validation: all four sources pass43 unchanged original tests per native/sanitizer build,1,920 iterator fixture cells/source, and28,192 state checks per build before timing. Two deliberate B reset omissions trigger UBSan/ASan. A separate additive oracle after the screen passes89,428 total state checks per source/build (including original28,192), adding direction toggles and mutation followed by explicit reinitialization; no invalid iterator is used after mutation. The initial invalid unequal-score SeekLex oracle expectation is retained in attempt001-oracle. See VALIDATION.md, comparison-freeze.json and raw logs.

Independent static review: main434e39ef5, experiments/NIGHT-EXPLORATION-001/reviews/aws-intel-iterator-cache-pre-screen.md. Every driver was compiled against its corresponding header. audit-screen.py reconstructs raw CSV rows, all141 effects, serial process windows, fixture/checksum identities, memory and frozen hashes. The two trailing rows are preserved but do not form an effect.

Missing promotion gates: complete qualified primary/guard schedules, all masks and small/long/tie/zero workloads, iterator setup/range-delete costs, fresh independent confirmation, candidate profile validation and final adversarial review. One bounded matched scoped profile/codegen diagnosis is next; it cannot complete or repair this timing schedule. ARM replication is a separate architecture experiment on exact retained A/B patches. Root source8fab511e remains unchanged.
