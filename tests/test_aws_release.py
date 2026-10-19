"""Release auditor must inspect systemd's nested slice, including descendants."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('release_audit', Path(__file__).resolve().parents[1] / 'scripts/audit-aws-release.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
GROUP = '/bplus.slice/bplus-night.slice/bplus-night-20261019.slice'


class ReleaseAuditTests(unittest.TestCase):
    def inspect(self, *, active=False, exists=True, children=False, group=GROUP,
                query_fails=False, walk_fails=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            group_root = root / 'cgroup' / GROUP.lstrip('/')
            if exists:
                group_root.mkdir(parents=True)
                (group_root / 'cgroup.procs').write_text('')
                if children:
                    (group_root / 'job.service').mkdir()
                    (group_root / 'job.service/cgroup.procs').write_text('101\n102\n')
            (root / 'LEASE-RELEASED').write_text('2026-10-19T08:00:00+00:00\n')
            (root / 'released-status.txt').write_text('coordinator RUNNING pid 42\n')
            original_path = Path

            def map_path(*args):
                value = str(original_path(*args))
                if value.startswith('/sys/fs/cgroup'):
                    return original_path(str(root / 'cgroup') + value[len('/sys/fs/cgroup'):])
                if value == '/proc/42':
                    return root
                return original_path(*args)

            def command(args, **kwargs):
                if 'supervisorctl' in args:
                    value = 'coordinator RUNNING pid 42, uptime 1 minute'
                elif '--property=ActiveState' in args:
                    value = 'active' if active else 'inactive'
                elif '--property=ControlGroup' in args:
                    return subprocess.CompletedProcess(args, 1 if query_fails else 0, group, '')
                else:
                    value = ''
                return subprocess.CompletedProcess(args, 0, value, '')

            def broken_walk(path, onerror):
                onerror(PermissionError('denied'))
                return iter(())

            output = io.StringIO()
            with patch('pathlib.Path', side_effect=map_path), patch('subprocess.run', side_effect=command), patch('sys.argv', ['audit', str(root)]), contextlib.redirect_stdout(output):
                if walk_fails:
                    with patch('os.walk', side_effect=broken_walk):
                        exec(MODULE.REMOTE, {})
                else:
                    exec(MODULE.REMOTE, {})
            return json.loads(output.getvalue())

    def test_descendant_processes_are_not_silently_missed(self):
        record = self.inspect(active=True, children=True)
        self.assertEqual(record['owned_cgroup_process_count'], 2)
        self.assertEqual(record['inspection_errors'], [])

    def test_removed_inactive_group_is_empty(self):
        record = self.inspect(exists=False, group='')
        self.assertEqual(record['owned_cgroup_process_count'], 0)
        self.assertEqual(record['inspection_errors'], [])

    def test_missing_active_group_fails(self):
        self.assertTrue(self.inspect(active=True, exists=False)['inspection_errors'])

    def test_query_failure_fails(self):
        self.assertTrue(self.inspect(query_fails=True)['inspection_errors'])

    def test_unexpected_path_fails(self):
        self.assertTrue(self.inspect(group='/wrong.slice')['inspection_errors'])

    def test_enumeration_failure_fails(self):
        self.assertTrue(self.inspect(walk_fails=True)['inspection_errors'])


if __name__ == '__main__':
    unittest.main()
