# H4 ARM static codegen gate

A, B and C are **ELIGIBLE for the selected codegen mechanism** in both saved ARM cohorts. None requires a mechanism-based `NONE`. This is permission to proceed through the existing measurement gates, not a performance selection or adoption recommendation. No binary, timing script, correctness suite or fleet command was executed for this review; only saved disassembly, size captures, metadata and patches were inspected.

Reviewer: helper-boundary implementer, conducting a separate pass from the controller. The reviewer authored H4-A; this is not an author-independent review of A. The B/C patches were inspected under this review assignment. Detailed participant provenance remains private.

References below use `N-A` for `build/arm-cont-private/fleet/H4-native/assembly-A.stdout`, `L-A` for the corresponding `H4-lto/assembly-A.stdout`, and similarly B/C. Line numbers are one-based in the full saved disassembly, not the extracted raw-function files. Metadata records source freeze `ee8e7f70152404649ac947157fd662d11b4a00d5`, with identical per-variant source hashes across the two cohorts. Artifact hashes are recorded below so these references remain exact.

The claim is **per table**: the successful home probe skips that table's negative filter. During resize, a lookup may first fail in the new table, consume its filter, then hit the old table's home bucket. Rehash maintenance may also compute insertion filters. Neither is evidence that the successful table's filter was hoisted. Candidate tag folding/broadcast, candidate-mask arithmetic, hashing, migration checks and the existing leaf call remain necessary and are not counted as negative-filter work.

## Executed lookup entry points

Native `lookup_loop` calls `zbtreeScoreRaw` at lines 1333 and 1356 in each artifact. LTO has two live functions: the scored path calls normal raw and the no-score path calls `zbtreeScoreRaw.constprop.0`. Their call-site pairs are L-A:11890/11908, L-B:11946/11964 and L-C:11466/11484. Checking only the normal raw extract would miss the primary no-score path.

## A — complete predicate boundary

The patch changes only the declaration of `zbtIndexHomeMayContain` to `noinline` (`variants/H4-A/implementation.patch`:9–13). Its formula, load, call sites and existing `probes == 0` placement are unchanged.

| Cohort | Successful candidate bypass | Deferred filter evidence |
| --- | --- | --- |
| Native | Leaf call `0xc364` at N-A:11993 branches on success at 11995 to `0xc90c`; that block returns 1 at 12355–12362. Other leaf-success branches at 12074, 12180 and 12302 reach the same exit. | Exhausted matches at 11998 reach `0xc720`; 12232–12237 tests the probe counter before calling the predicate at `0xc730`. The other width/table call sites are 12101, 12206 and 12329. |
| LTO scored | Leaf call at L-A:5728 and success branch at 5732 reach `0x406630`; other leaf-success branches 5813, 5952 and 6039 reach that same return block. | Predicate calls remain in fallback blocks at 5902, 5907, 6088 and 6093. |
| LTO no-score | Leaf call at L-A:6179 and success branch at 6183 reach `0x406d30`, which returns 1 at 6546–6553; other success branches are 6264, 6403 and 6489. | Exhaustion at 6186 reaches `0x4069c4`; 6327 tests the probe counter before the call at 6358. Other fallback calls are 6353, 6538 and 6543. |

The complete multiply/shift/OR mask and home-summary load/test reside in the outlined predicate: N-A:1491–1527 (`0x2160` onward), L-A:1445–1479 (`0x401ea0` onward). LTO's multiply is at 1458, summary load at 1472, and `bics` at 1473. The folded-zero special case remains inside this helper at 1476–1479. The helper has no stack frame. Success exits do not enter it. **Eligible in native and LTO.**

## B — query-mask boundary

`variants/H4-B/candidate.patch`:9–22 introduces a lookup-only `noinline` wrapper around the original mask formula. The insertion-side call remains inline; home addressing, summary comparison and all probe logic remain at their original source positions.

