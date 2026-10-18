# BOUNDARY-016 — packed insertion/deletion overlap geometry

Preregistered before new validation. BOUNDARY-013 independently covers scalar score
decoding; BOUNDARY-015 covers natural mixed-score mutation histories. This isolates
the remaining private packed-stream movement invariant across every insertion and
deletion position, especially when adjacent fields overlap a 64-bit move chunk.

Falsifiable claim: zbtInsertScoreBits and zbtDeleteScoreBits produce exactly the
bit-at-a-time out-of-place reference stream, preserving every bit outside the moved
region and clearing the deleted tail field. No score conversion is used: arbitrary
uint64 packed fields are private bitstream inputs, not NaN score API inputs.

Fixed widths0..64, insertion counts0,1,2,3,7,8,9,31,32,33,63,64,65,94,95; deletion
counts1,2,3,7,8,9,31,32,33,63,64,65,94,95,96. Test every valid position with seeds
44351/44357. Allocate one bounded leaf buffer plus sentinel region; randomize all
data/spare/canary bytes before each geometry. Build expected output from an immutable
original, bit by bit. Compare the entire buffer after each operation; this checks
unchanged prefix/suffix/spare/canary bits, not just decoded fields. Zero-width cases
must leave all bytes unchanged. Require actual multi-chunk/overlap and zero/full-width
coverage; exact deterministic fixture/operation counts and digest must agree.

Run baseline and retained EXP-004 A/B/C, O3/debug native and O1/debug ASan+UBSan:
eight cells. No timing comparisons, no adapter changes, no existing test weakening.
Each child<=120s, total<=400s. Freeze source/referee/oracle hashes before execution;
preserve all failure output and explicitly uncommitted snapshots. Root source stays
baseline. Two faults: copy insert chunks forward instead of backward; poison the
deleted tail field instead of clearing it. Both must compile and fail the new oracle.

This is one additional boundary suite if all controls pass, not a population,
optimization or qualified benchmark. Exact backend/model/token cost unknown;
reviewer unavailable, sequential adversarial review only. Existing source PARK gates
and separate morning commit/review remain unchanged.
