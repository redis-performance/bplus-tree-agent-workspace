# DIAG-011 caller-context profiles

Descriptive interrupted-PC counts;not unbiased time shares or exact-cycle attribution.
All instrumented timing values excluded from source speed comparison.

- calibrate-0: controls=True;182 samples;{'known_arithmetic': 182}
- calibrate-1: controls=True;210 samples;{'known_arithmetic': 210}
- control-dynamic-m4: controls=True;81 samples;{'zbtreeIteratorNext': 74, 'traverse': 6, '__thread_selfusage': 1}
- A-dynamic-m4: controls=True;67 samples;{'traverse': 15, 'zbtreeIteratorNext': 52}
- control-fixed-m4: controls=True;107 samples;{'zbtreeIteratorNext': 98, 'traverse_fixed4': 8, '__thread_selfusage': 1}
- A-fixed-m4: controls=True;77 samples;{'zbtreeIteratorNext': 63, 'traverse_fixed4': 13, '__thread_selfusage': 1}
- control-dynamic-m6: controls=True;118 samples;{'zbtreeIteratorNext': 104, 'traverse': 13, '__thread_selfusage': 1}
- A-dynamic-m6: controls=True;134 samples;{'zbtreeIteratorNext': 126, 'traverse': 7, '__thread_selfusage': 1}
- control-fixed-m6: controls=True;132 samples;{'zbtreeIteratorNext': 120, 'traverse_fixed6': 11, '__thread_selfusage': 1}
- A-fixed-m6: controls=True;119 samples;{'zbtreeIteratorNext': 111, 'traverse_fixed6': 7, '__thread_selfusage': 1}
