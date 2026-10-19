# Original delete operation baseline diagnostic

One bounded baseline-only scoped profile job, CPU2,180-second cap. Exact source8fab511e, unchanged original microbench delete case, sizes100K/1M,16byte members,seeds1/2/3. Requested operations1M but actual deletes equal size; preserve reported fields. Use existing validated FIFO-scoped baseline diagnostic binary, enable only around measured delete loop. Six cycle-sampling captures; no candidate or A/A and no optimization population yet.

Review prior AMD lower-bound materialization, builder-write and full-chunk move rejections before any proposal. First-match SSE2 scanning and physical/count-one packed decoders also have negative or unqualified prior results on Intel/Apple. Do not repackage those as new hypotheses. Select NONE if already exhausted paths dominate or fresh attribution is insufficient. Any novel proposal requires measured profile evidence and the required population process. Source stays NONE.
