# Independent adversarial review — preliminary

Reviewer: separate Codex reviewer session, not a proposer or implementer. Exact model/token/currency costs are unknown. Reviewed source, saved assembly, scripts and raw evidence only; no fleet access, builds or measurements. Review completed 2026-11-13 before candidate selection.

**No semantic blocker found in A/B/C. Acceptance remains pending candidate comparisons, fresh confirmation, matched profiles, current-upstream recheck and required portability validation.** One factual coverage claim needs correction before the report can be trusted.

## Finding: 256-byte members are not external

The pinned source defines `ZBT_EXTERNAL_MEMBER_AT` as320 (`current/src/zset_btree.c:178`). The `long` fixture and the long case in `output_oracle.c` use256 bytes. They exercise the inline16-bit-length representation, not an external allocation. PROTOCOL.md's parenthetical “external storage” is incorrect, and the90,000-case optional-output oracle cannot be cited as direct external-representation coverage.

This does not invalidate the registered longer-member timing guard and does not justify replacing or extending its frozen timing rows. Correct the description and preserve the cohort. If the report claims explicit external optional-output coverage, add separate correctness-only cases at/above320 bytes and retain the original oracle and logs; do not change the timed referee. Existing upstream tests provide broader semantic coverage but are not a substitute for accurately describing this oracle.

## Audited passes

- Independently compared all five extracted C/header/vendor files to Git blobs at unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`; bytes and manifest SHA256s match. This checks the recorded pin, not whether upstream has advanced after its fetch. Final fresh upstream verification remains required.
- Checked pinned `t_zset.c`: a two-input cardinality-only intersection disables hash reuse and requests no score. Single-pair short-member insertion converts at the129th member, reserves129 and imports the first128 using the modeled raw APIs. The standalone fixture keeps construction/iteration outside timing and queries bytes from a separately allocated source tree. The different allocator, fixed hash seed, small repeated hot working set and absence of Redis/integration work remain explicit limits.
- Reconstructed48 rows and12 ABBA controls directly, with A slots0/3 and B slots1/2. All hashes/checksums, operation counts, minimum windows and ±1% differences satisfy the declared baseline gate. Independent values are in preliminary-audit.json. No candidate conclusion follows from this baseline alone.
- Inspected each retained patch. A guards the unchanged conversion/output block; B returns only after complete member equality when neither output is requested; C computes the mapping only for requested outputs. The mapping helper reads count/reverse state and has no side effect. All probes, tag scans, packed decoding, external-hash filtering, byte comparison and mutation/index behavior remain unchanged. No new alignment, integer-width or ISA assumption appears.
- The optional-output oracle checks both orientations, all four output masks, score bits (including signed zero), exact logical positions and untouched outputs on misses. Its reference captures pre-reversal leaf state, so it is focused on output semantics; independent insertion/score semantics remain covered by the retained upstream tests. Oracle seeds are17,30,43; frozen timing/fixture qualification seeds are17,29,43. These are distinct, not missing runs.
- The retained correctness logs report57/57 native and57/57 sanitizer tests per candidate, plus12 native and12 sanitizer fixture cells; frozen referee manifests match. The captured ARM release fixture checks are an additional target-compiler check. No candidate timing result was available at this preliminary stage.
- Flat sample shares use the complete perf user-cycle sample denominator, with zero reported lost samples. Unknown libc PCs stay unresolved. perf-stat counts explicitly include process setup/warmup/teardown; they are not exact timed-loop counts. Actual perf is6.17.13 despite its kernel-tools directory name.

## TMA and consultation

Own discovery of exposed cpu-perf/library_status tools returned none. Under docs/PERFORMANCE-MCP.md's worker provision, this review consumes root's **shared** controller-local stdio consultation, library_status and actual ask/reconsultation records in CONSULTATION.md. Those calls are root's, not this reviewer's. The available passages do not establish the proposed CPU mechanism. The review instead tests the source/assembly and raw evidence.

| Category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Actual topdown-profiler0.2.3 capture uses CPU-wide `-a -C2`; sibling list2 shows no SMT, but continuous exclusion/occupancy evidence is absent. The report correctly keeps this funnel exploratory and all process-qualified categories unavailable. The raw L1 values sum to approximately100% with rounding; no children are collected. Neither those values nor flat samples establish the cost of the specific deferred instructions.

## Remaining acceptance checks

Reconstruct all candidate rows without choosing the nicest subset; enforce the registered primary/guard rules and retain equivalent binaries as equivalent implementations. Require matched codegen/counters to show the avoided work, fresh seeds29/43 for any selected contender, Intel qualification for any portability/acceptance claim, and a fresh upstream pin/equivalence check before final validation. Preserve all losing patches and failed/unexecuted gates. A passing standalone result still cannot claim the original command-level ARM gap is closed.
