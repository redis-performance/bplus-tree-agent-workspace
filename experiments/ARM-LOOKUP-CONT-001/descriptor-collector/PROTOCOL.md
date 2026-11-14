# Prepared descriptor collector — unused after H6 rejection

The controller reported that all three H6 native discovery candidates failed the
registered 2% primary improvement requirement. This collector was prepared and
tested offline only. It was not deployed, frozen for execution, or used to build,
qualify, compare or profile on the fleet. No descriptor guard timing or Intel H6
cohort is authorized by this artifact. The reviewed harness and original
collectors remain unchanged. Future use requires a separately authorized protocol;
the existing failure cannot be retried by renaming a directory.

`../fleet_descriptor_guards.py` preserves the existing build/qualify/compare
structure. Its revision 0 fixed cases and sweeps are member-forward 1000000,
member-reverse 1000000, lookup-inline 100000 and lookup-external 500000. It permits
only baseline and the exact frozen H6-A/B/C sources. The embedded source and
referee SHA-256 maps bind the new harness, build script, protocol and compilation
dependencies. A controller freeze must also pin the collector itself.

Build records exact source, compiler identity/version, ELF, disassembly and size
output hashes, and runs four untimed `verify` cells per ELF. Build and timing are
separate actions: the controller must review the exact fleet ELF assembly and
provide an immutable codegen decision before qualification. There is no automatic
static approval. Candidate timing additionally requires the exact source's passing
original H6 discovery result for the same host/compiler cohort.

Qualification is 48 baseline A/A rows: four cases, three ABBA blocks each. Comparison
is 48 rows per eligible candidate, using the same declared order. Every process
must match the independently recomputed operations, hits, lengths, byte samples,
scores and weighted checksums; fixture identity/counts and integer types are
checked. Windows below 250 ms invalidate the action. Each A/A block must stay within
±1%; each candidate block may regress by at most 1%. Integer comparisons preserve
the exact boundary. Cases/blocks/cohorts are never pooled to cancel failures.

Pre-loop and immediate post-loop owned memory are independently bounded at +1%,
with exact endpoint reproducibility within each binary/case. Baseline endpoints
must match qualification. Post-validation memory is retained but never substituted
for the immediate endpoint. No transient-peak claim is made.

Every owned child gets pre/post checks of source/referee/ELF/provenance hashes,
owned lease/deadline, original stopped coordinator PID/start ticks, active release
timer, CPU0 controller affinity, online CPU2, offline SMT sibling, idle container
state and competing collector/compiler/benchmark/profiler processes. Intel also
requires its recorded sibling50 state and inactive profiler service. Each child
is bounded to 240 seconds with a 300-second cleanup margin. A lock serializes this
collector; process checks also detect other existing collectors. These checks
detect observed interference; they do not make the host immutable against a new
uncoordinated process during a measurement.

Phases are fixed as `H6-descriptor-{arm|intel}-{native|gcc15-lto}-r0-seed{17|29|43}`.
Each action directory is claimed once. Existing actions, failed/short rows and
partial runs cannot resume, overwrite or retry. Failed effect gates retain the
complete declared grid; invalid output/isolation/timeouts stop immediately and
preserve raw stdout/stderr and failure metadata. Holding a reservation does not
override the original H6 rejection.

## Required controller documents and invocation contract

All artifact paths below are relative to the reserved fleet deployment root.
The root must be `/opt/bplus-arm-lookup-cont-*`; none of these commands were run.

* `H6-exclusions.json` is mandatory, even if `{}`. Its existing H2-compatible
  schema is `{"B":{"source_sha256":"exact H6-B SHA-256","reason":"rejection"}}`.
  Unknown letters, stale hashes and missing reasons fail closed. Exclusions apply
  across H6 host/compiler cohorts, and must be deployed identically on both hosts.
  A registry change during an action invalidates that action; a new exclusion
  between qualification/comparison removes that candidate before any timing.
