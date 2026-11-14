# Independent lifecycle correctness result

**PASS for the one fixed native lifecycle diagnostic.** The saved transcript demonstrates the required stale-hint, duplication, Rebuild and cleanup coverage under the frozen operation sequence. It is bounded correctness evidence for the original source plus shadow instrumentation, not a production hint implementation, performance result or adoption. Selected source remains NONE.

| Evidence | SHA256 |
|---|---|
| Frozen 29-file manifest | `cd9b4bf0ea2dc4b0ce0c5109d1d87e76ae08c0e686c8183d32aa6c7abdd5deee` |
| Harness | `87767ea2c51024323cfe25e0df9303bb3b617863bcbfb39630ec91a3148886bc` |
| Strict checker | `a9bc63863e97e5216b1b0f85152483e2fe83fffe2c7bb67cd9ca493a2154bee9` |
| Native executable | `88df91ad164ddee020fc88db60c010eb4ca32fa7cb7ecfad4c6b7359eb1e3208` |
| Raw archive | `bd4815d9a694fdcdafa8ac2ff80ed20657158825583e699d5669b60068b41e5d` |
| Raw stdout | `81cbf9004a8e863fead238b0c7c2dd6d6ca76f12435acb5eb6766c35c736ed42` |
| Independent semantic evidence | `f11320b74a343f3e73f533ecc82dabb511b933a0ae63f389e4d6292d6dcdbaaa` |

This reviewer proposed the bounded lifecycle sequence and previously reviewed the slot-hint census. The harness author and the independent lifecycle source/target reviewer are separate participants. This final review inspected frozen source and fetched raw evidence only; it executed no C program, accessed no fleet host and requested no retry. The [source review](SLOT-LIFECYCLE-SOURCE.md), [target review](SLOT-LIFECYCLE-TARGET.md) and separate operational review retain their respective scopes.

I rehashed all 29 manifest entries, all 135 configuration input pins and the exact retained executable. Configuration and admission hashes join. The archive hash matches, and its diagnostic/validation stdout, stderr, commands, completion and admission bytes match the fetched files. The command record contains exactly one no-argument native diagnostic invocation and one checker invocation, both status0; both stderr files are empty. Strict `loads()` followed by `check()` passes and exactly reproduces the saved `native-validation.stdout`. Completion records correctness only, with qualification and adoption false. Reservation, deadline and fetch-isolation verification belong to the operational audit.

Independent arithmetic, without using the checker's model generator, gives the following expected outputs. The five duplicate/deleted checkpoints deliberately share the same model.

| Checkpoint | Members | ID sum | Score sum | Observed owned bytes |
|---|---:|---:|---:|---:|
| inserted | 2,048 | 2,096,128 | 2,098,176 | 416,240 |
| deleted | 1,984 | 2,092,096 | 2,094,080 | 408,008 |
| dup_original | 1,984 | 2,092,096 | 2,094,080 | 408,008 |
| dup_copy | 1,984 | 2,092,096 | 2,094,080 | 408,008 |
| rebuilt_original | 959 | 976,896 | 977,855 | 202,504 |
| rebuilt_copy | 1,984 | 2,092,096 | 2,094,080 | 408,008 |
| freed_original_copy | 1,984 | 2,092,096 | 2,094,080 | 408,008 |

The fixture has 2,048 deterministic binary members of lengths16/128/384, embedded zeros and scoresID+1. The first deletion removes IDs0,2,…,126. The range victims are derived from the independent remaining-ID vector before the API call: inclusive ranks512–1536 remove exactly1,025 members. Every raw checkpoint matches the independently computed cardinality, ID sum and score sum. The reviewed C checks additionally cover every membership/score answer, forward/reverse rank and iteration, regenerated caller bytes, score object bytes and unchanged negative-output sentinels. Those detailed assertions are executable-bound evidence; the aggregate JSON does not serialize every member and output for separate replay.

Each checkpoint performs8,192 public model lookups, totalling57,344. Seven checkpoint hint audits plus the two immediate duplication audits add3,795 direct original leaf searches. Their sum is exactly **61,139**, below the fixed65,536 bound. This count excludes construction/deletion operations and iterator steps; it is the declared verification-lookup budget, not all operations performed by the process.

After insertion, all493 enabled hints are eligible, unchanged and successful. The64 individual deletions cause **57 slot-zero ID writes and57 invalidations**. The436 remaining hints partition into380 unchanged and **56 stale**, including28 out-of-range and28 in-range stale positions. All436 seed members are nevertheless found by the original full leaf search. Thus the run demonstrates fallback success for these stale seed-query cases; it does not infer staleness from an unrelated query mismatch or short-circuit the original search.

Duplication copies one512-bucket table into a distinct generation. Immediate pre-duplicate and duplicate audits agree exactly:436 enabled/eligible hints,380 unchanged,56 stale,28 out of range and436 full-search successes. The recorded reseed count is zero. The reviewed runtime assertion compares complete hint arrays, including copied bytes, rather than a fingerprint. Exact snapshots also remain equal around the original's range deletion and destruction. The duplicate passes its full1,984-member model after both actions, including after the original's external records have been freed.

The range deletion necessarily takes the original source's Rebuild branch:1,025 is greater than1,024 and at least one tenth of1,984. Lifecycle events24–25 allocate generation10 and retire generation8; generation9, the duplicate, stays live. The new256-bucket table has **250 Rebuild-origin seeds**. Every one is eligible, unchanged and successful; fresh stale, out-of-range and ineligible counts are zero. The original's959-member model and the unchanged duplicate model both pass.

I independently replayed all27 lifecycle records: nine allocations, one duplication, seven promotions and ten releases, with monotonically increasing generations and valid registry-slot reuse. At most three table generations are live simultaneously; the largest table has512 buckets. All observed IDs use narrow tables. Event26 releases the rebuilt original generation10; event27 releases duplicate generation9 in cleanup phase, leaving zero live generations. The success record follows the reviewed original/duplicate/member-buffer frees and completion assertions. The old fixed-query census arrays remain unused. This is successful bounded cleanup, not a general allocator leak detector or proof of forced address reuse.

Owned-byte fields are observations, not an independently fixed memory oracle or a <=1% candidate-memory guard. No sanitizer, defrag, high-ID boundary, forced address reuse, arbitrary mutation history, active receiving-table audit or compiler comparison is established. All hint audits were eligible; growth promotions occurred, but that alone does not establish the missing active-resize cases. Direct audits use copied seed identity as the query, so arbitrary-query predicate combinations remain outside this result. The native GCC13.3 executable is the only executed build.

The separate completed census and its exposure counts are unchanged. This result adds no performance population, approval or adoption; H2/Q4 remain PARK and ARM remains released. Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and every child category remain unavailable because no TMA or execution-time measurement was part of this correctness diagnostic.
