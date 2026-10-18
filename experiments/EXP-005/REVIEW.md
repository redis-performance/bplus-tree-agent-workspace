# Adversarial review — sequential coordinator

No independent reviewer ran;startupfailed. This is a separate final inspection of
semantics,ownership/UB,teststrength,measurementvalidity and maintainability.

Semantics: all three masks are equivalent for valid widths1..64,with width0 excluded by
unchanged guard. A shift count0..63;B unsigned64 multiplicationwrap at64 is defined;
C unsignednegation/mod64 gives the same lowones mask. Original cross-word conditional
load and shift remain. Layout/memberordering/scorebits/signedzeros/indexIDmaintenance
are untouched. Exhaustive scalar reader and real mutation tests cover fullwidth,
crossword,narrowwidth,physicalreversal and zerostoggles. No NaN input assumption.

Teststrength: all1096commands pass originaltests,modeoracles,mutation012,bitstream013,
zero014 in bothbuilds. Zero014 detects two planned faults independently. Its initial
rehash memory-precondition failure is retained and explicitly settled before equality,
not misreported as a librarybug. Existing checks unchanged.

Measurement: baseline profiles precede proposals; freshAA009 qualifies only0/4/7.
Every discovery/fresh row preserved;3ABBAblocks and freshseeds predeclared. Unqualified
2/6 never authorize acceptance. C freshprimary misses required interval;PARK correct.
A/C matching hotinstructions make claimed C intrinsic superiority especially suspect.
All local measured windows serial; root source/referee untouched. Independent review,
frequency/residency knowledge,broaderguards and committedprovenance remain missing.

Maintainability: A is clearer than C's modularnegative arithmetic; B wrap requires
explanation. No winning evidence justifies any code change. Keep small patches for
morning review; do not ship them based on instructioncount or screening alone.
