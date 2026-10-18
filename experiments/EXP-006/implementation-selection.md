# Implementation decision — C/PARK, source adoption NONE

Both population stages completed as separate sequential coordinator passes, not
independent agents. Three proposals/chair chose one hypothesis; three isolated
implementations share freeze.json and exact referee/flags/allocator. No source adopted.

All four sources pass native/ASan original43tests, raw-buffer guard pages,
1,585,152exact tag-first-match checks/build and36batch fixture cells/build. Added
protected-page validation passes198,144tag checks/build/source; its intentional
bounded-read violation is detected. Root source and all candidate patches are retained.

360screening rows (3ABBA blocks,2seeds,5cells,3variants) retain every observation.
Abyte scan regresses the qualified primary and long-key guard; rejectA. B8-byte scan
shows primary gains but does not pass declared bounds; retainB/PARK. C16-byte scan
has the best exploratory mean; no candidate passes both screening gates. The fixed
selection rule sendsC to fresh confirmation for falsification, not as a passing winner.

96fresh rows (6ABBA blocks,2new seeds,primary+qualifiedguard) pass all count/hash/memory
checks. Cprimary95%t intervals are[-4.8285,-2.7300]% and[-7.2805,-4.1181]% candidate
wall-time change, below the preregistered-2%upper bound. Long-hit guard intervals are
[-8.6891,+1.8067]% and[-2.8280,-1.2868]%; the first fails the<=+1%upper bound.
The large first-block contrast remains in full. No row removed, threshold changed,
or confirmation extended. See bench-results/{screen,confirm}/summary.json for raw-derived
per-block effects, per-member rates, exact owned bytes and separate thread intervals.

The unqualified single-lane hit guard also shows a concerning screening regression:
Cintervals[+4.063,+7.037]% and[+3.036,+6.266]%. Its A/A qualification failed, so it
cannot supply an accepted guard result, but it is evidence against treatingC as broadly
safe. Revisit this guard on a qualified runner before considering source adoption.
Short-hit/miss guards and original campaign guards remain unresolved. Fresh confirmation
only covers the two predeclared qualified cells; it does not erase other observations.

Matched8candidate+8baseline captures and four calibrationcontrols pass. Baseline
memchr attribution disappears forC; work moves into zbtScoreLeafFindMember, while
SipHash still leads long-key captures. All three assembly variants remove the leaf's
memchr call. This supports the code transformation, not a claim of unbiased time-share
reduction, frequency control, or a complete explanation of guard behavior. No PMU data.

Decision: **C/PARK** as an experimental preference; **source selection NONE**.
A is rejected; B/C patches retained. No ACCEPT with unresolved guard precision,
possible single-lane regression, independent confirmation/review, committed provenance
or architecture coverage. A new preregistered guard diagnostic/qualified runner is needed;
do not rerun the identical schedule or discard its unusual blocks.

Local M1arm64, one unpinned thread, Apple Clang17C11O3-g-Wall-Wextra-Werror
-fno-omit-frame-pointer-DREDIS_DEBUG, unchanged allocator/hash. Frequency/effective QoS/
within-window migration unknown. CPU MCP checker consulted before numeric reporting;
missing frequency means no portable rate claim. Backend/model/token cost unknown;
supervisor records actual CLI usage. All evidence remains local pending morning review.
