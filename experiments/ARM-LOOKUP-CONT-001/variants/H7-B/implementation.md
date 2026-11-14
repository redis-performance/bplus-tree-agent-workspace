# H7-B — exact masks for member and reference lookup

Correctness-ready; target ARM codegen and performance gates remain pending. No
candidate is selected by this report. The isolated starting commit is
`e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, original source
`16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
Frozen candidate source is
`ce8ed5476d5b04953e514a1a798947272a4ab2846034d417fe1e7e0b25e080eb`;
`candidate.patch` is
`6d28bf50be1c9364f110968a1c00416996c81c4ba574c5aa39f48b25002689e5`.

Only `current/src/zset_btree.c` changes: a named inline
`zbtIndexExactTagMask` is added, and `zbtIndexTableFind` plus
`zbtIndexTableFindReference` consume it without rereading their stored tag byte.
The original approximate helper remains unchanged for Boolean vacancy tests and
scan users. Leaf equality/decoder, hashing and zero-to-one folding, home filter,
probe order, IDs, tombstones, insertion hints, migration/free-ID checks, reference
repair and optional outputs remain as before. No H1–H6 patch, hint, prefetch,
SIMD, batching, fixture or flag change is included. A/C implementations were not
read. `scope-audit.json` checks the untouched helpers and exactly two new callers.

For `x = tags XOR broadcast(tag)` and `L = 0x7f7f7f7f7f7f7f7f`, the result is
`~(((x & L) + L) | x | L)`. Each byte of `x & L` is 0..127, so adding127 gives
127..254 with no inter-byte carry, including the most significant lane. The sum's
high bit is zero exactly when the low seven input bits are zero. OR with `x`
rejects a set original high bit, and OR with `L` removes all lower result bits
after complement. Thus a high result bit means exact byte equality. All operands
are unsigned64-bit; broadcast multiplication fits, and mask enumeration keeps
the existing guarded nonzero `ctz` and ascending numeric slot order. This does
not introduce host-endian memory interpretation or a wider load.

## Correctness

`run-correctness.sh` passed with its complete logs retained:

* Original57 native and57 ASan/UBSan tests, plus36 fixture cells across native/
  sanitizer, all six cases and seeds17/29/43.
* Supplied output oracle90000 and external-record oracle45000 checks under
  ASan/UBSan, including signed-zero scores, reversed leaves and optional outputs.
* `mask_oracle.c`:3507872 masks and4681407 enumerated lanes per native/sanitizer
  build. Every tag, possible byte and lane is checked against scalar equality,
  with both matching and nonmatching other lanes. Every adjacent XOR-byte pair
  is exhausted in each of seven lane pairs under tags0/1/127/128/255, with borrow
  and high-bit backgrounds;100000 deterministic mixed words supplement these.
  All tags are not crossed with all adjacent pairs; XOR translation and the byte
  proof explain that dimension.987938 tested masks expose approximate false
  candidates. Zero-mask extraction is never called, and all-match enumeration,
  no matches and folded-zero semantics are checked.
* `index_oracle.c`, reused from this implementer's prior H4-B correctness work,
  passes on candidate and original baseline in native and sanitizer builds:
  131584 filter checks,222 hits,24 misses,222 reference checks,126 wrapped hits,
  111 wide-ID hits,12 tombstone/hint checks,16 migration lookups and4 final resize
  steps per build. It covers full-hash collisions with distinct members,
  folded0/1 tags, high tags, displacement and narrow/wide storage.
* `reference_oracle.c` passes both builds:4 synthetic repairs and4668 mutations,
  including28 updates while resize is active and3952 cross-leaf updates. The
  targeted borrow adversary gives the false approximate lane the requested ID,
  then verifies repair changes only the true matching tag/ID entry. Its negative
  lookup preserves output sentinels. Public binary-member updates/deletes check
  full tree/index invariants after every mutation, using real IDs above70000 in
  the wide run and explicit growth/shrink resize rounds.

No source-correctness or sanitizer failure occurred. The first static-build
command mistakenly selected an existing directory as its output filename. The
linker rejected it (`static-baseline.build.stderr`); no executable ran. The v2
command changes only the output filename and records exact commands. This build
failure is retained; no source or compiler-flag repair was made.

## Static feasibility and remaining gate

Unexecuted local x86-64 GCC13.3.0 `-O3` ELF disassembly is saved for both raw lookup
and reference lookup. Both raw prologues push the same six registers including
frame pointer and subtract0x88; no frame growth appears. Native text is101058
baseline bytes and100330 candidate bytes, from `size`, not a runtime measurement.
Exact ELF hashes are in `manifest.json`; full disassembly remains in the isolated
ignored build directory. No out-of-line exact-mask helper is generated.

On the stable narrow raw path, baseline candidate extraction at `d9d1` is followed
by result copying, low-three-bit masking, a variable shift of stored tags, division
by8, byte comparison and a branch before ID load `d9e6`. Candidate extraction at
`db82` goes through division by8 directly to the same-width ID load `db8a`.
The reference function likewise loses its candidate stored-tag comparison.
Existing leaf/migration byte comparisons remain and are not this recheck.

The baseline zero-mask computation after XOR has independent NOT and subtract
branches joined by two ANDs; the candidate uses AND, ADD, OR, OR and complement
in a chain. This lengthens the per-bucket mask dependency by about two arithmetic
steps in this emitted x86 sequence, while removing the dependent candidate-tag
extraction/comparison branch. Constants, spills, full fallback costs and the
more expensive no-match mask still matter. The home filter and unused-slot
fallback stay present; reference vacancy checks still use the original approximate
Boolean helper. Local code supports target static review, not an ARM speed claim.
ARM exact native/LTO binaries, no-score paths and the chair's full static rejection
criteria have not been checked by this worker. They must pass before timing.

## Provenance and TMA

Public role: H7-B implementer. Own enabled-tool discovery found no callable
cpu-perf/library_status tools. The actual controller `mask-classifier-consult`
shared in `H7-selection.md` covers the mechanism and risks, with3/287 sources and
158 passages; its unrelated retrieved passage does not support a speedup.
This is shared evidence, not a consultation performed by this worker. Backend
details remain private; exact token costs are unknown.

Baseline and candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring
and all child shares are unavailable for this implementation: no profiling/TMA
was collected. No local timing, instruction measurement, benchmark, fleet access,
commit or push was performed. Correctness and static analysis authorize only the
next review gate; they do not establish a performance result.
