# H7-C independent source review

PASS for source correctness and artifact identity; fleet code-generation admission remains pending. The reviewer did not implement C or its focused tests and performed no performance measurement for this review.

Reapplied the retained patch to the frozen baseline and matched the final source byte-for-byte. Candidate SHA-256: `fa45c5d7bdd04f37bd448a48b573ef92128b56ed35df9d176659d9ddd00ca5d9`. The retained manifest file hashes all match. The patch changes only the shared mask contract and three consumers whose redundant byte checks relied on the old approximate mask.

The unsigned arithmetic is exact lane by lane: low-seven-bit values plus127 are bounded by254, preventing cross-byte carry; OR with the original high bit and low mask leaves a clear high bit only for zero XOR bytes. Bit extraction is still guarded by a nonzero mask. Table and reference lookup retain numeric slot order, IDs, tombstones and bounds. The leaf-word scan retains complete-word loads, the original endian conversion, folded tag1/tag0 union, reversal mapping and scalar tail. The header/record matcher and packed decoder are unchanged.

Focused tests derive byte truth and enumeration independently, compare reference lookup against scalar search, use guard-ended scan arrays and compare complete baseline/candidate public scan traces. All required native/sanitizer/fixture and supplied oracle artifacts pass. The initial baseline-only scan test API misuse and its correction remain retained; it does not establish a candidate failure. Actual32-bit and big-endian execution remain unvalidated.

The broader helper scope adds arithmetic to empty-bucket and scan consumers. It can regress misses and scans even if it removes the intended checks. Exact ARM native and target code must still satisfy the preregistered dependency and frame gates. Qualified collision/resize/scan guards, target timing, portability, fresh confirmation and profiles remain required before adoption. Source selection remains NONE.

No candidate pipeline capture exists. Qualified ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable; local assembly and correctness do not substitute for those measurements.
