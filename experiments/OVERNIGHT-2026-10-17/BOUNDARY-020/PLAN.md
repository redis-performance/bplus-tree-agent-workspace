# BOUNDARY-020 — relocation during active resize and cursor retirement

Preregistered additive correctness work, no timing claim. Baseline/EXP-004 A/B/C,
native -O3 debug and -O1 ASan/UBSan, eight frozen isolated cells. Two seeds60209,
60223 × two callback policies (all move / decline each third), four fixtures/cell.
319/320/321/1024-byte binary members, equal-score groups and signed zeros. Build
with public insert APIs until a natural resize has>=32uncopied leaves, max65536
members. Read-only observations must not advance migration. No private state edits.

Move header, ID map, both index buffers and rehash metadata with DefragStart;
copy old usable bytes to a distinct allocation requested64bytes larger, preserve
original callback free semantics, track exact usable-size delta. Require all five
allocations visited, and every one moved in all-move mode. Verify active resize,
model order/exact scores/lengths/scan completeness and full ownership sum.

Begin public incremental defrag, then retire exactly the saved defrag cursor leaf
with public rank deletion. Require saved cursor still names the freed ID, same
member resize still active, no ID reuse. Resume and require first allocation
callback names the current first leaf, proving missing-cursor restart occurred.
Complete pass in<=8*length+leafhighwater+8steps. Then reset and run a quiescent
pass, with a pre-enumerated allocation set: each live leaf/inner page and external
member receives exactly one callback, moves or explicitly declines. No lookup is
allowed to finish rehash before these coverage assertions. Verify count limits,
exact usable-size delta and tree ownership after every step; full vector/scan at
phase boundaries. Clone active tree, finish via lookups, verify both independently.

Two isolated sanitizer faults must compile and fail at runtime: lose relocated
active destination bucket pointer; stop defrag on a retired cursor rather than
restart. These exercise different defects from the existing settled-relocation
fault controls. Keep all failed plans/snapshots/logs. Child120s, matrix600s. All
original BOUNDARY-019 checks remain unchanged. No source candidate/population.
Independent reviewer startup already failed; review sequential, costsunknown.
