# BOUNDARY-012 — mixed mutations and changing iterator masks

Control and retained EXP-002 A/B/C all pass release/debug and ASan/UBSan. Four fixed
fixtures/build (sizes97/513,seeds8303/8311),1032 full model checks,2176436 iterator
results,10011 updates,4276 deletes and4276 inserts each. All8 masks vary per Next;
reverse parameters0,1,-1,2;copied iterator independent advancement and rank reseeks;
finite score extremes/signed zero/subnormals,empty/binary members and319/320/321 lengths.
Fresh iterators after every mutation honor documented invalidation;none used stale.

Two C faults detected:nonboolean-reverse guard and incorrect next-leaf position.
First fault-driver expected generic assertion phrase but actual adapter prints the
file/line/expression;original driver failure retained. Read-only audit confirms abort
at model assertion. Second distinct fault uses correct matcher;no first-fault rerun
or semantic weakening. See faults.json,faults-second.json,fault-review.json.

Twelfth boundary suite,24 boundary faults total;three HARNESS-004 referee sensitivity
faults counted separately. No baseline bug found. All sources/patch/commands/stdout/
stderr/hashes in manifest;uncommitted snapshots/root source preserved. Sequential
review only;actual backend/model/cost unknown. No performance/acceptance claim.
