# BOUNDARY-013 — exhaustive packed-score reader geometry

Before any score-reader optimization: independent bit-at-a-time writer,exact IEEE bits
from ordered-value model,synthetic leaf scores restricted to finite representable values.
All widths0..64,all shifts0..63 with width+shift<=64,counts1/2/3/7/8/9/31/48/95/96,
both physical directions,two fixed seeds1703/11213. Random/zero/max-fitting deltas and
poisoned spare bits. Direct reader is private and pure; no NaN public inputs. Synthetic
leaf need not be sorted because decoding depends only on position/layout; this does not
replace public API ordering/ownership tests. Release/debug and ASan/UBSan. Each<=120s.

Require exact output bits and finite values for every result; record all cases, source
hashes and commands. Two deliberate source faults in isolated copies:remove ninth-byte
merge; mishandle full64 mask. Require both detected. Do not weaken oracle on failure.
This suite validates helper geometry,not runtime path frequencies or performance.
Root source/support/referee untouched;uncommitted snapshots,morning commit review pending.
