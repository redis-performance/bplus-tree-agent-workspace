# Intel experiments

| Work | Type | Decision | Evidence |
|---|---|---|---|
| 002 lookup SSE2 first-match | Three-implementation local population | REJECT/NONE | 432 process rows, all primary blocks slower |
| 003 update direction | Profile/control diagnosis | NONE, no implementation | Insufficient helper cost and failed controls |
| 004 iterator offset cache | Three-implementation local population | PARK/NONE | Fixed cap incomplete and unresolved controls |
| 007–014 exact SSE2 SCAN | Architecture replication of existing population | REJECT/NONE | Primary confirmation passed; qualified supplemental guard regressed in all six blocks |
| 013 corrected adapter | Baseline requalification | 10/40 qualified, no candidate | 120 processes/960 rows |
| 016 corrected SCAN | Baseline-only profile and fresh A/A | Frozen, not executed | 60 captures/600s then 48 A/A rows/300s |

Independent proposal/implementation contributions to AMD and ARM populations are retained in 005/009/012/015 and counted by the owning campaign, not as additional Intel populations.
