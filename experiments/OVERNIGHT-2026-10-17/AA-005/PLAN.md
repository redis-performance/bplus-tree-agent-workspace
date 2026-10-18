# AA-005 — fresh traversal qualification

Distinct targeted baseline: PROFILE-003 now provides missing scoped traversal profiles
using public self-sampling. AA-001 once qualified short iterate/scan but lacked scan
profile and long-member guard. This tests fresh seeds plus long-member coverage; no
unchanged retry of failed lookup qualifications. Root source/referee untouched.
Use uninstrumented frozen HARNESS-003 executable; base commit/patch/hashes unchanged.

Six fixed ABBA blocks, identical executable A/B; cells iterate16,scan16,iterate320,
scan320;100000 members; iterate50m requested operations,scan10m;construction seed4109,
query seed4201,independent query order,10 warmup passes. Rotate cell order by block.
96 measured fresh processes. Exactly one separately recorded prospectively excluded
binary warmup iterate16,1m operations. Children<=120s,total matrix<=600s. Serial only;
no build/test/profile/agent computation overlap. All raw/failures retained; no optional
stopping,outlier removal,adaptive counts or gate changes. Any incomplete cell PARK.

Wall ns/effective emitted operation primary. Each cell24 successful rows, each>=10ms,
identical operation count,checksum,tree bytes,construction/query fingerprints; expected
traversals500(iterate) or100(scan). Iterator exact count and sum; scans can legally
repeat members, so effective count>=requested and per-row whole-scan binary-member/
score/coverage/count/checksum oracle in frozen harness must pass. No invented exact
unique scan count. Same-session six effects100*(mean(B)/mean(A)-1), descriptive95% t
interval df5,t2.5705818366147395. Entire interval within[-1,+1]% required unchanged.
Record thread/wall,opaque IDs,requested QoS; no frequency/effective QoS inference.

One thread on local M1/macOS26.3,Clang17 -O3/C11/debug symbols/assertions/libc as frozen.
No QoS setter or affinity; clock/residency unknown. PROFILE-003 descriptive counts
are bottleneck evidence only; cadence/perturbation limits retained. Qualifying traversal
subset cannot qualify lookup/mutation guards or full suite. Both populations,fresh
confirmation,matched profile and adversarial review remain required for source changes.
Backend/model/cost unknown; reviewer startup failed, sequential audit only.
