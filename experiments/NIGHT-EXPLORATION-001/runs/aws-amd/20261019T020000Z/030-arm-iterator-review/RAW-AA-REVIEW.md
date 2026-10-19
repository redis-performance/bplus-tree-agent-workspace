# ARM024 A/A independent raw review — both sizes qualify

Reconstructed immutable73c9e313f without importing worker audit code. All48 raw rows
and12 blocks match the fixed sixABBA/size schedule, seeds701–703 twice, alternating
size order,16-byte members and50M operations. Every process exited0, has serial
nonoverlapping timestamps, stayed within30s, and reports CPU2 at both timing endpoints.
The phase meets its300s bound. No retry, omission or substitution appears in the records.

| Size | Maximum absolute A/A effect | Minimum window | Qualification |
|---|---:|---:|---|
|100K|0.0539112482%|166.240475ms|all six within±1%, all windows>=10ms|
|1M|0.3715240827%|186.780319ms|all six within±1%, all windows>=10ms|

Effects are reconstructed with Decimal arithmetic from raw elapsed/actual-operation
fields, then compared with worker outputs at1e-10 percentage-point tolerance. Each
row has exactly500/50 traversals,50M visits, one warmup and expected integer checksum
2499975000000/24999975000000. Owned bytes agree within eachABBA block and across the
repeated seed fixture; different seeds are not forced to have the same allocation size.

All ten source/referee hashes match before/after. The unchanged actual013 baseline
binary330b39a9 is the only invoked executable. The execution freeze is52169964… .
The112-entry profile evidence seal is byte-identical to reviewed4e43c9f59; all profile
artifacts remain unchanged. A/A recorded audit/mapping hashes equal those exact files.
Both prerequisite outputs report complete/pass/mapped; source identity has not drifted.

Verified98 public A/A artifact hashes,100 A/A evidence-seal entries and112 unchanged
profile entries. Every raw CSV/result hash also verifies directly; raw stderr hashes
are empty-byte hashes, with normalized public copies containing only whitespace.
Exact schedule, process commands, return codes, checksum/owned-memory invariants and
all12 reconstructed effects are retained in raw-aa-audit.json. The independently
written auditor is audit-raw-aa.py; no runner access or new measurement was used.

This qualifies these native ARM corrected-source baseline fixtures/session only.
It establishes neither candidate benefit nor a portable performance result. The
separately reviewed profile preserves coarse attribution and caller-layout limits.
AMD029's failed100K control, older ARM full-member iterator results and original8fab
outcomes remain unchanged. No proposal, implementation or source adoption follows
without a separate root decision. Source selectionNONE.

Provenance: one native AMD reviewer, author of the imported AMD base harness; this
independently authored raw reconstruction is not a claim of unrelated harness authorship.
Root separately reviews. Exact inherited model, token usage and cost are unknown.
