# Independent raw-data audit — PASS / no eligible variant

Reviewer `/root/followup_proposal_c`, GPT-6/Codex family. Exact model, token usage
and monetary cost are unknown. I authored C and disclose that conflict. This is an
independent arithmetic/evidence audit of root's driver and measurements, not an
independent semantic review of my own patch or fresh timing confirmation.

**REJECT the declared dual-primary screen; source NONE is the correct decision.**
No variant improves both 100K and 1M by at least 2% in every block. The 1M control
also fails precision, and 62 of 101 baseline cells remain unqualified. No full
candidate guard, fresh confirmation or matched candidate profile was eligible or
performed. No source adoption is supported.

The standalone `independent-audit.py` reads retained evidence without importing the
campaign driver or executing benchmark binaries. It independently reconstructs:

- 303 calibration CSV rows, three per cell, including fastest-observation fixed
  operation/replica counts and caps for all 101 cells.
- 2,424 A/A CSV rows and all six-block effects for 101 cells.
- 144 screen CSV rows, 48 for each variant, including rotated ABC/BCA/CAB block
  order, alternating primary-size order, ABBA labels, fixed counts and seeds.
- All 2,871 CSV hashes and metadata, 2,871 nonoverlapping retained measurement
  command windows, plus 66 frozen source/referee/binary hashes.

Every retained row agrees with its CSV and hash. Per-referee operation counts,
requested counts, seed/member length, replicas, batch size/query seed, checksum and
owned-memory fields satisfy the declared checks. Replicated mutation working sets
stay within the recorded 64 MiB bound. The audit independently computes block
effects using exact rational ratios of integer elapsed totals: inner B pair divided
by outer A pair, with equal operation counts checked before forming the ratio.
Memory ratios also use exact rational CSV values. All saved effects and gates agree
within 1e-9 percentage point of that reconstruction; exact fractions are retained in
`INDEPENDENT-AUDIT.json`.

| Control | Qualification | Maximum absolute A/A effect | Shortest window |
|---|---|---:|---:|
| All cells |39 / 101 qualified|Per-cell values retained|All rows retained|
| 100K lookup primary |Qualified|0.808251%|101.290 ms|
| 1M lookup primary |Unqualified|1.252086%|98.011 ms|

Candidate effects below are elapsed-time changes; negative is faster. These are
discovery observations, not confirmation or an adoption ranking.

| Variant |100K median / block range|1M median / block range|Both primary gates?|
|---|---:|---:|---|
|A|−2.712445% / −3.126806..−2.377886%|−1.762149% / −4.644877..−0.213114%|No|
|B|−2.024243% / −2.710218..−0.972488%|−0.596450% / −2.216456..+1.141851%|No|
|C|−1.826502% / −2.956773..−1.099545%|−0.833121% / −2.949992..+1.805809%|No|

A meets the 100K every-block gate. Its 1M effects are **all negative**, but only two
of six blocks meet the required −2% threshold; describing those 1M effects as
mixed-sign would be incorrect. B and C miss the 100K every-block threshold and have
mixed-sign 1M effects. All screen owned-memory effects are exactly zero. Neither
the favorable A/100K result nor the zero memory differences waive either primary,
the failed controls or any missing adoption gate. Source identities and all patches
remain preserved; this audit does not revise earlier experiment decisions.

Reconstructed timed totals are 250.562225 seconds for A/A and 14.514873 seconds for
all three screens. Retained phase wall times satisfy their 900-second bounds and
all measurement command completions precede the preregistered experiment deadline.
There are 1,075 rows with differing recorded CPU endpoints among the calibration,
A/A and screen rows. Those observations do not establish exact core residency or
within-window migration. Effective QoS, frequency, DVFS and PMU evidence remain
unknown; no row was removed on their basis.

Run the read-only audit from the repository root with:

```sh
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/independent-audit.py
```

The script's output artifact records its own hash, the evidence hashes, all 107
reconstructed cell/variant result records, gates and exact effect fractions. This
review performed no build, benchmark rerun, profile, patch change, agent launch or
Git write. Further timing is unnecessary to establish this screen's no-winner
decision.
