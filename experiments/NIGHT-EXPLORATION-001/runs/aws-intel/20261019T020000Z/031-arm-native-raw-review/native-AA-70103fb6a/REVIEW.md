# Independent native A/A raw audit — 70103fb6a

**Integrity PASS; all six cells qualify.** Independently reconstructed144 raw processes/rows,36 ABBA blocks, exact fixedfa190bd9b schedule and314 immutable inputhashes. All effects are within±1%, no short window. This is native diagnostic qualification only: prior ARM027 REJECT/sourceNONE remains final, and no comparison/profile launch is granted by this review.

| Cell | Minimum effect | Maximum effect | Minimum window |
|---|---:|---:|---:|
| primary-forward-100000 | -0.689813% | +0.027652% | 166.363318 ms |
| primary-forward-1000000 | -0.369468% | +0.145538% | 186.610772 ms |
| h4-forward-100000 | -0.064865% | +0.233147% | 64.720507 ms |
| h4-forward-1000000 | -0.196347% | +0.551859% | 72.563264 ms |
| h4-reverse-100000 | -0.844004% | +0.102740% | 62.675807 ms |
| h4-reverse-1000000 | -0.191748% | +0.403157% | 74.580984 ms |

Raw elapsed-nanosecond sums use Decimal `100*((middle1+middle2)/(outer1+outer2)-1)`. Every block has independently checked equal visits, so this is exactly the planned ns/visit ratio. All six fixed cells remain; no retry, adaptive counts, relabeling or omittedrow. Primary uses50M visits/onewarmup and H4integer mask4 uses20M/threewarmups, unchanged frontends and seeds1601–1603 twice. Score checksums and H4shuffle/FNV fingerprints were independently regenerated, not imported from producer outputs.

All297 evidence-seal hashes and290 publication entries verify. Exact four source/binary identities, all15execution inputs, repeated-seed and within-ABBA outputs/tree-owned bytes, CPU2 endpoints and serial child timestamps pass. Children stay within60seconds. Driver phase10:57:43.053785–10:59:14.639896UTC takes91.588556 monotonicseconds; helper receipt covers10:57:42.998390–10:59:14.721238UTC,91.722848 wallseconds/600,return0, correct owned unit. See separate [helper-receipt-audit.json](helper-receipt-audit.json).

Retained preflight10:57:39.806255 and postcheck11:00:32.327742 bind the same source/referee/binary hashes, frozeninputs and leasehash `ec230256d78dbc71788bb1532590de040408b78d09a1c1d8268224bd849897df`. Both record zero owned units/PIDs. New namespace `bplus-frontjob-20261019-`, slice `bplus-front-20261019.slice`, CPU2, exact11:45UTC deadline and >=620-second startmargin agree. Preflight records OSSstopped/PID0 and active release timer; helper/release-script hashes are unchanged. These are independently checked retained records, not a new live SSH or claim of release completion.

Auditor provenance: preparedbeforepublication9ba1d38db, then a metadata-only adaptation to the actual public seal envelope (`files`) and newly available preflight/postcheck/job schema. The initial attempt stopped on missing Gitpath `files` before raw arithmetic; no result was silently skipped. The corrected audit reconstructed all raw rows once, and the helper receipt was checked separately afterwards without rerunning measurements. Original auditor remains in9ba1d38db; exact correction is documented in ../AUDITOR-SCHEMA-CORRECTION.md. Expected fixtures, schedule, arithmetic, qualification thresholds and source pins did not change.

Participant `/root/aws_intel`, native agenttools; exact backend/model/token and currencycosts unknown. Prior raw/static review authorship is disclosed. No producer code imported or executed for this rawaudit; no new benchmark, build, profile, SSH, source edit or runner action. Public normalized artifacts are rehashed; unavailable private originalbytes are not claimed rehashed. [raw-audit.json](raw-audit.json) preserves every exact effect and [input-hashes.json](input-hashes.json) pins all314inputs. Root retains phase-grant authority.
