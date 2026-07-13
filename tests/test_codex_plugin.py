import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAMES = {
    "setup-cn",
    "resume-audit",
    "job-import",
    "job-fit-cn",
    "apply-cn",
}


class PluginManifestTests(unittest.TestCase):
    def test_manifest_has_required_fields(self):
        manifest_path = ROOT / ".codex-plugin" / "plugin.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

        self.assertEqual(manifest["name"], "codex-job-search-cn")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(manifest["license"], "MIT")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(manifest["repository"], "https://github.com/xxzzzzy/codex-job-search-cn")
        self.assertIn("displayName", manifest["interface"])
        self.assertLessEqual(len(manifest["interface"]["defaultPrompt"]), 3)


class SkillStructureTests(unittest.TestCase):
    def test_all_expected_skills_are_complete(self):
        discovered = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(discovered, SKILL_NAMES)

        for name in SKILL_NAMES:
            skill_path = ROOT / "skills" / name / "SKILL.md"
            content = skill_path.read_text(encoding="utf-8")
            self.assertNotIn("[TODO:", content)
            self.assertTrue(content.startswith("---\n"))
            self.assertRegex(content, rf"\nname:\s*{re.escape(name)}\n")
            self.assertRegex(content, r"\ndescription:\s*\S")
            self.assertTrue((skill_path.parent / "agents" / "openai.yaml").exists())

    def test_apply_keeps_review_notes_out_of_submission_materials(self):
        content = (ROOT / "skills" / "apply-cn" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("outputs/application-review-<job-id>.md", content)
        self.assertIn("private/claims/<claim-id>.json", content)
        self.assertIn("Do not place warnings", content)


class SchemaTests(unittest.TestCase):
    def test_core_schemas_are_valid_json_objects(self):
        expected = {
            "candidate.schema.json",
            "evidence.schema.json",
            "claim.schema.json",
            "job.schema.json",
            "application.schema.json",
        }
        schema_dir = ROOT / "schemas"
        self.assertEqual({path.name for path in schema_dir.glob("*.json")}, expected)

        for path in schema_dir.glob("*.json"):
            schema = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertEqual(schema["type"], "object")
            self.assertTrue(schema["required"])


class PrivacyDefaultsTests(unittest.TestCase):
    def test_personal_directories_are_ignored(self):
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("private/", gitignore)
        self.assertIn("outputs/", gitignore)
        self.assertIn("*github-token*", gitignore)


class ReadmeTests(unittest.TestCase):
    def test_codex_usage_is_distinct_from_upstream_claude_commands(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## 在 Codex 中使用", readme)
        self.assertIn("$setup-cn", readme)
        self.assertIn("不是本插件", readme)


if __name__ == "__main__":
    unittest.main()
