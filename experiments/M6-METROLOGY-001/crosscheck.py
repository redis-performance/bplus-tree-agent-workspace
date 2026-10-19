#!/usr/bin/env python3
"""Compare independently reconstructed integer data, without rerunning workloads."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
root = json.loads((HERE / 'analysis.json').read_text())
columns = {
    'A': ['A_wall_ns', 'B_wall_ns', 'A_thread_ns', 'B_thread_ns'],
    'B': ['wall_A_sum_ns', 'wall_B_sum_ns', 'thread_A_sum_ns', 'thread_B_sum_ns'],
    'C': ['wall_A_ns_sum', 'wall_B_ns_sum', 'thread_A_ns_sum', 'thread_B_ns_sum'],
}
root_columns = ['wall_A_ns', 'wall_B_ns', 'thread_A_ns', 'thread_B_ns']
hashes = {}
for participant, names in columns.items():
    report = HERE / 'reviews' / (participant + '.json')
    review = json.loads(report.read_text())
    assert len(review['rows']) == 48 and len(review['blocks']) == 12
    for block in root['blocks']:
        peer = next(b for b in review['blocks'] if (b['size'], b['block']) == (block['size'], block['block']))
        assert [peer[n] for n in names] == [block[n] for n in root_columns]
    for row in root['rows']:
        peer = next(r for r in review['rows'] if r['index'] == row['index'])
        assert peer['wall_ns'] == row['elapsed_ns']
        assert peer['thread_ns'] == row['thread_elapsed_ns']
        assert int(peer['checksum']) == row['checksum'] and peer['tree_bytes'] == row['tree_bytes']
    for path in [report, report.with_suffix('.md')]:
        assert path.is_file() and path.stat().st_size
        hashes[str(path.relative_to(HERE))] = sha(path)
    script = HERE / ('analyze-' + participant.lower() + '.py')
    if participant == 'C':
        script = HERE / 'reviews/analyze-c.py'
    expected = review.get('script_sha256', review.get('analysis_script_sha256'))
    assert sha(script) == expected
    hashes[str(script.relative_to(HERE))] = sha(script)
result = {'status': 'PASS_THREE_INDEPENDENT_RECONSTRUCTIONS_AGREE', 'reviewers': list(columns),
    'matched_rows_per_reviewer': 48, 'matched_blocks_per_reviewer': 12,
    'root_analysis_sha256': sha(HERE / 'analysis.json'), 'review_sha256': hashes,
    'native_workloads_launched': 0, 'new_source_populations': 0,
    'limits': 'Agreement confirms recorded arithmetic, not causal attribution, clock accuracy or optimization acceptance.'}
(HERE / 'review-agreement.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
