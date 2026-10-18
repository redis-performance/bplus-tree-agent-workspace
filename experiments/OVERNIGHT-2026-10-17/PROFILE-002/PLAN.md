# PROFILE-002 preregistration — scoped self-process signal sampling

Preparation diagnostic, not optimisation or qualification. AA-003 failed all cells.
Hypothesis: public in-process ITIMER_PROF/SIGPROF can collect and symbolicate interrupted
user PCs within standalone operation loops, with a known-function calibration. This
uses the program's own timer, not external child inspection; no denied action retry,
permission escalation, policy change, external service or private configuration.

Inspect installed SDK getitimer/sigaction manual and ucontext/mcontext/dladdr declarations
before code. ITIMER_PROF accounts process user+system CPU time, signal delivery may be
coalesced/delayed and intervals rounded to OS resolution. This single-thread diagnostic
records PCs only, not call stacks, PMU events, cycles, actual frequency or kernel PCs.
Handler uses only checked lock-free atomics and ucontext field reads; symbolication and
I/O occur after timer disabled and SIGPROF blocked. No allocation/logging in handler.

Separate snapshot over HARNESS-002; unchanged target .c/.h. Instrument only benchmark
operation boundaries, exclude fixture construction and warmup. Record exact source,
patch,compiler/flags,binary hashes,requests,observed samples and overflow. Root unchanged.
Release same -O3 flags as AA-003, no source instrumentation; added sampler code may
change layout and perturb timings. Instrumented CSV cannot enter qualification tables.

Before tree captures: known noinline arithmetic loop, two requested intervals1000us and
3001us, fixed200000000 iterations/eight adds per iteration. >=20 samples and >=90% at
known function required for each calibration, no overflow. If calibration fails retain
failure and stop profile capture, no retry with relaxed sample threshold. Validate tiny
all-case benchmark under release and ASan/UBSan; small loops may deliver zero samples.

If calibration passes,12 fixed serial tree captures: hit16(50000000 ops),hit320(10000000),
rank16(10000000);100000 members,construction seeds503 and809,independent query seeds701
and907 respectively,10 warmup passes. Loop order seed,interval1000/3001,cell hit16/hit320/
rank16. Each child<=120s; full captures<=240s. No builds/tests/local agents overlapping.
Require counts/checksums and no overflow; >=100 samples per capture for a useful coarse
symbol distribution, otherwise mark that capture insufficient (do not extend it).
Symbolicate every PC, preserve unknowns and raw evidence. Report all twelve captures.
No optional stopping, discarded slow windows or promotion to precision remedy.

Public summaries strip absolute machine paths; full raw PC/log evidence remains ignored
scratch with SHA256. Executable PCs resolve offline via atos/dSYM; library attribution
via dladdr is coarser and may lack inline details. Function sample shares are descriptive,
not unbiased CPU-time fractions; timer quantization, interrupt-PC bias, phase aliasing,
signal overhead, sampling variance and layout remain limitations. Requested intervals
need not produce distinct effective cadences. No M4 CPU/clock/result transfer.

CPU MCP ask consulted; unrelated NAPI/perf passages do not support this method. Local
SDK documentation is primary evidence for API behavior. No independent agent available
(startup failed); sequential review only. Backend/model/cost unknown. All source and
acceptance decisions remain NONE/PARK until full prerequisites are met.
