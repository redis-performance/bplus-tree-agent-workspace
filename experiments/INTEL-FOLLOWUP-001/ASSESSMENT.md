# Decision: prioritize iterator B; source remains NONE

All16 configurations pass all48 L2 windows on the secondary Intel host with
sibling50 offline. This closes the selected profile gaps under a new measurement
condition; it does not qualify old timings or prove why earlier captures differed.

| Follow-up | Fresh observation | Decision / next evidence |
|---|---|---|
| Iterator B,1M full output | Memory Bound34.07→28.15%, Retiring46.81→53.01%; Frontend0.80→1.63%, Bad Speculation1.60→1.20%. | Best existing parked continuation. Validate precise-load collection, then distinguish leaf-transition loads from offset arithmetic. Diagnose original reverse/fraction timing guards before a new full A/A and ABBA campaign. |
| Update lookup,1M same/position | Memory Bound68.73/68.63%, versus48.75/48.83% at100K. | Strongest baseline bottleneck. Resolve which loads dominate using qualified PEBS plus explicit operation/phase counts before choosing an implementation hypothesis. Memory Bound alone does not identify DRAM. |
| Score-only iterator guards |100K base/B: Memory0/0%, Frontend2.11/3.28%.1M base/A: Memory8.52/8.21%, Frontend1.85/2.67%. | No clear memory-mechanism lead in these pairs. Keep guards; no throughput claim from slot fractions. |
| Corrected scan B |1M Frontend15.15→18.17%, Bad Speculation22.23→24.34%, Memory28.50→25.31%. | Mixed profile; no rescue of rejected timing result. Qualified LBR is needed to locate branch/layout effects. |
| Scan trim / resize guards | Trim has negligible branch-mispredict slots and≈13–14% Frontend. Resize has≈16% Bad Speculation and≈19–20% Core Bound baseline. | Different paths need separate explanations. Trim's seven-member scalar-tail/setup path must not be attributed to full SIMD chunks. Both baseline/candidate classifications now available. |

No absolute cycles/op, memory traffic reduction or speedup follows from these fractions.
No new source, population, approval or timing comparison. Existing PARK/REJECT statuses
remain unchanged; source NONE. Exact per-build four-root trees: [iterator](ITERATOR.md),
[update](UPDATE.md), [scan](SCAN.md). Every mean includes15 ordered one-second intervals.

## Precise-profile gate remains open

PEBS and LBR supported recording, but the command did not preserve enabled/running
measurements. Both probes failed the preregistered scheduling gate; no deeper captures
ran and neither probe supports causal attribution. [Independent gate](INDEPENDENT-PROBE-GATES.json).

The concrete collection configuration defect is now understood: requesting a read format does not
insert read structures into samples. A **separate preregistered capability validation**
should test the documented `:S` modifier plus timing fields, including the PEBS auxiliary
member semantics, actual event identity, precision, loss and per-event scheduling.
[Primary-source diagnosis](SCHEDULING-EVIDENCE.md). This fix has not been measured here.

Earlier libc attribution is independently reconstructed with exact ELF/debug identity,
but its host exclusivity was unproven; retain it as a provisional localization lead.
`memcmp`/`bcmp` share the resolved implementation. No dynamic caller attribution without
callchains. [Prior evidence corrections](../INTEL-PARKED-PROFILES-001/CORRECTIONS-20261020.md).
