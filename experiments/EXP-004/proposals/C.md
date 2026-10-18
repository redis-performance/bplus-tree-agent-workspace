# Proposal C — cache leaf score metadata in iterator

Sequential proposal pass C,not independent agent. Backend/model/token cost unknown.
Same frozen source/profile/qualification/history inputs. Census finds many items per
leaf and invariant width/base/shift for each leaf;baseline decoder reloads metadata
for every element. Hypothesis:store leaf encoding metadata in iterator state and
refresh only at leaf boundaries to improve score-only traversal >=2% without guard
or memory regression. Touch header iterator layout and all initialization/seek paths.

Risk:iterator layout expands,copy semantics/invalidation/stack footprint change;all
entry/seek paths must initialize metadata and mixed output masks remain valid. Existing
profiles do not distinguish load latency from other decode work. More complex than
pure predicate changes and not ready for narrow acceptance. Falsify on primary/guard
or tree-memory failure,missing initialization,or metadata refresh overhead. Broader
public iterator layout cost would need explicit reporting even if tree bytes unchanged.
