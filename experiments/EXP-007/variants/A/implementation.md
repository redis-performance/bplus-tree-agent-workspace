# Implementation A: specialized simple loop with scalar crossing fallback

Agent `/root/proposal_a`, 2026-10-19. Exact backend/model and token/currency
cost remain unknown. This implements the chair's selected explicit bulk-helper
hypothesis, superseding proposal A's suggested scalar-only implementation.
No other implementation was read. No build or timing was run by this implementer.

Only `decoder.inc` is supplied as candidate code. The chair constructs isolated
source/build copies and records hashes and patches. Main production source, header,
allocator, tests, and shared referee are unchanged.

`zbtScoreLeafDecodeRange` dispatches once per invocation. Widths 59, 61, 62,
and 63 call the existing scalar decoder in a simple loop. All other widths enter
a non-crossing loop with no ninth-byte read or crossing predicate. Zero width
fills the exact base score. The non-crossing loop computes its mask once, including
the explicit 64-bit case, and reuses base, score shift, and orientation. Physical
position still uses the original helper, minimizing indexing changes.

This deliberately leaves the crossing-capable implementation unchanged rather
than specializing every combination. Distinct choice: scalar fallback plus a
single non-crossing loop; no indirect dispatch, cached iterator state, reverse
loop duplication, or manually unrolled output. The bulk operation materializes
the same output as the control under the identical shared referee.

The range is logical forward `[start, start + count)`, even for physically reversed
leaves. Zero count returns before reading leaf metadata or touching output. Inputs
must obey the control's range and disjoint-output contract. No new production API
or scalar-iterator improvement is claimed.

Correctness risks requiring the chair's unchanged oracle and sanitizers:

- The non-crossing classification must hold for every width, position, and partial
  range. Width 58 reaches at most offset 6; width 60 reaches at most offset 4;
  width 64 is aligned. All widths at most 57 fit with every possible offset.
- Full-width mask construction must avoid a shift by 64. Endianness stays with
  `intrev64ifbe`, and the existing allocation's permitted eight-byte load is retained.
- Zero width, score shifts, physical reversal, exact finite score bits, and signed
  zero must match the scalar decoder. Reconstruction uses unsigned arithmetic and
  the original ordered-score conversion.
- Output canaries must prove that zero count and subranges do not overwrite nearby
  output. Leaf bytes and tree-owned memory must remain unchanged.

Performance risks: crossing widths pay an extra once-per-range dispatch; short
ranges may not amortize it. Hoisted metadata does not by itself guarantee better
generated code. Compiler unrolling/vectorization and register pressure can dominate.
Inspect the resulting code and measure only against the same bulk materialization
control; do not compare these numbers directly with EXP-004's four-checksum kernel.
