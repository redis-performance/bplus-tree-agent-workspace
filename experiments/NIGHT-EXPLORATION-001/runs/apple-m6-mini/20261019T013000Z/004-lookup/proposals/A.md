# A — Direct physical-slot score decode

The hit profile identifies leaf search, and release assembly at the hit return
loads reversed/count, maps physical to logical, then tests reversed again to decode
from physical packing. Unlike EXP-006, this change retains memchr and full member
validation. Hypothesis M6-LOOKUP-PHYSICAL-001: decode score directly at the already
found physical slot; compute logical position only for a requested position output.
Expected benefit: remove duplicate mapping/dependency in score-output lookups.
No layout, scan, hash, allocator, output contract or ownership change.
Risks: reversed base subtraction differs from physical position reversal; zero-width,
64-bit cross-byte fields, finite scores/signed zero and rank outputs must stay exact.
Predict gains on hit100K/1M, unchanged misses and memory. Falsify if either primary
cannot improve>=2% in all six screen blocks; unresolved controls cannot adopt.

Three sequential passes by one worker, not independent agents. Visible backend Codex/GPT-6 family; exact serving variant and measured token cost unknown. Same frozen profile/census/assembly and EXP-006 history.

