# DIAG-015 — fixed idle-gap intervention after predecessor workload

Preregistered before measurement. DIAG-014's selected zero-trim-f6 OTHER/SAME contrast
reproduced under reversed labels, but one placebo interval failed precision. Its
robustness claim remains PARK. This is a new intervention on the process boundary,
not a retry of unchanged warmup/QoS/count policies or a source comparison.

Hypothesis: the observed predecessor contrast is transient enough that a fixed100ms
idle interval between predecessor exit and target launch attenuates it. This includes
all unmeasured process/scheduler/power/cache effects; do not label it a frequency test.

Same frozen HARNESS-006 binary. Target95/bytes16/trimmed/forward/alternating-zero/mask6,
20m requested items/20000065effective,threewarmuptraversals. Predecessor SAME is the
target case; OTHER is integer/mask0 with other parameters unchanged. Freshseeds45121/
45131. Three protocols: gap0 contrast, gap100ms contrast, gap100ms SAME/SAME placebo.
Labels A=SAME,B=OTHER in contrast; bothSAME in placebo. Apply identical selected gap
to both arms. Open output files before precursor; defer parsing/hashing/bookkeeping
until target exit, apart from monotonic timestamps and the requested sleep. Record
actual coordinator gap separately; no inference that the requested gap is exact.

Six ABBA blocks per seed/protocol, rotateprotocolorder eachblock and alternate seeds.
144target+144predecessorrows andoneprospective1m binarywarmup. Fixed schedule; no row
exclusion, optionalstopping or analysis-driven extension. Child<=120s, total<=400s;
allserial, no agents/builds/tests/profiles duringmeasurement.

Primary target wallns/item, sixblockeffects100*(meanB/meanA-1) and95%t df5 intervals.
For eachseed also compute six paired interactions effect(gap100)-effect(gap0) with
the same interval. Support requires all invariants/duration>=10ms, bothgap0 intervals
below-1%, bothgap100contrast and bothplacebo intervals within[-1,+1]%, absolutegap100
mean at most halfgap0 mean forbothseeds, and bothinteractionlowerbounds above+1%.
Otherwise unsupported (invalid ifcontrols fail). Preserveeveryrow andallintervals.
This deliberately strong diagnostic criterion doesnot adoptanidlepolicy orrepairany
sourceguard evenifpassed; suchadoptionneedsseparatefreshqualification. No clock/core
type/portableperformanceclaim. Independentreview/model/backend/tokenusageunknown.
