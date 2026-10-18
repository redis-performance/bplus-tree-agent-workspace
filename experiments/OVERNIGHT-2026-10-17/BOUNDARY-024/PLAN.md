# BOUNDARY-024 — score moves during live mixed-width SCAN

Preregistered round17 correctness experiment; no performance claim. Keep root source
and referee unchanged. Control and retained EXP-004 A/B/C use exact freeze.json
snapshots, unchanged allocator, native O3/debug and O1 ASan/UBSan/debug. Seeds70501,
70507; fixed16cells, serial120s-bounded children, total900s budget. Stop on failure;
retain failed recipe before revising. Independent reviewer startup failed; sequential
review only. All commands, UTC boundaries, binary/source/raw hashes and patches saved.

Reuse BOUNDARY-023's public natural construction with319-byte binary keys and at
most850000members. Start one live hint1 SCAN cursor before widening. Append16members
between calls only until mixed-width migration is observed. Then stop appending:
score changes that exceed the old maximum would invalidate append's precondition.
All initial members remain continuously present. Existing interval/anchor/termination,
exact callback bytes/length/current-score bits, SCAN nonmutation, structural invariants
and exact usable-byte accounting checks remain unconditional. Independent hash-order
interval model is immutable; independent current-score vector changes after each
successful UpdateScore. Numeric score then binary member order defines sorted model;
zero equality is numeric for order and exact-bit for value. No NaN inputs.

At first active state move initial IDs1 and2 into the middle with unique fractional
scores; require observed migrated source and initially unmigrated destination leaf.
Over128successive active scan gaps move two distinct middle IDs per gap to new global
min/max scores, requiring observed old-table sources and copied target leaves on at
least one actual cross-leaf update. Use fresh successful FindForAdd immediately before
UpdateScore. Record source/destination IDs and migration markers before/after the
public call; iterator score seeks are read-only. Toggle ID0 to negative and positive
zero in the first two gaps, checking both exact results. Check full independent sorted
models at first active boundary, after128gaps and after migration; sampled rank seeks
are read-only during active state. No full lookup pass may drain active migration.

After the128mutation gaps, advance migration with16ordinary successful score lookups
between SCAN calls until complete; require completion and both actual cross-ownership
cases before cursor termination. Check all initial anchors. Then full lookup/rank/
ordered models and static scans hints0/256/ULONG_MAX, duplicate/free-original, model
and clone scan. Hash intervals permit duplicate callbacks. No private state mutation.

Two isolated ASan/UBSan fault controls, built after baseline passes: omit old-to-new
entry insertion in zbtIndexMove; suppress the packed-score update in the in-place
path (including signed zero). Successful compilation and observed oracle, production
assertion or sanitizer failure detect a fault; survivors/timeout are not detections.
Do not weaken any existing test. Public observations are local geometry, not portable
constants. Selection NONE and existing optimization PARK decisions remain unchanged.
