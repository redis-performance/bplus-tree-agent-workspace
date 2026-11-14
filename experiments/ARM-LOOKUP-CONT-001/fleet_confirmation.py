#!/usr/bin/env python3
"""Pinned, self-contained H2-B six-case confirmation. Fleet only."""
import argparse
import hashlib
import json
import math
import os
import pathlib
import platform
import statistics
import subprocess
import sys
import time

EXP = pathlib.Path('experiments/ARM-LOOKUP-CONT-001')
UPSTREAM = 'ee8e7f70152404649ac947157fd662d11b4a00d5'
BASE_SOURCE = '16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9'
B_SOURCE = '63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29'
CASES = {'hit': 50000, 'score': 50000, 'miss': 100000,
         'long': 20000, 'external': 20000, 'update': 20000}
REFEREE_PINS = {'lookup.c': '1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827',
 'current/src/zset_btree.c': '16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9',
 'current/src/zset_btree.h': 'e1575e812cdff6fae794c4dd619a4d6d7c586c5df01ac0c881376acd294161ac',
 'current/compat/server.h': '2e287290fe2b3492098d36c4dfee783be0c43b9cde5954a176c84aa28d4f36dd',
 'current/compat/standalone.c': '300e1c37c1679014e25446fd82f1c2d0bf36c46c79d29255c856782e14c10d71',
 'current/vendor/sds.h': '5109573260ba9e3297030a851a0da1e485512a8c8f5b3cdbd6b062bef023a7b4',
 'current/vendor/siphash.c': '2e53f604ab8389a744efa55c3891eb9ff8983d18314400338e17ecc6c5b4f75e',
 'current/vendor/testhelp.h': 'b8c5243aac89758f44db1578735d6e3afc8e975dc1daa976ad4160ce55cbe9bd'}
