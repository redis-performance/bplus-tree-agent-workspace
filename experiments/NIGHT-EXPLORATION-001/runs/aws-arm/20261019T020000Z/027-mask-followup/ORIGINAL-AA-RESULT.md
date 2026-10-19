# Fixed original-AA: retained complete evidence

Recorded status: complete. Processes recorded: 120; checked: 120. No retries, seed/count changes or discarded rows.

Independent producer-side audit: 120 processes, 960 rows, 40 cells; decision PARK (never source acceptance).

Required cells: 29; decisions {'QUALIFIED': 18, 'PARK': 11}.
Below10ms floor: 0; >1% precision failures: 11 (may overlap).
Unqualified: original-100/rank, original-1000/lookup-hit, original-1000/rank, original-1000/scan, original-10000/lookup-hit, original-10000/lookup-miss, original-100000/insert, original-100000/lookup-miss, original-100000/scan, original-1000000/rank, original-1000000/scan.

Predeclared diagnostic cells: 11; decisions {'UNQUALIFIED_DIAGNOSTIC': 11}.
Below10ms floor: 11; >1% precision failures: 8 (may overlap).
Unqualified: original-100/insert, original-100/iterate, original-100/delete, original-1000/insert, original-1000/iterate, original-1000/delete, original-10000/insert, original-10000/iterate, original-10000/delete, original-100000/iterate, original-1000000/iterate.

Every block and raw row is retained. Unqualified comparisons cannot establish calibrated speed/regression; qualified all-six>1% loss rejects, mixed exceedance parks, including qualified diagnostics. No average rescues a failed block.

Separate postcheck verifies immutable original/suffix receipts, snapshots, source/referee, protected and guard identities and owned-runner idle state. Original027 preparation remains FAILED and separate028 composite correctness stays explicit. Fresh primary improvement is provisional. Required guard qualification, independent held-out confirmation, validated matched profile and adversarial review remain gates. Source selectionNONE; old026 PARK unchanged.
