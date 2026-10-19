# Independent preliminary review: AMD lazy lower-bound member decoding

Reviewer: root native session agent, independent of the AMD implementer. Exact
backend variant and token/USD cost unavailable. Static review only; no independent
benchmark or sanitizer execution is claimed by this review.

Baseline:8fab511e, unchanged target SHA256
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.
Reviewed candidate patch hashes:

- Variant A: `68d351a8aa14132bb154ca827effe095aa98358d1e995117443c9b9278b2d249`.
- Variant B: `acbd94b897d58fe3314c9114e5405826f1e9adc0afa1d1e905ee15b36b24105a`.
- Variant C: `ea0d37f7e51e05628a118922987409a777cff247f6baeae276b47fca1d97e382`.

Verdict: no blocking semantic defect found in these three patches. They are
eligible for correctness validation and the preregistered exploratory screen.
This is not acceptance, final performance review, or permission to adopt source.

- All variants preserve the original `<`, `>` then lexical comparison sequence.
  Equal finite scores and +0/-0 therefore still compare exact member bytes and
  lengths. Even unordered comparisons reach the original lexical fallback;
  low-level NaN input is not asserted to be supported.
- Moving the read-only leaf-element accessor after unequal-score checks does not
  change tree state, leaf ownership, physical/logical mapping, index IDs, counts,
  resize state or iterator invalidation. No allocation, alias lifetime, vector
  overread or architecture-specific instruction is introduced.
- VariantC's early loop continuations make exactly the original lo/hi transition.
  VariantB adds a helper used only by this lower-bound operation. A is the smallest
  local spelling; choose among them from evidence, not source aesthetics alone.
- The hypothesis avoids packed-member pointer/length decoding. It does not remove
  unconditional memcmp: the baseline already calls memcmp only after score ties.
- The proposed linear oracle is independently structured from binary search and
  covers finite extremes, signed-zero ties,8/16/320/321-byte members, construction
  order and reversed leaves. Zero-length, common-prefix and different-length tie
  queries must also be included before the full screen. Existing upstream/native/
  sanitizer tests remain required and unchanged.

Measurement review still pending: the whole-process profile includes setup and
must not be presented as timed-loop attribution. Current1M A/A fails one block
(+1.113%);100K passes its observed range. The six-block screen can reject or retain
an exploratory lead, but cannot establish adoption. Required fresh confirmation,
complete guards, owned-memory checks and matched profile validation remain open.
