# AA-006 — iterator mode precision qualification

Preregistered before observing AA-006 outcomes. New HARNESS-004 separate iterator
fixture extends EXP-002 guard coverage; not a retry of failed lookup/QoS schedules.
HARNESS-004 frozen baseline source/headers, support, referee hashes and binary manifest
must pass validation first. Base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicit
uncommitted referee snapshot. Main src/referee and earlier variants stay unchanged.

14 cells: forward integer/16-byte members with masks0..7; reverse integer/16 mask4,7;
forward fraction/320 mask7; reverse wide/320 mask7; forward fraction/320 mask4;
forward wide/320 mask4. Mask bits:1 member,2 length,4 score. All100000 entries,
20m requested/emitted operations,200 traversals;seed7103;3 mode-matched warmup traversals.
Six ABBA blocks/cell, identical control executable A/B;336 fresh serial measured
processes. Rotate cells by block. One separately retained prospective binary warmup
forward/integer16/mask4,1m ops. No outlier exclusions or optional stopping.
Each child<=120s;total<=600s. Failure/timeout/incomplete cells PARK, preserve every row.
No builds/tests/profiles/agent computations during measurement.

Wall ns/emitted item primary. Independent model score bits/member bytes/order checked
before/after timing for every mode; iterator copy checks state even without outputs.
Exact effective counts, checksum, owned memory and construction fingerprint must match.
Qualify each cell only if24 rows, all successful and>=10ms, six ABBA effects
100*(mean(B)/mean(A)-1),95% t interval df5,t2.5705818366147395 entirely within[-1,+1]%.
No thresholds/counts changed after observations. Store all wall/thread/opaque CPU IDs/
requested QoS observations. These do not measure frequency/effective QoS or exclude
within-window migration. Local M1/arm64/macOS26.3,one thread,Clang17,C11,-O3,-g,
-fno-omit-frame-pointer,assertions/libc same as parent. No pinning/QoS intervention.

Qualification is local/scoped. Any qualified cell may support retained C/control guards;
unqualified cells cannot be promoted by a large exploratory effect. Existing population
stages remain recorded as sequential, no independent agents. Reviewer startup failed.
Backend/model/cost unknown; supervisor records actual CLI token usage separately.
