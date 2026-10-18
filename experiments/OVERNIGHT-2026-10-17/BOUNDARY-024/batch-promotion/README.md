# Batched lookup across natural width promotion

The initial eight discovery and eight fresh-confirmation cells pass their actual
lane schedule and detect a deliberately stale table descriptor. They retain a fixture
scope mismatch: the planned ID1/2 lanes selected only ID2. See [scope note](SCOPE-NOTE.md).
Those outputs and snapshots remain unchanged; they are not claimed as ID1 batch coverage.

[Attempt 002](attempt-002/README.md) changes only the lane expression to alternate
IDs1 and2, preserving all assertions, bounds, seeds, source candidates and compiler
settings. Its separate evidence is the final intended fixture. The original full
models checked ID1, but that did not substitute for the missing batch input.

Each actual fixture observes one16-lane public batch enter with a narrow current
index and wide resize destination, then return with completed wide current index.
Exact masks/hit scores, duplicated keys, misses and outside-count output canaries
are checked. Miss output lanes remain unspecified. The same SCAN cursor, all initial
anchors, current score model, external ownership and exact usable bytes are retained.
No timing result or source adoption follows these checks.