* `experiments/ARM-LOOKUP-CONT-001/descriptor-guards/FREEZE.json` must have
  `status: "FROZEN"`, `revision: 0`, `source_hashes: SOURCE_PINS`,
  `referee_sha256: REFEREE_PINS`, `cases: CASES` (the collector's exact maps), and
  `collector_sha256`. This file is deliberately **not** created by this preparation.
* A successful build writes `<phase>/build/metadata.json`. The controller's
  `<phase>/codegen.json` must name its `metadata_sha256`, a nonempty `reviewer`,
  `review_path` and `review_sha256`, and one `binaries` entry per built variant.
  Each entry names `source_sha256`, `binary_sha256`, `assembly_sha256` from the
  exact build and Boolean `eligible`. Eligible entries require
  `timer_and_loops_pass: true`; eligible candidates additionally require
  `descriptor_mechanism_pass: true` and a `discovery` object containing
  `metadata_path`, `metadata_sha256`, `analysis_path`, `analysis_sha256` for the
  original same-host H6 cohort. Source, upstream, seed17, cohort, original baseline
  ELF and candidate eligibility are checked. A source excluded globally never runs.
  With no eligible candidates, even supplemental A/A is refused.

The future invocation shape, after those gates and live reservation review, is:

```sh
taskset -c 0 python3 experiments/ARM-LOOKUP-CONT-001/fleet_descriptor_guards.py \
  --root "$descriptor_root" --platform arm --cohort native --seed 17 \
  --variants ABC --collector-sha256 "$descriptor_collector_sha" --action build
# After exact fleet assembly review only; the same variant list is required:
taskset -c 0 python3 experiments/ARM-LOOKUP-CONT-001/fleet_descriptor_guards.py \
  --root "$descriptor_root" --platform arm --cohort native --seed 17 \
  --variants ABC --collector-sha256 "$descriptor_collector_sha" \
  --approval-sha256 "$descriptor_codegen_sha" --action qualify
# Only after every qualification block passes:
taskset -c 0 python3 experiments/ARM-LOOKUP-CONT-001/fleet_descriptor_guards.py \
  --root "$descriptor_root" --platform arm --cohort native --seed 17 \
  --variants ABC --collector-sha256 "$descriptor_collector_sha" \
  --approval-sha256 "$descriptor_codegen_sha" --action compare
```

LTO uses the original baseline metadata's immutable GCC15 image and frozen
`-O3 -flto=auto` build script; native uses `-O3`. No native/LTO result is inherited.
Seeds29/43 have separate phases and fresh A/A. The same lease/coordinator identity
must cover build, review, qualification and comparison.

## Offline validation and limits

`python3 experiments/ARM-LOOKUP-CONT-001/descriptor-collector/test_offline.py`
passes 14 tests, including all 384 existing correctness rows, independent closed
forms, complete 48/144 synthetic grids, checksum/type/count corruption, exact 1%
duration/memory boundaries, missing/duplicate/reordered rows, per-case rejection,
source-bound exclusions, discovery scope, path escapes and exclusive file writes.
Mocked lease tests reject ownership/state/deadline/identity/timer/affinity/CPU/SMT/
architecture/container/coordinator/profiler and competing-process failures. The
test imports the collector with process spawning disabled; no collector main,
fleet connection, benchmark subprocess or timing was executed. Synthetic elapsed
integers test arithmetic only and are not measurements. Logs and the first test
expectation failure are retained alongside this note. End-to-end fleet behavior
remains unexecuted and needs controller review if a future protocol uses this code.

Public role: descriptor-collector implementer; also implemented H6-B, but did not
author the descriptor harness. Own enabled-tool discovery again found no callable
cpu-perf/library_status tools. The controller's shared descriptor consultation in
`../H6-selection.md` found no supporting passage; it is not a consultation performed
by this worker. Detailed backend provenance remains private and exact token costs
are unknown. For baseline and every candidate, Frontend_Bound, Bad_Speculation,
Backend_Bound, Retiring and their child shares are unavailable: this preparation
collected no TMA or performance data.
