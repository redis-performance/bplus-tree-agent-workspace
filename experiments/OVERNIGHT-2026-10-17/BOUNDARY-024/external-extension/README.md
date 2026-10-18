# External score moves during live mixed-width SCAN

All16fixed source/build/seed cells pass (control/EXP-004A/B/C, nativeO3/debug and
O1ASan/UBSan/debug, seeds71503/71509). Every260score update checks the same external
allocation before/after;258move to a different leaf. All3123external buffers have
unique ownership at structural checkpoints. Full current-score models, exact binary
values, live SCAN intervals/anchors, termination and usable-byte accounting pass.
Six full sorted models per cell; sampled rank/seek checks are not exhaustive ranks.

Public construction reaches widening at396329members locally, with395929continuous
initial anchors. Actual cross-leaf classes are256old-source/copied-target,1copied/
uncopied-target and1copied/copied. All2159mixed-width SCAN calls pass; the original
cursor completes within16384groups. Cardinalities are observations, not assumptions.
Two signed-zero updates keep exact bits. External lengths320/321/1024/4097 were fixed
before insertion; all other members remain319bytes. No key changes length mid-fixture.

The omitted-external-detach fault is detected by a production assertion in its
successfully built sanitizer binary. No prior oracle or production source changed.
The [execution capture](../../COUNTERS-010/README.md) distinguishes259actual detach/
reinsert operations and1in-place update from260pointer-preservation checks. The
original object is freed before a final clone model/scan; sanitizer checks pass.

See PLAN.md, run.py, manifest.json, summary.json, oracle.patch and faults/ for exact
frozen provenance, commands, raw outputs/hashes and sensitivity patch. SourceNONE;
optimizationPARK unchanged. This is an extension, not an additional suite count.
