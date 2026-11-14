# H2-C score-only iterator diagnostic

Static review, 2026-11-14. The [qualified guard decision](../H2-GUARD-DECISION.md) rejects C: forward iteration regressed 24.687–24.720% and reverse iteration 20.413–20.741%, in all three blocks per direction. B passes these five supplemental guards. This review supports a concrete additional dependency in C's score decoder; it does not establish that dependency as the sole cause or explain the magnitude. C remains rejected. This is diagnostic evidence, not a new population vote or authorization to retry C.

## Evidence identity and scope

Read the original `current/src/zset_btree.c`, public header, [guard fixture](../guards/guards.c), [C patch](../variants/H2-C/candidate.patch), [B patch](../variants/H2-B/change.patch), and saved ARM GCC15/LTO guard ELF disassemblies. No fresh proposal files were read. No source changes, new builds, timings, profiling, fleet access, commits or publication occurred.

Frozen source base: `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`; upstream extraction: `ee8e7f70152404649ac947157fd662d11b4a00d5`. Source SHA-256 from the retained variant manifests:

| Source | SHA-256 |
|---|---|
| Baseline | `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9` |
| B revision 1 | `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29` |
| C | `789ca7e217baa67cba165d2ebed7be0c9c1a2a7067f94ae870431395e66ffe49` |

Exact disassembly files are retained under `build/arm-cont-private/fleet/guards-gcc15-lto/`; these are disassembly-file hashes, not ELF hashes:

| File | SHA-256 |
|---|---|
| `assembly-base.stdout` | `aa788a00cfcbca4923a0afbe5e434788d362cfffe689114cc7fb0b1dc8d458d4` |
| `assembly-B.stdout` | `0673ac68d2e04f17a98483946b6a1ddad0e3b6c329e6131fbf5978a6fa0a8cb9` |
| `assembly-C.stdout` | `edc2df7326e26644bcc20949c6c8f7255a167344e506e83f098536da1efbbdb4` |

## The actual measured iterator path

`run_guard` visits 500 elements per sweep, calling `zbtreeIteratorNext(&it, reverse, NULL, NULL, &score)`. It accumulates score and ordinal-weighted score sums. The measured call uses `verify=0`; the model-comparison path is separate. Construction, warmup and full model verification are outside the timer.

LTO inlines iterator traversal into `run_guard` in all three binaries, but retains one call to `zbtScoreLeafScore` per returned element. The score decoder is at `0x403020` in all three. The actual no-verification call sites are:

| Binary | Forward call | Reverse call |
|---|---|---|
| Baseline | `0x40f97c` | `0x40f8ec` |
| B | `0x40f3ac` | `0x40f334` |
| C | `0x40f550` | `0x40f4d8` |

The loops retain leaf, position, ordinal and sums in registers across that call. Forward traversal loads count at leaf entry and compares the incremented position against it; reverse traversal decrements position and follows `prev` when it reaches zero. Their hot element bodies show no stack loads/stores. All three enclosing `run_guard` functions allocate 432 bytes, but that function also implements rank and churn. Its total frame is not evidence of iterator spill costs.

These score-only calls eliminate `zbtScoreLeafElement`, member offsets, hash tags and record decoding. C's cheaper member-offset address therefore supplies no direct benefit on this path. Traversal direction is independent of a leaf's `reversed` physical encoding; the reverse guard alone does not establish that all visited leaves use reversed encoding.

## Decoder difference that survives LTO

Baseline and B retain packed scores at `leaf + 56`. For nonzero score width they calculate physical position, multiply it by width, then load using the fixed data displacement:

```text
baseline/B 0x403040: umull x1, w1, w3
           0x403048: add   x1, x0, x1, lsr #3
           0x40304c: ldr   x2, [x1, #56]
```

Baseline/B load count inside the decoder only when `leaf->reversed` is nonzero. Their decoder instruction sequences otherwise match, apart from the score-shift byte moving from header offset 19 to 18 in B. B's masked flags representation needs no extra mask in this emitted variable-shift instruction; no broader compiler or architecture claim follows.

C moves packed scores behind `2*count` offset bytes and `count` tag bytes. `zbtScoreLeafScores` computes `leaf->data + 3*count`. Its emitted decoder reads count for every nonzero-width score and recomputes that base on every call:

