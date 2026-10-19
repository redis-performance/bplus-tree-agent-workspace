# Corrected instruction attribution — no candidate timings

The initial exact-mask proposal incorrectly called the 19.49% local-cycle sample at address 0x39bc a tag-verification comparison. Assembly inspection shows it is the `leaf->id == id` assertion immediately after loading the leaf ID. The tag-byte comparison is at 0x3964 and has 0.00% of local samples; its following branch has 0.19%. The 38.50% EOR sample at 0x3880 follows the index tag load and cannot isolate arithmetic cost from memory latency or sampling skid.

This correction removes the primary profile evidence used to choose exact masks. The chair decision is superseded to NONE before any candidate timing. Three proposed implementations and their build attempts remain as unmeasured patches; they are not qualified candidates. The first snapshots had different source filenames; the mapped build shares driver/adapter/hash objects and verifies that baseline .text and .rodata match the original qualified binary exactly. No failed schedule was rerun and no timing result was discarded.

Initial proposal and chair documents are retained in Git history and copied under `superseded/`. This is an abandoned candidate preparation, not a completed measured implementation population. New work requires a different profile-supported mechanism. Source adoption remains NONE.
