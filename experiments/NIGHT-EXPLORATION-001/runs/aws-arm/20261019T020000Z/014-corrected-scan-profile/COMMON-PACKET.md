# Corrected-adapter ARM SCAN: baseline-only common evidence

Source13e459ff8800be3f02b6b45c87dd7b0c39453fa9, exact original tree with reviewed
_Noreturn compatibility adapter. Profile job600s cap completed29.5s, six scoped
SCAN captures100K/1M×seeds1–3,16-byte fixtures,5M requestedops, serialCPU2.
All18 original/disabled/profile CSV rows match operations/checksum/ownedbytes and
fixture fields; disabled PMU control has zero events. Diagnostic FIFO source unchanged
from reviewed009, PMU enabled immediately before original clock and disabled after.

New source-linked instruction mapping: zbtIndexScanSlot diagnostic0x10574,
original0x10298. All-match including count/score-byte/tag-pointer/loop setup uses
relative half-open[0x160,0x208) and[0x244,0x4e0),209exactmatching opcodes across
original/diagnostic. Excludes physicalindex leaf-ID assertion[0x12c,0x138), resize
checks, count!=0 assertion0x4e0, later memberdecode/hash/callback. No SIMD instructions
in mapped scope. attribution-map.json enumerates every instruction and both addresses;
source-linked-slot.asm retains source lines, and profiles/ retains full assembly.

| Size | Scoped events | All-match+setup events | Period share | Forward word loop | Word mask/fold setup | Candidate-byte recheck |
|---|---:|---:|---:|---:|---:|---:|
|100K|1255|465|36.929%|29.631%|11.041%|5.067%|
|1M|1597|524|33.128%|27.657%|13.446%|3.175%|

These are sampled period shares, not elapsed-time speedups. Subregions overlap and
must not be added. Word mask scope includes load/shift/constants; no claim all of that
cost disappears with any vector implementation. Weights/skid are approximate; zero
reversed-path samples do not prove zero cost. Fixture is original shuffled insertion;
reversal/tag-distribution/resize/boundary guards remain required for any future source.
Raw perf remains on owned runner with SHA; samples, source-linked assembly and control
CSV outputs are public. Exact commands in job.sh. No profile data is pooled with old
8fab results or Intel data; no adapter speed claim. Fresh fixed015 A/A controls complete48rows/12blocks; both100K and1M qualify
(abs<=1% allsix,minimum415.775/535.062ms), exacteffects in015/aa-audit.json.
Root independent audit remains pending; no proposal or implementation selected. Original8fab failedA/A remains final.

Author/root/aws_arm, nativeCodex; exact model and measured token/USDcost unknown.
