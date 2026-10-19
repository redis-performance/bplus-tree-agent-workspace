# Five-size extension: include one million members

User explicitly requested 100/1K/10K/100K/1M, all eight operations. Preserve the
original four-size evidence at apple-m1/. New output: apple-m1-five-sizes/.

Same source, benchmark, compiler flags, seeds, six same-binary ABBA blocks, one
million requested operations and 16-byte members as PLAN.md. Only the size list
and timing cap change: 120 processes, 960 rows, 40 cells; 600-second timing budget.
At 1M, insertion/deletion each visit 1M members, reads/updates request 1M, and
iteration/scan do full passes. This gives fewer repeat passes at larger sizes;
record actual denominators and do not claim equal cache histories.

Native and ASan/UBSan upstream tests, then sanitizer all-operation checks at every
size with 2N+1 requests and seed101. Validate raw hashes, counts, checksum agreement,
complete size/case matrix and source identity. No retries for better numbers.

The runner records the size list in its manifest. Analysis remains compatible with
historical four-size manifests (which omit that field). New runs default to five
sizes; the old four-size plan/results remain historical and unchanged.

Reproduce:

```sh
python3 scripts/run-size-matrix.py --out experiments/SIZE-MATRIX-001/apple-m1-five-sizes --budget-seconds 600
python3 scripts/analyse-size-matrix.py experiments/SIZE-MATRIX-001/apple-m1-five-sizes
```

On M6 use a new host-specific directory with the same arguments. No M6 measurements
are claimed in this preparation. All measurement limits in PLAN.md still apply.
