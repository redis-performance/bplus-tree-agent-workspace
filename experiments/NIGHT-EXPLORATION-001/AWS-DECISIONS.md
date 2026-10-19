# AWS measured decisions — 19 October 2026

Current completed AWS count: **8 populations — 0 accepted, 5 rejected, 3 parked**.
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
| AMD | Exact all-match SSE2 scan | PARK | Conditional A/B leads; failed 1M control, incomplete guards/profile validation |
| ARM | Bounded NEON all-match scan, corrected adapter | REJECT | Every primary block was slower; all three implementations retained |

The exact iterator A/B patches also completed a separate ARM replication: PARK
because both primary controls failed; no qualified architecture confirmation.

Intel exact scan B replication is now REJECT after a qualified supplemental guard
regression, despite passing primary confirmation and 22 focused qualified guards.
Corrected ARM NEON is also REJECT. Separate corrected Intel baseline profiling and
ARM rejected-code diagnosis continue. Earlier AMD deletion and native ARM planning
stopped before implementation after failed controls. No source adoption.
The [scan chair decision](reviews/aws-amd-scan-population/selection.md) preserves the
three separately authored proposals and implementation assignments.
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


## 19 October — ARM iterator architecture replication: PARK / NONE

Exact Intel iterator A/B patches completed independent ARM screens: 192 A/A plus
192 processes per candidate, 576 total and 144 complete ABBA blocks. Both primary
controls fail (100K −2.523..+1.985%; 1M −3.997..+0.735%), so favorable observations
remain conditional. Primary medians for A/B are −10.812/−12.623% at 100K and
−7.446/−9.631% at 1M. There is no qualified A-versus-B ranking. A uses 24-byte
iterator state and B 16 bytes on this host; tree-owned bytes are identical.

Root independently reconstructed every raw row and effect, checked the full seal,
exact frozen schedules, serial windows, CPU2, fixture/checksum and memory parity.
A fresh read-only SSH check confirms the baseline/A/B binaries still match the
pre-screen hash manifest. Original tests and additive state checks pass. Broader
guards, fresh confirmation and candidate profiles remain absent. Source NONE.

This is one parked architecture replication of an existing population. Completed
AWS population counts stay **6 — 0 accepted / 4 rejected / 2 parked**, plus
**1 parked architecture replication**. Intel and ARM timings are not pooled.
Result pin: ARM `ca5ffa2a8`; independent audit is
`reviews/aws-arm-iterator-cache-raw-audit.json` in the night campaign.


## 19 October — AWS AMD SCAN-TAGS-001: PARK / NONE

Three actual agents separately authored proposals and isolated implementations,
with a fourth agent chairing and reviewing. The selected hypothesis replaces the
all-match leaf-tag loop with exact bounded SSE2 masks and retains a portable
fallback. All three patches remain immutable. Native/sanitizer, exact-position,
scan/resize/widen and fallback checks pass; all eight deliberate faults are caught.

The fixed 144-process screen completes all 36 ABBA effects. A/B show roughly
5.25/4.28% lower elapsed time at 100K and 4.36/4.30% at 1M, meeting the 2% gate in
every block. C misses the every-block 1M gate. Fresh 1M A/A fails, so no qualified
implementation winner follows. One alphabetical-priority A profile finds about
12% fewer instructions/branches but under 1% lower cycles, which does not validate
the 4–5% exploratory elapsed magnitude. Dense/folded/reversed/resize performance
guards remain missing. Decision PARK; source NONE.

Root independently reconstructs all 48 A/A and 144 comparison rows, verifies the
exact schedules, serial CPU2 windows, requested work, actual callback counts,
checksums and owned bytes. Effects reconstructed from integer elapsed times differ
from the worker's rounded ns/op calculation by at most 0.000654 percentage points.
Decision/profile pin: AMD `9f96d0518`; independent audit in the night campaign is
`reviews/aws-amd-scan-raw-audit.json`.

