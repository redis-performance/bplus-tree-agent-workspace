# EXP-005 retained mask algorithms — read-only inventory

**No hypothesis selected; no build or measurement.** EXP-005 remains PARK with source NONE. This inventory supports accurate review of forthcoming corrected native ARM baseline evidence; it does not revive the Apple experiment, requalify AMD's failed A/A or establish a new implementation population. The initial Intel019 mask expression was exactly EXP-005 A, as now explicitly corrected.

## Exact algorithms and validity domain

All three patches replace only the existing width mask in `zbtScoreLeafScore`, inside its unchanged `bits != 0` block. Valid encoded width is 1..64. The original cross-word predicate/load, physical reversal, score shift/base and ordered-to-double conversion stay byte-for-byte source unchanged.

| Variant | Retained expression applied to delta | Why defined for valid widths |
|---|---|---|
| A | `UINT64_MAX >> (64 - bits)` | Right-shift count is 0..63; width64 gives all ones without a shift64. |
| B | `((UINT64_C(1) << (bits - 1)) * 2) - 1` | Initial shift is 0..63. At width64, unsigned 64-bit multiplication wraps to zero and subtraction wraps to all ones; both are defined. |
| C | `UINT64_MAX >> ((-bits) & 63)` | `bits` is unsigned; modular negation followed by mask63 gives 64-bits for widths1..63 and zero for64. |

All yield the low-width ones mask. Width zero must bypass the expression: moving A/B outside the nonzero guard would introduce an invalid shift, and C would incorrectly yield all ones. No expression adds iterator state, changes ABI/layout, or allocates memory. A is the direct readable form; B's defined wrap and C's modular negation need explanation. This is semantic inventory, not a fresh maintainability selection.

Retained C-source hashes (complete exact SHA256 in inventory.json): control `d9123c82`, A `aa834a77`, B `e74a9a0d`, C `0960b038`. Each original patch is still in `experiments/EXP-005/variants/{A,B,C}/candidate.patch`.

## Original source, referee and decision

The freeze records base commit `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c` plus an **uncommitted isolated HARNESS-004 snapshot**, not a claim that the commit alone recreates every referee file. Its target C (`d9123c82`) and header (`496e72ff`) match corrected13e, while compatibility and benchmark inputs differ. inventory.json compares every recorded control input to exact `13e459ff8`; absent old additive files are explicit. Matching target source does not make old and corrected executables equivalent.

The original machine was Apple M1/arm64, macOS26.3, AppleClang17, libc, C11 `-O3 -g -fno-omit-frame-pointer`, unpinned serial measurement. Exact frequency, effective QoS and within-window placement were unknown. Three proposals/chair and three implementations were separate **sequential passes**, not independent agents. Fresh confirmation and final adversarial review were also by the coordinator, not independent participants. Historical instructions preventing publication are part of that original record; the present authorized inventory leaves it intact.

The additive HARNESS-004 referee uses exact score-bit checksums, member first bytes and lengths according to requested output masks, plus count; full member bytes/order are checked outside timing. Its integer scores are centered around zero. Current public microbench score-only iteration uses its original numeric checksum and nonnegative integer fixture. These have distinct consumer costs and fixture distributions. Neither old speeds nor old sample percentages transfer to the new ARM or AMD case.

AA-009 retained72 rows (six ABBA blocks each for masks0,4,7) at100K,16-byte integer members,20M visits, seed20101. Qualification required the six-block 95% interval wholly inside ±1%, plus minimum10ms windows and all invariants. It did not qualify masks2 or6. This is not the present overnight every-block ±1% rule; keep each contract with its own result.

Screening retained180 rows across all three variants and masks0,2,4,6,7. Mask4 is score-only primary;0 no output,2 length-only,6 length+score,7 all outputs. C was a provisional screening preference. Fresh216 rows tested all three variants on masks0,4,7 and two fixed fresh seeds; all failed the frozen primary confidence-bound requirement. No confirmed guard regression met that experiment's two-seed rejection rule, so final **PARK/NONE**, not acceptance or REJECT. Mask6 remained an adverse unqualified diagnostic for A/C; B's favorable mask6 observation does not establish a winner. No timing figures are imported here as a native ARM prediction.

Old static codegen found A/C iterator instructions equivalent after four panic-literal relocation normalizations, while full linked disassemblies differed. Both removed one mask instruction on that compiler; B did not reduce total iterator instructions. New corrected adapter code generation must be inspected afresh. Old A/C screening differences cannot justify intrinsic C superiority or selecting by a nominal instruction count.

## Retained correctness and limits

The validation driver ran control/A/B/C in native release and ASan/UBSan debug modes, 1096 build/test commands total, including original43 tests and128 mode fixtures per source/build. Mode fixtures used n129,16/320-byte binary members, integer/fraction/wide/zero encodings, both directions and all8 output masks; requests2n+1 verified3n visits. The larger HARNESS-004 referee qualification had640 fixtures per build across sizes1/31/32/33/129; do not describe those as640 rerun per EXP-005 candidate.

The retained independent scalar bitstream oracle spans widths0..64, valid width+shift combinations, ten counts1..96, two seeds and both physical directions, with poisoned padding, exact finite result bits and asserted crossing/fullwidth/zero/reversal coverage. It constructs expected bitstreams independently of the decoder. The current files match the original frozen oracle hashes.

The mutation oracle covers per-call output-mask changes, iterator copies, rank seeks, exhaustion sentinels, reverse flags0/1/−1/2, mixed insert/update/delete and diverse finite values including subnormals, extremes and signed zero. It reinitializes iterators after edits; it does not promise live iterator validity across mutation. Binary member lengths include empty and319/320/321 boundaries. The separate signed-zero oracle toggles exact ±0 bits through real updates, compares logical and physical decoding, checks rank/score/range, copies/deletes/edge deletion and actual reversed leaves. It settles incremental rehash before its read-only memory equality check; do not misstate that guard as timing active resize.

## Guard semantics required before any future native replication

A future authorization would need exact native source/referee/compiler identities, actual-binary profile mapping and fresh valid controls for the new schedule. Correctness should retain original tests and the above unchanged scalar/mutation/signed-zero oracles with native+sanitizer builds, exact width0/64 and cross-word reads, endian behavior, no NaN assumption, all output masks and both traversal/physical directions. All-common-score lexical seek is the documented valid lex setup; invalid mixed-score lex fixtures are not an appropriate oracle.

Performance guards must include no-output, length-only, length+score (historical unresolved adverse mode), all-output, both directions, fractional/wide/equal-score/signed-zero distributions, long/binary members and leaf transitions. The shared decoder also serves score lookup, rank/bounds, scan and mutation, requiring original-operation and memory guards beyond iteration. Existing code touches no state or allocation, but that is not a substitute for measured exact memory and mutation correctness. No full-output cache benefit may be carried into score-only evidence. Any added referee needs its own fixed semantic qualification and baseline precision; altering the checksum is a harness revision, not a tree optimization.

Broader guards, independent fresh confirmation and adversarial review remain acceptance gates; neither old local correctness nor forthcoming baseline profiling completes them. No repeated failed schedule, rebranding of old algorithms, retrospective source selection or host-pooled timing follows this inventory.

Author: actual participant `/root/aws_intel`; read-only inspection and local metadata hashing only. Exact backend/model, token usage and cost unknown. Original patches/plans/raw results unchanged. Await root's immutable ARM baseline evidence and review assignment.
