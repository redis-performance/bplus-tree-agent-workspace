# Intel architecture replication: exact AMD A/B

Frozen source 8fab511e; imports from AMD 5594fea17, immutable hashes in import-manifest.json. This is architecture replication of an existing independently authored population, not a new population. Baseline profile and 48 held-out A/A rows qualify both 100K/1M primary cases on this Intel host.

Exactly 96 serial CPU2 processes: A/B × 100K/1M × six ABBA blocks, 5M requested original scan operations, 16-byte members, seeds101/102/103 twice. Exact order is screen-schedule.json. Whole-screen fixed300-second cap; preserve partial rows, no extension/retry/adaptive operations. Original referee, assertions, allocator, Clang18 flags remain unchanged. Every timing binary compiled from its own snapshot using identical relative frontend paths and output build/btree-bench. Exact hashes frozen before timing.

Before screen: baseline/A/B original native and sanitizer tests, exact V2 all-match/page oracle, and A/B designated forced-portable oracle in both modes. Referee source unchanged except additive oracle. Every measured block must preserve checksum, actual operations and tree-owned bytes exactly; CPU start/end2; windows>=10ms. Each eligible source must improve >=2% in EVERY primary block in both sizes. Controls must remain valid; incomplete schedule means PARK.

Preregistered implementation choice: if both pass, prefer B for its memcpy load, original word/tail structure and accurate comment. This is a source-maintenance choice, not an A-vs-B speed claim. If only one passes, choose it. Neither passing, failed controls or missing/incomplete evidence means REJECT/PARK as applicable. No alternate-source retry after guard rejection.

Screen cannot establish acceptance. The chosen source requires full original-operation and long-key guards, focused dense/folded/reversed/resize guards, separate matched profile and fresh held-out confirmation seeds201–203, independent audit and adversarial review. ARM prepares focused guard referee separately. Tree source remains NONE until all gates pass. No state/memory tradeoff is authorized.