AWS completed populations: **7 — 0 accepted / 4 rejected / 3 parked**, plus
**1 parked ARM architecture replication**. Intel's separately preregistered scan
controls qualify and exact A/B replication is preparing; those measurements cannot
repair AMD's failed control. Full guards, fresh confirmation, profile validation
and final review remain mandatory before any acceptance recommendation.


## 19 October03:42 UTC — Intel scan primary replication qualifies; B advances

[Published discovery](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/5534ca6e7/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/007-scan-replication/README.md).
Root independently reconstructed48 baseline A/A rows and96 candidate rows /36 total
ABBA blocks, including frozen driver/schedule hashes, serial process windows, CPU2,
exact callback counts/checksums and tree-owned memory. Both baseline controls pass.
A median elapsed changes are−6.666%/−3.847% at100K/1M; B−6.665%/−3.661%.
Every candidate primary block improves by at least3.584%. B advances by the frozen
maintenance-based preference; these results do not establish A-versus-B superiority.
The driver completed in113.337s;133.451s includes bounded-helper cleanup overhead.

This is architecture replication of the existing scan population, not a new population.
**PARK pending full guards, fresh confirmation, matched profiles and final adversarial
review; source NONE.** Original-operation guards cover five sizes and two member lengths;
separate focused guards cover genuine dense/folded tags and naturally reversed leaves.
Short or noisy guard cells remain unresolved rather than silently excluded.
AWS counts remain7 populations (0 accepted/4 rejected/3 parked), one parked ARM
replication and this Intel replication in progress.

[Independent raw audit](reviews/aws-intel-scan-raw-audit.json).


## 19 October 03:47 UTC — AMD deletion proposal chair selects NONE

Three actual independent proposals agree on a plausible portable rewrite of the final
offset-adjust loop, conditional on precision qualification. The fixed1M A/A fails;
root independently audited48 rows /12 blocks, including exact schedule, serialCPU2,
checksums, actual deletes and owned memory.100K qualifies;1M ranges+0.499..+4.682%.
The chair selects NONE before implementation; no retry, candidate or new measured
population. All proposals and baseline profile/census/control evidence are retained.
AWS counts remain7 populations (0 accepted/4 rejected/3 parked), plus a parked ARM
replication and Intel scan B follow-up. Source NONE.
[Chair and participant evidence](reviews/aws-amd-delete-population/selection.md).


## 19 October 04:01 UTC — Native ARM scan chair selects NONE

All three actual independent proposals identify bounded native-vector all-match
comparison as plausible, conditional on qualification. Fresh5M-op controls fail
first1M block at+1.889270895%;100K qualifies. Root independently verified48 raw rows,
12 blocks and107 sealed files, exactsource/referee/driver hashes, serialCPU2, callbacks,
checksums and owned memory. NONE before implementation: no retry or failed-row removal.
All proposals/profile/controls remain. No candidate or new measured population.
[Chair](reviews/aws-arm-native-scan-population/selection.md),
[raw audit](reviews/aws-arm-native-scan-aa-audit.json).
Intel B remains in follow-up; independent untouched-seed confirmation will run only
after its current baseline guard job explicitly hands over the idle runner.


## 19 October 04:07 UTC — Intel full original control audit

Root independently reconstructed120 serial processes/960 rows/240 paired blocks across
all eight operations,five sizes and16/128-byte members. Frozen hashes, exact schedule,
CPU2, callbacks/checksums and owned memory pass.57/80 cells qualify;12 insert/delete
cells are shorter than10ms and11 other cells fail precision. Complete original guard
qualification is unavailable; no primary result can override these gaps. All cells
remain in the separately frozen diagnostic B comparison.
[Root audit](reviews/aws-intel-original-guards-aa-audit.json), worker d9713d463.

