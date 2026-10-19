# Build and calibration freeze, before M1 A/A

Apple M1 native and ASan/UBSan lookup binaries compiled with the exact
corrected-adapter tree and EXP-009 lookup harness identities in the
[plan](PLAN.md). Both lookup smoke runs passed the inherited independent
checksum/CSV contract. The six serial calibration commands passed, all
children reaped. Full raw stdout/stderr and command hashes are in
[`results/`](results/). No candidate binary exists.

Compiler: Apple clang 17.0.0 (clang-1700.6.3.2). Native binary SHA256:
`4a9244a0ab98011763fdc507e0619636295793de78dcbc5086dceef0eeca97ef`.
Frozen driver SHA256: `a94c910150aa78b4bd9e935b3ac21487039032a8fe72ecd902f810f4baaa997a`.
Build record SHA256: `d6be846d970e6e6afacac15dff486849cb78c006509159811fb53eee08d705d5`;
calibration record SHA256:
`0a8e0c492c81602c8177a1352299a3a94e3ae26b0c4c86ae7abd301a766e9cd5`.

| Members | Fastest 200K calibration | Fixed operations for ~600 ms | Capped? |
|---:|---:|---:|---|
| 100,000 | 16.576 ms | 7,239,383 | No |
| 1,000,000 | 56.011 ms | 2,142,437 | No |

The next and only native timing schedule is six ABBA blocks per size, seeds
1/2/3 repeated, 48 processes total. Alternate size order by block. Qualify
only when every exact paired block differs by at most 1% and each measured
window lasts at least 10 ms. Complete and retain the whole schedule even if
an early block fails. No count or threshold changes after seeing A/A data.
