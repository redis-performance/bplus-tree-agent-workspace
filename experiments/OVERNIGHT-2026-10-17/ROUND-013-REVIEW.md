# Round 13 sequential adversarial review

Independent reviewer startup failed before any agent ran. This is a separate
coordinator review pass, not independent confirmation. Exact backend/model and
measured token cost are unknown; the supervisor records CLI usage separately.

## Semantics and test strength

BOUNDARY-017's independent buffer model checks whole-allocation equality, so a
correct target ID cannot hide corruption of tags, filters, neighbors or canaries.
It exhausts all legal narrow storage IDs, including the sentinel translation, and
selected wide edges. The private accessor domain is broader than IDs normally
allocated by the public API; that is intentional storage coverage, not evidence of
a reachable public state. Tag-mask tests require all real matches but permit the
source's documented borrow false positives. Both planned faults fail semantic checks.

BOUNDARY-018 maintains a pointer vector and explicit free-ID stack separately from
the encoded registry. Full audits check live mappings, exact LIFO links, no duplicate
free IDs, zero unused capacity, and usable-size accounting. Active-rehash allocation
must grow the ID high-water mark even when free IDs exist; ending rehash permits
reuse without capacity or allocation changes. These are synthetic private registries,
not public trees. They must never be scanned or freed through the full-tree API.
The two faults detect premature reuse and truncated high-ID links. The initial compile
failure is preserved; the final oracle only changes the allocator function name.

Neither new oracle mutates production source. Release/debug and ASan/UBSan all agree
on logical digests. This does not establish portability to another architecture or
allocator. Existing frozen tests and checks are unchanged; no source bug was found.

## Measurement validity

DIAG-016 changes the complete bookkeeping policy. The cumulative manifest grows,
and rotating order reduces but does not eliminate time/order confounding. Parent CPU
measurements show the intended intervention occurred, but its precision criterion
fails. DIAG-017 changes transport, buffering and wait behavior together. Its descriptive
contrast attenuation does not isolate which part matters; its fixed criterion also
fails. Every row remains, including unsuccessful placebo intervals.

DIAG-018 adds an identical observer wrapper to both transport arms and matches the
parent/observer CLOCK_MONOTONIC API. Its interval begins after blocked waitpid returns,
not at exact kernel exit. It includes wrapper metadata/teardown and parent scheduling.
The extra process changes launch conditions, so the result cannot retroactively assign
causes to uninstrumented runs. Fresh reversed-order confirmation supports only this
narrow local interval claim. Benchmark A/A precision remains mixed. No policy, timing
normalization or source guard replacement is authorized by these findings.

The wrapper alarms at 110 seconds and kills/reaps its own child before Python's 120-second
wrapper limit. Normal, nonzero and timeout cases pass under both transports. During
benchmark execution the observer blocks in waitpid; it performs no concurrent profiling
or test work. Parent wrapper windows include their nested benchmark children rather
than double-counting them as independent simultaneous measurements.

The raw audit independently reconstructs 52 wall/thread/diagnostic intervals, verifies
868 serial measurement windows disjoint from 52 validation windows, checks commands,
schedules, journals, hashes, counts, checksums, memory, output masks and source isolation.
All are valid. Six-block t intervals assume approximately independent normal block
effects; serial host effects may violate that assumption. Core IDs are endpoints,
not continuous placement. Frequency and effective QoS remain unknown.

## Decision

Source NONE. EXP-004 A/PARK and EXP-005 PARK/NONE remain unchanged. No new population,
harness, baseline qualification or optimization acceptance. Four new boundary fault
types are detected. Three additional diagnostics are complete: two unsupported
precision interventions and one locally repeated completion-delay observation.
No portable speed headline. Committed provenance and independent review remain pending.

A useful next local task is a public-API counterpart to the private leaf-ID registry
oracle: force leaf retirement and new leaf allocation during an active member resize,
observe that retired IDs stay deferred, then verify reuse after resize completion with
an independent sorted-vector and exact-score model. Existing natural widening/scan
coverage does not explicitly establish this entire transition sequence. Preregister
coverage conditions before running; do not manufacture reachability or weaken them.
For performance, use a separately qualified runner or a distinctly preregistered
measurement method; do not repeat failed local transport/placebo schedules unchanged.
