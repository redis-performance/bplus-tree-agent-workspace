# ARM participant independent proposal: exact16-byte native all-match comparison

Actual participant/root/aws_arm, nativeCodex backend. Exact servingmodel, measuredtokens
and monetarycost unknown. Authored after immutablec9664ab44 commonpacket andd9c9dbbe3
controlpreregistration. No other nativeARM proposal or chair decision was read; no
candidate code written. Earlier x86SSE2 population and its conditional gains are known
context, not ARM timing evidence. This proposal is separately authored, not blind to
that operational history. Fresh ARM controls are running; their eventual full results
must be shared equally before chair selection. Conditional support is not acceptance.

Chosen falsifiable hypothesis: on little-endian AArch64, replace only complete16-byte
chunks of zbtLeafTagMatches with exact native byte comparisons and an exact scalar
lane bitmap. Emit every matching physical position in increasing order, mapping to
count−1−physical for reversed leaves. Preserve the original bounded scalar residual and
entire original implementation on unsupported architectures. Do not modify first-match
index lookup, record decoding, hashing, the caller, assertions, source flags or layout.
Fold tag0 into requestedtag1 exactly, with a single case choice outside the chunk loop
if the compiler preserves it. Count0..15 must never perform a16-byte load.

The existing forward8-byte loop accounts for26.34%/23.79% sampled period at100K/1M;
its mask/fold-select portion14.995%/16.866% and candidate byte recheck4.689%/2.357%.
These are overlapping sampled regions, not additive removable costs. The original
loop performs two approximate word-mask calculations and a per-word tag select, plus
rbit/clz and candidate reload/recheck. A native16-byte exact comparison could reduce
word-loop iterations and remove false-positive byte verification. The202opcodes in
selected original/diagnostic ranges match, and no existing SIMD occurs there. Modest
samplecounts and skid prohibit a precise headroom estimate or predicted whole-treegain.

One plausible mask construction narrows the16 equality bytes into16 four-bit lanes,
then retains one bit per lane in a64-bit scalar word. Trailing-zero count dividedby4
selects the exact original physical byte; clearing the selected bit progresses to the
next lane. This is a design description, not prescribed implementation code. Another
implementation can use weighted byte reduction to a16-bit bitmap. Independent authors
must establish lane order mathematically and test it, rather than copy another patch.
AArch64 little-endian guard avoids inventing untested big-endian lane assumptions.

Alternatives considered: a portable exact64-bit zero-byte mask removes approximate-match
rechecks but retains8-byte chunks and more scalar arithmetic; it may be simpler but
need not address the sampled mask/fold cost as strongly. Hoisting the folded-tag case
alone could remove unused ordinary-path calculations, but increases duplicated control
flow without addressing the remaining word-loop/recheck work. NONE is preferable if
fresh controls fail the required dual-primary qualification or reviewers reject the
semantic/headroom premise. No silent fallback to another hypothesis within this round.

Risks: native-vector-to-scalar mask extraction may cost more than scalar SWAR; register
pressure/spills, larger helper code and branch placement may dominate. Dense matching
may shift cost to output enumeration; small leaves and long external members may have
no gain. Unaligned loads must remain bounded bycount and may not read followingrecords.
Bitmaps must not lose lanes, reverse physical enumeration, double-emit nibbles, invoke
ctz(0), mishandlezero/one, or assume aligned/tagpadding. Original external ownership,
resize/SCAN duplicate semantics and narrow/wideIDs remain intact. Keep scalarfallback.

Preregistered prediction for a later selected population: nativevector code appears in
the exact all-match region, no redundant byte recheck remains for completechunks, and
matchedprofile fraction falls while both qualifiedoriginalSCAN primaries improve>=2%.
Reject if correctness differs, emittedcode does not realize the mechanism, either
qualifiedprimary misses2%, or any qualified original/dense/folded/reversed/external guard
regresses>1% in elapsed or treeownedbytes. PARK if A/A, completeguards, profilevalidation,
independent confirmation or adversarialreview remains unresolved. Required performance
coverage includes originaloperation/size/length boundaries and focused007matrix; its64
reversedmembers do not establish broad reversal, and existingresizecorrectness is not
an active-resize performanceguard. No baselinecandidate ranking without qualifiedcontrols.
