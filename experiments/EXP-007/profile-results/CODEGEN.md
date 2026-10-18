# EXP-007 release code-generation inspection

Read-only inspection before candidate timings, by delegated agent
`/root/proposal_b`, 19 October 2026. Exact backend/model and measured token cost
are unknown. No build or timing was performed for this inspection. The reviewer
implemented B earlier, so this is mechanism inspection, not independent
adversarial approval of B.

The saved release assembly supports the intended mechanism: candidate width
classification occurs outside each range's score loop, and the selected
noncrossing loop has no ninth-byte load/check. Packed loads, score conversion,
output stores, and subsequent checksum loads remain. These observations do not
establish a performance win or prove why a future timing difference occurs.

## Dispatch and loops actually generated

- **Control:** scalar decoding inlines into `decoder_batch`. Its score loops
  retain the per-score width/offset tests, including the possible ninth-byte
  load. For example, `LBB56_15` and its following blocks load width, select the
  physical position, load the word, test the bit offset and potentially load
  byte 8. The main unrolled loop starts at `LBB56_26`.
- **A:** the bulk helper inlines. In leaf-loop block `LBB57_7`, a width load,
  subtraction of 61 and range comparison classify widths 61..63; subsequent
  blocks handle zero and width 59. This occurs at loop depth 2, before score
  loops at depth 3. The crossing path retains scalar decoder checks. Separate
  noncrossing loops omit that scaffold. The compiler generates multiple
  unrolled/direction paths; this is not a single shorter instruction sequence.
- **B:** the bulk helper is outlined. `decoder_batch` calls
  `_zbtScoreLeafDecodeRange` once inside the leaf loop with `start=0`, the
  fixture count and a stack output pointer. The [saved helper](B-helper.s)
  checks zero count/width, tests `width & 7`, then compares width with 59 and
  60 before entering its score loops. Aligned forward/reverse loops are
  `LBB56_15`/`LBB56_14`; they use a byte stride and lack bit-offset arithmetic.
  Noncrossing forward/reverse loops are `LBB56_19`/`LBB56_18`, with word loads
  and variable shifts but no ninth-byte path. The crossing loop at `LBB56_7`
  retains the original offset check and byte-8 load. Direction was unswitched
  by the compiler for the simple loops. B's call/return and smaller loop bodies
  are meaningful context differences, especially for short ranges.
- **C:** the bulk helper inlines. At `LBB56_7`, `and width, #3`, `cmp width, #59`
  and `ccmp` classify crossing geometry before either score loop. The
  noncrossing loop at `LBB56_13`/`LBB56_12` contains word loads and shifts but
  no ninth-byte load; its unrolled counterpart is separate. The crossing loop
  at `LBB56_20` retains the original scalar path. Width classification is
  outside these loops even though orientation work remains inside some paths.

Block numbers are local to each assembly file; matching numbers in different
files do not identify the same code.

## Materialization and vectorization

All four versions write decoded score bits to the stack output array, then
reload it after the materialization compiler barrier. Control, A and C have
visible `str x...` output stores within their inlined decode loops. B passes
`sp + 16` as the helper's output pointer, and the helper emits `str x..., [x3],
#8`. The barrier emits no machine instruction. The following checksum loops
use `ld4.2d`, vector integer additions and reductions for long ranges, with
paired/scalar loads for tails. Thus the checksum consumes stored results; the
compiler has not reduced the benchmark to a precomputed constant or discarded
the decoder.

A/C, and B's outlined helper, contain vector stores for repeating the constant
zero-width score (`stp q0, q0`). These instructions do not demonstrate vector
decoding of nonzero packed scores. The nonzero decode paths inspected use
scalar word loads/shifts and scalar result stores. SIMD checksum reductions
are common to all variants and must not be described as candidate-specific
packed-decoder vectorization.

The round and leaf loops remain in every `decoder_batch`. Repeated rounds
therefore still invoke the decoder, materialize the scores and consume them.
This is a warmed throughput kernel with output storage, not the original scalar
iterator or a dependent-latency measurement.

## Static inventory and provenance

The inventory in [codegen.json](codegen.json) counts instruction-shaped lines
with operands, not executed instructions or exact text bytes. In particular,
the simple counting pattern does not count operandless `ret`. It gives:

| Variant | `decoder_batch` inventory | Additional timed helper inventory | Decode placement |
|---|---:|---:|---|
| Control | 420 | 0 | Inline |
| A | 853 | 0 | Inline |
| B | 212 | 145 | Outlined |
| C | 672 | 0 | Inline |

B's caller-only 212 cannot be compared with the other complete inlined bodies
as though it were all of B's timed code. A/C have more static code and more loop
versions. Neither code size nor a static branch count predicts elapsed time;
instruction-cache behavior, dispatch/call overhead and scheduling are unmeasured.
All callers retain the compiler's cold stack-check failure call. B's helper has
no calls. No instruction/cycle PMU counts are supplied by this inspection.

SHA-256 values were recomputed for all four full files and their saved batch
excerpts and matched `codegen.json`:

| Artifact | SHA-256 |
|---|---|
| `build/exp007/base/kernel.s` | `d2b0f1d510e45fca6b44cafc54355198a4cd7d06a7a3c1db37ebe11f97aed586` |
| `build/exp007/A/kernel.s` | `daf6385bde5793bad83e92d44383a570fe6f71b942f9deef8507680503b1e623` |
| `build/exp007/B/kernel.s` | `d00ad1ad98e36008e895cbb2cd63ab7ce214fe8e68f5396f93b8f2a56b82737b` |
| `build/exp007/C/kernel.s` | `2f613127557b37aba8b82197cab539fd74868bda34f0e036a6883451e21d1bc0` |
| `base-decoder_batch.s` | `453485804d7d721e7d2c00fce51ac96db847d308558c81ccf467ee0e32e6f7bd` |
| `A-decoder_batch.s` | `bf745aeb5dff70240f81887469be3d8e31d3088be85ddfd4b610ed76e4df9fc3` |
| `B-decoder_batch.s` | `f284a0d97391ad0ccb9ee265a002c551aad42f9211538ffb8c6a0050fa621295` |
| `C-decoder_batch.s` | `2e960f557a14f146f19d99c1421d84f2617ace35809b52dabca3b14b184ca8e1` |
| `B-helper.s` | `b28df9f9ad635ed020deb7dd80bbff81f76d94d51516363207c016abffde4896` |

`B-helper.s` was extracted from its symbol through its `Lfunc_end` label,
removing `.loc`, `.cfi_*` and `;DEBUG_VALUE:` lines and trailing whitespace.
Like the saved batch excerpts, it is an inspection excerpt, not a standalone
assemblable translation unit. Full assembly remains in ignored build storage.