Root independently verified the Intel runner idle at04:05:08UTC and granted AMD
the frozen independent confirmation protocol5c29cb07f. Intel waits until explicit
return. Source NONE; measured population counts unchanged.


## 19 October 04:11 UTC — Independent Intel B primary confirmation passes

Independent AMD operator on the Intel runner completed48 held-out A/A and48 B
comparison processes, seeds201–203 twice. All12 controls qualify and all12 candidate
blocks improve at least2%. B median elapsed changes are−6.783% at100K and−3.656%
at1M; ranges−6.858..−6.344% and−3.735..−3.580%. This is an Intel result, not an AMD
machine result. Immutable operator evidence27fed33a7; no retries/exclusions.

Root independently reconstructed all96 rows/24 blocks, frozen protocol, exact schedule,
serialCPU2, callbacks/checksums/owned memory across both phases, and source/referee/
binary hash records. Root also read the live binary hashes and independently verified
the runner idle04:09:44UTC before returning ownership to Intel.
[Root audit](reviews/aws-intel-scan-confirmation-raw-audit.json).

This closes only the fresh independent primary-confirmation gate. Full original
controls qualify57/80; diagnostic full B guards, focused guards and matched profiles
remain. **PARK/source NONE**, not acceptance or a portable/full-suite speedup.
Measured population counts remain7 (0 accepted/4 rejected/3 parked).


## 19 October 04:33 UTC — Full original Intel B guards remain PARK

Independent AMD review72553e841 reconstructs both120-process phases:1,920 raw rows,
480 block effects, exact serial CPU2 schedule and fixture/memory identity. All22
post-phase source/referee/binary hashes match. Of57 qualified cells,56 pass every
guard block. The100-member/16-byte iteration guard has+0.304%,−0.825%,+1.329%;
its mixed exceedance remains unresolved. No qualified cell has all three blocks
above+1%. Another23 cells retain failed/short controls, leaving24/80 unresolved.
Unqualified100/128 insert has three positive effects, retained as exploratory
rather than silently passed or promoted to a demonstrated regression.

PARK/source NONE. Independent primary confirmation remains valid only in its
narrow scope. Matched profiles and focused/supplemental guards continue serially.
Root verified the independent reports against their immutable publication.
[Audit summary](reviews/aws-intel-original-guards-independent-summary.json).
Measured AWS populations remain7:0 accepted/4 rejected/3 parked; no new population.


## 19 October 04:42 UTC — Profile, portability and corrected-baseline checkpoints

Independent review5bffe4d28 reconstructs all120 matched Intel captures. Helper
samples base→B are337→316 at100K and419→316 at1M, with matched callback denominators.
The21-sample100K gap is coarse;1M is directionally stronger. SSE2 codegen is present,
but these are captured-text samples from diagnostic layouts, not exact cycles or
a quantitative explanation of elapsed gains. All24 diagnostic and22 original
post-phase hashes match. The24 unresolved original guards still prevent adoption.
[Independent profile summary](reviews/aws-intel-matched-profile-independent-summary.json).

Exact B also passes native ARM original43 tests and V2 oracle299664 checks in both
release and ASan/UBSan through the natural portable fallback. Root verified the
24-file seal, exact source identity and14.2-second bounded CPU2 job. This is
correctness only, not performance qualification or big-endian coverage.
[Portability review](reviews/aws-selected-b-native-arm-review.json).

Separate corrected-adapter baselines on13e459ff8 now complete on AMD and ARM. Root
independently reconstructs120 processes/960 rows/240 blocks per host, exact schedules,
raw hashes, source/runner identities, validation commands, paired memory and summaries.
AMD qualifies11/40:11short plus18other noisy cells. ARM qualifies21/40:11short plus
8other noisy cells. All seven native/sanitizer stages pass on each host. M6's separate
corrected baseline also audits successfully with5/40 qualified; Intel remains queued.
[AMD raw audit](reviews/corrected-aws-amd-baseline-audit.json),
[ARM raw audit](reviews/corrected-aws-arm-baseline-audit.json).