ORIGINS = {'arm-native': {'platform': 'arm',
                'machine': 'aarch64',
                'origin': 'H2-native',
                'cohort': 'native',
                'scale': 1,
                'qualification': 'native-requalification',
                'baseline_path': 'bin/native/lookup',
                'baseline_sha256': '2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf',
                'candidate_path': 'bin/H2-native-B',
                'candidate_sha256': 'e16a70a4de79ede0bf177b2dd8bd2ddb3af4349c9e22509c8e5199d390a52cdd',
                'candidate_source': 'variants/H2-native/B/zset_btree.c',
                'provenance': {'H2-native/analysis.json': '3faeee061f1fed95f702f9b8f3f456a282b1ac15d3edbe181b4b6d147f73a841',
                               'H2-native/commands.jsonl': 'de4e610014a927ce027eca54ee32e2f2c307f05d3ff50fff12c667566c596e03',
                               'H2-native/comparison.jsonl': '1d1c0dbbdfbc1b90145cefe78256befade63263de1efde59f85c992ba1ea1525',
                               'H2-native/metadata.json': 'fee8d56e413905f9bf7037c978ee469dbde8aa0cba747f0e7c70720e6d0322e0',
                               'baseline/commands.jsonl': 'a5655de659f2f3a3f09edfc5c1535d2b13c2c456b9955bac596399c2b6298913',
                               'baseline/metadata.json': '9e662fdaab6b7cb8515271104332a7909a9b22dd3be4b8545f762d371fbe668f',
                               'native-requalification/aa.jsonl': 'a47ead4da0149a9e78ffa4eda63f8a8c14b3d30812c58a42cf5d7452525eb29e',
                               'native-requalification/analysis.json': 'e886febbfcd821415350fa7c95868c9fac6ea1189135db3f22bdc823b8be8793',
                               'native-requalification/commands.jsonl': '62137666e365c20fba35b1f9648cb19dd2c4f534eea5a5b604d39e6fa866051c',
                               'native-requalification/metadata.json': 'eb2805b3656be57a8413d331fbb68c9d656931b3adf17f22f8b924f4581c5655'}},
 'arm-gcc15-lto': {'platform': 'arm',
                   'machine': 'aarch64',
                   'origin': 'H2-lto',
                   'cohort': 'gcc15-lto',
                   'scale': 5,
                   'qualification': 'lto-long-qualification',
                   'baseline_path': 'bin/gcc15-lto/lookup',
                   'baseline_sha256': '77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb',
                   'candidate_path': 'bin/H2-lto-B',
                   'candidate_sha256': '283263f631cbc1440c1c688537edc8eb894de90cba86107d63faa3e68ca7a1f4',
                   'candidate_source': 'variants/H2-lto/B/zset_btree.c',
                   'provenance': {'H2-lto/analysis.json': '6b9657a7ee8e3878f9ae9ed1e26d42e6ad65cea583cb8bfa797c9885ce0a26f1',
                                  'H2-lto/commands.jsonl': '7320652982fe96c6ba34e07ad6a007319dcc604ca7a8a8a1bd84fd1b0d3354e0',
                                  'H2-lto/comparison.jsonl': 'b537d3e282af3bdad0d252b5ce76e69e762b033697f0c279c462ab17b7e73064',
                                  'H2-lto/metadata.json': '890e64fd75bf687b5228f1ab5e731c664e587b9603821ff1fc2d225d9cbba6f3',
                                  'baseline/commands.jsonl': 'a5655de659f2f3a3f09edfc5c1535d2b13c2c456b9955bac596399c2b6298913',
                                  'baseline/metadata.json': '9e662fdaab6b7cb8515271104332a7909a9b22dd3be4b8545f762d371fbe668f',
                                  'lto-long-qualification/aa.jsonl': '3d3ae6fb1285d3b8b96dc0f6d57a00478e6883866e6ae8764458ed46439275c5',
                                  'lto-long-qualification/analysis.json': '2b5041d955a910b45457c10033396094b107abe21c6cd77588f9dd40c82ba48f',
                                  'lto-long-qualification/commands.jsonl': '3be7f35671360bb1ef05296f4fa7d486fa7ba84db8ce6b35a3ae6bab3b61993d',
                                  'lto-long-qualification/metadata.json': '4bcb9ab52c86fdf19f5ad20543dc9210ee63d2912ff4ffe6b2eba7322946ea4d'}},
 'intel-native': {'platform': 'intel',
                  'machine': 'x86_64',
                  'origin': 'H2-native',
                  'cohort': 'native',
                  'scale': 5,
                  'qualification': 'baseline',
                  'baseline_path': 'bin/native/lookup',
                  'baseline_sha256': '2a38b93b94cfc59b347defaa3ccb5560f6bb7a70fbad92f350fbc5d74e00aebd',
                  'candidate_path': 'bin/H2-native-B',
                  'candidate_sha256': 'ff76b2b9e560cfaae0e48ca61f25d6f79c847cfad88df3bd5fcd6048e55eebd6',
                  'candidate_source': 'variants/H2-native/B/zset_btree.c',
                  'provenance': {'H2-native/analysis.json': '14a7460d47c26665cc255eefaeb9467a693d5fb40995c7063e7667c3bc63b58a',
                                 'H2-native/commands.jsonl': 'ec43825305c2f057765a4b2dc35f617866c69fd9720b327b479e67bc10ed0656',
                                 'H2-native/comparison.jsonl': '5959fa7a3948290f11f9ff51ee252af747ad4aa1b2ae84ca81db57ba2713904f',
                                 'H2-native/metadata.json': '5b657afb5b2aaee5690c35e74597e4fe1722560e97ad0de241b029db49fa85de',
                                 'baseline/aa.jsonl': '0d2297a1f37d983fe1debf6e4d0bf91d876ba5416917aba0b7bdacf146d6db37',
                                 'baseline/analysis.json': '9bcbc6bfc59977127e7c49339010d71410d9e9e5c87a9ceda4318c19ccba99b6',
                                 'baseline/commands.jsonl': '20635338b64c889dc31741636680a952db771c793bc03ee4fdce4df5a12a6b5a',
                                 'baseline/metadata.json': '814db33b5d30ea9c926ab38bd016668ca42b91591b53a57ca62a29a1a743acaa'}},
 'intel-gcc15-lto': {'platform': 'intel',
                     'machine': 'x86_64',
                     'origin': 'H2-lto',
                     'cohort': 'gcc15-lto',
                     'scale': 5,
                     'qualification': 'baseline',
                     'baseline_path': 'bin/gcc15-lto/lookup',
                     'baseline_sha256': '1d64647324ba83427c4eab71196e7d136ee566bd03b3c1b3b7acc9ae5ffe3868',
                     'candidate_path': 'bin/H2-lto-B',
                     'candidate_sha256': '0b6365ed258752de05af80434f8e85feb30ac833e3bba76ce93ff9e28375b293',
                     'candidate_source': 'variants/H2-lto/B/zset_btree.c',
                     'provenance': {'H2-lto/analysis.json': '39ad4bbeb69138a796b2f5faa2f4424118e34738e8d05257f015315dfda18cdd',
                                    'H2-lto/commands.jsonl': '5e9304318814cc601edca9989cc8097a80a6a35185d23af5cc6d1daacd0ff2cb',
                                    'H2-lto/comparison.jsonl': '918a13478243edf0f6467573295a512f65cc3452bcd6110e6050052686fa391f',
                                    'H2-lto/metadata.json': 'eeee6e1209123326ab4039d1a924f83dff367e927d976b3eeef6dcb2831fee1b',
                                    'baseline/aa.jsonl': '0d2297a1f37d983fe1debf6e4d0bf91d876ba5416917aba0b7bdacf146d6db37',
                                    'baseline/analysis.json': '9bcbc6bfc59977127e7c49339010d71410d9e9e5c87a9ceda4318c19ccba99b6',
                                    'baseline/commands.jsonl': '20635338b64c889dc31741636680a952db771c793bc03ee4fdce4df5a12a6b5a',
                                    'baseline/metadata.json': '814db33b5d30ea9c926ab38bd016668ca42b91591b53a57ca62a29a1a743acaa'}}}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def contained(root, relative):
    path = root / relative
    require(path.resolve().is_relative_to(root), 'Artifact outside reserved root')
    return path


