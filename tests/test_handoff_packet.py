import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/project-guide/scripts/handoff_packet.py'
SPEC = importlib.util.spec_from_file_location('handoff_packet', SCRIPT)
packet = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(packet)


class HandoffPacketTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name)
        (self.project / 'research.md').write_text('# Retry finding\nEvidence: contract.md\n')
        (self.project / 'contract.md').write_text('Partner GET 429 uses 25 ms ticks.\n')
        self.target = self.project / '.agent-handoff/retry'

    def test_create_verify_and_detect_changes(self):
        self.assertEqual(packet.create(self.project, self.target, 'research.md', ['contract.md'])['files'], 2)
        self.assertEqual((self.project / '.agent-handoff/.gitignore').read_text(), '*\n')
        self.assertIn('retry/analysis.md', (self.project / '.agent-handoff/INDEX.md').read_text())
        self.assertEqual(packet.verify(self.target)['status'], 'passed')
        with self.assertRaises(ValueError):
            packet.create(self.project, self.target, 'research.md', ['contract.md'])
        (self.target / 'evidence/01-contract.md').write_text('changed')
        with self.assertRaises(ValueError):
            packet.verify(self.target)

    def test_missing_outside_and_symbolic_link_sources(self):
        with self.assertRaises(ValueError):
            packet.create(self.project, self.target, 'research.md', ['missing.md'])
        self.assertFalse(self.target.exists())
        outside = self.project.parent / 'handoff-outside.txt'
        outside.write_text('outside')
        self.addCleanup(lambda: outside.unlink(missing_ok=True))
        with self.assertRaises(ValueError):
            packet.create(self.project, self.target, 'research.md', ['../handoff-outside.txt'])
        (self.project / 'alias.md').symlink_to(self.project / 'contract.md')
        with self.assertRaises(ValueError):
            packet.create(self.project, self.target, 'research.md', ['alias.md'])

    def test_git_ignores_packet_and_tracked_area_is_rejected(self):
        subprocess.run(['git', 'init', '-q', str(self.project)], check=True)
        packet.create(self.project, self.target, 'research.md', ['contract.md'])
        untracked = subprocess.check_output(['git', '-C', str(self.project), 'status', '--porcelain'], text=True)
        self.assertNotIn('.agent-handoff', untracked)
        subprocess.run(['git', '-C', str(self.project), 'add', '-f', '.agent-handoff/INDEX.md'], check=True)
        with self.assertRaises(ValueError):
            packet.create(self.project, self.project / '.agent-handoff/another', 'research.md', [])

    def test_symbolic_link_packet_area_is_rejected(self):
        other = self.project / 'other'
        other.mkdir()
        (self.project / '.agent-handoff').symlink_to(other, target_is_directory=True)
        with self.assertRaises(ValueError):
            packet.create(self.project, self.target, 'research.md', ['contract.md'])
        with self.assertRaises(ValueError):
            packet.verify(self.target)

    def test_cli_validates_identifier_and_existing_packet(self):
        create = subprocess.run(['python3', str(SCRIPT), '--project', str(self.project), '--id', 'api-retry',
                                 '--record', 'research.md', '--source', 'contract.md'], capture_output=True, text=True)
        self.assertEqual(create.returncode, 0, create.stderr)
        self.assertEqual(json.loads(create.stdout)['files'], 2)
        verify = subprocess.run(['python3', str(SCRIPT), '--project', str(self.project), '--id', 'api-retry',
                                 '--verify'], capture_output=True, text=True)
        self.assertEqual(verify.returncode, 0, verify.stderr)
        invalid = subprocess.run(['python3', str(SCRIPT), '--project', str(self.project), '--id', '../bad',
                                  '--verify'], capture_output=True, text=True)
        self.assertNotEqual(invalid.returncode, 0)


if __name__ == '__main__':
    unittest.main()
