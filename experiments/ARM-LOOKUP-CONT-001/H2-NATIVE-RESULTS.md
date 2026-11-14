# H2 native discovery — two eligible leads, acceptance pending

Three independent metadata variants completed216rows on the renewed qualified native cohort. All fixed2% primary /1% guard and memory gates retained. B and C pass discovery; no source acceptance before LTO target, additional guards, confirmation, profiles and independent review.

| Variant | Hit median | Score | Miss | Inline256 | External384 | Update | Memory |
|---|---:|---:|---:|---:|---:|---:|---|
| A enlarged header cache |−4.344%|−4.020%|+0.345%|−2.601%|−1.497%|−4.112%|+1.233% short /+1.109% update: FAIL|
| B same-size cached bytes |−4.801%|−5.096%|−0.777%|−2.028%|−1.670%|−4.026%|unchanged|
| C metadata-first layout |−5.661%|−2.900%|−0.322%|−2.717%|−1.840%|−1.147%|unchanged|

A is REJECT on the declared memorygate; it will not consume further LTO/Intel timing runs. Its patch, correctness and allnative measurements remain. Builds may retain its ELF for provenance, but future measured_variants explicitly list B/C only. This exclusion precedes any LTO/Intel candidate timing and does not hide a failing measurement.

ARM assembly confirms A/B replace width/multiply/round metadata sizing with cached16-bit loads; C uses fixed offsetbase and count-derived tags, reducing the leaf helper frame128→112bytes. Helperbody/scanner unchanged. A's declared header growth caused a measured memory failure; no relaxed tradeoff is introduced.

B/C require focused iterator, rank and delete/reinsert guards because metadata/flags affect paths outside the six original cases. Those guards will be separately frozen and qualified before adoption. Select the final implementation using independently qualified LTO results and guards, not these native medians alone.

## TMA classification

Native baseline/candidate Frontend_Bound,Bad_Speculation,Backend_Bound,Retiring and children unavailable as qualified workload categories; matched candidate profiles pending. Original CPU-wide baseline labels remain exploratory. Static address dependence is evidence for the hypothesis, not a pipeline cause claim.
