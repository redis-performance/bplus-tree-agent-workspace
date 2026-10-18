# BOUNDARY-013 — packed reader geometry passes

Release/debug and ASan/UBSan each pass85760 synthetic leaves,2572800 exact-bit checks;
7812cross-word,1200width64,76800width0,1286400reversed results per build. The independent
bit-at-a-time writer and IEEE-bit model cover every width0..64,all valid shifts,ten
counts,and two seeds. Spare bits start poisoned. All scores finite;no NaN API assumption.
Synthetic unsorted leaf contents test private pure decoding only;public-order tests
remain unchanged. Both intentional faults detected at exact-bit mismatches.

[Plan](PLAN.md),[commands/source/binary hashes](manifest.json),[fault evidence](faults.json),
[oracle patch](oracle.patch). Separate root test added;root tree/source/referee unchanged.
Also passes control/A/B/C of EXP-004 in both builds before any timing. No performance
claim. Sequential review;independent reviewer startup failed. Backend/model/cost unknown.
13boundary suites/26detected faults;selection pending separate experimental gates.
