# EXP-002 — Forward score-only iterator specialization

Date:2026-10-18. Current status/decision: **REJECT**, selection **NONE**.
Round7 [expanded guards](guard-extension/README.md) supersede the historical C preference:all
three implementations confirm no-output guard regressions on both fresh seeds.
The round6 discovery record below is retained unchanged as historical evidence.
Root source remains unchanged. [Plan](PLAN.md), [freeze](freeze.json), [selection](selection.md),
[implementation selection](implementation-selection.md), [screening](bench-results/SUMMARY.md),
[fresh confirmation](bench-results/CONFIRMATION.md), [profiles](profile-results/SUMMARY.md).

## Frozen context

Base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus HARNESS-003 frozen uncommitted patch;
PR source a7ecd959374d66847c095250bf2d373edf7316c5. Exact source/referee/binaries in freeze
and manifests. Local M1/arm64/macOS26.3,Clang17,C11,-O3,-g,-fno-omit-frame-pointer,libc,
unchanged assertions. One serial thread; frequency/effective QoS/residency unknown.
AA-005 qualifies forward iterate16/320; PROFILE-003 supplies descriptive baseline profile.
One hypothesis: separate forward score-only dispatch from generic optional outputs to
avoid generic register-save/handling cost. No packed decoder or iterator state change.

## Population step1

Three sequential coordinator proposal passes A/B/C, followed by chair pass; **not
independent agents**. A narrow dispatch ranked1/selected; C cached iterator state ranked2
(scope/risk); B scan tag matching ranked3(failed scan precision). Files in proposals/.
Actual backend/model and token cost unknown; reviewer startup failed before execution.

## Population step2

Three isolated implementations share exact baseline/referee: A inline early body,
B noinline specialized/generic helpers, C inline specialized/noinline generic fallback.
All patches and implementation notes in variants/. Control/A/B/C each pass43 original
tests and existing lexical/score-boundary oracles in release and ASan/UBSan.64 validation
commands pass.72 same-session serial ABBA rows,three blocks per variant/cell; all controls
and preregistered screening gates pass. C wins overlap/smaller-patch rule.

## Benchmark/profile validation

24 fresh-seed confirmation rows pass; four matched descriptive captures resolve all
samples. Saved codegen shows baseline saves six register pairs at public entry; C hot
path has no such saves and tail-dispatches generic fallback. Evidence supports dispatch/
register isolation, not exact cycle attribution. All raw timings/checksums/bytes/IDs/QoS,
commands/stdout/stderr/source and binary hashes retained; profile PCs/assembly in scratch.
CPU MCP evidence checker says drop_number; no portable performance headline promoted.

## Adversarial review and remaining gates

[Review](review/ADVERSARIAL.md). Generic reverse/output modes can regress from added
dispatch: existing correctness coverage is not a performance guard. Independent review/
performance confirmation and committed provenance absent. Therefore PARK despite strong
local exploratory evidence. Preserve all variants and baseline for morning review.
No upstream action,git retry,permission change or publishing. Next concrete action in
implementation-selection.md. Supervisor records CLI usage separately; no invented cost.
