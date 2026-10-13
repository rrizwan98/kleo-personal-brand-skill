import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "kleo-personal-brand" / "scripts" / "init_client.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("init_client", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ClientWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def create(self, client_id="maya-flowdesk", name="Maya Reed", url="https://www.linkedin.com/in/maya-reed/"):
        return module.ensure_client(self.root, client_id, name, url)

    def test_creates_complete_workspace_with_unknown_defaults(self):
        result = self.create()
        client = Path(result["path"])
        data = json.loads((client / "client.json").read_text())
        self.assertEqual(data["client_id"], "maya-flowdesk")
        self.assertEqual(data["authorization"], [])
        self.assertIsNone(data["preferences"]["timezone"])
        self.assertEqual(data["voice"]["confidence"], "provisional")
        self.assertEqual(len(list(client.glob("*.jsonl"))), 6)
        self.assertTrue((client / "drafts").is_dir())

    def test_repeat_initialization_preserves_content_byte_for_byte(self):
        client = Path(self.create()["path"])
        memory = client / "memory.jsonl"
        memory.write_text('{"rule":"No emojis"}\n')
        before = {p.name: p.read_bytes() for p in client.iterdir() if p.is_file()}
        self.assertEqual(self.create()["status"], "existing")
        self.assertEqual(before, {p.name: p.read_bytes() for p in client.iterdir() if p.is_file()})

    def test_clients_have_separate_state(self):
        first = Path(self.create()["path"])
        second = Path(self.create("omar-studio", "Omar Ali", "https://linkedin.com/in/omar-ali")["path"])
        (first / "memory.jsonl").write_text("client A only")
        self.assertEqual((second / "memory.jsonl").read_text(), "")

    def test_identity_mismatch_does_not_modify_state(self):
        path = Path(self.create()["path"]) / "client.json"
        before = path.read_bytes()
        with self.assertRaises(ValueError):
            self.create(name="Another Author")
        self.assertEqual(before, path.read_bytes())

    def test_url_mismatch_rejected(self):
        self.create()
        with self.assertRaises(ValueError):
            self.create(url="https://linkedin.com/in/someone-else")

    def test_unknown_url_not_silently_replaced(self):
        self.create(url=None)
        with self.assertRaises(ValueError):
            self.create()

    def test_url_normalization_supports_repeat_use(self):
        self.create()
        self.assertEqual(self.create(url="https://linkedin.com/in/maya-reed?trk=sample")["status"], "existing")

    def test_traversal_and_reserved_ids_rejected(self):
        for slug in ("../outside", "a/b", "a\\b", "CON", "con", "nul", "lpt1", "", "-name", "a" * 65):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                self.create(client_id=slug)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_credential_and_non_http_urls_rejected(self):
        for url in ("file:///tmp/x", "https://user:secret@example.com", "javascript:alert(1)", "relative/path"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                self.create(url=url)

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError):
            self.create(name=" ")

    def test_existing_nonclient_directory_rejected(self):
        (self.root / "maya-flowdesk").mkdir()
        with self.assertRaises(ValueError):
            self.create()

    def test_corrupt_manifest_not_reset(self):
        path = Path(self.create()["path"]) / "client.json"
        path.write_text("{broken json")
        with self.assertRaises(ValueError):
            self.create()
        self.assertEqual(path.read_text(), "{broken json")

    def test_mismatched_manifest_client_id_rejected(self):
        path = Path(self.create()["path"]) / "client.json"
        data = json.loads(path.read_text())
        data["client_id"] = "other-client"
        path.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            self.create()

    def test_skill_directory_cannot_store_client_data(self):
        with self.assertRaises(ValueError):
            module.ensure_client(SCRIPT.parent.parent / "clients", "example", "Example")


if __name__ == "__main__":
    unittest.main(verbosity=2)
