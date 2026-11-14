# Slot-hint census: completed execution operational audit

**PASS for the completed, admitted structural census.** All twelve scheduled case invocations and both output-checker invocations succeeded. This establishes execution and artifact consistency for the frozen diagnostic. It does not qualify performance, adopt a source change or authorize further execution. The separate semantic review assesses the structural observations. H2 and Q4 remain PARK, selected source remains NONE, and the performance population remains 47.

This reviewer performed the earlier operational, wrapper and staging reviews and authored their independent synthetic tests. The diagnostic implementation and semantic review have separate authors. This final audit used saved artifacts and local Python checks only; it made no fleet request and executed neither diagnostic ELF.

| Bound evidence | SHA256 |
|---|---|
| Census execution approval | `1c9bfc562da0290a92fa1e9e8ba3547b4b7c5e36ec5a43286a4fc93f21c73941` |
| Source freeze | `f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b` |
| Configuration | `5398c7efc9367a0f6b75db40ae8a85fe9d060ef2b015e7f9dc7e5f128cc6edf1` |
| Successful staging receipt | `f02f7d742f9ccd8c974acd7ccf227ff48e785fdcb0465b976ea5ce0c0e06748e` |
| Completed build receipt | `3e1cc2e88d5ae7eb14e113182da1823c00d46e3161d446b3458b6f2dd4f1fc13` |
| Native ELF | `8facf50e3c68a07ecc738aed446a0f0f9290e85e5d69c26e82d727e98031687c` |
| LTO ELF | `0a9c7f0dca40d181bd8770dcd0c46c7eb9030ca584749dfc2e0db6514cedaf39` |
| Final private operational audit | `2bf655e95b70ea19a9b2db23a4f11fe9eb05c57dd8f438535e742e868f285b7d` |

All 105 inputs were independently rehashed again. The configuration, fetched approval, original staging receipt, completed build receipt, two actual ELFs, assembly and compiler records match the admitted bytes. All 42 build-receipt entries still match. The original and published target-code reviews and their publication manifest match the approval. There was no source, compiler-flag, fixture or ELF substitution between build admission and execution.

The fourteen raw command records match the frozen sequence exactly: six cases and one strict checker for native, then the same sequence for LTO. Every diagnostic uses CPU 2, a 60-second outer cap with a 43-second GNU timeout and 15-second kill allowance. Checker commands have a 120-second cap and 103-second timeout. All return codes are zero and all command stderr files are empty. There is no recorded retry or extra case. The terminal record names exactly the twelve cases and reports `COMPLETE_STRUCTURAL_COUNTS`, with qualification and source adoption both false.

The actual service identity and command line bind the approved configuration, staging receipt, approval and absolute-deadline wrapper. Its properties match the reviewed census launch: `Type=exec`, startup limit 30 seconds, runtime ceiling 240 seconds, stop allowance 15 seconds, control-group termination and SIGKILL enabled. The service controller runs on CPU 0. The immutable **06:45 UTC on 2026-11-14** deadline remains in the actual command. All recorded phase isolation checks precede that ceiling; this is an operational bound, not a performance measurement.

Thirty-one raw isolation grids passed independent replay: prelaunch, admission, twenty-eight command boundaries and final isolation. All 310 underlying inspection commands succeeded. Recorded coordinator identity/stopped state, CPU state, exact saved profiler unit/inactive state, empty running-container listing, two active release timers and their exact schedule/precision, cleanup command hashes/service limits, and both inactive retired timers match the infrastructure record. These samples do not establish continuous absence of interference between checks.

Both strict Python checkers were rerun locally against the saved raw outputs. Their results exactly match the saved fleet checker outputs. All six native/LTO raw output pairs are byte-identical, including the full event arrays. The per-case copies also match the original command stdout bytes. Each case reports completion after cleanup, zero live generations, successful verification and untimed operation.

| Case | Counted operations per ELF | Hits | Original owned bytes before / immediately after / after validation | Reported useful queries |
|---|---:|---:|---:|---:|
| hit | 500 | 500 | 14,272 / 14,272 / 14,272 | 124 |
| score | 500 | 500 | 14,272 / 14,272 / 14,272 | 124 |
| miss | 500 | 0 | 14,272 / 14,272 / 14,272 | 0 |
| long | 500 | 500 | 146,656 / 146,656 / 146,656 | 118 |
| external | 500 | 500 | 217,600 / 217,600 / 217,600 | 126 |
| update | 1,000 | 1,000 | 14,432 / 14,432 / 14,432 | 248 |

Every fixture uses seed 17, 500 members and 1,000 warmup sweeps. The update case has **two counted sweeps**, as frozen in the original checker and harness; each other case has one. Thus there are 3,500 counted operations per ELF, 7,000 overall. The earlier build review's phrase “one fixed sweep” should read “one scheduled invocation of each frozen case”; it did not alter the admitted code or update count. The final audit initially repeated that wording in an assertion, then corrected only its own assertion to the frozen case-specific count. The initial reviewer script and correction record are retained.

The bytes column is the original allocator's owned-memory model, not total process memory including shadow instrumentation. All counted resize endpoints are zero. The retained phase summaries have setup ID writes and hint-seeding activity, but zero ID writes, invalidations and seeding in warmup/count/validation phases. Score updates therefore do not establish dynamic hint-invalidation coverage in these fixtures. No split/merge/defrag or live migration coverage should be inferred merely because those source hooks exist. The strict checker and independent semantic review retain their documented bounded-history limits. Useful-query counts and filter disagreements are structural observations; they imply no saved cycles or net performance gain.

The controller's fetch receipt reports inactive work with zero main PID and no owned work before and after transfer. The saved archive receipt records 607,195 bytes and SHA256 `d255033ba0473657a09eee23aedaadc9f65711f617f722f02a3ded482e8a9051`. This reviewer independently verified extracted-content hashes, but did not independently observe the live fetch checks or rehash the unavailable archive stream. Extracted ownership and permissions are not remote metadata proof. This audit does not establish fleet release; release requires its own live identity and restoration checks.
