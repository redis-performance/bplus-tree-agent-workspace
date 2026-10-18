# Expanded iterator guard profiles

Descriptive interrupted-PC counts;not unbiased time shares or exact-cycle attribution.
All instrumented timing values excluded from source speed comparison.

- calibrate-0: controls=True;215 samples;{'known_arithmetic': 215}
- calibrate-1: controls=True;219 samples;{'known_arithmetic': 219}
- control-m0: controls=True;46 samples;{'zbtreeIteratorNext': 38, 'traverse': 7, 'mach_timebase_info': 1}
- A-m0: controls=True;55 samples;{'zbtreeIteratorNext': 50, 'traverse': 4, '__thread_selfusage': 1}
- B-m0: controls=True;62 samples;{'zbtreeIteratorNext': 15, 'zbtIteratorGeneric': 40, 'traverse': 6, '__thread_selfusage': 1}
- C-m0: controls=True;60 samples;{'zbtIteratorGeneric': 45, 'zbtreeIteratorNext': 10, 'traverse': 4, '__thread_selfusage': 1}
- control-m7: controls=True;103 samples;{'zbtreeIteratorNext': 85, 'traverse': 17, '__thread_selfusage': 1}
- A-m7: controls=True;139 samples;{'zbtreeIteratorNext': 118, 'traverse': 20, '__thread_selfusage': 1}
- B-m7: controls=True;109 samples;{'zbtIteratorGeneric': 83, 'zbtreeIteratorNext': 11, 'traverse': 14, '__thread_selfusage': 1}
- C-m7: controls=True;140 samples;{'zbtIteratorGeneric': 117, 'zbtreeIteratorNext': 7, 'traverse': 16}
