# Validation cardinality correction before timing

PLAN.md's explicit matrix has2callers*3masks*2directions*4encodings*2member-lengths
=96fixture processes per source/build,384total,not192/768 as its prose states. The
running validation script's progress label repeats that arithmetic mistake. Keep the
original plan/driver evidence;all explicitly listed fixtures run,none removed. There
are384fixture runs plus4build commands=388manifest rows. This correction is recorded
before any DIAG-011 timing;no threshold,fixture or oracle changed.
