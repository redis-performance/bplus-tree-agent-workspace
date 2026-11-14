# H1 native discovery — REJECT, selection NONE

Exact upstream ee8e7f701, GCC13/O3/noLTO; renewed native A/A18/18blocks passes, all72rows≥250ms. All216comparison rows and exact source/binary joins retained. Every variant passes57native+57sanitizer upstream tests,36fixturecells,135000 sanitizer oraclechecks. Tree-owned memory unchanged. No confirmation or accepted-source claim.

Median elapsed changes (negative faster):

| Variant | Hit primary | Score | Miss | Inline256 | External384 | Update |
|---|---:|---:|---:|---:|---:|---:|
| A global inline |−1.287%|−0.732%|+1.901%|−2.188%|−1.022%|−1.802%|
| B selective membership |−6.787%|+2.457%|+3.530%|−3.183%|−1.721%|+2.003%|
| C match kernel |−2.308%|+2.889%|+2.755%|−3.451%|−2.706%|+0.206%|

A misses2%primary and fails missguard in allthreeblocks. B clears primary but fails score/miss/update in everyblock. C clears primary but fails score/miss in everyblock. No gate is waived. Rawlookup frames grow to272bytes for all; symbol removal alone did not predict safe performance. B is evidence that membership specialization can help one case, not an eligible optimization. Keep patches; proceed to separate metadata hypothesis.

GCC15/LTO was not measured after failed qualification. Native effects do not qualify it or establish server-command recovery. Optional bounded matched profiles of failedB can inform a genuinely new hypothesis, but cannot repair this rejection.

## TMA classification

Baseline/candidate Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring unavailable as validated workload categories. Baseline CPU-wide collection lacks continuous exclusion/formula qualification; candidate uncollected at discovery. Children unavailable. Hotspot/size/instruction observations are not pipeline-slot shares.
