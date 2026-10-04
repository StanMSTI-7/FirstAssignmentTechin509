"""Additional checks revealed after role rotation."""
import tempfile
import unittest
from pathlib import Path
import shutil
import json

from search import Library


class RevealChecks(unittest.TestCase):
    def setUp(self):
        self.fixture = Path(__file__).parent / "data" / "documents.json"

    def test_negative_limit(self):
        library = Library(self.fixture)
        self.assertEqual(library.search("password", limit=-1), [])
        self.assertEqual(library.search("password", limit=-5), [])

    def test_file_deletion_survival(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir) / "documents.json"
            shutil.copy(self.fixture, tmp_path)
            library = Library(tmp_path)
            # delete the temporary copy after construction
            tmp_path.unlink()
            self.assertTrue(library.search("password"))
            # second search should still work
            self.assertTrue(library.search("vacation"))

    def test_preserve_input_order(self):
        library = Library(self.fixture)
        results = library.search("password")
        sources = [r["source"] for r in results]
        self.assertEqual(sources, ["it.md", "security.md"])

    def test_new_library_loads_updated_data(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir) / "documents.json"
            shutil.copy(self.fixture, tmp_path)
            library1 = Library(tmp_path)
            # overwrite with a new document
            new_docs = [{"source": "new.md", "text": "brand new content about passwords"}]
            tmp_path.write_text(json.dumps(new_docs), encoding="utf-8")
            library2 = Library(tmp_path)
            self.assertEqual(library1.search("new"), [])
            self.assertEqual(library2.search("new"), new_docs)

    def test_result_fields_preserved(self):
        library = Library(self.fixture)
        result = library.search("vacation", limit=1)[0]
        self.assertIn("source", result)
        self.assertIn("text", result)
        self.assertEqual(result["source"], "leave.md")


if __name__ == "__main__":
    unittest.main()
