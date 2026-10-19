# Adversarial AWS reporting audit of fd4b5d2cb

**One material finding; count, patch-retention and corrected-chart metadata checks pass.** This is a reporting/provenance audit, not a new measurement or independent revalidation of my own Intel results. Actual reviewer `/root/aws_intel` authored the Intel campaign and some shared candidate sources. Exact backend/model, tokens and costs are unknown.

## Finding P2 — stale current decision contradicts demonstrated regression

At immutable `fd4b5d2cb`, **README.md:213** describes Intel scan as “primary gates pass, broader qualification incomplete,” and **README.md:223** says “Overall decision remains PARK.” The old-source exact B replication is already REJECT after the qualified319-byte/signed-zero guard regresses in all six blocks. This is explicitly stated at README.md:27–29 and AWS-DECISIONS.md:465–482. The discovery-checkpoint sentence at219–221 does not scope the later “overall” decision as historical. A reader entering through this results section receives the wrong current decision and may treat the guard problem as merely incomplete evidence.

Correction: lead this section with current old-source REJECT, link the supplemental raw audit/decision, label the earlier discovery/guard chart as a historical checkpoint, and keep the separate corrected-source attempt PARK before candidate timing distinct. Root acknowledged this finding and reported a local fix; this audit is pinned to fd4b5d2cb and does not certify a subsequently published correction.

## Verified reporting claims

- AWS-PATCH-INDEX.json:3–9, AWS-DECISIONS.md:3–17 and README.md:26 consistently identify eight measured populations: five REJECT, three PARK, zero accepted. Each population has exactly A/B/C records. Separate architecture/source replications, historical replay preparation, withdrawn implementations and NONE planning are excluded; their outcomes do not become new populations.
- All24 immutable patch URLs resolve to git objects with matching SHA256. All21 public-target patches match every original hunk at its declared position in unchanged13e target C/H, checked in memory without applying or building. The remaining three ARM count-one patches have the expected public-context mismatch and are explicitly labelled augmented private-control records. The24 hashes are distinct artifacts, not proof of24 distinct algorithms. No public applicability or performance validation is claimed for the private controls.
- Corrected-adapter-charts/README.md:3–6 and qualification table reconcile with four immutable source summaries:160 cells,24 observations/cell,3840 rows. Disjoint qualified/short/other-noisy counts are M6 5/14/21, Intel10/11/19, AMD11/11/18, ARM21/11/8. All16 displayed100K/1M rows agree with the rounded source medians across all four hosts. Independent raw-audit links resolve.
- Every source-parity hash matches its pinned source commit. Tree C/H, microbench, compatibility adapter, Makefile, vendor inputs and analyzer agree; the runner diff is the two declared Linux affinity metadata lines. Chart artifact, renderer and original five-host PNG hashes match the retained validation manifest. No rendering or visual comparison was rerun.
- Corrected chart README explicitly identifies medians and observed ranges, includes unqualified cells as coverage only, disclaims latency percentiles/confidence intervals, retains actual scan callback counts, separates old/corrected identities and missing M1, and names machine/compiler/OS/affinity confounding. I found no unsupported candidate-acceptance or isolated architecture-speed claim in this scope.
- The ledger preserves superseding Intel REJECT, corrected Intel pre-candidate PARK, corrected AMD rejected replication, ARM NEON rejection and later NONE/conditional planning separately. Historical timestamped provisional statements remain valid history; they do not excuse the unqualified current “overall” README claim above.

## Scope and limits

The reproducible metadata auditor uses immutable git objects and independently computes grouping, original patch contexts, source hashes, source-summary equality, qualification categories and displayed medians. It imports no campaign benchmark analyzer and invokes no benchmark, compiler, test, patch application, renderer or runner. Raw benchmark rows were not re-audited here; source summaries and existing independent audit provenance are the inputs. No absent private control is invented or reconstructed as a public baseline.

No source adoption is reported.08:00UTC/09:00Lisbon remains the deadline, not proof of completed release. AWS-DECISIONS.md:569–573 calls the fleet check a pre-deadline checkpoint and explicitly leaves restoration pending. A configured release timer, including AccuracyUSec=1minute scheduling slack, cannot certify actual release at08:00; live post-deadline service/lease checks remain necessary. This review neither reads the fleet nor claims restoration.

See audit.py and audit.json for exact immutable inputs and reconstructed checks. Apart from the decision contradiction, no additional material reporting problem was established within the requested scope. No style-only findings are raised.
