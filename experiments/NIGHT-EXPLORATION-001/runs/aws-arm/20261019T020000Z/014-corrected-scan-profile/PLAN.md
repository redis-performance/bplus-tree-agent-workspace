# Corrected-adapter baseline-only scoped SCAN profile

Exact source13e459ff8800be3f02b6b45c87dd7b0c39453fa9, corrected _Noreturn adapter.
Separate isolated original and diagnostic builds with identical compiler/flags/allocator,
assertions, tree/header/vendor; original8fab builds and evidence remain immutable.
Use the previously validated FIFO diagnostic unchanged: PMU enable acknowledgement
immediately before original timed window; disable immediately after. Six captures:
SCAN100K/1M,16-byte original fixtures,seeds1/2/3,5M requestedops each. Fixed5M chosen
before data for consistency with the fresh A/A protocol and longer profiling scope.
Original/disabled/profile outputs must match operations/checksum/memory/fixture fields;
one perf stat disabled control must count zero. CPU2 serial owned job cap600s including
build and all controls/captures; no retries or expanded scope after observations.

Exact same-IP source/instruction attribution will be mapped anew from this binary's
source-linked disassembly. Never reuse old8fab offsets, confuse index leaf-ID checks
with leaf tag matching, or treat inclusive parent percentages as exclusive costs.
Compare relevant instruction bytes between original and diagnostic; keep raw perf
locally with hashes and publish source-linked assembly/samples/controls. PMU sample
skid/weights approximate; zero samples do not prove zero cost. No speedup inference,
new candidate, proposal round or timing change. This is a distinct harness baseline,
not a rescue of original ARM failed A/A. Root decides later whether evidence supports
an actual independent proposal population, conditioned on separately frozen015 A/A.
