# DIAG-005 preregistration — construction/query-order interaction

Written after DIAG-004, before this instrument build/measurement. DIAG-004's descending
performance pattern is exploratory; do not relabel its failed hypothesis. New hypothesis:
the construction/query-permutation coupling contributes materially to the long-key
construction contrast. Independent query permutation will reduce the ascending/shuffled
wall-time ratio by at least10% relative to the coupled query permutation. This tests an
interaction, not a cache/allocator causal mechanism, speed optimisation or precision cure.

Four cells, same binary/source: A=ascending construction,B=shuffled construction;
S=original coupled query permutation,I=independently shuffled query permutation. Both
construction arms share the exact same S or I query array and hash/key fixture seed.
Both query arrays have the same size/allocation sequence; one array/process is copied
from construction permutation then optionally reshuffled with a separate deterministic
RNG. Query fingerprint recorded. Warmup uses that cell's query order. Tree bytes/leaf
occupancy may differ A vs B, must be identical S vs I for the same seed/construction.
Count/checksum remain fixed, arrays are complete permutations; no source changes.

Fresh fixture seeds211,211,307,307,401,401 in six serial process blocks. Block odd:
AS,BS,BI,AI,AI,BI,BS,AS; block even reverses the first half then mirrors it:
AI,BI,BS,AS,AS,BS,BI,AI. Eight processes/block,48 total. All100000 members,320-byte
binary keys,5000000 hits/process,10 fixed warmup passes. No excluded normal warmup.
Separate small size1000/ops10000 four-cell release/sanitizer tests excluded prospectively.
Child<=120s,total<=240s; no overlapping builds/tests/profiles/agents. Preserve all rows,
errors and timeouts. No optional stopping,outliers,adaptive counts or changed thresholds.

Per block compute ratios RS=mean(AS)/mean(BS), RI=mean(AI)/mean(BI), interaction=RS/RI.
Support only if median interaction>=1.10 and interaction>1 in>=5/6 blocks, all48 valid
windows>=10ms, checksums/counts correct, all structural/query-fingerprint controls pass.
Otherwise not supported. Report all cells, both ratios, per-seed outcomes, and memory.
Do not treat within-block repeats as independent confirmation or alter lookup PARK.

Same M1/compiler/libc/assertions as DIAG-004; one thread,4P+4E installed,no SMT. Frequency,
turbo state,effective QoS,residency unknown. Wall time primary, thread time/opaque CPU
IDs/requested QoS descriptive only. No policy change. Fresh frozen snapshot derived from
DIAG-004, root referee/source intact. Backend/model/cost unknown; reviewer startup failed,
sequential coordinator review only. No optimisation population or accepted candidate.
