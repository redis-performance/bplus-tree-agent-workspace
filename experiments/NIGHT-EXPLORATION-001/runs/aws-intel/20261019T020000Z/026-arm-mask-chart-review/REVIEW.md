# ARM historical mask chart and reporting review

Reviewed immutable main `a51d1a0ac`. The primary-only chart and metadata pass; no additional material reporting problem was found beyond the already identified command-count wording below. This is reporting review, not acceptance or a new measurement.

- Recomputed all 48 baseline A/A CSV rows at `73c9e313f`: twelve effects agree with the chart and independent root audit `27a4afee1`. Seeds **701–703 twice** are distinct from candidate screen seeds **401–403 twice**. All controls meet ±1% and 10 ms.
- All twelve candidate effects and both medians agree within `1e-10` percentage points with this reviewer's prior independent Decimal raw reconstruction `16f074fbe`. The medians are medians of paired ABBA elapsed-time effects: −7.766545% / −7.101923%, not throughput percentages or confidence bounds.
- Renderer SHA and PNG/SVG hashes match the JSON. Read the renderer without executing it: pinned inputs, ABBA calculation, all six blocks per size, separate control/primary axes and seed labels, thresholds and medians agree. The visually inspected PNG has the exact pinned hash; labels and caveats are readable. Different axis scales are explicit and do not omit observations.
- README lines 215–227, chart README lines 53–62, AWS-DECISIONS lines 588–620, AWS-STATUS lines 590–621, EXPERIMENTS lines 1361–1367 and SUMMARY lines 1036–1042 retain **PARK/source NONE**, score-only/16-byte/50M scope, missing qualified guards, fresh confirmation and matched candidate profile. Static mask instruction reduction is not presented as a causal explanation. The historical replication is separate from the eight measured AWS populations (0 accepted / 5 rejected / 3 parked); its patch does not inflate the 24 population patches. No general tree-speed or cross-host timing conclusion is warranted.
- The corrected Intel rejection headline remains separate from its corrected-source guard-first PARK. Post-screen idleness is explicitly not completed lease release. Actual release remains pending 08:00 UTC; no new timing phase is permitted after the cutoff.

## Known wording correction, pending at this revision

README line 44 says “570 correctness”; AWS-DECISIONS line 606 and AWS-STATUS line 607 say “Correctness passed570 commands.” These are **570 validation commands**, comprising 536 correctness/fault executions plus 34 preparation/build/inspection commands. The coordinator reports this correction is queued following AMD review. This review confirms the issue but does not claim its unpublished correction is already present. No chart/data change is required.

## Provenance and limits

Participant `/root/aws_intel`, native inherited agent tools; exact backend/model and token/currency costs unknown. Prior Intel campaign/shared-source authorship, historical-mask inventory, NONE proposal, chair review and ARM raw audit are disclosed. This is a separate reporting review, not independence from my own earlier raw analysis. Baseline raw effects were independently reconstructed here; candidate effects were checked against my sealed earlier raw audit. No producer audit code was imported or executed. No renderer, benchmark, build, SSH or remote workload was run. The 61 immutable inputs and checks are retained in `input-hashes.json`, `audit.py` and `audit.json`.