def phase_name(origin, seed):
    require(origin in {'H2-native', 'H2-lto'} and seed in {29, 43},
            'Only original H2 phases and held-out seeds29/43 allowed')
    return origin + '-confirmation-' + str(seed)


def check_row(row, case, seed, sweeps):
    require(row['case'] == case and row['seed'] == seed and
            type(row['ops']) is int and row['ops'] == sweeps * 500,
            'Unexpected case/seed/operation count')
    require(row['hits'] == (0 if case == 'miss' else sweeps * 500) and
            row['score_sum'] == (125250 * sweeps if case == 'score' else 0),
            'Checksum differs from fixture model')
    require(type(row['elapsed_ns']) is int and row['elapsed_ns'] > 0 and
            type(row['owned_bytes']) is int and row['owned_bytes'] > 0,
            'Invalid duration/memory field')


def block_result(rr, case, block, qualification, platform_name):
    require(len(rr) == 4 and [r['slot'] for r in rr] == list(range(4)) and
            [r['label'] for r in rr] == list('ABBA'), 'Invalid ABBA grid')
    for key in ['ops', 'hits', 'score_sum']:
        require(len({r[key] for r in rr}) == 1, 'Inconsistent block ' + key)
    aa, bb = rr[::3], rr[1:3]
    delta = (statistics.mean(r['elapsed_ns'] for r in bb) /
             statistics.mean(r['elapsed_ns'] for r in aa) - 1) * 100
    memory = (statistics.mean(r['owned_bytes'] for r in bb) /
              statistics.mean(r['owned_bytes'] for r in aa) - 1) * 100
    minimum = min(r['elapsed_ns'] for r in rr)
    limit = -2 if case == 'hit' and platform_name == 'arm' else 1
    passed = (abs(delta) <= 1 if qualification else delta <= limit)
    passed = passed and memory <= 1 and minimum >= 250000000
    require(math.isfinite(delta) and math.isfinite(memory), 'Nonfinite block effect')
    return dict(case=case, block=block, delta_pct=delta, memory_delta_pct=memory,
                min_window_ns=minimum, passed=passed)


def check_exclusions(root):
    path = root / 'H2-exclusions.json'
    if path.exists():
        excluded = read(path)
        require(isinstance(excluded, dict) and 'B' not in excluded,
                'H2-B excluded or exclusion evidence invalid')


