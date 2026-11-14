# H8-A — local range-first record decode

Status: **correctness ready; local static mechanism present; exact ARM admission pending**. Implementer role: local record-classification implementer. Baseline commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream freeze `ee8e7f70152404649ac947157fd662d11b4a00d5`. No H8-B/C draft or implementation was read. No timing, profiling, instruction-count measurement, fleet access, commit, push or external publication occurred.

## Source freeze

Candidate SHA-256: `e63caad0a6f81066a67ff964333cf0391c4a2ba71b592ce335bedefbd289f7f0`.
Baseline SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.

[implementation.patch](implementation.patch) changes one block inside the existing `zbtScoreLeafFindMember`. Actual ordinary headers below 254 directly supply length and `record + 1`. The remaining branch performs the original external full-hash rejection, then calls the unchanged generic decoder. The scanner, record offset/header storage, external ownership, memcmp condition and success-output block are unchanged. Generic decoder users, index/filter/resize logic and helper boundaries are unchanged. No prior candidate patch is stacked.

[source-verification.json](source-verification.json) verifies that this exact single replacement reconstructs the candidate from the baseline byte-for-byte and records source/referee/static-ELF identities. No source revision followed testing or codegen inspection. `git diff --check` passes.

## Correctness

GCC 13.3.0, Ubuntu 13.3.0-6ubuntu2~24.04.1. The unchanged `qualify.sh` completed successfully; fixture runs used its clock-free `verify` path. All parent test processes exited zero with empty stderr. The new representation oracle deliberately verifies one child assertion per run, described below; that expected child abort is not a test failure.

| Check | Result | Evidence |
| --- | --- | --- |
| Original native tests | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Original ASan/UBSan tests | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Original native fixtures, six cases × three seeds | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same sanitizer fixtures | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Supplied output oracle, sanitizer | 90,000 passed | [output_oracle-sanitizer.jsonl](output_oracle-sanitizer.jsonl) |
| Supplied external oracle, sanitizer | 45,000 passed | [output_external_oracle-sanitizer.jsonl](output_external_oracle-sanitizer.jsonl) |
| Representation oracle, native and sanitizer separately | Each: 6,257,596 checks; 23 early-rejection scenarios; one expected nonnull assertion | [representation_oracle-native.jsonl](representation_oracle-native.jsonl), [representation_oracle-sanitizer.jsonl](representation_oracle-sanitizer.jsonl) |
| Mutation model, native and sanitizer separately | Each: 5,546,600 model checks, 2,383 checked states, 1,750 mutations, 640 relocation callbacks | [mutation_oracle-native.json](mutation_oracle-native.json), [mutation_oracle-sanitizer.json](mutation_oracle-sanitizer.json) |

Both new oracles were also compiled and run against the unchanged baseline in native and sanitizer modes. Their complete result rows match H8-A byte-for-byte. All 36 candidate fixture rows match the saved baseline rows, including owned bytes. These are correctness/memory observations; they do not qualify a performance or fleet-memory result.

[representation_oracle.c](representation_oracle.c) extends the prior bounded-range oracle with independent expected presence, position and exact signed-zero score checks. It covers every ordinary header 0–253 and every inline length 254–319, all four score/position output modes, three binary patterns, mismatches at every payload byte and unequal-length equal-prefix queries. Source and query alignments each cover residues 0–7, with a fixed pairing rather than their full Cartesian product. Exact-size source allocations expose overreads to ASan. Every inline length also has record and query placements ending at protected-page boundaries; empty payloads use nonnull one-past pointers and must perform no byte access.

Every inline length is checked with both singleton physical orientations. Separate five-entry same-tag fixtures test meaningful physical/logical reversal and skipping wrong-hash, wrong-length and wrong-content records. Existing full reversed-leaf and empty-leaf cases remain. Full-byte equality is still evaluated by the existing variable-length comparator; this test does not introduce a substitute production comparator.

External guard cases include lengths 0, 1, 7, 8, 253, 254, 255, 256, 319, 320 and 384, including externally represented short/empty records, both orientations and protected-page-ended external payloads/queries/record fields. Full-hash-equal wrong-content comparisons and same-tag full-hash mismatch rejection are explicit. Wrong-hash records with null pointers must skip pointer validation. A further record exposes only its marker and four hash bytes before a guard page; a mismatching hash must reject without touching length/pointer fields. Finally, a matching-hash external empty record with a null pointer is checked in a child: it must terminate with SIGABRT and the original `ptr != NULL` assertion text. Core files are disabled for that child. This demonstrates both sides of the original validation contract.

