# Advisory index-slot hint: admit diagnostic preparation only

No optimization implementation is selected. Three independent proposals examined a positive physical-slot hint in a member-index entry. This differs from the rejected negative-leaf cache: the hint would try a current record before the leaf-tag scan, and could never establish absence. H2 and Q4 remain PARK; the failed ARM controls stay closed.

| Proposal | Representation | Decision at this stage |
|---|---|---|
| [A](proposals-fifth/A.md) | Full-ID and transition audit; sparse filter storage considered as a separate tradeoff | NONE without representation and useful-hit evidence |
| [B](proposals-fifth/B.md) | A side bitmap permits conversion of at most eight entries in a bucket back to full IDs | NONE; allocator, transient-memory and lifecycle costs remain unproven |
| [C](proposals-fifth/C.md) | One slot-zero hint in the existing home-filter word; fold the filter into 56 low bits | Plausible bounded storage option, with weaker-filter and stale-hint costs; diagnostic preparation only |

The full narrow ID domain must remain intact. Bit 15 is not spare: an active narrow receiving table can accept IDs above 32767. No implementation may lower that legal range, force a new whole-table conversion, or relax the memory and mutation guards.

C identifies a concrete storage tradeoff without changing bucket sizes or adding an allocation. Fold the existing mask `M` to `(M & ((1ULL << 56) - 1)) | (M >> 56)`. Folding commutes with OR, so recording and testing the same folded masks preserves filter membership; it may add false positives. The high byte can then hold an advisory physical position only for index slot zero. Every filter consumer, including scan, would need the folded interpretation. This is a source-level representation argument, not verified target layout, timing, or guard evidence.

Seed only where existing copy/rebuild loops already know the physical position. A write to index slot zero invalidates the old hint; ordinary insertion and reference moves do not search for a new position. Leaf mutations may leave hints stale. All original tag, tombstone, ID, live-leaf and migration checks remain ahead of any hinted access. A valid position must then pass the original raw leaf tag and complete current-record equality predicate, including external hash and optional outputs. Failure requires the full original scan. Reference interchangeability remains unchanged.

Prepare a separate baseline-only shadow census to determine whether that exact seeding policy supplies useful hints in the unchanged seed 17 fixtures, and to count additional filter positives. Original lookup and leaf searches must always execute. Shadow state must not change original tree bytes, allocations, mutation behavior, fixtures, warmup, query order, or result checks. Track disabled, out-of-range, wrong-tag, failed-predicate, successful and stale hints separately, with table allocation/release/duplication and slot-zero writes accounted for. Do not quietly seed more paths when coverage is poor. Zero usable primary hints closes this lead as NONE before candidate implementations.

A nonzero count would establish only exposure. It cannot be multiplied by sampled shares or static instructions to predict speed, prove a 2% primary gain, or excuse a guard failure. Any candidate still requires three isolated implementations, exact emitted-code review, new qualified fleet controls, all unchanged performance/memory gates, matched profiles and independent confirmation. No timing or candidate execution is admitted here, and no ARM reacquisition is planned.

A fresh actual CPU Performance Engineering stdio discovery, `library_status`, and `ask` challenged this specific 56-bit-filter representation and shadow-census scope. Bundled revision `deb5a0bac467` reports 3 of 287 sources indexed and 158 passages; this query returned no supporting passage. Unread catalog entries supply no evidence. The decision rests on the disclosed source argument and remains conditional on independent diagnostic review.

Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and all child categories are unavailable for this mechanism. No new pipeline-slot or performance result exists. This preparation adds no completed population, replication, qualification, or approved source to the ledger.
