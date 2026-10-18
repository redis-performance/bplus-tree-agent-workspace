# AA-010 — wall-time precision

Fixed six-block A/A; all384 rows retained. 95%t intervals assume independent normal block effects.
Frequency/effective QoS/within-window placement unknown. No source speed claim.

| Cell | Seed | Rows | B/A mean % [95% interval] | Qualified |
|---|---:|---:|---|---|
| int-asc-f4 | 31031 | 24 | -0.164 [-0.693,+0.364] | True |
| int-asc-f4 | 31043 | 24 | -0.704 [-2.159,+0.750] | False |
| int-desc-f4 | 31031 | 24 | +0.103 [-0.082,+0.288] | True |
| int-desc-f4 | 31043 | 24 | -0.346 [-1.173,+0.481] | False |
| int-desc-r4 | 31031 | 24 | +0.131 [-0.110,+0.372] | True |
| int-desc-r4 | 31043 | 24 | +0.017 [-0.415,+0.449] | True |
| zero-asc-f4 | 31031 | 24 | -0.112 [-0.265,+0.042] | True |
| zero-asc-f4 | 31043 | 24 | -0.271 [-0.626,+0.083] | True |
| zero-desc-f4 | 31031 | 24 | +0.052 [-0.277,+0.382] | True |
| zero-desc-f4 | 31043 | 24 | +0.005 [-0.280,+0.289] | True |
| zero-desc-r4 | 31031 | 24 | -0.012 [-0.526,+0.502] | True |
| zero-desc-r4 | 31043 | 24 | +0.094 [-0.275,+0.463] | True |
| zero-desc-f6 | 31031 | 24 | +0.089 [-0.153,+0.330] | True |
| zero-desc-f6 | 31043 | 24 | +0.039 [-0.256,+0.334] | True |
| zero-desc-f7 | 31031 | 24 | -0.185 [-0.456,+0.086] | True |
| zero-desc-f7 | 31043 | 24 | +0.037 [-0.147,+0.221] | True |

Both-seed eligible cells: int-desc-r4, zero-asc-f4, zero-desc-f4, zero-desc-r4, zero-desc-f6, zero-desc-f7
