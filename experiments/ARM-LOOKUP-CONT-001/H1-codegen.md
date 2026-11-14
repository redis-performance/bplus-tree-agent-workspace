# Helper population ARM code-generation gate

All three exact native builds pass the static boundary-change gate before timing. A removes the leaf helper symbol entirely; B and C retain generic output wrappers but inline the membership scan into raw lookup, with direct memchr/memcmp calls. B explicitly branches on the NULL-score input; C branches on output requirements. These are distinct helper-boundary implementations, not another spelling of rejected position arithmetic.

Raw lookup frame increases to272bytes in all three, so call removal does **not** establish fewer spills or a gain. Whole binary text: baseline95143bytes, A91119, B98607, C95135. These are static ELF/disassembly counts, not measured retired instructions or pipeline work. All source changes pass57native+57sanitizer upstream tests,18fixturecells each mode, and135000 sanitizer oraclechecks per variant. Candidate binary/source hashes are in H1/metadata.json when timing evidence is collected.

First lease expired before candidate timing; these exact binaries are retained for the new lease, conditional on fresh native qualification. LTO target remains PARK. No timing conclusion is drawn from size or symbol disappearance.

## TMA classification

Baseline/candidate Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring unavailable as validated workload categories; CPU-wide scope qualification absent and candidate capture notyetperformed. Childcategories unavailable. See native-profile/README.md.
