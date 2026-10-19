# Pre-measurement independent static review

Root reviewed all three sealed patches against exact13e459ff8 before any ARM candidate
timing. No source/referee changes are requested. Only src/zset_btree.c changes in each
patch; header, layouts, allocator, hashing and assertions remain unchanged. Provenance,
patch/source hashes and immutable author publications are recorded in the adjacent JSON.
All authors sealed before reading peer implementations.

A uses a word index with an explicit two-word entry check; C uses a byte index and
remaining-count check. Both narrow exact comparison bytes then retain one bit per
nibble before ordinary lowest-bit enumeration. B keeps four bits per matching nibble
and clears that complete nibble after each emitted lane. Every vector load is fully
inside count, original word/scalar residual boundaries remain exact, tag1 alone also
matches physical0, and reversed leaves map each ascending physical position through
count-1-position. Nonzero-loop guards protect bit scans; largest nibble shift is60.
Conservative little-endian AArch64 guards retain the portable behavior elsewhere.
No static semantic, bounds, shift or aliasing blocker found. This is not native proof.

An independent Python arithmetic model exhaustively enumerated all65,536 possible
16-lane equality patterns for both reductions: little-endian paired bytes shifted4
and narrowed produce two exact nibbles; A/C one-bit extraction and B whole-nibble
clearing both emit each matching physical lane exactly once in order. Reversed mapping
was checked too. Native intrinsics/codegen, original tests, V2 oracle, sanitizers and
full scan semantic coverage remain mandatory in the separately frozen600-second job.

## Maintenance preference frozen before timing

Comment-aware lexical filtering preserves C string/character literals, removes comments
and blank lines, strips line-end indentation, then counts added+deleted lines against
baseline with SequenceMatcher(autojunk=False). A=28, B=26, C=26. Under the already frozen
A/B/C tie-break, the preference among implementations passing every primary block is
**B, then C, then A**. This is a source-size maintenance preference, never a performance
superiority claim. No passing implementation means NONE. No changes or preference
adjustments after timing. Root still must review the worker's exact validation/timing
freeze before launching the fixed144-row screen. Source adoption remains NONE.
