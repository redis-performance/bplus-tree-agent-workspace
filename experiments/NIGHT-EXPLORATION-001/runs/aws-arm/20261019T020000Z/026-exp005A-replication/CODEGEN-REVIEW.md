# Native code-generation inspection, independent gate pending

The ordinary nonzero-width IteratorNext path reduces complete mask construction
from four instructions to three. Actual013 at a5b4/a5b8/a5bc/a5c0 uses
MOV-all-ones/CMP-width64/variableLSL/CSINV; candidate at a590/a594/a598 uses
NEG-width/MOV-all-ones/variableLSR. All constant/setup operations are counted;
there is no feeding operation moved elsewhere. AArch64 variable shifts use the low
six bits, so negative width implements64-width for1..64. Width0 still bypasses
this region; width64 shifts by0. The finalAND remains identical and excluded on both
sides; independent score_shift load likewise remains. Whole nonzero path loses one
instruction with no extra call, conditional branch or memory access. Cross-word
conditional ninth-byte load and physical reversal remain unchanged. UMULL operands
swap commutatively. Full function114→113 instructions includes unchanged assertion
path count; assertion string addresses/source line changed and remain unnormalized.

The separate exact instruction inventory retains PCs, raw words and assembly for all
five declared callers in actual/control/A. zbtreeScore25→25 has identical instruction
words. zbtreeRank585→585 and zbtreeFindForAdd688→688 differ only in direct call
relocations and assertion string/line immediates, with the same named call targets.
zbtIndexScanSlot509→508 has the same four-to-three mask construction, the same final
AND and conditional cross-word access. Its CBZ w8 becomes CBZ x8 immediately after
LDRB w8 at108d8, which zeroes upper bits; no test semantics change. Its UMULL operand
swap is commutative. Other differences are branch relocations/assertion addresses and
source lines, all retained explicitly. No extra load/store or conditional branch was
introduced in these declared paths. Full-binary disassembly is retained for review;
this inspection does not claim every caller is performance-qualified.

These are static instruction counts, not cycle savings or evidence of a2% gain.
The exact source/oracles and successful validation support semantics separately.
Root/AMD independent reviews and explicit root timing grant remain required; no
codegen-gate PASS certificate has yet been issued and no screen has run.

Author/root/aws_arm, native Codex; exact model and measured costs unknown.
