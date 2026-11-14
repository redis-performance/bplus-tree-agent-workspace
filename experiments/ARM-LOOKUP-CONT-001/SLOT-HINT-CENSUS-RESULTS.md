# Slot-hint census results

**All twelve fixed runs passed; selected source remains NONE.** This is a baseline shadow diagnostic, with no candidate fast path, timing, performance qualification or source adoption. Native and LTO outputs agree byte for byte for all six cases. Each ELF processed 3,500 counted queries, for 7,000 total; duplicate collector output files are aliases, not additional runs.

| Case | Useful queries per ELF | Original leaf-call events per ELF |
|---|---:|---:|
| Membership hit | 124 / 500 | 502 |
| Score | 124 / 500 | 502 |
| Miss | 0 / 500 | 9 |
| Long member | 118 / 500 | 503 |
| External member | 126 / 500 | 501 |
| Update | 248 / 1,000 | 1,004 |

“Useful” means that the complete shadow predicate and the original leaf search both succeed. Every original lookup and branch still executes. These fractions do not predict saved cycles or net speed. Update visits the same 124 useful member positions twice.

The folded filter adds two shadow positives among 500 miss queries, at query IDs456 and480: eleven original positives,487 negatives under both mappings, and two original negatives becoming folded positives. Original branch decisions remain authoritative, so the diagnostic executes no additional displaced probe for those two observations. It does not measure the cost of a real folded-filter implementation.

All initial hints come from CopyLeaf. There are no stale, out-of-range or wrong-tag hint observations, no Rebuild seeding, and no counted ID writes, invalidations, seed attempts or seeds. Warmup, validation and cleanup mutation totals are also zero. There is no counted active resize, duplication, defrag/rebind, reference-maintenance or direct-scan consumer coverage. The update case therefore establishes stable-hint exposure only. Maximum observed leaf ID is33, so large-ID boundaries remain untested.

The original output models and final assertions pass. Tree-owned bytes match the fixed baseline endpoints, and the completion fence follows all original frees with no live shadow registry or context. Shadow memory lies outside tree ownership: this is not a candidate memory-overhead guard or a general allocator leak detector.

The frozen source manifest is `f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b`. Reviewed native ELF: `8facf50e3c68a07ecc738aed446a0f0f9290e85e5d69c26e82d727e98031687c`; LTO ELF: `0a9c7f0dca40d181bd8770dcd0c46c7eb9030ca584749dfc2e0db6514cedaf39`. The source was published before fleet execution. Every command used pre/post isolation checks, the fixed06:45UTC execution ceiling and one-shot claims. All14 census/checker commands returned zero. Final fetch observed an inactive work unit with no owned workload; that observation is not fleet-release proof.

See the [semantic review](reviews/SLOT-HINT-CENSUS-FINAL.md), [operational review](reviews/SLOT-CENSUS-FINAL-OPERATIONS.md), [target-code review](reviews/SLOT-HINT-CENSUS-TARGET-CODE.md), [raw output and dual-hash manifest](slot-hint-census-results/manifest.json), and [root checker result](slot-hint-census-results/root-output-check.json). ELFs and operational identities remain privately retained; the manifest inventories withheld artifacts and maps published text to original hashes.

Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring, including all children, are unavailable for this diagnostic. No speed estimate or bottleneck attribution follows from these counts. H2 and Q4 remain PARK, ARM remains released, and the completed performance ledger remains47/25PARK/22REJECT/0approved.

A separately frozen baseline lifecycle correctness check is being prepared to address the observed coverage gap. It has no candidate and cannot admit timing or adoption. Its fixed source, review and completion cutoffs are06:15,06:30 and06:45UTC respectively; missing a cutoff closes it incomplete.
