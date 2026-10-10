#!/usr/bin/env python3
"""Non-destructive SHA-256 verification of a Pokémon frozen-reference ZIP.

Only prints archive metadata, filenames and hashes. It never extracts files.
The report's `ok` fields describe HISTORICAL claimed testing; this script
validates bytes and manifest linkage, not feature behavior or licensing.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
from zipfile import ZipFile, BadZipFile

FAMILY = "/01_MODERN_V35_REFERENCE/"
VERIFY_SUFFIX = FAMILY + "PokemonSaveFileHacks-v35-Verification.json"
DANGEROUS_SUFFIXES = (".gba", ".nds", ".sav", ".ups", ".psehstate", ".key", ".pem", ".p12")


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _unsafe_name(name: str) -> bool:
    path = PurePosixPath(name)
    return path.is_absolute() or ".." in path.parts or "\\" in name or "\x00" in name


def audit(path: Path) -> dict:
    """Return a deterministic evidence report without extracting the ZIP."""
    with ZipFile(path) as archive:
        names = archive.namelist()
        bad_paths = sorted({name for name in names if _unsafe_name(name)})
        candidates = sorted(name for name in names if FAMILY in name and name.endswith(".html"))
        manifests = [name for name in names if name.endswith(VERIFY_SUFFIX)]
        if len(manifests) != 1:
            raise ValueError(f"Expected one v35 verification manifest, found {len(manifests)}")
        verification = json.loads(archive.read(manifests[0]))
        entries = verification.get("results", [])
        if not isinstance(entries, list):
            raise ValueError("Verification results must be a list")
        seen_names, seen_branches = set(), set()
        results, issues = [], []
        by_filename = {PurePosixPath(name).name: name for name in candidates}
        if len(by_filename) != len(candidates):
            issues.append("Duplicate v35 candidate basenames")
        for item in entries:
            filename = item.get("file", "")
            branch = item.get("branch")
            if filename in seen_names:
                issues.append(f"Repeated verification entry: {filename}")
            seen_names.add(filename)
            if branch in seen_branches:
                issues.append(f"Repeated branch number: {branch}")
            seen_branches.add(branch)
            archive_name = by_filename.get(filename)
            if archive_name is None:
                issues.append(f"Missing candidate in ZIP: {filename}")
                continue
            blob = archive.read(archive_name)
            actual = _digest(blob)
            expected = item.get("sha256", "")
            match = actual == expected
            if not match:
                issues.append(f"SHA-256 mismatch: {filename}")
            results.append({
                "branch": branch,
                "id": item.get("id"),
                "file": filename,
                "size_bytes": len(blob),
                "sha256": actual,
                "manifest_sha256_match": match,
                "historical_test_claim_ok": item.get("ok"),
                "contains_embedded_data_images": b"data:image/" in blob,
            })
        for filename in sorted(set(by_filename) - seen_names):
            issues.append(f"Unlisted v35 candidate: {filename}")
        for name in bad_paths:
            issues.append(f"Unsafe ZIP path: {name}")
        flagged = sorted(name for name in names if name.lower().endswith(DANGEROUS_SUFFIXES)
                         or PurePosixPath(name).name.startswith(".env"))
        results.sort(key=lambda item: (item["branch"] is None, item["branch"] or 0))
        return {
            "archive_name": path.name,
            "archive_sha256": _digest(path.read_bytes()),
            "archive_entries": len(names),
            "v35_reference_count": len(candidates),
            "v35_verified_rows": len(results),
            "historical_runtime_description": verification.get("runtime"),
            "results": results,
            "flagged_sensitive_names": flagged,
            "issues": issues,
            "independent_runtime_tests_performed": False,
            "public_upload_safe": None,
            "notice": "Hash match does not establish authorship, license, privacy or functional correctness; review HTML embedded assets and links before public upload.",
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Original frozen reference ZIP")
    parser.add_argument("--output", type=Path, help="Optional JSON report destination")
    args = parser.parse_args(argv)
    try:
        result = audit(args.archive)
    except (BadZipFile, ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"Audit failed: {exc}", file=sys.stderr)
        return 2
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Wrote audit: {args.output}")
    else:
        print(output)
    return 0 if not result["issues"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
