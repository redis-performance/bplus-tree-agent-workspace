# 019 independent raw-capture/failure audit

**PASS: raw evidence is intact; 019 remains INCOMPLETE.** Three child processes succeeded, while only two rows were derived/serialized. The third capture did not fail. Analysis rejected three valid own-image linker-stub PCs because its frozen map accepted only the text section. No profile was repeated or discarded.

All 53 frozen identities, binary and shared native tree object verify. Frozen nm symbol groups reconcile with the exact section map. Inverting all three exact conditional hook insertions restores original frontend bytes, and the copied sampler is unchanged. Enabled/disabled frontend codegen differs; source restoration does not imply identical runtime codegen or instruction costs.

| Capture | Operations | Exact checksum | Owned bytes | Raw PCs | Own text | Own stubs | External | Derived |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 00-lookup-hit-100000-s1 | 10000000 | 499995000000 | 2984176 | 84 | 27 | 0 | 57 | yes |
| 01-lookup-hit-100000-s2 | 10000000 | 499995000000 | 2979056 | 97 | 41 | 0 | 56 | yes |
| 02-lookup-hit-1000000-s1 | 10000000 | 4999995000000 | 32936048 | 274 | 100 | 3 | 171 | no |

Each one-row CSV matches its case/size/seed, 10M operations, finite exact integer checksum, positive owned-byte count, zero traversals, 16-byte members and three warmups. Raw PROFILE headers match lookup-hit, requested 1000us, 84/97/274 rows and zero cap. All 455 raw PCs reconcile, including 181 in the two exact public summaries. Capture 02 has 274 retained PCs, meeting the fixed 10-PC floor, but has no original derived row. Elapsed/rate fields are unused.

Independent static otool inspection confirms image-relative __text=[1512,74408) and __stubs=[74408,74828), with 12-byte stubs. Two PCs at 74604 are +4 inside the _memchr stub starting 74600; one at 74616 is +4 inside _memcmp starting 74612. Every other own-image PC lies in __text. These are static/image-relative code offsets, not raw runtime pointers. The text-only assertion therefore fails deterministically while deriving capture 02; assigning these stubs to the preceding tree/text symbol would be incorrect. Exact static commands/private output hashes are in the JSON.

All three children exited 0, were reaped, and had empty owned process groups. UTC windows are serial and below their 45-second child bounds. Final release_safe=true is consistent with cleanup. The original completed_captures=2 means derived rows, whereas three journal entries prove three successful captures; thirteen planned cases never started. Phase wall 3.269144 seconds is budget bookkeeping only. No original status, summary, command or frozen input was edited.

A read-only audit precheck initially used a naive hook-removal regex, which left one blank line and failed an exact-byte assertion. Reversing the actual three frozen insertion blocks verifies exact restoration including whitespace. This was an auditor-side inspection correction, not a workload failure or capture retry.

Sampler boundaries exclude fixture preparation, warmup and post-oracle work while permitting hook/signal boundary PCs. Counts are interrupted-PC observations, not isolated instruction latency, cycles, cache behavior, speed, frequency or unbiased time shares. Raw profiles remain private; the incomplete set selects no source candidate.

Participant `/root/followup_proposal_a`, inherited GPT-6/Codex family; exact serving model/token/currency cost unknown. I did not prepare 019. No new capture/build/timing/profile/retry, Git/shared-status write or raw runtime-PC publication occurred. Static inspection children finished; reviewer is idle.
