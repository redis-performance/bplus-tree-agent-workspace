# Corrections discovered during follow-up

This adjacent note supersedes two interpretations in the sealed report/review.
Original files, raw rows, hashes and capture gates remain unchanged.

**Host exclusivity was not established.** A subsequently refreshed fleet inventory
and live reservation record identify another campaign's Intel-profiler reservation
starting20October14:19:19UTC, before the14:25–14:42 sweep. Its capture service was
active when checked during this follow-up; continuous activity during the old sweep
is unknown. The old preflight checked Docker and CPU scope but missed this competing
reservation.32/36 configurations passed their capture-quality gates; that does not
establish dedicated-host conditions or exclude interference through shared caches,
memory bandwidth or uncore resources. Treat the resulting priorities as provisional.
No source/timing acceptance existed to revoke. The separate campaign is untouched.

**Iterator annotation percentages had the wrong denominator description.**
`perf annotate --symbol … --percent-type global-period` filtered the event population
to that symbol. The percentages were conditional on IteratorNext, not all workload
sampled period. Independent unfiltered period reconstruction gives:

| 1M full-output site | Baseline | A | B |
|---|---:|---:|---:|
| Packed-length line589, workload period |18.64069%|13.46117%|13.08542%|
| Width-test attribution358, workload period |11.03793%|10.85756%|10.82710%|

The old20.60/15.02/14.60% and12.20/12.11/12.08% remain valid **within-symbol**
shares. TMA slot fractions and whole-function sample shares are unaffected.
Neither denominator establishes instruction latency or speedup.

[Independent reconstruction](../INTEL-FOLLOWUP-001/INDEPENDENT-ANNOTATION-DENOMINATOR.json)
· [Follow-up evidence](../INTEL-FOLLOWUP-001/README.md).
