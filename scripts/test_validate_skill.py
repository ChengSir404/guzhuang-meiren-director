#!/usr/bin/env python3
"""Regression checks for import metadata; uses only the standard library."""

import re
import runpy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = runpy.run_path(str(ROOT / "scripts" / "validate_skill.py"))
VALIDATE = VALIDATOR["validate_frontmatter"]
SOURCE = (ROOT / "SKILL.md").read_text(encoding="utf-8")
FIELDS = ("version", "display_name", "display_name_en", "description_zh", "description_en")


def without_field(text, field):
    header, body = text.split("\n---\n", 1)
    header = re.sub(r"^" + field + r":.*\n?", "", header, flags=re.MULTILINE)
    return header.rstrip("\n") + "\n---\n" + body


class ImportMetadataTests(unittest.TestCase):
    def test_current_package(self):
        self.assertEqual(VALIDATE(SOURCE), ROOT.name)

    def test_each_required_field_is_rejected_when_missing(self):
        for field in FIELDS:
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, field):
                VALIDATE(without_field(SOURCE, field))

    def test_empty_required_fields_are_rejected(self):
        for field in FIELDS:
            for value in ('""', '"   "', "null"):
                candidate = re.sub(r"^" + field + r":.*$", field + ": " + value, SOURCE, flags=re.MULTILINE)
                with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, field):
                    VALIDATE(candidate)

    def test_invalid_versions_are_rejected(self):
        for version in ("1", "1.0", "v1.0.0", "01.0.0", "1.0.0.0", "-1.0.0"):
            candidate = re.sub(r"^version:.*$", 'version: "' + version + '"', SOURCE, flags=re.MULTILINE)
            with self.subTest(version=version), self.assertRaisesRegex(ValueError, "version"):
                VALIDATE(candidate)

    def test_metadata_in_body_does_not_replace_frontmatter(self):
        candidate = without_field(SOURCE, "display_name_en") + "\ndisplay_name_en: English title\n"
        with self.assertRaisesRegex(ValueError, "display_name_en"):
            VALIDATE(candidate)

    def test_duplicate_keys_are_rejected(self):
        candidate = SOURCE.replace("\n---\n", '\nversion: "1.0.0"\n---\n', 1)
        with self.assertRaisesRegex(ValueError, "duplicate frontmatter key"):
            VALIDATE(candidate)


if __name__ == "__main__":
    unittest.main()
