# HARNESS-004 — iterator direction/output/encoding referee

Separate frozen additive iterator_modes.c, reusing HARNESS-003 timing/CPU-ID/requested
QoS primitives by including its unchanged microbench.c under a renamed legacy main.
Root referee/source untouched. Snapshot/provenance/hashes in freeze.json; git denial
from round1 not retried. Base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus uncommitted
snapshot; commit-based acceptance pending morning review.

Release and ASan/UBSan each pass original43 tests and640 fixture cells: sizes1,31,32,
33,129;16/320 byte binary keys;integer/fraction/wide/signed-zero scores;both directions;
all8 output masks. Each requests2n+1 and verifies3n effective items/3 full traversals.
Before/after independent ordered oracle checks exact score bits and full member bytes;
copying iterator state to inspect the next item checks masks without visible outputs.
Repeated exhaustion preserves output sentinels. Tree-owned memory unchanged.
Three isolated semantic faults (wrong length,score,reverse state) detected. Faults are
referee sensitivity controls, not new boundary-suite counts. All logs retained.

Timed checksum consumes each requested output (member first byte,length,score bits),
plus exact visited count; full byte/order checking outside timing. Modulo uint64 sums
are defined; expected sums come from fixture formula, not candidate outputs. Timed
mask branches and checksum overhead are shared across candidates; fixture does not
claim isolated iterator instruction latency. Warmup is3 same-mode fixed traversals;
no asserted settling/frequency effect. Wall time primary; thread/CPU IDs/requested QoS
observations do not establish effective QoS,frequency or within-window migration.

Method consults CPU MCP ask plus05/14 methods/code. Broad ask passages unrelated to
fixture design not used as support.05 describes consuming results;14 describes boundary
IDs/thread time and says "nothing pinned". M4 numbering/frequency/results not transferred.
Local public pthread_cpu_number_np already inspected/used in HARNESS-001 supports IDs;
round7 ask context incorrectly called IDs unavailable, corrected here from local code.
Exact backend/model/cost unknown; independent reviewer startup failed, sequential review.

Decision: locally validated fourth referee revision; baseline requalification AA-006
preregistered and pending. Source selection NONE for new changes; EXP-002 remains PARK.
