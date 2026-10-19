"""Exercise host isolation, real Git publication and worker acknowledgements."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    'night_sync', Path(__file__).resolve().parents[1] / 'scripts/sync-night-campaign.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve() / 'checkout'
        self.root.mkdir()
        self.remote = Path(self.tmp.name) / 'remote.git'
        subprocess.run(['git', 'init', '--bare', '-q', str(self.remote)], check=True)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Publication Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.config = dict(worktree='.', host_label='apple-m6-mini',
            campaign_dir='experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/test',
            runtime_dir='scratch/runtime', branch='exploration/apple-m6-mini-test')
        for value in ['README.md', 'experiments/EXPERIMENTS.md', 'experiments/SUMMARY.md',
                      'experiments/NEXT-STEPS.md', '.workspace-memory/MEMORY.md',
                      '.workspace-memory/LIVE-STATUS.md', '.workspace-memory/handoff.md',
                      'src/zset_btree.c', 'bench/new.c', 'compat/server.h',
                      'compat/standalone.c', self.config['campaign_dir']+'/STATUS.md']:
            path = self.root / value
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('initial\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'initial')
        self.git('switch', '-qc', self.config['branch'])
        self.git('remote', 'add', 'origin', str(self.remote))
        self.root_patch = patch.object(sync, 'ROOT', self.root)
        self.root_patch.start()

    def tearDown(self):
        self.root_patch.stop()
        self.tmp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, text=True).strip()

    def test_real_m6_push_includes_harness_and_memory_but_preserves_source_edit(self):
        (self.root/self.config['campaign_dir']/'STATUS.md').write_text('rank running\n')
        (self.root/'bench/new.c').write_text('new harness\n')
        (self.root/'.workspace-memory/LIVE-STATUS.md').write_text('rank running\n')
        (self.root/'src/zset_btree.c').write_text('uncommitted source\n')
        result = sync.publish(self.config, 1, ['bench/new.c'])
        self.assertIn('Published', result)
        head = self.git('rev-parse', 'HEAD')
        remote = subprocess.check_output(['git', '--git-dir', str(self.remote),
            'rev-parse', self.config['branch']], text=True).strip()
        self.assertEqual(head, remote)
        self.assertEqual(self.git('show', 'HEAD:src/zset_btree.c'), 'initial')
        self.assertEqual(self.git('show', 'HEAD:bench/new.c'), 'new harness')
        self.assertEqual(self.git('show', 'HEAD:.workspace-memory/LIVE-STATUS.md'), 'rank running')

    def test_host_branch_and_path_isolation(self):
        for changes in [dict(host_label='apple-m1'), dict(branch='main'),
                        dict(campaign_dir=self.config['campaign_dir']+'/../../../../elsewhere'),
                        dict(runtime_dir='../outside')]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                sync.validate_config(dict(self.config, **changes))
        for path in ['src/zset_btree.c', '../outside', '/tmp/outside',
                     'tests/upstream.c', 'experiments/EXP-008/RESULTS.md',
                     'compat/other.c', 'compat', 'compat/../src/zset_btree.c']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                sync.publication_paths(self.config, [path])

    def test_explicit_adapter_fix_publishes_without_staging_tree_or_other_adapter_files(self):
        (self.root/'compat/server.h').write_text('truthful panic declaration\n')
        (self.root/'compat/standalone.c').write_text('truthful panic definition\n')
        (self.root/'compat/other.c').write_text('unrelated adapter work\n')
        (self.root/'src/zset_btree.c').write_text('uncommitted source\n')
        sync.publish(self.config, 1, ['compat/server.h', 'compat/standalone.c'])
        self.assertEqual(self.git('show', 'HEAD:compat/server.h'), 'truthful panic declaration')
        self.assertEqual(self.git('show', 'HEAD:compat/standalone.c'), 'truthful panic definition')
        self.assertEqual(self.git('show', 'HEAD:src/zset_btree.c'), 'initial')
        self.assertEqual(self.git('ls-tree', '--name-only', 'HEAD', 'compat/other.c'), '')

    def test_private_path_and_unrelated_staging_refused(self):
        status = self.root/self.config['campaign_dir']/'STATUS.md'
        status.write_text('/' + 'Users/private/path\n')
        with self.assertRaisesRegex(RuntimeError, 'Public-evidence'):
            sync.publish(self.config, 1)
        status.write_text('safe\n')
        (self.root/'src/zset_btree.c').write_text('other writer\n')
        self.git('add', 'src/zset_btree.c')
        with self.assertRaisesRegex(RuntimeError, 'pre-staged'):
            sync.publish(self.config, 1)

    def test_all_aws_hosts_publish_to_their_own_branch(self):
        for host in ('aws-arm', 'aws-intel', 'aws-amd'):
            with self.subTest(host=host):
                config = dict(self.config, host_label=host,
                    campaign_dir=f'experiments/NIGHT-EXPLORATION-001/runs/{host}/test',
                    branch=f'exploration/{host}-test')
                self.git('switch', '-qc', config['branch'])
                evidence = self.root / config['campaign_dir']
                evidence.mkdir(parents=True)
                (evidence / 'STATUS.md').write_text('complete\n')
                self.assertIn('Published', sync.publish(config, 1))
                remote = subprocess.check_output(['git', '--git-dir', str(self.remote),
                    'rev-parse', config['branch']], text=True).strip()
                self.assertEqual(self.git('rev-parse', 'HEAD'), remote)

    def test_linux_paths_and_credentials_refused_in_evidence_and_requested_files(self):
        needles = ('/home/' + 'ubuntu/', '/home/' + 'fco/', '.' + 'pem',
                   'gh' + 'o_', 'github' + '_pat_', 'Authorization' + ': Bearer')
        for value in (self.config['campaign_dir'] + '/STATUS.md', 'bench/new.c'):
            for needle in needles:
                with self.subTest(path=value, needle=needle):
                    path = self.root / value
                    path.write_text(needle + 'synthetic\n')
                    with self.assertRaisesRegex(RuntimeError, 'Public-evidence'):
                        sync.publish(self.config, 1, ['bench/new.c'])
                    path.write_text('safe\n')

    def test_request_acknowledges_exact_revision_after_successful_push(self):
        runtime = self.root/self.config['runtime_dir']
        runtime.mkdir(parents=True)
        (runtime/'status.json').write_text(json.dumps(dict(status='deadline_reached', rounds=[])))
        (runtime/'publish-request.json').write_text(json.dumps(dict(id='rank-freeze-1', paths=['bench/new.c'])))
        config_path = self.root/'scratch/config.json'
        config_path.write_text(json.dumps(self.config))
        with patch.object(sys, 'argv', ['sync', '--config', 'scratch/config.json']):
            sync.main()
        ack = json.loads((runtime/'publish-ack.json').read_text())
        summary = json.loads(self.git('show', 'HEAD:' + self.config['campaign_dir'] + '/RUNTIME-SUMMARY.json'))
        self.assertEqual(summary['status'], 'deadline_reached')
        self.assertEqual(summary['configured_backend'], 'unknown')
        self.assertIsNone(summary['cost_usd'])
        self.assertEqual(ack['request_id'], 'rank-freeze-1')
        self.assertEqual(ack['status'], 'ok')
        self.assertIn(self.git('rev-parse', '--short', 'HEAD'), ack['publication'])


if __name__ == '__main__':
    unittest.main()
