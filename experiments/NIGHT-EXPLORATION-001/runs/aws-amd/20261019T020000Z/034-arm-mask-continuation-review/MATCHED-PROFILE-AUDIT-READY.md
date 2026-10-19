# Independent matched-profile audit prepared

Prepared for exact ARM029 freeze0a1040780 / SHA256 ecb0a87e282c93305fe77435ea264b9646bff79a3578623f763e81b0533cf1fe. No scientific result has been processed. The profile remains unexecuted at this checkpoint; this script neither authorizes nor starts it.

Usage after immutable results are published and extracted locally:

```sh
python3 audit-matched-profile-raw.py /path/to/029-mask-matched-profile --seal profile-evidence-seal.json --out /path/to/independent-profile-audit.json
```

Use the exact published relative seal filename. The script reads local artifacts only, imports no producer helpers and invokes no subprocess, compiler, perf tool or runner. Write output outside the frozen input directory. Exit0 means integrity and frozen supporting-mechanism gates pass; exit2 means integrity reconstructed but a profile validity gate parks; exit1 means missing/incomplete/inconsistent evidence. None means source acceptance.

The independent reconstruction checks104 contracts/serial timestamps/caps, complete source and protected/diagnostic binary identity records,23 frozen inputs and public seal/hash joins. It models literal tree semantics and known-control arithmetic, checks both disabled-zero controls and100% reported PMU runtime, recomputes all six paired instruction directions, independently parses all12 sample captures plus known control with loss/unknown denominators, and compares physical sampled ARM words to each own original/actual binary disassembly. It reconstructs full IteratorNext body differences, verifies reported mapping summaries and reproduces the finalizer's exact validity gates. Full raw perf hashes are rechecked only when those files are available; otherwise their retained provenance is explicitly listed as unavailable.

Raw evidence, not generic producer auditPASS, drives the result. Unknown/caller/layout differences remain visible; no new threshold or causality claim is introduced. Missing results or failure of any integrity assertion produce a retained FAIL_OR_INCOMPLETE audit. Operator before/after hash records are joined, never described as fresh live reads. Any additional post-idle proof will be reviewed separately when published. No protocol changes, row retries, new profiling or acceptance authority.

Local checks were limited to AST/module loading, independent known-work matrix arithmetic and tiny synthetic assembly/sample parser metadata. They are not benchmarks or scientific captures. Preparation hash and checks are in MATCHED-PROFILE-AUDIT-PREPARATION.json. Reviewer/root/aws_amd; inherited model/token/USD unknown. Current sourceNONE/PARK and all earlier reviews remain unchanged.
