# Matched scoped profile diagnosis

**PARK / NONE remains unchanged.**36 enabled captures and four disabled controls completed in55.61s including builds. Checksums, CPU2 residency, histogram counts, disabled-zero controls and16-bit overflow bounds pass. Each cell aggregates three fixed100M-item captures; this is coarse sampling, with no profile-duration speed claim. The earlier enabled known-work sampler control remains valid because sampler.c is unchanged.

| Source/cell | Captured in-range samples | IteratorNext share |
|---|---:|---:|
| base-100000-7 | 174 | 90.23% |
| base-1000000-4 | 138 | 94.20% |
| base-1000000-7 | 195 | 90.26% |
| A-100000-7 | 166 | 89.16% |
| A-1000000-4 | 139 | 94.96% |
| A-1000000-7 | 185 | 90.27% |
| B-100000-7 | 174 | 91.95% |
| B-1000000-4 | 141 | 92.91% |
| B-1000000-7 | 194 | 89.18% |
| C-100000-7 | 170 | 92.35% |
| C-1000000-4 | 139 | 92.81% |
| C-1000000-7 | 189 | 87.30% |

The denominator is captured samples within the executable text range only. Library/outside-text/lost samples are excluded; this is not a share of wall time or all CPU work. Scale65536,2-byte bins and actual10ms sampler interval are recorded per capture. Exact binary symbols, disassembly, hashes, histograms and metadata are retained in matched-profiles. matched-profile-pc-map.json maps the sampled bucket start to a containing instruction where possible; bucket boundaries and attribution are approximate.

Baseline full-output captures again place75 of369 captured samples at bucket0xca96, the packed-member prefix comparison following dependent offset/record loads. This does not mean the comparison instruction itself costs20.3%. A/B/C assembly bypasses the leaf count×score-width arithmetic after the cache is initialized; all retain physical-position and packed-record decoding. The initialized A path loads a pointer; B loads a32-bit relative offset; C loads/tests16 bits then zero-extends before adding the leaf base.

The broad hotspot remains IteratorNext (87.30–92.35% among captured full-output samples). Profiles shift toward cache tests, dependent member-prefix loads and score output. This is consistent with removal of repeated member offset computation, without proving a hardware-level cause for the measured effects.

C has an extra narrow test/zero-extension and different instruction layout, but its score-only timing regression bypasses cache access altogether. Therefore neither its16-bit cache access nor one sampled PC explains the overall regression. Code layout/register scheduling and host effects remain hypotheses; PMU evidence is unavailable. No new mechanism or timing retry is selected from this diagnosis.

Root independently audited the original192 A/A plus566 screen rows in main847ed4096, including141 full blocks, two preserved tail rows, ten missing rows and exact schedule prefix. No source adoption or independent fresh timing confirmation has occurred. ARM is testing exact A/B identities as a separate architecture replication.
