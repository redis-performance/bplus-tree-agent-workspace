# H3 — bounded short-inline record equality

Select the third distinct original proposal after helper rejection and independent metadata preparation. Fresh native profile has2.82% namedmemcmp plus decoding within the41.38% leaf helper. Exact libc attribution identifies the tag scanner as an existing SIMD memchr, so this hypothesis retains that scanner. A small memcmp share limits confidence; eliminating a generic decoder/call for proven short records is a testable mechanism, not a predicted gain.

All implementations start exact baseline ee8e7f701 at e13d9fc88, with unchanged referee. No H1 inlining or H2 metadata patches. After tagmatch and existing external-hash filter, permit a short fast path only when the actual inline record marker equals querylength and length≤8. Otherwise preserve the original decoder/length/memcmp path and all output semantics.

A uses bounds-safe scalar width comparisons: zero reads for0; byte for1; first/last2-byte memcpy loads for2–3; first/last4-byte loads for4–7; one8-byte load for8. B switches0..8 to constant-size memcmp equality. C uses bounded XOR/OR byte comparison. No overread, alignment assumption, fixturestring/seed, new scanner, explicitSIMD, batching or prefetch. Inspect generated code before timing; an unchanged generic call/loop with no plausible reduction is ineligible, retain its artifact.

Require existing57native+57sanitizer tests,36fixturechecks,135000 supplied output/external oraclechecks, plus focused lengths0..8,binarybytes,allmismatch positions,same-tag collisions,unaligned/end-of-page buffers, and generic/externalfallback. Guardpage tests must verify that both input ranges stay within actual lengths; output combinations and reversedleaves remain covered. Record zero-length semantics precisely, without widening unsupported public API contracts.

Each qualified host/compiler cohort uses its frozen workscale and same-session controls, three ABBA blocks per six cases,≥2% hit improvement everyblock,≤1% guard/memory regression, allrows≥250ms. Failed cohorts remainparked; no unchangedretry. Intel portability guards for an ARM-selected candidate remain≤1% on allcases. Preserve every variant/failedtest; selection/confirmation remain separate. Native/LTO/Intel results are never pooled.

Actual shared controller CPU-perf consultation asks this exact mechanism and safety coverage; no supporting retrieved passage establishes a speedup. Baseline/candidate Frontend_Bound,Bad_Speculation,Backend_Bound,Retiring and children unavailable until separately qualified captures. No pipeline claim from hotspotshares.
