# Proposal C — inline leaf tag search

Sequential pass 3 by the same worker; not independent. Model variant and cost are unknown.

Hypothesis: an inline fixed-width leaf tag search removes libc memchr overhead for a single query. Leaf member lookup accounts for 21.52% of whole-process samples and libc PCs contribute roughly another 10%; memory latency remains a confounder.

The portable scanner already exists as EXP-006 C and has single-lane guard concerns. Reusing it is replication, not a new hypothesis. ARM libc differs from Apple, but the current profile identifies no novel scanner mechanism. REJECT for this population. An explicit replication would require matching patch identity and a separate justification.
