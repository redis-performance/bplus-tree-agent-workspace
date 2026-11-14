# Failed selective-inlining diagnostic

One matched whole-process counter pair and one cycle-sample pair per hit/score/miss case, same exact native baseline/B ELFs, seed17 and200M operations. Setup/warmup included;100% counter scheduling. This diagnostic explains leads only and does not change H1 REJECT or qualify a candidate.

| Case | Instructions change | Cycles change | Branches change |
|---|---:|---:|---:|
| Hit |−6.832%|−6.477%|−6.912%|
| Score |+1.843%|+2.864%|+3.393%|
| Miss |+6.369%|+3.751%|−5.208%|

Instruction changes support the discovery direction, but one instrumented pair is not an independent timing confirmation. Allraw counters/reports retained. Score retains generic leafcall while rawframe grows176→272bytes; miss adds retired instructions despite fewer branches. These facts motivate investigating allocation of live state and shared dispatch in a future independent proposal population. They do not establish a pipeline bottleneck or prove any specific spill is the dominant cause.

## TMA classification

Baseline and B Frontend_Bound,Bad_Speculation,Backend_Bound,Retiring unavailable as validated workload categories. Every raw topdown capture is CPU2-wide and lacks continuous exclusion/formula qualification; childcategories unavailable. Rawlabels remain available without causal interpretation.
