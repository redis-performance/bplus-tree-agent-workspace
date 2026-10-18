# Variant B — nonzero width mask

Sequential implementation pass;not independent agent. Backend/model/cost unknown.
Only zbtScoreLeafScore mask expression changes.

For widths1..64,bits-1 lies0..63. Unsigned64 multiplication by2 wraps only at width64,then subtract1 yields UINT64_MAX. All other widths yield 2^bits-1. No signed overflow or shift64.

Original conditional ninth-byte read,zero-width guard,endianness,base/shift,
physical order,leaf layout,index ownership,assertions and allocator unchanged.
All expression forms use standard unsigned C semantics. Main source untouched.
