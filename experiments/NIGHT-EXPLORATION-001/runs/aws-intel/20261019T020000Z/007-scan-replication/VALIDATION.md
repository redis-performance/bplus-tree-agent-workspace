# Intel validation before architecture comparison

All3 sources (baseline and exact A/B) pass original43 tests in native and ASan/UBSan builds. V2 all-match/page oracle passes native and sanitizer for all3, plus designated forced-portable builds for A/B in both modes. Full stdout/stderr and serial commands retained in validation-processes.json. No source or oracle changes. Exact B source hash matches independent submission204edc2c.

Baseline timing binary remains b598d273956f17e79480f0343eaaed5f9bd96170dfa36058b3d679e5f1adbdc2. A/B use unchanged Makefile, same relative frontend source/output paths and flags. candidate-freeze.json records all sources/referees and executables; screen-freeze.json seals schedule/driver/plan. Validation consumed52.75s serial CPU2, separate from timing cap. No timing rows yet.

Portable selectors test fallback compilation and semantics on Intel, not execution on another architecture or big-endian hardware. Other scan histories/performance guards remain pending.
