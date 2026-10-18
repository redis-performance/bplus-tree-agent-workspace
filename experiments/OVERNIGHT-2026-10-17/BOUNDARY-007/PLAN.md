# BOUNDARY-007 — lexical seek and optional iterator outputs

Add deterministic sorted-vector oracle for equal-score lexical API precondition.
No unsupported mixed-score lexical semantics or post-mutation iterator reuse. Cases:
sizes0,1,31,97,257,1025; three common finite score families(-DBL_MAX,signed zeros,
DBL_TRUE_MIN), forward/reverse insertion. Binary keys include empty,+,-,embedded NUL,
high bytes,prefix relationships,lengths2,3,8,16,319,320,321,511. Preserve exact score bits.

Compare present/prefix/extended bounds plus pointer-identity min/max sentinels in both
directions and inclusive/exclusive modes against an independent sorted array. Validate
absolute rank output and NULL rank; Next optional key/length/score output masks0..7.
Seek must return its result on first Next and advance correctly across leaf boundaries.
Failed seek must leave an exhausted iterator. Repeat after deletion/reinsertion and
clone-original free; never use invalidated iterators or member pointers.

Release/debug and ASan/UBSan must pass all cases; each child<=120s. Preserve failures.
Two separately isolated fault controls: ignore reverse exclusive equality, and wrong
reverse maximum-sentinel rank. Both must fail relevant assertions. No source target edits,
no performance measurements/optimisation or claimed independent review. Exact patches,
commands,hashes,stdout/stderr retained; commit review pending. Backend/model/cost unknown.
