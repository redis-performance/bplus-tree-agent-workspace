# Corrected-adapter M6 baseline — preregistered

This requalifies the original five-size/eight-operation inventory after the
standalone panic contract correction. It measures a new adapter identity and does
not count as a tree optimization or acceptance. The original baseline and every
prior candidate comparison remain preserved under their frozen original adapter.
[Plan](PLAN.json), [adapter review](../010-assertion-contract-review/README.md),
[independent adversarial review](../010-assertion-contract-review/ADVERSARIAL-A.md).

Source C/header, benchmark loop, hashing, allocator and assertion evaluation remain
unchanged. `_Noreturn` conveys the existing unconditional abort. New baseline rows
must not be pooled with old-adapter rows. `--build` only selects an isolated binary
directory so historical binaries are preserved. No failed schedule is repeated.

Completed:120 processes/960 rows; five qualifying cells and14 short cells.
[Results](RESULTS.md) and [independent audit](INDEPENDENT-AUDIT.md).
