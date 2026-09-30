"""Release-integrity tests; these do not test model quality."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "tools" / "check_repo.py"


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        shutil.copytree(
            ROOT, self.repo,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "dist", ".venv"),
        )

    def check(self):
        return subprocess.run(
            [sys.executable, str(CHECKER), "--root", str(self.repo)],
            text=True, capture_output=True, check=False,
        )

    def test_valid_release_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_core_is_reported(self):
        (self.repo / "skills/dialectic/SKILL.md").unlink()
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing required file: skills/dialectic/SKILL.md", result.stdout)

    def test_dead_relative_link_is_reported(self):
        with (self.repo / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Missing](docs/does-not-exist.md)\n")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Broken local link", result.stdout)

    def test_altered_raw_output_is_reported(self):
        path = self.repo / "evals/runs/2026-09-29/baseline-1.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nAltered.\n", encoding="utf-8")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Checksum mismatch", result.stdout)

    def test_missing_rubric_judgment_is_reported(self):
        path = self.repo / "evals/runs/2026-09-29/manifest.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        del manifest["runs"][0]["checks"]["K6"]
        path.write_text(json.dumps(manifest), encoding="utf-8")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Judgment keys do not match case criteria", result.stdout)

    def test_unknown_rubric_judgment_is_reported(self):
        path = self.repo / "evals/runs/2026-09-29/manifest.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["runs"][0]["checks"]["nonexistent_rubric_check"] = True
        path.write_text(json.dumps(manifest), encoding="utf-8")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Judgment keys do not match case criteria", result.stdout)

    def test_duplicate_case_id_is_reported(self):
        path = self.repo / "evals/cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        cases.append(cases[0])
        path.write_text(json.dumps(cases), encoding="utf-8")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate case ID", result.stdout)


if __name__ == "__main__":
    unittest.main()
