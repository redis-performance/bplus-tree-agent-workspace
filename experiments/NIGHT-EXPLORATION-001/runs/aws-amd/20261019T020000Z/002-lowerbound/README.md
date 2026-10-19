# AMD LOWERBOUND-001 preparation

Target: existing +N distant-update workload at100K and1Mmembers,16-byte binary keys. Profile supports examining lower-bound member decoding. No population selection or candidate yet. Freeze baseline8fab511e, target C SHA256d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2; root referee unchanged.

Calibration: three100K-operation observations per primary, choose ceil(50ms / fastest ns/op), cap100M. A/A: six ABBA blocks,seeds1/2/3twice; rotate size order. Qualification requires every effect within±1% and every window≥10ms. One fixed exploratory screen allowed if unqualified, no repeated retry. Strict adoption requires≥2% both primary every fresh block and no>1% full guard/memory regression; all-eight-operation size guards and independent confirmation/review remain necessary. No source adoption overnight.
