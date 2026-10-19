# Fresh ARM original SCAN diagnosis

Baseline8fab511e, unchanged source/header/hash/allocator/assertions, Clang18-O3 on
NeoverseV2, owned CPU2 lease. Six original SCAN cases:100K/1M members,16bytekeys,
seeds1/2/3, requested1M operations each. No changed operation counts, candidate or
new A/A schedule. Exact AMD FIFO-scoped diagnostic copy enables cycles:u sampling
at997Hz immediately before the original elapsed start and disables after elapsed read;
control/timer edges remain included. Original workload and output checks remain intact.
Referee diff and SHA256 identify instrumentation. Sample/IP attribution is approximate;
no instrumented timing is a speed result. Do not conflate all-match zbtLeafTagMatches
with the previously withdrawn first-match/index lookup premise.

One bounded180second job builds separate original/diagnostic baseline executables,
compares disabled observer outputs and actual operations/owned bytes/checksum, verifies
one perf-disabled control has zero events, and captures six scoped profiles plus raw
period/IP output, reports, source-linked disassembly, compiler/source/binary hashes.
Raw perf data stays on the owned runner with SHA256. All workloads serial underlease.
Exact all-match instruction ranges and folded/tag-tail paths must be attributed before
forming a hypothesis. No candidate code or optimization population is authorized here.
Missing evidence yields NONE, not speculative NEON or portable rewrites. A later supported
native implementation would require a separate population/fixed referee/AA/guards/review.
Actual participant/root/aws_arm, backendnativeCodex; model/token/USD costs unknown.
