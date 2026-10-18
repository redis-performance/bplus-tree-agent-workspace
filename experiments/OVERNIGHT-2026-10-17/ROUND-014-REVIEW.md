# Round14 sequential adversarial review

Independent reviewer startup failed before execution (thread context unavailable).
This is the coordinator's separate read-only review, not an independent participant.
Exact backend/model/token costunknown; actual CLI usage belongs to the supervisor.

- **Semantics and ownership:** all mutations in new oracles use public APIs. Private
  reads require actual transition coverage; no resize cursor/generation is injected.
  Sorted-vector comparisons use binary lengths/bytes and exact score bits. Defrag
  callbacks copy all old usable bytes, move to distinct allocations, and obey separate
  start/step freeing contracts. Exact ownership summation and callback deltas are
  independent checks; clone/source free ordering checks copied ownership. This is
  not a global proof of leak freedom. Low-bit free markers are inspected, not freed.
- **Validity of new tests:** first lifecycle attempt incorrectly required a stale
  member cursor; source explicitly repairs it. Failed snapshot retained, new attempt
  asserts the correct successor. First mutation extension can decline header moves
  while demanding identity resets; stronger second intervention always moves headers.
  All prior checks and source assertions remain. The failed individual mutation
  counter was not printed; do not overstate the diagnosed component as measured.
- **Coverage sensitivity:** eight fault runs detect five new distinct defects plus
  three repeated controls. Premature reuse was already tested synthetically. Both
  active-relocation defects are repeated under fresh mutation schedules. Shrink
  orientation and zero-generation controls are new. No failed fault was hidden.
- **Branch evidence:** LLVM captures include complete oracle processes and setup,
  including calls from the read-only model; they are not CPU-time profiles. Actual
  repaired-member and retired-defrag paths differ. Shrinking fixture reaches normal
  EOF fallback; no captured schedule reaches a freed member-cursor fallback. Absence
  is not proof of unreachability. Initial source snippets mishandled macro file IDs;
  mapped-count files resolve them correctly without changing any count or execution.
- **Scope limitations:** generation wrap currently has baseline native/sanitizer only.
  Full models run at low water; high-water generation/length/leaf/deletion checks are
  narrower. Growth-side wrap and all retained variants are the next distinct scope.
  Physical fixtures may depend on allocation history, even though current outputs
  agree. Do not infer universal allocation geometry, memory savings or speedups.
- **Measurements and provenance:** no timing benchmark runs or precision threshold
  changes. No existing PARK is cleared. Four count captures are disjoint from all
  build/test windows. Source/support and all prior immutable evidence hashes pass;
  root source/referee unchanged. Uncommitted snapshots are not committed acceptance.
  No protected git retry, publishing, credentials, runtime/STOP or permission edits.

Read-only [audit](ROUND-014-VERIFY.json):120serial command windows, four captures,
2863hash checks, eight43-test cells, source/workspace/whitespace checks PASS.
