# Read-only follow-up: no new hypothesis selected

This inspection uses only the completed029 source-linked disassemblies, code map and
source13e459ff8. It ran no compiler, benchmark, census or runner job. It does not alter
the failed100K control or the NONE decision. The source is unchanged.

The public referee calls `zbtreeIteratorNext(&it,0,NULL,NULL,&score)` for every visit.
The actual015 function at0xb7e0 tests the two member output pointers and jumps directly
to0xb871 when both are null. Member offsets, packed member headers and external member
ownership are therefore outside the selected score-only path. The earlier Intel/ARM
full-member iterator offset-array cache results are a different output contract; they
are not evidence of an opportunity here.

On this x86 build, score decoding is inlined into the public iterator. It reads width
and reversal, computes the physical bit position, loads/shifts the packed word, checks
whether a ninth byte is required, builds the width mask, applies score_shift and base,
and converts ordered bits back into the exact score. Width64 remains explicitly
handled in mask selection. The ninth-byte path remains conditional; no unconditional
wider-load equivalence follows. Exact finite values and signed-zero/reversal behavior
remain required for any future change.

Several apparent opportunities are already represented in historical populations:

- EXP002 separated forward score-only dispatch to reduce generic handling and saved
  registers. Its expanded guards rejected all three variants, including no-output
  regressions. Current AMD samples at register-pop instructions (104 events pooled
  at+0x1ba/+0x1bb) do not establish the cost of those pops or revive that family.
- EXP004 rewrote the cross-word predicate. The actual015 sequence still has the
  shift-nonzero test followed by the width-versus-remaining-bits test. This is the same
  previously explored mechanism, not a new proposal created by a new architecture.
- EXP005 changed nonzero width-mask arithmetic. The actual015 mask sequence includes
  shift, width64 comparison and conditional selection. Existing evidence is PARK;
  its effects cannot be carried from Apple or inferred from sampled source share.

Score-only metadata caching would require a new state/lifetime contract, evidence of
leaf widths/shift/reversal/transition frequencies, and explicit invalidation/output-mode
and memory guards. This profile supplies no such census. It does not justify changing
the public iterator layout or assuming metadata remains stable across arbitrary calls.
A fresh, genuinely distinct hypothesis would need evidence beyond these samples and a
separate future measurement authorization. No such hypothesis is selected here.

The main-frame share is also substantive: source-linked diagnostic code contains two
signed `cvttsd2si` conversions plus arithmetic implementing the referee's unsigned
64-bit checksum cast. The observed IP after the first conversion is not a direct
measurement of that conversion's latency. Caller layout differs from actual015, as
retained by the byte map, so main-frame exact relative-offset comparisons cannot be
used as equivalent instructions. Changing this checksum or output contract would be a
separate harness revision and baseline requalification, not a tree optimization.

The present samples are coarse, may skid, and have no matching per-region PMU counts
or cache/branch counter diagnosis. Zero reported losses is not proof of unbiased
attribution. Both-size qualification failed; no timing pooling, pruning, extra seeds,
operation changes or candidate measurements follow. AMD remains idle/sourceNONE.

References: source lines4021–4055 and499–518; frozen profile/timing-full-asm.stdout,
profile/profile-full-asm.stdout and profile/code-map.json; EXP002/README.md,
EXP004/selection.md and EXP005/README.md. One native AMD author; exact model/cost unknown.
