# Independent H2-B acceptance-readiness review

2026-11-14. **GO for fresh confirmation of the four reviewed B cohorts with the pinned drivers below; source selection remains NONE.** Discovery and guard eligibility pass. Fresh seeds29/43, matched ARM profiles and final review of the returned confirmation evidence remain adoption blockers. No result in this review authorizes a failed-cohort retry or rehabilitation of A/C.

## Independence and scope

This reviewer did not implement H2-B/C, the supplemental guard harness, either confirmation driver or `fleet_guards.py`. I did author the hardened Intel offline parser and its earlier baseline audit. Reusing that parser here is disclosed overlap, not another independent review of the parser itself. The H2-B author's [profile/guard audit](H2-PROFILE-GUARD-AUDIT.md) is a self-audit and is not counted as independent acceptance review. [H2-CODE.md](H2-CODE.md) is an independent source review whose author separately disclosed authorship of the guard harness.

I independently reconstructed raw timing/control rows and command joins, read the final confirmation code, checked its pinned origin evidence, and performed pure offline negative checks. No runner access, new timing, profiling, collector/source edit, commit or push occurred. Only this report was written. Exact model, token usage and cost are unknown.

## Identity and existing eligibility

Baseline source is upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, C SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. I independently hashed the isolated final H2-B source to `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29`, matching every reviewed comparison/guard origin and the frozen guard source identity. This is the repaired revision1 source, not the earlier unconditional64-bit assertion revision. The guard C/build-script hashes match `guards/FREEZE.json` and every cohort's metadata.

The controller supplied fresh read-only live-ELF hashes in private `arm-H2-live-hashes.json` and `intel-H2-live-hashes.json`, captured at epoch1794624546. I independently compared all12 entries with the original comparison/guard metadata: four B lookup ELFs and eight baseline/B guard ELFs all match. The controller then copied the four exact B lookup ELFs into the private local evidence directories; I independently hashed all four saved files and matched the identities below to comparison metadata. The eight guard identities remain controller-collected live-byte attestations checked against the original metadata. I did not access the runner.

| B lookup cohort | ELF SHA256 |
|---|---|
| ARM native | `e16a70a4de79ede0bf177b2dd8bd2ddb3af4349c9e22509c8e5199d390a52cdd` |
| ARM GCC15/LTO | `283263f631cbc1440c1c688537edc8eb894de90cba86107d63faa3e68ca7a1f4` |
| Intel native | `ff76b2b9e560cfaae0e48ca61f25d6f79c847cfad88df3bd5fcd6048e55eebd6` |
| Intel GCC15/LTO | `0b6365ed258752de05af80434f8e85feb30ac833e3bba76ce93ff9e28375b293` |

Read private `fleet/{H2-native,H2-lto,native-requalification,lto-long-qualification,guards-native,guards-gcc15-lto}` and corresponding Intel comparison/guard directories plus Intel `baseline`. I independently checked288 six-case B comparison rows, their288 original A/A rows,240 supplemental A/A rows and240 B guard rows. Every expected case/block/slot cell is present once, in ABBA order. Individual JSON stdout, empty stderr, successful command return, CPU2 launcher, seed17, frozen sweeps, metadata ELF, operations/checksums and memory endpoints agree. Separate successful verification commands support the six-case harness, whose measurement JSON has no `verified` field. All controls pass±1%; all rows exceed250ms. Original six-case baseline ELF hashes join their own controls; earlier failed control attempts remain excluded and preserved.

The block effect was recomputed as100×((candidate slot1+slot2)/(baseline slot0+slot3)−1). Negative favors B. Every original hit block exceeds2% improvement; every other original case and each supplemental case stays within1%, with zero candidate/control owned-byte difference at the measured endpoints.

| Cohort | Hit improvement range | Worst original guard delta | Worst supplemental guard delta | Shortest six-case B row |
|---|---:|---:|---:|---:|
| ARM native | 4.785–4.818% | −0.771% | −0.501% | 471.747ms |
| ARM GCC15/LTO | 5.148–5.396% | −0.197% | +0.110% | 2295.067ms |
| Intel native | 3.543–4.311% | +0.113% | +0.741% | 2057.548ms |
| Intel GCC15/LTO | 5.326–5.824% | −0.399% | +0.279% | 1971.698ms |