def identities(root, config, collector_pin):
    require(sha(pathlib.Path(__file__).resolve()) == collector_pin,
            'Self-contained collector differs from reviewed SHA256 pin')
    for relative, expected in REFEREE_PINS.items():
        require(sha(contained(root, EXP / relative)) == expected,
                'Frozen source/referee mismatch: ' + relative)
    for relative, expected in config['provenance'].items():
        require(sha(contained(root, relative)) == expected,
                'Discovery/qualification provenance changed: ' + relative)
    require(sha(contained(root, config['candidate_source'])) == B_SOURCE,
            'Candidate source is not approved H2-B revision')
    for label in ['baseline', 'candidate']:
        require(sha(contained(root, config[label + '_path'])) ==
                config[label + '_sha256'], 'Immutable ELF mismatch: ' + label)
    check_exclusions(root)


def audit_origin(root, config):
    """Reconstruct original B comparison and its own qualified A/A controls."""
    origin, cohort = config['origin'], config['cohort']
    meta = read(root / origin / 'metadata.json')
    prior = read(root / 'baseline/metadata.json')
    require(meta['cohort'] == cohort and str(meta['seed']) == '17' and
            meta['scale'] == config['scale'] and meta['source_freeze'] == UPSTREAM and
            not meta.get('confirmation'), 'Origin is not frozen seed17 discovery')
    require(meta['baseline_sha256'] == prior['binary_sha256'][cohort] ==
            config['baseline_sha256'] and
            meta['variants']['B']['source_sha256'] == B_SOURCE and
            meta['variants']['B']['binary_sha256'] == config['candidate_sha256'],
            'Origin source/baseline/candidate join failed')
    require(prior['source_manifest']['upstream_sha'] == UPSTREAM and
            prior['source_manifest']['files']['current/src/zset_btree.c']['sha256']
            == BASE_SOURCE, 'Baseline is not pinned upstream extraction')
    qdir = root / config['qualification']
    qmeta, qreport = read(qdir / 'metadata.json'), read(qdir / 'analysis.json')
    require(qmeta['binary_sha256'][cohort] == config['baseline_sha256'] and
            qreport['cohorts'][cohort]['all_pass'] is True,
            'Original cohort qualification failed or used different ELF')
    report = read(root / origin / 'analysis.json')
    require(report['variants']['B']['eligible'] is True, 'Original H2-B did not pass')
    for qualification, directory, filename in [
            (True, qdir, 'aa.jsonl'), (False, root / origin, 'comparison.jsonl')]:
        selected = [r for r in rows(directory / filename) if r['cohort'] == cohort and
                    (qualification or r['variant'] == 'B')]
        require(len(selected) == 72, 'Origin grid incomplete or duplicated')
        commands = {}
        for command in rows(directory / 'commands.jsonl'):
            commands.setdefault(command['stem'], []).append(command)
        for case, count in CASES.items():
            case_rows = []
            for block in range(3):
                rr = [r for r in selected if r['case'] == case and r['block'] == block]
                for r in rr:
                    check_row(r, case, 17, count * config['scale'])
                    stem = (f'aa-{cohort}-{case}-{block}-{r["slot"]}' if qualification
                            else f'compare-B-{case}-{block}-{r["slot"]}')
                    require(len(commands.get(stem, [])) == 1, 'Missing/duplicate process')
                    command = commands[stem][0]
                    raw = read(directory / (stem + '.stdout'))
                    fields = {'case', 'seed', 'ops', 'elapsed_ns', 'hits', 'score_sum', 'owned_bytes'}
                    require(raw == {k: r[k] for k in fields} and
                            not (directory / (stem + '.stderr')).read_bytes() and
                            command['returncode'] == 0, 'Original process join failed')
                    label = 'baseline' if qualification or r['label'] == 'A' else 'candidate'
                    argv = command['argv']
                    require(len(argv) == 8 and argv[:3] == ['taskset', '-c', '2'] and
                            argv[3].endswith('/' + config[label + '_path']) and
                            argv[-4:] == ['measure', case, '17', str(count * config['scale'])],
                            'Original process arguments differ from cohort')
                    if not qualification:
                        require(r['binary_sha256'] == config[label + '_sha256'],
                                'Original comparison row ELF mismatch')
                result = block_result(rr, case, block, qualification, config['platform'])
                require(result['passed'], 'Original raw block failed declared gate')
                case_rows.extend(rr)
            for label in ['A', 'B']:
                require(len({r['owned_bytes'] for r in case_rows if r['label'] == label}) == 1,
                        'Original memory endpoints inconsistent')


