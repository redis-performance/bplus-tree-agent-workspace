# Standard mutation-replica referee — validation PASS

Owner `/root/followup_proposal_a`, actual independent agent, inherited GPT-6/Codex
family; exact serving variant, token usage and monetary cost unknown. Only this
referee, its validation records/logs and the authorized temporary scratch build were
written. No candidate variant, frozen bench/source, shared memory or Git was changed.
All validation processes have finished. No performance conclusion is drawn.

`standard.c` is a separate copy of the original `bench/microbench.c`. Original
operations, fixture generation, public API calls, single-tree warmup and assertions
remain. Default `--replicas 1` retains the original operation path for all eight
operations, including allowing a single tree larger than64MiB. The CSV appends fields
without renaming/removing the original fields. Original benchmark/source hashes and
all exact compiler/validation commands are in `standard-validation.json`.

## CLI and reporting

`--replicas N` defaults to1 and accepts1..4096. Values>1 require explicitly selecting
`--case insert` or `--case delete`; other cases and `all` reject that request. All
replicas use identical deterministic binary members, hash seed and insertion/query
order, with separate tree allocations. The existing `--ops` remains requested_ops;
each mutation runs exactly one complete n-member operation per replica.

Append-only CSV fields:

- `replicas`: independent trees used; one for the original path.
- `total_operations`: actual operations across every replica; equals the original
  `operations` field, which is n*replicas for replicated mutations.
- `working_set_tree_bytes`: sum of actual tree-owned allocations after insertion,
  or immediately before timed deletion after warmup; excludes fixture/driver storage.
- `estimated_working_set_tree_bytes`: replicated insertion's untimed populated-prototype
  estimate, or replicated deletion's observed prepared allocations before warmup.
  For replicas1 this reports the original per-tree observed bytes, without extra setup.
- `mean_tree_bytes`: decimal mean, working_set_tree_bytes/replicas. The integer
  numerator and denominator above retain the exact mean without rounding.

The original integer `tree_bytes` remains per-tree, using the first replica's bytes
at the same insertion/deletion boundary as the original single-tree path. It never
silently becomes aggregate bytes. Use the exact working-set sum/replica count for
mean-memory comparisons when individual allocator sizes differ.

## Timing boundaries and limits

Replicated insertion first constructs one untimed populated prototype to estimate
owned memory, frees it, then creates independent empty trees outside timing. One
full original insertion loop per empty tree is timed. Replicated deletion creates
and populates every tree outside timing and performs the original lookup warmup on
each; one complete original deletion loop per tree is timed. Construction/free,
warmup, final lookup/length/checksum checks and memory queries stay outside timing.
Replica checksums are individually verified; insertion additionally verifies every
member's exact generated score after final owned bytes have been recorded.

Replicated working sets must fit64MiB both in the predeclared estimate and actual
prepared/final measurements. A cheap member-bytes lower bound rejects impossible
requests before fixtures; insertion uses the complete populated-prototype estimate,
and deletion checks accumulated actual prepared/warmed bytes. Violations exit2.
The agreed cap concerns estimated/final tree-owned allocations, not an unmeasured
transient allocator peak. Replicas1 keeps the original unrestricted path. Replicas
change cache/allocator history and must be separately frozen/requalified; no old
baseline timings are reused.

## Bounded validation

Both native(-O3) and ASan/UBSan(-O1) builds pass, with original frame-pointer,
assertion, allocator and hashing options. Six compiler commands build this referee,
the unchanged original and the deliberate skipped-mutation control in both modes;
all build stderr logs are empty. The69 recorded commands comprise:

- Original/new semantic comparison of all eight operations at100members/16-byte keys
  and1Kmembers/321-byte keys in both modes:32 matched operation rows. Case, fixture,
  actual operation count, checksum, tree_bytes, traversal and warmup metadata match.
  Timing/CPU/QoS observations are deliberately excluded from semantic comparison.
- Replicas3 at sizes1/100/1K with16/321-byte keys for insertion and deletion:24
  passing process checks. Aggregate counts/checksums, <=64MiB working-set fields
  and exact mean accounting are checked.
- Replicas4096 at size1 for both mutations in both modes:4 passing maximum-count checks.
- Eleven invalid/cap inputs per mode:22 expected exit2 checks, including zero/negative/
  malformed/oversized replica counts, missing value, unsupported operation/all,
  impossible member-byte estimate, populated-prototype estimate and actual prepared
  allocation limit. Both separate estimate/actual-limit paths are observed.
- The deliberate fault omits the final member in each replicated timed insertion/
  deletion loop. All four native/sanitizer fault processes abort on the unchanged
  intended per-tree length or checksum postcondition. The fault source hash is saved;
  temporary faulty source/binaries remain under scratch/m6-caller/harness-standard.

The initial fault classifier wrongly required the word ASSERT/PANIC. This host
prints the assertion expression directly, so the first insertion fault was a real
intended detection but the classifier failed. Its prior validation snapshot and
`standard-logs/driver-erratum.json` preserve the failure. Classification was corrected
to require nonzero exit plus the exact intended length/checksum expression; completed
commands were reused, with no child rerun or harness/check weakening. Raw outputs are
retained in scratch; public logs replace the absolute workspace root with a generic
placeholder. Short timer columns emitted during correctness checks are not benchmark
results. Comparative timing remains the root coordinator's separately frozen work.
