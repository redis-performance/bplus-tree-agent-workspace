# PROFILE-002 descriptive interrupted-PC counts

No speedup or unbiased time fraction implied. Timed regions contain sampler overhead;
thread timer additionally includes post-loop profile dump and is unusable for CPU/wall ratios.
Requested intervals may be rounded/coalesced; boundary sampler instructions can be captured.

| Capture | Samples | Unknown | >=100 | Top sampled symbols (counts) |
|---|---:|---:|---|---|
| 503-1000-lookup-hit-16 | 409 | 0 | True | _platform_memchr: 239; zbtreeScoreRaw: 49; _platform_memcmp: 38; zbtScoreLeafFindMember: 35 |
| 503-1000-lookup-hit-320 | 391 | 0 | True | siphash: 262; _platform_memchr: 66; zbtreeScoreRaw: 25; zbtScoreLeafFindMember: 19 |
| 503-1000-rank-16 | 138 | 0 | True | _platform_memchr: 52; zbtreeRank: 49; main: 14; zbtScoreLeafFindMember: 10 |
| 503-3001-lookup-hit-16 | 398 | 0 | True | _platform_memchr: 221; zbtreeScoreRaw: 53; siphash: 45; zbtScoreLeafFindMember: 36 |
| 503-3001-lookup-hit-320 | 378 | 0 | True | siphash: 263; _platform_memchr: 66; zbtScoreLeafFindMember: 25; _platform_memcmp: 12 |
| 503-3001-rank-16 | 119 | 0 | True | _platform_memchr: 56; zbtreeRank: 37; zbtScoreLeafFindMember: 11; _platform_memcmp: 4 |
| 809-1000-lookup-hit-16 | 415 | 0 | True | _platform_memchr: 231; zbtreeScoreRaw: 53; siphash: 40; _platform_memcmp: 34 |
| 809-1000-lookup-hit-320 | 462 | 0 | True | siphash: 249; _platform_memchr: 71; zbtreeScore: 70; zbtScoreLeafFindMember: 30 |
| 809-1000-rank-16 | 127 | 0 | True | _platform_memchr: 43; zbtreeRank: 41; zbtScoreLeafFindMember: 18; siphash: 9 |
| 809-3001-lookup-hit-16 | 401 | 0 | True | _platform_memchr: 230; zbtreeScoreRaw: 51; zbtScoreLeafFindMember: 41; siphash: 34 |
| 809-3001-lookup-hit-320 | 380 | 0 | True | siphash: 252; _platform_memchr: 65; zbtScoreLeafFindMember: 23; _platform_memcmp: 18 |
| 809-3001-rank-16 | 119 | 0 | True | _platform_memchr: 46; zbtreeRank: 43; zbtScoreLeafFindMember: 10; _platform_memcmp: 8 |
