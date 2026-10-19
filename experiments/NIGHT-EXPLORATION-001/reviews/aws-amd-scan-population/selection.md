# Chair decision: exact all-match masks, exploratory only

Chair: `/root`, a separate native agent from the three proposers. Exact serving
models and measured token/USD costs are unknown for all participants. These are
three actual, separately authored proposals, not sequential passes by one author.
They used common packet `b1b670c0a` and baseline `8fab511e`. No proposer read a peer
proposal before submission. Intel had received AMD's tentative memchr direction
in an earlier operational message; it discloses that influence. ARM received the
same clarification after its original proposal commit. This was not a blinded
experiment, and no proposal was rewritten to manufacture diversity.

The copied proposals preserve original bytes from AMD `518814bc1`, Intel
`f73513a9a` (including its separate provenance clarification) and ARM `2d70dfd38`.

| Rank | Proposal | Evidence and expected mechanism | Risk and decision |
|---|---|---|---|
| 1, tied | Intel and ARM: exact 16-byte SSE2 masks | The existing all-match loop must scan every tag. Exact masks cover twice the bytes per chunk and remove false-positive byte verification. Both independently identify the distinction from the rejected first-match SIMD candidates. | Architecture-specific code, vector setup, tails and dense outputs may erase benefit. Choose one bounded experiment with unchanged portable fallback. |
| 2 | AMD: repeated bounded libc memchr | Portable source and a small local change; the census has sparse matches and short extraction lists. | A single match still needs a second search unless it is last; variable short spans and repeated calls add uncertain overhead. Retain the proposal, but do not combine it with the selected mechanism or start a parallel timing family. |

**Select the exact all-match SIMD hypothesis for exploratory implementation.**
The profile establishes a relevant helper, not an instruction-latency explanation:
its same-IP inclusive attribution is about 21–39% at 100K and 23–28% at 1M, from
only 67–91 sampled events per capture. Nested mask shares are already included.
The independent census reconstructs about 69 bytes per call, 76.6–76.7% single
matches and 0.78% folded tag-one calls. It contains no reversed leaves. None of
these numbers is a predicted speedup.

Fresh controls at `4a455e653` qualify 100K (maximum absolute effect 0.245%, minimum
window 69.6 ms), but fail 1M (+1.397% and −1.687% blocks, minimum 94.6 ms). The
corresponding thread-time effects are similar; changing metrics would not rescue
qualification. Keep all 48 rows. **No acceptance, A/A retry, operation adjustment,
or source adoption is authorized by this selection.** A useful outcome can be a
rejection or a conditional lead for an independently preregistered architecture
replication. An unexplained or unqualified speed claim stays PARK.

## Common implementation assignment

Three actual authors implement independently from exact baseline `8fab511e`:
AMD owns A, Intel B, ARM C. Each uses its own isolated source/build directory and
does not read peer patches before submitting its immutable patch and provenance.
No forced superficial divergence: if compiled implementations match, record that
fact. The root chair reviews all three before AMD builds/tests/times them serially
on its one reserved runner. ARM's separate iterator jobs remain isolated.

Only `zbtLeafTagMatches` and required local include/capability guards may change.
Use exact byte equality and masks for complete 16-byte spans on supported SSE2
targets, preserve tag-one folding of bytes zero and one, enumerate ascending
physical positions, then apply the original reversed logical mapping. Retain a
bounded residual and the original portable fallback. No first-match shortcut,
unbounded vector load, global flags, new allocator, index layout, prefetch,
callback change, decoder change, or libc-search alternative in these variants.
Normal timing builds keep identical flags; forced fallback is a correctness-only
build and must not be confused with native ARM or big-endian execution.

Keep the original tests/referee frozen. Baseline oracle `ef63534a7` already passes
native/sanitizer checks for all 256 tags, spans 0–96, both orientations and guarded
page edges, comparing exact outputs and unused-output canaries. Add missing SIMD
boundary/alignment patterns and deliberate fold/order/tail faults before timing,
with baseline revalidation for any additive oracle change. Preserve scan interval,
wide/live-widen, resize-generation and original ownership/migration checks. A
correctness failure makes the implementation ineligible; retain the failed patch.

Before timing, publish a concrete performance guard manifest. It must distinguish
implemented original-operation guards from missing reversed/dense-folded-tag/
resize performance fixtures; semantic tests cannot fill those timing gaps. The
fixed discovery remains 144 processes: three variants, two original scan primaries,
six ABBA blocks, seeds 1/2/3 repeated, one million requested operations, 16-byte
members, CPU2, and a 300-second ceiling. Preserve partial rows if it stops. No
adaptive tuning, extension or replacement variants after seeing timings. Require
the preregistered 2% primary gate on both sizes for a conditional lead, but passing
it cannot override the failed 1M control or missing guards. Fresh confirmation,
matched profile validation and adversarial review remain required for any later
recommendation. This planning decision does not increment completed populations.
