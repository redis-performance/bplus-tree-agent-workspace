# Adversarial review — sequential self-review only

No independent agent or other reviewer ran. This pass checks claims against
the frozen plan and raw reconstruction; it cannot satisfy an independence gate.

- The A/A windows are 0.011 ms at minimum and 0.161–0.180 ms at the two
  count-one primaries, versus the required 10 ms. Zero of 70 cells qualifies.
  The fixed schedule is unsuitable for the strict acceptance gate; do not
  relabel the repeated exploratory effects as a confirmed speedup.
- Count-one fixture deltas are invariant across seed literals. Six blocks are
  repeated measurements of this input shape, not six independently diverse
  input distributions.
- B/C inline the policy into `decoder_batch`; A/base keep it outlined. Large
  losses where the bulk path is nominally unchanged show that code layout and
  compiler decisions matter. The result does not isolate decoder arithmetic.
- The first two population steps were three sequential passes each by one
  worker, not independent agents. All source snapshots are isolated in scratch
  and patches are retained, but Git commit provenance is pending the recorded
  index-lock denial.
- A/A, candidate, release and sanitizer binaries used the same source inputs
  within their respective phases. The 1,040 focused validation cells and the
  1,820-fixture self-tests cover finite score bits, signed zeros, widths 0..64,
  both orientations and partial/empty ranges. They do not validate public
  iterator integration, because no such integration was implemented.
- System sampling on current binaries failed with return code 255. Previous
  EXP-008 whole-process samples and current assembly are mechanism clues only.
  No cycle, core-frequency or timed-only profile claim is made.
- No candidate passes the frozen guard and precision gates. Fresh confirmation
  and another-machine replication are correctly NOT RUN. The disposition is
  PARK/source NONE, and it leaves the original scalar iterator unchanged.
