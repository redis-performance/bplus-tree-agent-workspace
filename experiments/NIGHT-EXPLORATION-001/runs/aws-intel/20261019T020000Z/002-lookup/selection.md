# Chair decision: bounded inline SSE2 tag search

Three sequential proposal passes; no independent proposer agents (all team slots occupied). Ranking A>B>C: A has direct leaf/codegen evidence and a distinct16-byte SIMD mechanism; B is a previously tested SWAR patch with unresolved single-query guards; C lacks collision-specific evidence. Choose A for one fixed exploratory population.

A/A qualifies100K hit and1M miss only.100K hit effects-0.643%..+0.140%;1M hit-0.293%..+1.458%. No adoption qualification overall. Fixed screen six cells, three variants, six ABBA blocks, seeds1/2/3, calibrated counts, at most300s. All rows retained. Large consistent dual-primary effects may justify fresh confirmation but cannot waive controls/guards. Full LOOKUP-001 guard matrix remains required before recommendation. No source adoption overnight.

Implementation A16-byte loop/scalar tail; B16-byte loop/libc tail; C16-byte loop/overlapping masked16-byte tail with scalar handling below16. Every load remains within supplied range; scalar fallback uses memchr when SSE2 unavailable. No hashing, allocator, assertions or layout changes. Guard correctness before timing: original43tests each release/sanitizer, independent-query144fixture checks each candidate, exhaustive first-match/page boundary checks plus forced fallback.
