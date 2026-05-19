#!/usr/bin/env python3
import re
import shlex
import subprocess
import time
from pathlib import Path

clawhub_slug_map = {
    "analytical-thinking": "analytical-thinking",
    "creative-thinking": "creative-thinking",
    "critical-thinking": "critical-thinking",
    "design-thinking": "design-thinking",
    "ethical-thinking": "ethical-thinking",
    "lateral-thinking": "lateral-thinking",
    "strategic-thinking": "strategic-thinking",
    "systems-thinking": "systems-thinking",
    # "six-thinking-hats": "six-thinking-hats",
    # "first-principles-thinking": "first-principles-thinking",
}

SKILLS = [
    "lateral-thinking",
    "strategic-thinking",
    "systems-thinking",
]

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


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
    try:
        return clawhub_slug_map[folder]
    except KeyError:
        raise SystemExit(
            f"no clawhub slug for folder {folder!r}; add it to clawhub_slug_map"
        ) from None


def publish_cmd(folder: str) -> list[str]:
    slug = clawhub_slug(folder)
    path = SKILLS_DIR / folder
    if not path.is_dir():
        raise SystemExit(f"skill folder not found: {path}")
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


def main() -> None:
    for folder in SKILLS:
        cmd = publish_cmd(folder)
        # print(shlex.join(cmd))
        subprocess.run(cmd, check=True)
        time.sleep(1)


if __name__ == "__main__":
    main()