| Cohort | Successful candidate bypass | Deferred filter evidence |
| --- | --- | --- |
| Native | N-B:11979 calls the leaf at `0xc32c`; 11981 branches to the success epilogue `0xc930` at 12364–12371. Other success branches are 12062, 12176 and 12308. | Match exhaustion at 11984 reaches `0xc71c`; 12231–12238 tests the probe counter, calls the mask helper, then loads and compares the summary. Other helper calls are 12088, 12201 and 12334. |
| LTO scored | L-B:5725/5729 call the leaf and branch to success `0x40666c`. Other success branches 5814, 5959 and 6049 reach that exit. | Mask calls are 5903, 5912, 6007 and 6103, all in failed-home paths. |
| LTO no-score | L-B:6197/6201 call and branch to success `0x406dac`, returning 1 at 6577–6584. Other success branches are 6284, 6398 and 6510. | Exhaustion at 6204 reaches `0x406b48`; 6424 tests the probe counter and routes to the call at 6458. Summary load/test follows at 6462–6464. Other calls are 6449, 6560 and 6569. |

The mask helper is frameless at N-B:1491–1506 and L-B:1445–1460; the LTO multiply/shift/OR sequence is 1453–1459. Its calls were not hoisted across successful home matching in either captured build. The pre-candidate multiply at N-B:11941 or L-B:6157 broadcasts the candidate tag with `0x0101010101010101`; it is not the negative-filter multiplier. Home address preparation can remain live across matching because candidate lookup also uses that address. **Eligible in native and LTO.**

## C — failed-home continuation boundary

`variants/H4-C/change.patch`:14–62 extracts the original candidate body into one inline helper; the removed original body at 85–123 matches its order and checks. Lines 153–161 retain the table-size guard, try home candidates, then call the continuation. The continuation checks the original predicate at 77, starts at home with probe count zero, and skips only the already-exhausted home candidates at 128–132. Existing home tombstone/empty-slot bookkeeping remains immediately afterward (134–135); wrap progression and final first-deleted hint handling are unchanged context. Thus home tombstone priority, early-empty termination, collision order, optional outputs, narrow/wide IDs and migration checks remain structurally preserved. This is a source/control-flow audit, not a replacement for the existing correctness results.

| Cohort | Successful candidate bypass | Deferred filter evidence |
| --- | --- | --- |
| Native | N-C:12529/12532 call and branch to `0xcf3c`, returning 1 at 12751–12759. Other home candidate successes at 12602, 12646, 12691 and 12794 reach that exit. | Only after exhaustion at 12535–12536 does argument setup 12537–12546 reach continuation call 12547 (`0xcc0c`). The other table uses call 12723 (`0xcecc`). |
| LTO scored | L-C:6532/6535 call and branch to success `0x407094`. Other successful leaf returns at 6620, 6662, 6707, 6760 (nonzero falls through) and 6831 converge there. | Continuation calls are 6549 (`0x406d44`) and 6634 (`0x406e98`), after home candidate failure. |
| LTO no-score | L-C:6933/6935 call and branch to `0x4076cc`, returning 1 at 7161–7169. Other success branches are 7019, 7063, 7106, 7160 (nonzero falls through) and 7231. | Continuation calls are 6949 (`0x40737c`) and 7035 (`0x4074d4`), after home candidate failure. |

The negative-filter multiply and summary test are entirely in the continuation: native `0x3d00`, `0x3d38`–`0x3d40` (N-C:3300,3314–3316); LTO `0x404ea8`, `0x404ee0`–`0x404ee8` (L-C:4572,4586–4588). Native probe zero initialization and candidate bypass are visible at 3324–3338: home bookkeeping runs before any subsequent bucket candidates. The continuation's source precondition is a nonempty table, enforced by its inline caller; a later compiler-emitted size test does not make it safe to call directly on an empty table. **Eligible in native and LTO.**

## Static tradeoffs and limits

