# Intel summary

Source adoption: **NONE**. Local measured populations: **2 (0 accept, 1 reject, 1 park)**. Architecture replications: **1 rejected**. The Intel runner is idle for coordinator review; no corrected-source candidate timing is authorized.

The original-source SSE2 SCAN candidate passed primary discovery and independent confirmation, but its qualified 319-byte reversed-leaf/signed-zero supplemental guard was slower in every block: +5.167%, +4.695%, +3.246%, +5.738%, +6.877%, +1.566%. The median is +4.931%; the minimum window is 199.87 ms. This rejects the candidate despite other gains. Eight of ten qualified supplemental cells pass; one additional qualified cell is mixed and twenty controls are noisy. The original 24 unresolved guard cells and focused 14 noisy cells remain unchanged. No alternate implementation retry is permitted.

Independent audit `1217ba80a` reconstructs all 2,124 supplemental calibration/A/A/B processes, 360 effects, exact schedules/models and post-phase identities. The decisive fixture has seven members and no full vector or word chunk, so its regression does not establish the cause of the overhead.

The corrected-adapter baseline uses frozen source `13e459ff8`; its separate SCAN diagnosis is complete. The helper accounts for 368/1,315 and 478/1,740 captured executable-text samples, with actual instruction/source mappings retained. Both fresh A/A cases using seeds 401–403 qualify, with maximum absolute effects of 0.288% and 0.196%. These are baseline-only results, not a candidate speedup claim. No old timing is reused to clear corrected-source controls or guards.

The first corrected profile driver finished all 60 captures before failing on an absent unreferenced linker symbol. A separately frozen metadata-only correction used ELF headers and function symbols, retained the failed attempt, and finished within the original 600-second deadline. No benchmark, control or capture was repeated.

Exact backend/model and measured token/USD costs are unknown. All public artifacts use generic machine and workspace identifiers.
