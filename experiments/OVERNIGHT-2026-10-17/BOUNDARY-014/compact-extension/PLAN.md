# BOUNDARY-014 compact-size extension

Preregistered additive correctness coverage; no timing/optimization decision. Reuse the
unchanged exact-zero scalar/public-API model and mutation sequence, with a separate
entry point enumerating EVERY size0..96,memberlengths16/253/254/319/320,twohashseeds
31121/31123,bothinsertiondirections:1,940fixtures/build. Each fixture checks both zero
signs through score updates, cloning, minimum deletion, refill and alternating-edge
removal; packed scalar reading, leaf ID links, rank/lookup, count bounds and exact bits.
Existing original24fixture suite has already run on exact sources; not weakened/replaced.

Control and retained EXP-004 A/B/C,release/debug and ASan/UBSan,8runs. Build/run commands
bounded120s each; serial children. Exact expected totals per run derived BEFORE running:
289060modelchecks and86570560exact results. Formula for size n:3n+5 modelchecks and
14n^2+29n exact-bit results;20fixtures per size. All outputs must match across8builds.
No cross-build allocator usable-size comparison; existing per-check memory equality stays.

Two retained sourcefaults rechecked against new matrix: wrong last-score reversal base
and numeric-equality early return for signed-zero update. Original patches unchanged;
new isolated copies. Faults must abort on exact-bit/debug decode oracle. No new boundary
suite count (extension of014); counts remain14suites/28distinctfaulttypes. New instances
recorded separately. Baseline/rootpreserved,allcosts/backend/model unknown.
