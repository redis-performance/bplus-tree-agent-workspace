# Fresh-seed allocator/source confirmation

Preregistered after baseline factorial and exploratory threshold trace. Separate serial
correctness extension; no timings, optimization choice or additional suite count.
Exact baseline and retained EXP-004 A/B/C source hashes; controlled exact and round16
adapters unchanged from COUNTERS-006. Release O3/debug and ASan/UBSan O1/debug:16cells.
All compiler/assertion/hash options identical within each build type. Root unchanged.

Fresh seeds31133/31139. Every n0..96 plus n97/513, five lengths16/253/254/319/320,
both insertion directions. Same unchanged semantic oracle and appended layout/capacity
hashes:1980fixtures/cell,325860modelchecks and163246200exactresults/cell. Expected
counts derived from3n+5 and14n²+29n,twentyfixtures/size. Original oracle not weakened.

Predictions: all semantics pass; within EACH controlled capacity policy, all four source
variants and both build types produce identical complete stdout on the fresh matrix.
Do not demand equality across capacity policies. An output mismatch fails that prediction,
is retained and classified without rerunning. Validate exact file hashes before/after.
Unit controls already passed at both optimization levels/instrumentation for these exact
adapters; repeat no unit cell. Save patches/source hashes/binary hashes/commands/rawoutput.

Each child <=120s; total diagnostic budget480s. Stop incomplete cells if budget expires,
record partial status and preserve all rows. No detached processes or overlap with any
benchmark/profile. Deadline check before starting. Expected <=6minutes from earlier
complete-matrix controls; no source acceptance even on success. Independentreviewfailed,
coordinator confirmation explicitly sequential;backend/model/costunknown.