AMD and ARM will reassess scan only under the corrected identity, starting with
separately frozen baseline profiles and48-row A/A controls at5M requested operations,
100K/1M members and seeds401–403 twice. No candidate timing is yet authorized.
Failed controls stop that new comparison without retry. These new harness results
do not repair or replace any original8fab511e decision. Source NONE; measured
AWS population counts remain7:0 accepted/4 rejected/3 parked.


## 19 October 05:00 UTC — corrected ARM population selected; AMD exact replication

Fresh corrected-adapter scan controls qualify on both ARM and AMD. Root independently
reconstructed each48-row/12-block schedule, CPU2 serial windows, checksums/callbacks,
exact owned memory and source/referee/binary identities. Maximum absolute A/A changes:
ARM0.398%/0.762%, AMD0.504%/0.890% at100K/1M. Scoped profiles link to the actual timing
binaries; this is a distinct13e459ff8 source identity, not a rescue of old8fab controls.

Three actual independently authored ARM proposals agree on bounded16-byte native NEON
exact tag matching. Root selects that one hypothesis for three isolated implementations,
with fixed correctness,144-row discovery and held-out confirmation contracts. Existing
21 patches and seven completed populations remain unchanged until this new round is
measured. [Chair and proposals](reviews/aws-arm-corrected-scan-population/selection.md).
AMD separately validates exact selected x86B under the corrected adapter before its
fixed48-row comparison; no new x86 population or candidate switching. Intel continues
its frozen old-adapter focused guards, then its corrected baseline and supplemental
guards. All source adoption remains NONE; no claim of a completed optimization.


## 19 October 05:06 UTC — corrected AMD replication rejected; ARM implementations sealed

Root independently reconstructs corrected AMD exactB evidence db7fdb5b4:60 validation
commands, four original43-test runs,30 oracle executions,48 serialCPU2 raw comparison
rows,12 ABBA effects, original A/A fixture joins and exact source/memory/binary identities.
Median elapsed changes are−1.848% at100K and−1.785% at1M; only2/6 blocks per size meet
2%. **REJECT this replication / NONE**, no guards/profile/confirmation advancement or
retry. This is not a new population, and original8fab scan PARK remains unchanged.
[Independent audit](reviews/aws-amd-corrected-B-independent-audit.json).

All three corrected ARM NEON implementations are sealed independently: A=a223b96b1,
B=9b2456c01,C=3b137666b. Root static review finds no blocker and exhaustively verifies
65,536 lane-match patterns for each of the two reduction methods. Native correctness,
codegen and timing remain pending. Frozen maintenance scores A28/B26/C26 give B,C,A
preference only among implementations passing every primary block, not a speed ranking.
[Review and retained patches](reviews/aws-arm-corrected-scan-population/implementation-static-review.md).

Intel focused A/A completes864 rows/216 blocks,22/36 qualified cells,14 precision
failures and no short windows. Root independently checks immutable c5a734191 raw data,
all36 retained fixture hashes, frozen schedules, serialCPU2, semantic/memory parity and
24 post-phase source/referee/binary identities. Full fixed candidate comparison continues,
retaining all failed-control cells. No new accepted source; completed AWS populations
remain7 (0 accepted/4 rejected/3 parked), plus separate replications.
[Focused control audit](reviews/aws-intel-focused-aa-independent-audit.json).


## 19 October 05:18 UTC — ARM discovery approved after native review

All three corrected ARM implementations pass the fixed native validation: 145 serial
commands, eight original 43-test runs, 56 semantic suite runs, six forced-portable
oracle runs and eight detected faults. Root independently checks every required
outcome, source/referee/patch hash, native vector codegen and comparison binding.
AMD independently reviews coverage/provenance, explicitly disclosing authorship of C.
The rebuilt baseline text equality is supported by the completed frozen driver; neither
reviewer claims to have independently rehashed unpublished section bytes. The overread
fault fails a count/canary assertion before a page signal, so no signal proof is claimed.

