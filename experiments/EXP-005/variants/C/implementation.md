# Variant C — nonzero width mask

Sequential implementation pass;not independent agent. Backend/model/cost unknown.
Only zbtScoreLeafScore mask expression changes.

bits is unsigned. For widths1..64,(-bits)&63 equals64-bits modulo64,including zero at64. The shifted UINT64_MAX has the desired low ones. Width0 remains guarded.

Original conditional ninth-byte read,zero-width guard,endianness,base/shift,
physical order,leaf layout,index ownership,assertions and allocator unchanged.
All expression forms use standard unsigned C semantics. Main source untouched.
