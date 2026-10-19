# Independent Intel iterator-cache pre-screen review

Root reviewed source/header patches independently of the implementer. Exact model
and token/USD cost are unknown. This is static review, not a new correctness run.

| Variant | Patch SHA256 |
|---|---|
| A | `aff88760ed68d8c09c6cad1ebbd1ac0474da9d427dfe879d76c6d992528359c8` |
| B | `8ec11ac9b68af3a4aa7d80b41545a3b6428915ad77722710cb4ac0ba69f7be2f` |
| C | `032dd5a8908aada4cb5c3f57fdb2e64a2ee7d6f7c5e7dab3c11970535b5a07f2` |

No semantic blocker found under the existing valid-iterator contract:

- All11 leaf assignments reset the cache: successful/failed rank, score and lex
  seeks, empty trees, starts and both leaf-transition directions. Lex sentinel
  paths call Start or the resetting failure path. Direction changes within a leaf
  do not change its offset-array base.
- Lazy initialization occurs only for member/length output. The original physical
  position and packed-record decoder preserve reversed leaves, binary lengths,
  inline/external members and the external-pointer assertion. Score-only/all-null
  output paths leave the cache unused.
- B/C's zero sentinel differs from every valid array base after the leaf header.
  The relative byte offset fits the fixed4095-byte leaf bound; C statically checks
  UINT16_MAX. Alignment and host-native offset-array encoding remain unchanged.
- Copying a valid iterator copies consistent leaf/position/cache state. Mutation
  still invalidates it. Reinitialization clears stale state; no lifetime extension
  or mutation-safety claim is made.

A grows iterator state16→24bytes on the measured64-bit target, an explicit8-byte
cost per live iterator distinct from tree-owned memory. B/C remain16bytes there
using padding.32-bit sizes remain unmeasured. Every consumer/referee must compile
against its matching candidate header; reusing a16-byte driver object for A would
be invalid and is explicitly excluded by the plan.

New tests should poison state before successful/failed seeks, copy initialized
iterators, change output masks/directions, cross leaves and reinitialize after
mutation, preserving exact finite score bits and binary/external members. Existing
checks remain unchanged. The worker's successful validation is still required.

The100K primary A/A fails while1M qualifies, so the screen is exploratory. Full
performance guards still need score-only/count-only traversal, iterator setup,
mutation and range-deletion paths that construct iterators internally. Static
review and tree-memory equality alone cannot justify acceptance.
