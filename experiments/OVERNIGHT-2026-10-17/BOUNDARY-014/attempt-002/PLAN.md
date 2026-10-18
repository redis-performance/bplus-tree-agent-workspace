# BOUNDARY-014 — signed-zero mutation and physical order

Preregistered before execution, round 9. No timing or source acceptance claim.
Use real trees with 97/513 members, uniform binary lengths 16/319/320, ascending
and descending insertion, two deterministic hash seeds (19001/19009). All scores
are alternating +0/-0, with member order independent of the score sign. Toggle
every sign through the public update API, clone, then drain by named minimum
deletion. Inspect actual forward/reversed packed leaves and decode bits with an
independent scalar reader. Check exact IEEE bits, binary members, forward/reverse
iteration, ranks, lookup, count, leaf links/IDs, and no allocation change during
read-only checks. Repeat refill and alternating-edge deletion; do not reuse stale
iterators across mutations. Require both physical orders and an observed first-leaf
reversal opportunity; these are structural counts, not time shares.

Run unchanged control and retained EXP-004 A/B/C in isolated snapshots, release/debug
and ASan/UBSan. Each child <=120s. Two isolated sensitivity faults: reverse-for-pop
base incorrectly taken from last score; in-place update incorrectly treating numeric
equality as bitwise equality. Both must fail an exact-score check/assertion. Preserve
all failures and patches. No existing check weakened. Main source/referee unchanged.
Independent reviewer startup failed; coordinator sequential review, model/cost unknown.
