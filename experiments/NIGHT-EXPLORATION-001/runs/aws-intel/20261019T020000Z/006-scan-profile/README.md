# Intel baseline scan profile — helper materially present

Six preregistered scoped captures completed on baseline8fab511e:100K/1M members,16-byte members,seeds1/2/3 and5M requested operations. No candidate timing, new implementation population, A/A retry or source selection. Intel measured-population totals stay2 (0 accepted/1 rejected/1 parked).

| Size | Captured samples | TagMatches inline samples | Helper share | ScanSlot inclusive share |
|---|---:|---:|---:|---:|
| 100000 | 131 | 36 | 27.48% | 86.26% |
| 1000000 | 174 | 42 | 24.14% | 90.23% |

Both sizes meet the preregistered descriptive signal of at least10 helper-attributed samples and5% of captured samples. This establishes a relevant Intel target for possible later replication; it does not predict SIMD improvement or qualify a benchmark. AMD timing effects and Intel profiles must remain separate.

Scope is original scan loops plus small timer/control edges, excluding setup, warmup and postvalidation. Original duplicate-emission/count semantics, callbacks and complete validation remain intact; actual operations can exceed requested operations. Same baseline target source, compiler/flags/assertions/hash and allocator as the Intel campaign. No-pg function instrumentation; process-only profil timer interval10ms,scale65536,2-byte16-bit bins. The denominator is captured executable-range samples, excluding libraries/outside-range/lost samples; missed-event counts are unavailable. Nested inline scopes overlap and must not be added.

GNU addr2line reported no separate TagMatches inline function frame while mapping15/12 samples directly to its source lines4129–4153. LLVM18 recovered full inline frames for the same PCs, yielding36/42 helper samples including nested inline work. Both maps and the preliminary GNU audit are retained. The direct source-line subset alone is11.45%/6.90%; shared TagMask lines were not blindly added. LLVM mapping is the final reported attribution. PC buckets/source boundaries are approximate and per-capture counts are small. No adaptive capture extension followed this mapping check.

Controls: enabled known-work66/66 captured samples in known_work; disabled known-work and scoped-disabled scan controls zero. Original versus scoped-disabled native semantic fields and owned bytes match at100/1K/10K. Matching original/scoped-disabled sanitizer semantic fields and owned bytes match at1K. First attempt incorrectly compared native32544 owned bytes with sanitizer32446 and stopped before enabled scan captures; all semantic fields matched. That failed precondition and its original script/output are retained in attempt001 and CONTROL-ERRATUM.md. No cross-mode equality is claimed. The valid correction adds an original sanitizer control, preserving every matched-mode assertion.

Total bounded helper runtime17.571s: first attempt8.128s, continuation9.329s, metadata-only LLVM remapping0.114s. Initial cap300s; after the first stop continuation was limited291s, and remapping used30s from the remaining282.543s. Aggregate actual work remained under the original300s ceiling. No capture was repeated or discarded. Fifteen serial benchmark/control process windows, exact raw rows, sampler overflow checks and source/referee hashes pass audit-profile.py.

Artifacts: PLAN.md and source-manifest.json pin the target/referee; build-sha256.txt pins executables; profiles contains raw CSV rows/histograms/metadata; processes.json records command boundaries; inline-map.txt and llvm-inline-map.json retain both symbolizers; scan-slot-assembly.txt preserves actual codegen; profile-audit.json records the final counts. Sampler source is identical to the validated iterator sampler. Public paths are normalized and objdump copies trim trailing whitespace; private remote originals remain intact.

Execution was through the leased remote helper, CPU2, scripts scan-diagnostic.sh then scan-diagnostic-resume.sh, followed by metadata-only scan-symbolize.sh. The first driver version is attempt001/run-diagnostic.py; current run-diagnostic.py is the continuation version that loads preserved control records. To reconstruct the historical sequence from a clean directory, restore the attempt001 driver for the first script, then restore the current continuation driver for the second; do not silently run the continuation without its retained controls. No permission/governor/PMU changes.

Next: await AMD’s fixed comparison and root decision before any Intel candidate timing. A new architecture comparison would require its own frozen schedule, baseline A/A and exact candidate identity; these profiles alone authorize no winner.