The five supplemental cases are separate forward/reverse iteration, forward/reverse rank and churn. Their immediate post-timing endpoint is distinct from the post-validation diagnostic endpoint; each actual reviewed block agrees across baseline/B. Endpoint equality does not establish transient peak memory or unmeasured workload behavior. A's prior memory failure and C's qualified ARM LTO forward/reverse iterator regressions remain disqualifying under [the guard decision](../H2-GUARD-DECISION.md). B is the sole eligible H2 selection.

## Exact confirmation-driver review

**Six-case GO:** `fleet_confirmation.py` SHA256 `1491e9dd9fede0f5c62ce5e04169a62b48626f04f56b799e6e47e3c1f7e2237b`. The author confirmed these final bytes; I independently reread them and verified the same hash before/after offline validation. This supersedes the blocked `20406fad…` driver identified in the self-audit.

The new driver is self-contained and checks its own supplied reviewed hash. It embeds the four exact eligible origins, source/referee/ELF pins, original work scales and36 provenance-file hashes. I independently verified every embedded file hash and referee pin, and ran its pure `audit_origin()`/`select_origin()` functions successfully on all four saved cohorts. Those functions reconstruct original complete raw A/A/B grids and joins, require B eligibility and source identity, and reject exclusions. Runtime identity checks rehash the executable and evidence rather than accepting an arbitrary `--source-sha256` label.

Only original H2 native/LTO phases and seeds29/43 are admitted. An atomic deterministic phase claim happens before fresh processes; an existing, partial or failed phase cannot restart. It checks owned live lease, timer, stopped coordinator identity, controllerCPU0, actual architecture, CPU2/sibling state, Docker absence and Intel service inactivity, both before and after each child. It repeats identity checks, records timeout/failure evidence, verifies both fresh-seed binaries, runs all72 A/A rows before any comparison, and evaluates the complete72-row comparison with fixed duration/memory gates. ARM hit requires≥2%; Intel is the preregistered≤1% portability guard. Failure writes PARK/FAIL/ERROR with source adoption false.

Independent offline negative checks rejected a wrong source, ineligible original B, failed original controls, missing row, duplicate measurement command, renamed phase and seed17. A separate boundary check confirmed that a1% hit gain fails ARM's2% objective while passing Intel's portability bound. No mocked or real fleet/measurement execution was needed for these checks.

**Supplemental guard GO, scoped:** `fleet_guard_confirmation.py` SHA256 `72a0d1771c830becf95a8f7439378b9f88b2c689c214dcd8d2b7b2a386841a67`, invoking reviewed `fleet_guards.py` SHA256 `a1ddc7e99f7a03076757dd64f263a3c3dd6d4fc0501dc516a83a6a1306c09704`. This approval covers the actual reviewed `guards-native` and `guards-gcc15-lto` origins on ARM/Intel, with those explicit hashes. It does not authorize an arbitrary new origin directory.

The guard driver checks original seed17 cases, complete passing baseline/B block reports, frozen harness/source/ELFs, exclusions and collector pin. It atomically claims origin+seed, preserves failure, parks a failed fresh A/A stage, and checks the complete60-row/15-block B result. The collector checks lease/coordinator/CPU/service state per row, returns exact semantic joins and applies each directional/memory gate separately. Its current collector hash intentionally differs from the older orchestration hash in `FREEZE.json`; frozen harness/build bytes match and the explicit reviewed collector pin is required.

Guard orchestration is less self-contained than the six-case driver: it trusts the original derived reports, permits a supplied origin basename, and relies on the external collector. This review independently reconstructed the genuine origins' raw rows, closing that evidence gap for these specific inputs. The phase guard is not a global tamper-proof attempt ledger. Docker absence is checked at stage entry, not in every guard row's lease check; the controller must preserve the registered serial dedicated-runner condition throughout. Returned fresh guard rows still need independent raw reconstruction before acceptance.

## TMA classification and remaining adoption gates

I re-ran the hardened offline parser, SHA256 `9d4b8b838cf2bb472b42bb1210f9de6c61999b9a635bbdcc083407d5d34396a3`, without writes on Intel `H2-profile-{native,gcc15-lto}-{base,B}`. All four pass full capture quality. Their source/ELF identities agree with comparison metadata and the supplied live hashes. The parser authorship overlap stated above applies.

