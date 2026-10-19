# Actual enabled-binary hot-region map — observations, no proposal

This maps retained PCs to the exact enabled binary
`7c088393dcd381154869327e626d06e4bd73c42a93ed888663e796b1e8cfefb8`,
the shared corrected-adapter tree object, and source d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2.
No workload ran. Actual linked disassembly and symbol inventories were read with
bounded metadata commands; optimized DWARF lookups use the retained tree.o.
All five inspected functions have identical linked/object instruction counts and
ordered mnemonics, supporting translation by the same symbol-relative offset.
Addresses and relocation operands differ; this is not a runtime-equivalence claim
about the ordinary uninstrumented benchmark.

## Scan: what the captured locations actually identify

The four scan captures have 417 exclusive PC observations: 367 zbtIndexScanSlot,
26 zbtIndexScanGroup,17 SipHash,5 scan_count and2 zbtreeScan. These are one-PC
locations, not inclusive stack frames or time/cycle estimates.

DWARF identifies the inlined zbtLeafTagMatches instance at slot-relative ranges
`[496,612)` and `[620,1256)`, called from src/zset_btree.c:4195. These are exact
range-membership partitions of the retained locations:

|Size|Seed|Scan-slot locations|Inlined tag-match locations|Other slot locations|
|---:|---:|---:|---:|---:|
|100K|1|93|46|47|
|100K|2|88|45|43|
|1M|1|95|49|46|
|1M|2|91|44|47|
|Inventory total|—|367|184|183|

The actual slot function contains 514 static instructions and no `vN`/`qN` vector
register instruction. Its inline tag matching uses **scalar 64-bit SWAR**, comparing
eight tag bytes per loaded word, rather than NEON auto-vectorization. This is
already an eight-byte comparison algorithm; absence of NEON is not evidence of a
profitable transformation. No other-ISA executable was inspected or compared.

The emitted operations include the source's word XOR/subtract/high-bit mask,
zero-tag folding for index tag 1, clearing the first mask bit, `rbit`/`clz` to obtain
the matching byte index, exact candidate-byte checking and logical-position stores.
The source explicitly permits false-positive mask bits, so candidate verification
is semantic work. Complete-word loads and the scalar tail remain present.

|Slot offset|Captured locations|Actual instruction/region|Source mapping|
|---:|---:|---|---|
|+512|18|`tst w8,#7`: tail remainder test|4148, inlined tag matching|
|+888|10|`ldr x0,[x12,x17]`: tag-word load|4138, inlined tag matching|
|+916|14|`cmp w9,#1`: tag 1 mask selection|4140, inlined tag matching|
|+960|98|`cmp w9,#1`: candidate-check sequence|DWARF line 0; inline region known, exact statement unresolved|
|+1256|26|`cbz w27,...`: zero-match assertion branch|4198, after inline tag matching|
|+1376|10|`ldr w19,[x8,x20,lsl#2]`: selected position|DWARF line 0; no exact statement claim|
|+1640|14|`ldr x13,[x13]`: reachability-probe bucket tags|4107, inlined zbtIndexHashReachesBucket|
|+1668|12|`add x10,x10,#1`: reachability probe advance|4108, same helper|
|+1748|10|`ldrh w10,[x10,w11,uxtw#1]`: member record offset|379, inlined zbtScoreLeafOffset|
|+1756|16|`ldrb w2,[x10]`: packed-record type byte|589, inlined zbtPackedData|

Near +960, the actual sequence continues `rbit`(+964), `clz`(+968), byte-position
combination(+972), `ldrb`(+976), conditional compares and the position store.
The large count at the comparison does not establish that the comparison, branch
prediction or a nearby load caused the delay. Signal delivery, sampling cadence,
code layout and the instrumented frontend remain possible influences.

The other slot locations include leaf/table validation, output position consumption,
collision/home-range reachability checks, packed member/score decoding, callback
dispatch and return. They must not all be relabeled tag-match cost. ScanGroup's
observed offsets include tag tests and the prefetch loop at source 4248–4253; an
actual `prfm pldl1keep` location occurs at +672. This establishes emitted prefetch
code, not cache residency or effectiveness.

## Lookup and rank: bounded additional map

External dladdr labels identify 402 `_platform_memchr` locations in lookup-hit and
521 in rank. They are coarse external locations without captured caller stacks;
they are not memchr latency or inclusive leaf-search cost. The actual
zbtScoreLeafFindMember has a memchr stub call at +188, consistent with the source
search at 1287. Across the selected lookup/rank functions, the largest retained
member-helper offset is +212 (`ldrb w8,[x9]`, 127 locations), mapped to the packed
record-type check at 1293; +204 loads the member offset (19 locations, 1290).
The combined inventory is explicitly split by capture in JSON, not interpreted
as a pooled performance estimate.

zbtreeScoreRaw +1192 is `ldr x8,[x21]`, 37 locations, inside the inlined index-table
find at 1939. +1340 resolves the leaf pointer (10 locations, 1950), and +1360 loads
the leaf ID for its assertion (16 locations, 1957). These are actual bucket/leaf
access instructions, without evidence of their load latency.

zbtreeRank contains index lookup and the later ancestor/left-sibling count sum.
Its +1408 load maps to the same index source 1939 (27 locations). Its +2216
`ldp q4,q5,[x10,#-0x30]` has 41 locations and maps to source 3254's child-count sum;
the surrounding `add.2d`/`addp.2d` instructions demonstrate NEON vectorization of
**that separate rank reduction**, not LeafTagMatches. +2308 is a loop-control branch
(60 locations, 3253). +52 is a member-header byte load in the rank entry sequence
(59 locations; optimized line mapping 3262). None is assigned cycles or a unique
source-level cost.

## Provenance and limits

hot-region-map.json retains every sampled offset for the five functions, actual
instruction, per-capture count, optimized DWARF line/inline ranges and vector
instruction inventory. selected-instructions.s is an annotated linked disassembly
listing, not new compilable source; addresses are presented relative to the image
or symbol. commands.json contains all bounded read-only tool commands and private
raw-output hashes. Full raw metadata remains in ignored scratch/m6-member-hot-map.

DWARF line 0/no-line remains unresolved; declaration lines are never substituted
for exact statements. Coalesced/unknown/import mappings retain their earlier
limitations. No system memchr implementation or other-ISA code was disassembled.
The enabled frontend differs from the original benchmark; shared tree.o does not
prove unchanged runtime behavior. No new hypothesis, proposal, source change,
measurement, build, profile, test, shared-document or Git action is selected here.
Participant /root/followup_proposal_b; exact model/token/currency cost unknown.
