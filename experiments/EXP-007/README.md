# EXP-007: per-leaf bulk decoder specialization

Status: prepared for the fixed local comparison. Source adoption NONE. This tests
a private bulk helper, not the public scalar iterator. Two genuine independent
three-agent populations completed proposal and implementation steps; exact model
and per-agent token/currency cost unavailable. See [selection](selection.md) for
the chair's choice and preserved dissent.

Three implementations share the original source commit4fd3a3fd and the reference
range helper: A caches noncrossing metadata; B adds a byte-aligned loop; C is the
minimal width-class split. Isolated detached source worktrees and build directories
keep sources separate. Root production files are unchanged.

The common referee was committed as fd1f96c5 before timing. It materializes output
for every variant, then applies the same four checksum chains. An explicit compiler
barrier retains output writes/reads. Absolute timings differ in scope from EXP-004's
direct-checksum kernel. See [plan](PLAN.md) for primary, guards, budgets, shortlist
and fresh-seed confirmation. No candidate may be retuned after discovery.

Validation: four Python groups passed for each of baseline/A/B/C in release and
ASan/UBSan (eight suites). Each checks1820 width/direction/count/shift fixtures,
selected partial/empty ranges, exact bits, canaries and batch checksums. Additional
272 commands cover all variants/builds with eight leaves and explicit signed-zero,
subnormal and extreme finite bases. An initial validation invocation used unsupported
warmup0 and exited2; retained separately, corrected to documented warmup1 before
rerunning the fixed matrix. No semantic assertion was weakened.

Baseline external sampling succeeded on the actual release binary:841 top frames
in decoder_batch. It samples the whole process, including warm-up, not a timed-only
region or CPU cycles. The shared output/checksum overhead is part of the measured
bulk operation. Assembly and matched sampling are descriptive evidence only.

Run from repository root:

```sh
python3 experiments/EXP-007/build.py
python3 experiments/EXP-007/build.py --sanitize
python3 tests/test_decoder.py build/exp007/base/decoder-bench
python3 experiments/EXP-007/validate-boundaries.py
python3 experiments/EXP-007/run.py --out scratch/exp007-new
python3 experiments/EXP-007/analyse.py scratch/exp007-new
```

All compiler flags, source/referee/binary hashes and successful validation outputs
are in [validation](validation/) and [freeze.json](freeze.json). Actual Linux/big-endian
execution, hardware counters, frequency/QoS controls and scalar integration are absent.
The local user-authorized campaign does not restart overnight experimentation.
