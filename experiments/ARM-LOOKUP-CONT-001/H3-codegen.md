# H3 ARM static gate

All three isolated candidates were built on the reserved ARM host under both frozen compiler cohorts, before any H3 timing. Their source hashes match correctness-qualified artifacts; full build metadata, disassembly and sizes are retained in the private fleet capture and will accompany results.

A emits bounded first/last halfword or word comparisons and an eight-byte comparison on the proven short-inline path. B emits a compare/branch length dispatch with constant-width comparisons, without a short-path memcmp call. C emits an unrolled byte XOR/OR ladder through eight bytes. Its increasing instruction/branch count is a risk, but it is not the original generic call or an unchanged loop. All retain the original generic/external fallback calls. The actual generated paths satisfy the declared mechanism gate; none is approved on static evidence.

Native A/B retain128-byte leaf frames and the compiler duplicates parts of tag traversal around the specialized paths; C uses112bytes with a single scanner-call site. LTO emits different arrangements and keeps both generic fallbacks. These are compiler outcomes, not new source mechanisms or measured speed causes. Longer functions and extra branches may lose guards. Exact timings will decide under unchanged2%/1% gates.

The six built ELF hashes are recorded in each cohort metadata. Native: A5459e195c70e4e103cb13878a60a0c14fc2b2e9b5e36aae30967d3c1d9828b5e; B8c541425ee19fbc153ce032ecd4590ed7ff7ced2f3bc1deedb5caee245558a78; Cf0c7ac7ad1ea8733152b3ca3b2326999a9095e9cedc5ccadbbf8d4385cb16d7c. LTO: A9644be98aab3fb0c1aa6b812344b9ccb19742c42c0fb527ea1e0e2e0a09094c8; Bae5a58f9c3ca6cd9064727e9a661bbadac0abc4e18358974cd3b7bde7b5e2a45; Cffc9b686c66ce41862c7183d40934b3370d7a7e53e009270691b707e12af05ee.

Qualified ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable; static load/call counts do not supply pipeline slots.
