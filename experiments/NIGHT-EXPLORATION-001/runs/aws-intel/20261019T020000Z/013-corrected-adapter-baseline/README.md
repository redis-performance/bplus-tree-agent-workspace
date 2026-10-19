# Corrected-adapter Intel baseline

Corrected-adapter baseline complete: 120 processes, 960 raw rows, 240 A/A effects and seven validations pass. Exact detached 13e459ff8 and all old/new pre/post hashes verified. Only 10/40 cells qualify, including 11 short cells among the 30 unresolved. This is a new harness baseline, not an optimization result; source adoption NONE. Supplemental 014 preparation is next.

Timing phase: 337.6026312559843 seconds under the frozen 1200-second cap; whole helper 05:10:17–05:16:44 UTC under 1800 seconds. Same-binary ABBA uses seeds 1–3 twice, five sizes, eight operations, 16-byte members and one million requested operations. No retry or duration adjustment. All raw rows and per-cell qualification are retained in `results/` and `audit.json`. The original driver has no per-process UTC boundaries; serial execution follows its unchanged loop. CPU affinity and endpoints are 2.

| Size | Case | Qualified | Minimum ms | Max absolute effect % |
|---:|---|---|---:|---:|
| 100 | insert | False | 0.0476 | 5.4617 |
| 100 | lookup-hit | False | 30.6011 | 1.7770 |
| 100 | lookup-miss | False | 15.4798 | 8.1014 |
| 100 | rank | False | 26.6046 | 6.0534 |
| 100 | iterate | False | 3.9250 | 3.1080 |
| 100 | scan | False | 22.5216 | 2.1994 |
| 100 | update | False | 318.7226 | 1.0006 |
| 100 | delete | False | 0.0250 | 6.8372 |
| 1000 | insert | False | 0.4714 | 1.3987 |
| 1000 | lookup-hit | False | 39.3955 | 1.1457 |
| 1000 | lookup-miss | True | 18.0445 | 0.7899 |
| 1000 | rank | False | 36.6062 | 2.3493 |
| 1000 | iterate | False | 3.9601 | 3.9935 |
| 1000 | scan | False | 33.0967 | 4.4952 |
| 1000 | update | True | 506.5842 | 0.4513 |
| 1000 | delete | False | 0.2366 | 0.9332 |
| 10000 | insert | False | 4.6570 | 1.4888 |
| 10000 | lookup-hit | True | 58.6044 | 0.4298 |
| 10000 | lookup-miss | False | 23.7833 | 2.6404 |
| 10000 | rank | True | 76.6567 | 0.6702 |
| 10000 | iterate | False | 3.9777 | 11.9236 |
| 10000 | scan | False | 67.1051 | 1.0462 |
| 10000 | update | True | 553.6806 | 0.7371 |
| 10000 | delete | False | 2.3080 | 0.6634 |
| 100000 | insert | False | 54.4750 | 6.7530 |
| 100000 | lookup-hit | False | 130.9435 | 5.6825 |
| 100000 | lookup-miss | False | 71.1159 | 2.0698 |
| 100000 | rank | False | 173.7937 | 2.9210 |
| 100000 | iterate | False | 4.0173 | 0.5537 |
| 100000 | scan | False | 87.4682 | 9.1541 |
| 100000 | update | False | 728.0516 | 2.6313 |
| 100000 | delete | False | 34.1095 | 4.4971 |
| 1000000 | insert | False | 770.7528 | 2.3479 |
| 1000000 | lookup-hit | True | 209.0917 | 0.3917 |
| 1000000 | lookup-miss | False | 148.3001 | 1.7453 |
| 1000000 | rank | True | 299.5126 | 0.4111 |
| 1000000 | iterate | False | 4.5302 | 4.0469 |
| 1000000 | scan | True | 116.4247 | 0.2276 |
| 1000000 | update | True | 1034.0219 | 0.4253 |
| 1000000 | delete | True | 555.5783 | 0.6067 |
