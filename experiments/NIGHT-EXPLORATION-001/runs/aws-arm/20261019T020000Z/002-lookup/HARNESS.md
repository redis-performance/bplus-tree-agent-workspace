# Independent-query lookup referee

Exact unmodified Apple M1 lookup-bench.c from published commit4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9. It separates construction and query permutation; root referee remains untouched. SHA256 7c37bb1b1fffa3dd0331179d0ae61f1cce554bc8a1f93eca389eec264a898aa2. New ARM qualification required.

Validation plan: native and ASan/UBSan, hit/miss, sizes100/1K/10K/100K/1M, lengths8/16/319/320/321/1024 at100K, seeds1/101,2001queries. Existing checksum/memory/order assertions retained. Profile whole process includes setup;20millionqueries reduce but do not eliminate setup contribution. Calibrate each primary on three observations then freeze50ms minimum-target counts from fastest observation; sixABBA A/Ablocks seeds1/2/3.
