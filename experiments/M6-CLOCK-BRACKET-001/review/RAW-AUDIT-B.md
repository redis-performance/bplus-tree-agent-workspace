# Independent raw audit B

**Raw integrity/reconstruction PASS; campaign remains PARK.** The 100K wall controls pass 6/6 blocks and the 1M controls pass 2/6. This is baseline harness verification, not candidate confirmation, source acceptance or a physical clock qualification. Reviewer `/root/followup_proposal_b`; inherited Codex/GPT-6 family, exact backend variant/token/currency costs unknown. No native execution, retry, profile, build, external runner or new peer postreview was used.

All 48 CSV observations and 12 ABBA blocks were independently reconstructed from the raw stdout files before comparing derived values with the campaign summary. The exact gate is `abs(Bsum-Asum)*100 <= Asum`, with A positions 0/3, B positions 1/2, equal actual counts, and every wall window at least 10 ms. Percentages below are display values only. Negative means less recorded elapsed time for the B-labelled executions of the same binary.

| Block | Seed | 100K wall | Gate | 1M wall | Gate | 1M thread diagnostic |
|---|---|---:|---|---:|---|---:|
| 1 | 1 | +0.091572784% | PASS | +3.418338086% | FAIL | +3.395634280% |
| 2 | 2 | +0.062479980% | PASS | +1.014037726% | FAIL | +0.987702760% |
| 3 | 3 | -0.025045106% | PASS | -0.891521919% | PASS | -0.876172947% |
| 4 | 1 | -0.374418176% | PASS | -1.573060730% | FAIL | -1.482851843% |
| 5 | 2 | -0.170972283% | PASS | -0.664938219% | PASS | -0.645551997% |
| 6 | 3 | -0.801226674% | PASS | +1.253821892% | FAIL | +1.238471342% |

The fixed counts remain 13,834,448 and 4,978,427; sizes alternate order each block and seeds 1/2/3 repeat once. All 48 rows remain present. Raw windows span **594,536,000–650,797,000 ns**; recorded boundary margins span **0–4,000 ns**. The AA phase completed in 43.77916025 seconds. The one barely passing 1M thread contrast changes no wall gate and supplies no causal explanation.

The 72 raw control rows comprise 24 exact empty/CPU/block triplets. Independent affine-transform exponentiation reproduces the 2M-LCG checksum **3,294,929,107,973,101,697**. All rows pass the protocol's structural checks; every block control meets same-clock sleep ≥20 ms and recorded residual ≥18 ms. Empty repetitions 1, 12 and 13 have inner-wall values 0 ns, thread values 292/250/375 ns and margins 0 ns: their conditional zero-error intervals are empty. These are retained **INCONCLUSIVE** model observations under preregistered v2, not omitted rows or clock-error calibration. Physical accuracy/accounting lag remains **UNVALIDATED**.

The intended query permutation and aggregate checksum were independently rebuilt from the C SplitMix64/Fisher–Yates rules for all six size/seed fixtures. All SHA-256 little-endian-u64 permutation digests and raw checksums match. The fixture digest is reconstructed metadata: the CSV is not a trace of every native query. Operations, output modes, members, seeds and one warmup pass match every command/row. Tree-owned memory is identical within each ABBA and across the repeated same-seed blocks; seed-dependent tree geometry is preserved rather than pooled as one fingerprint. The build's 36 new/old native/sanitizer smoke pairs match their raw semantic and memory fields, and both original43 outputs explicitly report 43 passed/0 failed. The eight compilation commands use their frozen native/sanitizer options; no assertion disabling or LTO was introduced.

All **134 journal commands** (85 build, 1 controls, 48 AA) join to exactly **170+2+96 retained streams** by path, SHA-256 and byte count. Every stderr is empty. Command names/coverage and full AA argv match the fixed protocol. Recorded UTC intervals are serial, each command has rc0 and records reaped direct child, empty owned process group and safe release. All commands/final statuses fall inside their per-phase and absolute 15:41:10.756095 UTC bounds. The later release metadata pins the exact controls/AA statuses, records no queued target work, and the owned lock is absent. This verifies supervision records and metadata continuity; it cannot independently recreate historical OS process state.

All sealed identities match before and after this audit:

| Manifest | Pins |
|---|---:|
| Immutable inputs | 80 |
| Build manifest | 285 |
| Build evidence | 173 |
| Controls evidence | 4 |
| AA evidence | 98 |

These are **640 overlapping pins over 388 distinct paths**, not 640 different files. Current source/header, corrected compatibility files and all eight produced native/sanitizer binaries match their frozen identities. The JSON retains explicit source/binary hashes, all 48 observations, all control rows, integer block sums, chronological command intervals and manifest hashes. Original failures remain visible; source selection remains NONE.

Own availability check exposed no callable CPU-performance MCP tools. This audit explicitly consumed the **shared root stdio results consultation**, not a B-owned ask: `scratch/cpu-perf-m6-bracket-20261019/results/results-calls.jsonl`, SHA-256 `06e7199e4f35b77b244f30e48e1aacd29ed545bc4f2e72ab78642ce71a65ddb5`. Its 2/287-source, 93-passage keyword-only service misclassified these CSV rows as `perf stat -x` and read QoS text as 0% counter multiplexing. **No such counters were collected.** Those parser-generated multiplexing/top-down assertions are excluded; no resulting hardware recommendation or causal attribution is adopted.

Reproduce offline from the worktree root: `python3 experiments/M6-CLOCK-BRACKET-001/review/raw-audit-b.py`. It reads retained files, independently reconstructs fixtures and checks results; it imports no campaign driver and launches no native child. This review does not loosen the gate, retry a row or convert thread diagnostics into a noise correction.
