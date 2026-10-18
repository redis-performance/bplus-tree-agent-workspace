# PROFILE-003 descriptive interrupted-PC counts

No speedup or unbiased time fraction implied. Timed regions contain sampler overhead;
Thread endpoint precedes dump, but sampler boundary syscalls remain in the interval.
Requested intervals may be rounded/coalesced; boundary sampler instructions can be captured.

| Capture | Samples | Unknown | >=30 | Top sampled symbols (counts) |
|---|---:|---:|---|---|
| 3407-1000-scan-16 | 1302 | 0 | True | zbtIndexScanSlot: 1178; siphash: 59; zbtIndexScanGroup: 51; scan_count: 10 |
| 3407-1000-scan-320 | 890 | 0 | True | zbtIndexScanSlot: 841; zbtIndexScanGroup: 46; scan_count: 3 |
| 3407-1000-iterate-16 | 75 | 0 | True | zbtreeIteratorNext: 64; main: 11 |
| 3407-3001-scan-16 | 996 | 0 | True | zbtIndexScanSlot: 892; siphash: 50; zbtIndexScanGroup: 46; scan_count: 6 |
| 3407-3001-scan-320 | 768 | 0 | True | zbtIndexScanSlot: 719; zbtIndexScanGroup: 44; scan_count: 4; zbtreeScan: 1 |
| 3407-3001-iterate-16 | 64 | 0 | True | zbtreeIteratorNext: 57; main: 7 |
| 3803-1000-scan-16 | 1388 | 0 | True | zbtIndexScanSlot: 1265; zbtIndexScanGroup: 65; siphash: 50; scan_count: 5 |
| 3803-1000-scan-320 | 1223 | 0 | True | zbtIndexScanSlot: 1163; zbtIndexScanGroup: 54; scan_count: 5; zbtreeScan: 1 |
| 3803-1000-iterate-16 | 86 | 0 | True | zbtreeIteratorNext: 77; main: 9 |
| 3803-3001-scan-16 | 1003 | 0 | True | zbtIndexScanSlot: 917; siphash: 42; zbtIndexScanGroup: 34; scan_count: 6 |
| 3803-3001-scan-320 | 1024 | 0 | True | zbtIndexScanSlot: 974; zbtIndexScanGroup: 42; scan_count: 6; zbtreeScan: 2 |
| 3803-3001-iterate-16 | 73 | 0 | True | zbtreeIteratorNext: 57; main: 16 |
