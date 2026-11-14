# AMD diagnostic result

Both compiler timing cohorts remain PARK. Baseline-only hit/update diagnostics complete in native and GCC15/LTO builds; no candidate was measured. The first path-resolution failure, four incompatible CPU/PID selector attempts, and corrected PID-only captures are retained. The correction changes collection invocation only; failed timing controls are not repeated.

All twelve corrected uProf captures return successfully. Their workload/CPU tick accounting differences stay within the registered 1% bound. Auxiliary attached user counters report 100% scheduling, and workload affinity remains CPU2. IPC is a three-second-window ratio, not instructions per operation or a timing-acceptance result.

| Capture | Maximum scope accounting difference | Window IPC |
|---|---:|---:|
| baseline-diagnostic-gcc15-lto-hit-v3 | 0.0000% | 3.84011 |
| baseline-diagnostic-gcc15-lto-update-v3 | 0.0000% | 4.48262 |
| baseline-diagnostic-native-hit-v3 | 0.3175% | 4.33604 |
| baseline-diagnostic-native-update-v3 | 0.0000% | 4.52268 |

## TMA classification

**Qualified Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and child shares: unavailable.** Raw uProf pipeline percentages are preserved separately. The CSV reports an aggregate heading despite PID selection; it does not expose raw event counts, actual per-event scheduling coverage or sufficient formula provenance to independently establish the reported slot denominator. A one-millisecond multiplex interval is a setting, not proof of full scheduling. Do not use these output percentages as qualified categories or compare them causally with Intel/ARM.

The diagnostics do not establish the cause of the earlier A/A variation. No duration-only retry, source trial or threshold relaxation follows. A future AMD campaign needs a separately justified measurement protocol and fresh reservation. The runner was released after artifact capture: original coordinator identity resumed, work and both cleanup timers inactive, no owned workload/container, preexisting Parca and CPU topology unchanged. Independent release verification agrees.
