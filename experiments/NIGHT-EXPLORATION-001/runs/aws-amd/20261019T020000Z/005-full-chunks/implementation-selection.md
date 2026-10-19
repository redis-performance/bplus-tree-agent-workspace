# FULL-CHUNKS-001 implementation selection

Decision: **REJECT / NONE**. No measured block reaches the required 2% elapsed improvement; all three variants fail both primary gates. No independent confirmation or performance-guard timing warranted. Source baseline stays unchanged.

| Variant | 100K median elapsed change | 1M median elapsed change |
|---|---:|---:|
| A | -0.609% | +0.380% |
| B | +0.265% | +0.403% |
| C | -0.824% | +0.854% |

Positive means slower. Fixed screen completed02:50:13 UTC:144 serial processes,36 ABBA effects, six blocks per variant and size, seeds1/2/3 twice, exactly1M updates per process,16-byte members, leased AMD Zen5 CPU2. All returncodes, checksum equality, owned-byte equality, and before/after binary hashes pass. Fresh A/A qualified both cells, maxabs0.557%/0.386%; minimum windows491ms/1.111s. No extra post-result timing.

All59 validation commands passed original43tests plus frozen score-boundary, packed-decode, packed-move oracles across four snapshots and native/sanitizer. Packed-move146250 exact whole-buffer reference operations percell. Root [independent static review](independent-pre-screen-review.md) found no blocker. [Guards](GUARDS.md) were frozen before screen but remain unrun because all primaries failed; new tied-score performance referee is unimplemented.

Mechanism evidence: full64 chunks constituted76.14%/76.13% of matched update packed-move chunks, baseline retained dynamic width dispatch, variants specialize bulk64 loops. Code size grew from80479 to81615/82383/81615; A/C are distinct generated code but closely related transformations. Instruction opportunity did not produce useful elapsed gain. No causal attribution to code size or cache effects without further measurements. No candidate profile needed for rejection.

Three sequential proposal passes/chair and three isolated implementation passes, same native agent, not independent agents. Exact inherited backend/model and measured token/USD cost unavailable. All patches/raw files retained. AMD totals:3 completed populations,0 accepted,3 rejected,0 parked. No overnight adoption.

Publication note: fail-closed scanner prevented private path prefixes from reaching Git in validation logs; sanitized evidence commit lagged screen start, while exact patches, validation, and independent review existed before timing. Detailed activity record retained.

Decision UTC: 2026-10-19T02:51:26.101130+00:00.
