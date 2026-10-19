# M6 RANK-001 — profile and calibrated referee

Current source selection NONE; candidate NOT BUILT. Public referee published in
`ca5cacfb`; source hashes in freeze.json and launcher manifest. Host Apple M6,
macOS27, Apple Clang21; metadata is launcher-recorded because worker sysctl was denied.

138 harness checks pass across native/ASan/UBSan; the oracle detects an injected
rank +1 error. Historical upstream checks already passed in baseline-attempt002.
bench/night-rank.c has independent construction/query permutations and sorted member/
score oracle, optional score output, reverse/miss modes, tie and finite layouts.

External sample attachment failed once; no sudo or permission changes. The public
SIGPROF diagnostic has48/42 calibration PCs, all in the known busy function. Rank
captures44/107/389 PCs at10K/100K/1M;13/35/98 fall in inspected accumulation offsets
1564..1752 of zbtreeRank. These are coarse code-location observations, not exact
runtime fractions, cadence or hardware counters. Release and profile assembly both
vectorize groups of8 child counts; explicit SIMD is not justified.

Private pre-resolved accumulation is a separate cache path, never a component time
obtained by subtraction. Its census has mean2/3/3 ancestors and13.376/27.823/37.418
preceding siblings. Public profile therefore supports examining reduced count visits,
subject to actual public timing and extra branch/metadata cost. No gain is measured.

Fixed operations after three baseline observations per size: `{'10000': 1788014, '100000': 807246, '1000000': 240090}`.
Three measured batches/process; six ABBA process blocks with seeds1/2/3 repeated.
Qualification not yet run. See CALIBRATION-LIMITATION.md for summary-calculation
overlap during count selection. Helper missing-include build failure is preserved in
validation/ and PROFILE-ERRATUM.json; only that calibration helper was fixed.

Reproduce serially from repo root with `python3 <this-directory>/run.py prepare`,
`profile`, `calibrate`, then `qualify` in a NEW output directory (driver constants
must be explicitly frozen for a new campaign). Analyse PCs with analyse-profile.py.
Commands are in commands.jsonl, full assembly and external raw sample logs in ignored
scratch/m6-rank; compact rank assembly, diagnostic PCs and checksums are committed.
CPU Performance Engineering MCP unavailable. No independent agents or review yet;
backend exact model and measured token costs unknown. Network refresh of M1/main
failed DNS once; cached published M1 revision remains the context only.

Updated 2026-10-19T01:43:06.281580+00:00. Next run fully serial A/A, then proposal/chair passes if still useful.

## A/A completed 2026-10-19T01:44:38.181856+00:00

72 serial processes /216 batches, 10.53s measured windows; raw
checksums, owned-memory equality and reconstruction pass. No cell qualifies.

| Size | Max absolute block effect | Minimum window ms | Strict gate |
|---:|---:|---:|---|
| 10000 | 8.840% | 46.677 | PARK |
| 100000 | 1.886% | 48.626 | PARK |
| 1000000 | 7.406% | 42.807 | PARK |

This is the single frozen A/A schedule; no block repeated or outlier removed.
A profile-supported exploratory screen may run once, beside these controls, but
no strict adoption or candidate ranking for small effects within noise is allowed.
