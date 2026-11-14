# Fixed native lifecycle correctness check

Preparation only. This is a distinct baseline correctness diagnostic, not an
optimization candidate, timing experiment or extension of the completed census.
The original 93-file census freeze remains unchanged. Its generated source,
shadow header and clock-denial source are copied byte-for-byte here; existing
instrumentation bounds and the original production leaf search remain intact.
The fixed-query census is never enabled.

One native process accepts no arguments. Hash seed is 17. Create 2048 unique
binary members with length selected by ID modulo 3: 16, 128, 384. Byte j initially
equals `(ID*17+j*29+0x5a)&255`; bytes 0–3 encode ID little-endian; bytes 7 and 11
are zero. Scores are ID+1. Insert in ascending ID order through the original
FindForAdd/InsertNew APIs, preserving returned insertion positions. Caller-owned
bytes are regenerated and checked at every model checkpoint.

Delete exactly IDs 0,2,…,126. Require positive slot-zero ID writes, invalidations,
stale hints and unchanged hints. Audit every enabled hint in both current and
receiving tables, applying original ID/free/migration eligibility before access.
Staleness compares the copied seed hash/length/bytes against the current physical
record, with external hash rejection before pointer decoding. Every eligible hint
also calls the original full leaf search. A matching physical record must agree
with original score and logical-position outputs. Direct audit uses the seed as
its query; it does not claim all arbitrary-query terminal combinations.

Duplicate immediately without intervening public lookup. Require distinct table
generations, exact full hint-array copying including stale hints, and no reseeding.
Audit before public verification, because ordinary reads may advance rehash.
Derive ranks 512–1536 from the independent alive-ID model before deleting that
inclusive range on the original: exactly 1025 victims. Require old table retirement,
a new generation and positive Rebuild-origin seeds. Every freshly rebuilt hint
must be eligible, unchanged and successful; none may be stale or out of range.

Keep exact bounded snapshots of the duplicate's generations and full hint arrays
around the original's range deletion and destruction. Verify the original's 959
survivors and the duplicate's unchanged 1984 members. Free the original, reverify
the duplicate, then free the duplicate and all caller-owned buffers. Success is
printed only after zero live generations and absent query/table/seed contexts.

Seven ordered checkpoints are fixed: inserted, deleted, dup_original, dup_copy,
rebuilt_original, rebuilt_copy, freed_original_copy. Each checks all 2048 membership
and score answers, forward/reverse ranks, forward/reverse iteration, exact bytes,
score object bytes and unchanged negative score sentinels. The vector model is
independent of tree outputs. Each checkpoint performs exactly 8192 public lookup
operations; total verification lookups additionally include the eligible hints
from all seven checkpoint audits and the two immediate duplication audits.
The checker rederives that exact count and enforces the 65536 bound.

Other hard bounds remain 2 live sets, 16 live table generations, 1024 buckets per
table, 4096 lifecycle events and 384 bytes per seed snapshot. The existing census
event arrays remain empty. Capacity, coverage, model, sanitizer-independent C
assertion, build or review failure means INCOMPLETE, with no adaptive input/bound
change or retry. Native only is declared; no sanitizer, compiler comparison,
defrag, high-ID, forced-address-reuse or active-resize coverage is claimed.

Build from the checkout root with
`sh experiments/ARM-LOOKUP-CONT-001/slot-lifecycle-check/build.sh OUTPUT_DIR native`.
The output directory must not exist. `TASK_CC` selects the compiler; flags are
`-O3 -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`. Build never runs
its output. The binary is `OUTPUT_DIR/lifecycle`, invoked without arguments.
Static admission is `python3 .../slot-lifecycle-check/validate_static.py OUTPUT_DIR`;
raw admission is `python3 .../slot-lifecycle-check/check_output.py SAVED_STDOUT`.
One complete JSON record is required. Unknown fields, duplicate keys, wrong
integer types, missing stages, impossible lifetimes and incomplete cleanup fail.

`DEPENDENCIES.json` maps experiment-relative input paths to hashes. Validation
rehashes all prior 93 files and the copied inputs. Build receipts bind actual
ELF, assembly, symbols, compiler, harness, helpers and dependencies. Static review
checks all 13 clock-denial bodies and the retained original leaf-search call CFG.
No timer exists in the harness, and no C program has been executed locally.

Eight Python synthetic/static tests pass, including wrong-but-plausible model,
freshness, duplication, lifecycle, cleanup, schema and count failures. The initial
draft and pre-freshness source/checker snapshots are retained. Native compile-only
evidence is `STATIC-VALIDATION-v2.json`; no failed compile or C execution occurred.
Independent source and target review remain separate gates.

Source/schema freeze cutoff: 06:15 UTC. Independent source and target review:
06:30 UTC. At most one owned-Intel execution must finish before 06:45 UTC, otherwise
INCOMPLETE. ARM remains released. The controller owns operational admission and
cleanup; this preparation authorizes no fleet action. Actual freeze time and the
complete packet are pinned separately. No speed prediction or source adoption
follows from any result.

Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and their children are
unavailable: no performance profiling is part of this correctness check. The
shared consultation supplied no supporting passage; no independent consultation
or performance evidence is claimed here.
