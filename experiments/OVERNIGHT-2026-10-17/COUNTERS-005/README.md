# COUNTERS-005 — compact fully reversed specimen established

All336fixtures pass release/debug and ASan/UBSan:672serial children. Every trimmed
history has one physical leaf with all members reversed; every ordinary ascending
control has one ordinary leaf. Exact scalar packed decode, full byte/score/state oracles,
all8outputmasks and both directions pass. Clone and reinsertion/deletion histories pass.
Two diagnostic sensitivity faults are detected: disabled physical reversal and zero-sign
loss. These are not additional boundary-suite counts.

The recipe is entirely public API: insert a sentinel at nextafter(first model score,
-infinity), insert the requested members ascending, then remove minimum. Sizes1..95 and
16/320-byte members stay within one leaf for these fixtures. The adjacent finite sentinel
avoids introducing an arbitrarily distant score. Packed widths can still differ by history;
the complete histograms are retained, not assumed identical to ordinary construction.

This closes the coverage concentration problem from COUNTERS-004: large descending
fixtures had only64 reversed members. It is structural/correctness evidence,not timing,
an executed-branch count or a CPU profile. No source optimization or benchmark accepted.

[Plan](PLAN.md),[code](census.c),[commands/hashes/results](manifest.json),[fault audit](fault-audit.json). The initial driver stopped because zero-sign loss was
caught by the earlier iterator-copy assertion; [erratum](FAULT-DRIVER-ERRATUM.md) retains
the original classification and corrects it by reading unchanged raw stderr, without reruns.
Native/ASan structural fields agree; owned usable bytes compared within each execution,
not across allocators. Frozen baseline tree included unmodified in isolated census build.

Decision: nineteenth diagnostic completed, source NONE; EXP-004 remains A/PARK. Next:
add this explicit public-API history to a separate referee revision, validate/freeze it,
profile and qualify its small-tree workload before any retained-candidate comparison.
Current census translation unit includes source,so it is not an equivalent timing binary.
Main baseline/referee untouched. Sequential review; backend/model/cost unknown.
