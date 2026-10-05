#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

clawhub_slug_map = {
    "analytical-thinking": "analytical-thinking",
    "creative-thinking": "creative-thinking",
    "critical-thinking": "critical-thinking",
    "design-thinking": "design-thinking",
    "ethical-thinking": "ethical-thinking",
    "lateral-thinking": "lateral-thinking",
    "strategic-thinking": "strategic-thinking",
    "systems-thinking": "systems-thinking",
    "six-thinking-hats": "six-hats-thinking",
    "first-principles-thinking": "first-principles-reasoning",
    "five-whys": "five-whys",
    "swot-analysis": "swot-analysis",
    "pre-mortem": "pre-mortem",
    "tradeoff-analysis": "tradeoff-analysis",
    "prioritization": "prioritization",
    "fermi-estimation": "fermi-estimation",
    "thinking-method-selector": "thinking-method-selector",
}

SKILLS = [
]

OWNER_HANDLE = "ysskrishna"
REGISTRY_URL = "https://clawhub.ai"
RATE_LIMIT_RETRIES = 5

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

SyncStatus = Literal["new", "update", "synced"]


@dataclass(frozen=True)
class SyncState:
    folder: str
    slug: str
    status: SyncStatus
    local_version: str
    registry_version: str | None


def title_case(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def version(skill_dir: Path) -> str:
    text = (skill_dir / "SKILL.md").read_text()
    m = re.search(r"^\s*version:\s*[\"']?([^\"'\n]+)", text, re.M)
    if not m:
        raise SystemExit(f"no metadata.version in {skill_dir}/SKILL.md")
    return m.group(1).strip().strip('"')


def changelog(skill_dir: Path) -> str:
    return f"Release version: {version(skill_dir)}"


def clawhub_slug(folder: str) -> str:
    if folder in clawhub_slug_map:
        return clawhub_slug_map[folder]
    raise SystemExit(
        f"no clawhub slug for folder {folder!r}; add it to clawhub_slug_map"
    )


def target_folders() -> list[str]:
    if SKILLS:
        return list(SKILLS)
    folders: list[str] = []
    for path in sorted(SKILLS_DIR.iterdir()):
        if not path.is_dir() or not (path / "SKILL.md").is_file():
            continue
        if path.name not in clawhub_slug_map:
            continue
        folders.append(path.name)
    if not folders:
        raise SystemExit(
            f"no skills found under {SKILLS_DIR} (need SKILL.md and clawhub_slug_map entry)"
        )
    return folders


def registry_get(slug: str, owner: str | None) -> tuple[int, dict]:
    """GET one skill from the registry. Retries on HTTP 429 using the reset header.

    Slugs are scoped per owner, so `clawhub inspect <slug>` fails with
    AMBIGUOUS_SKILL_SLUG when another owner shares it. The registry accepts an
    `owner` query parameter, which the CLI does not expose.
    """
    url = f"{REGISTRY_URL}/api/v1/skills/{urllib.parse.quote(slug)}"
    if owner:
        url += "?" + urllib.parse.urlencode({"owner": owner})
    for _ in range(RATE_LIMIT_RETRIES):
        request = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.status, json.loads(response.read())
        except urllib.error.HTTPError as err:
            if err.code == 429:
                wait = int(err.headers.get("ratelimit-reset") or 10)
                time.sleep(wait + 1)
                continue
            body = err.read().decode(errors="replace")
            try:
                return err.code, json.loads(body)
            except json.JSONDecodeError:
                return err.code, {"message": body}
        except urllib.error.URLError as err:
            raise SystemExit(f"registry unreachable for {slug!r}: {err.reason}")
    raise SystemExit(f"registry rate limit did not clear for {slug!r}")


def inspect_registry_version(slug: str) -> str | None:
    """Return my published version, or None when I have not published this slug.

    Any other outcome (network error, rate limit that never clears, unexpected
    status) stops the script. A failed lookup must never read as "new".
    """
    status, data = registry_get(slug, OWNER_HANDLE)
    if status == 404:
        return None
    if status != 200:
        raise SystemExit(f"unexpected registry status {status} for {slug!r}: {data}")
    skill = data.get("skill")
    if not skill:
        return None
    latest = data.get("latestVersion") or {}
    registry = latest.get("version")
    if registry:
        return str(registry).strip()
    tagged = (skill.get("tags") or {}).get("latest")
    return str(tagged).strip() if tagged else None


def other_owners(slug: str) -> list[str]:
    """Other owners publishing the same slug. Informational: collisions do not block publishing."""
    status, data = registry_get(slug, None)
    if status == 200:
        handle = ((data.get("owner") or {}).get("handle")) or ""
        return [] if handle in ("", OWNER_HANDLE) else [handle]
    if data.get("code") == "AMBIGUOUS_SKILL_SLUG":
        handles = {m.get("ownerHandle") for m in data.get("matches", [])}
        return sorted(h for h in handles if h and h != OWNER_HANDLE)
    return []


def check_sync_state(folder: str) -> SyncState:
    slug = clawhub_slug(folder)
    path = SKILLS_DIR / folder
    if not path.is_dir():
        raise SystemExit(f"skill folder not found: {path}")
    local = version(path)
    registry = inspect_registry_version(slug)
    if registry is None:
        return SyncState(folder, slug, "new", local, None)
    if local == registry:
        return SyncState(folder, slug, "synced", local, registry)
    return SyncState(folder, slug, "update", local, registry)


def format_status_line(state: SyncState) -> str:
    if state.status == "synced":
        return f"{state.folder}  synced  ({state.local_version})"
    if state.status == "new":
        return f"{state.folder}  new  ({state.local_version})"
    return (
        f"{state.folder}  update  "
        f"local {state.local_version} → registry {state.registry_version}"
    )


def publish_cmd(folder: str) -> list[str]:
    slug = clawhub_slug(folder)
    path = SKILLS_DIR / folder
    ver = version(path)
    return [
        "clawhub",
        "publish",
        str(path),
        "--slug",
        slug,
        "--name",
        title_case(slug),
        "--version",
        ver,
        "--changelog",
        changelog(path),
        "--tags",
        "latest",
    ]


def cmd_plan() -> None:
    for folder in target_folders():
        state = check_sync_state(folder)
        line = format_status_line(state)
        others = other_owners(state.slug)
        if others:
            line += f"  (slug also used by: {', '.join(others)})"
        print(line)


def cmd_publish() -> None:
    published = 0
    for folder in target_folders():
        state = check_sync_state(folder)
        print(format_status_line(state))
        if state.status == "synced":
            continue
        subprocess.run(publish_cmd(folder), check=True)
        published += 1
        time.sleep(1)
    if published == 0:
        print("Nothing to publish.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish skills to ClawHub.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "plan",
        help="Show new / update / synced (SKILLS list, or all skills/ if empty)",
    )
    subparsers.add_parser(
        "publish",
        help="Publish new or updated (SKILLS list, or all skills/ if empty)",
    )
    args = parser.parse_args()
    if args.command == "plan":
        cmd_plan()
    elif args.command == "publish":
        cmd_publish()


if __name__ == "__main__":
    main()
