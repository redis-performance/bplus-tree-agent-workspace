# Proposal population and chair

2026-10-19 01:34 UTC. Three passes by one GPT-6 worker, sequential, not
independent agents. Exact backend variant and measured token cost are unknown.
All passes read the same EXP-007/008 results, focused count-one profiles,
frozen decoder source, and generated code. No new timing was done here.

1. Pass one: use the original scalar accessor only when `count == 1`; the
   count-four scalar losses in EXP-008 argue against a larger threshold.
2. Pass two: use scalar at count one only for noncrossing geometries, to avoid
   the ninth-byte path for width 59/61–63. This reduces guard exposure but
   requires a width dispatch.
3. Pass three: use scalar only for the primary width 60 at count one. This is
   the smallest scoped test of the prior lead, with less general benefit.

Chair: test the falsifiable count-one hypothesis, with all three policy
variants A/B/C in isolated source snapshots. No source adoption follows from
the prior EXP-008 8–9% observation. Equal-score output, checksum and setup
must be identical. The prior sampling cannot attribute timed-only cost, so
this population is exploratory pending new A/A, guards and confirmation.
