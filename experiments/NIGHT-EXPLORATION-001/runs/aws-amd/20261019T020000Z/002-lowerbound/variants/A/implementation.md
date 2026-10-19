# Implementation A

Sequential pass, same baseline8fab511e, separate remote snapshot/build. Structured local comparator with lazy equality block. Numeric< and> retain signed-zero ties. Finite scores only; NaN is outside low-level contract. No allocation, hashing, assertion or layout changes. Equality still calls existing exact length-aware byte comparator. Compiler may make variants identical; do not invent algorithmic independence.
