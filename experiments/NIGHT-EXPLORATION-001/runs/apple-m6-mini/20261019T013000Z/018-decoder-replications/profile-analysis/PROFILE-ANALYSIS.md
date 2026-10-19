# Canonical M6 profiles: decoder locations captured, costs unqualified

All three captures pass the read-only audit. Each sampler and benchmark child
returned 0. Recorded binary hashes match the current frozen native binaries and
their build manifests. Original source/referee/helper identities verify against
the EXP-007 canonical freeze and EXP-008's published preparation freeze map.
All private capture hashes match PROFILE-CAPTURE.json. No profile was rerun.

| Capture | Stack-root observations | Exclusive decoder/helper observations | Other observations |
|---|---:|---|---:|
| EXP-007 base, count 96 |777|decoder_batch 777|0|
| EXP-007 B, count 96 |777|zbtScoreLeafDecodeRange 651; decoder_batch 126|0|
| EXP-008 base, count 16 |172|zbtScoreLeafDecodePolicy 148; decoder_batch 23|1 printing/write location|

Counts identify captured software locations; they are **not cycles, elapsed-time
costs or independent instruction observations**. The audit uses exclusive leaves
of the sample call graph, checks their sum against each stack root and never adds
inclusive parent frames. Several PC offsets can be collapsed into one printed
record. These counts are not counts of distinct instructions. Captures are reported
separately, without cross-experiment or cross-host pooling.

Each fixed capture contains substantial decoder-region observations, sufficient
for the descriptive conclusion that the intended release kernel was reached.
No statistical precision threshold was preregistered for these canonical profiles.
They are insufficient for exact source-line, dependent-latency, cycle or hardware
stall attribution, or for qualifying a comparative mechanism or speed gain.

EXP-007 base inlines scalar range decoding into decoder_batch, which also contains
the round/leaf loop, materialization barrier and four unsigned checksum chains.
B retains a separate geometry-specialized zbtScoreLeafDecodeRange call and output
stores; its other observed locations are in the same caller/checksum loop. Those
different symbol boundaries prevent interpreting the helper fractions as a direct
comparison of decoder cost. The reports collapse offsets and provide no reliable
per-source-line distribution. EXP-008 base similarly reaches its bulk-policy helper
and caller/checksum loop; one captured leaf is in printing/write code.

The sampling boundary is the whole process. Setup/construction, warmup, measured
work and output can all be sampled. No construction frame happens to be an
exclusive observed leaf here; that does not establish zero setup cost. EXP-007
includes observations through two main/caller contexts, which are not labeled as
warmup versus measured phases by the sample report. No time-scoped split is invented.

Each benchmark emits 64 retained profile CSV rows with identical fixture/count/
checksum metadata within its capture, sample indices 0..63, and blank hardware
cycle/instruction fields. EXP-007 base/B agree on the fixture hash and exact checksum
for count 96; EXP-008 count 16 is a different workload. CSV timing fields remain
excluded from discovery/confirmation. Referee stderr says counters were not
requested. Hardware costs remain unqualified.

The canonical profile invocations and target commands are retained in
PROFILE-ANALYSIS.json, with only a generic owned-PID placeholder in sampler commands.
All use width 60, eight leaves, 65536 rounds, 64 samples, 16 warmups and seed 81031;
EXP-007 uses count 96 and EXP-008 count 16. The sampler requests 1 second at 1 ms interval.
Actual captured observations are the counts above, rather than an assumed 1000.
Raw sample text and sampling JSON stay private because they contain local process,
path and platform metadata. Only generic summaries, commands and hashes are public.

`audit-profiles.py` performs this audit without spawning subprocesses. No build,
test, new timing or profiling ran, and discovery outputs/shared documents were not
changed. Participant /root/followup_proposal_b; inherited Codex/GPT-6 family;
exact serving model, token usage and cost unknown.
