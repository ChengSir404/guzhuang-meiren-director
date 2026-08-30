#!/usr/bin/env python3
"""Validate the public skill package without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
OPENAI_YAML = ROOT / "agents" / "openai.yaml"
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
NOISE_NAMES = {".DS_Store", "__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache"}
NOISE_SUFFIXES = {".pyc", ".log"}
OBSOLETE_DEFAULT_RATIO_PHRASES = {
    "默认横向 9:6",
    "横向 9:6（3:2）",
    "默认 4:5",
    "默认横向 16:9",
}


def fail(message: str) -> None:
    raise ValueError(message)


def parse_flat_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter format is invalid")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            fail(f"unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in values:
            fail(f"duplicate frontmatter key: {key}")
        values[key] = value
    return values


def validate_frontmatter(skill_text: str) -> str:
    frontmatter = parse_flat_frontmatter(skill_text)
    extra = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    if extra:
        fail(f"unexpected frontmatter keys: {', '.join(sorted(extra))}")

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("skill name must use lowercase hyphen-case")
    if len(name) > 64:
        fail("skill name exceeds 64 characters")
    if name != ROOT.name:
        fail(f"skill name {name!r} does not match folder {ROOT.name!r}")
    if not description or len(description) > 1024:
        fail("description must contain 1-1024 characters")
    if "<" in description or ">" in description:
        fail("description cannot contain angle brackets")
    return name


def validate_local_links() -> int:
    checked = 0
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    root = ROOT.resolve()
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_text = target.split("#", 1)[0]
            if not path_text:
                continue
            checked += 1
            resolved = (markdown.parent / path_text).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                fail(f"local link escapes repository root in {markdown.relative_to(ROOT)}: {target}")
            if not resolved.exists():
                fail(f"broken local link in {markdown.relative_to(ROOT)}: {target}")
    return checked


def validate_ui_metadata(name: str) -> None:
    if not OPENAI_YAML.is_file():
        fail("agents/openai.yaml is missing")
    text = OPENAI_YAML.read_text(encoding="utf-8")
    for key in ("display_name:", "short_description:", "default_prompt:"):
        if key not in text:
            fail(f"agents/openai.yaml is missing {key[:-1]}")
    if f"${name}" not in text:
        fail("default_prompt does not mention the skill name")


def validate_behavioral_invariants(skill_text: str) -> int:
    required = {
        "adult default": "20–25 岁、明确成年的东方古典美人",
        "ChatGPT scope": "ChatGPT 文生图",
        "prompt-only boundary": "不调用图片生成工具",
        "automatic completion": "自动补全",
        "art direction routing": "art-direction.md",
        "beauty direction routing": "beauty-direction.md",
        "quality bar routing": "quality-bar.md",
        "body taxonomy routing": "body-silhouette.md",
        "director structure": "九层",
        "vertical default": "9:16",
        "safe clothing": "衣着完整",
        "non-sexual framing": "非色情化",
    }
    missing = [label for label, phrase in required.items() if phrase not in skill_text]
    if missing:
        fail(f"missing behavioral invariants: {', '.join(missing)}")
    return len(required)


def validate_noise() -> None:
    offenders: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.name in NOISE_NAMES or (path.is_file() and path.suffix in NOISE_SUFFIXES):
            offenders.append(str(path.relative_to(ROOT)))
    if offenders:
        fail(f"repository contains noise files: {', '.join(sorted(offenders))}")


def validate_default_ratio() -> None:
    runtime_files = [SKILL_MD, *sorted((ROOT / "references").glob("*.md"))]
    offenders: list[str] = []
    for path in runtime_files:
        text = path.read_text(encoding="utf-8")
        for phrase in OBSOLETE_DEFAULT_RATIO_PHRASES:
            if phrase in text:
                offenders.append(f"{path.relative_to(ROOT)}: {phrase}")
    if offenders:
        fail(f"obsolete default ratio remains: {', '.join(offenders)}")


def main() -> int:
    if not SKILL_MD.is_file():
        fail("SKILL.md is missing")
    skill_text = SKILL_MD.read_text(encoding="utf-8")
    if "[TODO:" in skill_text:
        fail("unfinished TODO placeholder remains in SKILL.md")

    name = validate_frontmatter(skill_text)
    validate_ui_metadata(name)
    invariant_count = validate_behavioral_invariants(skill_text)
    checked_links = validate_local_links()
    validate_default_ratio()
    validate_noise()

    print(f"PASS skill={name}")
    print(f"PASS local_links={checked_links}")
    print("PASS ui_metadata=agents/openai.yaml")
    print(f"PASS behavioral_invariants={invariant_count}")
    print("PASS default_ratio=9:16")
    print("PASS repository_noise=none")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(f"FAIL {error}", file=sys.stderr)
        raise SystemExit(1)
