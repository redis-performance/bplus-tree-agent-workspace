# External ownership extension — preregistration

Separate extension of BOUNDARY-024, not a new optimization or timing experiment.
Use immutable natural-width recipe and all existing checks with current scores.
Fresh seeds71503/71509, control/A/B/C, native O3/debug and O1ASan/UBSan/debug:
16cells, serial120schildren,900stotal. Freeze separately before compiling.

Change only fixture/oracle: IDs0,1,2 and every127th ID have external member length
320/321/1024/4097 (ID-derived cycle); other keys retain319bytes. Generate lengths
before construction and never change existing key identity. Find natural threshold
with the same850000cap, not earlier fixed cardinalities. Select min/max-moving IDs
as successive multiples of127 beginning at floor(anchors/254)*127, so all260updates
include actual external buffers and distinct continuous members. First two moves
still target the middle with fractional scores; exact signed-zero updates remain.

Independent sorted vector compares numeric current scores then lexicographic bytes
and length. SCAN validates current exact bytes/length/score plus independent immutable
hash intervals. Structural accounting includes every external usable allocation and
requires unique buffer ownership. Every mutation captures its external pointer from
the old record, then requires the same allocation at its new record (specific current
implementation transfer invariant, not general public API constraint). At clone time
free original and validate clone with sanitizers. Keep all existing checks, observed
cross-ownership conditions, live cursor anchors, bounded termination, full models.

After successful matrix, separate fault control removes zbtBuildElementDetach only
from UpdateScore's external path. Build success and oracle/assertion/sanitizer failure
required; survival/timeout reported honestly. This is new targeted transfer sensitivity;
it cannot establish leak freedom or performance. Preserve every failure and source.
