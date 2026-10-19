# Byte-aligned packed moves

Three sequential native Codex analysis passes, not independent agents. Exact inherited model/backend and measured token/USD usage are unavailable. Same frozen source, profiles, assembly, census and fresh A/A evidence.

Hypothesis: memmove for byte-aligned packed fields removes generic bit shifting. Census shows only 1.79% aligned moved bits in the previous partial 1M update; insertion/deletion are around 28%. Scoped 1M insert/delete write helpers are 3.53%/5.32%, placing limited expected total headroom near or below the 2% target. Additional guard cost for generic widths and libc call overhead could offset benefits. Rank second; do not implement this direction now.
