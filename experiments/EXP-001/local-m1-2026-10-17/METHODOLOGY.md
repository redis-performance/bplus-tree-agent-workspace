# CPU Performance Engineering MCP application

Used the MCP for [usamahz/cpu-performance-engineering](https://github.com/usamahz/cpu-performance-engineering),
not a separate generic web search. Calls made during this experiment:

1. `ask`: how to qualify/profile direct B+ tree API microbenchmarks on Apple M1,
   with the actual compiler, allocator, warm-up and fixture description as context.
2. `get_benchmark("05-measurement-pitfalls")`: method/build/run implementation.
3. `read_source` for Hoefler/Belli: confidence intervals, repetition and reproducibility.
4. `ask`: distinguish hashing, branch, dependent decode and memory hypotheses with
   sampled stacks and assembly but no hardware counters.
5. `check_evidence`: audit the eventual result and its missing machine-control fields.
6. `lookup` and `get_benchmark` for 04-cache-latency and 14-pcore-vs-ecore:
   identify suitable future cache and scheduler controls.
7. `ask` with the actual macOS sampled-stack counts and the leaf-tag search source:
   explore scan hypotheses. Returned passages did not directly establish a suitable
   replacement, so the local follow-up proposals are our reasoning, not MCP endorsements.

## What was applied

The library's [measurement-pitfalls experiment](https://github.com/usamahz/cpu-performance-engineering/tree/main/misc/benchmarks/05-measurement-pitfalls)
uses fresh processes, retained observable results, separate warm-up, repeated samples,
load records, spread and generated code. Its method explicitly uses a “warmup of the
binary itself”. We excluded our calibration process, preserved every later raw result,
recorded load per process and inspected optimised assembly. The library's M4 Pro timing
numbers were not reused as M1 expectations. Our existing harness has no explicit DVFS
settling phase; this is disclosed rather than silently modifying the referee.

Hoefler/Belli warn that “differences in median or mean may not be statistically significant”
([Scientific Benchmarking, p. 5](https://htor.inf.ethz.ch/publications/img/hoefler-scientific-benchmarking.pdf#page=5)).
We therefore report paired A/A intervals and dispersion, not single-shot speedups. The
six-block t interval is an explicit approximation, not proof of stable hardware or a
distribution-free confidence guarantee. The +/-1% and 10 ms gates are our preregistered
campaign choices, not requirements attributed to that paper.

The paper also notes that warmed data “may or may not be representative”
([p. 7](https://htor.inf.ethz.ch/publications/img/hoefler-scientific-benchmarking.pdf#page=7)).
The current workload repeats a shuffled permutation after a full lookup warm-up. Tree
bytes omit the separate key fixtures and allocator overhead. We describe size sensitivity,
not cold-cache latency, and make no inference that a footprint crossing a cache capacity
proves misses. A full traversal reports time per emitted member, not request latency.

## What the MCP did not establish

The second ask returned broadly related model/counter references, but no passage diagnosing
this code on this M1. We do not attribute a specific cache, branch or execution bottleneck
to those references. Local profiles and assembly below guide hypotheses only; hardware
events and controlled variants would be needed to test those mechanisms. Blocked/unread
entries and the library's other CPU measurements are not evidence for this experiment.

## Follow-up controls learned from the MCP

The [cache-latency benchmark](https://github.com/usamahz/cpu-performance-engineering/tree/main/misc/benchmarks/04-cache-latency)
constructs a validated single-cycle permutation and a dependent pointer chase, with
line/page placement controls and inspected load-loop assembly. That is a separate latency
experiment, not what our B+ tree requests currently measure. A future access-pattern study
should specify whether it seeks serial latency or throughput with independent requests.

The [core-placement benchmark](https://github.com/usamahz/cpu-performance-engineering/tree/main/misc/benchmarks/14-pcore-vs-ecore)
records CPU identity and thread CPU time around each sample and uses a settling phase.
This suggests the next referee revision: log actual placement, thread versus wall time,
warm-up duration and timer properties. Its measured core numbering and clock estimates
are specific to its M4 Pro and are not imported as facts about this M1.