Intel Xeon Platinum8488C/Sapphire Rapids, CPU2-wide with CPU50 offline and workload tick accounting within1%; controllerCPU0 and Parca inactive at endpoints. Native GCC13.3.0 and separate GCC15.2.0/LTO cohorts share the frozen hit fixture, seed17. Each column has three five-second captures/fifteen intervals. Collector topdown-profiler0.2.2, pmu-tools `2568760ffc9394ddaa7a71f0c39930e780cf2dca`, TMA5.1-full, perf7.0.14. Full binary provenance, commands and raw checksums are retained in [the profile audit](H2-PROFILE-GUARD-AUDIT.md).

| % total pipeline slots | Native base | Native B | LTO base | LTO B |
|---|---:|---:|---:|---:|
| Frontend_Bound | 3.100 | 3.127 | 5.387 | 4.693 |
| Fetch_Latency | 0.727 | 0.700 | 0.700 | 0.940 |
| Fetch_Bandwidth | 2.373 | 2.420 | 4.673 | 3.660 |
| Bad_Speculation | 6.033 | 6.300 | 6.833 | 7.100 |
| Branch_Mispredicts | 5.927 | 6.293 | 6.680 | 6.720 |
| Machine_Clears | 0.107 | 0.000 | 0.133 | 0.373 |
| Backend_Bound | 20.427 | 18.853 | 21.533 | 20.020 |
| Memory_Bound | 0.800 | 0.800 | 0.800 | 0.400 |
| Core_Bound | 19.627 | 18.060 | 20.733 | 19.620 |
| Retiring | 70.440 | 71.720 | 66.253 | 68.187 |
| Light_Operations | 67.680 | 68.527 | 63.107 | 65.080 |
| Heavy_Operations | 2.727 | 3.100 | 3.073 | 3.100 |

These are unweighted means of displayed interval fractions, not pooled slot ratios. Root sums retain rounding error (LTO baseline100.006% at shown precision); children use total slots and are not independently normalized. Raw event counts/runtime model-selector proof are unavailable. Lower backend/core share is consistent with reduced address work, but serial profile fractions alone do not identify a causal instruction sequence. Fixed-window instruction totals cannot be divided by a separate timing row's operation count. No deeper memory children were collected.

**Adoption blockers:** both fresh seeds29/43 must pass their own qualified six-case and five-guard controls/comparisons with the exact source/ELFs and original limits; failures remain failures. Matched ARM baseline/B profiles and counter/scope review remain outstanding. ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children are unavailable in this readiness review; Intel values cannot fill that gap. Finally, independent returned-row/identity/guard review and a chair decision are required. This report is a pre-confirmation readiness review, not that final acceptance.

Source correctness review found no concrete semantic blocker, but B adds a maintained count/width/cache invariant. The retained focused regression oracle remains valuable.32-bit execution and big-endian execution are unvalidated; the repaired assertion and source reasoning do not erase that gap. Supplemental performance coverage is500 short members/position-preserving churn, not all ownership, rehash, peak-memory or tree-size workloads.

## AMD counting and consultation

Independently recomputed the saved144 AMD control rows/36 blocks: one native and four LTO blocks fail±1%, exactly matching `AMD-RESULTS.md`; minimum row1627.727ms. Both compilers form **one closed qualification protocol**, not two attempts or a candidate population. The current ledger arithmetic is41 completed =23 PARK+18 REJECT+0 approved =29 ARM+6 Intel+6 AMD =24 populations+5 replications+12 qualifications. Active H2 and subsequent populations remain excluded. A stale40/22 pointer in root `SUMMARY.md` was reported to the controller for correction; canonical `experiments/SUMMARY.md` and README already carry41/23.

Own fresh tool discovery found no directly exposed cpu-perf `library_status`/`ask`. The controller's actual stdio consultation in [CONSULTATION.md](../CONSULTATION.md) is shared evidence, not this reviewer's call. Its limited retrieval supplies no primary passage proving this workload mechanism. All numerical conclusions here derive from the saved, separately scoped evidence; none are imported from library examples or another architecture.
