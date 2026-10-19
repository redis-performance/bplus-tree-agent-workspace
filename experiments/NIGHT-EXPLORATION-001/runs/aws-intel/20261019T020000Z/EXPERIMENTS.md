# Intel experiments

| Work | Type | Decision | Evidence |
|---|---|---|---|
| 002 lookup SSE2 first-match | Three-implementation local population | REJECT/NONE | 432 process rows, all primary blocks slower |
| 003 update direction | Profile/control diagnosis | NONE, no implementation | Insufficient helper cost and failed controls |
| 004 iterator offset cache | Three-implementation local population | PARK/NONE | Fixed cap incomplete and unresolved controls |
| 007–014 exact SSE2 SCAN | Architecture replication of existing population | REJECT/NONE | Primary confirmation passed; qualified supplemental guard regressed in all six blocks |
| 013 corrected adapter | Baseline requalification | 10/40 qualified, no candidate | 120 processes/960 rows |
| 016 corrected SCAN | Baseline-only profile and fresh A/A | Complete, both A/A sizes qualify; root review pending | 60 captures, exact timing-binary mapping, 48 A/A rows |

Independent proposal/implementation contributions to AMD and ARM populations are retained in 005/009/012/015 and counted by the owning campaign, not as additional Intel populations.

Corrected exact-B attempt017: **PARK before candidate measurement**. Correctness and actual baseline.text parity pass, but fresh trim319/signed-zero A/A fails two blocks. No B guard/primary rows exist, no new measured population is counted, and no source is adopted.
