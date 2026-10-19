# AWS measured decisions — 19 October 2026

Current completed AWS count: **6 populations — 0 accepted, 4 rejected, 2 parked**.
All losing patches and per-run evidence are retained. No source has been adopted.
These counts exclude unmeasured diagnoses and do not combine Apple results.

| Host | Hypothesis | Decision | Main reason |
|---|---|---|---|
| AMD | Lazy lower-bound member metadata | REJECT | Missed the dual-primary speed gate |
| Intel | First-match SSE2 lookup | REJECT | Every primary block was slower |
| AMD | Fixed metadata while building leaves | REJECT | Every primary block was slower |
| ARM | Count-one private decoder fallback | PARK | Failed precision controls and guard concerns; candidate code identical |
| AMD | Separate full packed-move chunks | REJECT | No primary block reached 2% improvement |
| Intel | Lazy iterator offset-array cache | PARK | Conditional A/B leads; noisy control and incomplete fixed schedule |

Active work: ARM is independently testing the exact iterator A/B patches; AMD is
preparing an exploratory all-match scan comparison after three separately authored
proposals and a [chair decision](reviews/aws-amd-scan-population/selection.md).
Failed controls cannot be overridden by favorable candidate timings. See the
[live dashboard](AWS-WORKERS.md) for current revisions and phases.


## 19 October — AWS AMD LOWERBOUND-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/865beadd/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/002-lowerbound/implementation-selection.md). Three sequential proposal passes and three isolated
implementations tested lazy packed-member metadata decoding in leaf lower-bound
search. All fail the 2% primary improvement gate at 100K and 1M. Median effects
for A/B/C are −0.434/−0.037/−1.281% at 100K and +0.441/+0.819/−0.702% at 1M.
No fresh confirmation or full performance guards were run after rejection.

Root independently reconstructed all 36 effects from 144 raw CSV processes and
verified serial windows, checksums, operation counts, seeds and owned-memory equality.
The difference from effects calculated using rounded ns/op is below 0.00015 percentage
points. All native/sanitizer and targeted semantic checks passed before timing.
The 1M A/A control remains unqualified. All three patches are retained; source NONE.

Historical Apple counts remain separately scoped, not silently combined with these.

[Independent raw audit](reviews/aws-amd-lowerbound-raw-audit.json).


## 19 October — AWS Intel SIMD-LOOKUP-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b8945b4d/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup/implementation-selection.md).
Three sequential proposal passes and three isolated bounded SSE2 tag scanners were
measured against the frozen baseline. All three slow successful lookup in every
primary block: median A/B/C effects are +11.870/+9.236/+10.614% at 100K and
+9.654/+8.994/+3.891% at 1M (positive means slower). Source selection **NONE**.

Root independently audited 432 raw processes and 108 paired blocks, serial windows,
CPU2 boundaries, operation counts, seeds, checksums, fixture fingerprints and owned
memory. Native/sanitizer correctness and targeted first-match bounds checks passed.
The 1M A/A control remains unqualified; no fresh confirmation or full adoption guards
were needed after rejection. Instrumented whole-process gprof is not a scoped PMU
measurement. All three losing patches remain available on the host branch.

AWS completed measured populations: **2 — 0 accepted / 2 rejected / 0 parked**.
ARM's withdrawn, unmeasured index-mask proposal is excluded from this count.

[Independent Intel raw audit](reviews/aws-intel-sse2-raw-audit.json).


## 19 October — AWS AMD BUILDER-WRITE-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/f3fcad103/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/004-builder-write/implementation-selection.md).
Three isolated implementations tested fixed encoding metadata while constructing a
new forward leaf. Fresh controls qualified both primaries, and native/sanitizer plus
finite-boundary, signed-zero and packed-decoder checks passed. Every measured primary
block was slower. Median A/B/C effects were +1.039/+1.250/+5.777% at100K and
+1.362/+1.745/+2.766% at1M. Both cases used one million updates per process.

Root independently reconstructed all144 raw processes and36 paired effects, verifying
serial windows, CPU2 boundaries, fixed operations/seeds, checksums and owned memory.
No fresh confirmation or full performance guards were warranted after rejection.
All three patches remain available; source selection **NONE**.

