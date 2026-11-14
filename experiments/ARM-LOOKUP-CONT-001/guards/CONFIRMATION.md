# Supplemental guard confirmation — prepared, not executed

The controller must review this protocol and `../fleet_guard_confirmation.py` before launching. This preparation performs no fleet access, builds, measurements or qualification. Original H2-B guards must qualify separately on each intended host/compiler before that cohort can advance. Passing this supplemental confirmation does not adopt a source optimization or replace the original six-case confirmation/profile/review gates.

For each original seed17 guard phase, run seed29 and seed43 as separate confirmation phases. Reuse its exact immutable baseline and H2-B ELFs directly; do not rebuild, copy source into a new build, or include C. Each seed repeats all five cases with unchanged counts: iterator-forward/reverse 1,000,000 sweeps each, rank-forward/reverse 200,000 each, churn 20,000. Warmup remains 1,000 sweeps. Each phase has 60 fresh A/A rows followed, only upon full qualification, by 60 B comparison rows. Both seeds therefore require 240 processes per host/compiler cohort. Check the live lease and cleanup budget before admission; the driver's five-minute residual check is a safety floor, not a duration estimate.

The original metadata must identify the requested cohort, seed17, all five frozen counts, baseline/B source hashes and ELF hashes. Original qualification must pass all 15 unique case/block cells and report 60 rows. Original comparison may contain failed C blocks and an overall false pass flag: the driver explicitly selects B and requires all 15 unique B blocks to pass their elapsed, immediate-memory and duration gates. It does not use C's outcome to qualify B. It consumes existing reports rather than repeating the independent raw audit; the controller remains responsible for the original phase's audit and complete immutable artifacts.

The driver verifies the current harness and build-script hashes against both original metadata and `FREEZE.json`, verifies baseline/B source identities against the freeze, and hashes the two original ELFs before each child action. The existing collector has evolved since the initial freeze, so `--collector-sha256` is mandatory: the controller must supply the hash of the exact reviewed `fleet_guards.py`. The original freeze's historical collector hash is preserved. This explicit pin prevents accepting an unreviewed collector change by merely calculating its current hash at launch.

Example invocation on the already reserved fleet host, with reviewed values substituted:

```sh
taskset -c 0 python3 experiments/ARM-LOOKUP-CONT-001/fleet_guard_confirmation.py \
  --root /reserved/experiment-root \
  --origin-phase guards-gcc15-lto \
  --cohort gcc15-lto --seed 29 \
  --collector-sha256 REVIEWED_COLLECTOR_SHA256
```

Use the original native phase/cohort for native, and `--seed 43` for the second independently qualified seed. The output name is deterministic: `<origin-phase>-confirmation-29` or `-43`. Any existing output directory prevents rerunning that phase, including incomplete, failed or parked phases. Do not bypass that protection by renaming the origin or deleting output. A future changed-condition attempt needs a distinct preregistered protocol and review.

Before creating output, the driver checks the owned, live reservation, active release timer, saved stopped coordinator identity, controller affinity `{0}`, no running Docker work and, where recorded by the lease, offline Intel sibling50 and inactive Parca service. The existing collector rechecks lease/isolation before each measured process and pins each child to CPU2. The wrapper rechecks identities and lease before each complete action. It does not acquire reservations, stop services, manipulate CPU state or manage cleanup.

The new metadata copies only the original cohort/compiler/case/referee fields and baseline/B ELF/source records; its seed and start time are new. It records confirmation origin, hashes of original metadata/qualification/comparison reports, driver/collector hashes and requested variant B. There is no C binary in confirmation metadata. Original files remain unchanged. Commands and return codes are retained in `orchestration-qualify.json` and `orchestration-compare.json`, with distinct stdout/stderr files; the collector retains individual process command/output records as usual. The command record is written before launch, so interruption leaves evidence of the attempted action.

The wrapper calls only the existing collector's `qualify`, then `compare --variants B` if all fresh A/A gates pass. It never invokes `build`. A qualification failure records PARK with `comparison_executed=false`; no comparison, retry or count change follows. Process failure leaves the phase consumed and its output retained. Completed comparison records PASS or FAIL with `source_adoption=false`. All five directions/cases retain their independent per-block ≤1% regression and immediate memory gates, A/A ±1%, minimum250ms, checksum and endpoint-reproducibility requirements from `PROTOCOL.md`. Validation memory remains diagnostic, never a substitute for the immediate endpoint.

This driver collects no counters or profiles. Supplemental-guard baseline/candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable until separately qualified captures exist. Intel lookup baseline classifications concern another workload and cannot qualify these guards.

Prepared by the independent guard reviewer under an explicit implementation assignment; root review is required before launch. Exact backend/model/token/currency costs are unknown. Own cpu-perf/library_status discovery in this session found no exposed tools; controller consultation in `../CONSULTATION.md` is shared evidence, not this worker's calls. No mechanism claim follows from the orchestration. Local validation is limited to Python compilation, static action inspection and synthetic in-memory checks of the eligibility gate; no measure/collector/fleet invocation is authorized by this preparation.
