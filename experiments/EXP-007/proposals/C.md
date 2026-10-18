# Proposal C: source-level leaf-width specialization, with scalar-call guards

Independent proposal by agent `/root/proposal_c`. Backend: Codex collaboration
agent; exact model identifier and token/currency costs unavailable. No other
proposal was read. No build, timing, source mutation or acceptance performed.
Inspected baseline HEAD `4fd3a3fdbce5acca18ee292642a3d80a79f50362`, AGENTS.md,
POPULATION.md, shared-memory status, production decoder/iterator, focused decoder
kernel, EXP-004 selection, historical profiles and assembly.

## Evidence and hypothesis

The focused EXP-004 report records forward 8/64-bit regressions of 15.65%/10.39%
for A, despite its smaller static branch inventory. The baseline short-circuits
the crossing arithmetic when physical bit offset is zero. This is evidence of
layout-sensitive cost, not measured instruction latency or a universal mechanism.
Historical EXP-004 interrupted-PC captures place most observed samples in
`zbtreeIteratorNext`; they are descriptive, not unbiased time shares. Its assembly
includes the packed-score predicate, but that function emits only one score per
call. The focused benchmark instead contains a whole-leaf loop and four independent
checksum chains. That distinction is essential to interpreting a new win.

One hypothesis: express ninth-byte eligibility as a leaf-width invariant in the
production decoder, so the compiler can eliminate or hoist the crossing logic
when decoding an entire leaf. An inlined helper should retain the exact existing
eight-byte load, mask, score shift, reversal and ordered-double conversion, while
only the crossing-capable path contains the conditional ninth-byte reconstruction.
The source wrapper selects the helper using the invariant
`bits > 58 && (bits & 3) != 0` for valid widths 0..64. This identifies exactly
59, 61, 62 and 63. The zero-width path stays separate and unchanged.

For width w, reachable offsets are multiples of gcd(w, 8), with maximum
8-gcd(w, 8). Width 58 reaches offset 6 and ends exactly at bit 64; width 60
reaches offset 4 and also ends at 64; width 64 only reaches offset 0. Thus the
excluded widths cannot require a ninth byte. Keep the original per-position
crossing condition inside the crossing-capable helper. No unconditional ninth
byte read, new allocation, iterator state field or persistent classification cache.

Exact target: `src/zset_btree.c:zbtScoreLeafScore` and a small adjacent inline
helper if needed. All existing callers stay unchanged. The same frozen
`bench/decoder_kernel.c` must call the same source entry point in every variant.
Implementers may choose source arrangements for the same invariant; they must
not replace the timed kernel with bespoke loops available only to candidates.

## Predictions and adversarial constraints

- On full warmed leaves, assembly should show classification outside the inner
  position loop or removal of ninth-byte code from its simple path. If it remains
  per score, the promised amortisation has not occurred.
- Widths 8 and 64 are mandatory regression guards against the original baseline,
  not against the slower EXP-004 A. Width 60 is a useful primary layout because
  it still has variable nonzero offsets but never crosses. Guard 0, 31, 57 and
  all four crossing widths in both physical orientations.
- Count 1 and short leaves can lose because dispatch is not amortised. Include
  fixed short counts such as 1 and 7 alongside 96; report dispatch cost within
  timed work, never classify fixtures outside timing just for the candidate.
- The public iterator cannot select a code path once per leaf without additional
  state/API machinery: each call returns to its caller. The proposed minimal
  source change may therefore repeat classification and regress that iterator.
  A kernel winner is only eligibility for actual score-plus-length and score-only
  iterator checks; it is not a production improvement.
- Warm eight-leaf synthetic fixtures cannot establish cold-cache performance or
  random lookup benefit. Do not add cold-cache claims or a cold-only acceptance
  exception. Fresh iterator guards can detect a transfer failure without changing
  this one hypothesis into a larger iterator redesign.

## Correctness and falsification

Preserve exact finite bit patterns, signed zero, both physical orientations,
all score shifts, width-zero behavior, tail padding/read bounds, and unsigned
shift safety at width 64. Exercise every width 0..64 and tail positions in native
and sanitizer checks. No structure growth or tree-owned-memory change is expected.

Preregister the exact primary and guard cells, >=2% primary gate, <=1% demonstrated
guard regression, A/A qualification, serial ABBA discovery, and fresh held-out
confirmation before timing. Reject a variant for semantic failure, demonstrated
guard loss, or lack of the proposed code movement. Park noise or a kernel-only
win pending actual iterator confirmation. Fewer static branches alone never pass
the profile gate. If no source arrangement hoists classification in the frozen
loop, select NONE rather than silently moving the optimization into the referee.

Recommendation: test this bounded source-only hypothesis, but do not promise true
once-per-leaf production iterator dispatch. Its largest practical risk is that the
microbenchmark can amortise work that the existing scalar API necessarily repeats.
