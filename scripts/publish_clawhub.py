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
PACKAGE_NAME = "@ysskrishna/ai-agent-skills"
PACKAGE_DISPLAY_NAME = "Thinking Methods"
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


@dataclass(frozen=True)
class PackageSyncState:
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


def repo_release_version() -> str:
    data = json.loads((ROOT / "package.json").read_text())
    ver = data.get("version")
    if not isinstance(ver, str) or not ver.strip():
        raise SystemExit("package.json version required")
    return ver.strip()


def changelog(skill_dir: Path) -> str:
    return f"Release version: {version(skill_dir)}"


def package_changelog(ver: str) -> str:
    return f"Release version: {ver}"


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


def registry_get(path: str, owner: str | None) -> tuple[int, dict | str]:
    url = f"{REGISTRY_URL}{path}"
    if owner:
        url += "?" + urllib.parse.urlencode({"owner": owner})
    for _ in range(RATE_LIMIT_RETRIES):
        request = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read()
                if not body:
                    return response.status, {}
                try:
                    return response.status, json.loads(body)
                except json.JSONDecodeError:
                    return response.status, body.decode(errors="replace")
        except urllib.error.HTTPError as err:
            if err.code == 429:
                wait = int(err.headers.get("ratelimit-reset") or 10)
                time.sleep(wait + 1)
                continue
            body = err.read().decode(errors="replace")
            try:
                return err.code, json.loads(body)
            except json.JSONDecodeError:
                return err.code, body
        except urllib.error.URLError as err:
            raise SystemExit(f"registry unreachable for {path!r}: {err.reason}")
    raise SystemExit(f"registry rate limit did not clear for {path!r}")


def inspect_registry_version(slug: str) -> str | None:
    """Return my published version, or None when I have not published this slug.

    Any other outcome (network error, rate limit that never clears, unexpected
    status) stops the script. A failed lookup must never read as "new".
    """
    path = f"/api/v1/skills/{urllib.parse.quote(slug)}"
    status, data = registry_get(path, OWNER_HANDLE)
    if status == 404:
        return None
    if status != 200:
        raise SystemExit(f"unexpected registry status {status} for {slug!r}: {data}")
    if not isinstance(data, dict):
        raise SystemExit(f"unexpected registry payload for {slug!r}: {data}")
    skill = data.get("skill")
    if not skill:
        return None
    latest = data.get("latestVersion") or {}
    registry = latest.get("version")
    if registry:
        return str(registry).strip()
    tagged = (skill.get("tags") or {}).get("latest")
    return str(tagged).strip() if tagged else None


def inspect_package_registry_version() -> str | None:
    path = f"/api/v1/packages/{urllib.parse.quote(PACKAGE_NAME, safe='')}"
    status, data = registry_get(path, OWNER_HANDLE)
    if status == 404:
        return None
    if status != 200:
        raise SystemExit(
            f"unexpected registry status {status} for package {PACKAGE_NAME!r}: {data}"
        )
    if not isinstance(data, dict):
        raise SystemExit(f"unexpected registry payload for package: {data}")
    package = data.get("package")
    if not package:
        return None
    latest = package.get("latestVersion")
    return str(latest).strip() if latest else None


def other_owners(slug: str) -> list[str]:
    """Other owners publishing the same slug. Informational: collisions do not block publishing."""
    path = f"/api/v1/skills/{urllib.parse.quote(slug)}"
    status, data = registry_get(path, None)
    if not isinstance(data, dict):
        return []
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


def check_package_sync_state() -> PackageSyncState:
    local = repo_release_version()
    openclaw = ROOT / "openclaw.plugin.json"
    if not openclaw.is_file():
        raise SystemExit("openclaw.plugin.json required for package publish")
    manifest_version = json.loads(openclaw.read_text()).get("version")
    if manifest_version != local:
        raise SystemExit(
            f"openclaw.plugin.json version {manifest_version!r} != package.json {local!r}"
        )
    registry = inspect_package_registry_version()
    if registry is None:
        return PackageSyncState("new", local, None)
    if local == registry:
        return PackageSyncState("synced", local, registry)
    return PackageSyncState("update", local, registry)


def format_status_line(state: SyncState) -> str:
    if state.status == "synced":
        return f"{state.folder}  synced  ({state.local_version})"
    if state.status == "new":
        return f"{state.folder}  new  ({state.local_version})"
    return (
        f"{state.folder}  update  "
        f"local {state.local_version} → registry {state.registry_version}"
    )


def format_package_status_line(state: PackageSyncState) -> str:
    label = PACKAGE_NAME
    if state.status == "synced":
        return f"{label}  synced  ({state.local_version})"
    if state.status == "new":
        return f"{label}  new  ({state.local_version})"
    return (
        f"{label}  update  "
        f"local {state.local_version} → registry {state.registry_version}"
    )


def publish_cmd(folder: str) -> list[str]:
    slug = clawhub_slug(folder)
    path = SKILLS_DIR / folder
    ver = version(path)
    return [
        "clawhub",
        "skill",
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


def package_publish_cmd(ver: str) -> list[str]:
    return [
        "clawhub",
        "package",
        "publish",
        str(ROOT),
        "--owner",
        OWNER_HANDLE,
        "--name",
        PACKAGE_NAME,
        "--display-name",
        PACKAGE_DISPLAY_NAME,
        "--version",
        ver,
        "--changelog",
        package_changelog(ver),
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


def cmd_package_plan() -> None:
    state = check_package_sync_state()
    print(format_package_status_line(state))


def cmd_package_publish() -> None:
    state = check_package_sync_state()
    print(format_package_status_line(state))
    if state.status == "synced":
        print("Nothing to publish.")
        return
    subprocess.run(package_publish_cmd(state.local_version), check=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish skills and OpenClaw bundle package to ClawHub.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "plan",
        help="Per-skill: show new / update / synced (SKILLS list, or all skills/ if empty)",
    )
    subparsers.add_parser(
        "publish",
        help="Per-skill: publish new or updated (SKILLS list, or all skills/ if empty)",
    )
    package = subparsers.add_parser("package", help="OpenClaw bundle-plugin package")
    package_sub = package.add_subparsers(dest="package_command", required=True)
    package_sub.add_parser("plan", help="Show new / update / synced for the bundle package")
    package_sub.add_parser("publish", help="Publish bundle when repo version differs")
    args = parser.parse_args()
    if args.command == "plan":
        cmd_plan()
    elif args.command == "publish":
        cmd_publish()
    elif args.command == "package":
        if args.package_command == "plan":
            cmd_package_plan()
        elif args.package_command == "publish":
            cmd_package_publish()


if __name__ == "__main__":
    main()
