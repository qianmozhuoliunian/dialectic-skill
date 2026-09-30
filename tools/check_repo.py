#!/usr/bin/env python3
"""Offline checks for this release, using only Python's standard library.

This validates the repository's simple metadata/link conventions and artifact
hashes. It is not a full Markdown/YAML parser, a model eval, or a safety verifier.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

REQUIRED = (
    "README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
    "skills/dialectic/SKILL.md", "skills/dialectic/references/protocol.md",
    "skills/dialectic/agents/openai.yaml", "docs/installation.md", "docs/usage.md",
    "docs/related-work.md", "docs/publishing.zh-CN.md",
    "examples/README.md", "examples/product-idea.md",
    "examples/technical-plan.md", "examples/learning-plan.md",
    "evals/README.md", "evals/results.md", "evals/cases.json",
    "evals/runs/2026-09-29/manifest.json",
    "evals/runs/2026-09-29/input.txt", "evals/runs/2026-09-29/criteria.json",
    "tools/check_repo.py", "tests/test_check_repo.py", ".github/workflows/check.yml",
)


def validate(root):
    root = root.resolve()
    errors = []

    def inside(relative):
        if not isinstance(relative, str) or not relative:
            errors.append("Invalid empty/non-string artifact path")
            return None
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            errors.append("Path escapes repository: " + relative)
            return None
        return path

    def load(relative):
        path = inside(relative)
        if path is None:
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"Cannot read JSON {relative}: {exc}")
            return None

    def check_hash(relative, expected):
        path = inside(relative)
        if path is None:
            return
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            errors.append("Invalid SHA-256: " + str(relative))
            return
        try:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError:
            errors.append("Missing recorded artifact: " + relative)
            return
        if actual != expected:
            errors.append("Checksum mismatch: " + relative)

    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append("Missing required file: " + relative)

    skill = root / "skills/dialectic/SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not match:
            errors.append("Missing skill frontmatter")
        else:
            fields = {}
            for line in match.group(1).splitlines():
                key, separator, value = line.partition(":")
                if not separator or key in fields:
                    errors.append("Invalid/duplicate skill frontmatter key: " + key)
                fields[key] = value.strip()
            if set(fields) != {"name", "description"}:
                errors.append("This release expects name and description frontmatter only")
            if fields.get("name") != skill.parent.name:
                errors.append("Skill name must match its directory")
            if not 1 <= len(fields.get("description", "")) <= 1024:
                errors.append("Skill description must contain 1-1024 characters")
        if len(text.splitlines()) > 500:
            errors.append("Skill core exceeds 500 lines")

    # Check simple inline relative links outside fenced code. External URLs and
    # intra-page anchors are deliberately not checked by this offline command.
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", "__pycache__", ".venv", "dist"} for part in path.parts):
            continue
        body = re.sub(r"(?ms)^\s*```.*?^\s*```[^\n]*$", "", path.read_text(encoding="utf-8"))
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", body):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            linked = (path.parent / unquote(parts.path)).resolve()
            if not linked.is_relative_to(root) or not linked.exists():
                errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")

    cases = load("evals/cases.json")
    case_ids = set()
    criterion_ids = {}
    if isinstance(cases, list) and cases:
        for case in cases:
            if not isinstance(case, dict):
                errors.append("Invalid case object")
                continue
            identifier = case.get("id")
            if not isinstance(identifier, str) or not identifier:
                errors.append("Missing case ID")
                continue
            if identifier in case_ids:
                errors.append("Duplicate case ID: " + identifier)
            case_ids.add(identifier)
            if not isinstance(case.get("input"), str) or not case["input"].strip():
                errors.append("Missing input: " + identifier)
            criteria = case.get("criteria")
            if not isinstance(criteria, list) or not criteria or not all(
                isinstance(item, dict)
                and isinstance(item.get("id"), str) and item["id"].strip()
                and isinstance(item.get("description"), str) and item["description"].strip()
                for item in criteria
            ):
                errors.append("Invalid criteria: " + identifier)
            else:
                ids = {item["id"] for item in criteria}
                if len(ids) != len(criteria):
                    errors.append("Duplicate criterion ID: " + identifier)
                criterion_ids[identifier] = ids
    else:
        errors.append("Cases must be a nonempty list")

    manifest = load("evals/runs/2026-09-29/manifest.json")
    if isinstance(manifest, dict):
        snapshots = manifest.get("skill_files")
        if not isinstance(snapshots, dict) or not snapshots:
            errors.append("Missing skill snapshot hashes")
        else:
            for relative, expected in snapshots.items():
                check_hash(relative, expected)
        runs = manifest.get("runs")
        seen = set()
        if not isinstance(runs, list) or not runs:
            errors.append("Missing recorded runs")
        else:
            for run in runs:
                if not isinstance(run, dict):
                    errors.append("Invalid run record")
                    continue
                identifier = run.get("id")
                if not isinstance(identifier, str) or not identifier:
                    errors.append("Missing run ID")
                    continue
                if identifier in seen:
                    errors.append("Duplicate run ID: " + identifier)
                seen.add(identifier)
                if run.get("case_id") not in case_ids:
                    errors.append("Unknown run case: " + identifier)
                check_hash(run.get("output"), run.get("sha256"))
                checks = run.get("checks")
                if not isinstance(checks, dict) or not checks or not all(
                    type(value) is bool for value in checks.values()
                ):
                    errors.append("Invalid recorded judgments: " + identifier)
                elif set(checks) != criterion_ids.get(run.get("case_id")):
                    errors.append("Judgment keys do not match case criteria: " + identifier)
    else:
        errors.append("Manifest must be an object")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        parser.error("Python 3.10 or newer is required")
    try:
        errors = validate(args.root)
    except (OSError, UnicodeError, ValueError) as exc:
        errors = [f"Cannot inspect repository: {exc}"]
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: required files, skill metadata, local links, cases and recorded artifact hashes")
    print("This does not measure model quality or prove the recorded judgments.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
