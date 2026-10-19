# M6 driver campaign — rank controls PARK; exploratory proposal next

Updated 2026-10-19T01:43:06.281580+00:00. Deadline08:00UTC; no new experiments after07:15UTC.
Actual Apple M6,12 physical/logical cores,arm64,macOS27,Apple Clang21.
Metadata provenance launch-manifest.json; worker sysctl denied in preflight, not retried.
Frequency,DVFS,actual core residency,counters unknown. Baseline source unchanged.
Acknowledgements: baseline48b00870; public rank referee ca5cacfb.

| Target | Status | M1 action |
|---|---|---|
| Five-size baseline | COMPLETE | baseline-attempt002 reused:120processes/960rows/40cells,162.42s.36cells fail A/A,14 short. |
| RANK-001 | RUNNING; profile supports bounded accumulation proposal | No candidate or veto. Already vectorized; do not assume explicit SIMD helps. A/A next. |
| UPDATE-001 | NOT STARTED | Await bounded rank work. |
| LOOKUP-001 | NOT STARTED | Public rank profiles also sample memchr heavily; later target. |
| Optional / confirmation | RESERVED | No contender. |

002-rank/ contains138 passing native/sanitizer harness checks and detected rank fault,
public self-profile/calibrations/assembly and private census. Exact identities in
freeze.json; profile helper include correction in PROFILE-ERRATUM.json. Fixed counts
{'10000': 1788014, '100000': 807246, '1000000': 240090}. CALIBRATION-LIMITATION.md records lightweight summary work while
calibration driver was active; no comparative claim. Fully serial A/A complete:72processes/216batches, all3cells fail±1%; windows42.807ms or longer. No rerun.
External sample attachment failed under sandbox, exact reason unknown; no retry. CPU MCP unavailable. M1 context cached published commit
4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9; remote refresh failed DNS
at01:41UTC, latest remote outcome UNKNOWN. No candidate population yet, no adoption.
Exact backend model and measured token costs unknown; no agents used.

Latest acknowledgement210c06a2. 2026-10-19T01:44:38.181856+00:00 — rank AA maximum effects10K8.840%,100K1.886%,1M7.406%; no adoption-qualified cell. No candidate yet.

2026-10-19T01:45:55.394138+00:00 — three sequential proposal passes/chair choose shorter-side accumulation for ONE exploratory three-variant screen. No candidate built. Full guards, qualified controls and independent review remain missing; source NONE. Discovery plan in002-rank/DISCOVERY-PLAN.md. Latest published acknowledgementb5ebd930.

2026-10-19T01:48:31.090343+00:00 — A/B/C isolated implementations validated:each43upstream tests/native+sanitizer,38targetedchecks; allreferees identical. Patches/source/binary/driver hashes in002-rank/comparison-freeze.json and implementation-manifest.json. Await publication then ONE exploratory screen, no concurrent work. Latest acknowledged chairfedb7d41.
