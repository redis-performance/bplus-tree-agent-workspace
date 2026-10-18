# BOUNDARY-002 — score bounds and member ownership

Additional semantic checks, not timings or source candidates. Before running: fixed
129-member fixture spanning binary lengths0/1/7/8/16/319/320/321; exact finite boundary
scores including both zero signs, extreme normal and subnormal values, adjacent values
around one. Insert in two opposite orders. Poison/free caller member buffers after
insertion, compare against separate model copies. Verify inclusive/exclusive forward
and reverse score seeks and counts. For every pair of score bounds and every exclusivity
combination, duplicate, delete range, compare exact survivors and recheck original.
No NaN inputs. Preserve failures; no source changes to make tests pass. Release/debug
and ASan/UBSan, 120s child bounds. This extends evidence, not A/A qualification.
