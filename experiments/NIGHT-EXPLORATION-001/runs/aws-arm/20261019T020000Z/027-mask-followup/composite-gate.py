"""Exact immutable two-attempt correctness gate; never relabel the failed attempt."""
import hashlib,json,pathlib
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def verify(here,checkout):
    receipt_path=here/'composite-correctness.json';receipt=json.loads(receipt_path.read_text())
    assert receipt['status']=='PASS_COMPOSITE_CORRECTNESS' and receipt['original_attempt_status']=='failed'
    assert receipt['root_closure_review'] and receipt['independent_closure_review']
    suffix=checkout/'scratch/arm-mask-continuation-20261019'
    assert sha(suffix/'binding.json')==receipt['binding_sha256']
    b=json.loads((suffix/'binding.json').read_text())
    assert sha(here/'validation/result.json')==receipt['original_raw_result_sha256']
    assert sha(suffix/'continuation/result.json')==receipt['suffix_raw_result_sha256']
    old=json.loads((here/'validation/result.json').read_text());new=json.loads((suffix/'continuation/result.json').read_text())
    assert old['status']=='failed' and len(old['commands'])==2118
    assert all(x.get('checked') for x in old['commands'][:2117]) and not old['commands'][-1].get('checked',False)
    assert new['status']=='six_command_suffix_complete_pending_independent_closure' and new['identity_unchanged']
    assert len(new['commands'])==6 and all(x.get('checked') for x in new['commands'])
    assert [x['original_command_number'] for x in new['commands']]==list(range(2119,2125))
    assert sha(here/'preparation-freeze.json')==b['prior_freeze_sha256']
    assert sha(suffix/'execution-freeze.json')==receipt['suffix_execution_freeze_sha256']
    sf=json.loads((suffix/'execution-freeze.json').read_text())
    for n,h in sf['files'].items():assert sha(suffix/n)==h
    for n,h in b['prior_inputs'].items():assert sha(here/n)==h
    for n,h in b['prior_raw_artifacts'].items():assert sha(here/'validation'/n)==h
    for n,h in receipt['suffix_raw_artifacts'].items():assert sha(suffix/'continuation'/n)==h
    snapshots={v:{n:sha(here/v/n) for n in files} for v,files in b['snapshots_before'].items()};assert snapshots==b['snapshots_before']
    guards={v:{n:sha(here/v/'build/native'/n) for n in files} for v,files in b['guard_binary_sha256'].items()};assert guards==b['guard_binary_sha256']==receipt['guard_binary_sha256']
    protected={n:sha(checkout/n) for n in b['protected_binaries']};assert protected==b['protected_binaries']==receipt['protected_binaries']
    return dict(receipt_sha256=sha(receipt_path),binding_sha256=sha(suffix/'binding.json'),original_status=old['status'],suffix_status=new['status'],snapshots=snapshots,guard_binary_sha256=guards,protected_binaries=protected,original_raw_result_sha256=sha(here/'validation/result.json'),suffix_raw_result_sha256=sha(suffix/'continuation/result.json'))