Root approves the exact 144-row, 300-second discovery schedule, source13e459ff8,
actual baseline8694 and frozen candidate binaries from24a1694d6. No retry or source
repair. Maintenance preference B,C,A applies only to complete primary survivors.
[Native review and grant](reviews/aws-arm-corrected-scan-population/native-validation-review.json).
Completed population counts remain seven until this round is measured.

The independent full Intel focused audit223d6d7de reconstructs 2,052 processes and
432 paired effects: all 22 qualified guard cases pass; 14 noisy controls remain
unresolved. Across all candidate blocks, changes range from−24.951% to+0.260%, but
unqualified rows remain exploratory. Original 24 guard gaps still block adoption.
[Independent summary](reviews/aws-intel-focused-independent-summary.json).

AMD's separate corrected rank/update profile survey4ed690fd1 completes 74 commands
and 12 scoped captures with matched controls and actual timing-binary mapping.
Sampled instruction locations identify index probing/ID stores as diagnostic topics;
load/store adjacency and sampling skid prevent calling their arithmetic removable.
No new hypothesis is selected. Intel's corrected baseline runs before its frozen
supplemental guards; a distinct corrected SCAN profile/control plan is queued later.

The05:08 live release preflight verifies all three coordinators remain stopped,
all host timers still target08:00UTC/09:00Lisbon, and cgroup inspection reports no
errors. This is not release proof; the final live auditor remains scheduled08:00:20.
[Sanitized preflight](reviews/aws-release-preflight-0508.json).


## 19 October 05:27 UTC — corrected four-host baseline charts published

The corrected-adapter Intel baseline01a7b464d completes seven validation stages,
120 processes and 960 rows. Root independently reconstructs all raw hashes, 240
paired blocks, exact fixtures and source identities: 10/40 cases qualify; 11 have
short windows and 19 further cases fail precision. No candidate gain is inferred.

The new [corrected four-host charts](corrected-adapter-charts/README.md) include M6,
Intel, AMD and Graviton, with separately audited 3,840 rows and 160 cells. Ten source
files match exactly; the runner differs only in two Linux affinity metadata lines.
Compiler/OS/affinity differences remain confounded. No corrected M1 data is present.
The original five-host chart remains byte-identical. PNG/SVG, per-host summaries,
source parity, reproduction commands and checksums are retained; the combined PNG
was visually inspected. All source adoption remains NONE.


## 19 October 05:30 UTC — corrected ARM NEON discovery rejected

The actual three-proposal / three-implementation population completes all 144
serial CPU2 rows and 36 ABBA blocks against qualified corrected-source controls.
Every candidate is slower in every primary block. Median elapsed changes at
100K / 1M: A +100.169% / +69.898%, B +78.161% / +55.342%, C +100.075% / +69.457%.
Decision **REJECT / NONE**. No survivor or eligible independent confirmation;
the prepared held-out driver remains unexecuted. All three patches are retained.

Root independently reconstructs the exact rotating schedule, every raw row and
elapsed-based effect, fixture/checksum/callback/owned-memory joins, CPU boundaries,
serial windows and 298 immutable evidence hashes. Independent AMD review also
reconstructs all 48 controls and 406 total evidence hashes; C authorship is disclosed.
Pre/post identities rely on the completed frozen driver's checks and published live
record; neither reviewer claims a new remote binary read.
[Root audit](reviews/aws-arm-corrected-neon-discovery-audit.json),
[independent review](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/ffd0dbf58/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/023-arm-neon-validation-review/DISCOVERY-REVIEW.md).

