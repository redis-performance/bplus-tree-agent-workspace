# Chair decision: NONE before native ARM scan implementation

Actual chair `/root`, separate from the three independently authoring participants.
Exact serving model and measured token/USD costs are unknown. The common baseline
packet is ARM c9664ab44, source8fab511e, original compiler/referee. Proposals are copied
byte-for-byte with their source revisions and SHA256. No proposer read another's
proposal. All knew earlier x86 work as context, never as ARM performance evidence;
the same completed ARM control update was shared with all three before this decision.

| Chair rank | Proposal | Mechanism/evidence | Scope/risk/portability | Decision |
|---|---|---|---|---|
| 1 equal | Intel | Exact bounded16-byte native comparison; nibble-mask extraction option | Single helper, native little-endian guard, original residual/fallback; mask extraction and dense-store risks | Conditional support becomes NONE |
| 1 equal | AMD | Same exact matching hypothesis; weighted lane reduction option | Single helper; explicit mask/endianness bounds, differing profile/timing operation counts | NONE after failed qualification |
| 1 equal | ARM | Same exact matching hypothesis; one-bit-per-nibble extraction option | Single helper; compares portable exact-mask/hoisted-fold alternatives and leaves them unselected | Conditional support becomes NONE |

The202 instruction encodings in the selected original/profile ranges match; root
inspected the source-linked disassembly and exclusion of the preceding leaf-ID assertion.
All-match period shares34.459%/26.769% are approximate locations of cost, not strict
cycle ceilings. The nested mask and recheck ranges overlap. Native extraction overhead,
code growth, dense matches and incomplete guard coverage remain meaningful risks.
These are implementation alternatives within one hypothesis, not measured rankings.
No candidate was built or timed, so no implementation winner can be named.

Fresh controls were preregistered d9c9dbbe3 before execution:5M requested operations,
100K/1M,16-byte members,seeds101/102/103 twice,six ABBA blocks per size,300s cap.
Root independently reconstructed all48 rows /12 blocks and verified107 sealed files,
source/referee/driver hashes, exact schedule, serialCPU2, callbacks/checksums and owned
memory.100K qualifies. The first1M block is+1.889270895%, outside the fixed±1% limit;
its other five blocks pass. Timer windows exceed424/542ms, so short windows do not
explain away this failure. Failed first-block removal, retries and count changes are
not allowed. Full evidence is ARM f22b8f82e and the [root audit](../aws-arm-native-scan-aa-audit.json).

**Select NONE and stop before the implementation population.** Preserve all three
proposals and baseline evidence for a separately justified future qualified campaign.
No native ARM patch, source adoption, speedup claim or additional measured population.
Counts remain7 completed AWS populations (0 accepted/4 rejected/3 parked), one parked
ARM iterator replication, and the existing Intel scan B follow-up still in progress.
