# Round 20 — retained-candidate correctness and coverage

**Source adoption NONE. EXP-006 remains C/PARK.** EXP-004 A/PARK and EXP-005 PARK/NONE
also remain. This round adds 112 passing correctness cells and six detected deliberate
faults, with no new timing campaign, source candidate or population. Main source,
header, root referee, allocator adapter and original test entry retain their hashes.

All experimental children finished at **06:25:59 UTC**. Round deadline is 06:31:31 UTC;
handoff cutoff is 06:30:01 UTC. This is not the final campaign round. The final worker
still owes MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed work and decisions

The [cross-boundary matrix](../EXP-006/cross-boundary-round020/README.md) passes all
80 fixed source/build/seed/mode cells and 48 builds. Exact control/A/B/C snapshots use
three frozen BOUNDARY-023/025 oracles: partial promotion, widening then narrowing,
and external clone/full-relocation/partial-decline modes. Discovery seed 92503 uses
debug assertions; held-out 92521 disables only debug assertions. Native and ASan/UBSan
builds preserve every unconditional check. Logical digests agree across sources and
builds per seed/mode. This extends EXP-006 coverage; it does not add a named suite.

Five transferred faults on isolated C copies are detected at the intended boundaries:
stale table after promotion causes an ASan use-after-free; last-hit omission fails the
mask check; outside-count write fails the canary; stale compacted ID fails the registry
check; shallow external clone fails pointer disjointness. Exact failure logs and patches
remain. These repeat known controls, not production bugs or new source candidates.

The [scalar fallback probe](../EXP-006/scalar-fallback-round020/README.md) passes 16
semantic cells, 16 builds and 16 preprocessing commands. It deliberately selects the
fallback while preserving host header/adapter configuration. Preprocessed programs are
identical except for B/C's helper body; control/A are identical throughout. Each relevant
cell passes 1,585,152 first-match or 198,144 protected-page checks. A deliberately added
zero-span read fails at the protected page under ASan. This validates the forced scalar
branch on the M1, **not actual big-endian execution** or another architecture.

The [dense promotion extension](../EXP-006/dense-promotion-round020/README.md) passes
eight control/C cells, including held-out debug-off confirmation, and eight builds.
The old long-member fixture did not require 16 tags in a hit leaf. The new fixture keeps
its original promotion family and adds short-key queries with that explicit requirement.
Each cell passes 36 promotion cases, 264 requested lanes, 68 dense-hit leaf checks,
43 complete models and more than 36 million reported exact member/score results.
External ownership, score moves, signed zeros, live SCAN, original canaries and usable
allocation accounting remain checked. A/B were not run against this new fixture.

The final [generation-wrap matrix](../EXP-006/generation-wrap-round020/README.md)
passes eight control/A/B/C cells and eight builds. Only fixed seeds changed in the
successful BOUNDARY-021 multi-member oracle. Each cell checks 262,160 natural resizes,
four growth wraps, 262,188 full models and 24,254,190 exact public results. Logs observe
65535→1 and the required one-/two-leaf batch behavior. All logical digests agree.
These are fresh fixed fixture seeds with debug enabled, not a separate selection or
confirmation phase. No additional fault run was performed for this extension.

All four decisions are **PASS for their stated correctness scope only**. No original
performance guard is replaced. EXP-006's long-key uncertainty and single-lane concern
remain unresolved. Counts of named suites, diagnostics and optimizations stay unchanged.

## Evidence and verification

Commands used, with complete child arguments/stdout/stderr in each manifest:

```sh
python3 experiments/EXP-006/cross-boundary-round020/run.py
python3 experiments/EXP-006/cross-boundary-round020/faults.py
python3 experiments/EXP-006/scalar-fallback-round020/run.py
python3 experiments/EXP-006/dense-promotion-round020/run.py
python3 experiments/EXP-006/generation-wrap-round020/run.py
python3 experiments/OVERNIGHT-2026-10-17/audit-round020-static-leaf.py
python3 experiments/OVERNIGHT-2026-10-17/verify-round020.py
python3 scripts/check-workspace.py --pristine-source
git diff --check
```

[Audit](ROUND-020-VERIFY.json) passes **3,960 hashes, 220 serial experimental command
windows and 23 patch reconstructions**, including all 15 optimization patches. It
recomputes schedules, logical digests, matrix counts and preprocessor equality. The
separate [prior audit](ROUND-020-PRIOR-AUDIT.json) verifies 2,149 immutable round19-sealed
files; only the six intentionally shared mutable ledgers are excluded. The earlier
successful checkpoint and all 469 sealed files are also preserved and reverified via
[checkpoint index](ROUND-020-CHECKPOINT-INDEX.json). Workspace links,
pinned source/support and whitespace checks pass. No unexpected semantic, compile or
sanitizer failure occurred in the new experiments; all six deliberate failures remain.
Raw sanitizer diagnostics stay in ignored snapshots; public stderr redacts only the
workspace path. No test was weakened and no prior evidence was overwritten.

[Static inventory](ROUND-020-STATIC-LEAF-AUDIT.md) describes already frozen round18
compiler assembly. C has a larger own frame/body than control in that output. This is
post-hoc source inspection, not a new diagnostic, linked-code-size measurement, dynamic
instruction count, peak-stack claim or explanation of the batch-size timing contrast.
It changes no selection or gate. The [coverage matrix](ROUND-020-CANDIDATE-COVERAGE.md)
separates exact EXP-006 coverage from older baseline/EXP-004 tests.

CPU MCP ask, benchmark 05/14 methods/code and evidence checker were consulted. The ask
retrieval was not direct M1 evidence and is not cited as support. No M4 numbering,
frequency or results were transferred. The checker returned no_number for the
qualitative claim; that is not methodology approval. [Method record](ROUND-020-METHOD.json).

## Handoff

Totals remain **7 harnesses / 13 baselines / 34 diagnostics / 26 named boundary suites;
5 sequential populations; 0 accepted / 2 rejected / 3 parked**. The historical count of
54 distinct boundary fault types remains, plus two round19 lane-reuse controls awaiting
taxonomy review. This round's six controls repeat existing families.

[Adversarial review](ROUND-020-REVIEW.md) is sequential: independent reviewer startup
failed before work. Exact backend/model/token cost is unknown; the supervisor records
CLI usage separately. Independent review/confirmation, committed provenance, actual
architecture portability and qualified performance guards remain pending. Frequency,
effective QoS and within-window migration remain unknown. No publishing, git metadata
retry, credentials, permission changes or supervisor/runtime/STOP edits occurred.

Next: use [morning-review preparation](ROUND-020-NEXT.md) to reconcile the final report
with the candidate decision/coverage matrices. Do not revive rejected variants or rerun
the failed timing schedule. Keep main baseline for separate morning review. If future
experimental work is requested, preregister the remaining candidate coverage or obtain
qualified guard measurements; correctness alone cannot make C acceptable.
