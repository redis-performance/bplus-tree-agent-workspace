# Independent review of rejected ARM code generation

**The static claims in ARM018 revision3e085fdcf are supported.** The generated
predicate reconstruction is a plausible contributor, not an established causal
allocation of the measured slowdown. No runner access, build, candidate edit,
timing or profile occurred during this review. REJECT/NONE is unchanged.

An independently authored parser checks the existing017 validation disassemblies,
all instruction/opcode records used by the report, command/snapshot provenance,
and continuing zero-mask control flow. It does not run the worker's analyze.py.

Each of six candidate predicate regions (A/B/C, forward/reversed) contains exactly
35 reconstruction instructions:2strb,1ldrh,1scalar and,14ubfx,1lsr,1fmov into the
first vector lane, and15lane moves for lanes1–15. Interleaved tag loads/address
arithmetic and C comparisons are correctly excluded. Source-linked assembly and
setup dataflow connect this packed predicate to tag==1. The chunk loop backedges
return before the stack stores; no per-chunk tag!=1 branch bypasses reconstruction.
Thus the report correctly identifies repeated work even for ordinary tags.

|Variant|Function instructions|Frame bytes|Continuing zero-mask path|
|---|---:|---:|---:|
|base|509|528|19 per8bytes|
|A|654|544|56 per16bytes|
|B|642|544|51 per16bytes|
|C|646|544|54 per16bytes|

These counts independently match. Frame size includes the initial96-byte register
save plus432/448-byte subtraction. Path tracing takes cbz for zero masks, does not
take cbnz, follows the backedge, and leaves the final-chunk exit untaken. Two full
baseline chunks correspond to38 static instructions on this specifically chosen
path. This is not a general dynamic instruction count or a cycles comparison.

A forward0x10778–0x10788 and C0x10758–0x10768 contain fmov/cnt/uaddlv/fmov followed
by a population-count zero test; the output loop decrements that count while
clearing one low bit. B tests its full nibble mask at0x10650 and clears the chosen
four-bit nibble with a shifted0xf and bics. Those distinct compiled loops are real.
They do not isolate the reason for B's smaller measured loss: changes in surrounding
register allocation, scheduling and decode remain confounded. Reverse/output/tail
paths must not be replaced by this one zero-mask trace in any performance model.

Candidate disassembly commands target each exact build/btree-bench; validation
snapshot binary hashes join the unchanged comparison freeze and post-discovery
identity. Baseline disassembly is of the validation rebuild, whose complete.text
hash equals the actual869425... A/A/discovery control by the immutable completed
validation assertion. The raw section bytes are not public here, so this reviewer
checks that provenance chain, not an independent live ELF rehash. Source paths and
debug information alone would not suffice; the binary/text joins are essential.

The report appropriately keeps tree-owned heap memory separate from a16-byte
stack-frame increase. Static duplicate hash call sites do not establish two calls
per operation. The apparent35-instruction redundancy neither gives its cycle cost
nor proves that removing it would recover the regression. A matched scoped
baseline/B diagnostic can test whether extra retired instructions and samples are
consistent with this mechanism, while accounting for sample skid, changed layouts
and actual callback counts. It cannot by itself isolate a counterfactual fix.
No old baseline sample share can be assigned to newly changed addresses.

Reviewer AMD authored C; this is independently authored static reconstruction,
not independent C authorship review. Root's source review remains separate. Exact
inherited model and costs unknown. No stronger-model panel or complete skill
workflow is claimed. All losing patches and the unexecuted confirmation remain.
