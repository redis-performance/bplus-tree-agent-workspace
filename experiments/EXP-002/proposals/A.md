# Sequential proposal pass A — narrow iterator dispatch

Participant: coordinator pass A, not an independent agent. Backend/model/cost unknown.
Shared context: HARNESS-003 freeze, PROFILE-003 all captures, AA-005 all rows, source pin.
Bottleneck: score-only forward iteration samples concentrate in zbtreeIteratorNext.
Baseline arm64 disassembly saves six register pairs before testing optional member
outputs; the qualified loop never requests those outputs. Inference: generic optional
member handling may impose avoidable register/dispatch work on this common path.

One falsifiable hypothesis: isolating forward score-only iteration from the generic
optional-output/reverse path reduces wall ns/visit by>=2%, with no>1% long-member
regression and no tree-owned byte increase. Target only zbtreeIteratorNext and local
helpers. Reuse existing score decoder, retain generic fallback unchanged.
Risks: iterator final position at leaf/end, reversed physical leaf encoding, NULL score,
reverse direction and optional outputs. Full original tests and lexical output-mask
oracle plus score-boundary oracle must pass both builds. No iterator struct/API change.
Prediction: short/long forward score-only gain similarly; other paths need performance
confirmation before broad claim. Falsify if measured threshold fails, new prologue remains,
or profile/codegen fails to support reduced dispatch/register work.
