# Variant A — nonzero width mask

Sequential implementation pass;not independent agent. Backend/model/cost unknown.
Only zbtScoreLeafScore mask expression changes.

For widths1..64,64-bits lies0..63. Shifting UINT64_MAX leaves exactly bits low ones; width64 is shift0. Width0 remains outside the branch.

Original conditional ninth-byte read,zero-width guard,endianness,base/shift,
physical order,leaf layout,index ownership,assertions and allocator unchanged.
All expression forms use standard unsigned C semantics. Main source untouched.