```text
C 0x403030: ldrb  w5, [x0, #17]       // count
  0x403038: add   x4, x0, #56
  0x403044: ubfiz x7, x5, #1, #8      // twice count
  0x40304c: add   x5, x7, w5, uxtw    // three times count
  0x403050: add   x4, x4, x5          // score-stream base
  0x403054: umull x1, w1, w3
  0x40305c: lsr   x1, x1, #3
  0x403060: ldr   x2, [x4, x1]
```

C also computes the reversed-position alternative unconditionally and selects it with `csel` at `0x403048`, where baseline/B branch around that work for normal encoding. The optional cross-word read has an additional address add at `0x4030b4` before its byte load. Zero-width leaves skip these paths. Because the score helper remains out of line, the loop's existing count value does not hoist or replace the decoder's count load and address calculation.

The relocated score stream changes load alignment as well: its base can be odd, and cache-line crossings can differ. Baseline's packed loads can already be unaligned, so “C introduced unaligned loads” would be inaccurate. Neither crossing frequency nor latency is measured here. Source relocation also moves score bytes on count changes, but that mutation work is outside these read-only iterator loops.

This establishes an actual extra load/address dependency on the observed path. It does not isolate dependency latency from branch selection, instruction scheduling, code placement or load alignment, and static instruction listings are not dynamic instruction-count measurements.

## Distinct follow-up, conditional on further evidence

A defensible separate hypothesis is **cache the relocated score-stream base once per iterator leaf**, then decode each element through a scalar helper taking that base. It must change C's per-element mechanism; rerunning unchanged C is excluded. Prefer an explicit iterator cache over relying on forced inlining to happen to hoist it. This is a possible future experiment, not a recommendation to displace the still-eligible B.

The targets would be `zbtreeIterator` plus `zbtreeIteratorStart`, `zbtreeIteratorSeekRank`, `zbtreeIteratorSeekScore`, `zbtreeIteratorSeekLex`, and leaf transitions in `zbtreeIteratorNext`, with one shared scalar decoder accepting a supplied stream base. Set or invalidate the cache through a single helper on every initialization/transition. Public iterators are already invalid after set modification, but every path must preserve that contract. A fresh protocol must explicitly allow the header change; it is outside the current frozen referee.

Risks include larger iterator state, setup cost for short scans or member-only scans, forgotten seek/transition initialization, compiler register pressure and duplicated decoder logic. A cached pointer would typically enlarge the present 16-byte iterator on 64-bit targets; exact layout and calling-code effects require checking. C's altered score alignment remains even if repeated base calculation disappears. Scalar rank/score lookups also remain unchanged, so this follow-up does not claim to repair all C costs.

Before allocating a new timing attempt: inspect a correctness-only census of the exact fixture's leaf counts, widths, physical encoding and score-byte alignment; verify exact emitted candidate loops eliminate repeated base construction without adding hot spills; check start/each seek/empty tree/leaf crossings/both traversal directions, all output combinations, zero/full score widths and external members. Preserve reference checks and mutation coverage. Then a separately preregistered fleet comparison needs qualified A/A, paired baseline/B/new-candidate timing, the original lookup and mutation/memory guards, and timed-region profiles. A persistent >1% iterator regression despite removed base work falsifies the proposed repair; a passing guard alone still would not prove the original regression was entirely address arithmetic.

## Consultation and TMA classification

Backend: inherited execution session; exact model and token cost unknown. This worker's fresh exposed-tool discovery for `cpu-perf`/`library_status` returned no tools, including a second check during this diagnostic. The [controller consultation](../CONSULTATION.md) is shared evidence, not this worker's call: stdio server 0.1.1, bundled list `deb5a0bac467`, 3/287 indexed sources and 158 passages. Its H2 question covered count/width address chains and cache/layout alternatives; no retrieved primary passage established this workload mechanism. A fresh controller consultation on the newly observed iterator regression remains appropriate before selecting a follow-up. No external authority is claimed for the assembly observations above.

| TMA category, share of total pipeline slots | Baseline | B | C |
|---|---|---|---|
| Frontend_Bound | unavailable | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable | unavailable |
| Retiring | unavailable | unavailable | unavailable |

Qualified timed-region TMA roots and children were not collected for these iterator guards. No shares or causal pipeline classification can be inferred from the timing regression, instruction listings or prior CPU-wide captures. This static diagnostic adds no collection or run IDs.
