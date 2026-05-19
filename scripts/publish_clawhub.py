#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import time
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
}

SKILLS = [
]

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


def inspect_registry_version(slug: str) -> str | None:
    result = subprocess.run(
        ["clawhub", "inspect", slug, "--json"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    skill = data.get("skill")
    if not skill:
        return None
    latest = data.get("latestVersion") or {}
    registry = latest.get("version")
    if registry:
        return str(registry).strip()
    tags = skill.get("tags") or {}
    tagged = tags.get("latest")
    return str(tagged).strip() if tagged else None


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
        print(format_status_line(state))


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
