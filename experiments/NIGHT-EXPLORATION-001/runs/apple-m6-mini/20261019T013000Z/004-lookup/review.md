# Sequential adversarial review — adoption blocked

Same worker as implementation, not an independent reviewer. Exact model/cost unknown.

Semantics: found physical slot maps to logical only on position output. Reversed
packing still subtracts delta from base; removal of reversal in the bit offset
must not remove that subtraction. Private deliberate faults detect both mistakes.
Width0/64 and shifts use unchanged guards, endian conversions and memcpy reads.
B reuses zbtReadBits with width>0; A retains logical wrapper. C duplicates decoding,
a maintenance cost if score format changes. No leaf writes or allocator changes.
Original43 tests and public lookups protect broader ownership/mutation/rank behavior.
Private synthetic leaves check exact bits/output combinations, not complete tree
invariants; this targeted oracle does not replace original tests or pending guards.

Measurement: baseline release instruction text is identical after isolation. Frozen
calibration/controls precede one144row exploratory screen; no overlapping children
or omitted rows. B passes qualified100K but fails unqualified1M. The dual-primary
hypothesis is not eligible; lowering the requirement to100K now would change it.
Static instruction counts cannot substitute for selected-candidate profile validation.
No PMU, migration/frequency data, independent review, exact cross-host replication,
fresh confirmation or full all-size/mixed/long/batch guards. No source adoption.

Portability: only Apple M6 arm64 little endian tested. Reused endian/bit primitives
are portable by source inspection, not measured portability. Signed-zero exact bits
are checked; NaN was neither assumed supported nor supplied to the oracle.
