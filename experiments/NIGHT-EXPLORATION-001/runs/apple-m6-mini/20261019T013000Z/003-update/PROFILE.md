# UPDATE-001 baseline diagnosis

Untimed seed1 census: all same-value calls stay in place. For preserve,100K has
18,483 successes/1,517 packing failures out of20K calls;1M has8,942/11,058. No neighbor
failure in preserve. Nearby/distant/plus-n first20K calls all fail following-neighbor
order and take remove/reinsert. Full25-cell census is census.json. Counts are logical
branch observations, not PMU counts, and match the cached M1 fixture counts exactly.

Two self-sampler controls attribute every captured PC to sampler_probe. Initial1M-op
profiles retained; sparse preserve captures extended once to10M ops. At100K the long
capture has128 PCs:51 memchr,22 FindForAdd,17 LeafFindMember,12 UpdateInPlace. At1M409
PCs:207 memchr,87 FindForAdd,48 LeafFindMember,27 UpdateInPlace and9 allocator PCs.
This shows lookup cost and amortization: the pack-failure path is prominent early,
while the long sweep mostly samples lookup. Do not call symbol counts exact time
shares. Static cold-symbol attribution can be nearest-symbol attribution. No cycles,
frequency, hardware counters or exact core residency were observed.

Source/public release assembly: profile/update-zbtreeUpdateScore.asm and matching
FindForAdd; separate profile binary assembly is also saved. A potential bounded
mechanism is re-encoding the existing allocation after order succeeds but exact pack
fails, preserving member records and index. It is not yet a selected hypothesis.
Only baseline calibration/A/A next; freeze counts before any proposals/candidates.

All source/referee hashes remain frozen. No baseline source change. Exact serving
model/cost unknown. Publication still lacks acknowledgement; local evidence only.
