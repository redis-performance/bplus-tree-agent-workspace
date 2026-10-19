# Preparation validation

No overnight campaign was started as part of preparation. No tree optimization was
implemented or accepted. The baseline extension was run separately with user authorization.

- `python3 tests/test_overnight.py -v`: six tests passed in 47.902 seconds. Tests use
  a fake local worker, not a model. Coverage includes deadline cleanup of descendants
  in separate sessions, preserving an unrelated process, STOP interruption, continuation
  and actual usage capture, exclusive lock, custom prompt/host-specific blocker (ignoring
  the old campaign's blocker), and rejection of an outside-repository evidence path.
- `python3 -m py_compile scripts/run-size-matrix.py scripts/analyse-size-matrix.py`: passed.
- Legacy analysis executed against a temporary copy of the old manifest and a read-only
  link to its raw directory: 96 runs / 768 rows / 32 cells reconstructed. Historical
  checked-in summaries were not regenerated or overwritten.
- Five-size M1 release and sanitizer checks plus analysis: [run manifest](../SIZE-MATRIX-001/apple-m1-five-sizes/manifest.json)
  and [results](../SIZE-MATRIX-001/apple-m1-five-sizes/SUMMARY.md). All 120 runs / 960 rows /
  40 cells reconstructed, native/sanitizer upstream tests passed (43 each), sanitizer
  benchmark checks passed at every size.
- Local documentation links and staged whitespace checked; both charts visually reviewed.
- Blog/cbitset/template review is source inspection, not execution of their benchmarks.

The supervisor was not exercised with a real model on M6. Launch preflight must verify
that host's CLI/toolchain/permissions. The shared plan does not promise identical noise
or results across machines. Host names are labels; actual hardware is recorded at run time.
