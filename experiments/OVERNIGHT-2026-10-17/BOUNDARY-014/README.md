# BOUNDARY-014 — exact zero signs through real mutations

PASS: unchanged control and EXP-004 A/B/C, release/debug and ASan/UBSan. Each build
checks 24 fixtures, 22,080 full models and 46,005,384 exact-score results. It observes
both physical orders and 626 first-leaf reversal opportunities. Uniform binary member
lengths16/319/320,97/513members,twohashseeds,bothinsertionorders;all score signs toggle,
clones drain by named minimum deletion, refilled trees drain alternating edges.
Independent scalar packed reader, iterator/rank/lookup, links/IDs, copied members and
stable read-only memory assertions pass. These are structural counts, not timings.

Both isolated faults are detected: last-score reversal base and numeric-equality
update early return. All eight successful build outputs match exactly; no source bug
found. Root source and retained variants unchanged.14suites/28faults;EXP-004 stays PARK.

The first new-test allocation assertion failed because lookup advanced active rehash.
[Erratum](PRECONDITION-ERRATUM.md) retains that failure and explains explicit rehash
settling before the same memory assertion. No exact-score check or existing referee
was weakened. [Passing manifest](attempt-002/manifest.json),[plan](PLAN.md),
[faults](faults.json),[oracle patch](attempt-002/oracle.patch). Uncommitted provenance;
review sequential, independent reviewer startup failed,model/cost unknown.
