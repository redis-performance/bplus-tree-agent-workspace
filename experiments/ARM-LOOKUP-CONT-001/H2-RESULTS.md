# H2 cached-metadata population: PARK / source NONE

B passes the original six cases and five supplemental guards on both ARM and Intel with both compilers, and passes all eleven held-out seed-29 cases on ARM and Intel. It still cannot be accepted: ARM seed-43 baseline qualification fails one miss block before any candidate comparison. A and C remain rejected for their earlier memory/update and iterator guard failures.

The failed A/A block has elapsed nanoseconds 2,933,432,897 / 2,931,161,925 / 2,945,491,659 / 3,162,753,291 in ABBA order, all from the same immutable baseline. The contrast is **-3.601147%**, outside the frozen ±1% gate. Owned bytes remain 14,272 and every row exceeds 250 ms. Seventeen other control blocks pass. The failure is unresolved baseline noise, not an observed regression in B. No row is removed and no unchanged retry is admitted.

| Completed held-out cohort | Primary elapsed change, three blocks | Worst guard | Outcome |
|---|---|---:|---|
| ARM target, seed29 | -5.175%, -5.136%, -5.313% | +0.098% | All eleven cases pass |
| Intel target, seed29 | -4.813%, -4.784%, -4.732% | +0.278% | All eleven cases pass |
| ARM target, seed43 | No candidate comparison | Not run | Baseline A/A fails |
| Intel target, seed43 | -5.640%, -5.458%, -5.660% | +0.298% | Retained; cannot rescue ARM |

Both complete host sequences were launched in advance with only per-host continuation gates. Intel's last supplemental phase began about13.426 seconds after ARM recorded its failed qualification, before the controller observed it. This is a cross-host stopping limitation, not a phase already executing at the instant of failure. Its raw evidence is retained without acceptance credit. No new H2 sequence followed the observed failure.

The [independent final review](reviews/H2-FINAL.md) reconstructs all864 held-out rows, immutable source/referee/ELF/collector joins and the stopping chronology. Earlier [readiness review](reviews/H2-INDEPENDENT-READINESS.md) covers1,056 original A/A and B rows. All losing patches and additional rejected-variant rows remain retained. The prospective source snapshot and exact-upstream patch stay private and unadopted; historical root source and every frozen extraction remain unchanged.

A fresh audit found the pre-existing ARM profiler active with unrestricted CPU affinity. This establishes a concrete isolation difference, not the cause of the failed sample. [Q4](ARM-PROFILER-OFF-QUALIFICATION.md) separately proposes baseline-only qualification with that service stopped and verified restoration; it does not reopen or erase this PARK. Any later candidate validation needs its own admission and all acceptance gates.

## TMA classification and profiles

Matched ARM process-user counters support reduced lookup work, but ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and child shares remain unavailable under the collector's scope/formula limits. The [ARM audit](reviews/H2-ARM-PROFILE-AUDIT.md) verifies counters and sample evidence, with explicit LTO build-ID and negligible kernel-labelled-sample caveats. Prior ARM measurements retained the active background profiler; continuous CPU2 exclusion was not established. No attribution of the noise or pipeline cause follows from that fact.

Qualified Intel roots and children are reported separately with bounded CPU-wide scope and raw-formula limits. [Matched profile assessment](H2-ARM-PROFILES.md) and [Intel profile/guard audit](reviews/H2-PROFILE-GUARD-AUDIT.md) remain supporting evidence, not substitutes for failed ARM confirmation. Standalone results do not establish server-command recovery.