def leasecheck(root, config, saved=None):
    d = read(root / 'reservation.json')
    require(d['owner'] == 'bplus ARM-LOOKUP-CONT-001' and d['state'] == 'RESERVED' and
            time.time() < d['deadline'] - 300, 'Owned lease/cleanup margin unavailable')
    identity = (d['coordinator_pid'], d['coordinator_ticks'], d['deadline'])
    require(saved is None or identity == saved, 'Lease/coordinator changed during confirmation')
    require(subprocess.run(['systemctl', 'is-active', '--quiet', root.name + '-release.timer'],
                           capture_output=True).returncode == 0, 'Release timer inactive')
    fields = (pathlib.Path('/proc') / str(d['coordinator_pid']) / 'stat').read_text().rsplit(') ', 1)[1].split()
    require(fields[0] == 'T' and fields[19] == str(d['coordinator_ticks']),
            'Original coordinator identity or stopped state changed')
    require(os.sched_getaffinity(0) == {0}, 'Controller not confined to CPU0')
    require(platform.machine() == config['machine'], 'Host architecture differs from cohort')
    cpu = pathlib.Path('/sys/devices/system/cpu/cpu2')
    require((cpu / 'online').read_text().strip() == '1' and
            (cpu / 'topology/thread_siblings_list').read_text().strip() == '2',
            'Measurement CPU offline or effective SMT sibling present')
    require(not subprocess.check_output(['docker', 'ps', '-q'], text=True).strip(),
            'Concurrent Docker container')
    if config['platform'] == 'intel':
        require('sibling50_online' in d and
                pathlib.Path('/sys/devices/system/cpu/cpu50/online').read_text().strip() == '0',
                'Intel saved SMT state absent or sibling50 online')
        status = subprocess.run(['systemctl', 'show', '--property=ActiveState', '--value',
                                 'snap.parca-agent.parca-agent-svc.service'],
                                capture_output=True, text=True)
        require(status.returncode == 0 and status.stdout.strip() == 'inactive',
                'Intel Parca service not verified inactive')
    return identity


