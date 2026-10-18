# Fixed fault controls after baseline passes

Two isolated ASan/UBSan/debug snapshots, one <=120s run each; no oracle changes after
outcomes. Keep root source pristine and preserve all outputs, including undetected faults.

- Omit zbtIndexRebuild after the large rank-delete loop. Expect stale index/leaf-ID
  invariant or model failure; active-resize ownership must not survive this path.
- Clamp an oversized rank endpoint to length-2 instead of length-1. Expect the
  full-range ULONG_MAX deletion count/survivor oracle to detect the endpoint loss.

These are semantic sensitivity controls, not performance/source candidates.
