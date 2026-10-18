# Implementation C: simple bulk loop and unchanged scalar fallback

Agent `/root/proposal_c`, independent implementation. Backend: Codex collaboration
agent; exact model identifier and measured token/currency cost unavailable. No
other implementation was read. No builds or timings were run by this implementer.

The chair's implementation task supersedes my narrower source-wrapper proposal:
this is an explicitly private bulk experiment, with the same output materialization
and checksum referee for every variant. It does not claim scalar iterator dispatch
has been amortised. No production source, header, iterator state or public API is
changed by these files.

`decoder.inc` defines only `zbtScoreLeafDecodeRange`. It returns immediately for an
empty range, then selects one of two loops using the invariant
`bits > 58 && (bits & 3) != 0`. For valid widths 0..64 that predicate is true only
for 59, 61, 62 and 63. That loop uses the unchanged `zbtScoreLeafScore`; therefore
it preserves the original conditional ninth-byte access exactly. The other loop
copies the original scalar decoder with its unreachable ninth-byte arm removed.
No precomputed mask, cached reversal state, pointer walk or aligned-width-specific
kernel is introduced. Natural compiler inlining/hoisting remains permitted.

For width w, reachable bit offsets are multiples of gcd(w, 8), so their maximum
is 8-gcd(w, 8). For w <=57, w+7 <=64. Width 58 reaches at most offset6; width60
at most4; width64 only0. They cannot cross. The crossing set above is exhaustive.

The loop retains original logical-to-physical mapping, bytewise unaligned-safe
`memcpy`, endian conversion, conditional mask at width64, score shift, unsigned
base addition/subtraction and exact ordered-score conversion. Width0 performs no
score-data load. Output writes exactly count doubles, in forward logical order,
and accepts arbitrary valid start/count including zero. Caller must provide a
disjoint output range, matching the fixed control contract.

Expected advantage: the noncrossing loop removes per-element eligibility and
ninth-byte reconstruction control flow after one dispatch. Crossing widths should
remain close to control except for dispatch/code placement. Short ranges may lose
because dispatch is not amortised; both directions and count1/7 guards matter.
Generated assembly must establish what was actually hoisted. Correctness and
sanitizer failures disqualify this variant; unresolved A/A or regression precision
parks it. A bulk win alone does not establish a scalar iterator or cold-cache win.

Builds, isolated source provenance, patches, validation and all timing selection
are delegated to the chair's serial campaign. These outcomes are not yet known.
