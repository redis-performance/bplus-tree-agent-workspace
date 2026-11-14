# Offline Intel parser hardening

2026-11-14, independent reviewer; exact model, tokens and cost unavailable.

Changed only [analyse_intel_profile.py](../analyse_intel_profile.py) and this validation note. Parser SHA256: `9d4b8b838cf2bb472b42bb1210f9de6c61999b9a635bbdcc083407d5d34396a3`. No collector changes, new measurements, fleet access, commits or pushes. Existing raw captures and saved analyses were preserved.

## Qualification contract

`all_qualified` now requires all three TMA captures, process counters, samples, the sample report and recorded provenance to pass. These have separate top-level flags; command return codes, scope checks and data checks remain separately visible. Malformed/missing evidence yields an explicit failed check, not a trusted saved boolean or a successful empty report. Invalid captures cannot mark any aggregated metric qualified.

The parser independently recomputes `/proc/stat` busy ticks and `/proc/PID/stat` utime+stime, checks identity/start time, one live thread, increasing timestamps/counters, endpoint CPU2 affinity and isolation, compares saved arithmetic, then applies the registered1% bound. It also joins process identities across the non-resumed captures and verifies attached counter/sample PIDs. This remains aggregate CPU-wide attribution; endpoint checks are not continuous isolation proof.

Each of five ordered TMA windows must contain exactly four unique roots, eight unique children and MUX. Slot units, finite0–100 values,100% scheduling, the100±0.3 root partition and child partitions are checked. The child rounding allowance is0.15 percentage point: three independently rounded one-decimal values can contribute at most that residual. Numeric rows outside the CSV, unknown diagnostics, duplicate headers/columns, malformed timestamps and unsupported values fail closed. Known watchdog/advisory/footer text is retained separately.

Grouped process counters require the four expected user events,100% scheduling, equal positive running duration and valid values. Samples require existing nonempty data, a positive recorded sample count, an explicit zero-loss report, user-cycle event and successful commands. The report command must refer to the sample command's output. Verification must target the same binary and fixture; the workload must have completed the declared intentional termination. The collector/model version must match this registered cohort.

Resume qualification checks the prior sibling directory, matching metadata except start time, all four copied TMA0 files byte-for-byte and the recorded checksum. An incomplete prior attempt remains incomplete when analysed on its own.

Aggregation is explicitly **an unweighted mean of displayed interval percentages**, not a pooled slot-count ratio. The output states that original event counters and the runtime model selector are unavailable; the parser checks units and consistency, not raw-counter-derived formulas or causal explanations. Saved binary hashes are recorded provenance; this parser does not independently rebuild binaries or rehash a remote binary.

## Offline validation

Used importable `analyse(path)` and the CLI with `--no-write` on every saved Intel profile dataset available for this review:

| Saved dataset | Full qualification | CLI exit |
|---|---|---:|
| profile-native | false: aborted launch/missing scope and captures | 1 |
| profile-native-v2 | false: only TMA0 is complete | 1 |
| profile-native-v3 | true, including verified resumed TMA0 | 0 |
| profile-gcc15-lto-v3 | true | 0 |

Thirty targeted negative cases were executed on temporary copies of saved evidence. All failed full qualification; temporary copies were removed. Cases covered stale scope arithmetic, changed PID identity, online sibling, missing child, duplicate root, wrong units, broken child partition, nonfinite metric, malformed timestamp, duplicate header, failed TMA command, wrong CPU, counter multiplexing, unsupported/empty counters, failed counter command, wrong counter PID, lost/absent loss evidence, failed sample/report commands, wrong report input, absent sample data, missing scope, malformed JSON, changed resume bytes/metadata, numeric evidence hidden outside CSV, wrong model revision and verification-binary mismatch. Partial metrics were never marked qualified.

Before/after SHA256 inventories matched for all140 files across the four original profile directories, including their existing `analysis.json` files. The final parser was rechecked against all four saved datasets after the added strict checks. `git diff --check` passed. These were file/schema/correctness checks, not performance measurements.

For read-only revalidation:

```sh
python3 -B experiments/ARM-LOOKUP-CONT-001/analyse_intel_profile.py \
  build/arm-cont-private/intel-fleet/profile-native-v3 --no-write
```

Without `--no-write`, the prior behavior of writing `analysis.json` is retained. The CLI now emits the full structured result and returns1 for unqualified evidence. The detailed capture schema is richer; `metrics`, `all_qualified`, `counters_scope` and `samples_scope` remain available. This parser deliberately targets the registered collector format; a future perf/collector format change needs review rather than silent acceptance.

## Consultation

This worker's fresh tool discovery found no directly exposed cpu-perf tools. The controller's actual stdio consultation in [CONSULTATION.md](../CONSULTATION.md) is shared evidence, not a call claimed by this worker. The change implements the concrete evidence checks identified by [the independent baseline audit](INTEL-TMA-BASELINE.md); no retrieved source is claimed to establish a workload mechanism.
