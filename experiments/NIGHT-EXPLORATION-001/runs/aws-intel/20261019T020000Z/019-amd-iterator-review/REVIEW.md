# Read-only critique of corrected AMD score-only iteration

Current action: **NONE**. AMD's frozen 100K A/A fails its first block (+2.430913%); all six 1M blocks pass, but the contract requires both sizes. No retry, implementation population, runner workload or acceptance follows this review. The old Intel iterator-cache PARK and old SCAN REJECT remain final.

Evidence is AMD029 at commit `6d19f4df4`, exact corrected source `13e459ff8`, actual timing binary SHA256 `1ecbe6a426bd3a593a9fce6b8e8c6796c8c2287706fdd7eafdba595df9bad9ed`. The immutable input hashes and a small independently derived source-line aggregation are in evidence.json. This is a future-direction critique, not an independent reconstruction of all raw samples or an optimization proposal round.

## What the measured path does

The public referee requests forward score-only iteration: `zbtreeIteratorNext(&it, 0, NULL, NULL, &score)`, 50 million visited members, 16-byte keys, finite nonnegative integer scores. Actual timing assembly at `b7f7..b7fd` tests the member/length outputs and jumps over member record decoding to `b871`. The old Intel004 cache targets member-offset array address calculation in that skipped region. Its conditional full-output gains cannot be transferred to this workload; caching that address would add initialization/state work without removing executed score-only work.

There is material evidence in packed score decoding: exclusive sampled-period shares are 25.819%/29.350% for score decode at 100K/1M, plus separate 3.607%/4.032% ordered-to-score and 3.365%/3.866% physical-position shares. Iterator body is 22.980%/22.183%; those categories are exclusive, while same-IP inline-inclusive totals overlap. The caller accounts for 44.229%/40.568%. All sampled tree instructions match actual timing code, but caller mappings differ or are absent. This establishes a tree-code location worth inspecting, not a removable cost or expected elapsed improvement.

## One specific future mechanism worth code-generation inspection

Within the existing `bits != 0` block in `zbtScoreLeafScore`, the width mask is regenerated for each item. Actual `b8da..b8f6` builds a shifted all-ones mask, complements it and selects the all-ones result for width 64 before applying the mask. A possible future source-only simplification is expressing the mask as `UINT64_MAX >> (64 - bits)` for the established width range 1..64. This includes width 64 with shift zero and could remove the special-width select and some mask construction instructions while retaining the packed load/overflow-byte/score-shift logic unchanged. This is an algebraic direction for future compiler inspection, not a patch or a claim that Clang will produce faster code.

The supplied physical instruction map contains 104 events and sampled period 482,804,062 at source line 511, 8.669599% of the pooled 5,568,932,013 period across both sizes. The selected rows include the mask-width comparison and conditional move; evidence.json retains each exact PC, opcode and count. Source-line attribution and sampling skid do not assign this percentage as the mask's causal cost. Some instructions in the sequence have no samples. The large epilogue `pop` samples likewise do not justify blaming stack maintenance. No SIMD or member-cache conclusion follows.

This direction adds no iterator state and need not change tree-owned allocation or the 16-byte iterator representation. By contrast, caching per-leaf score metadata would create seek/start/leaf-transition reset obligations and possible ABI/state costs before evidence shows a benefit. A cache is not the direction identified here.

## Risks and missing evidence

The alternative mask is defined only when bits is in 1..64; it must remain inside the nonzero path, with the encoding-width invariant established. Width zero must still return the exact base score. Width 64, unaligned packed offsets, the extra overflow byte, endian conversion, reversed physical order, ordered-score reconstruction and exact finite/signed-zero bits must remain unchanged. The shared decoder serves lookup, updates, bounds, scan and iteration, so iterator-only testing would be inadequate. No change to supported inputs, assertions or frozen referee is justified.

Before any future population, inspect matching compiler output for actual mask simplification and census score widths/alignments/reversal under a separately approved diagnostic; current integer fixtures do not cover arbitrary fractional scores, equal-score leaves, signed zero, both directions, optional output combinations or reseeks. A new fully preregistered qualification must be justified independently, not rerun this failed schedule. Any eventual comparison needs all original-operation guards, exact score-bit and iterator oracles, matching memory, fresh confirmation and profile review against unchanged baseline. If code generation is unchanged, mask handling ceases to be a specific supported mechanism; select NONE rather than timing a cosmetic rewrite.

Authored by actual participant `/root/aws_intel`, read-only, with prior Intel004 cache authorship disclosed. No peer new proposal was required or manufactured. Exact backend/model, token usage and cost are unknown. No benchmark, build, source mutation or runner access was performed for this critique.
