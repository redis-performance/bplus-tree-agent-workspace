# COUNTERS-003 — structural coverage established

All160 fixed fixtures pass release/debug and ASan/UBSan;320 serial executions. Exact
member/score/state oracles cover both directions/all masks; independent bitwise decode
matches each leaf. All four preregistered primary cells meet the narrow-width coverage
criterion. Width64 and cross-word paths still occur in other elements/encodings, and
ordered insertion is needed to exercise reversed physical leaves. This is a structural
census, not an executed-branch count or time profile. No speed claim or source acceptance.

The original post-run whole-result equality check failed because reported owned bytes
include native/ASan allocator usable-size differences. All320 children succeeded. A
read-only audit finds only owned bytes differ; all structural fields agree, and within
EACH execution the original unchanged-memory assertion passes. Original driver and
manifest/raw rows retained without rerunning or weakening any in-process check.
`analyse.py` verifies this distinction;`cross-build-audit.json` preserves the first audit
(the differing_fields value concatenates values rather than counting them; summary.json
has corrected field counts). No timing binary or referee changed.

[Plan](PLAN.md),[result](SUMMARY.md),[snapshot/commands/hashes](manifest.json).
Root preserved. Independent reviewer failed startup;review sequential. Backend/model/
cost unknown. Decision: coverage diagnostic complete; source NONE, existing precision
PARKs unchanged. Next: exhaustive synthetic decoder boundary oracle before any score
read-condition simplification; current source is still the baseline.