def select_origin(root, origin):
    require(origin in {'H2-native', 'H2-lto'}, 'Unrecognized origin phase')
    meta = read(root / origin / 'metadata.json')
    matches = [c for c in ORIGINS.values() if c['origin'] == origin and
               c['baseline_sha256'] == meta.get('baseline_sha256')]
    require(len(matches) == 1, 'Origin not one of four reviewed cohorts')
    return matches[0]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', required=True)
    p.add_argument('--origin-phase', choices=['H2-native', 'H2-lto'], required=True)
    p.add_argument('--seed', type=int, choices=[29, 43], required=True)
    p.add_argument('--collector-sha256', required=True,
                   help='Reviewed SHA256 of this self-contained collector')
    a = p.parse_args()
    root = pathlib.Path(a.root).resolve()
    os.chdir(root)
    phase = phase_name(a.origin_phase, a.seed)
    out = root / phase
    require(not out.exists(), 'Confirmation already claimed; failed/partial phases cannot retry')
    config = select_origin(root, a.origin_phase)
    identities(root, config, a.collector_sha256)
    audit_origin(root, config)
    saved_lease = leasecheck(root, config)
    out.mkdir()  # Atomic one-shot claim before any fresh-seed process.
    sweeps = {k: v * config['scale'] for k, v in CASES.items()}
    metadata = dict(confirmation=True, origin=a.origin_phase, seed=a.seed,
                    cohort=config['cohort'], platform=config['platform'],
                    scale=config['scale'], sweeps=sweeps, source_freeze=UPSTREAM,
                    baseline_sha256=config['baseline_sha256'],
                    variants={'B': dict(source_sha256=B_SOURCE,
                                        binary_sha256=config['candidate_sha256'])},
                    source_and_referee_sha256=REFEREE_PINS,
                    provenance_sha256=config['provenance'],
                    collector_sha256=a.collector_sha256, started=time.time())
    write(out / 'metadata.json', metadata)

    def run(command, stem):
        identities(root, config, a.collector_sha256)
        leasecheck(root, config, saved_lease)
        record = dict(argv=command, stem=stem, started=time.time(),
                      preflight_identity_lease_isolation='passed')
        try:
            process = subprocess.run(command, capture_output=True, text=True, timeout=240)
            stdout, stderr, code = process.stdout, process.stderr, process.returncode
        except subprocess.TimeoutExpired as error:
            stdout, stderr, code = error.stdout or '', error.stderr or '', None
            stdout = stdout.decode(errors='replace') if isinstance(stdout, bytes) else stdout
            stderr = stderr.decode(errors='replace') if isinstance(stderr, bytes) else stderr
            record['timeout'] = True
        (out / (stem + '.stdout')).write_text(stdout)
        (out / (stem + '.stderr')).write_text(stderr)
        record.update(returncode=code, finished=time.time())
        with (out / 'commands.jsonl').open('a') as f:
            f.write(json.dumps(record) + '\n')
        require(code == 0 and not stderr, 'Process failed; phase consumed: ' + stem)
        identities(root, config, a.collector_sha256)
        leasecheck(root, config, saved_lease)
        with (out / 'postflight.jsonl').open('a') as f:
            f.write(json.dumps(dict(stem=stem, checked=time.time(),
                      identity_lease_isolation='passed')) + '\n')
        return stdout

    try:
        run(['taskset', '-c', '2', sys.executable, '-c',
             'import os,sys;sys.exit(0 if os.sched_getaffinity(0)=={2} else 1)'],
            'affinity-zero-work')
        for label in ['baseline', 'candidate']:
            for case in CASES:
                result = json.loads(run(['taskset', '-c', '2', str(root / config[label + '_path']),
                    'verify', case, str(a.seed), '1'], 'verify-' + label + '-' + case))
                require(result['verified'] is True and result['case'] == case and
                        result['seed'] == a.seed and result['members'] == 500,
                        'Fresh-seed fixture verification failed')
        aa_memory = {}
        for qualification in [True, False]:
            blocks, allrows = [], []
            action = 'aa' if qualification else 'compare'
            for case, count in sweeps.items():
                memory_by_binary = {}
                for block in range(3):
                    rr = []
                    for slot, label in enumerate('ABBA'):
                        which = 'baseline' if qualification or label == 'A' else 'candidate'
                        stem = f'{action}-{case}-{block}-{slot}'
                        row = json.loads(run(['taskset', '-c', '2', str(root / config[which + '_path']),
                            'measure', case, str(a.seed), str(count)], stem))
                        check_row(row, case, a.seed, count)
                        row.update(cohort=config['cohort'], variant='B', block=block, slot=slot,
                                   label=label, binary_sha256=config[which + '_sha256'])
                        memory_by_binary.setdefault(which, set()).add(row['owned_bytes'])
                        require(len(memory_by_binary[which]) == 1,
                                'Memory changes between identical fresh-seed processes')
                        if not qualification and which == 'baseline':
                            require(row['owned_bytes'] == aa_memory[case],
                                    'Control memory differs from fresh qualification')
                        with (out / ('aa.jsonl' if qualification else 'comparison.jsonl')).open('a') as f:
                            f.write(json.dumps(row) + '\n')
                        rr.append(row)
                        allrows.append(row)
                        print(stem, flush=True)
                    blocks.append(block_result(rr, case, block, qualification, config['platform']))
                if qualification:
                    aa_memory[case] = next(iter(memory_by_binary['baseline']))
            passed = all(b['passed'] for b in blocks)
            report = dict(rows=len(allrows), blocks=blocks, finished=time.time())
            report['pass'] = passed
            write(out / ('qualification.json' if qualification else 'comparison-analysis.json'), report)
            if not passed:
                write(out / 'confirmation-result.json', dict(status='PARK' if qualification else 'FAIL',
                      stage=action, comparison_executed=not qualification, source_adoption=False))
                return
        write(out / 'confirmation-result.json', dict(status='PASS', stage='compare',
              comparison_executed=True, source_adoption=False))
    except Exception as error:
        write(out / 'confirmation-result.json', dict(status='ERROR', phase_consumed=True,
              error_type=type(error).__name__, error=str(error), source_adoption=False))
        raise


if __name__ == '__main__':
    main()
