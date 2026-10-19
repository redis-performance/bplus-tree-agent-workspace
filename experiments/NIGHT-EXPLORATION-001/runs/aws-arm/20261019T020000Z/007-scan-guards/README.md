# Additive focused SCAN guard referee

This referee covers36 cells and three seeds (108 independently checked fixtures):
4096/100000 members,16/321-byte binary keys, shuffled/descending/all-equal insertion,
and unfiltered/dense-high17/folded-high0+1 original SipHash distributions. It is a guard
for the existing all-match scan population, not a new optimization population. No
candidate timing is performed by this worker. See PLAN.md for the frozen timing schedule
and2100-second budget approved before timing. Root review must precede Intel execution.

`scan-guard.c` uses only public tree APIs and original hashing/allocator. The independent
model supplies expected bytes, exact finite score bits and full member coverage. Legitimate
SCAN duplicates are allowed; emitted callback count is reported separately from logical
members. `passes=0` validates without reading either benchmark clock. For timed runs,
key loading/hash verification/insertion, two warmup traversals and complete pre/post
semantic oracles are outside the clocks. The timed callback consumes ID, length and score
bits; no private profiling/census code is linked into that executable. There is no claim
that this callback has the same cost as the original count-only scan referee.

`tree-census.c` includes the exact selected tree source only in a separate diagnostic
executable. That executable refuses nonzero passes. It checks physical stored tags
against recomputed original hashes, and reports reversed members/leaves, external records,
leaf populations, tag histogram, active resize and wide-ID state. Diagnostic source
inclusion can change compilation; its runtime is never treated as a performance result.
The independent semantic outputs and owned bytes must equal the separate-TU native
binary for the same fixture. Sanitizer allocation sizes and legal duplicate counts need
not equal native allocator results; each sanitizer output is checked against its own
independent model. Same-allocator comparison binaries must match callback count/checksum
and owned bytes, along with all fixture metadata.

Build from isolated baseline8fab511e or exact selected B snapshot; never patch this repo's
bench, compatibility layer, vendor tree or original tests. Use the same relative output
path for every source snapshot. Example (REFEREE is the published007 directory):

```
python3 "$REFEREE/build.py" --source "$SNAPSHOT" --out "$SNAPSHOT/build/focused"
python3 "$REFEREE/build.py" --source "$SNAPSHOT" --out "$SNAPSHOT/build/focused-san" --sanitize
python3 "$REFEREE/validate.py" --native "$SNAPSHOT/build/focused" --sanitize "$SNAPSHOT/build/focused-san" --out "$RESULTS" --seeds 101,102,103 --seconds 600
```

The builder copies exact driver/census inputs beneath the requested output directory;
all compiler frontend/output paths are relative to each snapshot. Use identical relative
output paths across sources, compiler, flags, assertions and allocator. No LTO or timing
REDIS_TEST/REDIS_DEBUG/NDEBUG. Original43-test binaries are also built and must be run.

Fixtures are compact deterministic nonce files, not serialized tree layouts. Header is
8-byte magicSCANG001, followed by big-endian64-bit n/bytes/seed/distribution, then n
big-endian32-bit nonces. Every timing process reconstitutes keys and checks genuine hash
selection outside the clock. Generator bounds each nonce search at1000000 attempts;
failure terminates rather than substituting tags. SHA256 manifests identify complete
fixture files. The driver generates them with:

```
scan-guard generate FILE N BYTES SEED DIST v1
scan-guard run FILE ORDER PASSES FAULT
```

DIST0=unfiltered,1=high17,2=high0or1. ORDER0=shuffled,1=descending,2=all-equal shuffled.
FAULT0=normal;1=wrong score;2=wrong length;3=omit every callback for actual member0;
4=wrong member content. Fault controls must exit2. No faults are used in timing.

Resize semantic coverage is explicitly provided by unchanged original tests in baseline
src/zset_btree.c: the block near4930 reserves50000, triggers a real incomplete resize
with fewer than half the members in the new table, scans all live members and verifies
rehash remains active; the block near5822 exercises repeated table replacement and
anchor coverage. These are correctness checks, not focused resize performance guards.
Dense/folded active-resize performance and tied-score construction/traversal performance
remain separate missing gates. A census showing only one64-member reversed leaf gives
sparse reversed coverage, not an all-reversed workload. Native IDs may remain narrow;
report that actual limitation. No source acceptance follows from guard correctness.
