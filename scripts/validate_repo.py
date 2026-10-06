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
BUNDLE = "ai-agent-skills"
BUNDLE_SOURCE = "./"
# Manifests whose "version" must equal the repo release version.
VERSIONED_MANIFESTS = [
    "plugin.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".kimi-plugin/plugin.json",
    "gemini-extension.json",
    "package.json",
]
# Closed schemas: these CLIs reject unknown keys.
AGENT_PLUGINS_KEYS = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}
CURSOR_MARKETPLACE_ENTRY_KEYS = {"name", "source", "description", "minClientVersions"}
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


def check_router(info: dict) -> None:
    """The router must list every other skill in its table and its fallback outlines."""
    router = "thinking-method-selector"
    if router not in info:
        return
    text = (SKILLS_DIR / router / "SKILL.md").read_text()
    for name in sorted(set(info) - {router}):
        mentions = text.count(f"`{name}`") + text.count(f"**{name}:**")
        if mentions < 2:
            err(router, f"must list `{name}` in both the selection table and the fallback outlines")


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
    plugins = {p["name"]: p for p in market.get("plugins", []) if p.get("name") != BUNDLE}
    bundle = next((p for p in market.get("plugins", []) if p.get("name") == BUNDLE), None)
    if bundle is None:
        err(BUNDLE, "bundle plugin missing from .claude-plugin/marketplace.json plugins")
    elif bundle.get("source") != BUNDLE_SOURCE:
        err(BUNDLE, f"bundle source is {bundle.get('source')!r}, expected {BUNDLE_SOURCE!r}")

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


def load_json(rel: str):
    path = ROOT / rel
    if not path.is_file():
        err("manifests", f"{rel} is missing")
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        err("manifests", f"{rel} is not valid JSON: {e}")
        return None


def check_no_pipe_to_shell() -> None:
    """Hermes scans the whole repo on plugin install and blocks it on pipe-to-shell patterns."""
    pattern = re.compile(r"curl[^\n|]*\|\s*(?:ba|z)?sh\b")
    this = Path(__file__).resolve()
    files = [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "CHANGELOG.md", ROOT / "validate-skills.sh"]
    for folder in ("docs", "scripts", ".github", "skills"):
        files += [f for f in (ROOT / folder).rglob("*") if f.is_file() and f.suffix in {".md", ".sh", ".py", ".yml", ".yaml", ".json"}]
    for f in files:
        if f.resolve() == this or not f.is_file():
            continue
        if pattern.search(f.read_text(errors="ignore")):
            err("hermes", f"{f.relative_to(ROOT)} pipes curl into a shell. Hermes blocks plugin installs on that; download to a file, then run it")


def check_manifests() -> None:
    """Every per-CLI manifest must parse, agree on version, and follow its CLI's path and key rules."""
    docs = {rel: load_json(rel) for rel in VERSIONED_MANIFESTS}
    market = load_json(".claude-plugin/marketplace.json") or {}
    expected = (docs.get(".claude-plugin/plugin.json") or {}).get("version")
    versions = {rel: d.get("version") for rel, d in docs.items() if d}
    versions[".claude-plugin/marketplace.json metadata"] = market.get("metadata", {}).get("version")
    bundle = next((p for p in market.get("plugins", []) if p.get("name") == BUNDLE), {})
    versions[".claude-plugin/marketplace.json bundle"] = bundle.get("version")
    for where, v in versions.items():
        if v != expected:
            err("release", f"{where} version is {v!r}, expected {expected!r}")

    for rel, d in docs.items():
        if d and rel != "package.json" and d.get("name") != BUNDLE:
            err("manifests", f"{rel} name is {d.get('name')!r}, expected {BUNDLE!r}")

    root = docs.get("plugin.json") or {}
    unknown = set(root) - AGENT_PLUGINS_KEYS
    if unknown:
        err("manifests", f"plugin.json has keys outside the Agent Plugins 1.0 schema: {sorted(unknown)}")
    if root.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        err("manifests", "plugin.json $schema must be the Agent Plugins 1.0.0 schema URL")

    for rel in (".codex-plugin/plugin.json", ".cursor-plugin/plugin.json", ".kimi-plugin/plugin.json"):
        d = docs.get(rel) or {}
        skills = d.get("skills")
        if skills != "./skills/":
            err("manifests", f"{rel} skills is {skills!r}, expected './skills/'")

    cursor_author = set((docs.get(".cursor-plugin/plugin.json") or {}).get("author", {}))
    if not cursor_author <= {"name", "email"}:
        err("manifests", f".cursor-plugin/plugin.json author allows only name and email, found {sorted(cursor_author)}")

    gem = docs.get("gemini-extension.json") or {}
    if not re.fullmatch(r"[a-zA-Z0-9-]+", gem.get("name", "")):
        err("manifests", "gemini-extension.json name must match [a-zA-Z0-9-]+")
    if "contextFileName" in gem:
        err("manifests", "gemini-extension.json must not set contextFileName (skills load by description)")

    codex = load_json(".agents/plugins/marketplace.json") or {}
    entries = codex.get("plugins", [])
    if [e.get("name") for e in entries] != [BUNDLE]:
        err("manifests", ".agents/plugins/marketplace.json must list exactly the bundle plugin")
    for e in entries:
        src = e.get("source", {})
        if src.get("source") != "local" or src.get("path") != BUNDLE_SOURCE:
            err("manifests", ".agents/plugins/marketplace.json bundle source must be local with path './'")
        for field in ("installation", "authentication"):
            if field not in e.get("policy", {}):
                err("manifests", f".agents/plugins/marketplace.json policy.{field} is missing")
        if "category" not in e:
            err("manifests", ".agents/plugins/marketplace.json category is missing")

    cursor = load_json(".cursor-plugin/marketplace.json") or {}
    if "name" not in cursor or "plugins" not in cursor:
        err("manifests", ".cursor-plugin/marketplace.json needs name and plugins")
    for e in cursor.get("plugins", []):
        if e.get("name") != BUNDLE or e.get("source") != BUNDLE_SOURCE:
            err("manifests", ".cursor-plugin/marketplace.json must list the bundle with source './'")
        bad = set(e) - CURSOR_MARKETPLACE_ENTRY_KEYS
        if bad:
            err("manifests", f".cursor-plugin/marketplace.json entry has unsupported keys {sorted(bad)}")

    pkg = docs.get("package.json") or {}
    if pkg.get("main") != "index.js" or not (ROOT / "index.js").is_file():
        err("manifests", "package.json main must be index.js and the file must exist")


def main() -> int:
    info: dict = {}
    for path in skill_dirs():
        if (path / "SKILL.md").is_file():
            check_skill(path, info)
    check_unique_prefixes(info)
    check_router(info)
    check_sync(info)
    check_manifests()
    check_no_pipe_to_shell()

    for w in warnings:
        print(f"  warning: {w}")
    for e in errors:
        print(f"  error: {e}")
    print(f"Repository checks: {len(info)} skills, {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
