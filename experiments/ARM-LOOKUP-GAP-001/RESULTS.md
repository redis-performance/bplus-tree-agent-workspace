# ARM lookup investigation: reject the tested optimization

**REJECT / source selection NONE.** The current-source standalone fixture reproduces lookup cost concentration. Three independent proposals converged on deferring an unused logical-position calculation; all three implementations pass correctness, but none clears the registered 2% primary speed gate. No optimization was adopted or sent upstream.

The baseline is synchronized with Redis unstable **`ee8e7f70152404649ac947157fd662d11b4a00d5`**. Fetch/byte verification at 22:25:57UTC and final fresh fetch at 22:43:51UTC agree. Both B+ tree files and the same-pin SipHash/SDS/test dependencies match upstream exactly. The relevant files happen to equal the earlier squash; the squash is retained as historical provenance, not used as a substitute for current unstable. [Manifest](unstable-manifest.json) · [Final verification](final-upstream-check.json) · [Extraction audit](SOURCE-AUDIT.md).

## What the measurements establish

The fixture builds two distinct 500-member trees, models the initial 128→129-member conversion, and performs ascending successful raw membership lookups without requesting scores. Construction and iteration are outside timed intervals. The primary median is 29.867ns/lookup on the qualified ARM baseline. All 48 A/A rows pass:12/12 blocks across primary, score-returning, missing-member and256-byte guards fall within±1%. [Baseline and scope](BASELINE.md).

Whole-process user-cycle sampling places **41.91%** of sample weight in the leaf membership helper and **21.91%** in raw lookup. SipHash accounts for 6.75% and named libc memcmp 3.45%. Several libc PCs remain unresolved. The leaf helper combines tag search, packed-record decoding, equality checks and optional outputs; flat samples do not separate their individual costs or charge all helper time to its call boundary. Long-member sampling shifts 45.22% to SipHash. These are localization results, not a measured explanation of the entire command-level ARM gap or an ARM-versus-Intel comparison.

Exact ARM assembly exposes one unnecessary operation: after a verified hit, the baseline computes physical-to-logical leaf position before testing the optional score pointer, while the position output is already specialized away. All three proposals independently selected this narrow question; none proposed changing the scanner or decoder. Candidate assembly moves that work behind output requests. [Population chair](selection.md) · [Proposals](proposals/) · [Retained patches and correctness](variants/).

## Fixed discovery comparison

Negative elapsed-time differences are faster. Each cell contains three same-session ABBA blocks with 50 million lookups per process. All 144 rows completed, with equal checksums and tree-owned memory. All 48 baseline and 144 comparison unprofiled timing rows are retained; no timing attempt was retried or discarded. Six separate instrumented baseline runs (three counter, two sample and one topdown capture) are preserved outside those 192 rows.

| Variant | Primary median | Primary block range | Score guard median | Missing guard median | 256-byte guard median | Decision |
|---|---:|---:|---:|---:|---:|---|
| A: guard output block | −1.394% | −1.709% to−1.175% | +0.189% | −0.002% | −0.705% | Reject: primary below gate |
| B: early success return | −1.528% | −1.571% to−1.418% | +0.006% | +0.090% | −0.726% | Reject: primary below gate |
| C: mapping per output | −1.841% | −2.182% to−1.481% | +0.083% | −0.067% | −0.743% | Reject: only1/3 primary blocks clears gate |

No measured guard block exceeds +1%; the largest is C's score guard at +0.961%. That does not rescue the failed primary gate. The discovery medians are observations, not confirmed speedups or acceptance evidence. C is not selected simply because its median is numerically largest. [Raw rows](comparison/rows.jsonl) · [Reproducible analysis](comparison/analysis.json) · [Binary/source identities](comparison/manifest.json).

Fresh-seed A/A/confirmation, selected-candidate profiles and Intel replication were **not executed** after the rejection. Their prepared scripts are unexecuted artifacts, not queued work. No candidate dynamic-instruction reduction, validated causal profile change, Intel neutrality or command-level recovery is claimed. The baseline remains unchanged.

## Correctness and review

Baseline and each candidate pass 57 upstream tests in native and ASan/UBSan builds, plus 12 native and 12 sanitizer fixture cells. Each also passes 90,000 correctness-only optional-output checks covering score/position masks, reversed leaves, exact signed-zero bits and binary long members. An independent reviewer identified a documentation error: 256-byte members are inline here, since external storage begins at 320 bytes. The timing fixture and original logs were preserved; descriptions were corrected. A separate 384-byte oracle asserts external record tags and passes 45,000 additional sanitizer checks on every build. No external-member performance result is claimed.

Three actual independent proposers and three isolated implementations ran the population steps. A separate adversarial reviewer independently reconstructed source identities and raw A/A results, then audited the comparison decision. Exact model/token/currency costs remain unknown. [Independent review](review/FINAL.md) · [Preliminary correction](review/PRELIMINARY.md) · [Methodology consultation](CONSULTATION.md).

## TMA classification

| Category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

The actual topdown-profiler 0.2.3 wrapper produces `perf stat --topdown -I1000 -x, -a -C2`. Perf reports version 6.17.13 despite its 6.14 kernel-tools path. Six baseline windows are labeled percent-of-slots: Frontend 5.4%, BadSpeculation 1.8–1.9%, Backend 41.5–41.6%, Retiring 51.2%, approximately 100% within rounding. This CPU-wide capture lacks continuous exclusion evidence, and its labels alone do not validate formulas or process isolation. It remains exploratory, with no qualified child metrics. No candidate capture ran after rejection. Raw commands, collector source checksum, binary identity, CPU2/no-SMT scope and counter scheduling are in the baseline evidence. Stall cycles and flat samples were not converted into TMA.

## Completion and next question

The ARM fleet lease was released and independently checked at 22:43:55UTC: original coordinator identity resumed, zero owned processes or benchmark containers, work unit and release timer inactive, PMU/SMT settings unchanged. Fresh coordinator heartbeat and empty pending/lag checks followed. [Sanitized release proof](RELEASE.json). All operational identities/raw profiles stay outside the public repository. No workstation performance measurement ran.

This closes one measured optimization population, not the overall ARM gap. The next useful investigation is to resolve the remaining libc PCs and separate leaf tag/record work from helper-boundary costs with a newly preregistered experiment, preserving this rejection and rechecking unstable. Do not rerun the same candidate unchanged to chase the2% threshold. Historical rejected scanners and decoder changes remain rejected/parked.
