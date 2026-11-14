# Independent supplemental-guard review

**Current verdict (revision 1, 2026-11-14): GO for controller freeze.** Both original blockers are resolved. This permits protocol/identity freeze, not candidate acceptance or a performance claim. The original review below is preserved; the revision 1 rereview follows it.

**HOLD before fleet freeze: two methodology issues require correction.** No source-semantic failure found in the supplied verification cells. This reviewer did not author or edit the guard harness, access a runner, run measurement mode, commit or push. Only this review file was written.

Reviewed `guards/{guards.c,PROTOCOL.md,README.md,build.sh,verify.py,correctness-manifest.json}` plus recorded correctness calls and relevant public tree implementation. Reviewed referee C SHA256 `7386bb5d1be5cd796946d76f452a104b93f15181dd01782b6734652174d74a4a`. Baseline source SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`; H2-B `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29`; H2-C `789ca7e217baa67cba165d2ebed7be0c9c1a2a7067f94ae870431395e66ffe49`. All checked against current files.

## Blocking finding 1 — memory endpoint occurs after mutating validation

`guards.c:218–220` calls `check_tree()` before reading `owned_bytes_after`. The protocol promises an immediate post-timing endpoint. `check_tree()` is not physically read-only: its rank/score calls reach `zbtIndexFind()`, which advances incremental rehash when one is active. It can therefore migrate/finalize an index before the memory sample, potentially hiding the memory actually present when the timed loop ended. This is a proven call-path difference; this review does not claim a measured memory distortion in the current cohort, since no timing was run.

Required correction: read and retain tree-owned bytes immediately after the measured loop/timer and before any validation lookup. Optionally retain a separately named post-validation endpoint too. Apply the declared≤1% memory bound to the actual pre/post timing endpoints. Clarify that transient peaks are still unmeasured. Keep both endpoints reproducible per binary/case, without requiring pre==post in churn. Refreeze/revalidate after the change; do not repair prior measured rows if any exist.

## Blocking finding 2 — directional regressions can cancel

`guards.c:93` alternates directions inside one iterator/rank elapsed result. A forward improvement can offset a reverse regression, so the single≤1% aggregate guard does not bound either direction individually. That matters for H2's metadata/flags and the historical direction-sensitive iterator failures. Mixed-direction traffic is a legitimate workload, but it cannot supply separate forward/reverse acceptance coverage.

Required correction: give forward/reverse iterator and rank paths separately named, fixed cases with independent A/A qualification and≤1% per-block candidate gates. Preserve or deliberately omit the mixed case before freeze; do not use it as a replacement for per-direction results. Adjust process counts, checksums, explicit workload dimensions and lease budget. Physical reversed-leaf representation remains distinct from traversal direction; the protocol correctly discloses that separate limitation, and existing semantic oracles still apply.

## Verification performed

Independently audited all216 recorded calls: every command is verify-only, return code0, empty stderr, expected verified output and no elapsed field. Verified current referee/source hashes and all six local executable hashes against the supplied manifest.

Independently ran18 fresh verify-only cells: baseline/H2-B/H2-C × native/ASan-UBSan × iterator/rank/churn, seed43,7sweeps. Seven is a new odd endpoint relative to the author's1/2/5/8 grid. All passed with3500 operations; same-mode outputs and both memory values match across baseline/B/C. No clock/PMU or measure mode was invoked. Native churn reported before14272/after10816 bytes; sanitizer before14277/after10752. These are correctness endpoints under different allocator instrumentation, not comparable performance measurements or proof of which action changed memory.

## Reviewed aspects that pass

- Construction matches the short lookup fixture's reserve129/raw-first128/general-rest sequence, with distinct member strings and public APIs.
- Verify mode rejects counts above8 and never enters the timer branch. Setup, warmup and full validation lie outside the timed interval; checksum accumulation and fixed safety/count assertions are explicitly inside.
- The even measurement count and1000-sweep warmup restore churn's model to integer scores. Odd verify runs update their model correctly. The0.125 increment preserves order and is exactly representable.
- Iterator checksums include score sum and direction-sensitive weighted sum; rank adds successful count/rank sum and weighted rank association. Churn input checksums are honestly distinguished from observed output; successful deletes plus final model checks cover the measured logical result, while verify checks each transition.
- Planned integer/dyadic sums stay within exact double integer/fraction precision at the proposed counts. Counts and operation units match their descriptions: returned iterator elements, rank queries, and mutation pairs/two API calls.
- Supplemental tests do not replace the original primary, external-record/ownership, packed-flag/cache, signed-zero, resize or upstream semantic gates.
- Each compiler/architecture cohort has its own controls and binary/source identities, no pooling, no silent retry and a250ms minimum. The proposed counts are planning estimates rather than claimed durations. They must be recomputed for the split-direction design before freeze; actual fleet admission remains the controller's responsibility.
- The intended post/pre memory gates do not waive H2-A's prior memory failure; the acknowledged absence of transient-peak accounting is appropriate. Finding1 must still be fixed to make the endpoint names truthful.

## Review provenance and TMA

Independent reviewer backend/model/token/currency costs unknown. Fresh cpu-perf/library_status tool discovery returned no exposed tools. This review consumes the controller's shared consultation in `CONSULTATION.md` under the documented worker provision; it does not claim those calls as its own. No supporting retrieved passage establishes a workload cause, and none is needed to identify these harness/control-flow issues.

Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring are unavailable as qualified guard baseline/candidate categories; no guard performance profile was run. Children unavailable. This review supplies correctness and measurement-design evidence only, not pipeline-slot classification.

After both corrections, rerun verify-only checks, refresh manifests and request independent rereview before timing. No source or harness edits were made by this reviewer.


## Revision 1 independent rereview — 2026-11-14

**GO for controller freeze; no remaining blocking review finding.** Independently reread the revised source, protocol, README, build/verification drivers and manifest. Confirmed `guards.c` SHA256 `f1e67e306afdd59b5e0eff8b67025129227aebf037ded199a026d87c63f9049e`. The baseline/B/C source identities remain those recorded above. The author preserved revision 0 separately; this review does not supersede its historical HOLD retroactively.

Finding 1 is resolved: after the selected loop and (only in measure mode) stop-clock call, `zbtreeAllocSize(t)` captures `owned_bytes_after` before `check_sums()` or `check_tree()`. The second allocation sample is explicitly `owned_bytes_after_validation`. Protocol and README apply the memory gate independently to before/immediate-after values, treat after-validation as diagnostic, require endpoint reproducibility, and retain the transient-peak limitation. Verify-mode churn checks inside the loop can still advance physical state; its endpoints are correctness evidence, not substitutes for fleet measure-mode endpoints.

Finding 2 is resolved: iterator-forward, iterator-reverse, rank-forward and rank-reverse select a constant direction throughout their own process; churn is the fifth case. Each case has separate three-block A/A qualification and candidate regression gates. The analytical weighted checksum is now forward sum(i²) times sweeps or reverse sum(i*(501−i)) times sweeps, as appropriate; rank totals and fractional churn expectations remain consistent. Setup, 1,000-sweep warmup, full model checks and JSON output stay outside timing. Even measure counts restore the final integer-score model, while odd verify counts update the model explicitly. No new equivalence or arithmetic defect found.

The revised process arithmetic is correct: five cases × three ABBA blocks × four rows = 60 A/A rows; 60 rows per candidate yields 120 comparison rows for B/C and 180 processes total per cohort. Separate iterator cases retain 1,000,000 sweeps each, rank cases retain 200,000 each and churn retains 20,000. Duration remains unproven until qualified fleet execution. The controller must accommodate the increased workload in the live reservation and cleanup budget. A failed/sub-250ms window parks its cohort under the registered rules; this review grants no exception or retry.

Independently verified all manifest referee/source hashes and all six executable hashes. Audited all 360 recorded calls, including the exact five-case × three-seed × four-count grid per executable: each command is verify-only, returns zero, has empty stderr, reports verified with expected operation count and no elapsed field. Recorded same-mode output files match exactly between baseline/B/C.

Independently executed 30 fresh verify-only cells: baseline/B/C × native/ASan-UBSan × all five cases, seed 43, seven sweeps. Every cell passed with 3,500 operations and no elapsed field or stderr. All output fields, including before, immediate-after and after-validation owned bytes, match exactly across baseline/B/C within each build mode. Forward iterator/rank weighted sums were 292542250; reverse sums were 146709500; churn weighted sum was 292604875. Native churn endpoints were 14272/10816/10816; sanitizer endpoints were 14277/10752/10752. These are correctness observations under their own instrumentation, not timing, peak-memory bounds or cross-allocator comparisons.

Remaining limits are explicitly scoped: score-only iterator timing, 500 short members, position-preserving churn and logical traversal direction do not establish coverage of every physical leaf representation, ownership mode, resize pattern or transient allocation. Existing broader semantic oracles and original performance/confirmation gates still apply. The original failed LTO qualification remains PARK; this review supplies no LTO or architecture performance qualification.

Own fresh cpu-perf/library_status name discovery again returned no exposed tool. Shared consultation limits and unavailable TMA categories remain as recorded above. Reviewer backend/model/token/currency costs remain unknown. No harness/source changes, measure mode, timing/PMU collection, fleet access, commits or pushes were performed. Only this review file was updated.
