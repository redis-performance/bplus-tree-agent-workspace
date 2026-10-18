# BOUNDARY-010 — explicit raw lengths at inaccessible page boundaries

Correctness-only test, preregistered before building. Public mmap/mprotect allocations
belong to this test process; no external inspection or permission changes. Raw member
buffers touch PROT_NONE guards on either side in separate left/right placements. Test
lengths0,1,2,3,4,7,8,15,16,17,31,32,33,63,64,65,95,96,97,127,128,129,255,256,257,
319,320,321,4095,4096,4097,65535,65536; hash seeds17/101; mixed binary bytes including
NUL. Distinct length identifies each member; equal prefixes intentionally test explicit
length handling. Zero length at the inaccessible boundary is a non-NULL pointer that
must not be dereferenced. No NaN input.

For every seed/alignment, insert through zbtreeInsertNewRaw with/without valid absent
position, query via raw buffers for hit and absent controls, verify exact finite score
bits including signed zeros, then overwrite/unmap caller buffers. Tree lookup/ordered
iteration/clone after original tree and buffers are freed must still match the independent
SDS model. Read-only protected buffers are used for lookups. Tree nodes never point to
caller pages. Keep all original checks and compile release/debug plus ASan+UBSan.
Each child<=120s. No timings, source optimisation or memory-overhead claim.

Two preregistered isolated intentional faults: raw lookup reads ele[elelen] (guard-page
fault expected), and raw lookup hashes one fewer byte for nonempty buffers (oracle
failure expected). Preserve patches/commands/failures. Tests are sensitive controls,
not source defects. All private changes restricted to test-owned mappings/snapshots.
Root source/referee unchanged; exact provenance/hashes saved; backend/model/cost unknown.
