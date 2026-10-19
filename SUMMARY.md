

19October2026 AWS Intel native lookup: **REJECT/NONE**,1completed sequential population(0accepted/1rejected/0parked),3retained patches.432rows/108blocks, all variants slow both primaries; baseline source unchanged. [Intel evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup/implementation-selection.md). Other-host and historical counts remain separate.


19October2026 AWS Intel update diagnosis **NONE**: separate validated five-pattern referee,360semanticcells,15scopedprofiles+disabledcontrol,25censuscells,600baseline rows/25cells(2qualified). No newimplementationpopulation; Intelcount stays1measuredpopulation/1REJECT/3retainedpatches. See experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/003-update/README.md. Source unchanged.


19 October2026 AWS Intel iterator cache: **PARK / NONE**, fixed screen566/576 rows (141 complete blocks plus two trailing rows), budget stopped without extension. A/B conditional leads; C rejected. Intel totals: **2 measured sequential populations,0 accepted /1 rejected /1 parked;6 retained patches**. Iterator population comparison is partial. Update diagnosis NONE adds no implementation population. Source unchanged. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator/README.md).


Intel baseline scan diagnosis:6 scoped captures show TagMatches27.48%/24.14% of captured executable-range samples at100K/1M. This is a coarse hotspot observation, not a speed claim. Source remains NONE; no new population. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/006-scan-profile/README.md).


Intel scan baseline qualification:48 held-out-seed A/A rows complete, both100K/1M controls qualify within±1% with windows>=444ms. No candidate timing or population increment. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/007-scan-replication/README.md).

Intel scan architecture replication: exact A/B pass both discovery primaries; B advances under preregistered source preference, **PARK/source NONE** pending guards and fresh confirmation. No new population. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/007-scan-replication/README.md).

Intel full original guard A/A completes960rows;57/80 cells qualify,23 unresolved. Scan B remains **PARK/source NONE**; no new population. Runner handed idle for independent confirmation. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/008-original-guards/README.md).

Intel full original B guard comparison completes960rows;56/57 qualified cells pass,24/80 unresolved overall. **PARK/source NONE**, no population increment. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/008-original-guards/README.md).

Intel focused SCAN controls complete864rows/216blocks:22/36 cells qualify,14 failprecision,none short. **PARK/source NONE**, no population increment. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/011-focused-scan-guards/README.md).

Intel focused B guards complete864rows/216blocks;all22 qualifiedcells pass,14 controls remain unresolved,24 original guardgaps unchanged. **PARK/source NONE**; no population increment. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/011-focused-scan-guards/README.md).
