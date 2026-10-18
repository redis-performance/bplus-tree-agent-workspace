# COUNTERS-001 — scoped execution-count profiles: COMPLETE

Three serial instrumented children passed semantic checks and profile-boundary checks.
Clang17 public reset/dump APIs exclude setup, warm-up, validation and cleanup from the
saved counters. No insertion/deletion calls remain. Lookup API count and scan callback
count exactly match the effective operation count in each CSV. Raw profraw/profdata
and complete JSON exports stay in ignored scratch; manifest records their SHA256.

| Scoped function entries | Scan16 | Scan320 | Lookup-hit16 |
|---|---:|---:|---:|
| scan callback | 1025150 | 1024930 | 0 |
| leaf tag matcher | 1066100 | 1064350 | 0 |
| leaf hash retrieval | 588460 | 582110 | 0 |
| SipHash | 588460 | 0 | 1000000 |
| leaf member finder | 0 | 0 | 1014150 |

These are execution counts, not time shares or performance rates. Source inspection
explains the absence of SipHash in scan320: external member records retain their hash,
while inline members must hash bytes when the scan collision/probe path requests it.
The counts establish exercised paths; they do not establish which path is expensive.
The instrumented CSV timings are not comparable with uninstrumented A/A timings.

[Plan](PLAN.md), [instrument patch](instrument.patch), [freeze](freeze.json),
[runner](run.py), [manifest](manifest.json), per-cell function-count summaries and
build/runtime stdout/stderr preserve method and evidence. CPU MCP ask retrieved no
relevant instrumentation passage. Mechanics come from the inspected installed public
profile/instr_prof_interface.h, whose dump API prevents a second dump at process exit.

Decision: execution-count diagnostic complete. No scan time profile, PMU, stable
frequency, or independent confirmation gained. Source selection NONE and prior PARK
decisions unchanged. Backend/model/token costs unknown.
