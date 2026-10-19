# RANK-001 bounded exploratory result — Apple M1

Decision: **REJECT the three shorter-side implementations for this scheduled trial; source NONE.** No variant showed a consistent improvement on both preregistered primary cells. This is an exploratory rejection, not a proof that all shorter-side algorithms are slower. Rank adoption remains blocked by the earlier failed strict A/A controls.

## Provenance and validation

- Launch source commit: `77d32df82cd5da02b95c6afb6193fcf83f67223f`; host branch later advanced to `c53b1d91ab8103f7e923791f5380c434db5da0c7` to publish round 1, with identical tree blob.
- Base tree SHA256 `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`; frozen `bench/microbench.c` SHA256 `b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde`.
- Four isolated `git archive` snapshots in ignored scratch, built using Apple Clang 17, C11, `-O3` native and `-O1 -fsanitize=address,undefined` for validation; no root `src/` edit. All `make all check` and `make sanitize` calls pass. Base/A/B/C also pass independent sorted-vector boundary and exact signed-zero physical rank oracles. Logs and commands: `variants/validation.json`, `variants/semantic.json`.
- Three implementation passes were sequential by one GPT-6 worker, not independent agents. Exact backend variant and measured token cost are unavailable. Patches A/B/C are retained in `variants/`. All use the same subtree identity and change only `zbtScoreRank`.
- Generated `zbtreeRank` assembly is retained for all four binaries. Base/A/B/C function disassembly lengths are 450/498/496/506 lines; Clang emits `add.2d` in every build. These static counts are not runtime cost estimates. `variants/codegen.json` records binary hashes.
- CPU Performance Engineering MCP consulted. Its returned sources do not establish an Apple M1 B+ tree gain; no external machine numbers were adopted.

## Frozen discovery screen

Public successful rank at 100K/1M, 16-byte binary members, operation counts 305,781/118,521, seeds 1/2/3 repeated in six ABBA blocks per variant. One process at a time, size and variant order rotated; no build, test or profile overlapped timing. 144 process CSVs, 88.94 seconds. All matching baseline/candidate checksums and tree-owned bytes agree within each four-process cell. `discovery/manifest.json` retains every command, timestamp, raw CSV path/hash and per-run timing; `discovery/analysis.json` reconstructs block effects. Negative effects are faster.

| Variant | 100K block effects | 1M block effects | Bounded decision |
|---|---|---|---|
| A | +9.38%, +8.55%, -2.07%, +2.95%, +1.94%, -2.44% | -4.08%, +0.57%, -1.61%, -8.60%, -1.62%, -1.64% | REJECT |
| B | +4.61%, -12.92%, -1.25%, +13.17%, +9.65%, +0.60% | +13.32%, -2.46%, +2.44%, -6.89%, -8.55%, -1.92% | REJECT |
| C | +11.95%, +15.35%, -7.64%, -0.24%, +1.32%, +3.40% | -1.12%, -4.76%, +5.76%, +9.96%, +0.13%, +1.36% | REJECT |

The earlier same-binary rank A/A maxima were 37.66% at 100K and 6.71% at 1M, both outside ±1%. The 100K candidate effects vary in sign and reach double digits; no variant has all six blocks at or below −2% on either paired primary. There is no candidate shortlist, fresh confirmation, candidate profile, full guard matrix, or adoption. Source and referee remain baseline.

M6 check at 2026-10-19 01:13:02 UTC and 01:15:22 UTC: `git ls-remote --heads origin 'refs/heads/exploration/apple-m6-mini-*' refs/heads/main` failed because `github.com` could not be resolved. Branch/commit/outcome **UNKNOWN**; no M6 result was inferred or pooled.

Next: UPDATE-001 path decomposition and profile. Do not rerun this rank A/A schedule unchanged. A distinct measurement diagnosis would be needed before fine rank adoption can be reconsidered.