| Variant | Native raw frame | LTO scored / no-score frame | Outlined fallback frame, native / LTO | Native / LTO whole-executable text bytes |
| --- | ---: | ---: | ---: | ---: |
| A | 176 | 176 / 160 | 0 / 0 | 98,151 / 55,651 |
| B | 176 | 176 / 160 | 0 / 0 | 94,543 / 55,871 |
| C | 144 | 144 / 144 | 192 / 208 | 87,623 / 54,075 |

Frame evidence: N-A:11924, N-B:11908, N-C:12444; L-A:5660/6112, L-B:5652/6127, L-C:6444/6846. C continuation allocations are N-C:3272 and L-C:4554. Text values are line 2 of each corresponding `size-{A,B,C}.stdout`; they are static executable totals, not isolated-function savings, instruction counts, or timing measurements. Native prehashed frames are A=160, B=176, C=144 (N-A:12380, N-B:12389, N-C:12816); the raw-path gate above does not claim an exhaustive codegen review of every other public API.

A adds a predicate call on failed-home lookups and other existing predicate users. B adds a mask call while retaining caller-side home-summary addressing/comparison. Both retain the large raw frames and existing leaf boundary. C shrinks the raw frame/text but introduces a larger general continuation with optional-output handling and stack argument stores (for example N-C:12537–12546). Its caller-plus-continuation allocation is 336 bytes native or 352 bytes LTO before any deeper callee frame; its lower hot frame does not establish lower fallback stack usage. Collision/displaced/resize guard costs remain a measured question. No cache, branch-predictor, IPC or throughput conclusion follows from these static differences.

TMA classification: for ARM baseline and all H4 candidates, Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and all child shares remain **unavailable**: qualified collector scope/formulas/exclusions are absent. This review collected none and does not infer them from assembly or transplant Intel classifications.

Availability/provenance: this review's tool-catalog discovery found no callable `cpu-perf` / `library_status` endpoint. The shared controller's actual H4 filter-boundary stdio consultation is recorded in `H4-selection.md`:13; it supplied no supporting source passage. No new consultation is claimed. Backend/model costs are not measured here. Eligibility is scoped to these exact saved builds; correctness, fresh frozen traffic guards, all speed/memory gates, independent confirmation and adversarial review remain required by `H4-selection.md`.

## Artifact identity

**native**

| Variant | ELF SHA-256 from capture metadata | Full assembly SHA-256 |
| --- | --- | --- |
| A | `821ac6b6df2d0f6b7cbf73939a9d740eba90176cd970aed3338efb4504c5d076` | `a67ed4d85d054ef83fc4d0033f7689bd88209309f555dac6779c6f9588d1328e` |
| B | `d4bfd7bbde2096af3219f7f95e3a9bea7c64cbb786819d7088f34a4ea8a99a22` | `93c6c5324bf50b75605111bf47b67b8f36688deaf4d1cb5b7685c4ceb71011ae` |
| C | `aa6795d727a79d7c1297589ae96a46f21db0b70d3bc1e68103c6542ab20809ca` | `d7559906c805b2e37d16221bbe2b5bb390574bbca8913c8ee2b2887c92015c18` |

**lto**

| Variant | ELF SHA-256 from capture metadata | Full assembly SHA-256 |
| --- | --- | --- |
| A | `8459ace5e95a39dffb74c0e437358eb57062aade3eb2b8d4cbe163db1a8f078f` | `846d0eb203b50b8b0749c07f9af674d63d78628f13515ce498c59ecd83e935cb` |
| B | `af82c89299132d0f88cd13c992b121bd16614f09f2c20297bfadaf64dfcbad83` | `6295ed37bd08e282c294a75a6b98ac4a87674b11027a85887af3a4d2f3bb8a9c` |
| C | `11b27b036225992a6e548ad7b865323c84c127e97da3f3d7a32ed1cdcf85025c` | `735a4d5057ddaf44a7ff433842fd6b27d02699982c6966469b5f1d5abf616477` |

Raw captures remain controller-retained under the artifact directory above; no private runner addresses or operational command paths are reproduced here.
