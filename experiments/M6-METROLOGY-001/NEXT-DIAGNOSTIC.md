# Future design: bound clock attribution before interpreting residuals

Proposed, unimplemented, unexecuted; no benchmark or runner lease queued. This is a
measurement-validity diagnostic, not a source proposal, baseline retry, or optimization
acceptance path. The 105.605µs target below is explicitly derived from completed data
for planning a new investigation; it never changes or requalifies EXP-009.

One falsifiable question: can a new interval estimator detect a controlled blocking
perturbation while bounding its boundary/accounting uncertainty below the smallest
observed failed thread-contrast margin? Success validates only that estimator on its
control workloads. It proves neither the old cause nor stable tree measurements.

Candidate bracketing, with CPU/QoS metadata outside the entire bracket:

    w0, t0, w1; fixed body; w2, t1, w3

Define inner wall I=w2−w1, thread T=t1−t0, margins M=(w1−w0)+(w3−w2).
Under explicitly validated interval-accounting/error assumptions, extra boundary CPU
lies in[0,M]; inner off-CPU lies in[I−T,I−T+M] intersect[0,I]. Unknown clock error must
widen that interval. Long pauses in margins widen bounds; they are retained, not excluded.
For ABBA, propagate every per-row interval to paired-sum contrast bounds before testing
any sufficient explanation. Empty intervals flag an accounting-model failure.

Necessary controls for a future preregistration: declared nominal clock resolution;
empty brackets; deterministic CPU-work with exact checksum; separately bracketed
controlled blocking with all interruptions/overshoots retained; fixed order/counts,
wall budget, complete raw journals and no retries. clock_getres and empty-bracket
samples alone cannot establish worst-case accuracy/accounting lag. The error model
must be made concrete and independently reviewed before choosing a numerical pass gate.

All native commands, counts, budgets and error gates still require that new frozen
plan; none is implied here. Keep harness changes in a separate referee commit. A later
tree comparison needs fresh profiles and qualified wall A/A, three independent proposals,
three isolated implementations, serial ABBA, full guards, fresh independent confirmation
and adversarial review. Never borrow precision from this control or another host.
