#!/usr/bin/env python3
"""Repository checks that go beyond the Agent Skills spec.

Called by validate-skills.sh. Standard library only so CI needs no installs.
Errors fail the run. Warnings are printed and do not.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
EVALS_DIR = ROOT / "evals"

DESC_MIN, DESC_MAX = 200, 350
MAX_BODY_LINES = 120
MIN_EVAL_QUERIES_PER_SIDE = 8
UNIQUE_PREFIX_CHARS = 80
BANNED_PHRASES = [
    "obvious misspellings",
    "naming or directing",
    "typos is decisive",
    "decisive)",
]

errors: list[str] = []
warnings: list[str] = []


def err(skill: str, msg: str) -> None:
    errors.append(f"{skill}: {msg}")


def warn(skill: str, msg: str) -> None:
    warnings.append(f"{skill}: {msg}")


def frontmatter(text: str) -> dict[str, str]:
    """Minimal parser for the fields used here: name, description (folded or plain), version."""
    parts = text.split("---")
    if len(parts) < 3:
        return {}
    lines = parts[1].splitlines()
    out: dict[str, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m and m.group(1) in ("name", "description"):
            key, val = m.group(1), m.group(2).strip()
            if val in (">", ">-", "|", "|-"):
                chunk = []
                i += 1
                while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                    chunk.append(lines[i].strip())
                    i += 1
                out[key] = " ".join(c for c in chunk if c)
                continue
            out[key] = val.strip("\"'")
        m = re.match(r"^\s+version:\s*[\"']?([^\"'\n]+)", line)
        if m:
            out["version"] = m.group(1).strip()
        i += 1
    return out


def skill_dirs() -> list[Path]:
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


def check_skill(path: Path, info: dict) -> None:
    name = path.name
    text = (path / "SKILL.md").read_text()
    fm = frontmatter(text)
    desc = fm.get("description", "")
    info[name] = {"description": desc, "version": fm.get("version", "")}

    if not desc.startswith("Use "):
        err(name, 'description must start with "Use " (imperative when-to-use opener)')
    if not DESC_MIN <= len(desc) <= DESC_MAX:
        warn(name, f"description is {len(desc)} chars (target {DESC_MIN}-{DESC_MAX})")
    for phrase in BANNED_PHRASES:
        if phrase in desc:
            err(name, f'description contains banned meta phrase "{phrase}"')
    if not re.search(r"\b(skip|do not use)\b", desc, re.I):
        err(name, 'description needs a "Skip ..." clause that states when not to use the skill')

    lines = text.count("\n")
    if lines > MAX_BODY_LINES:
        warn(name, f"SKILL.md is {lines} lines (target <= {MAX_BODY_LINES}; move detail to references/)")

    if not (path / "references" / "example.md").is_file():
        err(name, "missing references/example.md (one worked example)")

    eval_file = EVALS_DIR / f"{name}.json"
    if not eval_file.is_file():
        err(name, f"missing evals/{name}.json")
    else:
        try:
            queries = json.loads(eval_file.read_text())
            pos = sum(1 for q in queries if q.get("should_trigger") is True)
            neg = sum(1 for q in queries if q.get("should_trigger") is False)
            bad = [q for q in queries if not isinstance(q.get("query"), str) or not q["query"].strip()]
            if bad:
                err(name, f"evals/{name}.json has entries without a query string")
            if pos < MIN_EVAL_QUERIES_PER_SIDE or neg < MIN_EVAL_QUERIES_PER_SIDE:
                err(name, f"evals/{name}.json has {pos} positive / {neg} negative queries (need >= {MIN_EVAL_QUERIES_PER_SIDE} each)")
        except (json.JSONDecodeError, AttributeError, TypeError) as e:
            err(name, f"evals/{name}.json is not a valid list of queries: {e}")


def check_unique_prefixes(info: dict) -> None:
    seen: dict[str, str] = {}
    for name, d in info.items():
        prefix = d["description"][:UNIQUE_PREFIX_CHARS].lower()
        if prefix in seen:
            err(name, f"first {UNIQUE_PREFIX_CHARS} description chars duplicate {seen[prefix]}")
        seen[prefix] = name


def slug_map() -> dict[str, str]:
    text = (ROOT / "scripts" / "publish_clawhub.py").read_text()
    block = re.search(r"clawhub_slug_map\s*=\s*\{(.*?)\}", text, re.S)
    return dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', block.group(1))) if block else {}


def check_sync(info: dict) -> None:
    names = set(info)
    readme = (ROOT / "README.md").read_text()
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    slugs = slug_map()
    plugins = {p["name"]: p for p in market.get("plugins", [])}

    for name in sorted(names):
        d = info[name]["description"]
        checks = [
            (f"skills/{name}/SKILL.md", "README skills table link"),
            (f"npx skills add ysskrishna/ai-agent-skills --skill {name}", "README skills.sh install line"),
            (f"gh skill install ysskrishna/ai-agent-skills {name}", "README gh skill install line"),
            (f"/plugin install {name}@ai-agent-skills", "README Claude Code install line"),
        ]
        for needle, label in checks:
            if needle not in readme:
                err(name, f"{label} missing from README.md")
        if name not in slugs:
            err(name, "missing from clawhub_slug_map in scripts/publish_clawhub.py")
        else:
            badge = f"https://clawhub.ai/ysskrishna/{slugs[name]}"
            if badge not in readme:
                err(name, f"README Registry badge link {badge} missing")
        entry = plugins.get(name)
        if entry is None:
            err(name, "missing from .claude-plugin/marketplace.json plugins")
        else:
            if entry.get("source") != f"./skills/{name}":
                err(name, f"marketplace source is {entry.get('source')!r}, expected './skills/{name}'")
            if entry.get("description") != d:
                err(name, "marketplace description differs from SKILL.md description")
        if name not in plugin.get("keywords", []):
            err(name, "missing from .claude-plugin/plugin.json keywords")

    for extra in sorted(set(plugins) - names):
        err(extra, "listed in marketplace.json but has no skills/ directory")
    for extra in sorted(set(slugs) - names):
        err(extra, "in clawhub_slug_map but has no skills/ directory")

    if plugin.get("version") != market.get("metadata", {}).get("version"):
        err("release", "plugin.json version differs from marketplace.json metadata.version")


def main() -> int:
    info: dict = {}
    for path in skill_dirs():
        if (path / "SKILL.md").is_file():
            check_skill(path, info)
    check_unique_prefixes(info)
    check_sync(info)

    for w in warnings:
        print(f"  warning: {w}")
    for e in errors:
        print(f"  error: {e}")
    print(f"Repository checks: {len(info)} skills, {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
