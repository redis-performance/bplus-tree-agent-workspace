# Exact-binary iterator annotation

Offline `perf annotate` uses the original ELF and raw cycles:u data, with the
runner's perf7.0.14 decoder on the controller. Controller perf6.17 cannot read the
new raw ABI; this is a reader incompatibility, not a failed capture. No new profiling.
[Commands and hashes](commands.json). Percentages use **global sampled event period**,
not TMA slots, invocation counts, per-operation cycles or attributable latency.

At1M/full-output, baseline/A/B samples attributed to the packed-member length source line
(`zbtPackedData`, line589) are20.60%/15.02%/14.60%. The optimized DWARF attribution to the offsets helper callsite (line358) remains12.20%/12.11%/12.08%. In B, the latter
attributed instruction is `d96b: testq %rax,%rax` (the width-zero test is source line350), immediately after loading leaf score width,
on the cache-initialization branch. Its persistence despite less frequent arithmetic
makes **leaf-transition load dependencies versus arithmetic removal** a concrete
question. Baseline line589 combines0.56% on the prefix load and20.04% on its compare;
these are line aggregates, not single-instruction costs. This does not prove the test itself costs12% or establish a memory level.

B's cache-presence test (`d962`) has0.19% attributed samples; this does not establish
its total cost or rule out layout/branch effects. Optimized DWARF, skid and one bounded
sample window per build prevent instruction-level causal claims. The frontend rise
in TMA therefore remains an observation requiring a controlled follow-up.

Next diagnostic: count actual leaf transitions/member visits outside timing, then
use precise load sampling where supported to distinguish transition metadata loads
from packed-record loads. Keep existing binaries as transfer controls. Any code
experiment requires its own hypothesis/population, qualified timing and guards.
