# Implementation selection: NONE

All three isolated variants are semantically eligible and pass unchanged-referee checks, original 57-test native/sanitizer suites, 24 fixture cells,90,000 optional-output oracle cases and45,000 separate external-record oracle cases per build. No tree-owned bytes changed.

The fixed144-row comparison rejects all three at the primary speed gate: A median−1.394%, B−1.528%, C−1.841%; only one of nine primary blocks reaches−2%. Every guard block remains at or below+1%. No source is selected, no discovery winner is promoted, and no fresh confirmation or selected profile is run. See RESULTS.md and comparison/analysis.json for full ranges/raw joins. Preserve all three patches.

All four qualified TMA categories—Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring—are unavailable: baseline capture was CPU-wide without continuous exclusion evidence, candidate capture unexecuted after rejection. This decision relies on the registered timing gate, not an inferred resource classification. Independent review is in review/FINAL.md. Backend/model costs are recorded as unknown where unavailable.
