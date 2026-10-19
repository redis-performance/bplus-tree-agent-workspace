# ARM lookup diagnosis — NONE

The independent-query referee passed 80 native/sanitizer cells. Its fixed A/A run completed 288 serial processes: 10/12 cells qualify, including both 100K/1M hit primaries, both miss guards and all 100K key lengths. The 100/1K hit guards fail. No candidate timing occurred.

Whole-process hit profiles place 36.00% of samples in zbtreeScoreRaw and 21.52% in leaf member lookup at 100K. Dedicated miss profiles place 31.97%/26.32% in zbtreeScoreRaw and 39.79%/43.12% in the sds wrapper at 100K/1M. These profiles include setup; the larger miss capture has visible construction work. CPU counters are available, but no precise load-latency attribution is claimed.

The initial exact-mask proposal mistook a leaf-ID assertion comparison for tag verification. Detailed assembly corrected that before timing, and the chair selected NONE. See PROFILE-ERRATUM.md. The actual tag comparison has no samples in this capture, which is not proof of zero cost. All three unmeasured patches and build attempts remain. Existing tests were not weakened; candidate correctness was not pursued after the premise was withdrawn.

The separate read-only empty-slot idea also lacks a material sampled hotspot in the dedicated miss profile. Most index samples cluster at the dependent tag-load/EOR sequence; the eight conditional comparisons are not prominent. Without a path census or load-latency experiment, no arithmetic or prefetch remedy is selected. The existing leaf scanner is a prior EXP-006 hypothesis and was not repeated as new work.

Source selection NONE. This adds baseline qualification and profile diagnostics, not an accepted optimization or a completed measured implementation population. Next useful direction is the previously documented count-one decoder lead, with fresh ARM profiling and controls. No Redis server work occurred.
