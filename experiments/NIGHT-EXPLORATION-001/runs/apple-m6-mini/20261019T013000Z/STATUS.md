# M6 driver campaign — rank rejected; update paths next

Updated 2026-10-19T01:55:31.258617+00:00. Campaign deadline **08:00 UTC / 09:00 Lisbon**; reporting starts07:15 UTC.
Branch `exploration/apple-m6-mini-20261019T013000Z`. Launcher-verified Apple M6,
arm64,12 cores, macOS 27, Apple Clang 21. Host/source hashes: launch-manifest.json.
Worker sysctl unavailable in preflight, never retried. Frequency, DVFS, core residency,
hardware counters unknown. Baseline src unchanged; selected source **NONE**.

| Target | Status | Evidence / M1 action |
|---|---|---|
| Five-size baseline | COMPLETE | Reused baseline-attempt002;120 processes / 960 rows, 162.42s. 36/40 cells fail A/A, 14 short. |
| RANK-001 | REJECT / NONE | All 3 variants regress the 100K primary in every block. See [results](002-rank/RESULTS.md). Skip exact min-span policy/patches as contenders. |
| UPDATE-001 | NOT STARTED | Next: profile and validate distinct update-path cases, then proposals only if evidence supports them. |
| LOOKUP-001 | NOT STARTED | Rank profile also samples memchr; no lookup hypothesis chosen. |
| Optional / confirmation | RESERVED | No eligible contender from rank. |

Hypothesis identity `M6-RANK-SHORTER-001`: unconditional smaller sibling span using
existing subtree totals. Both population steps completed as three **sequential**
passes each, not independent agents. All patches preserved in002-rank/variants.

| Variant | 100K median effect | 100K block range | 1M median effect | Decision |
|---|---:|---:|---:|---|
| A | +3.808% | +2.733..+4.393% | -4.002% | REJECT |
| B | +3.425% | +2.856..+10.610% | -2.551% | REJECT |
| C | +3.871% | +2.829..+4.367% | -2.148% | REJECT |

A/A maxima 10K 8.840%,100K 1.886%, 1M 7.406%; all 3 fail±1%. No 1M gain claim or noisy
winner. Tree-owned bytes match.216 processes / 648 candidate batches; 72 / 216 A/A. Native/
sanitizer 43 upstream tests/build and 38 targeted checks/candidate pass. Public profile
and term census support a real arithmetic change; all rank function bodies grow.
Final raw/patch/source/referee audit PASS. No full candidate guards, fresh confirmation,
independent review or adoption profile validation. No baseline source adoption.

Public referee SHA256 `db2f2d0bb470d918935a4ffaebc25b9b76ee1709e260fc8308bc0f18846e1e90`. Exact patch/source/binary identities:
002-rank/comparison-freeze.json and implementation-manifest.json. Published milestones:
referee ca5cacfb; profile 210c06a2; controls b5ebd930; chair fedb7d41; comparison 3102530f;
rejection 23df69a3. Latest final audit/publication pending coordinator acknowledgement.

Limitations: brief summary calculation during duration calibration is disclosed in
CALIBRATION-LIMITATION.md; no recorded other work overlaps control/candidate phases.
External sample attach failed (reason unknown), self-sampler used; helper missing
include fixed with failed build retained. CPU Performance MCP absent. Exact serving
model and measured token cost unknown; visible identity Codex / GPT-6 family. No agents used.

Cached M1 published branch revision `4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9`
inspected at 01:37 UTC; later Git DNS refresh/public raw fetch failed. Current exact
M1 patch/harness outcome UNKNOWN / NOT RUN. Hosts remain separate; no results inferred.

Final round audit and self-review saved at 2026-10-19T01:58:06.384675+00:00. Shared logs/counts/memory updated; next action is UPDATE-001. See [round report](ROUND-001.md) and [handoff](HANDOFF.md). Final publication acknowledgement will be recorded in the next status update.

2026-10-19T01:58:55.309396+00:00 — coordinator rejected final publication due to generated Python bytecode cache. Cache moved intact to ignored scratch; diagnostic loader cache creation disabled. PUBLICATION-NOTE.md records the failure once. Measurement/source evidence unchanged; corrected final publication pending.

Publication update 2026-10-19T02:01:23.704328+00:00: corrected request r1-final-audit-handoff-cache-fixed-20261019T015855Z timed out after 120 seconds with no matching acknowledgement. Last ack is the earlier bytecode-cache rejection; see PUBLICATION-TIMEOUT.json. Final audited report/logs remain local and publication is unresolved. Last successful decision commit is23df69a3. The corrected request remains pending; check it before a new round publication. No Git writes or permission changes were attempted. Continue useful bounded UPDATE-001 preparation; do not claim unpublished provenance is acknowledged.

Round2 resumed 2026-10-19T02:04:22.845384+00:00: launcher baseline-attempt002 and RANK-001 REJECT reused, no rerun. UPDATE-001 referee preparation RUNNING in003-update; cached M1 branch4c48fa7e inspected for context only. M1 pack failures are a lead, not M6 measurements. Final round1 corrected request still lacks matching acknowledgement. No worker Git writes.

2026-10-19T02:04:36.729913+00:00: UPDATE-001 referee freeze ready:100 pattern/size/member-length checks plus2 finite/signed-zero/binary-tie/clone oracles passed. Source unchanged. freeze.json pins toolchain, source and binaries. Metadata-only dSYM hash failure retained in PREPARATION-NOTE.md; no experimental rerun. Publication barrier before census/profile/calibration.

UPDATE referee publication timed out after120s without matching acknowledgement. Last successful published decision remains23df69a3. Exact local hashes retained; acknowledged harness provenance unresolved. Continue bounded local census/profile; no Git retries or settings changes.

2026-10-19T02:08:04.899118+00:00: UPDATE baseline path census/profile COMPLETE. preserve packing failures1517/20000 at100K and11058/20000 at1M; no order failures. Longer captures show lookup dominates after amortization. See003-update/PROFILE.md; no hypothesis selected. Baseline calibration/A/A next. SourceNONE, prior rankREJECT unchanged. Publication requested for diagnosis.
