# One duration diagnostic, frozen before candidate timing

Root independently reviewed the original candidate patches and semantics in main commit dd5b63d9. No semantic blocker was found; qualified controls remain mandatory. Before any candidate timing, this separate referee revision tests longer batches. It is the single allowed duration/noise diagnostic for this target. Original short-run profiles, calibration and A/A remain unchanged.

Only the existing driver maximum `--rounds` value and its help text change from65536 to100000000. Kernel, source candidates, original tests, output contract and checksums remain frozen. One identical new driver object is linked into all five sources; native and ASan/UBSan modes both rerun the unchanged test suite. Additional cap checks cover65537, accepted100000000 and rejected100000001, using `--help` after the parsed boundary to avoid an unnecessary huge run; a bounded65537 actual run also verifies accounting.

Fresh baseline-only calibration uses three observations and targets at least100ms, using the fastest positive observation and the new cap. All counts freeze before comparisons. Revised A/A uses the same29 cells, both controls and six ABBA blocks. Every timed sample must be at least10ms and every A/A block within±1% for eligibility. If it fails, no further harness or noise iteration is allowed; only the fixed exploratory screen and explicit PARK remain.

Budget declaration before candidate data: calibration and A/A each300seconds; each29-cell candidate/root screen300seconds; a complete176-cell selected-candidate guard phase and fresh confirmation may each use600seconds to fit the100ms target. Every child remains capped120seconds, and all jobs remain within the lease deadline. These budgets are fixed now; no extra time will be granted to chase a win. A duration change can alter noise; a successful requalification alone does not prove short duration caused the earlier variation.

The scope remains conditional on unadopted EXP-007 B. The unchanged-root scalar adapter stays a separate control. No adoption, public-tree claim or historical guard removal is authorized by this diagnostic.
