import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InstallationTests(unittest.TestCase):
    def test_documented_copy_on_fresh_and_existing_installs(self):
        readme = (ROOT / 'README.md').read_text()
        section = readme.split('**Claude Code (direct):**', 1)[1]
        block = re.search(r'```bash\n(.*?)```', section, re.S).group(1)
        # Stage the clone locally so this test needs no network.
        commands = '\n'.join(block.strip().splitlines()[1:])
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp)
            shutil.copytree(ROOT / 'skills', work / 'gtm-cofounder/skills')
            home = work / 'home'
            home.mkdir()
            env = dict(os.environ, HOME=str(home))
            installed = home / '.claude/skills'
            for existing in (False, True):
                subprocess.run(['sh', '-eu', '-c', commands], cwd=work,
                               env=env, check=True)
                for source in (ROOT / 'skills').rglob('*'):
                    if source.is_file():
                        target = installed / source.relative_to(ROOT / 'skills')
                        self.assertEqual(source.read_bytes(), target.read_bytes())
                if existing:
                    self.assertEqual((installed / 'unrelated/SKILL.md').read_text(),
                                     'Keep this skill')
                else:
                    (installed / 'unrelated').mkdir()
                    (installed / 'unrelated/SKILL.md').write_text('Keep this skill')

    def test_onboarding_templates_are_bundled(self):
        for skill in ('00-start-here', '01-strategy-and-roadmap'):
            folder = ROOT / 'skills' / skill
            links = re.findall(r'\]\((assets/[^)]+\.template\.md)\)',
                               (folder / 'SKILL.md').read_text())
            self.assertEqual(len(links), 1)
            self.assertTrue((folder / links[0]).is_file())


if __name__ == '__main__':
    unittest.main()
