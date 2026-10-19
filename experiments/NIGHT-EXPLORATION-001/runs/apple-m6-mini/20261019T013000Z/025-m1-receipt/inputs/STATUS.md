# Apple M1 night exploration — status during round 3

Round 3 optional DECODE-001 is [complete](005-decode/RESULT.md): three
sequential isolated count-one policies pass release/sanitizer self-tests and
1,040 focused cells. Four phases ran 6,720 serial processes / 866,880 sample
rows; the independent raw archive audit passes. All 70 same-binary A/A cells
miss the 10 ms window gate, while each candidate has large repeated guard
losses despite scoped width-60 count-one gains. Decision PARK, source NONE,
no fresh confirmation or public iterator integration. Existing EXP-008
whole-process samples and current release assembly support only a narrow
mechanism lead; fresh macOS sampling was denied. M6 remains UNKNOWN after
DNS failures through 01:39:28 UTC. Totals: **0 accepted / 3 rejected /
6 parked across 9 optimization populations**. Launch tree source unchanged.

The first-pass queue is closed early under the [blocked note](BLOCKED.md)
and [early final report](MORNING-REPORT.md), written before the round cutoff.

The first eight-hour queue is exhausted. No eligible contender remains for
confirmation. Git commit provenance is pending the recorded index-lock denial;
do not retry that denied write in this worker. Next action, if work resumes:
read a newly published M6 decision and exact patch/harness hashes, then use
the bounded extension only for a new profile-supported contender or a
separately frozen precision referee. Do not rerun the failed DECODE-001
schedule. Campaign deadline is still the injected 20:00 UTC.

## Prior round 2 status

Started 2026-10-19 00:50:42 UTC; campaign deadline 2026-10-19 20:00:00 UTC. Round 2 ends 01:42:43 UTC. Actual host: Apple M1 MacBook Air, eight cores (four performance/four efficiency), macOS 26.3, Apple Clang 17. Launch HEAD `77d32df82cd5da02b95c6afb6193fcf83f67223f`; full sanitized host/toolchain and source/referee hashes: `HOST-MANIFEST.json`.

| Target | Status | Evidence / next action |
|---|---|---|
| Five-size baseline | COMPLETE | `001-baseline/matrix/`: native/sanitizer checks pass, 120 serial processes, 960 rows, 40 cells, 388.7s timing; 39/40 cells fail strict A/A |
| Rank | REJECT bounded shorter-side trial; source NONE | `002-rank/RESULT.md`: three sequential isolated implementations pass native/sanitizer and targeted oracles; 144 serial discovery processes; no consistent dual-primary gain; strict A/A remains failed |
| Update paths | COMPLETE diagnostic; candidate NONE; A/A PARK | 003-update/RESULT.md: five named paths, 75-process baseline inventory, untimed path census, six scoped profiles and failed 48-process primary A/A |
| Single lookup | COMPLETE diagnostic; chair NONE | 004-lookup/RESULT.md: independent-query release/sanitizer referee, two scoped profile captures, untimed tag/member counts; no new hypothesis beyond EXP-006 |
| Decoder or iterator | DECODE-001 diagnostic selected; candidate NOT STARTED | 005-decode/SELECTION.md: prior EXP-007/008 count-one lead; targeted current profile and fresh plan required; ITERATE-001 skipped for this optional slot |

UPDATE-001 diagnostic finished about 2026-10-19 01:25 UTC. Independent
construction/query permutations, release smoke and sanitizer smoke pass.
Untimed path counts show 1,517/20,000 preserve updates reinsert at 100K and
11,058/20,000 at 1M; all are exact pack failures in a separate reason pass.
The 75-process five-size/five-pattern inventory and six public profiles are
retained. New-referee position-preserving A/A fails both primary cells:
100K block effects −7.11%..+0.47%, 1M −10.49%..+5.45%, despite minimum
windows 45.009/52.895 ms. No update candidate or population; source remains
NONE. M6 check at 01:23:28 UTC again failed DNS, outcome UNKNOWN. Next queue
target advanced to LOOKUP-001 independent-query profile.

LOOKUP-001 then validated an independent-query referee through 1M in release
and ASan/UBSan. Longer public hit profiles captured 251/439, 189/344 and
160/233 PCs in platform memchr at 10K/100K/1M; source-instrumented counts
show 1.14–1.16 full comparisons per hit. Three proposal passes were
sequential, and the chair selected NONE because the supported inline scan
was already explored by EXP-006 with single-lane concerns. No lookup
candidate, comparison or new population. The optional slot is assigned
to DECODE-001 for a targeted count-one profile, not yet an implementation.
See 004-lookup/RESULT.md and 005-decode/SELECTION.md. Round 2 raw-data
audit is ROUND-002-AUDIT.json. Source and frozen rank referee hashes remain
unchanged. Optimization totals: 0 accepted / 3 rejected / 5 parked across
8 populations.

The only tree source is the unchanged baseline. Rank A/A maxima 1.32%/37.66%/6.71% at 10K/100K/1M fail ±1%; no candidate gain or adoption claim exists. Public in-process sampling captures the accumulation range at both primary sizes, while release assembly already vectorizes the sum. The shorter-side census predicts 14.933/19.842 fewer child-count visits at 100K/1M, not a measured speedup. Profile ratios are coarse diagnostic counts, not exact time fractions.

Round 2 rank discovery finished 2026-10-19 01:16 UTC: three isolated snapshots from launch commit, three retained patches, all native/sanitizer and targeted oracle checks pass. Same-referee six-block ABBA discovery at both primary sizes completed 144 serial processes in 88.94 seconds. The 100K/1M block effects span A −2.44%..+9.38% / −8.60%..+0.57%; B −12.92%..+13.17% / −8.55%..+13.32%; C −7.64%..+15.35% / −4.76%..+9.96%. No dual-primary winner or shortlist. Root source stays unchanged. Implementations were sequential by one worker, not independent agents. Exact backend variant and measured token cost remain unavailable. See `002-rank/RESULT.md` and raw manifest.

M6 publication checks at 2026-10-19 01:13:02 and 01:15:22 UTC: `git ls-remote --heads origin 'refs/heads/exploration/apple-m6-mini-*' refs/heads/main` failed to resolve `github.com`. Branch, commit, decision and patch outcome: **UNKNOWN**. No matching published discard observed; no M6 performance data used. Current local host branch HEAD `c53b1d91ab8103f7e923791f5380c434db5da0c7` was published externally after round 1; launch tree blob hash is unchanged. Git writes are not retried in this round following the recorded index-lock denial.

M6 publication check during round 1, approximately 2026-10-19 01:04 UTC: `git ls-remote --heads origin 'refs/heads/exploration/apple-m6-mini-*' refs/heads/main` failed because `github.com` could not be resolved. Branch, commit and outcome: UNKNOWN. Recheck before implementation/timing; no M6 results were adopted. No matching M6 veto has been observed.

Git write attempt once: `git add scripts/run-size-matrix.py` failed because `.git/worktrees/.../index.lock` could not be created (Operation not permitted). Do not retry this round. The metadata-only runner patch and SHA256 are in `001-baseline/`; commit-based provenance and host-branch push remain pending. No push was attempted. No children remain.
