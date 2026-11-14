# Offline test correction

The first offline suite ran 14 tests: 13 passed and one assertion failed in
`test_both_immediate_memory_endpoints`. The test increased a single candidate
row by 2000 bytes against the two-row baseline sum of 200000 bytes and expected
rejection. This is exactly 1%, which the protocol permits. The collector correctly
accepted the boundary. The test increase was corrected to 2001 bytes; collector
acceptance logic was unchanged. No benchmark, clocked harness invocation, fleet
access or performance observation occurred. The original failure was:

```text
FAIL: test_both_immediate_memory_endpoints
line 147: self.assertFalse(c.block_result(rr, False)['passed'])
AssertionError: True is not false
Ran 14 tests
FAILED (failures=1)
```
