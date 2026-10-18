# Round5 adversarial review — sequential coordinator pass

No independent reviewer ran: startup failed before context loading. This read-only
review is separate from implementation/analysis passes but is not independent performance
confirmation, a population, or evidence of a second backend/model. Costs unknown.

- Source/ownership: root target and HARNESS-001 referee hashes match their pins. New
  diagnostic/calibration/referee binaries live in separate snapshots. No source candidate
  exists. Batch and raw-buffer tests mutate only through public APIs; private reads in
  batch tests establish active resize, never force it. Raw buffers are explicitly read-
  only during use and unmapped before ownership checks. Empty guard pointers are non-NULL;
  no NaN or unsupported batch count introduced. Missing batch score slots remain unspecified.
- Harness: HARNESS-003 changes only miss warmup and records actual warmup operation.
  Measured operations/checks/counts are unchanged; other cases still warm with hits and
  the metadata says so. Warmup time differs between arms by design, so DIAG-008 is a
  bundled operation/time-history intervention, not a cache-only causal result.
- Timing: every fixed schedule completes; phase diagnostics retain every short window
  and explicitly treat processes as clusters. Observation-gap bounds do not establish
  code-layout neutrality. Thread brackets enclose wall clocks, allowing tiny ratios>1;
  no clamping/filtering. AA-004 still fails all four unchanged precision gates, including
  the nearly passing cell. No optional stopping, relaxed guard or optimisation claim.
- Profiles: DIAG-009 fixes the archival calibrate interface in a new snapshot and keeps
  output outside clocks. It adds no handler library/timestamp calls. Sample-count/thread
  duration ratios include boundaries/handler cost and do not prove exact cadence or CPU
  frequency. Rates measured on the arithmetic loop must not be carried to tree workloads.
  All known-function samples resolve; this does not establish unbiased time fractions.
- Test strength: exhaustive batch masks/counts plus duplicates, exact score bits and
  output canaries detect both predeclared semantic faults. Guard-page buffers at33 lengths
  detect overread and truncated-hash faults. First guard-test compile failure is retained;
  only string.h was added, without weakening assertions or changing fixtures.
- Evidence: independent PRNG reconstruction in read-only audit verifies measured
  fingerprints; all raw/source/binary hashes and fixed schedules checked, phase/ABBA/rate
  decisions independently recomputed. Prior frozen evidence untouched. Audit is not an
  independent experiment or statistical confirmation. CPU MCP heuristic metadata misses
  are disclosed; unknown clock/effective QoS/residency remain unknown.
- Acceptance: NONE/PARK remains mandatory. Both population stages, suitable qualified
  target/guards, matched profiles, fresh independent confirmation, source commit review
  and independent adversarial review remain open. New tests/harness artifacts are useful
  local preparation and await morning review; no publishing or upstream action authorised.
