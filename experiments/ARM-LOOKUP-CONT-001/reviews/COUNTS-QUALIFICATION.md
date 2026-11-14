# Continuation qualification counting audit

Reviewed 2026-11-14. **Recommend closing two distinct qualification attempts, each once, and updating the current totals to 40 completed / 22 PARK / 18 REJECT / 0 approved; ARM 29 / Intel 6 / AMD 5; 24 populations / 5 replications / 11 qualifications.** H2, H3 and H4 remain active and excluded from completed decisions. This is a bookkeeping recommendation; shared ledgers were not edited.

## Counting basis

The [published counting rules](../../EXPERIMENT-FLOWS-20261020/README.md#counting-rules) define one recorded attempt as a population, exact-patch replication or qualification; A/B/C variants are not separate attempts. Approval requires an adopted source optimization. Baseline runs, profiles and oracles are supporting work rather than extra populations.

The current [experiment ledger](../../EXPERIMENTS.md) and [summary](../../SUMMARY.md) explicitly add Q1 and Q2 as **two** qualification attempts, even though each contains native and GCC15/LTO compiler cohorts and 144 rows. The same paragraph assigns renewed native controls to H1 rather than adding an attempt. Thus compiler cohort, A/A block, profile capture, implementation variant and ordinary supporting requalification are not the counting unit.

The new ARM protocol is independently preregistered changed-condition metrology: fivefold work counts plus CPU0 controller isolation, with prior Q2 failure preserved. The new Intel protocol is separately scoped to a newly qualified architecture and includes both compiler controls and baseline profiling. These are two distinct qualification protocols, rather than three attempts for their three compiler cohorts. Their subsequent candidate comparisons stay inside the corresponding hypothesis population/replication decision; never count these same qualification rows again there as additional attempts.

A terminology caveat must accompany closure: **qualification PASS; ledger disposition PARK / source NONE**. These completed controls passed. PARK here records that the qualification attempt itself adopts no optimization and leaves downstream acceptance pending; it must not be described as failed/noisy qualification. The ledger's three adoption-outcome buckets have no separate QUALIFIED-only category. Preserve the successful operational qualification in an explicit field or sentence. Q1/Q2 retain their actual failed qualification outcomes unchanged.

## Evidence for the two closures

| Proposed unique record | Architecture/type | Completed evidence | Qualification outcome | Ledger outcome |
|---|---|---|---|---|
| ARM-LOOKUP-CONT-001-Q3-LTO-LONG | ARM / qualification | [Protocol](../LTO-LONG-COHORT.md), [completion](../lto-long-qualification/COMPLETE.json), [analysis](../lto-long-qualification/analysis.json), [raw rows](../lto-long-qualification/aa.jsonl) | 72 rows, 18/18 blocks pass; completed 01:45:07 UTC | PARK / source NONE; qualification PASS |
| ARM-LOOKUP-CONT-001-Q-INTEL | Intel / qualification | [Protocol](../INTEL-COHORT.md), [completion](../intel/qualification/COMPLETE.json), [analysis](../intel/qualification/analysis.json), [raw rows](../intel/qualification/aa.jsonl), [independent TMA review](INTEL-TMA-BASELINE.md) | 144 rows, 18/18 blocks per compiler pass; A/A completed 01:40:12 UTC; both baseline profile cohorts independently audited by 02:04 UTC | PARK / source NONE; qualification PASS |

These proposed IDs distinguish the protocols without renumbering prior history. Both pin upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`; current source SHA256 is `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.

I independently counted 72/144 raw JSONL rows, grouped all 18/36 blocks, checked slots 0/1/2/3 and ABBA labels, seed17, within-block operation/checksum/memory equality, and recomputed every mean-ratio effect and minimum window against the analyses. All agree and pass. ARM maximum absolute A/A is 0.474174961%; minimum window 2.374480842 seconds. Intel maximum absolute A/A is 0.631511106%; minimum window 2.037196910 seconds. This offline audit does not repeat process/source/ELF or TMA quality audits; the existing independent TMA report is the authority for the latter. No new measurement was run.

The invalid Intel profile launch and parser correction remain evidence within this Intel qualification, not extra completed qualification attempts. Native profile v3 resumes the valid first capture byte-for-byte and supplies the remaining captures under the declared repair. Separate files or repair labels do not create a new counting unit. Likewise the 360 local guard verification cells, 30 independent guard checks and supplemental guard protocol freeze add no completed population or qualification while their fleet stages remain active.

## Arithmetic

| Dimension | Current | Delta | Proposed |
|---|---:|---:|---:|
| Completed attempts | 38 | +2 | 40 |
| PARK | 20 | +2 | 22 |
| REJECT | 18 | 0 | 18 |
| Approved | 0 | 0 | 0 |
| ARM | 28 | +1 | 29 |
| Intel | 5 | +1 | 6 |
| AMD | 5 | 0 | 5 |
| Populations | 24 | 0 | 24 |
| Replications | 5 | 0 | 5 |
| Qualifications | 9 | +2 | 11 |

Cross-checks: 22+18+0 = 29+6+5 = 24+5+11 = 40. A hypothetical 41 total would incorrectly count the Intel compilers twice. Closing H2/H3/H4 now would incorrectly count unfinished work. Neither a failed H2 implementation nor correctness-ready H3/H4 patches constitute additional completed populations.

## Exact proposed ledger edits

1. Prepend a dated addendum to `experiments/EXPERIMENTS.md` and `experiments/SUMMARY.md`, retaining the earlier 38-attempt checkpoint:

   “14 November: two additional qualification protocols complete. ARM long-window/controller-isolated GCC15/LTO passes all 18 blocks/72 rows. Independent Intel native and GCC15/LTO each pass 18 blocks, 144 rows total, with both baseline TMA cohorts independently audited. Record each protocol once as PARK / source NONE, with qualification PASS; these are not failed controls or adopted optimizations. Prior Q1/Q2 failures remain unchanged. Completed totals: **40 attempts / 22 PARK / 18 REJECT / 0 approved; ARM 29 / Intel 6 / AMD 5; 24 populations, 5 replications, 11 qualification attempts.** H2/H3/H4 remain active and excluded.”

   Link the two records to the protocol/evidence paths in the table above. Preserve renewed native H1 controls as supporting work, not an additional attempt.

2. Replace the current count sentence in `README.md` with:

   “**40 completed experiment attempts: 22 parked · 18 rejected · 0 approved.** ARM 29 · Intel 6 · AMD 5. Includes 24 populations, 5 replications, 11 qualification attempts; active work excluded. The latest two qualification protocols passed; their PARK disposition records no source adoption.”

   In its current activity paragraph replace “Independent metadata work and Intel qualification are underway” with “Metadata, short-equality and raw-state work remain active; ARM long-window LTO and both Intel compiler qualifications are complete.” This change does not close the campaign.

3. In only the current-summary sentence at the top of root `EXPERIMENTS.md` and `SUMMARY.md`, replace “38 completed attempts, 20 parked, 18 rejected, 0 approved” with “40 completed attempts, 22 parked, 18 rejected, 0 approved”. Keep the historical notes intact.

4. In the top active continuation blocks of `.workspace-memory/{MEMORY.md,LIVE-STATUS.md,handoff.md}`, update the current aggregate to “40 completed attempts, 22 PARK, 18 REJECT, 0 approved; ARM29/Intel6/AMD5; 24 populations/5 replications/11 qualifications; active H2/H3/H4 excluded.” Add “Two additional qualification protocols complete and pass; ledger PARK means no adoption.” Do not globally replace numbers in historical checkpoints.

5. If the controller updates `STATUS.md`, distinguish completed qualification from active candidate work using the same labels. Historical October charts and their sealed JSON/validation totals should stay historical; this audit does not request regeneration or modification of them.

## TMA and consultation provenance

This is a ledger audit, not a new performance experiment. ARM long-window qualification has Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children unavailable because that protocol collected no profile. Intel baseline means are native 3.100/6.167/20.347/70.387% and LTO 5.400/6.700/21.600/66.300% in that order; the linked independent report supplies measured children, ranges, exact binaries and CPU-wide scope limitations. Candidate categories remain unavailable in this qualification record. No counters are inferred from attempt counts.

Own cpu-perf/library_status discovery returned no exposed tools. Controller consultation in [CONSULTATION.md](../CONSULTATION.md) is shared evidence, not calls by this reviewer; its source coverage cannot establish a counting convention. The conventions above derive from the actual ledgers/protocols. Exact reviewer backend/model/token/currency costs are unknown. Only this review file was written; no shared ledger/source/harness changes, measurements, fleet access, commits or pushes.
