# Independent raw capture audit

PASS: all 16 fixed cells and 32 raw streams validate. This audit reads retained files only; it executes no native binary, build, sampler or capture. The independent script imports no capture/classifier code. Full identities, semantic values and per-cell symbol locations are in [INDEPENDENT-CAPTURE-AUDIT.json](INDEPENDENT-CAPTURE-AUDIT.json).

The schedule is reconstructed as four contracts (hit, miss, rank, scan), then 100K/1M, then seeds 1/2. Original 019 indices 00–02 occur exactly once; continuation indices 03–15 occur exactly once. Every command uses the same frozen binary, 10,000,000 requested operations, 16-byte members, three warmup passes and the explicit 1,000-microsecond sampler override. The published release ACK records commit `bdca132a7420f4334e3af96afafafc646cad2d9f` and exact final driver/PLAN/freeze hashes. All arguments, fixture identities, CSV integer semantics, owned bytes and uncapped headers match.

All 53 original freeze entries and all 86 continuation freeze entries match; 98 distinct inputs/state artifacts remain unchanged before/after the audit, including every existing 019 file. The enabled binary remains `7c088393dcd381154869327e626d06e4bd73c42a93ed888663e796b1e8cfefb8`. The baseline tree, header and corrected adapter identities are retained in the frozen input tables. No source or original evidence was edited.

PC classification was reconstructed from the actual immutable Mach-O load-command bytes (nine sections) and retained `nm` T/t entries (103 distinct text-address groups, including three coalesced alias groups). It independently matches every summary bin, including aliases, relative image offsets, section labels, mapping limits and sample counts. ASLR is normalized using each raw sample’s own image base; runtime addresses are not published. Text is restricted to aligned addresses in relative [1,512, 74,408); stubs occupy [74,408, 74,828). PCs outside text cannot inherit a nearest cold symbol. All 10 actual stub samples retain unknown imported targets and mapping limits. There are no actual unmapped own-image samples or ambiguous coalesced-alias samples.

The 2,469 retained PCs comprise 1,422 text samples, 1,037 external-symbol samples and 10 import-stub samples. Every cell is uncapped and meets the minimum, with 19–429 samples. No samples are dropped.

| Contract | Members | Seed | PCs | Text | External | Stub |
|---|---:|---:|---:|---:|---:|---:|
| lookup-hit | 100000 | 1 | 84 | 27 | 57 | 0 |
| lookup-hit | 100000 | 2 | 97 | 41 | 56 | 0 |
| lookup-hit | 1000000 | 1 | 274 | 100 | 171 | 3 |
| lookup-hit | 1000000 | 2 | 296 | 127 | 166 | 3 |
| lookup-miss | 100000 | 1 | 27 | 26 | 1 | 0 |
| lookup-miss | 100000 | 2 | 19 | 18 | 1 | 0 |
| lookup-miss | 1000000 | 1 | 78 | 76 | 2 | 0 |
| lookup-miss | 1000000 | 2 | 98 | 93 | 5 | 0 |
| rank | 100000 | 1 | 129 | 74 | 53 | 2 |
| rank | 100000 | 2 | 128 | 73 | 55 | 0 |
| rank | 1000000 | 1 | 429 | 177 | 252 | 0 |
| rank | 1000000 | 2 | 393 | 173 | 218 | 2 |
| scan | 100000 | 1 | 105 | 105 | 0 | 0 |
| scan | 100000 | 2 | 97 | 97 | 0 | 0 |
| scan | 1000000 | 1 | 112 | 112 | 0 | 0 |
| scan | 1000000 | 2 | 103 | 103 | 0 | 0 |

Coarse locations across the retained samples include member comparison/search (`_platform_memchr` 932, `_platform_memcmp` 105, `_zbtScoreLeafFindMember` 228), hash computation (`_siphash` 175), score lookup (`_zbtreeScoreRaw` 165, `_zbtreeScore` 56), rank (`_zbtreeRank` 368), and scan (`_zbtIndexScanSlot` 367, `_zbtIndexScanGroup` 26). The remaining samples are `_main` 24, `_dictGenHashFunction` 6, `_scan_count` 5, `_zbtreeScan` 2, and 10 unknown-target stubs. These are sampled locations, not instruction costs, cycles, unbiased frequency/time shares, cache evidence or speed measurements. Counts across different operation contracts are descriptive inventory only.

Scan duplicates retain original semantics: entries beyond one copy per member per traversal are 2,515/2,706 at 100K seeds 1/2 and 1,813/1,840 at 1M. Actual operations total 160,558,630 across all cells versus 160,000,000 requested. The frozen internal post-bracket oracle checks exact member bytes, score, coverage, duplicate count and checksum; every native capture exits zero with assertions enabled. The audit checks aggregate scan divisibility/checksums and those preserved assertion mechanisms. Aggregate raw rows alone cannot independently reconstruct which members were duplicated. No new correctness execution is claimed. Tree-owned bytes are identical across contracts for each fixture: 2,984,176/2,979,056 at 100K and 32,936,048/32,915,824 at 1M, seeds 1/2.

All 16 child intervals are serial; every journal reports exit zero, child reaped, owned group empty, no timeout and safe release. Original captures run from 05:41:29.830994 to 05:41:33.098814 UTC; continuation captures run from 05:57:04.804949 to 05:57:20.220233 UTC. The declared repair pause is **931.704861 seconds (15 minutes 31.704861 seconds)**, separate from the two actual phases. Continuation phase wall is 15.419949 seconds; prior phase wall is 3.269144 seconds; combined phase wall is 18.689094 seconds. The 480-second continuation and 07:15 UTC bounds pass. The driver’s post-continuation 86-identity gate is recorded complete, and the independent audit rechecks those identities.

The original 019 remains INCOMPLETE, preserving its three raw captures and two original derived rows. Logical 16-cell completeness comes from the separately reviewed 020 continuation and offline rederivation. No cross-pause continuity is implied. Native timing and rate columns remain unused. No tree proposal, implementation or acceptance follows from this audit.

Command: `PYTHONDONTWRITEBYTECODE=1 python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/020-member-index-profile-continuation/independent-capture-audit.py`. The script enforces a 180-second offline alarm. Its exact stdout/stderr are retained alongside it; final exit code is zero. The seal excludes itself and hashes the audit script, report and command logs. Participant `/root/followup_proposal_a`; inherited Codex/GPT-6 family, exact serving model/token/currency costs unknown. All work is finished and no child remains active.
