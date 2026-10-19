# Independent ARM iterator comparison raw audit

**REJECT / source NONE. Integrity PASS.** All nine listed guards qualified under the immutable earlier A/A and regress by more than 1% in every one of six ABBA blocks. This rejects the fresh corrected-source ARM replication of exact historical EXP005A; it does not change the historical EXP005 population decision, add a population, or adopt any source.

Reviewed immutable ARM `f30ac4330ddb3ef6fcdddb20ade8e4a8cdb259ac` against A/A `8ed45423c386d3e1b24d366a84b6d96951c5d8da` and contract `380ef3109`. Independent auditor is unchanged from `b67dc2d89`, SHA256 `fbf4dd72de1e6f13593d20a6f674d9e9f1e533d4a869aeeb9f9fe6deb3a9d355`.

Reconstructed all 1,968 comparison processes/rows, 492 ABBA blocks and 82 required cells, plus the entire 1,968-row/492-block A/A. Among 43 qualified cells: **30 PASS, nine REJECT, four mixed PARK**. All 39 unqualified cells remain unresolved. Qualified mixed cells are g010, g018, g025 and g074. No averaging across guards or favorable primary result can override these required guard failures.

| Cell | Size | Encoding | Direction | Mask | Median effect | Block range |
|---|---:|---|---|---:|---:|---:|
| g004 | 100000 | integer | forward | 4 | +2.864594% | +2.572515% to +2.997482% |
| g012 | 100000 | integer | reverse | 4 | +8.414612% | +8.270516% to +8.510297% |
| g020 | 1000000 | integer | forward | 4 | +2.953312% | +2.712211% to +3.104075% |
| g028 | 1000000 | integer | reverse | 4 | +3.147384% | +2.964153% to +3.522909% |
| g033 | 100000 | fraction | forward | 4 | +2.872471% | +2.754759% to +2.986926% |
| g037 | 100000 | fraction | reverse | 4 | +8.518772% | +8.485382% to +8.635443% |
| g041 | 100000 | wide | forward | 4 | +2.860358% | +2.651173% to +3.083338% |
| g049 | 100000 | zero | forward | 4 | +2.898071% | +2.711171% to +3.004868% |
| g053 | 100000 | zero | reverse | 4 | +8.395306% | +7.326691% to +8.490353% |

Effects are exact Decimal `100*((B1+B2)/(A1+A2)-1)`, reconstructed from raw integer nanoseconds; positive means candidate slower. Display rounding above does not determine classification. Every listed mask is 4, but no causal explanation of the slowdown is inferred from that association. The callback/referee differs from the public primary microbenchmark; a similar output request does not make timings interchangeable. Minimum comparison window is 44.696826 ms, above the frozen 10 ms floor.

Verified all 7,919 immutable inputs, including 3,944 comparison seal hashes and 3,938 comparison publication entries; independently regenerated all scheduled commands and checked source/referee/freeze/composite receipts, protected binaries, guard binaries and all 513 snapshot bindings. Actual source/text identities remain the fixed baseline and exact historical candidate. Every row matches its same-fixture A/A reference for output checksums, construction fingerprints, traversals/visits and tree-owned bytes; repeated-seed and within-ABBA identities also agree. CPU2 endpoints, serial timestamps, 60-second child caps, 1,500-second phase cap, sufficient deadline margin and before/after source identities pass. Comparison began `2026-10-19T09:47:58.664364+00:00` and finished `2026-10-19T10:00:41.434881+00:00`; reported monotonic duration 762.891762892 seconds. Retained post-phase evidence records no owned work; this audit did not query the runner live or establish OSS release.

The previous original-operation controls and mixed 100-member SCAN guard remain unresolved independently. Required iterator regressions now provide a decisive rejection. Matched profiling and independent held-out seeds1201–1203 confirmation must remain unexecuted under this plan; no retry, alternative candidate, coverage waiver, or launch grant follows this review. Root owns release verification.

Auditor provenance: actual participant `/root/aws_intel`, native agent tools; exact backend/model and token/currency costs unknown. I previously authored the confirmation protocol/static reviews and independently reviewed earlier raw stages. This is independent of the ARM producer and its audit implementation, not blind to earlier campaign discussion or independent of my own prior audit code. No producer code was imported/executed, and no benchmark, build, SSH or remote workload ran for this review. Public normalized evidence bytes are rehashed; unavailable original private raw bytes are not claimed rehashed. Construction fingerprints are range/equality checked, not regenerated from RNG state; unchanged assertion-checked referees retain semantic-oracle responsibility.

Reproduce locally from this branch using `../audit.py --revision f30ac4330ddb3ef6fcdddb20ade8e4a8cdb259ac --phase iterator-comparison --aa-revision 8ed45423c386d3e1b24d366a84b6d96951c5d8da --output <new-output-directory>` from the repository root with the full auditor path. All exact cell effects are retained in [raw-audit.json](raw-audit.json), independently reconstructed controls in [aa-raw-audit.json](aa-raw-audit.json), and immutable hashes in [input-hashes.json](input-hashes.json).
