# Actual timing-binary code mapping

Read-only objdump/source-line comparison after017publication; no new measurement, rebuild or source edit. The actual corrected015/AA timing binary is1ecbe6a4…, independently hash-checked; it is not substituted with the separately built profile control8852aff6… . The diagnostic binary3d8edd53… has zbtIndexScanSlot at0x11930, whereas both original binaries place it at0x11760. Whole binary hashes differ and no whole-program equivalence is claimed.

The two relative half-open regions[0x1d3,0x36a) and[0x69a,0x7c0) cover the helper's word loops, mask/rechecks and scalar tails, excluding later decode/hash/callback and panic paths. All191 instructions, including encoded continuation bytes and source-line attribution, match exactly between all three binaries. Every718 sampled zbtLeafTagMatches inline frame lands on one of these mapped instruction starts. audit-mapping.py independently verifies this mapping against the retained source-linked disassembly and original sample text.

This supports transferring the helper relevance observation to the actual AA code body. It does not establish equal runtime context, cache placement, precise removable cycles or any candidate elapsed gain. Layout/driver differences and coarse sampling limits remain. SourceNONE; no candidate measurement at this checkpoint.
