# EXP-008 population step 2 — implementation selection

Three independent variants implemented the chair's short-range scalar fallback at
cutoffs 4 (A), 8 (B), and 16 (C). All use the same frozen EXP-007 B bulk helper above
their cutoff and share one referee, output buffer, materialization barrier, and checksum.
They built in detached worktrees and passed native plus ASan/UBSan decoder suites.

| Variant | Correctness | Primary: width60 forward, count16 | Secondary: width60 forward, count96 | A/A gate | Decision |
|---|---|---:|---:|---|---|
| A, cutoff 4 | pass | -0.58% | +0.32% | failed ±1% all-block precision | PARK |
| B, cutoff 8 | pass | -0.87% | +0.32% | failed ±1% all-block precision | PARK |
| C, cutoff 16 | pass | +38.06% | +0.38% | failed ±1% all-block precision | PARK |

The fixed minimum primary gain was 2% at both count16 and count96. No variant meets
those gates; count16 A/A itself ranges -0.69% to +2.79%. The full matrix also leaves
134/160 A/A cells unresolved. Per-cell data and the raw-derived selection inputs are
in `discovery/SUMMARY.md` and `discovery/selection-input.json`.

Count1 at width60 shows a local improvement of -8.79% for A and -8.48% for B, while
scalar count4 or higher regresses substantially under the wider cutoffs. This suggests
a count1-only experiment, but the variants' code layout differs and count16 A/A failed.
This signal does not qualify as a selected implementation. No candidate is shortlisted;
under the preregistered plan, fresh confirmation is skipped. Preserve all three patches.

All profile samples include setup and warmup. The generated assembly verifies call
placement and threshold selection; neither it nor `/usr/bin/sample` attributes timed-only
cycles. Machine replication must keep separate raw data and A/A qualification.
