# Intel summary

Source adoption: **NONE**. Local measured populations: **2 (0 accept, 1 reject, 1 park)**. Architecture replications: **1 rejected**. No fresh source switch after the guard rejection.

The old-source SSE2 SCAN candidate improved primary cases under independent confirmation, but its qualified 319-byte reversed-leaf/signed-zero supplemental guard was slower in all six blocks: +5.167%, +4.695%, +3.246%, +5.738%, +6.877%, +1.566%. Median +4.931%; minimum window 199.87ms. This rejects the candidate despite other gains. Eight of ten qualified supplemental cells pass; one additional qualified cell is mixed and twenty controls are noisy. Original 24 guard gaps and focused 14 noisy cells remain historical unresolved evidence.

Corrected-adapter baseline source13e459ff8 is separately frozen; no old timing is reused for its pending baseline-only SCAN profile/control qualification. Exact model/backend and measured token/USD costs are unknown.
