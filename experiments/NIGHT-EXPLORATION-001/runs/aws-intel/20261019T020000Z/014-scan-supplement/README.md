# Intel supplemental SCAN guards

Supplemental correctness preparation passes: 756 validator commands, 90 fixture models per source, native/sanitizer public-census parity, 43 original tests per build and 32 total negative controls. Exact reviewed model manifests match, baseline/B outputs agree within build modes, and 38 post-preparation hashes remain unchanged. Completed in 69.55 seconds under the 600-second cap. Frozen baseline calibration is next; no supplemental candidate timing yet.

Imported referee ec21ce601 and frozen protocol 7dbfe8259. Original 8fab baseline and exact SSE2 B are distinct from the corrected-adapter source. This covers 30 cells with lengths 8/319/320/321/1024, three score encodings including signed zero, small fully reversed leaves and active paused resize. All original guard gaps remain unresolved. Source adoption NONE.

Supplemental calibration completes 684 baseline-only rows in 34.24 seconds under 180 seconds. Raw schedule, CPU2, semantic identity and 38 post-phase hashes pass. All 30 counts and both complete 720-process schedules frozen before comparison; next A/A has a fixed 480-second cap. No retry or adaptation.

2026-10-19T05:27:48.219557+00:00 Supplemental A/A completes 720 raw processes and 180 blocks in 157.126 seconds under 480 seconds. Ten of 30 cells qualify; 0 short cells. Exact frozen schedule, serial CPU2, model/checksum/owned bytes and 38 post-phase hashes pass. All 30 cells remain in the frozen full B diagnostic, including 20 unresolved controls. Overall source NONE/PARK remains.

2026-10-19T05:32:10.024207+00:00 Supplemental B completes 720 processes/180 blocks in 154.887 seconds under 480 seconds. Eight of ten qualified guard cells pass; trim/319-byte/signed-zero regresses in all six blocks (+1.566% to +6.877%, median +4.931%), so the old-source Intel SSE2 B replication is REJECTED. Qualified resize/319-byte/signed-zero is mixed; twenty noisy controls remain. Exact CPU2/serial schedule, checksums/owned bytes and 38 supplemental plus 22 original post-phase hashes pass. Source adoption NONE, no alternate A retry. Corrected-source baseline-only 016 remains a separate approved diagnostic.
