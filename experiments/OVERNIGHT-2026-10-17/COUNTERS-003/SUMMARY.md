# Structural path census

No timing or hardware cost claim. All160 fixtures pass release/debug and sanitizers.
All structural fields identical across builds; native/ASan usable-size totals differ.
Original post-run equality assertion and all raw outputs retained;no rerun or changed test.

| Seed | Bytes | Encoding | Width: element count | Reversed | Cross-word |
|---|---|---|---|---|---|
| 7103 | 16 | integer | 6:44389, 7:55263, 8:267, 64:81 | 0 | 0 |
| 7103 | 320 | integer | 6:44389, 7:55263, 8:267, 64:81 | 0 | 0 |
| 7103 | 16 | fraction | 6:44339, 7:54290, 8:50, 9:973, 10:267, 64:81 | 0 | 0 |
| 7103 | 320 | fraction | 6:44339, 7:54290, 8:50, 9:973, 10:267, 64:81 | 0 | 0 |
| 7103 | 16 | wide | 6:44916, 7:55084 | 0 | 0 |
| 7103 | 320 | wide | 6:44916, 7:55084 | 0 | 0 |
| 7103 | 16 | zero | 6:44760, 7:55018, 8:151, 63:71 | 0 | 54 |
| 7103 | 320 | zero | 6:44760, 7:55018, 8:151, 63:71 | 0 | 54 |
| 11213 | 16 | integer | 6:42924, 7:56682, 8:262, 9:80, 64:52 | 0 | 0 |
| 11213 | 320 | integer | 6:42924, 7:56682, 8:262, 9:80, 64:52 | 0 | 0 |
| 11213 | 16 | fraction | 6:42771, 7:55712, 8:153, 9:970, 10:262, 11:80, 64:52 | 0 | 0 |
| 11213 | 320 | fraction | 6:42771, 7:55712, 8:153, 9:970, 10:262, 11:80, 64:52 | 0 | 0 |
| 11213 | 16 | wide | 6:43271, 7:56729 | 0 | 0 |
| 11213 | 320 | wide | 6:43271, 7:56729 | 0 | 0 |
| 11213 | 16 | zero | 6:43099, 7:56750, 8:76, 63:75 | 0 | 56 |
| 11213 | 320 | zero | 6:43099, 7:56750, 8:76, 63:75 | 0 | 56 |

Coverage hypothesis supported in all four preregistered integer cells.
This does not establish the decoder as dominant or justify removing width64 support.
