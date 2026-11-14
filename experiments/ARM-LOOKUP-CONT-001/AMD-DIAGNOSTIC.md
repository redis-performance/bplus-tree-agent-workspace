# AMD failed-control diagnostic — separate from acceptance

Original144-row AMD qualification is PARK. Native update block1 is−1.124%; GCC15/LTO score block0+1.170%, update blocks+1.087%,+1.422%,−1.422% fail the fixed±1% A/A bound. Every original row and protocol remain. No candidate timing or unchanged control retry is authorized by this diagnostic.

Bounded baseline-only assessment: for each compiler, capture three5-second pipeline-utilization windows for hit and update under the frozen baseline binary, with the workload attached onCPU2 and controllerCPU0. Use the actual topdown-profiler0.3.1 UprofPcmRunner command generator, explicitly replace its hardcoded all-core flag with documented `-c core=2 -p PID -u 1`. Installed uProf5.2 help supports process/core/user selection, unlike the helper's obsolete per-PID claim. Preserve generated and executed argv and tool source hash. Record before/after CPU2/process accounting, live affinity, and single-thread identity. Root/category units and formulas need separate audit; unavailable event scheduling/formula provenance keeps categories unqualified even if percentages look plausible.

Also capture3-second process-user grouped counters and sampled cycles for each workload/compiler, kept separate from acceptance. Compare instruction/cycle rates only within their actual scope; a fixed-time counter total is not instructions per operation. No raw timing from this instrumentation enters a comparison. The workload is intentionally long-running and terminated only after captures; use valid fixed sweep counts and preserve any launch/capture failure.

Read-only process, CPU topology/frequency and housekeeping observations may explain a concrete changed-condition proposal. Do not pin unrelated services, disable sysctls, discard outliers or silently lengthen/retry the parked cohort. Any subsequent metrology attempt requires a separately frozen condition and its own complete controls. ARM/Intel evidence remains separate.

## Collector path correction

The first diagnostic stopped before workload launch: the kernel-specific perf path was a broken symlink. Preserve that directory and its failure. Revision 2 requires an explicit existing perf executable and records its resolved path, version and SHA256. The installed 7.0.14 executable is selected, while the running kernel remains 6.14.0. This tool/kernel difference is disclosed; counter scheduling and capture success remain qualification gates. Use new `-v2` capture labels; no timing or source change, and no failed baseline control is repeated.

Revision 2 captured auxiliary counters/samples but uProf rejected `-p` together with `-c`. All four failures are retained. Revision 3 removes the incompatible core selector and uses PID/user selection with the workload pinned to CPU2. First run only one bounded native-hit capability capture; do not fan out before inspecting success and scope. This is a tool-invocation correction, not baseline timing requalification.
