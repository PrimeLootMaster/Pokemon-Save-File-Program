"""Synthetic fixtures only: no user saves or Pokémon binaries required."""

import hashlib
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from zipfile import ZipFile
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from audit_frozen_reference import audit, main  # noqa: E402


class FrozenReferenceAuditTests(unittest.TestCase):
    def make_fixture(self, base, manifest_hash=None, malicious_path=False):
        path = base / "test.zip"
        body = b"<!doctype html><title>synthetic</title>"
        actual = hashlib.sha256(body).hexdigest()
        prefix = "reference/01_MODERN_V35_REFERENCE/"
        with ZipFile(path, "w") as z:
            z.writestr(prefix + "example.html", body)
            z.writestr(prefix + "PokemonSaveFileHacks-v35-Verification.json", json.dumps({
                "runtime": "synthetic fake report",
                "results": [{"branch": 1, "id": "demo", "file": "example.html", "sha256": manifest_hash or actual, "ok": True}]
            }))
            if malicious_path:
                z.writestr("../untrusted.sav", b"not a real save")
        return path

    def test_matching_hash_is_metadata_only(self):
        with TemporaryDirectory() as d:
            result = audit(self.make_fixture(Path(d)))
            self.assertEqual(result["issues"], [])
            self.assertTrue(result["results"][0]["manifest_sha256_match"])
            self.assertIs(result["independent_runtime_tests_performed"], False)
            self.assertIsNone(result["public_upload_safe"])

    def test_hash_mismatch_returns_nonzero(self):
        with TemporaryDirectory() as d:
            path = self.make_fixture(Path(d), manifest_hash="0" * 64)
            self.assertEqual(main([str(path)]), 1)

    def test_unsafe_zip_path_flagged(self):
        with TemporaryDirectory() as d:
            result = audit(self.make_fixture(Path(d), malicious_path=True))
            self.assertTrue(any("Unsafe ZIP path" in s for s in result["issues"]))
            self.assertEqual(result["flagged_sensitive_names"], ["../untrusted.sav"])


if __name__ == "__main__":
    unittest.main()
