# Active mixed-width clone and relocation — validated

All48fixed source/build/seed/mode cells pass. Natural widening and every original
BOUNDARY-023 interval/anchor/model check remain. At the first mixed-width state,
cloning frees the original and continues its numeric cursor on the independent clone;
relocation moves all allocations or declines every third callback. No encoding change.

Each relocation pass visits exactly34955pre-enumerated allocations, including five
header/registry/index/rehash allocations and all pages. It completes32769public steps.
All-move releases34955old allocations; selective mode moves/releases23304and declines
11651. Exact owned-byte delta and rehash metadata hold at every step; full structures
and exact logical contents pass before/after. These are local operation counts, not
portable geometry, CPU time, memory savings or benchmark performance guards.

Both sanitizer faults detected: truncating wide clone allocation to narrow byte count
(new type) and dropping relocated destination assignment (repeat type). ASan's external
symbolizer emits warnings, retained; no retry or dependency/permission change. Raw
fault stderr remains in scratch, public copies replace workspace paths with a marker.
[Plan](PLAN.md), [manifest](manifest.json), [summary](summary.json), [faults](faults/manifest.json),
[oracle patch](oracle.patch). Original evidence unchanged; source NONE, performance
PARK unchanged.23suites/47distinctfaulttypes; sequential review only, model/cost unknown.
