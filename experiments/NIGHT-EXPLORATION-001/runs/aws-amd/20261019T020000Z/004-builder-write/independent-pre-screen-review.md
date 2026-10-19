# Independent AMD builder-write pre-screen review

Root reviewed A/B/C independently of their implementer, against unchanged source
`8fab511e`. Exact serving model and measured token/USD cost are unknown. This is
static semantic and scope review, not independent correctness or timing execution.

| Variant | Patch SHA256 |
|---|---|
| A | `53c0f64f55e36d4613a43c2af9c6cea6bf3a7b3edb5e29077e8b28234b3ca9f0` |
| B | `4c73ef05e15ff3ee2dc07eab278297037d8a47ac774cd706d6f10af5c63ece73` |
| C | `3a8b430288d389ff325233686d50b11fc2a45fd61f1bc4f68f789de1a3a93ac4` |

No correctness blocker found before the fixed screen:

- A and B substitute the builder's fixed forward orientation and encoding locals
  for fields read by the generic writer. The header is zeroed and never reverses
  during construction. Encoding is unchanged, including ordered-bit minima for
  numeric-equal signed zeros. Zero-width fields still perform no data access.
- The word read/OR/write, little-endian conversions, crossing condition and ninth
  byte update are identical to the generic writer. The existing score allocation
  padding remains unchanged; neither patch widens access or introduces a shift by64.
- C completes the same generic score writes before member writes. The new leaf is
  separate from the still-live input arrays/old leaves. Record writes and external
  ownership transfers preserve their relative order and unchanged code. Offsets,
  tags and records remain outside the allocated score area. All debug assertions
  remain enabled and execute with the same source/build settings.
- No layout, allocation size, hash, index maintenance, public API or existing-leaf
  orientation behavior changes. Mutable target remains only zset_btree.c.

A has a minor documentation issue: its new helper sits between the detailed builder
comment and the builder declaration. Move it before that comment if A is selected;
this is not a semantic reason to discard the retained experiment patch.

The three planned frozen oracles supplement the original tests: public finite-score
and ownership boundaries, physical signed-zero/reversed-leaf checks, and independent
packed-decoder bit checks. Their successful execution is still the worker's separate
validation gate. Synthetic decoder checks alone would not validate leaf construction.

The profile suggests limited 1M headroom (3.31% scoped samples in the score writer),
so a primary gain is not assumed. Fresh A/A reportedly qualifies both primary cases;
the screen must retain all raw rows and exact operation/checksum/memory equality.
Each primary uses one million updates, which means ten passes at100K and one at1M;
these are explicitly different mutation histories, not interchangeable samples.
Fresh confirmation, full guards, mechanism profiles and final adversarial review are
still required for any later acceptance. Source adoption remains NONE overnight.
