# EXP-004 preregistered screening

One hypothesis:remove redundant shift!=0 branch in zbtScoreLeafScore cross-word read.
A uses bits+shift>64;B uses bits>64-shift;C uses shift>64-bits. All retain exact load,
merge,mask,zero guard,layout,assertions,allocator and byte order. Three isolated source
snapshots share HARNESS-004 base/referee and base commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c
plus uncommitted manifests/patches. Main src/referee never updated. Sequential passes,
not independent agents. Proposals/chair recorded separately before implementation.

Each control/A/B/C passes original43tests,128iterator mode cells(n129;16/320bytes;
4encodings;2directions;8masks),BOUNDARY-012 mutation oracle,and new BOUNDARY-013 exact
bitstream oracle in release/debug and ASan/UBSan. Identical referee hashes. BOUNDARY-013
two sensitivity faults must be detected. Freeze all source/binary hashes before timing.

Existing same-machine AA-006 qualifies10/14 iterator modes. Use identical14cells,
size100000,20m emitted operations,seed7103,3 mode warmups. Three serial ABBA blocks per
variant/cell;504 rows. Rotate variantsABC/BCA/CAB and cells per block. Child<=120s,total
<=600s. No build/test/local agent computation during timing. No optional stopping,
outlier exclusions or changed thresholds. Preserve all failures. Wall ns/item primary;
thread time/CPU IDs/reported QoS diagnostic only,not evidence of stable frequency.

Primary f-int16-m4 entire95%t(df2,t4.302652729911275) paired effect interval<=-2%.
All qualified guards upper<=+1%;any qualified guard lower>+1% disqualifies. All exact
counts/checksum/tree memory/construction fingerprint match;each timing>=10ms. Four
unqualified modes diagnostic only and block ACCEPT. No memory tradeoff. Select eligible
best primary mean,overlapping intervals prefer smaller patch;none=>NONE/PARK or REJECT
on subsequently confirmed failure. Identical generated code remains eligible but record
convergence;do not pretend independent mechanisms. Fresh-seed confirmation/profile plan
must be written before its runs. New trial cutoff01:22:36UTC;handoff before round end.

Local M1/arm64/macOS26.3,one thread,Clang17,C11,-O3,-g,-fno-omit-frame-pointer,libc.
No pinning/QoS intervention;frequency/effective QoS/within-window residency unknown.
No portable headline. Backend/model/cost unknown. Morning commit/review pending.

Before screening,AA-007 current-round prerequisite requalifies only the10 previously
qualified modes with fixed240rows. Use its results for current eligibility;four prior
unqualified modes stay diagnostic. If primary fails,skip screening and PARK. This
addition is made before any AA-007 or EXP-004 timing rows.
