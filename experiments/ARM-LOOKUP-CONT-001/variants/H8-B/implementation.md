# H8-B — checked packed-record decoder for lookup

Correctness-ready, with local static feasibility established. Exact ARM native
and target LTO codegen remain pending; no performance/adoption decision follows.
Starting commit is `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, source
`16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
Frozen candidate source:
`24151adc87c1c7c7262adfc360b2b2e7ae662320050c60f1014889bf7c8f5040`.
Patch SHA-256:
`68e1be5f08266af66c77dab01554faeeaba439468fbdca7078a351d471155ecc`.

Only the isolated `current/src/zset_btree.c` changes. A named static-inline
`zbtPackedLookupData` returns eligibility plus payload/length. It classifies the
actual header's entire ordinary range0–253 first, then extended-inline254, then
external255. External full-hash mismatch returns false before reading or
asserting the pointer, leaving its output arguments unchanged. Accepted external
records retain the nonnull assertion and the original length decoder. The leaf
helper uses this eligibility result to advance the original `memchr` traversal;
its length/variable-`memcmp` equality and complete successful-output block remain.

The generic `zbtPackedData`, external accessors, index finders, filter, record
format, score/offset/tag layout and ownership are unchanged. There is no forced
whole-leaf inlining, new runtime boundary, comparator, query-length shortcut,
SIMD, batching, prefetch, branch hint, flag change or stacked candidate. The
scope audit verifies the unchanged functions and frozen referees. No A/C draft
or implementation was inspected.

## Correctness evidence

The unchanged qualification script passes57 native and57 ASan/UBSan tests, plus
36 fixture cells: six cases × seeds17/29/43 × native/sanitizer. Both supplied
ASan/UBSan oracles pass90000 output checks and45000 external-record checks.
`run-correctness.sh` records all commands and logs.

Focused tests run against both original baseline and candidate, in native and
ASan/UBSan builds. They are adaptations of this implementer's earlier H3-B/H6-B
correctness fixtures; no earlier implementation is imported into the source.

* Final `record_oracle.c` results:974932 output checks per build,17496 guarded
  short-record fixtures,9 exact-end heap fixtures,36 collision arrangements and
  260 representation/length cases. These cover every ordinary header0–253,
  inline254/255/256/319, external320/384, every byte mismatch position in each
  length case, unequal lengths/equal prefixes, binary zero/high bytes, all four
  output modes, signed-zero score bits, reversed physical order, empty leaves,
  unaligned records/queries, and inaccessible leading/trailing pages. The
  length-mismatch check uses an inaccessible query to prove no payload read is
  needed before rejecting the length. Short records exhaust address residues
  modulo16; large boundary records use guard-ended layouts, not every residue.
* Same-tag/full-hash collision candidates do not bypass equality. External
  short/empty representations remain distinct from ordinary headers. A rejected
  external record containing NULL leaves outputs unchanged. Another external
  record ends immediately after its header/hash, with length/pointer fields
  inaccessible: hash mismatch still returns normally. A matching external NULL
  deliberately violates the unchanged contract in a forked child and must end
  with SIGABRT, even for length0. All four baseline/candidate builds produce that
  expected assertion; retained `record*.stderr` lines are test evidence, not
  unexplained sanitizer failures. Core dumps are disabled in those children.
* `mutation_oracle.c`:1541 full tree/index invariant checks,2209680 optional-output
  lookups,108 allocation relocations and736 observations of reversed leaves per
  build. Mixed-length inserts and score moves, compaction, duplication, active
  resize plus defragmentation, deletion/merge, rank deletion and alternating edge
  pops preserve exact scores and lookup results. External short/empty ownership
  is checked through actual writer, compaction and duplicate paths.

All baseline/candidate result counts agree. No source correctness, build or
sanitizer failure occurred. The first record suite passed972856 checks; a coverage
audit added unequal-length/equal-prefix checks across every large representation
case, producing the final974932. Earlier passing logs remain, with final record
logs explicitly named `record-v2`; only those tests were rerun after that test
addition. Candidate source was unchanged. `run-focused.sh` and
`run-record-v2.sh` reproduce the focused checks.

## Local static feasibility and hazards

Saved unexecuted x86-64 GCC13.3.0 `-O3` ELF assembly includes both leaf variants and
the raw caller. The ordinary path of the candidate leaf clone loads the actual
header at`305d`, compares against253 at`3067`, then branches at`306b` directly to
the length comparison at`3090`. Header254 is tested only on the nonordinary arm
at`306d`; the extended record retains its uint16 length read and record+3 payload.
The generic leaf has the same range-first shape at`31fe`/`3204`. Baseline leaf
clone instead compares255 at`3f86` and254 at`3f8f` on the ordinary path.

There is no `zbtPackedLookupData` symbol/call or indirect jump table. Both leaf
variants keep `memchr`/variable `memcmp`, the existing score helper call when
requested, and their original boundary. Each leaf frame still subtracts0x48
with the same saved registers; the raw frame still subtracts0x88. Whole text is
101058 baseline bytes versus101106 candidate bytes (+48). Exact local ELF hashes,
compiler string and frame figures are in `manifest.json`; these are static file
observations, not performance measurements.

External fallback now crosses two representation decisions instead of the
baseline's first255 decision: **one added necessary classifier**. Extended-inline
crosses two decisions as before. No redundant third marker check appears. The
external full-hash comparison at`3078` and rejection branch at`307b` precede the
pointer load at`307d`, nonnull test at`3081`, and length load at`308a`. The change
therefore preserves early rejection in this local compiler; exact ARM builds
must establish that ordering independently.

Primary gain may still fall below2%. External-path overhead and code-layout
effects must satisfy the original1% guards and may reject this candidate.
Maintaining a lookup-only decoder duplicates the three record interpretations;
future format changes must update both checked and generic decode paths. This
maintenance cost is a reason to prefer the smaller scope if another independently
validated implementation ties. No source rescue based on later codegen or timing
is proposed. No memory/layout/allocation change exists in the patch; fleet memory
acceptance remains a separate unexecuted gate.

## Consultation and TMA

Public role: H8-B implementer. Own enabled-tool discovery found no callable
cpu-perf/library-status tool. The controller's actual shared mask-classifier
consultation, described in root `H8-selection.md`, covered this separate mechanism;
coverage3/287 sources and158 passages retrieved no supporting causal or speed
passage. This worker did not perform that consultation. Detailed backend
provenance remains private; exact token costs are unknown.

Baseline and candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring
and child-category shares are unavailable/uncollected for this work. No pipeline
cause is inferred from local branches or frame sizes. No benchmark, timing,
profiling, instruction measurement, fleet access, commit, push or publication was
performed. Correctness readiness permits exact target review only.
