# Baseline process-counter variance diagnostic proposal

**Recommend one separately preregistered, fixed diagnostic: four consecutive process-counter captures of the unchanged target baseline hit workload.** This can distinguish newly observed differences in completed instruction work, user-cycle cost and process scheduling exposure. It cannot explain the earlier failed rows, establish a stable variance distribution, qualify the timer, or admit a candidate. H2 and Q4 remain PARK regardless of the outcome. No build, execution, new consultation or fleet operation is authorized or performed by this proposal.

The Q4 first seed43 hit A/A block failed at+1.019883%; its other17 blocks passed. Reported whole-child user times were3.784421/3.882117/3.780056/3.800633seconds, with involuntary switches29/27/25/27 and no major faults. These observations do not identify a cause: switch counts omit descheduling duration, user CPU time includes setup/warmup, and no hardware counters were collected. A new counter capture cannot reconstruct them retrospectively. This review read saved Q4 metadata and the existing matched-baseline counter format; it did not independently repeat the Q4 numerical audit.

## Freeze before any execution

Use original ARM GCC15/LTO source `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, actual ELF `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb`, original lookup referee `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827`, and the current registered target environment with Parca off. No rebuild or source/fixture/allocator/compiler change. Save all source, ELF, referee, launcher and collector hashes and the exact command before running. The normal live reservation and isolation checks remain prerequisites for any later fleet execution.

Exactly one support/model probe followed, if it passes, by exactly four full captures, D0–D3. The probe invokes the existing `verify hit 43 1` under the same counter collection. Each full capture invokes **`measure hit 43 250000`**, matching Q4 hit work:500 members and125,000,000 reported lookup operations, with the original setup and warmup. No alternate seed/case/compiler, longer window, interleaved candidate, A/B labels, excluded warmup capture, adaptive repetition or same-phase retry. Retain every attempt. If a capture fails a gate, stop and report incomplete diagnostic coverage; never replace its row. If all four are uneventful, finish with “no variance episode characterized,” not a request for more runs.

The existing model validator must check every workload stdout: operation count, hits, score/checksum fields and tree-owned bytes against the frozen model, not against the first observed row. Preserve before/after identity/isolation checks and actual return codes. Do not edit the benchmark to emit counters or move validation into its timed loop.

## Events, support and scheduling gates

Collect these nine events in one process-lifetime `perf stat` invocation per capture:

- One **strong hardware group**: `{cycles:u,instructions:u,branches:u,branch-misses:u}`.
- Software events: `task-clock,context-switches,cpu-migrations,minor-faults,major-faults`.

The four hardware aliases already appear in retained target baseline captures with displayed100.00% scheduling. That historical observation is not a live support check for this new group/software combination. The single probe must establish current support. Record perf/kernel version, actual resolved event configuration where exposed, event modifiers, strong-group syntax and the complete raw stdout/stderr. No automatic alias replacement, raw-PMU encoding guess, weak group, event splitting, unsupported-event omission or CPU-wide substitute. Zero branch misses or faults is valid; unsupported/not-counted/NaN/negative values are not.

Use unscaled counts (`--no-scale`) and machine-readable output retaining each event's runtime and running percentage. **Every required event must have positive runtime and report100.00% running** in the probe and all full captures; grouped hardware runtimes must agree. Any lower percentage, absent scheduling field, unsupported event or unschedulable group ends this diagnostic without qualified counter interpretation. The existing CSV reports scheduling rounded to two decimals:100.00% is bounded displayed full scheduling, not proof of exact unrounded equality. Preserve raw enabled/running times if the installed collector exposes them, and require equality then; do not invent precision absent from the capture. No scaled reconstruction of a failed group.

Zero is valid for switch/migration/fault counts, but a zero task-clock, cycles or instructions count is invalid for a completed workload. Minor+major faults can be reported as total faults; no redundant total-fault event is necessary. Hardware counters exclude kernel execution; software task-clock and scheduling/fault events retain their documented process scope. Do not divide a user-only numerator by task-clock and label it core frequency without that scope caveat.

## Scope and launcher contract

Collect **whole-process** counts, including launch/setup/warmup/measurement/exit; do not label them steady-state instructions/lookup. No attachment after warmup, sampling, topdown collector or new interval monitor is needed. The perf controller must stay off the workload CPU; the benchmark ELF must execute pinned to the existing workload CPU. Preserve the existing reviewed CPU-affinity launcher if it supports complete process-lifetime counters with those properties.

If using the conventional off-CPU `perf stat -- taskset -c <workload CPU> <ELF> ...` arrangement, explicitly freeze and disclose its launch contract: counts include taskset startup on the controller CPU before affinity changes. The baseline ELF itself must start pinned, and that known launcher transition can contribute a migration. It is not comparable to Q4's stricter child-before-taskset affinity record and cannot diagnose an unexpected benchmark migration by itself. Do not silently claim identical launcher scope. If this distinction cannot be recorded and validated, select NONE rather than placing the perf controller on the workload CPU or omitting startup counts.

Keep benchmark inner-loop elapsed time, process wall time, task-clock and rusage as separate fields with separate scopes. In particular the parent's rusage of a `perf` wrapper can include collector work; it must not be relabeled as Q4's baseline-child rusage. Use explicitly scoped child accounting if already supported, otherwise leave that comparison unavailable. The collector itself changes conditions; no counter-instrumented elapsed value qualifies the original uninstrumented timer.

## Fixed analysis and decision limits

Publish all four rows in capture order, or the incomplete prefix and failed attempt. Show raw counts, runtimes/scheduling, workload/model outputs, affinity, inner elapsed, process wall time and software events. For valid full captures only, calculate min/max and fractional range relative to their median for each quantity, plus per-row user cycles/instruction, branch-misses/branches and task-clock/process-wall occupancy with units and scope. No A/A pairing,±1% pass/fail calculation, outlier removal, significance claim, inferred confidence interval or acceptance decision. Four captures are descriptive, not a reliable tail estimator. Normalizing whole-process counters by125million may be shown only as explicitly amortized whole-process totals, never pure lookup cost.

Interpretation is bounded:

- Stable completed instructions/branches with varying user cycles is consistent with changing execution cost. It does not distinguish frequency, execution stalls, cache behavior, interrupts, thermal effects or code-layout causes.
- Stable task-clock with larger process wall time, especially with additional switches, is consistent with off-CPU exposure. Counts alone neither measure descheduled duration per switch nor identify the competing task. Known launcher migrations must remain separate from suspected workload migration.
- Varying retired work or faults with equal model outputs points to setup/runtime-path differences worth a separate diagnostic; it does not establish a defect in the frozen loop or justify removing setup from the original measurement after the fact.
- Stable counters and no visibly variable row mean this bounded diagnostic did not capture the issue. They do not show Q4's failure was harmless noise or establish a future qualification pass.

A future change of conditions needs independent, contemporaneous evidence tying a controllable condition to the new capture: for example, verified workload affinity escape, a reservation conflict, a recorded collector/isolation violation, or a separately documented frequency policy mismatch. Such evidence can justify correcting that condition under a new reviewed protocol with new controls. Counter ratios or one slow row alone do **not** justify changing affinity/governor, extending windows, discarding rows or rerunning the failed qualification. Any later condition change must be named, preserved and reviewed separately; it cannot retroactively repair H2/Q4. This proposal contains no such change or acceptance route.

## Evidence limits

This is an independent proposal, not a newly executed diagnostic. No fresh MCP call or event-support claim is made; the controller will consult before selection. No qualified ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring or child percentages can be derived from these events. Those categories remain unavailable. A CPU-wide topdown result, a hotspot share or a cycle/instruction ratio cannot fill that gap.
