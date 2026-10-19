# Implementation B

Sequential pass, same baseline8fab511e, separate remote snapshot/build. Inline leaf-position comparator helper reused only by lower bound. Numeric< and> retain signed-zero ties. Finite scores only; NaN is outside low-level contract. No allocation, hashing, assertion or layout changes. Equality still calls existing exact length-aware byte comparator. Compiler may make variants identical; do not invent algorithmic independence.
