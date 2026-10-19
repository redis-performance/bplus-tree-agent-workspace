# Frozen builder-write screen

Six ABBA blocks, seeds 1/2/3 twice, 100K and 1M members, 16-byte binary keys, 1,000,000 distant +N updates at each size. Rotate candidate/size order by block; 144 serial process rows. Timing limit 300 seconds, individual child limit 120 seconds, CPU2. Original baseline binary remains the A side.

Before timing each source passes original 43 tests, frozen score_boundary_oracle, zero_physical_oracle, and packed_decode_oracle in native and ASan/UBSan builds. Referee hashes must match and every patch is preserved. At least 2% improvement required in every block of both primaries; failure rejects. All comparison checksums and owned memory must agree. An eligible contender still needs fresh held-out confirmation, all declared guards, matched profile validation and independent adversarial review; no source adoption overnight.
