# DIAG-019 — batch size and bucket-prefetch interaction

Preregistered before preparation or timing. One hypothesis: removing only the two
bucket-prefetch clauses in zbtreeScores attenuates the control-to-EXP-006C penalty
for batch1 relative to batch16 on identical all-hit short-member queries.
PROFILE-005 scoped captures show baseline memchr and candidate leaf lookup dominate;
they establish the changed path but do not explain the earlier single-lane guard.
The prior mixed-primary versus hit-guard contrast also confounds hit ratio, so all
cells here use hits. This is a diagnostic, not a sixth optimization population.

Four isolated snapshots from EXP-006 freeze.json: control-on, C-on, control-off,
C-off. Off deletes only the two bucket-prefetch clauses in zbtreeScores; all other
prefetch sites, hashing, allocator, assertions and HARNESS-007attempt002 stay exact.
Preserve patches and complete assembly. This intervention changes instruction schedule
and layout too; positive evidence supports an intervention, not a pure latency cause.
Run original43 tests and existing exhaustive batch_score_oracle in native and ASan/UBSan
for all4sources; small batch fixture checks at n17/257, lengths16/320, counts1/3/16,
hit/miss/mixed. No build/test/profile/agent work overlaps timing. Reviewer startup failed;
all review/confirmation sequential, exact backend/model/token cost unknown.

Local Apple M1 arm64, single unpinned thread. Apple Clang17 C11 O3-g-Wall-Wextra-Werror
-fno-omit-frame-pointer-DREDIS_DEBUG; sanitizers O1. Unchanged libc usable-size adapter
and SipHash. Frequency/turbo behavior, effective QoS and within-window migration unknown.
Wall elapsed_ns/member is primary. Thread time, boundary CPU IDs and requested QoS are
observations only. Do not transfer M4 numbering/rates or normalize by thread time.

Fixed workload n8192,member16,all-hit,2million requested members,3warmup passes.
Cells on/batch1,on/batch16,off/batch1,off/batch16. All phases6ABBA blocks/cell/seed.
AA seeds81903/query81919,81911/query81923: same control binary for A and B per mode.
Discovery seeds82003/query82019,82011/query82023: Acontrol,BexistingC per mode.
Fresh confirmation seeds82103/query82119,82111/query82123: same comparisons, mirrored
cell order. Every phase192rows; total576rows. Rotate cell order byblock, reverse seed
order on even blocks. No discarded warmup process, all child internal warmups retained.
All three phases run regardless of AA outcome to diagnose, never for acceptance.
No child >120s; each phase600s ceiling; absolute no new child after06:02UTC. Incomplete
schedule stays PARK, no continuation or count change. Preserve failures/stdout/stderr.

Each AA cell/seed needs95%t(df5) wall block-effect interval wholly in[-1,+1]%, each
window>=10ms, exact operations/calls/hits/checksum/query+construction fingerprints and
unchanged tree-owned bytes. Joint qualification requires all8AA cells. No outlier
removal, optional stopping, threshold change or combining seeds as replicates.

Per block define e(p,b)=100*(meanC/meanControl-1), g(p)=e(p,1)-e(p,16),
i=g(on)-g(off), in percentage points. Report95%t(df5) intervals separately per seed.
Support requires every discovery AND fresh seed: g(on) lower bound>=2points,
i lower bound>=1point, mean g(off)<=0.5*mean g(on), AND jointAA qualification.
Otherwise criterion unsupported/PARK; no new claim of a remedy. All raw individual
source effects retained, not only interaction. Independent blocks/t assumptions and
four-cell temporal spacing are explicit limitations. Memory equality mandatory across
sources per seed; no memory/speed tradeoff authorized. No source adoption, replacement
of original guards or mixing with old measurements. Existing EXP-006C/PARK unchanged.

Attempt002 pre-timing correction: strip ANSI control sequences in the original-test output classifier. All fixtures, checks, counts, seeds, policies and sources unchanged; first failure retained.
