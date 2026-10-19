# 019 runtime map gap — preserved incomplete attempt

019's executable-section model was incomplete. Its frozen map covers only
`__TEXT,__text` (image offsets 1512..74408, half-open). The third child legitimately
sampled three PCs in the adjacent import-stub section, reported by root as
`__TEXT,__stubs` offsets 74408..74828: offset 74604 twice and 74616 once. The sampler's
raw dladdr nearest-name field says `sdsfree.cold.1` for all three. That is not
evidence those PCs executed that cold function.

The own-image derive branch requires the PC inside `__text` before looking up a
symbol, so it asserted and stopped. It did not silently drop the PCs or publish
the third capture with that misleading cold label. Widening the nearest-symbol
lookup across the section boundary would turn this explicit failure into false
attribution and is not an acceptable fix.

All three launched children returned 0, were reaped and left empty owned groups;
their six raw log hashes verify. The captured counts are 84, 97 and 274, totaling 455
locations. Only the first two rows were derived into 019/summary.json. Thus the
historical status correctly remains **INCOMPLETE**, completed_captures=2,
exclusive_runner_release_safe=true, wall 3.2691437499997846 seconds. Three successful
child executions must not be described as three successfully derived 019 rows.
All 53 frozen identities still match freeze
`2aad43fdd9ce492a5f5fb01c27fc0d065686d7338e6ec70c23aeedb072295020`.

My earlier static PASS checked consistency within the declared text map, aliases
and driver gates, but did not establish coverage of every executable section in
which the owned process could be sampled. That check was insufficient. The
historical review remains unchanged; this runtime failure limits its mapping
coverage conclusion. No source, binary or referee defect is established here.

## Necessary prelaunch checks for separate 020

- **Freeze the complete provenance.** Pin the original three stdout/stderr pairs,
  sampler headers, commands journal, incomplete status and two-row summary, together
  with all 53 original frozen source/object/binary identities. Pin 020's corrected
  parser, section metadata and plan separately. Verify them before and after the
  continuation. No original file is overwritten or silently relabeled complete.
- **Classify sections before symbols.** Derive section bounds from the exact frozen
  enabled Mach-O, including import stubs and any other executable instruction
  sections. Use half-open bounds. Only use the text-symbol map within its declared
  text section. Preserve aliases/ambiguity. Import stubs lacking a verified indirect
  symbol mapping remain explicit unknown-import/stub bins, never nearest
  `sdsfree.cold.1` or another text symbol. Unknown sections/modules remain visible.
- **Conserve every PC.** For each retained or new capture, raw header count must
  equal raw PC rows and the sum of all derived bins, including unknown/import and
  hook/boundary locations. Keep malformed-data failures explicit rather than
  dropping rows. Offline checks must cover the observed 74604/74616 cases, the
  text/stub boundary, an unknown location, coalesced aliases and conservation.
  Corrected classification must account for all 455 original PCs without executing
  any of those original captures again.
- **Continue only unstarted indices 03..15.** The first child is lookup-hit/1M/seed2;
  it is followed by lookup-miss, rank and scan, each 100K/1M × seeds 1/2 in original
  order. Reprocessing 00..02 is offline only. Preserve original index identities;
  do not renumber 13 new rows as a fresh 16-row experiment or rerun failed derivation
  index 02. Each operation/member/seed/warmup/PROFILE_USEC value stays frozen.
- **Retain runtime semantics and sufficiency.** Keep the original CSV/count/checksum/
  ownership checks and unchanged in-binary oracle. Scan duplicate emissions remain
  legitimate actual operations. At least 10 PCs, no cap overflow and the 65536 limit
  still govern every row. Unknown/stub samples count toward conservation and must
  not be reassigned to make a target region look sufficient. Report target-region
  coverage separately if making a region-specific statement. No retry or retuning.
- **Bound the continuation independently.** The new fixed 480 second wall cap plus
  original 3.2691437499997846 seconds remains below the original 600 second exposure
  ceiling. Clip by the earlier 07:15 UTC cutoff, retain the 45 second child cap and
  cleanup reserve, and include offline derivation/serialization in completion
  checks. Retain the parent watchdog, SIGALRM deferral through mandatory cleanup/
  journal, kill/reap/group-empty checks and conservative safe-release status.
- **Require a fresh exclusive published ACK.** Root plus independent review must
  cover the new exact freeze and continuation plan. All other experimental work
  must stop before new captures. Use new public/private output locations with
  refusal of existing outputs; no permission or sampler change is needed.
- **Report the two phases truthfully.** 020 may link corrected offline summaries
  of the original three to the remaining 13 new captures, with distinct acquisition
  and derivation provenance. It cannot rewrite 019 as a completed capture set.
  Retain all missing/insufficient outcomes. Counts remain sampled locations, not
  cycles, latency, cache costs, unbiased time shares or a source optimization.

This postmortem uses static code/map inspection and read-only verification of
already retained metadata/raw hashes. No binary, build, test, profile or timing
was executed. Only this new postmortem was written; prior PASS records are intact.
Participant `/root/followup_proposal_b`; inherited Codex/GPT-6 family; exact serving
model, token usage and cost unknown.
