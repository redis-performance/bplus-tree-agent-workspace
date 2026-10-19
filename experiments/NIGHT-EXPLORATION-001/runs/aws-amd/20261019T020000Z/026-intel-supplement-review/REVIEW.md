# Independent Intel supplemental guard review

**REJECT of the exact original-adapter Intel B is supported.** The qualified
trim/319-byte/encoding2 guard is slower by more than1% in all six frozen blocks:
+5.166785%,+4.694751%,+3.245691%,+5.737852%,+6.877159%,+1.565989%; median+4.930768%.
Its A/A effects are−0.478654%,−0.603076%,+0.079926%,+0.517231%,+0.016823%,+0.783417%.
All windows satisfy the100ms floor, fixture outputs and owned memory are exact.
The frozen rule requires rejection for all-six qualified regressions. Earlier
primary gains and passing guards cannot override this rule. Source adoptionNONE.

Independent audit of immutablefcb17380a reconstructs all2124 processes:684 baseline
calibration,720 A/A and720 B comparison,180 ABBA blocks per comparison phase. All
raw JSON/stdout pairs agree, stderr is empty, CPU observations are2, commands and
serial UTC intervals match. Phase times34.219/157.126/154.887s fit180/480/480s caps.
The audit was authored without reading or importing Intel's audit.py.

Calibration is reconstructed from the1,10,... probe sequence and first20ms stop,
followed by three fixed trials per seed. All30 counts equal ceil200ms/minimum
ns-per-pass across nine trials. Every count and both720-slot schedules match the
immutable6ed4d361e freeze. No retries, row pruning or operation adjustment appear.
Schedules reverse cell order on odd blocks; seeds201–203 repeat twice.

|Supplemental classification|Cells|
|---|---:|
|Qualified, all six guard blocks pass|8|
|Qualified, all six exceed1%: REJECT|1|
|Qualified, mixed exceedance: PARK|1|
|A/A control unqualified: PARK|20|

There are no short windows. The mixed cell is resize/319-byte/encoding2:
+0.685581%,−0.932122%,+3.007870%,+2.899095%,+3.771728%,+2.661329% (median+2.780212%).
It stays PARK despite a positive median. Unqualified cells remain in the raw audit;
the full30-cell matrix was retained. Prior24 unresolved original guards and14
unqualified focused guards remain distinct, not repaired by this supplement.

The semantic audit joins callbacks, per-pass checksum, fixture size/encoding/seed,
owned bytes, warmup/oracle counts and public validation across calibration/A/A/B.
Logical_members is n*passes; legal duplicate SCAN callbacks are independently
preserved and can exceed n. Within a paired block, normalization per pass or per
callback gives the same effect because callback counts and pass counts are exact.

All frozen input/import hashes pass. The38 supplemental source/referee/binary
entries match after preparation, calibration, A/A and B;22 original baseline/B
entries match the original007 freeze after B. This is the original8fab adapter,
not the corrected13e identity. No live remote rehash or measurement was performed.
The driver asserts returncode0 before storing each row, but does not retain an
explicit exit-code column. This provenance limit is disclosed rather than invented.

The90 independent fixture model records match imported reviewed referee models.
All360 native/sanitizer baseline/B census records match their raw evidence and
one another; native fixture outcomes join timed outputs. The decisive trim guard
has seven fully reversed inline319-byte members, no full16-byte or full8-byte tag
chunk, no active resize, and no wide IDs. Encoding2 uses exact alternating+0/−0.
Thus this failure is a legitimate scalar-tail/overhead guard; it is not evidence
that executed SSE2 vector comparisons themselves were slower. Static layout,
register allocation or surrounding helper work could contribute, but no causal
attribution follows from these timings alone. Larger reversed trees, wide IDs,
and combined reversal+resize are not implied by this fixture.

This review reconstructs timing and census provenance; it does not reexecute the
separately reviewed correctness/fault suite or claim every validation command was
reaudited. Exact inherited native model and costs unknown; one actual reviewer,
no complete multi-reviewer skill workflow. All artifacts and losing patches remain.
