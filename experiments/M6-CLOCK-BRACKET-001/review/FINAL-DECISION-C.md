# C — final instrumentation and decision review

**PASS: empirical harness/control validation is separate from physical accuracy; the fresh baseline is PARK/source NONE.** No source candidate was implemented, timed, accepted or rejected. The guarded physical-slot idea remains unresolved. No clock substitution, gate relaxation, row exclusion or retry is justified.

I independently read the72-row control CSV and all48 A/A CSVs, reconstructed their clock algebra and all12 block decisions with integer sums, and compared raw hashes/rows with journals and summaries. I did not import driver calculations or read B's new post-run audit. Both the80-entry input and285-entry build tables still match actual files; build/controls/A/A final states are COMPLETE/release-safe. The full native lease is RELEASED with no queued work. This decision review complements, and does not impersonate, B's complete raw/process audit.

## Instrumentation result

All72 fixed control rows pass their declared structural/output/blocking-sensitivity checks:24 each empty/CPU/block in fixed order, exact CPU checksum3294929107973101697, and every20ms blocking request observed by the fixed≥90% residual detector and same-clock sleep bracket. Interrupted/overshot sleep values remain; syscall continuation is not a schedule retry. These are empirical demonstrations on these rows, not an accuracy calibration or a proof that arbitrary off-CPU time is measured exactly.

Exactly three empty controls have measured I=M=0 with T>0: repetitions1,12,13 yield292,250,375ns respectively. Their zero-error CPU intervals are empty and remain explicitly INCONCLUSIVE. They are not hidden, clamped into fabricated valid intervals, or treated as new fatal structural errors. They demonstrate that the literal zero-error accounting model is not universally compatible with these recorded short intervals. They do not identify quantization, accounting lag or another implementation detail as the unique cause.

All48 lookup model intervals are nonempty, and their recorded margins M are0–4000ns. Nominal resolutions are1000ns wall and42ns thread. Neither fact supplies a worst-case accuracy/accounting bound; M=0 does not prove zero read overhead. Under the ideal assumptions, I=w2−w1, T=t1−t0 and M=(w1−w0)+(w3−w2) yield CPU[max(0,T−M),min(T,I)] and off-CPU[I−T,I−T+M] intersect[0,I]. Those remain **conditional model intervals, not confidence intervals or validated physical bounds**. The three empty-control inconsistencies reinforce this limitation.

The lookup residual I−T is off-CPU time minus boundary CPU work plus clock error under the accounting model; a small measured bracket margin does not eliminate the unmeasured error term. Empirical sleep sensitivity does not turn lookup residuals into exact descheduling. No CPU-type/residency/DVFS/cache or migration cause is established, and endpoint equality cannot exclude intermediate migration.

## Baseline qualification

All48 A/A rows and all12 blocks remain. Every measured wall window is594.536–650.797ms, above10ms. The100K wall controls qualify6/6;1M qualifies2/6. The failed1M blocks are:

| Block / seed | Wall effect | Thread effect, diagnostic only |
|---:|---:|---:|
| 0 / 1 | +3.418338086% | +3.395634280% |
| 1 / 2 | +1.014037726% | +0.987702760% |
| 3 / 1 | -1.573060730% | -1.482851843% |
| 5 / 3 | +1.253821892% | +1.238471342% |

The block1/seed2 wall contrast+1.014037726% fails, while its thread contrast+0.987702760% passes. Even its narrow *zero-error conditional* CPU contrast interval, about+0.987218..+0.988193%, cannot rescue the wall gate: it assumes unvalidated accounting and is a different metric. Thread diagnostic qualification is3/6 at1M; the preregistered wall result remains2/6. All other failed wall blocks remain visible. These are same-binary noise controls, not candidate gains or evidence of a source regression.

No hypothetical100K-only primary, CPU/ISA dispatch, count increase, new failed-row tolerance or successful control subset can replace both-size/every-block qualification. The original fixed counts, fixtures, native source and corrected adapter are unchanged. EXP-009's original old-frontend PARK and the offline metrology result remain frozen; do not compare separate sessions as an optimization gain. Harness validation and baseline precision failure can both be true.

## Refinement chronology and provenance

Git objectc9994a3a7e825ed792141884204afe402c9569cc includes exact PLANrevision2 and C's pre-native explanation before the first build. Its commit timestamp15:07:23UTC precedes actual build start15:07:35.691150UTC; the original PLANv1 hash13a54e9306de2dcfa65f3970af5cc2b9e55fb676f4aa4d4c1ff189ab40eea1c8 is preserved in plan-history. Published revision2 hashb50d0fe0d7c553f872075815b70f4c7e066a30efb33c77ab4f3e4c1d6aea2c5e matches current/frozen PLAN. The empty-interval refinement therefore preceded all native observations; it is not a retrospective exception for the three observed rows. No guessed accuracy tolerance was introduced.

Actual source/header hashes remain d912/496e; corrected adapter468a/c923 remains separate from original legacy004 timing. Inputs/build artifacts are hash-pinned; no production source optimization or population is added. Later source work would still require fresh profiling, qualified full controls/guards, actual proposals/chair/isolated implementations, confirmation and adversarial review. No unchanged schedule rerun or new native work is queued by this decision.

## Mandatory consultation and scope

Own enabled-tool availability search found zero direct CPU-perf tools. I explicitly consumed root's real shared stdio results consultation (cpu-perf0.1.1, bundleddeb5a0bac467,2/287indexed/93passages); these are **not my server calls**. Exact shared inputs, UTC times and response hashes appear in the JSON without source bodies. They occurred after native-release observation.

The shared ask misclassified the control/lookup CSV as perf stat-x, then inferred false0% counter multiplexing from unrelated fields including QoS metadata. **No performance counters were collected.** That parser output and its unrelated top-down/counter advice are inapplicable and were not used. The retrieved [Linux clock manual](https://man7.org/linux/man-pages/man2/clock_gettime.2.html) states that the thread clock “measures CPU time consumed by this thread”; it does not validate Darwin accuracy or establish a present migration-clock bug from historical Linux SMP text. No M4/other-host MCP performance number transfers. Source ordering and conditional algebra, not MCP parser guesses, support this review.

Participant `/root/followup_proposal_c`, Codex/GPT-6 family; exact serving model/token/currency cost unknown. Prior pre-native/bracket/metrology reviewer disclosed. Only FINAL-DECISION-C.md/json were written. No native/build/profile command, source/frozen edit, retry or Git mutation was run. All review activity stopped; root alone publishes the final report and evidence on main.
