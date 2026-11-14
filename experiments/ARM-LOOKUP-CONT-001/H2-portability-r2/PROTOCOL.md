# H2 portability operational revision2

Status: PREPARED, NOT ADMITTED. This is a separately reviewed operational correction within the original absolute task window, ending2026-11-14 05:24:45.781UTC. It does not retry a failed guest/source result: the controller reports the earlier preparation stopped before image or C workload execution. The original H2-portability files, manifest, failed preparation001 and all evidence remain unchanged. H2 remains PARK.

The [original protocol](../H2-portability/PROTOCOL.md) still defines the exact source pair, image/tool recipe, C harnesses, ABI proofs,57 unit tests per cell, fixed18 verifies, supplied135k output checks per cell, focused mutation/refresh coverage and failure gates. R2 does not change them. All original C/shell files continue to run from `H2-portability/`; there are no copied or edited candidate/referee/oracle files in r2.

Only these operational differences apply:

1. With CPU50 offline, the observed CPU2 topology sibling list is `2`. R2 requires CPU2online1, runtime siblings exactly2 and CPU50online0. The saved original reserved pair remains `2,50` in the reviewed record/provenance; CPU50 is not brought online. Record additions are `cpu2_expected_siblings:"2"` and `saved_sibling_pair:"2,50"`.
2. Driver/manifest/test/protocol artifacts reside under `H2-portability-r2`. Atomic single-use driver phase directories are `H2-portability-r2-image-receipt-001` and `H2-portability-r2-correctness-001`; root's separately reviewed image preparation uses its new preparation002 claim. Original claims are never deleted or reused. Exact named containers/cleanup owner-root-generation labels remain unchanged.
3. Before any driver container/image inspection or launch, a hash-bound successful staging receipt must exactly join the reviewed r2 manifest, complete file mapping, run root and revised isolation record. Add required CLI `--staging-receipt` and `--staging-receipt-sha256`; both mode-review JSONs include `staging_receipt_sha256`. The receipt must have exactly:

```json
{
  "schema_version":1,
  "status":"STAGED",
  "run_root":"<exact reviewed absolute root>",
  "manifest_sha256":"<r2 files.json hash>",
  "isolation_sha256":"<revised operational-record hash>",
  "verified_files":{"<every manifest path>":"<its exact hash>"},
  "failed_files":[]
}
```

No missing/duplicate/partial/failed staging output authorizes image setup or correctness. Root's new image launcher must independently check this receipt before import/claim/subprocess; the driver checks it before constructing Runner and rechecks its byte hash on every identity check. Failures consume the new attempt and are retained, with no retry.

4. The original task timestamps are now explicit constants checked against the record: start1794632085.7812834, deadline1794633885.7812834. No renewed30-minute budget is available. Existing absolute command deadlines, in-container GNU timeout/TERM/KILL15seconds and2seconds margin remain unchanged. If review/staging/support cannot finish in the remaining original window, report incomplete.

`driver.diff` shows the exact changes from the original frozen driver. `files.json` retains all original pins and additionally pins the original manifest plus r2 artifacts. Original source16def20 and B63b18cd5, prepare-image scriptd9a3dfcf and clock/ABI/metadata/output harnesses are unchanged.

Validation:26 synthetic Python tests pass, including the unchanged tests, actual offline topology success/old online topology rejection, complete staging joins, failed-staging orchestration proving no Runner is constructed, complete mocked matrix and baseline-failure stop. No C, Docker, fleet, perf or timing workload ran during this preparation. No new package or tool-support claim is made. Fresh shared portability CPU-perf consultation remains retrieved-but-irrelevant as documented in the original report; no new independent consultation is claimed. Role: operational harness implementer; independent review and execution admission remain required.

TMA classification: baseline and B Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and child categories remain unavailable. No performance or source-adoption claim follows from r2.