[mutation_oracle.c](mutation_oracle.c) maintains an independent caller-owned key/score/live model for 600 binary members, covering every length 0–320 plus external 384-byte members. Its own score/byte/length comparator determines expected sorted order. Every insertion, score movement, deletion, reinsertion and edge deletion validates public raw lookup, untouched miss output, both iterator directions, exact member bytes, ranks, signed-zero/finite score bits and structural invariants. Alternate-end insertion, cross-order score updates, deletion/reinsertion, shrink-to-fit, duplication and defragmentation exercise records created and moved by the existing lifecycle. Each defragmentation step is checked; larger copied allocations force real pointer changes. The test finishes by alternating edge deletions until empty. It does not claim that every internal compaction/split branch was individually instrumented; the original upstream suite remains required.

Build arguments, return codes and binary hashes are retained in [oracle-runs.json](oracle-runs.json), [mutation-runs.json](mutation-runs.json) and [baseline-oracle-runs.json](baseline-oracle-runs.json). Candidate entries run from the isolated tree; baseline entries run from the original repository root, with `<H8_TREE>` expanded to the isolated tree for the test source/output paths. Literal local baseline arguments remain in private evidence. Representation native builds use O3, mutation native builds O2; sanitizer builds use O1 with ASan/UBSan and nonrecovering sanitizer failures. Added oracles use C11, debug assertions, frame pointers and warnings as errors with unchanged compatibility/SipHash sources. The original qualification flags are unchanged.

No runtime or compilation failure occurred. A passing earlier coverage version without explicit singleton reversal at every inline length is retained under `coverage-before-singleton-reversal/`; only the added test changed to close that coverage gap. All four final baseline/candidate native/sanitizer representation runs passed after the extension. The implementation source remained frozen.

## Static codegen observation

Built separate, **unexecuted x86-64** baseline and candidate lookup ELFs using the same local GCC 13.3/O3 flags: C11, `-g -Wall -Wextra -Werror -fno-omit-frame-pointer`, no LTO, unchanged lookup/compatibility/SipHash sources. The original relative source names were retained for both builds. These are local static artifacts, not fleet Intel or ARM performance evidence.

| Artifact | SHA-256 | Whole executable text bytes |
| --- | --- | ---: |
| Baseline ELF | `04b928e457a299f9e805a8580a0a563311de15e84789abb80e63794d2a3ef8d0` | 101,074 |
| Candidate ELF | `47bbc23a29629f06b28e903a28eb1485aa3974b37196a459f561f0962a4ef964` | 101,042 |

The [baseline leaf assembly](baseline-leaf-codegen.txt) checks header 255 at `0x3f86`, then 254 at `0x3f8f` for ordinary hits. The [candidate leaf assembly](candidate-leaf-codegen.txt) loads the header at `0x4034`, compares it with 253 at `0x403b`, and branches directly to length comparison at `0x4050` for the entire 0–253 domain. The original `memchr` call remains at `0x400e`, and bounded variable `memcmp` remains at `0x4066`. No new successful-path decoder call or indirect jump table appears.

Fallback costs are explicit: extended-inline records still pass two representation classifiers; external records now pass two instead of the baseline's first external-marker decision alone. At most one additional classifier is present on external hits. The external full-hash compare at `0x40b3` branches away on mismatch at `0x40b6`, before the pointer load at `0x40bc`; the pointer's existing nonnull assertion follows. The cold assertion-failure helper call already existed in the baseline and is not a decoder call on an accepted record path.

Leaf prologues have identical six pushes and 72-byte local reservations; [baseline](baseline-raw-codegen.txt) and [candidate](candidate-raw-codegen.txt) raw lookup prologues have identical six pushes and 136-byte local reservations. Thus neither local leaf nor raw frame grows. The 32-byte text difference is a static executable-size observation, not a speed or tree-memory claim.

This local compiler does not recreate the rejected two-classifier common path, so there is no local mechanism-based NONE. Exact native ARM and target LTO helpers/raw clones must still pass the independently applied selection gates before timing. A failure there must be preserved as NONE without broadening source scope, forcing inlining or changing flags. External/extended guard losses remain binding even if primary lookup improves.

## Consultation, TMA and limits

Own enabled-tool discovery found no callable cpu-perf/library_status endpoint. The controller's actual shared mask/classifier consultation covered this separate range-first mechanism, exact baseline marker tests, external-hash ordering and fallback risk. Its library remains revision `deb5a0bac467`, 3/287 sources and 158 passages; the retrieved sampling-register passage does not establish the mechanism's speed. These are shared controller calls, not calls made by this implementer. The source/control-flow contract and test evidence support evaluation; no retrieved causal support is claimed. Detailed backend provenance remains private; exact token/cost totals are unknown.

| TMA category | Qualified ARM baseline | H8-A |
| --- | --- | --- |
| Frontend_Bound | Unavailable: collector scope/formula/exclusion qualification absent | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

All child categories are unavailable. No pipeline cause is inferred from static code or another architecture. Exact ARM codegen admission, separately qualified fixed-work comparison, original ≥2% primary/≤1% guard and memory gates, ≥250 ms windows, Intel portability, affected-operation guards, fresh confirmation, matched profiles and independent acceptance review remain outstanding.
