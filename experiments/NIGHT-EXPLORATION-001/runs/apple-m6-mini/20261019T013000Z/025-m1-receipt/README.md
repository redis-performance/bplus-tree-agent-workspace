# M1 round-three receipt and M6 handoff

The M6 operator observed remote M1 commit `9ce51754a9eebb0e53c65afe650c54a146515808` at the timestamp in RECEIPT.json. The commit is dated 01:46:33 UTC. That is a publication observation, not proof the M1 runner is active now or has consumed M6 evidence.

M1's first-pass queue is recorded as closed. Its count-one decoder trial ran 6,720 serial processes / 866,880 sample rows in four phases. All 70 A/A cells miss the fixed 10 ms window gate; local count-one leads and repeated guard losses remain unqualified. Decision PARK / source NONE. The worker records nine total populations, 0 accepted / 3 rejected / 6 parked. Its local rank/decoder passes were sequential; inherited historical populations have mixed provenance. These counts remain separate from M6. The archive reconstruction was a separate algorithm by the same worker; the original report explicitly says no independent agent or reviewer ran.

The original M1 tree C/H matches the unchanged M6 tree; M1's adapter remains legacy. Corrected-adapter M6 controls do not qualify M1, and old-adapter M1 data does not qualify corrected M6. Original compressed archives remain in immutable Git blobs; their SHA256 values and source paths are recorded here. No native workload ran for this receipt.

At the original round-three snapshot, the M1 worker reported DNS failures for M6 through 01:39:28 UTC and a denied local index write. This snapshot has since been published externally; it does not establish that the worker's network or permissions changed. Do not retry a denied write or change permissions to bypass it.

M6 publishes milestones on `exploration/apple-m6-mini-20261019T013000Z`; the main README contains the combined five-host baseline and current charts. Its latest exact NEON attempt is PARK before candidate timing after failed fresh controls. Decoder replication leads also remain unqualified or guarded; no tree optimization is accepted. Read the M6 MORNING-REPORT and exact frozen identities before any new M1 proposal. Do not repeat either completed count-one schedule, pool host timings or substitute a private-kernel lead for public-iterator validation.

The [independent receipt audit](INDEPENDENT-RECEIPT-A.md) reconstructs all 6,720 process outputs and 866,880 sample rows from the four Git archives. Every sample window is below 10 ms. This checks counts, coverage, bounds and source/archive pins; it does not rerun native correctness, recompute every candidate effect or establish missing serial/return-code metadata. The operator's initial all-nine-sequential wording is corrected; original M1 evidence is untouched.

Post-receipt update: [M1 now explicitly confirms reading the M6 decision](../026-m1-gate-confirmation/README.md). This later record resolves the earlier consumption uncertainty without changing the original archived evidence.
