# Member lookup narrow tag scan

Sequential coordinator pass, not an independent agent. Same frozen HARNESS-004 source, EXP-004 baseline profiles/codegen, prior experiment history. Backend/model/cost unknown.

EXP-001 short-key profiles show leaf memchr cost; tag matching could fuse candidate enumeration. Hypothesis: faster short-member lookup at unchanged hashing and exact collision semantics. Exact target leaf tag match. Requires current lookup qualification, which remains absent. Do not infer win from SIMD width or old timings. PARK until a distinct qualified lookup fixture and fresh matching profile exist.
