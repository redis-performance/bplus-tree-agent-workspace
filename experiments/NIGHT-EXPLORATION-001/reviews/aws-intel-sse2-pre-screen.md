# Independent preliminary review: Intel bounded SSE2 leaf-tag search

Reviewer: root native session agent, independent of the Intel implementer. Exact
backend variant and token/USD cost unknown. Static source/oracle review only;
no independent correctness execution or performance acceptance is claimed.

Reviewed hashes:

- Variant A: `0b2f2ff32316c5f2df51f90e8a05ae45bb011dc709c7c3f7c2e3820b7b455f34`.
- Variant B: `ee3882230b3aed7754f42ea76d6999ae89956c55643f3bed9d82155a120f5d67`.
- Variant C: `ebff896cdadc0c0a3b30bca88155da82b00a0b6655f2de5a483ce2da373f7efd`.

Verdict: no blocking semantic or bounds defect found. Proceed only after original
native/sanitizer and targeted oracle checks pass. Source adoption remains NONE.

- A/B/C load16bytes only while count≥16, use unaligned SSE2 loads, compare exact
  byte lanes, and call ctz only for a nonzero16-bit mask. SSE2 movemask lane order
  is increasing address order, preserving memchr's first-match semantics.
- A's scalar tail and B's libc tail remain inside the supplied interval. C's
  overlap tail runs only after at least one16-byte chunk and with1..15remaining
  bytes. Its endpoint-minus16 address stays inside the original interval. Masking
  low lanes discards bytes already searched; shifts are1..15bits in unsigned32.
  A repeated lookup after a collision gets a fresh original_count and cannot
  reach backwards before that invocation's supplied range.
- Non-SSE2 builds retain memchr. No hashing, owned-memory, leaf physical/logical
  mapping, length equality, external hash prefilter, score decoding, index/leaf ID,
  resize state or iterator invalidation behavior is otherwise changed.
- The page oracle covers every tag0..255, lengths0..96, both guarded endpoints,
  each first-match position, a second match and suffix searches. It also passes
  an inaccessible pointer with zero count. This meaningfully tests first-match
  and no-overread behavior; sanitizer/native and original tree tests remain needed.
- Before portable adoption, run a forced non-SSE2 build or an actual non-x86 host.
  The intrinsic header placed mid-file and the unchanged memchr-specific caller
  comment are maintainability nits for any eventual final patch, not semantic
  blockers to this isolated measurement.

Performance evidence is provisional. Intel gprof self-time includes instrumentation
and whole-process setup; dynamically linked libc attribution is incomplete. The
assembly's memchr call supports a call/scan hypothesis, not proof of its time share.
PMU access was unavailable without changing host settings. The1M-hit A/A range
exceeds±1%, so a screen can reject or preserve a lead but cannot establish adoption.
Full guards, fresh confirmation, matched profile validation and final review remain.
