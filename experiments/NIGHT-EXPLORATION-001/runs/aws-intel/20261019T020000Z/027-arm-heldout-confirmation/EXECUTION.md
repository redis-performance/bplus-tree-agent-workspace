# Prepared executable confirmation — no launch grant

This adds execution code to protocol8b9aa2aba. The original PLAN/schedules/identities/protocol freeze remain unchanged. The new coordinator-owned ARM lease runs08:12–10:15UTC on19October2026; old overnight release remains complete. `execution-freeze.json` pins this code and the unchanged protocol inputs. No SSH, build or benchmark has run during preparation.

ARM027 draft `b56bf0cac` reserves discovery1101–1103, guards1301–1303, profiles1401–1403, correctness1501/1502. Confirmation1201–1203 remains unused. The final reviewed guard inventory, rather than every original diagnostic cell automatically, defines required coverage **before data**. Root and AMD must review concrete alternatives for any predeclared short diagnostic cells. Every required inventory cell must qualify and pass; unresolved acceptance coverage keeps PARK. No post-result waiver is allowed.

## Launch contract

`run-phase.py` has separate `aa` and `confirmation` modes; it cannot automatically advance. Each invocation is a new owned serial CPU2 helper job with a300s cap, child cap30s, and at least320s remaining before10:15UTC at launch. The same300s includes driver pre/post checks. The outer helper enforces process-group termination, resource isolation and lease lock. All output uses a fresh directory; an existing directory is an attempt marker and prevents replacement/retry.

Root publishes a reviewed receipt, then pins its SHA explicitly in the separately sealed private launch configuration. This is publication provenance, **not a cryptographic signature**. The driver requires:

- Exact protocol/execution freeze, full baseline/candidate binary identities, new lease hash/deadline, explicit idle handoff to `/root/aws_intel`, and a phase-only grant.
- Artifact hashes for correctness, guard A/A, guard comparison, fresh primary A/A/discovery, coverage review, root driver review and AMD driver review; each prerequisite explicitly has both `audit_status: PASS` and `gate_pass: true`; audit integrity alone never grants progression.
- A frozen required-guard inventory, exact unique required cell IDs, all qualified/guard-pass/memory-pass, and unchanged coverage disclosures. The inventory also retains predeclared coverage-only diagnostics. Every coverage-only diagnostic also has a bound, complete six-block result and evidence: qualified all-block losses are REJECT and mixed qualified losses are PARK, both blocking progression. Unqualified diagnostic observations remain disclosed, and memory failures always block. No ACCEPT receipt is permitted.
- No held-out seed overlap with any new discovery/guard/profile/correctness list; both exact48-row schedules are checked against an independently generated fixed contract before execution.
- For confirmation only, a separate root progression receipt binds the48-row held-out A/A result,96 raw CSV/stderr files and passing independent audit. The96 raw file hashes must equal the independent audit’s exact filename/hash map, not merely its filenames. The driver checks these hashes before and after measurement. A/A's exact owned bytes are carried into candidate comparisons.

The private per-phase `aa-job-config.json` / `confirmation-job-config.json` is **not provided or executable yet**. It contains only lease, baseline_root, candidate_root, evidence_root, receipt, receipt_sha256 and output. Root reviews and seals its hash with final operational commands before granting launch. `job-entry.py` builds subprocess arguments directly; no shell evaluation of configuration occurs. Configurations and connection endpoints are never committed publicly. `aa-job.sh` and `confirmation-job.sh` are helper entrypoints; do not run them directly.

Generic eventual helper command, with private absolute paths supplied only at handoff:

```
python3 <reviewed-helper> --lease <new-lease> --name <unique-phase-name> --seconds 300 --script <leased-phase-job.sh>
```

After retrieving immutable output, the independent auditor runs locally:

```
python3 audit-phase.py --phase aa --directory <retained-aa-output>
python3 audit-phase.py --phase confirmation --directory <retained-confirmation-output> --aa-directory <retained-aa-output>
```

This auditor imports no execution-driver code and reconstructs expected order, command arguments, all raw CSV rows, exact score/checksum/memory/CPU2 semantics, serial timestamps, every child’s ≤30-second wall duration, Decimal ABBA effects and gate decisions. Its integrity PASS is distinct from `gate_pass`; failed qualification cannot advance. An incomplete/failed phase retains its raw partials and requires a failure report; the auditor does not reinterpret it as a completed screen.

## Review and remaining gates

`receipt-template.json` documents the required public schema but is deliberately invalid/ungranted. The required inventory schema is `{required_cell_ids: [...], coverage_only_diagnostics: [...], coverage_disclosures: [...]}`; the coordinator binds the independently reviewed actual ARM027 manifests through prerequisite evidence. No fabricated result or invented approval is supplied. The execution freeze excludes future receipts/configs because their root-approved hashes are separate prelaunch bindings.

Local preparation checks parse Python syntax without executing the driver, verify the original protocol freeze and every48-row schedule, validate no seed overlap with the coordinated ranges, and check shell syntax. These checks are not benchmark, semantic or sanitizer evidence. Root/AMD review must precede any launch, and the coordinator must explicitly provide a fresh idle handoff. All prior review authorship and exact-model/cost limitations in PLAN remain applicable.

## Review correction v2

AMD review identified three prelaunch gaps at67365d7b7. All diagnostic outcomes are now bound and classified (qualified adverse or mixed blocks progression); prerequisite audit integrity is explicitly separate from gate success; held-out A/A raw hashes join the independent audit map exactly; and the independent auditor checks each child’s30-second cap. `execution-freeze-v1-67365d7b7.json` retains the original unexecuted manifest, with original file versions still at67365d7b7. The current freeze supersedes it before any workload. Fifteen synthetic local metadata checks cover classification, hash substitution/duplicates and child duration boundaries; no phase main, benchmark, build or SSH was invoked.

Each diagnostic result has `complete`, `qualified`, `memory_pass`, six finite `block_effect_pct`, its exact `classification`, and nonempty bound `evidence`. Inventory `coverage_only_diagnostics` is the exact unique list of diagnostic cell IDs, disjoint from required IDs. Allowed qualification-independent diagnostic state is only `UNQUALIFIED_DIAGNOSTIC`; qualified cells must classify PASS (all six effects≤+1%). Classification is recomputed by the driver, not accepted as a caller label.
