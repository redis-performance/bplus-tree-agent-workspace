# COUNTERS-001 — scoped Clang execution counts

Sampling inspection failed in SCAN-PROFILE-001. This uses the program's own Clang
source instrumentation instead; no permission escalation or process inspection.
It measures execution frequencies, not CPU time, cycles, stalls or hot-path cost.
It cannot on its own establish a bottleneck or replace required time-profile validation.

Inspected installed Clang17 public profile/instr_prof_interface.h: reset_counters zeros
counters; dump writes a snapshot and prevents exit from dumping again. Separate isolated
harness inserts reset immediately before the wall-clock operation loop, then dump after
wall/thread/CPU/QoS observations and before semantic verification/cleanup. Source
src/zset_btree.c/.h unchanged. Reset/dump declarations come from the installed header.
No coverage binary participates in timing comparisons; its CSV times are noncomparable.

Fixed three serial cells: scan16, scan320, lookup-hit16; size100000, seed1, ops1000000,
ten warm-up passes. Source instrumentation -fprofile-instr-generate -fcoverage-mapping
on the same -O3 compiler/flags. One process per cell, timeout120s. Save profraw/profdata
and complete export in ignored scratch, public function-count summaries plus hashes,
commands and stdout/stderr. No timing-based pass criterion or optional repetition.
Check reset boundary by absence of insertion/deletion calls; check lookup entry count
and scan callback count against effective CSV operations. Retain failures as evidence.
CPU MCP ask retrieved no relevant instrumentation passage; use local public API docs,
not unrelated retrievals, to justify reset/dump mechanics. No performance claim.
