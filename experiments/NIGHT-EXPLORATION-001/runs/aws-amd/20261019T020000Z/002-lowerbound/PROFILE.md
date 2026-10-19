# AMD baseline profile

Whole-process perf stat and cycles:u997Hz frame-pointer sampling include construction, warmup, timed loop and validation/destruction. These are not timed-loop percentages or causal speed estimates. Source8fab511e, Clang18.1.3 -O3, CPU2, libc allocator, unchanged assertions/hash. Three million operations,100Kmembers,16bytes,seed1. Raw profiles remain private scratch with checksums; text evidence retained.

Update samples: zbtScoreInsertAt22.70%, zbtScoreLeafBuild13.03%, zbtScoreLeafLowerBound11.00%, zbtScoreFindLeaf9.09%. Within lower bound, packed member decoding appears as3.09% of whole process; score-only comparisons currently materialize members first. Hit lookup: leaf finder14.76%, score-raw35.41%; miss leaf finder1.91%. Lower-bound lazy member access is an evidence-led candidate; first qualify fresh baseline A/A.
