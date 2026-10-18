# BOUNDARY-015 — mixed finite-score mutations under controlled capacity

Preregistered in round 12 before running the new oracle. COUNTERS-006 established
allocator-sensitive physical history for alternating zero. This extends semantic
coverage to adjacent binary64 values, extreme finite scores and integer packing.
Falsifiable claim: all public results and independent scalar packed-score decoding
remain exact through construction, updates, deletion, clone, rank-range deletion,
refill and draining, under ambient, exact and 16-byte-rounded usable capacity.
This is a correctness experiment, not a timing or memory-efficiency claim.

Fixed matrix: sizes 0,1,2,31,32,33,63,64,65,95,96,97,127,128,129,513;
three score families; seeds 42101 and 42109; 256 mixed edits per nonempty fixture.
Members mix lengths 0,2,3,8,16,253,254,319,320,321,511 with embedded NULs.
The independent model sorts numeric score then binary member; signed zero bits
remain exact. Use no NaN or infinity. Check both iterator directions and optional
output masks, lookup/raw lookup, rank, rank/score seeks, score counts, batched score
lookup, settled scan, linked-leaf ownership/IDs and read-only memory equality.
Read packed scores bit by bit independently of tree helpers; compare both to model.
Observe width/shift/orientation and leaf-count transitions; require nonzero coverage
of zero/partial/full widths, nonzero shifts, both orientations, growth and shrinkage.

Run unchanged baseline plus retained EXP-004 A/B/C: three capacity policies, native
O3/debug and O1/debug ASan+UBSan = 24 cells. Each child <=120s; 600s total execution
budget. Fixed matrix, all failures retained, no acceptance thresholds weakened.
Controlled policies must produce equal complete output across builds/variants;
ambient physical equality is NOT required. Logical digests must agree everywhere.
Diagnostic adapter overhead and slack are never substituted for production guards.

Two new intentional fault controls in isolated baseline copies: corrupt a nonzero
decoded finite score bit and make numeric updates return success without applying
changed score. Each must compile then fail a semantic assertion (timeout is not
detection). Retain exact patches. Original tests are unchanged, run in every cell.
Freeze base commit, source/referee/adapter/oracle SHA256 and commands before execution.
Protected git is not retried; provenance is explicitly uncommitted snapshots.

Reviewer agent startup failed before execution. Review is sequential, not independent;
exact backend/model/token cost unknown. No optimization population or source adoption.
EXP-004 A/PARK and EXP-005 PARK/NONE remain pending their existing gates.
