# Validation record

Completed before timing, against both baseline and reconstructed EXP-004 A:

- `make decoder-check`: four Python test groups passed per binary.
- `make decoder-sanitize`: four groups passed per binary with ASan/UBSan.
- Each binary's self-test checked 1,820 fixture combinations: widths 0..64,
  both directions, seven counts, and zero/maximal valid score shift. Per-value
  exact finite bits and checksummed batches at rounds 0, 1 and 3 passed.
- Python checks covered CLI rejection, CSV shape, sample/count accounting,
  reachable offsets and crossings, checksum scaling, and the unavailable
  hardware-counter path on macOS. Successful Linux PMU reads were not tested.
- `python3 -m py_compile` passed for new build/run/analysis scripts and tests.
- `python3 scripts/check-workspace.py --pristine-source` passed.
- Generated `decoder_batch` assembly retained packed loads and loops in both
  variants; no direct calls occur inside the extracted functions.
- Staged whitespace checks passed before the harness commit.

This is a record of observed command results, not captured test stdout. Build
manifests retain compiler commands and their successful return codes. Original
whole-tree tests were not rerun for this diagnostic; production source is unchanged.

After timing, `audit.py` independently reconstructed the process statistics and
paired effects from raw CSVs, checked file hashes, serial scheduling, fixture
invariants, elapsed-time arithmetic and histogram sample totals. See
`local-m1/AUDIT.json`. This audit is not a second experimental run or an independent
reviewer's confirmation. No measured samples were removed or rerun.

Publication check caught CRLF histogram line endings from Python CSV defaults.
The analysis writer now emits LF and labels the ABBA roles explicitly. Derived
outputs were regenerated and audited; timing code, raw samples and effects are
unchanged. The initial whitespace check failure is retained here as an erratum.
