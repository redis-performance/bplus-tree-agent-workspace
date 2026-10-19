# ARM iterator replication — PARK / no qualified winner

Exact Intel A/B patches were replicated on ARM from unchanged source8fab511e. Both fixed screens completed:192 processes and48 ABBA blocks per candidate, eight cells and six blocks per cell. Together with192 A/A processes, the campaign has576 comparison processes and144 complete blocks. Every phase finished within its fixed600-second budget; no restart, count adjustment or qualification retry occurred. Raw CSV hashes, serial order, CPU2 endpoints, exact fixtures, checksums, operation counts and tree-owned bytes pass the audit.

The full-output results are promising observations, but both ARM primaries failed A/A:100K -2.523..+1.985%;1M -3.997..+0.735%. Only the1M score-only cell qualifies among eight required cells. Every A/A window lasted at least96.29ms. No acceptance or qualified architecture-confirmation claim follows from these screens. Intel results stay separate and are not pooled into ARM effects.

A stores a pointer and grows a64-bit iterator from16 to24bytes (+8 per live iterator). B stores a32-bit relative offset in padding and remains16bytes. All consumers were compiled against the matching candidate header. Tree-owned bytes remain identical in every paired block.32-bit ABI sizes and native big-endian behavior remain unmeasured.

Values below are percent changes in time per visited item, median followed by the six-block range; negative is faster. They are observations, not confidence intervals. A/B were each compared with the unchanged baseline; there was no qualified direct A-versus-B comparison.

| Cell: size-encoding-direction-output mask | A | B |
|---|---|---|
| 100000-fraction-forward-7 | -11.900% (-14.450..-9.907%) | -13.125% (-13.774..-11.333%) |
| 100000-integer-forward-4 | -0.581% (-0.952..+0.467%) | +0.236% (-0.010..+0.666%) |
| 100000-integer-forward-7 | -10.812% (-13.332..-7.502%) | -12.623% (-13.559..-11.271%) |
| 100000-integer-reverse-7 | -11.915% (-13.251..-10.531%) | -12.741% (-13.479..-10.843%) |
| 1000000-fraction-forward-7 | -8.838% (-13.730..-7.274%) | -8.935% (-9.559..-7.773%) |
| 1000000-integer-forward-4 | -0.123% (-0.314..+0.660%) | +0.424% (+0.070..+0.569%) |
| 1000000-integer-forward-7 | -7.446% (-9.819..-6.846%) | -9.631% (-11.900..-8.323%) |
| 1000000-integer-reverse-7 | -10.174% (-12.433..-7.074%) | -9.558% (-11.910..-7.901%) |

Full-output integer forward is the preregistered primary at both sizes. Reverse full output, fraction full output and forward score-only are the initial screen guards. The only qualified guard,1M score-only, has all effects within±1% for both candidates. Other guards cannot be declared strictly qualified based on favorable effects alone. B's smaller state and observed lead make it useful follow-up evidence, but do not establish a winner over A.

Correctness passes on baseline/A/B:43 unchanged original tests per native/sanitizer build,1,920 existing output-fixture cells per source, and89,428 additive state checks per build. The latter includes the existing28,192 checks plus direction toggles and mutation followed by explicit reinitialization; copying a valid iterator, poisoned successful/failed seeks, nullable outputs, binary/external members and exact finite/signed-zero values remain covered. Mutation still invalidates an iterator; no lifetime extension is claimed.

Fresh baseline profiles preceded replication selection. Exact offset-array geometry0xb7d0–0xb7ec had11.08%/14.46% local IteratorNext samples at100K/1M; the much larger record-header comparison sample was explicitly excluded from cached work. These are sampled local shares, not instruction latency. Candidate assembly preserves distinct implementations and bypasses repeated geometry after cache initialization. IteratorNext grows620→640 code bytes in both candidates; whole executable text grows64bytes for A and52 for B. Candidate matched profiles were not run, so code generation alone is not profile validation.

Decision: **PARK; qualified implementation winner NONE; source adoption NONE.** This is one architecture replication of an existing three-implementation Intel population, not another three-implementation population. ARM's new measured population count remains1 (decoder:0 accepted/0 rejected/1 parked), plus this separately recorded parked replication. No C rerun or fabricated implementation diversity.

Broader performance guards remain unrun: all remaining output masks/count-only, long members, small trees, wide/zero encodings, iterator setup/seeks and internal mutation/range-deletion iterator paths. Fresh independent confirmation and candidate profile validation are also absent. Correctness and tree-byte equality do not fill those gaps. Required A/A failures prevent promotion regardless of the large observed primary effects; no noise or harness iteration was performed.

Independent root static review434e39ef5 covers the exact patches and memory/reset contract. Final independent ARM raw-data audit is requested against this immutable result commit. Author `/root/aws_arm`, native Codex worker; exact serving model and measured token/USD costs unknown. Original Intel proposal/implementation authorship is retained in origin.json and the published Intel campaign. No upstream action.
