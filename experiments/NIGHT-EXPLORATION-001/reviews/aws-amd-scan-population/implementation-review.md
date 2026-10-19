# Independent pre-screen review of A, B and C

Reviewer `/root` did not author any candidate. Exact serving model and measured
cost are unknown. Reviewed immutable A at AMD `d76d63b79`, B at Intel `89dc8721f`,
and C at ARM `d1921d793`, after all three authors separately submitted their patches
without reading peers. Root independently applied each patch to `8fab511e` and
verified that only `src/zset_btree.c` changes. No candidate timing informed this
review.

**No static semantic blocker found for the declared 0–96 tag-span contract.**
This clears serial AMD builds and correctness validation, not acceptance. The
original source/referee, flags, allocator and hashing remain fixed; all local
validation must be repeated on the timing host. Preserve every patch and failed
check. Root adoption remains NONE.

| Candidate | Complete chunks | Residual | Portable fallback |
|---|---|---|---|
| A | Unaligned SSE2 load, byte offset advances by 16 | Original SWAR word from `base/8`, then original scalar tail | SIMD block excluded, base stays zero |
| B | Bounded memcpy into vector, original word index advances by two | Original SWAR loop resumes at that index, then original scalar tail | Word index starts at zero |
| C | Bounded memcpy into vector, byte offset advances by 16 | Scalar scan of at most 15 remaining bytes | Original helper body under alternate compile branch |

All compare exactly against the requested byte and OR zero-byte equality only for
tag one. Each movemask has at most 16 low bits; ctz is reached only for a nonzero
mask, then its lowest bit is cleared. Physical positions therefore increase and
the original reversed mapping yields decreasing logical positions. Counts and
duplicates remain exact, preserving the caller's collision disambiguation.

A's vector predicate implies at least 16 remaining bytes. Its byte offset is a
multiple of 16, so resuming at `base/8` cannot repeat or omit a full word. B's
`w+1 < count/8` implies a complete pair of words; the surviving index correctly
identifies any last word. C maintains `pos <= count`, so its unsigned subtraction
cannot underflow; only complete chunks reach memcpy. Scalar residuals stop at
count. Empty spans perform no input loads or output writes. Reversed `count-1`
underflow in A/B is unsigned and unused for an empty span, as in the baseline.

Only supported SSE2 builds include intrinsics. B/C use memcpy for unaligned,
alias-safe loading; A uses the compiler's unaligned intrinsic. No global ISA flag,
layout, API or hash change is present. Forced portable builds test the unchanged
algorithm but do not establish execution on ARM or a big-endian machine. Code
generation must still be recorded; separate authorship does not guarantee distinct
machine code or independent mechanism confirmation.

A retains the old comment saying eight tags are compared at once. This is a
documentation nit for any later recommendation; retain this submitted patch
unchanged during comparison. B/C update that comment.

The V1 guard oracle lacked deliberately misaligned complete-vector spans. Root
requested an additive correction before timing. V2 at `fa2d07d7d` adds 1,680 such
alignment and boundary-only cases and passes baseline native/sanitizer validation;
V1 evidence is retained. Run V2, unchanged original tests, scan interval/wide/live
widen/resize-generation checks, and forced portable coverage for each candidate.
Freeze and demonstrate deliberate fold/order/tail fault detection before timing.
Do not substitute correctness coverage for missing dense/reversed/resize timing
guards.

After those gates pass and binary/source/referee hashes are frozen, the chair's
unchanged 144-process, 300-second exploratory screen may run serially. The failed
1M A/A control already prevents acceptance; this review does not authorize a
control retry, larger timing budget, metric change or new variant after results.

Patch SHA256:

- A: `8c55d42ea53a6f689a53668c8cffcf9a7e01d274d3fcf9306ff154b1f8aa3547`
- B: `bd93f3922c72c4f1e8776a897e80321e3380345ee4dbd37d6d62e99683f4a644`
- C: `b4780cb8998db2931a63533849c658551a676c064be0071f23fd608b98e4f41a`

Reconstructed source SHA256:

- A: `30306a73d024ddcb986387ec91f1d1d8746697890e1b22a7f04de10afe029974`
- B: `204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23`
- C: `364b78b368a4b4100ca7339b07100947b5670bf21d6dcbf60195be4f84f63b0a`
