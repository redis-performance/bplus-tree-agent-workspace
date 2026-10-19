# Corrected-adapter scan baseline: fresh controls qualify, source NONE

Exact corrected identity13e459ff8 has fresh qualifying scan controls at100K/1M with16-byte members and5M requested operations. This is a baseline-only diagnosis; no candidate was built or measured. It does not rescue original8fab failed AMD controls or replace the separate completed corrected-adapter size matrix. No old/new timing comparison is made.

The600-second profile job completed in34.1seconds wall time with44 serial CPU2 commands: four builds, six original/disabled native fixture pairs, sanitizer original/disabled parity, one disabled PMU control, assembly capture and six fixed counter plus six sampled captures. Exact callbacks/checksum/tree-owned bytes/traversals/warmup match across each native fixture; sanitizer parity is checked within sanitizer mode. All four disabled counters are zero/not-counted. Source and diagnostic binaries match their pre/post hashes. Enabled counters report100% running time.

| Profile fixture | Helper cycle-period share | Helper events / total sampled events |
|---|---:|---:|
|100K, seeds1–3,5Mops|31.277%|322 /1044|
|1M, seeds1–3,5Mops|29.900%|396 /1334|

These same-IP inline shares establish a relevant all-match helper location. They are coarse, overlapping with caller/helper frames and include FIFO/clock edges and unknown frames in the period denominator. Setup/warmup/postvalidation are excluded. They are not a precise removable cycle fraction, candidate speedup or elapsed prediction. The diagnostic layout differs from the original timing executable. Raw perf.data stays local with six verified hashes; sample text, reports, counters, controls and all commands are public. The audit can reconstruct public attribution without perf.data and explicitly reports how many raw binary hashes were available.

The separate300-second fresh A/A job completed48 processes/12 blocks in53.5seconds wall time. It used the unchanged corrected015 binary1ecbe6a426bd3a593a9fce6b8e8c6796c8c2287706fdd7eafdba595df9bad9ed, seeds401/402/403 twice, same-binary ABBA and frozen alternating size order. All raw rows, exact unrounded elapsed-per-actual-callback effects and CPU2/serial/hash/semantics/memory checks pass.

| Size | Largest absolute A/A effect | Shortest elapsed window | Qualification |
|---|---:|---:|---|
|100K|0.504394%|338.039ms|All six blocks pass|
|1M|0.889833%|434.076ms|All six blocks pass|

No row was discarded, repeated or retuned. Source selection remains NONE. Both fresh controls and a relevant baseline helper profile are now available for the root chair's separate decision about exact B replication with the corrected adapter. This is not a new proposal/implementation population and does not increment AMD counts. Old original-adapter AMD scan remains PARK; its failed1M A/A and instruction/branch-versus-cycle discrepancy are retained in008/mechanism.

Evidence: profile/audit.json, aa/audit.json, all raw rows under profile/ and aa/, immutable plans/freeze, and bounded-job/idle records under jobs/. Actual inherited model and measured token/USD costs remain unknown.