AWS completed populations: **8 — 0 accepted / 5 rejected / 3 parked**; architecture
replications remain separately counted. Main tree source is unchanged. A read-only
assembly diagnosis identifies unexpected per-chunk predicate reconstruction; a new
bounded matched profile may test attribution, without revising this rejection.
Intel supplemental guard comparison continues. Its separately frozen corrected-source
baseline profile/control protocol6ed4d361e is reviewed and approved after that job ends.


## 19 October 05:35 UTC — Intel scan B rejected on a qualified supplemental guard

Root independently reconstructs all 1,440 A/A and B raw processes, 360 paired
blocks and the frozen 30-cell schedules from immutablefcb17380a. Ten controls
qualify; eight corresponding B guards pass. The fully reversed small-leaf,
319-byte, alternating signed-zero cell qualifies all six controls but regresses
in all six B blocks: +1.566% to +6.877%, median +4.931%, minimum window199.87ms.
The preregistered all-block regression rule therefore selects **REJECT this Intel
replication / NONE**, superseding its provisional PARK. No fallback to A or retry.

Twenty noisy controls and one mixed qualified guard remain unresolved; earlier
primary gains and independent confirmation do not override this demonstrated loss.
Exact callbacks/checksums/owned bytes, serial CPU2 and published38 supplemental plus
22 original post-phase identities pass. Separate full AMD review is pending.
[Root raw audit](reviews/aws-intel-supplemental-independent-audit.json),
[worker evidence](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/fcb17380a/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/014-scan-supplement/README.md).
This is a replication decision; AWS population counts remain8 (0 accepted /5 rejected
/3 parked). Main tree source remains unchanged.

The separately approved corrected-source Intel baseline-only profile/control job016
now runs. ARM's rejected NEON codegen diagnosis3e085fdcf is independently verified
by AMD51dad06f8: 35 repeated predicate reconstruction instructions per complete
chunk. Root reviews and grants frozen diagnosticd8b21e3c6: exact existing baseline/B
binaries, 12 full-process captures,16 semantic/disabled controls,600-second cap.
Analysis filters the verified timed main call site and retains all other/incomplete
stacks; it is not physically scoped PMU capture. No new candidate is authorized.


## 19 October 05:45 UTC — profile reviews and fresh controls complete

Independent AMD supplemental audit1217ba80a reconstructs all2,124 processes,
360 effects,30 calibrated counts,90 models and360 census records, confirming
Intel old-source B REJECT. Its decisive seven-member319-byte fixture has zero
full16-byte and full8-byte chunks; the regression cannot be attributed directly
to execution of the vector comparison. Source adoption remains NONE.

Root independently audits corrected Intel8d8687467:60 profile captures, seven
semantic controls, known-work66/66 samples and disabled0,320 immutable inputs,
and48 fresh A/A rows. Both primary sizes qualify all six controls. All sampled
helper buckets map to actual timing-binary opcodes/source;542/552 ScanSlot
instructions match, with ten mismatches retained. The original metadata failure
is preserved; only read-only mapping continued, with unchanged raw samples and
aggregate268.15s within600s. No measurement reruns or corrected candidate timings.
[Root profile/control audit](reviews/aws-intel-corrected-profile-aa-independent-audit.json).
Intel prepares a frozen corrected-source exactB plan that must separately qualify
and pass the known small-leaf guard before advancing; no execution grant yet.

Root and independent AMD45ecc704e reconstruct all17,482 ARM profile samples,
52 commands,28 semantic executions and124 sealed files. B's exact predicate region
has400/421 events and17.670%/16.866% of filtered timed sampled period at100K/1M.
All frozen materiality gates pass. Full-process capture and timed-call-site filtering
remain distinct;70 incomplete stacks and all other samples remain accounted for.
Reported loss is zero. This is sampled materiality, not a recoverable-time estimate.
[Root audit](reviews/aws-arm-neon-profile-independent-audit.json).

