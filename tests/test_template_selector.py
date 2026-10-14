"""Regression tests for evidence eligibility, bounded retrieval and packaged provenance."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "kleo-personal-brand" / "scripts" / "select_template.py"
SPEC = importlib.util.spec_from_file_location("template_selector", SCRIPT)
SELECTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SELECTOR)


class TemplateSelectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library, cls.examples = SELECTOR.load_library()

    def select(self, **overrides):
        args = dict(goal="education", audience="operator", pillar="operations",
                    evidence=["process", "product"], limit=3)
        args.update(overrides)
        return SELECTOR.shortlist(self.library, self.examples, **args)

    def test_supported_founder_brief_returns_applicable_bounded_cards(self):
        result = self.select()
        self.assertEqual(result["status"], "shortlist")
        self.assertLessEqual(len(result["candidates"]), 3)
        for item in result["candidates"]:
            self.assertLessEqual(set(item["template"]["required_evidence"]), {"process", "product"})
            self.assertIn("education", item["template"]["goals"])
            self.assertTrue(item["reasons"])

    def test_no_evidence_yields_empty_result_not_fake_proof(self):
        result = self.select(evidence=[])
        self.assertEqual(result["status"], "no_eligible_template")
        self.assertEqual(result["candidates"], [])
        self.assertTrue(result["blocked_for_evidence"])
        self.assertTrue(result["fallback"])

    def test_external_research_does_not_unlock_client_case_results(self):
        result = self.select(goal="authority", evidence=["research", "process", "reasoning"], limit=5)
        self.assertFalse(any("results" in c["template"]["required_evidence"] for c in result["candidates"]))
        self.assertTrue(any("results" in c["missing_evidence"] for c in result["blocked_for_evidence"]))

    def test_result_case_becomes_eligible_with_required_client_evidence(self):
        result = self.select(goal="authority", evidence=["results", "process"], limit=5)
        self.assertTrue(any("results" in c["template"]["required_evidence"] for c in result["candidates"]))

    def test_story_templates_require_the_clients_story(self):
        result = self.select(goal="trust", evidence=["decision", "product"], limit=5)
        self.assertFalse(any("personal_story" in c["template"]["required_evidence"] for c in result["candidates"]))

    def test_reader_fit_beats_unmatched_audience(self):
        result = self.select(goal="demand", audience="agency_owner", pillar="customer_experience",
                             evidence=["offer", "process"], limit=5)
        first = result["candidates"][0]["template"]
        self.assertIn("agency_owner", first["audiences"])
        self.assertIn("customer_experience", first["pillars"])

    def test_recent_template_and_opening_lower_rank_without_changing_eligibility(self):
        initial = self.select(limit=5)
        first = initial["candidates"][0]
        repeated = self.select(recent=[first["id"]], recent_openings=[first["template"]["opening_type"]], limit=5)
        self.assertEqual(initial["eligible_count"], repeated["eligible_count"])
        self.assertNotEqual(first["id"], repeated["candidates"][0]["id"])
        item = next(c for c in repeated["candidates"] if c["id"] == first["id"])
        self.assertLess(item["tag_fit_score"], first["tag_fit_score"])

    def test_recent_penalties_never_relax_evidence_gate(self):
        result = self.select(goal="authority", evidence=[], recent=["T17"], recent_openings=["result"])
        self.assertEqual(result["candidates"], [])

    def test_bad_tags_are_explicit_errors(self):
        for kwargs in ({"goal": "viral"}, {"audience": "celeb"}, {"pillar": "unknown"},
                       {"evidence": ["assumed_revenue"]}, {"recent": ["T404"]},
                       {"recent_openings": ["invented"]}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.select(**kwargs)

    def test_invalid_limits_fail_and_ties_are_repeatable(self):
        for limit in (0, 6):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                self.select(limit=limit)
        self.assertEqual(self.select(), self.select())

    def test_references_have_provenance_without_copied_posts_or_claimed_performance(self):
        self.assertEqual(len(self.library["templates"]), 40)
        self.assertEqual(len(self.examples), 24)
        self.assertEqual(len({e["author"] for e in self.examples.values()}), 8)
        self.assertEqual(len({e["url"] for e in self.examples.values()}), 24)
        for card in self.library["templates"]:
            self.assertEqual(card["origin"], "original_project_authored")
            self.assertEqual(card["performance_status"], "not_empirically_validated")
        for example in self.examples.values():
            self.assertTrue(example["url"].startswith("https://www.linkedin.com/posts/"))
            self.assertEqual(example["observed_on"], "2026-10-14")
            self.assertTrue(example["limitations"])
            self.assertIsNone(example["quoted_text"])
            self.assertIsNone(example["metrics"])
            self.assertFalse(example["verification"]["performance_verified"])
            self.assertFalse(example["verification"]["kleo_authorship_verified"])
            self.assertNotIn("body", example)

    def test_cli_works_outside_repository_and_returns_json(self):
        with tempfile.TemporaryDirectory() as folder:
            result = subprocess.run([sys.executable, str(SCRIPT), "--goal", "education", "--evidence", "process"],
                                    cwd=folder, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["status"], "shortlist")
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_cli_invalid_input_reports_failure(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--goal", "viral"],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Unknown goal", result.stderr)

    def test_malformed_library_does_not_silently_drop_missing_references(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            modified = json.loads(json.dumps(self.library))
            modified["templates"][0]["example_ids"] = ["E404"]
            (root / "templates.json").write_text(json.dumps(modified), encoding="utf-8")
            (root / "examples.json").write_text(json.dumps({"schema_version": 1, "library_version": "1.1.0", "examples": list(self.examples.values())}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Unknown example"):
                SELECTOR.load_library(root)


if __name__ == "__main__":
    unittest.main()