AWS completed measured populations: **3 — 0 accepted / 3 rejected / 0 parked**.
Unmeasured chair-NONE diagnostics are excluded; ARM's decoder population is ongoing.

[Independent builder raw audit](reviews/aws-amd-builder-write-raw-audit.json).


## 19 October — AWS ARM COUNT-ONE-001: PARK / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/e4c5398b2/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/RESULT.md).
Three sequential isolated source implementations completed29-cell screens, alongside
the unchanged scalar-root adapter:2784 processes/696 paired effects. Relative to the
unadopted EXP007B bulk helper, A/B/C primary medians were−8.321/−8.263/−11.372%.
Count-eight guard medians were+1.931/+1.725/+1.804%. These are conditional private
helper observations, not whole-tree gains or strictly qualified regression claims.

Longer controls still failed both primary A/A gates; the count-eight bulk control
also narrowly failed. Its final unrelated guard block stopped at the fixed budget,
leaving three uninterpreted rows. All candidate linked text sections match, so their
sampled differences cannot select an implementation. Native/sanitizer checks passed;
full176-cell guards, fresh confirmation and candidate profile validation were not run.
Root independently audited4175 raw CSVs (1391 longer-control+2784 comparison rows),
including hashes, serial windows, CPU2 boundaries, fixture outputs and fixture bytes.
Source adoption and implementation winner remain **NONE**.


## 19 October — AWS AMD FULL-CHUNKS-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b02b79b30/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/005-full-chunks/implementation-selection.md).
Three sequential isolated implementations separated full64-bit packed-move chunks
from the partial tail. Correctness and both fresh primary A/A controls passed, but
no measured primary block reached2% improvement. Median A/B/C effects were
−0.609/+0.265/−0.824% at100K and+0.380/+0.403/+0.854% at1M.
Root independently reconstructed144 raw processes/36 effects and verified serial
CPU2 runs, exact operations/seeds, checksums and owned-byte equality. No full guards
or fresh confirmation were warranted. All patches remain available; source **NONE**.

AWS completed measured populations: **5 — 0 accepted / 4 rejected / 1 parked**.
Intel's iterator population is ongoing. Unmeasured chair-NONE diagnostics are excluded.

Independent audits: [ARM decoder](reviews/aws-arm-count-one-raw-audit.json), [AMD full chunks](reviews/aws-amd-full-chunks-raw-audit.json).


## 19 October — AWS Intel ITERATOR-CACHE-001: PARK / NONE

The fixed exploratory screen completed566/576 processes,141 complete ABBA blocks
and two trailing rows before its300-second ceiling. No extension or repaired timing
schedule followed. Pointer-cache A and32-bit-offset B show conditional primary leads:
100K medians−7.574/−6.023%,1M−6.559/−4.643%. The100K primary A/A fails; fractional
guards have noisy slowdowns, and the last1M block is incomplete for all variants.
16-bit-offset C is observed slower in forward/full and score-only cases. No winner.
A increases64-bit iterator state16→24 bytes; B/C remain16. Tree-owned bytes match.

All original43 tests pass per source/native-sanitizer build, plus1,920 iterator
fixtures/source and28,192 pre-screen state checks/build. A separate additive oracle
passes89,428 total checks/build, including direction toggles and mutation followed
by explicit reinitialization. Two missing-reset fault controls are detected. Root
independently reconstructs192 A/A and566 comparison rows, verifies the exact frozen
schedule prefix, hashes, serial windows, CPU2, fixture/checksum and owned-byte parity.
Full performance guards, fresh independent confirmation and acceptance review remain
pending. ARM is separately profiling exact retained A/B patches for possible native
replication; its measurements cannot repair this Intel schedule. Source remains NONE.

AWS completed measured populations: **6 — 0 accepted / 4 rejected / 2 parked**.
Unmeasured diagnostics and architecture replications are not new implementation
populations. Decision: Intel branch `f320d3f67`.

[Independent iterator raw audit](reviews/aws-intel-iterator-cache-raw-audit.json).
