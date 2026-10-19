# Apple M1 night exploration — status after round 1

Started 2026-10-19 00:50:42 UTC; campaign deadline 2026-10-19 20:00:00 UTC. Round 1 ends 01:20:42 UTC. Actual host: Apple M1 MacBook Air, eight cores (four performance/four efficiency), macOS 26.3, Apple Clang 17. Launch HEAD `77d32df82cd5da02b95c6afb6193fcf83f67223f`; full sanitized host/toolchain and source/referee hashes: `HOST-MANIFEST.json`.

| Target | Status | Evidence / next action |
|---|---|---|
| Five-size baseline | COMPLETE | `001-baseline/matrix/`: native/sanitizer checks pass, 120 serial processes, 960 rows, 40 cells, 388.7s timing; 39/40 cells fail strict A/A |
| Rank | PARK for adoption; exploratory hypothesis CHOSEN | `002-rank/`: public profile, private census, 72-row rank A/A, three sequential proposals and chair; next three isolated implementation variants under `DISCOVERY-PLAN.md` |
| Update paths | NOT STARTED | Advance after bounded rank screen or if M6 vetoes it |
| Single lookup | NOT STARTED | Proposal B retained for its scheduled target |
| Decoder or iterator | NOT STARTED | Choose later from profile |

The only tree source is the unchanged baseline. Rank A/A maxima 1.32%/37.66%/6.71% at 10K/100K/1M fail ±1%; no candidate gain or adoption claim exists. Public in-process sampling captures the accumulation range at both primary sizes, while release assembly already vectorizes the sum. The shorter-side census predicts 14.933/19.842 fewer child-count visits at 100K/1M, not a measured speedup. Profile ratios are coarse diagnostic counts, not exact time fractions.

M6 publication check during round 1, approximately 2026-10-19 01:04 UTC: `git ls-remote --heads origin 'refs/heads/exploration/apple-m6-mini-*' refs/heads/main` failed because `github.com` could not be resolved. Branch, commit and outcome: UNKNOWN. Recheck before implementation/timing; no M6 results were adopted. No matching M6 veto has been observed.

Git write attempt once: `git add scripts/run-size-matrix.py` failed because `.git/worktrees/.../index.lock` could not be created (Operation not permitted). Do not retry this round. The metadata-only runner patch and SHA256 are in `001-baseline/`; commit-based provenance and host-branch push remain pending. No push was attempted. No children remain.
