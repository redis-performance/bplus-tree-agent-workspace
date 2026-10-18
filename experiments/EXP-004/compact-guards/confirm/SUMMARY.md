# EXP-004 compact guards — confirm

Wall ns/item paired effects; negative is faster.95%t df2 assumes independent normal blocks.
All guards share effective counts,exact checksums,construction fingerprints and tree bytes.
No primary substitution,headline speed claim or independent confirmation.

| Variant | Cell | Seed | Effect% [95%CI] | Guard pass |
|---|---|---:|---|---|
| A | zero-trim-f4 | 41051 | -2.110 [-3.795,-0.425] | True |
| A | zero-trim-f4 | 41063 | -2.518 [-3.457,-1.580] | True |
| B | zero-trim-f4 | 41051 | -0.927 [-1.845,-0.008] | True |
| B | zero-trim-f4 | 41063 | -0.666 [-0.865,-0.466] | True |
| C | zero-trim-f4 | 41051 | -0.328 [-2.249,+1.592] | False |
| C | zero-trim-f4 | 41063 | -0.403 [-1.319,+0.513] | True |

```json
[
  {
    "variant": "A",
    "both_seed_failures": [],
    "both_seed_passes": [
      "zero-trim-f4"
    ],
    "status": "PARK"
  },
  {
    "variant": "B",
    "both_seed_failures": [],
    "both_seed_passes": [
      "zero-trim-f4"
    ],
    "status": "PARK"
  },
  {
    "variant": "C",
    "both_seed_failures": [],
    "both_seed_passes": [],
    "status": "PARK"
  }
]
```