Fresh ARM020 controls c3323969a qualify both sizes:48 rows/12 blocks/105 seals,
seeds701–703 twice, no retries, unchanged8694 binary. Root raw audit passes.
Three actual independent proposal passes now run from the same frozen packet;
NONE is permitted. Proposals must address the severe prior55–79% B slowdown,
not merely assume removal of a17% sampled region would beat the baseline.
No new implementation, measured population or adoption yet. Counts remain8:
0 accepted /5 rejected /3 parked. [Fresh controls](reviews/aws-arm-fold-predicate-aa-audit.json).


## 19 October 05:49 UTC — ARM fold-predicate chair selects NONE

Three actual independent proposals from commonc3323969a are sealed: ARM790b93446
proposes conditional invariant dispatch; Intelbde3caf03 and AMD0efaf90a8 recommend
NONE. Root chair selects **NONE before implementation**, preserving ARM's dissent.
The~17% sampled predicate share establishes materiality but does not establish
sufficient recovery from the prior55–79% loss; the proposed static instruction gate
is not end-to-end speed evidence. No new implementation or measured population.
[Full ranking, rationale and verbatim proposals](reviews/aws-arm-fold-predicate-population/selection.md).

Counts remain8 (0 accepted /5 rejected /3 parked), source NONE. ARM performs only
read-only attribution of existing baseline samples. AMD prepares a distinct corrected
iterator baseline profile/control plan; Intel prepares corrected exactB replication
with the known guard first. Neither new execution plan is granted yet. Deadline and
actual OSS release verification remain08:00UTC /09:00Lisbon.


## 19 October 06:11 UTC — corrected controls stop advancement

Corrected Intel017 exact-B replication is **PARK before candidate timing**. All
50 preparation commands plus756 validator rows pass, including native/sanitizer
original tests, portable-path checks and32 negative controls. Reproduced baseline
text matches the actual013 timing executable. The fixed calibration produces
1,316,073 traversals;24 fresh A/A rows have minimum199.345ms windows, but two of
six blocks fail precision (−1.417% and−1.047%). No B guard, primary comparison or
retry ran. Root independently verifies1,744 immutable files. Original-adapter B
REJECT remains final and separate.
[Root audit](reviews/aws-intel-corrected-known-guard-independent-audit.json).

AMD029 baseline score-only iterator completes51 profile commands and48 A/A rows.
Known-work/disabled scope controls pass;1,218 scientific samples retain caller
mapping gaps. The100K first block fails precision at+2.430913%;1M qualifies all
six blocks. **NONE; no candidate or retry.** Root independently reconstructs232
public files and all rows; independent ARM58fec78b7 additionally audits scope and
actual instruction mapping. Sampled score-decode shares25.819%/29.350% are not
removable-cycle estimates. Existing full-member iterator cache work is a different
output contract.
[Root audit](reviews/aws-amd-iterator-independent-audit.json).

Counts remain8 measured populations:0 accepted/5 rejected/3 parked. These separate
replication/control outcomes add no population. All runner jobs have ended at this
checkpoint; evidence review continues. No source adoption. The06:02 live fleet
check confirms three stopped OSS coordinators and08:00UTC release timers; actual
restoration remains pending.
[Pre-deadline check](reviews/aws-release-preflight-0602.json).


## 19 October 06:49 UTC — ARM iterator chair selects conditional historical replication

Three actual independent proposals use qualifiedARM024 profile/AA packet27a4afee1.
ARM recommends conditional exactEXP005A replication; Intel andAMD recommendNONE.
Root selects bounded preparation of the unchanged historicalA patch, preserving
both dissenting proposals and originalPARK/NONE. No code/build/runner grant yet.
Native codegen/correctness/time gates precede any fixed48-row primary comparison;
missing guards/fresh confirmation/profile prevent acceptance. No new algorithm or
measured population; existing8counts and sourceNONE unchanged.
[Chair and verbatim proposals](reviews/aws-arm-iterator-proposals/selection.md).
