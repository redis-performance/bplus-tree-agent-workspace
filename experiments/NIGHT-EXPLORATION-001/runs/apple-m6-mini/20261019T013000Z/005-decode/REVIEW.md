# Adversarial review — sequential self-review, independence pending

The original scalar handles logical start/reversal and bits0/64; no duplicated
packed-score reader or new persistent state. Empty/partial output canaries and
nonzero-offset count1 subranges are exercised by the shared oracle. Both deliberate
wrong-output and skipped-bulk faults are caught. Frozen helper bytes are unchanged.
Only Apple Clang/ARM64 was measured; compiler attributes and generated call layouts
require separate portability checks. Static sizes grew; no whole-tree performance claim.

A/A fails primary,41 cells hit the50ms cap, and three baseline guard profiles are
insufficient. No independent confirmation/review or selected-candidate profile.
Successive fixed A/B/C phases do not satisfy rotated cross-candidate ordering;
this deviation prevents qualified variant ranking and is explicitly preserved.
B/C caller disassembly equality does not imply equal bulk helper instructions.
The all-six-block guard losses under qualified uncapped controls reject every policy.
The count1 delta-zero fixture is seed invariant; no fresh-input claim is permitted.

The first broad manifest audit failed on a documentation hash because uppercase
and lowercase selection filenames collided. Git80177d1e/e62f839d prove both documents
were published before executable freeze6e9e4ec8 and timing. Keep the initial failure
and original manifest; all executable and original-source hashes remain strict.
No acceptance or independent-review claim is made.
