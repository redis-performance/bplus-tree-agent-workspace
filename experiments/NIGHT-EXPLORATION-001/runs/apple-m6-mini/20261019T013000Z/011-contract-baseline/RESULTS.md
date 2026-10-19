# Corrected-adapter M6 baseline — complete, precision remains limited

All 120 processes and 960 rows pass the independent audit. All seven native/sanitizer
validation stages pass. Five of 40 cells qualify; 35 exceed the noise limit, and
14 have windows below 10 ms. No failed schedule was repeated.

The measurement subprocess loop took 160.052971 seconds wall time, including setup,
warmup and verification. Operation timers sum to 71.958584 seconds. Full manifest
span including validation is 180.821794 seconds. The original runner records ordered
serial subprocess calls but no per-child UTC interval; the audit discloses that limit.

Tree C/header remain d9123c… /496e72…, and the corrected adapter matches the exact
reviewed two-line patch. Separate fix commit7f299a5f5 preceded launch. Existing
source, hashing, allocation and assertion checks remain intact. The baseline binary
hash is unchanged before/after/audit. These rows belong to the corrected adapter
identity; the original five-host chart and prior comparisons retain their old identity.
No tree optimization or speedup is claimed by this baseline.

[Full five-size table](matrix/SUMMARY.md), [raw manifest](matrix/manifest.json),
[independent audit](INDEPENDENT-AUDIT.md), [plan](PLAN.json). The next same-session
old/new adapter diagnostic will use much longer iterator workloads and its own
controls; it must not subtract these rows from historical baselines.
